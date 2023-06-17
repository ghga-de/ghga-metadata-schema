#!/usr/bin/env python
"""Script to generate XLSX spreadsheets for metadata entry"""
from contextlib import contextmanager
import glob
import os
from pathlib import Path
from sys import stderr
import sys
from tempfile import TemporaryDirectory
from typing import Generator, Optional
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.styles import Alignment, PatternFill, Font
from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl.utils import get_column_letter
from pydantic import BaseModel
import yaml
from script_utils.cli import echo_failure, echo_success, run

HERE = Path(__file__).parent.resolve()
SCHEMA_PATH = HERE.parent / "src" / "schema" / "submission.yaml"
CONF_PATH = HERE.parent / "spreadsheet_conf.yaml"
XLSX_DIR = HERE.parent / "spreadsheets"


class WorksheetConfig(BaseModel):
    """A worksheet configuration"""

    class_name: str
    prefix: str = ""
    header_color: Optional[str]
    content_color: Optional[str]


class WorkbookConfig(BaseModel):
    """A workbook configuration"""

    file_name: str
    worksheets: list[WorksheetConfig]


class Config(BaseModel):
    """A XLSX generator config"""

    slot_order: list[str]
    workbooks: list[WorkbookConfig]


def _get_ghga_schema_version(schema: SchemaView) -> str:
    schema_def = [
        sdef
        for sdef in schema.all_schema()
        if sdef.name == "GHGA-Submission-Metadata-Schema"
    ]
    if len(schema_def) != 1 or schema_def[0].version is None:
        raise RuntimeError("Unable to identify GHGA Model version.")
    return schema_def[0].version


THIN_BORDER = Border(
    left=Side(border_style=BORDER_THIN, color="00000000"),
    right=Side(border_style=BORDER_THIN, color="00000000"),
    top=Side(border_style=BORDER_THIN, color="00000000"),
    bottom=Side(border_style=BORDER_THIN, color="00000000"),
)
THIN_BORDER_GRAY = Border(
    left=Side(border_style=BORDER_THIN, color="808080"),
    right=Side(border_style=BORDER_THIN, color="808080"),
    top=Side(border_style=BORDER_THIN, color="808080"),
    bottom=Side(border_style=BORDER_THIN, color="808080"),
)
ALIGN_HEADER = Alignment(wrapText=True, horizontal="center", vertical="top")


class ColumnMeta:
    @property
    def type_help(self) -> str:
        """The type help text"""
        return "type: " + (self.type_name if self.type_name else "string")

    @property
    def mv_help(self) -> str:
        """The multiple values help text"""
        return "multiple values" if self.slot_def.multivalued else "single value"

    @property
    def restriction_help(self) -> str:
        """The restriction help text"""
        if self.enum_name:
            return "controlled vocabulary"
        elif self.cls_name:
            id_slot = self.schema.get_identifier_slot(self.cls_name)
            if id_slot:
                id_slot_name = id_slot.name
                try:
                    target_prefix = self.prefix_map[self.cls_name]
                except KeyError:
                    print(
                        f"Class '{self.cls_name}' is referenced, but not included in the workbook!",
                        file=stderr,
                    )
                    sys.exit(2)
                return f"restriction: value from {self.cls_name}.{target_prefix}{id_slot_name}"
        return "unrestricted"

    @property
    def required_help(self) -> str:
        """The required / recommended / optional help text"""
        if self.slot_def.required:
            return "required"
        elif self.slot_def.recommended:
            return "recommended"
        return "optional"

    @property
    def name(self) -> str:
        """The name of the column"""
        return self.slot_def.name

    @property
    def description(self) -> str:
        """The description text"""
        return self.slot_def.description if self.slot_def.description else ""

    def __init__(
        self,
        schema: SchemaView,
        slot_def: SlotDefinition,
        prefix_map: dict[str, str],
    ):
        """Creates a new ColumnMeta object"""
        self.slot_def = slot_def
        self.schema = schema
        self.prefix_map = prefix_map
        self.range = slot_def.range if slot_def.range else "string"
        self.cls_name = str(range) if range in schema.all_classes() else None
        self.enum_name = str(range) if range in schema.all_enums() else None
        self.type_name = str(range) if range in schema.all_types() else None


def _make_value_cell(ws, fill_content):
    """Creates a new cell for the value area of the worksheet"""
    value_cell = Cell(ws)
    if fill_content:
        value_cell.fill = fill_content
    value_cell.border = THIN_BORDER_GRAY
    return value_cell


def _build_prefix_map(wb_config: WorkbookConfig) -> dict[str, str]:
    """Builds a dictionary mapping every class to the configured column header prefix"""
    return {
        ws_config.class_name: ws_config.prefix for ws_config in wb_config.worksheets
    }


def _get_ordered_slots(
    schema: SchemaView,
    slot_order: list[str],
    cls_name: str,
    prefix_map: dict[str, str],
) -> list[SlotDefinition]:
    """Given a class, generates a list of slots that must be rendered. Slots
    that are listed in the slot_order config parameter are at the top of the
    list in their respective order. Slots that are referencing other classes
    which are not part of this workbook are omitted."""
    slots = schema.class_induced_slots(cls_name)
    slot_names = {slot.name: idx for idx, slot in enumerate(slots)}
    ordered = [
        slots[slot_names[slot_name]]
        for slot_name in slot_order
        if slot_name in slot_names
    ]
    unordered = [slot for slot in slots if slot.name not in slot_order]
    all_slots = ordered + unordered
    # We ignore slots which have a class range when the target class is not included in this workbook.
    ignored_slots = [
        slot
        for slot in all_slots
        if slot.range in schema.all_classes()
        and slot.range not in prefix_map
        and schema.get_identifier_slot(slot.range)
    ]
    # If one of those is mandatory, we raise an error
    for ignored_slot in ignored_slots:
        if ignored_slot.required:
            raise RuntimeError(
                f"Slot '{cls_name}.{ignored_slot.name}' is mandatory, but target class is not included in the workbook!"
            )
    slots = [slot for slot in all_slots if slot not in ignored_slots]
    return slots


def create_xlsx_files(config_path: Path, out_dir: Path):
    """Creates the XLSX workbooks as configured in the provided configuration
    and writes them to the specified output path"""
    with open(config_path, "r", encoding="utf8") as config_file:
        config = Config.parse_obj(yaml.safe_load(config_file))

    # Read schema
    schema = SchemaView(str(SCHEMA_PATH))

    # Create the workbooks
    for wb_config in config.workbooks:
        print(wb_config.file_name, end="", flush=True)
        # Create a new workbook
        wb = Workbook()
        # Remove the default worksheet
        wb.remove(wb.worksheets[0])
        # Get all prefixes per class
        prefix_map = _build_prefix_map(wb_config=wb_config)
        # Add worksheets as specified in config
        for ws_config in wb_config.worksheets:
            ws = wb.create_sheet(ws_config.class_name)
            col_metas = [
                ColumnMeta(schema, slot_def, prefix_map)
                for slot_def in _get_ordered_slots(
                    schema=schema,
                    slot_order=config.slot_order,
                    cls_name=ws_config.class_name,
                    prefix_map=prefix_map,
                )
            ]

            # Generate the header rows
            rows = []
            rows.append([Cell(ws, value=col_meta.name) for col_meta in col_metas])
            rows.append(
                [Cell(ws, value=col_meta.description) for col_meta in col_metas]
            )
            rows.append([Cell(ws, value=col_meta.type_help) for col_meta in col_metas])
            rows.append([Cell(ws, value=col_meta.mv_help) for col_meta in col_metas])
            rows.append(
                [Cell(ws, value=col_meta.restriction_help) for col_meta in col_metas]
            )
            rows.append(
                [Cell(ws, value=col_meta.required_help) for col_meta in col_metas]
            )

            # Format the header rows
            font_bold = Font(bold=True)
            fill_header = (
                PatternFill("solid", fgColor=ws_config.header_color)
                if ws_config.header_color
                else None
            )
            for cell in rows[0]:
                cell.font = font_bold
            for row in rows:
                for cell in row:
                    cell.alignment = ALIGN_HEADER
                    if fill_header:
                        cell.fill = fill_header
                    cell.border = THIN_BORDER

            # Format the sheet tab color
            if ws_config.header_color:
                ws.sheet_properties.tabColor = ws_config.header_color

            # Color the value fields
            fill_content = (
                PatternFill("solid", fgColor=ws_config.content_color)
                if ws_config.content_color
                else None
            )

            for _ in range(1000):
                rows.append(
                    [_make_value_cell(ws, fill_content) for _ in range(len(col_metas))]
                )

            for row in rows:
                ws.append(row)

            # Format column width
            for column in range(1, ws.max_column + 1):
                ws.column_dimensions[get_column_letter(column)].width = 35

        # Encode metadata model version in the workbook
        ws = wb.create_sheet("__properties")
        ws.sheet_state = "hidden"
        ws.cell(row=1, column=1, value=_get_ghga_schema_version(schema))

        # Save to file name specified in config
        wb.save(out_dir / wb_config.file_name)
        print(" - done.", flush=True)


class ContentDifference(RuntimeError):
    """Raised when a content difference was detected"""


@contextmanager
def working_directory(working_dir: Path) -> Generator[None, None, None]:
    """Temporarily changes the working directory to the specified directory"""
    cwd = Path.cwd()
    try:
        os.chdir(working_dir)
        yield
    finally:
        os.chdir(cwd)


def compare_xls(expected: Workbook, observed: Workbook):
    """Compares two workbooks and raises a ContentDifference error if
    differences are detected."""
    if expected.sheetnames != observed.sheetnames:
        raise ContentDifference(
            f"Sheets differ. expected={expected.sheetnames}. observed={observed.sheetnames}"
        )

    for sheet in expected.sheetnames:
        for row_idx, (row_a, row_b) in enumerate(
            zip(expected[sheet].iter_rows(), observed[sheet].iter_rows()), 1
        ):
            for col_idx, (cell_a, cell_b) in enumerate(zip(row_a, row_b), 1):
                if cell_a.value != cell_b.value:
                    raise ContentDifference(
                        f"Cell values differ in sheet {sheet}, row {row_idx}, col {col_idx}: expected={cell_a.value}, observed={cell_b.value}"
                    )
                for attr in ["alignment", "font", "border", "fill"]:
                    if getattr(cell_a, attr).__dict__ != getattr(cell_b, attr).__dict__:
                        raise ContentDifference(
                            f"Cell {attr} differs in sheet {sheet}, row {row_idx}, col {col_idx}: expected={getattr(cell_a,attr).__dict__}, observed={getattr(cell_b, attr).__dict__}"
                        )


def compare_folders(expected: Path, observed: Path):
    """Function to check equality of contents of two folders"""

    with working_directory(expected):
        expected_glob = glob.glob("*")

    with working_directory(observed):
        observed_glob = glob.glob("*")

    if sorted(expected_glob) != sorted(observed_glob):
        raise ContentDifference(
            f"Different directory contents. expected={expected_glob}. observed={observed_glob}"
        )

    for fname in expected_glob:
        expected_wb = load_workbook(expected.joinpath(fname))
        observed_wb = load_workbook(observed.joinpath(fname))
        try:
            compare_xls(expected=expected_wb, observed=observed_wb)
        except ContentDifference as err:
            # pylint: disable=raise-missing-from
            raise ContentDifference(f"{fname}: {err}")


def main(check: bool = False):
    """The main routine."""
    if check:
        with TemporaryDirectory() as tmpdirname:
            tmp_docs_dir = Path(tmpdirname)

            create_xlsx_files(config_path=CONF_PATH, out_dir=tmp_docs_dir)

            try:
                compare_folders(XLSX_DIR, tmp_docs_dir)
                echo_success("Documents are up-to-date")
            except ContentDifference as err:
                echo_failure("Documents are not up-to-date")
                echo_failure(str(err))
                sys.exit(1)
    else:
        create_xlsx_files(config_path=CONF_PATH, out_dir=XLSX_DIR)


if __name__ == "__main__":
    run(main)

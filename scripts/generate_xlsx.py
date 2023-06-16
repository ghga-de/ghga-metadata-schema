#!/usr/bin/env python
"""Script to generate XLSX spreadsheets for metadata entry"""
from contextlib import contextmanager
from filecmp import dircmp
import glob
import os
from pathlib import Path
from sys import argv, stderr
from tempfile import TemporaryDirectory
from typing import Generator, Optional
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model.meta import SlotDefinition, SchemaDefinition
from openpyxl import Workbook, load_workbook
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
    class_name: str
    prefix: str = ""
    header_color: Optional[str]
    content_color: Optional[str]


class WorkbookConfig(BaseModel):
    file_name: str
    worksheets: list[WorksheetConfig]


class Config(BaseModel):
    slot_order: list[str]
    workbooks: list[WorkbookConfig]


def _get_ghga_schema_version(schema: SchemaView) -> str:
    schema_def = [
        sdef
        for sdef in schema.all_schema()
        if sdef.name == "GHGA-Submission-Metadata-Schema"
    ]
    if len(schema_def) != 1:
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


def create_xlsx_files(config_path: Path, out_dir: Path):
    with open(config_path, "r", encoding="utf8") as config_file:
        config = Config.parse_obj(yaml.safe_load(config_file))

    # Read schema
    schema = SchemaView(str(SCHEMA_PATH))

    def _build_prefix_map(wb_config: WorkbookConfig) -> dict[str, str]:
        return {
            ws_config.class_name: ws_config.prefix for ws_config in wb_config.worksheets
        }

    def _generate_type_help(
        slot_def: SlotDefinition, prefix_map: dict[str, str]
    ) -> tuple[str, str, str]:
        """Generates a type help text given a slot definition"""
        range = slot_def.range if slot_def.range else "string"
        cls_name = range if range in schema.all_classes() else None
        enum_name = range if range in schema.all_enums() else None
        type_name = range if range in schema.all_types() else None

        help = []

        # Type help
        type_help = "type: " + (type_name if type_name else "string")

        # Multivalue help
        mv_help = "multiple values" if slot_def.multivalued else "single value"

        # Restriction help
        if enum_name:
            restr_help = "controlled vocabulary"
        elif cls_name and schema.get_identifier_slot(cls_name):
            id_slot = schema.get_identifier_slot(cls_name).name
            try:
                target_prefix = prefix_map[cls_name]
            except KeyError:
                print(
                    f"Class '{cls_name}' is referenced, but not included in the workbook!",
                    file=stderr,
                )
                exit(2)
            restr_help = f"restriction: value from {cls_name}.{target_prefix}{id_slot}"
        else:
            restr_help = "unrestricted"

        return type_help, mv_help, restr_help

    def _get_ordered_slots(
        cls_name: str, prefix_map: dict[str, str]
    ) -> list[SlotDefinition]:
        """Given a class, generates a list of slots that must be rendered. Slots
        that are listed in the slot_order config parameter are at the top of the
        list in their respective order. Slots that are referencing other classes
        which are not part of this workbook are omitted."""
        slots = schema.class_induced_slots(cls_name)
        slot_names = {slot.name: idx for idx, slot in enumerate(slots)}
        ordered = [
            slots[slot_names[slot_name]]
            for slot_name in config.slot_order
            if slot_name in slot_names
        ]
        unordered = [slot for slot in slots if slot.name not in config.slot_order]
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
            content_fill = PatternFill("solid", ws_config.content_color)
            header_cells = []
            slots = _get_ordered_slots(
                cls_name=ws_config.class_name, prefix_map=prefix_map
            )
            for column, slot_def in enumerate(slots, 1):
                # Header
                name_cell = ws.cell(
                    row=1, column=column, value=ws_config.prefix + slot_def.name
                )
                name_cell.alignment = Alignment(horizontal="center")
                name_cell.font = Font(bold=True)
                # Description
                desc = slot_def.description if slot_def.description else ""
                desc_cell = ws.cell(row=2, column=column, value=desc)
                desc_cell.alignment = Alignment(
                    wrapText=True, horizontal="center", vertical="top"
                )
                # Help content
                type_help, mv_help, restr_help = _generate_type_help(
                    slot_def=slot_def, prefix_map=prefix_map
                )
                # Type Help
                type_help_cell = ws.cell(row=3, column=column, value=type_help)
                type_help_cell.alignment = Alignment(wrapText=True, horizontal="center")
                # Multi-valued help
                mv_help_cell = ws.cell(row=4, column=column, value=mv_help)
                mv_help_cell.alignment = Alignment(wrapText=True, horizontal="center")
                # Restriction help
                ws.cell(row=5, column=column, value=restr_help).alignment = Alignment(
                    wrapText=True, horizontal="center"
                )

                ws.column_dimensions[get_column_letter(column)].width = 35

            # Color the header and sheet tab
            if ws_config.header_color:
                header_fill = PatternFill("solid", ws_config.header_color)
                ws.sheet_properties.tabColor = ws_config.header_color
                for row in range(1, 6):
                    for column in range(1, len(slots) + 1):
                        cell = ws.cell(row=row, column=column)
                        cell.fill = header_fill
                        cell.border = THIN_BORDER

            # Color the value fields
            if ws_config.content_color:
                for row in range(ws.max_row + 1, ws.max_row + 1001):
                    for column in range(1, len(slots) + 1):
                        cell = ws.cell(row=row, column=column)
                        cell.fill = content_fill
                        cell.border = THIN_BORDER_GRAY

            ws.cell(row=3, column=2).border = THIN_BORDER

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
def working_directory(dir: Path) -> Generator[None, None, None]:
    cwd = Path.cwd()
    try:
        os.chdir(dir)
        yield
    finally:
        os.chdir(cwd)


def compare_xls(expected: Workbook, observed: Workbook):
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
    else:
        create_xlsx_files(config_path=CONF_PATH, out_dir=XLSX_DIR)


if __name__ == "__main__":
    run(main)

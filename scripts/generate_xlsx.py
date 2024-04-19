#!/usr/bin/env python
# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import glob
import os
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Final, Generator, Mapping, Optional

import yaml
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.styles import Font, PatternFill
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import BORDER_THIN, Border, Side
from openpyxl.utils import get_column_letter
from pydantic import BaseModel
from schemapack import load_schemapack
from schemapack.spec.schemapack import Relation, SchemaPack
from script_utils.cli import echo_failure, echo_success, run
from typer import Option

################################################################################

HERE: Final[Path] = Path(__file__).parent.resolve()
SCHEMAPACK_PATH: Final[Path] = (
    HERE.parent / "src" / "schema" / "submission.schemapack.yaml"
)
CONFIG_PATH: Final[Path] = HERE.parent / "spreadsheet_conf.yaml"
XLSX_DIR: Final[Path] = HERE.parent / "spreadsheets"

################################################################################

THIN_BORDER: Final[Border] = Border(
    left=Side(border_style=BORDER_THIN, color="00000000"),
    right=Side(border_style=BORDER_THIN, color="00000000"),
    top=Side(border_style=BORDER_THIN, color="00000000"),
    bottom=Side(border_style=BORDER_THIN, color="00000000"),
)
THIN_BORDER_GRAY: Final[Border] = Border(
    left=Side(border_style=BORDER_THIN, color="808080"),
    right=Side(border_style=BORDER_THIN, color="808080"),
    top=Side(border_style=BORDER_THIN, color="808080"),
    bottom=Side(border_style=BORDER_THIN, color="808080"),
)
ALIGN_HEADER: Final[Alignment] = Alignment(
    wrapText=True, horizontal="center", vertical="top"
)


class WorksheetStyle(BaseModel):
    """Style for a worksheet"""

    header_color: Optional[str] = None
    content_color: Optional[str] = None


class Config(BaseModel):
    """A XLSX generator config"""

    output_filename: str
    styles: Optional[dict[str, WorksheetStyle]] = {}


class GHGASchemaError(RuntimeError):
    """Raised when a schema violates GHGA schema rules."""



def _validate_relation(relation: Relation) -> None:
    if relation.multiple.target:
        raise GHGASchemaError(
            "One-to-Many and Many-to-Many relations are not supported in GHGA schemas."
            " One-to-Many relations must be inverted to Many-to-One relations."
        )


@dataclass
class ClassReference:
    class_name: str
    id_property_name: str


@dataclass
class Column:
"""Model defining a column"""
    name: str
    description: Optional[str]
    type: str
    multivalued: bool
    class_reference: Optional[ClassReference]
    enum: bool
    required: bool

    @property
    def restriction(self) -> str:
        if self.enum and self.class_reference:
            raise ValueError("Column cannot be both an enum and a reference")
        if self.enum:
            return "controlled vocabulary"
        if self.class_reference:
            return f"restriction: value from {self.class_reference.class_name}.{self.class_reference.id_property_name}"
        else:
            return "unrestricted"


@dataclass
class Sheet:
    columns: list[Column]
    header_color: Optional[str] = None
    content_color: Optional[str] = None


def _get_element_type_from_schema(schema: dict) -> str:
    """Get the type of the elements in an array from a JSON schema."""
    element_type = schema.get("type", "object")
    if element_type == "array":
        element_type = schema.get("items", {}).get("type", "object")
    return element_type


def parse_schema(schemapack: SchemaPack, config: Config) -> Mapping[str, Sheet]:
    """Parses a SchemaPack into a set of sheets for an XLSX workbook."""
    sheets: dict[str, Sheet] = {}

    # Iterate over each class in the SchemaPack
    for class_name, class_ in schemapack.classes.items():
        columns: list[Column] = []

        # ID column
        columns.append(
            Column(
                name=class_.id.propertyName,
                description=class_.id.description,
                type="string",
                enum=False,
                multivalued=False,
                class_reference=None,
                required=True,
            )
        )

        # Relations
        for relation_name, relation in class_.relations.items():
            columns.append(
                Column(
                    name=relation_name,
                    description=relation.description,
                    type="string",
                    enum=False,
                    multivalued=False,
                    class_reference=ClassReference(
                        class_name=relation.targetClass,
                        id_property_name=schemapack.classes[
                            relation.targetClass
                        ].id.propertyName,
                    ),
                    required=relation.mandatory.origin,
                )
            )

        # Content
        content_schema = class_.content.json_schema_dict
        for property_name in content_schema.get("properties", {}):
            columns.append(
                Column(
                    name=property_name,
                    description=content_schema["properties"][property_name].get(
                        "description", ""
                    ),
                    type=_get_element_type_from_schema(
                        content_schema["properties"][property_name]
                    ),
                    multivalued=content_schema["properties"][property_name]["type"]
                    == "array",
                    class_reference=None,
                    enum="enum" in content_schema["properties"][property_name],
                    required=property_name in content_schema.get("required", []),
                )
            )

        style = config.styles.get(class_name, WorksheetStyle())
        sheets[class_name] = Sheet(
            columns=columns,
            header_color=style.header_color,
            content_color=style.content_color,
        )
    return sheets


def _make_value_cell(ws, fill_content):
    """Creates a new cell for the value area of the worksheet"""
    value_cell = Cell(ws)
    if fill_content:
        value_cell.fill = fill_content
    value_cell.border = THIN_BORDER_GRAY
    return value_cell


def generate_workbook(sheets: Mapping[str, Sheet]) -> Workbook:
    """Generates a workbook from a dictionary of sheets."""
    # Create a new workbook
    workbook = Workbook()
    # Remove the default sheet
    workbook.remove(workbook.worksheets[0])

    for sheet_name, sheet in sheets.items():
        # Create a new sheet for the class
        wb_sheet = workbook.create_sheet(title=sheet_name)

        cols = sheet.columns
        rows = []
        rows.append([Cell(wb_sheet, value=col.name) for col in cols])
        rows.append([Cell(wb_sheet, value=col.description) for col in cols])
        rows.append([Cell(wb_sheet, value=col.type) for col in cols])
        rows.append(
            [
                Cell(
                    wb_sheet,
                    value="multiple values" if col.multivalued else "single value",
                )
                for col in cols
            ]
        )
        rows.append([Cell(wb_sheet, value=col.restriction) for col in cols])
        rows.append(
            [
                Cell(wb_sheet, value="required" if col.required else "optional")
                for col in cols
            ]
        )

        # FORMATTING

        font_bold = Font(bold=True)

        fill_header = (
            PatternFill("solid", fgColor=sheet.header_color)
            if sheet.header_color
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

        if sheet.header_color:
            wb_sheet.sheet_properties.tabColor = sheet.header_color

        fill_content = (
            PatternFill("solid", fgColor=sheet.content_color)
            if sheet.content_color
            else None
        )

        for _ in range(1000):
            rows.append(
                [
                    _make_value_cell(wb_sheet, fill_content)
                    for _ in range(len(sheet.columns))
                ]
            )

        for row in rows:
            wb_sheet.append(row)

        for column in range(1, wb_sheet.max_column + 1):
            wb_sheet.column_dimensions[get_column_letter(column)].width = 35

    # Save the workbook to the specified output path
    return workbook


def load_config(config_path: Path) -> Config:
    """Loads a config from a file."""
    with config_path.open("r") as file:
        return Config.model_validate(yaml.safe_load(file))


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


def compare_folders(expected: Path, observed: Path):
    """Function to check equality of contents of two folders with xlsx files."""

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
            raise ContentDifference(f"{fname}: {err}")


def _add_transpiler_metadata(workbook: Workbook, sheets: Mapping[str, Sheet]) -> None:
    """Adds metadata to the workbook"""
    ws = workbook.create_sheet("__transpiler_protocol")
    ws.sheet_state = "hidden"
    ws.cell(row=1, column=1, value="1.0.0")

    # Add metadata about the sheets
    ws = workbook.create_sheet("__sheet_meta")
    ws.sheet_state = "hidden"
    ws.append(
        [
            Cell(ws, value="sheet"),
            Cell(ws, value="n_cols"),
            Cell(ws, value="header_row"),
            Cell(ws, value="data_start"),
        ]
    )
    for sheet_name, sheet in sheets.items():
        ws.append(
            [
                Cell(ws, value=sheet_name),
                Cell(ws, value=len(sheet.columns)),
                Cell(ws, value=1),
                Cell(ws, value=7),
            ]
        )

    # Add metadata about the columns
    ws = workbook.create_sheet("__column_meta")
    ws.sheet_state = "hidden"
    ws.append(
        [
            Cell(ws, value="sheet"),
            Cell(ws, value="column"),
            Cell(ws, value="multivalued"),
            Cell(ws, value="type"),
            Cell(ws, value="ref_class"),
            Cell(ws, value="ref_class_id_property"),
            Cell(ws, value="enum"),
            Cell(ws, value="required"),
        ]
    )
    for sheet_name, sheet in sheets.items():
        for column in sheet.columns:
            ws.append(
                [
                    Cell(ws, value=sheet_name),
                    Cell(ws, value=column.name),
                    Cell(ws, value=column.multivalued),
                    Cell(ws, value=column.type),
                    Cell(
                        ws,
                        value=column.class_reference.class_name
                        if column.class_reference
                        else None,
                    ),
                    Cell(
                        ws,
                        value=column.class_reference.id_property_name
                        if column.class_reference
                        else None,
                    ),
                    Cell(ws, value=column.enum),
                    Cell(ws, value=column.required),
                ]
            )


def create_xlsx_files(xlsx_dir: Path = XLSX_DIR) -> None:
    schema = load_schemapack(Path(SCHEMAPACK_PATH))
    config = load_config(Path(CONFIG_PATH))
    sheets = parse_schema(schema, config)
    workbook = generate_workbook(sheets)
    _add_transpiler_metadata(workbook, sheets)
    workbook.save(xlsx_dir / config.output_filename)


def main(
    check: bool = Option(
        False,
        help="Run read-only check that verifies that the documents are up-to-date.",
    ),
):
    """Generate a submission XLSX file from the schema pack."""
    if check:
        with TemporaryDirectory() as tmpdirname:
            tmp_docs_dir = Path(tmpdirname)

            create_xlsx_files(xlsx_dir=tmp_docs_dir)

            try:
                compare_folders(XLSX_DIR, tmp_docs_dir)
                echo_success("Documents are up-to-date")
            except ContentDifference as err:
                echo_failure("Documents are not up-to-date")
                echo_failure(str(err))
                sys.exit(1)
    else:
        create_xlsx_files()


if __name__ == "__main__":
    run(main)

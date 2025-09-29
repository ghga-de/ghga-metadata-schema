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
from typing import Final, Generator, Mapping

import yaml
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.styles import Font, PatternFill
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import BORDER_THIN, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet
from pydantic import BaseModel
from schemapack import load_schemapack
from schemapack.spec.schemapack import ClassDefinition, MultipleRelationSpec, SchemaPack
from script_utils.cli import echo_failure, echo_success, run
from typer import Option

HERE: Final[Path] = Path(__file__).parent.resolve()
SCHEMAPACK_PATH: Final[Path] = (
    HERE.parent / "build" / "ghga_metadata_schema.resolved.schemapack.yaml"
)
CONFIG_PATH: Final[Path] = HERE.parent / "spreadsheet_conf.yaml"
XLSX_DIR: Final[Path] = HERE.parent / "spreadsheets"


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
    """Style configuration for a worksheet"""

    header_color: str | None = None
    content_color: str | None = None


class Config(BaseModel):
    """A XLSX generator config"""

    output_filename: str
    styles: dict[str, WorksheetStyle] = {}


class GHGASchemaError(RuntimeError):
    """Raised when a schema violates GHGA schema rules."""


def _validate_relation(multiplicity: MultipleRelationSpec) -> None:
    """Raises a schema error if the relation violates GHGA schema rules."""
    if multiplicity.target:
        raise GHGASchemaError(
            "One-to-Many and Many-to-Many relations are not supported in GHGA schemas."
            " One-to-Many relations must be inverted to Many-to-One relations."
        )


@dataclass
class IdAnnotatedClass:
    """
    Describes a class name and its associated ID property name.

    Attributes:
        class_name (str): The name of the class.
        id_property_name (str): The name of the property that serves as the unique identifier for the class.
    """

    class_name: str
    id_property_name: str


@dataclass
class Column:
    """Represents metadata for a column in a sheet.

    Attributes:
        name: The name of the column.
        description: An optional description explaining the column's meaning.
        type: The data type of the column's values (e.g., "string", "int").
        multivalued: Whether the column can contain multiple values per cell.
        class_reference: A reference to another class if the column links to an external entity.
        enum: Whether the column is restricted to values from a controlled vocabulary.
        required: Whether the column must have a value in every row.

    """

    name: str
    description: str | None
    type: str
    multivalued: bool
    class_reference: IdAnnotatedClass | None
    enum: bool
    required: bool

    @property
    def restriction(self) -> str:
        if self.enum and self.class_reference:
            raise GHGASchemaError("Column cannot be both an enum and a reference")
        # If the column is an enum, its values are restricted to a predefined set (controlled vocabulary).
        if self.enum:
            return "restriction: value from controlled vocabulary (see schema for allowed values)"
        if self.class_reference:
            return f"restriction: value from {self.class_reference.class_name}.{self.class_reference.id_property_name}"
        return "unrestricted"


@dataclass
class WorksheetMetadata:
    """
    Metadata defining the structure and styling of a sheet.

    Attributes:
        columns (list[Column]): The columns present in the worksheet.
        id_property_name (str): The name of the property that serves as the unique identifier for the worksheet's class.
        header_color (None | str): The color used for the header row, if any.
        content_color (None | str): The color used for the content rows, if any.
    """
    class_name: str
    columns: list[Column]
    id_property_name: str
    header_color: None | str
    content_color: None | str


def _get_element_type_from_schema(schema: dict) -> str:
    """Get the type of the elements in an array from a JSON schema."""
    element_type = schema.get("type", "object")
    if element_type == "array":
        element_type = schema.get("items", {}).get("type", "object")
    return element_type

class ClassColumnFactory:
    """Factory for creating columns from class definitions"""

    @staticmethod
    def set_id_column(class_definition: ClassDefinition) -> Column:
        """Creates a column representing the ID property of a class definition."""
        return Column(
            name=class_definition.id.propertyName,
            description=class_definition.id.description,
            type="string",
            enum=False,
            multivalued=False,
            class_reference=None,
            required=True,
        )

    @staticmethod
    def set_content_columns(class_definition: ClassDefinition) -> list[Column]:
        """Extracts columns from the content schema of a class definition. Returns a list of
        columns representing the properties defined in the class's content schema."""

        properties = class_definition.content.get("properties", {})
        required_fields = class_definition.content.get("required", [])

        return [
            Column(
                name=property_name,
                description=properties[property_name].get("description", ""),
                type=_get_element_type_from_schema(properties[property_name]),
                multivalued=properties[property_name]["type"] == "array",
                class_reference=None,
                enum="enum" in properties[property_name],
                required=property_name in required_fields,
            )
            for property_name in properties
        ]

    @staticmethod
    def set_relations_columns(
        class_definition: ClassDefinition, model: SchemaPack
    ) -> list[Column]:
        """Extracts columns from the relations of a class definition."""

        class_relations = class_definition.relations

        return [
            Column(
                name=relation_property_name,
                description=class_relation.description,
                type="string",
                enum=False,
                multivalued=False,
                class_reference=IdAnnotatedClass(
                    class_name=class_relation.targetClass,
                    id_property_name=model.classes[
                        class_relation.targetClass
                    ].id.propertyName,
                ),
                required=class_relation.mandatory.origin,
            )
            for relation_property_name, class_relation in class_relations.items()
        ]

def generate_worksheet_metadata(
    class_name: str, class_definition: ClassDefinition, model: SchemaPack, config: Config
) -> WorksheetMetadata:
    """Builds a worksheet from a class definition. Combined the column specs with
    the worksheet style parameters.
    """
    columns: list[Column] = []

    # ID column
    columns.append(ClassColumnFactory.set_id_column(class_definition))

    # Relations
    columns.extend(ClassColumnFactory.set_relations_columns(class_definition, model))

    # Content
    columns.extend(ClassColumnFactory.set_content_columns(class_definition))

    style = config.styles.get(class_name, WorksheetStyle())
    return WorksheetMetadata(
        class_name=class_name,
        columns=columns,
        id_property_name=class_definition.id.propertyName,
        header_color=style.header_color,
        content_color=style.content_color,
    )


def annotate_worksheet(worksheet_metadata: WorksheetMetadata, worksheet: Worksheet) -> Worksheet:
    """
    Annotates a worksheet object from openpyxl with metadata from WorksheetMetadata.
    """
    row_specs = [
        lambda col: col.name,
        lambda col: col.description,
        lambda col: col.type,
        lambda col: "multiple values" if col.multivalued else "single value",
        lambda col: col.restriction,
        lambda col: "required" if col.required else "optional",
    ]
    for spec in row_specs:
        worksheet.append([spec(col) for col in worksheet_metadata.columns])

    return worksheet

# def _make_value_cell(ws, fill_content):
#     """Creates a new cell for the value area of the worksheet"""
#     value_cell = Cell(ws)
#     if fill_content:
#         value_cell.fill = fill_content
#     value_cell.border = THIN_BORDER_GRAY
#     return value_cell


# def generate_workbook(sheets: Mapping[str, WorksheetMetadata]) -> Workbook:
#     """Generates a workbook from a dictionary of sheets."""
#     # Create a new workbook
#     workbook = Workbook()
#     # Remove the default sheet
#     workbook.remove(workbook.worksheets[0])

#     for sheet_name, sheet in sheets.items():
#         # Create a new sheet for the class
#         wb_sheet = workbook.create_sheet(title=sheet_name)

#         cols = sheet.columns
#         rows = []
#         rows.append([Cell(wb_sheet, value=col.name) for col in cols])
#         rows.append([Cell(wb_sheet, value=col.description) for col in cols])
#         rows.append([Cell(wb_sheet, value=col.type) for col in cols])
#         rows.append(
#             [
#                 Cell(
#                     wb_sheet,
#                     value="multiple values" if col.multivalued else "single value",
#                 )
#                 for col in cols
#             ]
#         )
#         rows.append([Cell(wb_sheet, value=col.restriction) for col in cols])
#         rows.append(
#             [
#                 Cell(wb_sheet, value="required" if col.required else "optional")
#                 for col in cols
#             ]
#         )

#         # FORMATTING

#         font_bold = Font(bold=True)

#         fill_header = (
#             PatternFill("solid", fgColor=sheet.header_color)
#             if sheet.header_color
#             else None
#         )
#         for cell in rows[0]:
#             cell.font = font_bold
#         for row in rows:
#             for cell in row:
#                 cell.alignment = ALIGN_HEADER
#                 if fill_header:
#                     cell.fill = fill_header
#                 cell.border = THIN_BORDER

#         if sheet.header_color:
#             wb_sheet.sheet_properties.tabColor = sheet.header_color

#         fill_content = (
#             PatternFill("solid", fgColor=sheet.content_color)
#             if sheet.content_color
#             else None
#         )

#         for _ in range(1000):
#             rows.append(
#                 [
#                     _make_value_cell(wb_sheet, fill_content)
#                     for _ in range(len(sheet.columns))
#                 ]
#             )

#         for row in rows:
#             wb_sheet.append(row)

#         for column in range(1, wb_sheet.max_column + 1):
#             wb_sheet.column_dimensions[get_column_letter(column)].width = 35

#     # Save the workbook to the specified output path
#     return workbook


def load_config(config_path: Path) -> Config:
    """Loads a config from a file."""
    with config_path.open("r") as file:
        return Config.model_validate(yaml.safe_load(file))


# def compare_xls(expected: Workbook, observed: Workbook):
#     """Compares two workbooks and raises a ContentDifference error if
#     differences are detected."""
#     if expected.sheetnames != observed.sheetnames:
#         raise ContentDifference(
#             f"Sheets differ. expected={expected.sheetnames}. observed={observed.sheetnames}"
#         )

#     for sheet in expected.sheetnames:
#         for row_idx, (row_a, row_b) in enumerate(
#             zip(expected[sheet].iter_rows(), observed[sheet].iter_rows()), 1
#         ):
#             for col_idx, (cell_a, cell_b) in enumerate(zip(row_a, row_b), 1):
#                 if cell_a.value != cell_b.value:
#                     raise ContentDifference(
#                         f"Cell values differ in sheet {sheet}, row {row_idx}, col {col_idx}: expected={cell_a.value}, observed={cell_b.value}"
#                     )
#                 for attr in ["alignment", "font", "border", "fill"]:
#                     if getattr(cell_a, attr).__dict__ != getattr(cell_b, attr).__dict__:
#                         raise ContentDifference(
#                             f"Cell {attr} differs in sheet {sheet}, row {row_idx}, col {col_idx}: expected={getattr(cell_a, attr).__dict__}, observed={getattr(cell_b, attr).__dict__}"
#                         )


# class ContentDifference(RuntimeError):
#     """Raised when a content difference was detected"""


# @contextmanager
# def working_directory(working_dir: Path) -> Generator[None, None, None]:
#     """Temporarily changes the working directory to the specified directory"""
#     cwd = Path.cwd()
#     try:
#         os.chdir(working_dir)
#         yield
#     finally:
#         os.chdir(cwd)


# def compare_folders(expected: Path, observed: Path):
#     """Function to check equality of contents of two folders with xlsx files."""

#     with working_directory(expected):
#         expected_glob = glob.glob("*")

#     with working_directory(observed):
#         observed_glob = glob.glob("*")

#     if sorted(expected_glob) != sorted(observed_glob):
#         raise ContentDifference(
#             f"Different directory contents. expected={expected_glob}. observed={observed_glob}"
#         )

#     for fname in expected_glob:
#         expected_wb = load_workbook(expected.joinpath(fname))
#         observed_wb = load_workbook(observed.joinpath(fname))
#         try:
#             compare_xls(expected=expected_wb, observed=observed_wb)
#         except ContentDifference as err:
#             raise ContentDifference(f"{fname}: {err}")


# def _add_transpiler_metadata(
#     workbook: Workbook, sheets: Mapping[str, WorksheetContent]
# ) -> None:
#     """Adds metadata to the workbook"""
#     ws = workbook.create_sheet("__transpiler_protocol")
#     ws.sheet_state = "hidden"
#     ws.cell(row=1, column=1, value="1.0.0")

#     # Add metadata about the sheets
#     ws = workbook.create_sheet("__sheet_meta")
#     ws.sheet_state = "hidden"
#     ws.append(
#         [
#             Cell(ws, value="sheet"),
#             Cell(ws, value="n_cols"),
#             Cell(ws, value="header_row"),
#             Cell(ws, value="data_start"),
#             Cell(ws, value="id_property_name"),
#         ]
#     )
#     for sheet_name, sheet in sheets.items():
#         ws.append(
#             [
#                 Cell(ws, value=sheet_name),
#                 Cell(ws, value=len(sheet.columns)),
#                 Cell(ws, value=1),
#                 Cell(ws, value=7),
#                 sheet.id_property_name,
#             ]
#         )

#     # Add metadata about the columns
#     ws = workbook.create_sheet("__column_meta")
#     ws.sheet_state = "hidden"
#     ws.append(
#         [
#             Cell(ws, value="sheet"),
#             Cell(ws, value="column"),
#             Cell(ws, value="multivalued"),
#             Cell(ws, value="type"),
#             Cell(ws, value="ref_class"),
#             Cell(ws, value="ref_class_id_property"),
#             Cell(ws, value="enum"),
#             Cell(ws, value="required"),
#         ]
#     )
#     for sheet_name, sheet in sheets.items():
#         for column in sheet.columns:
#             ws.append(
#                 [
#                     Cell(ws, value=sheet_name),
#                     Cell(ws, value=column.name),
#                     Cell(ws, value=column.multivalued),
#                     Cell(ws, value=column.type),
#                     Cell(
#                         ws,
#                         value=column.class_reference.class_name
#                         if column.class_reference
#                         else None,
#                     ),
#                     Cell(
#                         ws,
#                         value=column.class_reference.id_property_name
#                         if column.class_reference
#                         else None,
#                     ),
#                     Cell(ws, value=column.enum),
#                     Cell(ws, value=column.required),
#                 ]
#             )


# def create_xlsx_files(xlsx_dir: Path = XLSX_DIR) -> None:
#     schema = load_schemapack(Path(SCHEMAPACK_PATH))
#     config = load_config(Path(CONFIG_PATH))
#     sheets = parse_schema(schema, config)
#     workbook = generate_workbook(sheets)
#     _add_transpiler_metadata(workbook, sheets)
#     workbook.save(xlsx_dir / config.output_filename)


# def main(
#     check: bool = Option(
#         False,
#         help="Run read-only check that verifies that the documents are up-to-date.",
#     ),
# ):
#     """Generate a submission XLSX file from the schema pack."""
#     if check:
#         with TemporaryDirectory() as tmpdirname:
#             tmp_docs_dir = Path(tmpdirname)

#             create_xlsx_files(xlsx_dir=tmp_docs_dir)

#             try:
#                 compare_folders(XLSX_DIR, tmp_docs_dir)
#                 echo_success("Documents are up-to-date")
#             except ContentDifference as err:
#                 echo_failure("Documents are not up-to-date")
#                 echo_failure(str(err))
#                 sys.exit(1)
#     else:
#         create_xlsx_files()

def main():
    schema = load_schemapack(Path(SCHEMAPACK_PATH))
    config = load_config(Path(CONFIG_PATH))
    sheetmetadata = generate_worksheet_metadata("Analysis", schema.classes["Analysis"], schema, config)
    # annotated_ws = annotate_worksheet(sheetmetadata, Workbook().create_sheet(title="Analysis"))
    print(sheetmetadata)

if __name__ == "__main__":
    run(main)

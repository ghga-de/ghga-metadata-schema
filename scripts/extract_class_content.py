#!/usr/bin/env python3
"""Script to convert linkML schema to JSON schema and extract the class contents into
individual files"""

import json
import os
import subprocess
from pathlib import Path
from typing import Union

import yaml
from pydantic import BaseModel, TypeAdapter
from script_utils.cli import run

ROOT = Path(__file__).parent.parent.resolve()
LINKML_SCHEMA_PATH = ROOT / "src" / "schema" / "submission.yaml"
CLASS_CONTENT_DIR = ROOT / "src" / "content_schemas"
ENUM_CLASS_CONTENT_DIR = CLASS_CONTENT_DIR / "enums"
RELATIONS_CONFIG = ROOT / "relations_config.yaml"
EXCLUDE_CONFIG = ROOT / "exclude_config.yaml"


class Relation(BaseModel):
    """Model to represent the relation of a class."""

    name: str
    relations: list[Union[None, str]]


def load_yaml(path: Path):
    """Load the yaml file content."""
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data


def _reshaped_relation(path: Path = RELATIONS_CONFIG):
    """Reshape relations, convert it from a nested structure to a simple
    list with relation names."""
    data = load_yaml(path)
    return [
        {"name": key, "relations": value["relations"].keys()}
        for key, value in data["classes"].items()
    ]


def load_config():
    """Load the relations from relations_config.yaml."""

    def _construct_config(relations_config):
        return TypeAdapter(list[Relation]).validate_python(relations_config)

    relations_config = _reshaped_relation()
    return _construct_config(relations_config)


def linkml_to_json(file: Path) -> dict:
    """Create a JSON representation of the schema described in LinkML using LinkML
    command line option."""
    with subprocess.Popen(["gen-json-schema", file], stdout=subprocess.PIPE) as process:
        stdout, _ = process.communicate()
    return json.loads(stdout.decode("utf-8"))


def import_specification(json_schema: dict) -> dict:
    """Add the json schema specification to the class definitions."""
    for _, value in json_schema["$defs"].items():
        value["$schema"] = json_schema["$schema"]
    return json_schema


def add_id_to_class_defs(json_schema: dict) -> dict:
    """The reusable sub-schemas will live under the local content_schemas folder.
    Thus, it adds that path as id to class definitions"""
    for key, value in json_schema["$defs"].items():
        if "Enum" in key:
            value["$id"] = os.path.relpath(ENUM_CLASS_CONTENT_DIR / key, ROOT)
        else:
            value["$id"] = os.path.relpath(CLASS_CONTENT_DIR / key, ROOT)
    return json_schema


def delete_identifier(class_def: dict, identifier: str = "alias") -> dict:
    """Delete the identifier (alias) from the class contents since it
    should be a part of schemapack definition."""
    if class_def.get("properties") and identifier in class_def["properties"]:
        del class_def["properties"][identifier]
    if class_def.get("required") and identifier in class_def["required"]:
        class_def["required"].remove(identifier)
    return class_def


def replace_schema_refs(schema_defs: dict) -> dict:
    """Recursively replace '#/$defs/' references with the specified schemas path."""
    for key, value in schema_defs.items():
        if key == "$ref" and "Enum" in value:
            schema_defs[key] = value.replace(
                "#/$defs",
                str(os.path.relpath(ENUM_CLASS_CONTENT_DIR, ROOT)),
            )
        elif key == "$ref":
            schema_defs[key] = value.replace(
                "#/$defs",
                str(os.path.relpath(CLASS_CONTENT_DIR, ROOT)),
            )
        elif isinstance(value, dict):
            schema_defs[key] = replace_schema_refs(value)
    return schema_defs


def delete_class_relations(class_def: dict, class_relations: list):
    """Delete the class properties that denotes to its relatives."""
    for relation in class_relations:
        if relation in class_def["properties"]:
            del class_def["properties"][relation]
        if relation in class_def["required"]:
            class_def["required"].remove(relation)
    return class_def


def clean_schema_relations(schema_defs: dict, config: list[Relation]):
    """Delete class relations from the classes of schema definition."""
    for element in config:
        if schema_defs.get(element.name):
            delete_class_relations(schema_defs[element.name], element.relations)
    return schema_defs


def clean_content_identifier(schema_defs: dict):
    """Remove class identifiers from the class definitions."""
    for _, class_info in schema_defs.items():
        delete_identifier(class_info)
    return schema_defs


def export_class_content(schema_defs: dict):
    """Write class schemas to separate files."""

    # Ensure content_schemas and enums directory exists; create it if not
    ENUM_CLASS_CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    for class_name, class_info in schema_defs.items():
        if "Enum" in class_name:
            filename = str(ENUM_CLASS_CONTENT_DIR / class_name) + ".json"
        else:
            filename = str(CLASS_CONTENT_DIR / class_name) + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(class_info, file, indent=4)
            file.write("\n")


def main():
    """The main routine."""
    schema_in_json = linkml_to_json(LINKML_SCHEMA_PATH)
    schema_bundle = import_specification(add_id_to_class_defs(schema_in_json))
    modified_refs = replace_schema_refs(schema_bundle["$defs"])
    deleted_identifier = clean_content_identifier(modified_refs)
    deleted_relations = clean_schema_relations(deleted_identifier, load_config())
    export_class_content(deleted_relations)


if __name__ == "__main__":
    run(main)
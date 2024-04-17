#!/usr/bin/env python3

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

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
CLASS_CONTENT_DIR = HERE.parent / "src" / "content_schemas"
RELATIONS_CONFIG = HERE.parent / "relations_config.yaml"
EXCLUDE_CONFIG = HERE.parent / "exclude_config.yaml"


class Relation(BaseModel):
    """Model to represent the relation of a class"""

    name: str
    relations: list[Union[None, str]]


def load_yaml(path: Path):
    """Loads the yaml file content"""
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data


def _reshaped_relation(path: Path = RELATIONS_CONFIG):
    """reshapes the relations, converts them from a nested structure to a simple
    list with relation names"""
    data = load_yaml(path)
    return [
        {"name": key, "relations": value["relations"].keys()}
        for key, value in data["classes"].items()
    ]


def load_config():
    """Loads the relations from relations_config.yaml"""

    def _construct_config(relations_config):
        return TypeAdapter(list[Relation]).validate_python(relations_config)

    relations_config = _reshaped_relation()
    return _construct_config(relations_config)


def linkml_to_json(file: Path) -> dict:
    """Creates a JSON representation of the schema described in LinkML using LinkML
    command line option"""
    with subprocess.Popen(["gen-json-schema", file], stdout=subprocess.PIPE) as process:
        stdout, _ = process.communicate()
    return json.loads(stdout.decode("utf-8"))


def add_id_to_class_defs(json_schema: dict) -> dict:
    """The reusable sub-schemas will live under the local class-content-schema.
    Thus, it adds that path as id to class definitions"""
    for key, value in json_schema["$defs"].items():
        value["$id"] = os.path.relpath(CLASS_CONTENT_DIR / key, ROOT)
    return json_schema


def delete_identifier(class_def: dict, identifier: str = "alias") -> dict:
    """Deletes the identifier (alias) from the class contents since it
    should be a part of schemapack definition"""
    if class_def.get("properties") and identifier in class_def["properties"]:
        del class_def["properties"][identifier]
    if class_def.get("required") and identifier in class_def["required"]:
        class_def["required"].remove(identifier)
    return class_def


def replace_schema_refs(schema_defs: dict) -> dict:
    """Recursively replaces '#/$defs/' references with the specified schemas path."""
    for key, value in schema_defs.items():
        if key == "$ref":
            schema_defs[key] = value.replace(
                "#/$defs",
                str(os.path.relpath(CLASS_CONTENT_DIR, ROOT)),
            )
        elif isinstance(value, dict):
            schema_defs[key] = replace_schema_refs(value)
    return schema_defs


def delete_class_relations(class_def: dict, class_relations: list):
    """Deletes the class properties that denotes to its relatives"""
    for relation in class_relations:
        if relation in class_def["properties"]:
            del class_def["properties"][relation]
        if relation in class_def["required"]:
            class_def["required"].remove(relation)
    return class_def


def clean_schema_relations(schema_defs: dict, config: list[Relation]):
    """Deletes class relations from the classes of schema definition"""
    for element in config:
        if schema_defs.get(element.name):
            delete_class_relations(schema_defs[element.name], element.relations)
    return schema_defs


def clean_content_identifier(schema_defs: dict):
    """Removes class identifiers from the class definitions"""
    for _, class_info in schema_defs.items():
        delete_identifier(class_info)
    return schema_defs


def export_class_content(schema_defs: dict, excluded_list: list):
    """Writes class schemas to separate files"""
    for class_name, class_info in schema_defs.items():
        if class_name not in excluded_list:
            filename = str(CLASS_CONTENT_DIR / class_name) + ".json"
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(class_info, file, indent=4)
                file.write("\n")


def main():
    """The main routine."""
    schema_in_json = linkml_to_json(Path("src/schema/submission.yaml"))
    schema_bundle = add_id_to_class_defs(schema_in_json)
    modified_refs = replace_schema_refs(schema_bundle["$defs"])
    deleted_identifier = clean_content_identifier(modified_refs)
    deleted_relations = clean_schema_relations(deleted_identifier, load_config())
    exclusions = load_yaml(EXCLUDE_CONFIG)
    export_class_content(deleted_relations, exclusions)


if __name__ == "__main__":
    run(main)

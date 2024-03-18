#!/usr/bin/env python3
"""Script to convert linkML schema to JSON schema and extract the class contents into 
individual files"""

import subprocess
from pathlib import Path
from script_utils.cli import run
import json
from os import fspath
from pydantic import BaseModel, TypeAdapter
import yaml
from typing import Union

HERE = Path(__file__).parent.resolve()
CLASS_CONTENT_DIR = HERE.parent / "src" / "schemas"
RELATIONS_CONFIG = HERE.parent / "relations_config.yaml"


class Relation(BaseModel):
    """Model to represent the relation of a class"""
    name: str
    relations: list[Union[None, str]]


def load_config():
    """Loads the relations from relations_config.yaml"""

    def _construct_config(relations_config):
        return TypeAdapter(list[Relation]).validate_python(relations_config)

    with RELATIONS_CONFIG.open("r", encoding="utf-8") as file:
        relations_config = yaml.safe_load(file)
    return _construct_config(relations_config["classes"])


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
        value["$id"] = fspath(CLASS_CONTENT_DIR / key)
    return json_schema


def replace_schema_refs(schema_defs: dict) -> dict:
    """Recursively replaces '#/$defs/' references with the specified schemas path."""
    for key, value in schema_defs.items():
        if key == "$ref":
            schema_defs[key] = value.replace("#/$defs", str(CLASS_CONTENT_DIR))
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
            delete_class_relations(schema_defs[element.name],  element.relations) 
    return schema_defs


def export_class_content(schema_defs: dict):
    """Writes class schemas to separate files"""
    for class_name , class_info in schema_defs.items():
        filename = str(CLASS_CONTENT_DIR / class_name) + ".json"
        with open (filename, "w", encoding="utf-8") as file:
            json.dump(class_info, file, indent=4)


def main():
    """The main routine."""
    schema_in_json = linkml_to_json(Path("src/schema/submission.yaml"))
    schema_bundle = add_id_to_class_defs(schema_in_json)
    modified_refs = replace_schema_refs(schema_bundle["$defs"])
    deleted_relations = clean_schema_relations(modified_refs, load_config())
    export_class_content(deleted_relations)



if __name__ == "__main__":
    run(main)

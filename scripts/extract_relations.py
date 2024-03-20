#!/usr/bin/env python3
"""Script to extract the relations between classes from the metadata model described in LinkML"""

from pathlib import Path
from typing import Any, Union
import yaml
from pydantic import BaseModel, Field
from script_utils.cli import run


class SchemaClass(BaseModel):
    """Model describing a basic schema class"""

    name: str
    slots: list
    relations: list[Union[Any, str]] = Field(default_factory=list)


class Schema(BaseModel):
    """Model describing a basic linkML schema """

    json_schema: dict[str, Any]
    classes: list[SchemaClass]

    @property
    def class_names(self) -> list[str]:
        """function"""
        return self.json_schema.get("classes", {}).keys()

    @property
    def slots(self) -> dict:
        "function"
        return self.json_schema.get("slots", {})


def construct_classes(schema: dict) -> list[SchemaClass]:
    "Converts the classes contained in the schema into a list of SchemaClass objects"
    class_dict = schema.get("classes", {})
    return [
        SchemaClass(name=key, slots=value["slots"])
        for key, value in class_dict.items()
        if value.get("slots")
    ]


def load_schema(path: Path) -> Schema:
    """Loads the metadata schema from a file"""
    with path.open("r", encoding="utf-8") as file:
        schema = yaml.safe_load(file)
    return Schema.model_validate(
        {"json_schema": schema, "classes": construct_classes(schema)}
    )


def slots_with_class_range(schema: Schema) -> dict:
    """Extracts the slot names that have a 'class' range and outputs a dictionary with
    slot name, range key-value pairs."""
    return {
        slot: value["range"]
        for slot, value in schema.slots.items()
        if value.get("range") and value.get("range") in schema.class_names
    }


def class_relations(schema_class: SchemaClass, class_ranged_slots: dict) -> list:
    """Extracts the classes that a given class is in relation with"""
    return [
        slot
        for slot in schema_class.slots
        if slot in class_ranged_slots
    ]


def save_relations(schema: Schema, filename: str):
    "Creates a config file that involves the classes and their relations to other classes"

    def _relations(schema) -> dict:
        """function"""
        return schema.model_dump(
            exclude={
                "classes": {"__all__": "slots"},
                "json_schema": True,
                "class_names": True,
                "slots": True,
            }
        )

    with open(filename, "w") as outfile:
        yaml.dump(_relations(schema), outfile, default_flow_style=False)


def main():
    """The main routine."""
    schema = load_schema(Path("/workspace/src/schema/submission.yaml"))
    class_ranged_slots = slots_with_class_range(schema)
    for schema_class in schema.classes:
        schema_class.relations = class_relations(schema_class, class_ranged_slots)
    save_relations(schema, "relations_config.yaml")


if __name__ == "__main__":
    run(main)

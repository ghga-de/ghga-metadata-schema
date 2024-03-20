#!/usr/bin/env python3
"""Script to convert linkML schema to schemapack definition"""

# it needs to take the linkml schema as an input

# it needs to extract the classes (what should I do with the mixins and the enums? they do not belong to the schemapack)

# after the class, it will be id, content, relation

from pathlib import Path

import yaml
from pydantic import BaseModel
from schemapack.spec.schemapack import (
    ClassDefinition,
    ContentSchema,
    FrozenDict,
    IDSpec,
    MandatoryRelationSpec,
    MultipleRelationSpec,
    Relation,
    SchemaPack,
)
from script_utils.cli import run

HERE = Path(__file__).parent.resolve()
LINKML_SCHEMA = HERE.parent / "src" / "schema" / "submission.yaml"
RELATIONS_CONFIG = HERE.parent / "relations_config.yaml"
CLASS_CONTENT_FOLDER = HERE.parent / "src" / "schemas"
EXCLUDED_CLASSES = HERE.parent / "exclude_config.yaml"


def load_yaml(path: Path):
    """Loads the data from a yaml file"""
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def construct_relation(class_relations: list) -> dict[str, Relation]:
    """Creates objects of Relations from the relation list of a class"""

    return {
        relation: Relation(
            description=None,
            targetClass=relation.upper(),
            mandatory=MandatoryRelationSpec(origin=True, target=True),
            multiple=MultipleRelationSpec(origin=True, target=True),
        )
        for relation in class_relations
    }


def construct_content_schema(path: Path) -> str:
    """function"""
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def construct_schemapack_class(class_name: str, class_desc: str, class_relations: list):
    """Creates ClassDefinition object"""
    return ClassDefinition(
        description=class_desc,
        id=IDSpec(propertyName="alias", description=None),
        content=ContentSchema(
            json_schema=construct_content_schema(
                Path(f"{CLASS_CONTENT_FOLDER}/{class_name}.json")
            )
        ),
        relations=FrozenDict(construct_relation(class_relations)),
    )


def get_class_relations(class_name: str, relations_config: dict) -> list:
    """Extracts the relations of a given class from the relations config"""
    for info in relations_config["classes"]:
        if info["name"] == class_name:
            return info["relations"]
    return []


def construct_schemapack(
    schema: dict, relations_config: dict, excluded_config: list
) -> list[ClassDefinition]:
    """function"""
    return [
        construct_schemapack_class(
            key, value["description"], get_class_relations(key, relations_config)
        )
        for key, value in schema["classes"].items()
        if key not in excluded_config
    ]


def main():
    """The main routine."""
    schema = load_yaml(LINKML_SCHEMA)
    relations = load_yaml(RELATIONS_CONFIG)
    excluded = load_yaml(EXCLUDED_CLASSES)
    print(construct_schemapack(schema, relations, excluded))


if __name__ == "__main__":
    run(main)

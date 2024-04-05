#!/usr/bin/env python3
"""Script to convert linkML schema to schemapack definition"""

from pathlib import Path

import yaml
from schemapack._internals.dump import dump_schemapack
from schemapack.spec.schemapack import (
    ClassDefinition,
    ContentSchema,
    IDSpec,
    MandatoryRelationSpec,
    MultipleRelationSpec,
    Relation,
    SchemaPack,
)
from script_utils.cli import run

HERE = Path(__file__).parent.resolve()
SCHEMA_FOLDER = HERE.parent / "src" / "schema" / "schemapack.yaml"
LINKML_SCHEMA = HERE.parent / "src" / "schema" / "submission.yaml"
RELATIONS_CONFIG = HERE.parent / "relations_config.yaml"
CLASS_CONTENT_FOLDER = HERE.parent / "src" / "content_schema_artifacts"
EXCLUDED_CLASSES = HERE.parent / "exclude_config.yaml"


def load_yaml(path: Path):
    """Loads the data from a yaml file"""
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def construct_mandatory(relation_name: str, class_schema: dict):
    """Returns the constraints in the relationship modality"""
    return MandatoryRelationSpec(
        origin=True,
        target=class_schema.get("slot_usage", {})
        .get(relation_name, {})
        .get("required", False),
    )


def construct_multiple():
    """Returns the schemapack specification for 1 to n relationship"""
    return MultipleRelationSpec(origin=True, target=False)


def construct_relation(
    class_relations: dict, class_schema: dict
) -> dict[str, Relation]:
    """Creates objects of Relations from the relation list of a class"""

    return {
        key: Relation(
            description=None,
            targetClass=value.get("targetClass"),
            mandatory=construct_mandatory(key, class_schema),
            multiple=construct_multiple(),
        )
        for key, value in class_relations.items()
    }


def construct_content_schema(path: Path) -> str:
    """Reads the content schema"""
    with path.open("r", encoding="utf-8") as file:
        content = file.read()
    return content


def construct_schemapack_class(
    class_name: str, class_relations: dict, class_schema: dict
) -> ClassDefinition:
    """Creates ClassDefinition object"""
    return ClassDefinition(
        description=class_schema["description"],
        id=IDSpec(propertyName="alias", description=None),
        content=ContentSchema(
            json_schema=construct_content_schema(
                Path(f"{CLASS_CONTENT_FOLDER}/{class_name}.json")
            )
        ),
        relations=construct_relation(class_relations, class_schema),
    )


def get_class_relations(class_name: str, relations_config: dict) -> dict:
    """Extracts the relations of a given class from the relations config"""
    for info in relations_config["classes"]:
        if info["name"] == class_name:
            return info["relations"]
    return {}


def _class_definitions(
    schema: dict, relations_config: dict, excluded_config: list
) -> dict:
    """Generates ClassDefinition and maps it to class name"""
    return {
        key: construct_schemapack_class(
            key, get_class_relations(key, relations_config), value
        )
        for key, value in schema["classes"].items()
        if key not in excluded_config
    }


def construct_schemapack(class_defs: dict):
    """Creates schemapack object"""
    return SchemaPack(
        schemapack="0.3.0",
        description="Schemapack definition",
        classes=class_defs,
        rootClass=None,
    )


def main():
    """The main routine."""
    schema = load_yaml(LINKML_SCHEMA)
    relations = load_yaml(RELATIONS_CONFIG)
    excluded = load_yaml(EXCLUDED_CLASSES)
    schemapack = construct_schemapack(_class_definitions(schema, relations, excluded))

    dump_schemapack(
        schemapack, path=SCHEMA_FOLDER, content_schema_dir=CLASS_CONTENT_FOLDER
    )


if __name__ == "__main__":
    run(main)

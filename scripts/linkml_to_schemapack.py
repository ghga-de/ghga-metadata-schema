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
SCHEMA_FOLDER = HERE.parent / "src" / "schema" / "submission.schemapack.yaml"
LINKML_SCHEMA = HERE.parent / "src" / "schema" / "submission.yaml"
RELATIONS_CONFIG = HERE.parent / "relations_config.yaml"
CLASS_CONTENT_FOLDER = HERE.parent / "src" / "content_schema_artifacts"
EXCLUDED_CLASSES = HERE.parent / "exclude_config.yaml"

SCHEMAPACK_SCHEMA_DESCRIPTION = "Metadata schema for the German Human Genome-Phenome Archive (GHGA)"

def load_yaml(path: Path):
    """Loads the data from a yaml file"""
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def construct_mandatory(relation_name: str, linkml_class_schema: dict):
    """Returns the constraints in the relationship modality"""
    return MandatoryRelationSpec(
        origin=False,
        target=linkml_class_schema.get("slot_usage", {})
        .get(relation_name, {})
        .get("required", False),
    )


def construct_multiple(relation_name: str, linkml_overall_schema: dict):
    """Returns the schemapack specification for 1 to n relationship"""
    return MultipleRelationSpec(
        origin=True,
        target=linkml_overall_schema.get("slots", {}).get(relation_name, {}).get("multivalued", False),
    )


def construct_relation(
    class_relations: dict, linkml_class_schema: dict, linkml_overall_schema: dict
) -> dict[str, Relation]:
    """Creates objects of Relations from the relation list of a class"""

    return {
        key: Relation(
            description=None,
            targetClass=value.get("targetClass"),
            mandatory=construct_mandatory(key, linkml_class_schema),
            multiple=construct_multiple(key, linkml_overall_schema),
        )
        for key, value in class_relations.items()
    }



def construct_schemapack_class(
    class_name: str, class_relations: dict, linkml_class_schema: dict, linkml_overall_schema: dict
) -> ClassDefinition:
    """Creates ClassDefinition object"""
    return ClassDefinition(
        description=linkml_class_schema["description"],
        id=IDSpec(propertyName="alias", description=None),
        content=ContentSchema(
            json_schema= Path.read_text(
                Path(f"{CLASS_CONTENT_FOLDER}/{class_name}.json")
            )
        ),
        relations=construct_relation(class_relations, linkml_class_schema, linkml_overall_schema),
    )


def get_class_relations(class_name: str, relations_config: dict) -> dict:
    """Extracts the relations of a given class from the relations config"""
    return relations_config["classes"][class_name].get("relations", {})


def _class_definitions(
    linkml_overall_schema: dict,
    relations_config: dict,
    excluded_config: list,
) -> dict:
    """Generates ClassDefinition and maps it to class name from linkml schema"""
    return {
        key: construct_schemapack_class(
            key, get_class_relations(key, relations_config), value, linkml_overall_schema
        )
        for key, value in linkml_overall_schema["classes"].items()
        if key not in excluded_config
    }


def construct_schemapack(schemapack_class_definitions: dict, schemapack_schema_description: str = SCHEMAPACK_SCHEMA_DESCRIPTION):
    """Creates schemapack object"""
    return SchemaPack(
        schemapack="0.3.0",
        description=schemapack_schema_description,
        classes=schemapack_class_definitions,
        rootClass=None,
    )


def main():
    """The main routine."""
    linkml_overall_schema = load_yaml(LINKML_SCHEMA)
    relations = load_yaml(RELATIONS_CONFIG)
    excluded = load_yaml(EXCLUDED_CLASSES)
    schemapack = construct_schemapack(_class_definitions(linkml_overall_schema, relations, excluded))

    dump_schemapack(
        schemapack,
        path=SCHEMA_FOLDER,
        content_schema_dir=CLASS_CONTENT_FOLDER,
    )


if __name__ == "__main__":
    run(main)

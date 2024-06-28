#!/usr/bin/env python3
"""Script to convert linkML schema to schemapack definition"""

from pathlib import Path
from typing import Any
import json
import yaml
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

ROOT = Path(__file__).parent.parent.resolve()
SCHEMA_FOLDER = ROOT / "src"/ "ghga_metadata_schema.schemapack.yaml"
LINKML_SCHEMA = ROOT / "src" / "schema" / "submission.yaml"
RELATIONS_CONFIG = ROOT / "relations_config.yaml"
CLASS_CONTENT_FOLDER = ROOT / "src" / "content_schemas"
EXCLUDED_CLASSES = ROOT / "exclude_config.yaml"

SCHEMAPACK_SCHEMA_DESCRIPTION = (
    "Metadata schema for the German Human Genome-Phenome Archive (GHGA)"
)


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
        target=linkml_overall_schema.get("slots", {})
        .get(relation_name, {})
        .get("multivalued", False),
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
    class_name: str,
    class_relations: dict,
    linkml_class_schema: dict,
    linkml_overall_schema: dict,
) -> ClassDefinition:
    """Creates a ClassDefinition object that describes a schemapack class definition"""
    return ClassDefinition(
        description=linkml_class_schema["description"],
        id=IDSpec(propertyName="alias", description=None),
        content=ContentSchema(
            json_schema=Path.read_text(
                Path(f"{CLASS_CONTENT_FOLDER}/{class_name}.json")
            )
        ),
        relations=construct_relation(
            class_relations, linkml_class_schema, linkml_overall_schema
        ),
    )


def get_class_relations(class_name: str, relations_config: dict) -> dict:
    """Extracts the relations of a class from the relations config"""
    return relations_config["classes"][class_name].get("relations", {})


def _class_definitions(
    linkml_overall_schema: dict,
    relations_config: dict,
    excluded_config: list,
) -> dict:
    """Maps a ClassDefinition to its class name from linkml schema"""
    return {
        key: construct_schemapack_class(
            key,
            get_class_relations(key, relations_config),
            value,
            linkml_overall_schema,
        )
        for key, value in linkml_overall_schema["classes"].items()
        if key not in excluded_config
    }


def construct_schemapack(
    schemapack_class_definitions: dict,
    schemapack_schema_description: str = SCHEMAPACK_SCHEMA_DESCRIPTION,
):
    """Creates schemapack object"""
    return SchemaPack(
        schemapack="0.3.0",
        description=schemapack_schema_description,
        classes=schemapack_class_definitions,
        rootClass=None,
    )


def get_content_schema_path(class_name: str, content_schema_dir: Path, root_dir: Path = ROOT 
) -> Path:
    """Create a path to a content-schema file of a class, relative to the root directory.
    """
    return  content_schema_dir.relative_to(root_dir) / f"{class_name}.json"


def set_content_schema_paths(
    schemapack_dict: dict[str, Any], content_schema_dir: Path = CLASS_CONTENT_FOLDER
) -> dict[str, Any]:
    """Sets the content-schema paths in the schemapack dictionary."""
    modified_classes = {
        class_name: {
            **class_,
            "content": str(
                get_content_schema_path(
                    class_name, content_schema_dir
                )
            ),
        }
        for class_name, class_ in schemapack_dict["classes"].items()
    }

    return {**schemapack_dict, "classes": modified_classes}


def dump_schemapack(schemapack: SchemaPack, *, path: Path):
    """Dumps the contents of a SchemaPack object to a YAML file at the path.
    It produces a non-condensed schemapack definition, where the value of the class
    -contents are set to the relative paths of their corresponding json schema file."""

    parent_dir = path.parent
    if not parent_dir.exists():
        raise FileNotFoundError(f"The parent directory of '{path}' does not exist.")

    schemapack_dict = json.loads(schemapack.model_dump_json(exclude_defaults=True))
    modified_schemapack_dict = set_content_schema_paths(
        schemapack_dict,
    )
    with open(path, "w", encoding="utf-8") as file:
        yaml.dump(modified_schemapack_dict, file)


def main():
    """The main routine."""
    linkml_overall_schema = load_yaml(LINKML_SCHEMA)
    relations = load_yaml(RELATIONS_CONFIG)
    excluded = load_yaml(EXCLUDED_CLASSES)
    schemapack = construct_schemapack(
        _class_definitions(linkml_overall_schema, relations, excluded)
    )
    dump_schemapack(schemapack, path=SCHEMA_FOLDER)


if __name__ == "__main__":
    run(main)
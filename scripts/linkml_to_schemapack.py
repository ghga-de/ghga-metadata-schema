#!/usr/bin/env python3
# Copyright 2021 - 2025 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
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

"""Script to convert linkML schema to schemapack definition"""

import json
from pathlib import Path
from typing import Any

import yaml
from arcticfreeze import FrozenDict
from schemapack.spec.schemapack import (
    ClassDefinition,
    ClassRelation,
    IDSpec,
    MandatoryRelationSpec,
    MultipleRelationSpec,
    SchemaPack,
)
from script_utils.cli import run

ROOT = Path(__file__).parent.parent.resolve()
SCHEMA_FOLDER = ROOT / "src" / "ghga_metadata_schema.schemapack.yaml"
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

def _get_relation_description(slot_name: str, linkml_class_schema:dict, linkml_overall_schema: dict) -> str:
    """Extracts the description of a relation slot."""
    try:
        return linkml_overall_schema["slots"][slot_name].get("description", "")
    except KeyError:
        original_target = linkml_class_schema["is_a"]
        return linkml_overall_schema["classes"][original_target]["slot_usage"][slot_name].get("description", "")


def construct_relation(
    class_relations: dict, linkml_class_schema: dict, linkml_overall_schema: dict
) -> FrozenDict[str, ClassRelation]:
    """Creates objects of Relations from the relation list of a class"""
    return FrozenDict({
        key: ClassRelation(
            description=_get_relation_description(key, linkml_class_schema, linkml_overall_schema),
            targetClass=value.get("targetClass"),
            mandatory=construct_mandatory(key, linkml_class_schema),
            multiple=construct_multiple(key, linkml_overall_schema),
        )
        for key, value in class_relations.items()
    })



def construct_schemapack_class(
    class_name: str,
    class_relations: dict,
    linkml_class_schema: dict,
    linkml_overall_schema: dict,
) -> ClassDefinition:
    """Creates a ClassDefinition object that describes a schemapack class definition"""
    return ClassDefinition(
        description=linkml_class_schema["description"],
        id=IDSpec(propertyName="alias", description=linkml_overall_schema["slots"]["alias"].get("description", "")),
        content=Path(f"{CLASS_CONTENT_FOLDER}/{class_name}.json"),  # type: ignore
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
) -> FrozenDict:
    """Maps a ClassDefinition to its class name from linkml schema"""
    return FrozenDict({
        key: construct_schemapack_class(
            key,
            get_class_relations(key, relations_config),
            value,
            linkml_overall_schema,
        )
        for key, value in linkml_overall_schema["classes"].items()
        if key not in excluded_config
    })


def construct_schemapack(
    schemapack_class_definitions: FrozenDict[str, ClassDefinition],
    schemapack_schema_description: str = SCHEMAPACK_SCHEMA_DESCRIPTION,
):
    """Creates schemapack object"""
    return SchemaPack(
        schemapack="3.0.0",
        description=schemapack_schema_description,
        classes=schemapack_class_definitions,
        rootClass=None,
    )


def get_content_schema_path(
    class_name: str, content_schema_dir: Path, root_dir: Path = ROOT
) -> Path:
    """Create a path to a content-schema file of a class, relative to the root directory."""
    return content_schema_dir.relative_to(root_dir) / f"{class_name}.json"


def set_content_schema_paths(
    schemapack_dict: dict[str, Any], content_schema_dir: Path = CLASS_CONTENT_FOLDER
) -> dict[str, Any]:
    """Sets the content-schema paths in the schemapack dictionary."""
    modified_classes = {
        class_name: {
            **class_,
            "content": str(get_content_schema_path(class_name, content_schema_dir)),
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

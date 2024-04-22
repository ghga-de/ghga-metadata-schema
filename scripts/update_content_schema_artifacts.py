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

"""Script to generate content schema artifacts"""

import json
import os
from difflib import unified_diff
from pathlib import Path
from typing import Union

import yaml
from referencing import Registry, Resource, Specification
from referencing._core import Resolver
from referencing.jsonschema import DRAFT7
from referencing.typing import URI
from script_utils.cli import echo_failure, echo_success, run

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
CONTENT_SCHEMAS_DIR = ROOT / "src" / "content_schemas"
SCHEMA_ARTIFACTS_DIR = ROOT / "src" / "content_schema_artifacts"
EXCLUDE_CONFIG = ROOT / "exclude_config.yaml"


class MissingResourceException(Exception):
    """Raised when an expected resource is missing in the existing registry."""


class DifferentArtifactContentException(Exception):
    """Raised when the content of a resource differs between the existing and expected
    registries."""


def is_equal(existing_resource: Resource, expected_resource: Resource) -> bool:
    """Check if the contents of the two resources are equal."""
    if (
        existing_resource.id() == expected_resource.id()
        and existing_resource.contents == expected_resource.contents
    ):
        return True
    return False


def print_diff(existing_resource: dict, expected_resource: str):
    """Print differences between expected and observed files."""
    echo_failure("Differences in content schema artifacts:")
    existing_content = "\n".join(sorted(str(existing_resource).split(",")))
    expected_content = "\n".join(sorted(str(expected_resource).split(",")))
    for line in unified_diff(
        expected_content.splitlines(keepends=True),
        existing_content.splitlines(keepends=True),
    ):
        print("   ", line.rstrip())


def compare_registries(
    existing_registry: Registry, expected_registry: Registry
) -> bool:
    """Compare two registries to check if they contain the same resources."""
    for uri, resource in expected_registry.items():
        if not existing_registry.get(uri):
            raise MissingResourceException(
                f"{uri} does not exist in the registry. Update the artifacts"
            )
        if not is_equal(resource, existing_registry[uri]):
            print_diff(existing_registry[uri].contents, expected_registry[uri].contents)
            raise DifferentArtifactContentException(
                f"Differences in {uri}: Update content schema artifacts"
            )
    return True


def retrieve_from_filesystem(path: Path) -> Resource:
    """
    Retrieve a JSON object from a file.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        Resource: A resource object representing the JSON content.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Schema file '{path}' not found")
    with path.open("r", encoding="utf-8") as file:
        contents = json.load(file)
    return Resource.from_contents(contents=contents)


def create_registry_from_filesystem(
    schema_dir: Path,
) -> Registry:
    """
    Create a registry of JSON objects obtained from the file system.

    Args:
        schema_dir (Path): The directory containing JSON schema files.

    Returns:
        Registry: A registry object containing resources parsed from JSON files.
    """
    my_registry = Registry()
    for schema_file in schema_dir.glob("*.json"):
        resource = retrieve_from_filesystem(schema_file)
        my_registry = resource @ my_registry
    return my_registry


def resolve_referenced_schemas(
    resource_content: dict, resolver: Resolver, resolved_uris: Union[None, list] = None
) -> tuple[dict, list]:
    """
    Modify the resource content by replacing referenced paths with corresponding JSON schemas.

    Args:
        resource_content (dict): The content of the resource to be modified.
        resolver (Resolver): Resolver object used to look up referenced paths.

    Returns:
        tuple: The modified resource content.
    """

    if resolved_uris is None:
        resolved_uris = []

    for _key, value in resource_content.items():
        if isinstance(value, dict) and "$ref" in value.keys():
            value.update(resolver.lookup(value["$ref"]).contents)
            resolved_uris.append(value["$ref"])
            del value["$ref"]
        elif isinstance(value, dict):
            resolve_referenced_schemas(value, resolver, resolved_uris)
    return resource_content, resolved_uris


def create_resource(content: dict) -> Resource:
    """
    Create a resource object from content and specification.
    """
    return Resource.from_contents(contents=content)


def export_registry(registry: Registry, export_dir: Path):
    """
    Export the contents of the registry resources to individual files.

    Args:
        registry (Registry): The registry containing the resources to be exported.
        export_dir (Path): The directory where the exported files will be saved.
    """
    export_dir.mkdir(parents=True, exist_ok=True)
    for uri, resource in registry.items():
        file_path = export_dir / f"{uri.split('/')[-1]}.json"
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(resource.contents, file, indent=4)


def get_content_uris(
    class_content_dir: Path = CONTENT_SCHEMAS_DIR,
    relative_to: Path = ROOT,
) -> list[URI]:
    """Return the list of URIs of the class content schemas. The URIs are relative to root path"""
    return [
        os.path.join(
            os.path.relpath(class_content_dir, relative_to),
            cls.replace(".json", ""),
        )
        for cls in os.listdir(class_content_dir)
    ]


def _load_yaml(path: Path):
    """Loads the yaml file content"""
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data


def _exclusion_uris(
    base_uri: Path = CONTENT_SCHEMAS_DIR, exclusions: Path = EXCLUDE_CONFIG
) -> list[URI]:
    """Create a list of uris of the classes that are to be excluded."""

    to_exclude = _load_yaml(exclusions)
    return [
        os.path.join(
            os.path.relpath(base_uri, ROOT),
            name,
        )
        for name in to_exclude
    ]


def exclude_uris(registry: Registry, exclusions: list) -> Registry:
    """Removed uris from the registry"""
    for uri in exclusions:
        if uri in registry._resources:
            registry = registry.remove(uri)
    return registry


def generate_artifacts(
    content_json_schemas_registry: Registry, schema_uris: list
) -> Registry:
    """The routine to create a registry of the artifacts generated from content schemas."""

    resolved_registry_uris = set()
    # incorporate referenced sub-resources in the resource content
    for schema_uri in schema_uris:
        resolved_content, resolved_uris = resolve_referenced_schemas(
            content_json_schemas_registry.contents(schema_uri),
            content_json_schemas_registry.resolver(),
        )
        resolved_registry_uris.update(resolved_uris)
        modified_resource = create_resource(resolved_content)
        updated_registry = modified_resource @ content_json_schemas_registry
    # remove the content of the resolved resources from the registry
    updated_registry = exclude_uris(updated_registry, list(resolved_registry_uris))
    # remove the content of the classes that should be excluded from the registry
    final_registry = exclude_uris(updated_registry, _exclusion_uris())
    return final_registry


def main(check: bool = False):
    """The main routine."""

    expected_registry = generate_artifacts(
        create_registry_from_filesystem(CONTENT_SCHEMAS_DIR),
        get_content_uris(),
    )

    if check:
        existing_registry = create_registry_from_filesystem(SCHEMA_ARTIFACTS_DIR)
        if compare_registries(existing_registry, expected_registry):
            echo_success("Content schema artifacts are up-to-date")
    else:
        export_registry(expected_registry, SCHEMA_ARTIFACTS_DIR)
        echo_success(f"Content schema artifacts are saved to {SCHEMA_ARTIFACTS_DIR}")


if __name__ == "__main__":
    run(main)

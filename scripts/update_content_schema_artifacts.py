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

from referencing import Registry, Resource, Specification
from referencing._core import Resolver
from referencing.jsonschema import DRAFT202012
from referencing.typing import URI
from script_utils.cli import echo_failure, echo_success, run

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
CLASS_CONTENT_DIR = HERE.parent / "src" / "content_schemas"
SCHEMA_ARTIFACTS = HERE.parent / "src" / "content_schema_artifacts"


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
    return Resource(contents=contents, specification=DRAFT202012)


def create_registry_from_filesystem(schema_dir: Path) -> Registry:
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
        my_registry = my_registry.__rmatmul__(resource)
    return my_registry


def modify_content(resource_content: dict, resolver: Resolver) -> tuple[dict, list]:
    """
    Modify the resource content by replacing referenced paths with corresponding JSON schemas.

    Args:
        resource_content (dict): The content of the resource to be modified.
        resolver (Resolver): Resolver object used to look up referenced paths.

    Returns:
        dict: The modified resource content.
    """
    resolved_uris = []
    if resource_content.get("properties"):
        for key_, value_ in resource_content["properties"].items():
            if isinstance(value_, dict) and "$ref" in value_.keys():
                resource_content["properties"][key_] = resolver.lookup(
                    value_["$ref"]
                ).contents
                resolved_uris.append(value_["$ref"])
    return resource_content, resolved_uris


def create_resource(
    content: dict, specification: Specification = DRAFT202012
) -> Resource:
    """
    Create a resource object from content and specification.
    """
    return Resource.from_contents(contents=content, default_specification=specification)


def update_registry(my_registry: Registry, new_resource: Resource) -> Registry:
    """
    Update a resource in the registry.

    Args:
        my_registry (Registry): The registry to be updated.
        new_resource (Resource): The new resource to be updated.

    Returns:
        Registry: The updated registry with the new resource.
    """
    modified_registry = my_registry.remove(URI(new_resource.id()))
    return modified_registry.with_resource(
        uri=URI(new_resource.id()), resource=new_resource
    )


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
    class_content_dir: Path = CLASS_CONTENT_DIR, relative_to: Path = ROOT
) -> list[URI]:
    """Return the list of URIs of the class content schemas. The URIs are relative to root path"""
    return [
        os.path.join(
            os.path.relpath(class_content_dir, relative_to),
            file.replace(".json", ""),
        )
        for file in os.listdir(class_content_dir)
    ]


def generate_artifacts(
    content_schemas_registry: Registry, schema_uris: list
) -> Registry:
    """The routine to create a registry of the artifacts generated from content schemas."""

    resolved_registry_uris = set()
    # incorporate referenced sub-resources in the resource content
    for schema_uri in schema_uris:
        modified_content, resolved_uris = modify_content(
            content_schemas_registry.contents(schema_uri),
            content_schemas_registry.resolver(),
        )
        resolved_registry_uris.update(resolved_uris)
        modified_resource = create_resource(modified_content)
        updated_registry = update_registry(content_schemas_registry, modified_resource)
    # remove the content of the resolved resources from the registry
    for uri in resolved_registry_uris:
        updated_registry = updated_registry.remove(uri)
    return updated_registry


def main(check: bool = False):
    """The main routine."""
    expected_registry = generate_artifacts(
        create_registry_from_filesystem(CLASS_CONTENT_DIR), get_content_uris()
    )
    if check:
        existing_registry = create_registry_from_filesystem(SCHEMA_ARTIFACTS)
        if compare_registries(existing_registry, expected_registry):
            echo_success("Content schema artifacts are up-to-date")
    else:
        export_registry(expected_registry, SCHEMA_ARTIFACTS)
        echo_success(f"Content schema artifacts are saved to {SCHEMA_ARTIFACTS}")


if __name__ == "__main__":
    run(main)

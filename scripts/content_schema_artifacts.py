import json
import os
from pathlib import Path
from typing import Union

from referencing import Registry, Resource, Specification
from referencing._core import Resolver
from referencing.jsonschema import DRAFT7
from referencing.typing import URI
from script_utils.cli import run

HERE = Path(__file__).parent.resolve()
CONTENT_SCHEMAS_DIR = HERE.parent / "src" / "content_schemas"
SCHEMA_ARTIFACTS_DIR = HERE.parent / "src" / "content_schema_artifacts"


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
    return Resource(contents=contents, specification=DRAFT7)


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
        elif isinstance(value, dict):
            resolve_referenced_schemas(value, resolver, resolved_uris)
    return resource_content, resolved_uris


def create_resource(content: dict, specification: Specification = DRAFT7) -> Resource:
    """
    Create a resource object from content and specification.
    """
    return Resource.from_contents(contents=content, default_specification=specification)


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


def main():
    """The main routine."""
    content_json_schemas_registry = create_registry_from_filesystem(CONTENT_SCHEMAS_DIR)
    resolver = Resolver(
        base_uri=URI(CONTENT_SCHEMAS_DIR),
        registry=content_json_schemas_registry,
    )
    resolved_registry_uris = set()
    # incorporate referenced sub-resources in the resource content
    for schema_name in os.listdir(CONTENT_SCHEMAS_DIR):
        resource = content_json_schemas_registry.contents(
            os.path.join(CONTENT_SCHEMAS_DIR, schema_name.replace(".json", ""))
        )
        modified_content, resolved_uris = resolve_referenced_schemas(resource, resolver)
        resolved_registry_uris.update(resolved_uris)
        modified_resource = create_resource(modified_content)
        updated_registry = modified_resource @ content_json_schemas_registry

    # remove the content of the resolved resources from the registry
    for uri in resolved_registry_uris:
        updated_registry = updated_registry.remove(uri)
    # export updated registry
    export_registry(updated_registry, SCHEMA_ARTIFACTS_DIR)


if __name__ == "__main__":
    run(main)

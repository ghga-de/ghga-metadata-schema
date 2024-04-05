import json
import os
from pathlib import Path

from referencing import Registry, Resource, Specification
from referencing._core import Resolver
from referencing.jsonschema import DRAFT202012
from referencing.typing import URI
from script_utils.cli import run

HERE = Path(__file__).parent.resolve()
SCHEMAS = HERE.parent / "src" / "content_schemas"
SCHEMA_ARTIFACTS = HERE.parent / "src" / "content_schema_artifacts"


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


def update_registry(my_registry: Registry, new_resource: Resource):
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


def main():
    """The main routine."""
    content_json_schemas_registry = create_registry_from_filesystem(SCHEMAS)
    resolver = Resolver(
        base_uri=URI(SCHEMAS),
        registry=content_json_schemas_registry,
    )
    resolved_registry_uris = set()
    # incorporate referenced sub-resources in the resource content
    for schema_name in os.listdir(SCHEMAS):
        resource = content_json_schemas_registry.contents(
            os.path.join(SCHEMAS, schema_name.replace(".json", ""))
        )
        modified_content, resolved_uris = modify_content(resource, resolver)
        resolved_registry_uris.update(resolved_uris)
        modified_resource = create_resource(modified_content)
        updated_registry = update_registry(
            content_json_schemas_registry, modified_resource
        )
    # remove the content of the resolved resources from the registry
    for uri in resolved_registry_uris:
        updated_registry = updated_registry.remove(uri)
    # export updated registry
    export_registry(updated_registry, SCHEMA_ARTIFACTS)


if __name__ == "__main__":
    run(main)

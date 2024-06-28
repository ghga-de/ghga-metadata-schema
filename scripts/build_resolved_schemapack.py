#!/usr/bin/env python3
"""Script to build resolved resolved ghga-metadata-schema  schemapack definition"""

from referencing import Registry, Resource
from referencing._core import Resolver
import yaml
from difflib import unified_diff

from pathlib import Path
import json
from schemapack import dump_schemapack
from schemapack.spec.schemapack import SchemaPack
from script_utils.cli import echo_failure, echo_success


ROOT = Path(__file__).parent.parent.resolve()
UNRESOLVED_SCHEMAPACK_PATH = ROOT / "src" / \
    "ghga_metadata_schema.schemapack.yaml"
RESOLVED_SCHEMA_PATH = ROOT / "build" / \
    "ghga_metadata_schema.resolved.schemapack.yaml"
CONTENT_SCHEMA_DIR = ROOT / "src" / "content_schemas"


class OutdatedSchemapackBuild(Exception):
    """Raised when the schemapack is not up to date with the changes made in schemapack content schemas."""


class ParsingError(Exception):
    """Raised when parsing JSON or YAML data fails."""


class SchemapackDefinitionNotFound(Exception):
    """Raised when reading a schemapack file fails with FileNotFound error"""


def is_equal(existing_schemapack: dict, expected_schemapack: dict) -> bool:
    """Check if the contents of the two dictionaries are equal."""
    if existing_schemapack == expected_schemapack:
        return True
    return False


def print_diff(existing_schemapack: dict, expected_schemapack: dict):
    """Print differences between expected and observed files."""
    echo_failure(
        "Expected schemapack build is different than the one in repository:")
    existing_content = "\n".join(sorted(str(existing_schemapack).split(",")))
    expected_content = "\n".join(sorted(str(expected_schemapack).split(",")))
    for line in unified_diff(
        expected_content.splitlines(keepends=True),
        existing_content.splitlines(keepends=True),
    ):
        print("   ", line.rstrip())


def compare_schemapack_builds(
    existing_schemapack: dict, expected_schemapack: dict
) -> bool:
    """Compare two dictionaries to check if they contain the same schemapack definition."""

    if not is_equal(existing_schemapack, expected_schemapack):
        print_diff(existing_schemapack, expected_schemapack)
        raise OutdatedSchemapackBuild(
            "Schemapack definition is outdated. Run 'build_resolved_schema.py' to update."
        )
    return True


def read_yaml(path: Path):
    """Read data from a YAML file into a dictionary"""
    with path.open("r", encoding="utf-8") as file:
        try:
            data = yaml.safe_load(file)
        except FileNotFoundError:
            raise SchemapackDefinitionNotFound(
                f"Schemapack definition file could not be found at {path}"
            )
        except yaml.YAMLError as error:
            raise ParsingError(
                f"The file at '{path}' could not be parsed.") from error
    return data


def retrieve_from_filesystem(path: Path) -> Resource:
    """
    Retrieve a JSON object as a Resource from a file.
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
    """
    my_registry = Registry()
    for schema_file in schema_dir.rglob("*.json"):
        resource = retrieve_from_filesystem(schema_file)
        my_registry = resource @ my_registry
    return my_registry


def resolve_referenced_schemas(resource_content: dict, resolver: Resolver) -> dict:
    """Modify the resource content by replacing referenced paths with corresponding
    JSON schemas.
    """
    for _key, value in resource_content.items():
        if isinstance(value, dict) and "$ref" in value.keys():
            value.update(resolver.lookup(value["$ref"]).contents)
            del value["$ref"]
        elif isinstance(value, dict):
            resolve_referenced_schemas(value, resolver)
    return resource_content


def create_resolved_registry(content_json_schemas_registry: Registry) -> Registry:
    """Create a registry of the resolved content schemas."""
    for schema_uri in content_json_schemas_registry:
        resolved_content = resolve_referenced_schemas(
            content_json_schemas_registry.contents(schema_uri),
            content_json_schemas_registry.resolver(),
        )
        updated_registry = (
            Resource.from_contents(contents=resolved_content)
            @ content_json_schemas_registry
        )

    return updated_registry


def embed_content_schemas(schemapack_dict: dict, registry: Registry):
    """Embed resolved content-schemas into the schemapack dictionary."""
    for _, value in schemapack_dict["classes"].items():
        value["content"] = registry[value["content"].removesuffix(
            ".json")].contents
    return schemapack_dict


def main(check: bool = False):
    """The main routine."""
    resolved_registry = create_resolved_registry(
        create_registry_from_filesystem(CONTENT_SCHEMA_DIR)
    )
    expected_schemapack_dict = embed_content_schemas(
        read_yaml(UNRESOLVED_SCHEMAPACK_PATH), resolved_registry
    )
    if check:
        existing_schemapack_dict = read_yaml(RESOLVED_SCHEMA_PATH)
        if compare_schemapack_builds(
            existing_schemapack_dict, expected_schemapack_dict
        ):
            echo_success("Schemapack definition is up-to-date")
    else:
        schemapack_def = SchemaPack.model_validate(expected_schemapack_dict)
        dump_schemapack(schemapack_def, path=RESOLVED_SCHEMA_PATH)
        echo_success(
            f"The schemapack definition is saved to {RESOLVED_SCHEMA_PATH}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Update entity relation ship diagrams for LinkML yamls."""

import sys
import os
import subprocess
import difflib
from pathlib import Path

import yaml

try:
    from script_utils.cli import echo_failure, echo_success, run
except ImportError:
    echo_failure = echo_success = print  # type: ignore

    def run(main_fn):
        """Run main function without cli tools (typer)."""
        main_fn(check="--check" in sys.argv[1:])


HERE = Path(__file__).parent.resolve()
SCHEMA_DIR = HERE.parent / "src" / "schema"
SUMMARY_DOC = HERE.parent / "docs" / "entity_relations.md"


def fix_enum_line(line: str):
    """Fix problem with enum line."""

    slot, _, target = line.partition("enum")
    fixed_slot = slot.strip().replace(" ", "_")
    return f"    string {fixed_slot}"


def fix_enum_problems(*, erd_diagram: str) -> str:
    """Names of enum slots are not in snake case causing problems. This fixes that."""

    return "\n".join(
        [
            fix_enum_line(line) if "enum" in line else line
            for line in erd_diagram.splitlines()
        ]
    )


def get_detailed_erd_diagram(*, linkml_yaml: Path) -> str:
    """Get a detailed erd diagram for the provided model.."""

    with subprocess.Popen(
        ["gen-erdiagram", str(linkml_yaml)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as process:
        stdout, stderr = process.communicate()

        if process.wait() != 0:
            raise RuntimeError(
                f"Could not generate erd diagram for model '{linkml_yaml}',"
                + f" the error was: {stderr.decode('utf-8')}"
            )

    erd_diagram = stdout.decode("utf-8")
    return fix_enum_problems(erd_diagram=erd_diagram)


def get_basic_erd_diagram(*, linkml_yaml: Path) -> str:
    """Get a basic erd diagram for the provided model."""

    with subprocess.Popen(
        ["gen-erdiagram", "--exclude-attributes", "--structural", str(linkml_yaml)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as process:
        stdout, stderr = process.communicate()

        if process.wait() != 0:
            raise RuntimeError(
                f"Could not generate erd diagram for model '{linkml_yaml}',"
                + f" the error was: {stderr.decode('utf-8')}"
            )

    return stdout.decode("utf-8")


def get_model_name(*, linkml_yaml: Path) -> str:
    """Extract the name of the specified linkml model."""

    with open(linkml_yaml, "r", encoding="utf-8") as file:
        linkml_dict = yaml.safe_load(file)

    return linkml_dict["name"]


def get_schema_paths() -> list[Path]:
    """Returns a list of paths to the models."""

    paths = [
        SCHEMA_DIR / filename
        for filename in os.listdir(SCHEMA_DIR)
        if filename.endswith(".yaml")
    ]

    return sorted(paths)


def generate_doc(*, linkml_yaml: Path) -> str:
    """Returns a markdown-based erd diagram for the specified linkml yaml."""

    model_name = get_model_name(linkml_yaml=linkml_yaml)
    detailed_erd_diagram = get_detailed_erd_diagram(linkml_yaml=linkml_yaml)
    basic_erd_diagram = get_basic_erd_diagram(linkml_yaml=linkml_yaml)

    return (
        f"## {model_name}\n\n"
        f"### Basic Diagram:\n\n{basic_erd_diagram}\n\n"
        f"### Detailed Diagram:\n\n{detailed_erd_diagram}"
    )


def generate_summary_doc() -> str:
    """Returns a markdown-based doc that contains erd diagrams for all models."""

    linkml_yamls = get_schema_paths()

    docs_per_yaml = [
        generate_doc(linkml_yaml=linkml_yaml) for linkml_yaml in linkml_yamls
    ]

    return "# Entity Relationship Diagrams\n\n" + "\n\n".join(docs_per_yaml)


def write_summary_doc(doc: str) -> None:
    """Write a summary doc to the corresponding markdown file."""

    with open(SUMMARY_DOC, "w", encoding="utf-8") as file:
        file.write(doc)


def read_summary_doc() -> str:
    """Read the summary doc markdown file."""

    with open(SUMMARY_DOC, "r", encoding="utf-8") as file:
        return file.read()


def main(check: bool = False):
    """Update or check the current entity relationship diagram."""

    expected_summary_doc = generate_summary_doc()

    if check:
        observed_summary_doc = read_summary_doc()

        if expected_summary_doc == observed_summary_doc:
            echo_success("Entity relationship diagrams are up to date.")
            return

        print(f"Observed file differs from the expected one:")
        for line in difflib.unified_diff(
            observed_summary_doc.splitlines(keepends=True),
            expected_summary_doc.splitlines(keepends=True),
            fromfile="observed",
            tofile="expected",
        ):
            print("   ", line.rstrip())

        echo_failure("Entity relationship diagrams are not up to date.")
        sys.exit(1)

    write_summary_doc(expected_summary_doc)
    echo_success("Successfully updated the entity relationship diagram.")


if __name__ == "__main__":
    run(main)

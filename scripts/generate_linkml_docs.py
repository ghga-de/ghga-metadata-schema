#!/usr/bin/env python3
"""Script to generate linkml markdown documents"""

from pathlib import Path
import sys
import subprocess
from tempfile import TemporaryDirectory
from typer import run
from linkml.generators.markdowngen import MarkdownGenerator

HERE = Path(__file__).parent.resolve()
LINKML_YAML = HERE.parent / "src" / "schema" / "submission_centric_schema.yaml"
DOCS_DIR = HERE.parent / "docs" / "schema_markdown"


def generate_linkml_markdown(docs_dir):
    """Function to generate markdown documentations of a given schema"""
    return MarkdownGenerator(schema=str(LINKML_YAML), directory_output=True).serialize(
        directory=docs_dir
    )


def compare_folders(expected: str, observed: str):
    """Function to check equality of contents of two folders"""
    try:
        subprocess.run(
            ["diff", "-arq", expected, observed],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return "Schema documents are up to date"
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.stderr)
        sys.exit(1)


def main(check: bool = False):
    """Update or check the current entity relationship diagram."""
    generate_linkml_markdown(DOCS_DIR)

    if check:
        with TemporaryDirectory() as tmpdirname:
            generate_linkml_markdown(tmpdirname)

        compare_folders(str(DOCS_DIR), tmpdirname)


if __name__ == "__main__":
    run(main)

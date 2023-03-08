#!/usr/bin/env python3
"""Script to generate linkml markdown documents"""

from typing import TextIO
from pathlib import Path

from typer import run
from linkml.generators.markdowngen import MarkdownGenerator

HERE = Path(__file__).parent.resolve()
DOCS_DIR = HERE.parent / "docs" / "schema_markdown"


def generate_linkml_markdown(linkml_yaml: TextIO):
    """Function to generate markdown documentations of a given schema"""
    return MarkdownGenerator(schema=linkml_yaml, directory_output=True).serialize(
        directory=DOCS_DIR
    )


def main(linkml_yaml):
    """Main function"""
    generate_linkml_markdown(linkml_yaml)


if __name__ == "__main__":
    run(main)

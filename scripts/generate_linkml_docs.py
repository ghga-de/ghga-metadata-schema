#!/usr/bin/env python3
"""Script to generate linkml markdown documents"""

from pathlib import Path
import sys
import subprocess
from tempfile import TemporaryDirectory
from typer import run
from linkml.generators.markdowngen import MarkdownGenerator
from script_utils.cli import echo_failure, echo_success

HERE = Path(__file__).parent.resolve()
LINKML_YAML = HERE.parent / "src" / "schema" / "submission_centric_schema.yaml"
DOCS_DIR = HERE.parent / "docs" / "schema_markdown"


def generate_linkml_markdown(docs_dir: Path):
    """Function to generate markdown documentations of a given schema"""
    return MarkdownGenerator(schema=str(LINKML_YAML), directory_output=True).serialize(
        directory=docs_dir
    )


class ContentDifference(Exception):
    """Custom exception to raise non-equality of the compared folders"""



def compare_folders(expected: Path, observed: Path):
    """Function to check equality of contents of two folders"""

    with subprocess.Popen(
        ["diff", "-arq", str(expected), str(observed)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    ) as process:
        stdout, _ = process.communicate()

        if process.returncode != 0:
            raise ContentDifference(f"Documentations are outdated. {stdout}")


def main(check: bool = False):
    """Update or check the current documentation folder."""
    if check:
        with TemporaryDirectory() as tmpdirname:
            tmp_docs_dir = Path(tmpdirname)

            generate_linkml_markdown(tmp_docs_dir)

            try:
                compare_folders(DOCS_DIR, tmp_docs_dir)
                echo_success("Documents are up-to-date")
            except ContentDifference:
                echo_failure("Documents are not up-to-date")
                raise
    else:
        generate_linkml_markdown(DOCS_DIR)
        echo_success("Documents are successfully generated.")


if __name__ == "__main__":
    run(main)

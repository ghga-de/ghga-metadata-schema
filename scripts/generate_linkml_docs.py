#!/usr/bin/env python3
"""Script to generate linkml markdown documents"""
from pathlib import Path
from filecmp import dircmp
import shutil
from tempfile import TemporaryDirectory
from typer import run
from linkml.generators.markdowngen import MarkdownGenerator
from script_utils.cli import echo_failure, echo_success

HERE = Path(__file__).parent.resolve()
LINKML_YAML = HERE.parent / "src" / "schema" / "submission_centric_schema.yaml"
DOCS_DIR = HERE.parent / "docs" / "schema_markdown"


def generate_linkml_markdown(docs_dir: Path):
    """Function to generate markdown documentations of a given schema"""
    shutil.rmtree(docs_dir)
    docs_dir.mkdir()
    return MarkdownGenerator(schema=str(LINKML_YAML), directory_output=True).serialize(
        directory=docs_dir
    )


class ContentDifference(RuntimeError):
    """Custom exception to raise non-equality of the compared folders"""


def compare_folders(expected: Path, observed: Path):
    """Function to check equality of contents of two folders"""

    diff = dircmp(expected, observed)
    if diff.diff_files:
        raise ContentDifference(f"Contents do not match for files: {diff.diff_files}")
    if diff.right_only:
        raise ContentDifference(f"Missing files in {observed}: {diff.right_only}")
    if diff.left_only:
        raise ContentDifference(f"Missing files in {expected}: {diff.left_only}")


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

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


def compare_folders(expected: Path, observed: Path):
    """Function to check equality of contents of two folders"""
    try:
        process = subprocess.run(
            ["diff", "-arq", str(expected), str(observed)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return process.returncode, process.stdout
    except subprocess.CalledProcessError as exc:
        return exc.returncode, exc.stdout


def main(check: bool = False):
    """Update or check the current entity relationship diagram."""
    if check:
        with TemporaryDirectory() as tmpdirname:
            generate_linkml_markdown(Path(tmpdirname))

            code, out = compare_folders(DOCS_DIR, Path(tmpdirname))
            if code != 0:
                echo_failure("Checks failed on the linkml schema")
                print(out)
                sys.exit(1)
            else:
                echo_success("All checks passes on the linkml schema")
    else:
        generate_linkml_markdown(DOCS_DIR)
        echo_success("Documents are successfully generated.")


if __name__ == "__main__":
    run(main)

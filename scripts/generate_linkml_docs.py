#!/usr/bin/env python3
"""Script to generate linkml markdown documents"""

import subprocess
from pathlib import Path


HERE = Path(__file__).parent.resolve()
DOCS_DIR = HERE.parent / "docs" / "schema_markdown"
SCHEMA_DIR = HERE.parent / "src" / "schema"


class LinkmlDocumentationError(Exception):
    """Classifying errors under Linter"""


def generate_docs(linkml_yaml: Path, docs_dir: Path):
    """Function to call linkml markdown generator"""
    with subprocess.Popen(
        [
            "gen-markdown",
            "--dir",
            str(docs_dir),
            "--index-file",
            "index.md",
            str(linkml_yaml),
        ],
        stderr=subprocess.PIPE,
    ) as process:
        _, stderr = process.communicate()

        if stderr:
            raise LinkmlDocumentationError(
                f"Linkml documentation error, {stderr.decode('utf-8')}"
            )
if __name__ == "__main__":
    generate_docs("/workspace/src/schema/advance_schema.yaml", DOCS_DIR)

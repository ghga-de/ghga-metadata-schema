#!/usr/bin/env python3

"""Script to employ linkml-linter"""
import subprocess
from pathlib import Path


HERE = Path(__file__).parent.resolve()
LINTER_CONFIG = HERE.parent / ".linkml_linter.yaml"
SCHEMA_DIR = HERE.parent / "src" / "schema"
LINTING_DOC = HERE.parent / "docs" / "linkml_linter.md"


def run_linter(linkml_yaml: Path, report: Path):
    """Function to call linkml-linter"""
    return subprocess.Popen(
        [
            "linkml-lint",
            "--config",
            LINTER_CONFIG,
            "--format",
            "markdown",
            "--output",
            str(report),
            str(linkml_yaml),
        ]
    )


if __name__ == "__main__":
    run_linter(SCHEMA_DIR, LINTING_DOC)

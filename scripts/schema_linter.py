#!/usr/bin/env python3

import subprocess
from pathlib import Path


HERE = Path(__file__).parent.resolve()
LINTER_CONFIG = HERE.parent / "src" / "linter_config.yaml"
SCHEMA_DIR = HERE.parent / "src" / "schema"
LINTING_DOC = HERE.parent / "docs" / "linkml_linter.md"


class LinkmlLinterError(Exception):
    """Classifying errors under Linter"""

    pass


def run_linter(linkml_yaml: Path, report: Path):
    """Function to call linkml-linter"""
    with subprocess.Popen(
        [
            "linkml-lint",
            "--config",
            LINTER_CONFIG,
            "--format",
            "markdown",
            "--output",
            str(report),
            str(linkml_yaml),
        ],
        stderr=subprocess.PIPE,
    ) as process:
        _, stderr = process.communicate()

        if stderr:
            raise LinkmlLinterError(f"Linkml linter error, {stderr.decode('utf-8')}")
    return report


if __name__ == "__main__":
    print(run_linter(SCHEMA_DIR, LINTING_DOC))

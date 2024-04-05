#!/usr/bin/env python3

"""Script to employ linkml-linter"""

import subprocess
from pathlib import Path

from script_utils.cli import echo_failure, echo_success

HERE = Path(__file__).parent.resolve()
LINTER_CONFIG = HERE.parent / ".linkml_linter.yaml"
SCHEMA = HERE.parent / "src" / "schema" / "submission.yaml"


class SchemaLinterError(Exception):
    """Custom exception to raise the errors and the warning of the schema linter"""


def run_linter(schema_yaml: Path):
    """Function to call linkml-linter"""

    with subprocess.Popen(
        [
            "linkml-lint",
            "--config",
            LINTER_CONFIG,
            str(schema_yaml),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    ) as process:
        stdout, _ = process.communicate()
        if process.returncode != 0:
            raise SchemaLinterError(f"Checks failed on the linkml schema. {stdout}")


if __name__ == "__main__":
    try:
        run_linter(SCHEMA)
        echo_success("All checks passes on the linkml schema")
    except SchemaLinterError:
        echo_failure("Checks failed on the linkml schema")
        raise

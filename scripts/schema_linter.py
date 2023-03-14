#!/usr/bin/env python3

"""Script to employ linkml-linter"""
import subprocess
import sys
from pathlib import Path
from script_utils.cli import echo_failure, echo_success

HERE = Path(__file__).parent.resolve()
LINTER_CONFIG = HERE.parent / ".linkml_linter.yaml"
SCHEMA_DIR = HERE.parent / "src" / "schema"


def run_linter(schema_yaml: Path):
    """Function to call linkml-linter"""
    try:
        process = subprocess.run(
            [
                "linkml-lint",
                "--config",
                LINTER_CONFIG,
                str(schema_yaml),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            check=True,
        )
        return process.returncode, process.stdout
    except subprocess.CalledProcessError as exc:
        return exc.returncode, exc.stdout


if __name__ == "__main__":
    code, out = run_linter(SCHEMA_DIR)
    if code != 0:
        echo_failure("Checks failed on the linkml schema")
        print(out)
        sys.exit(1)
    else:
        echo_success("All checks passes on the linkml schema")

#!/usr/bin/env python3

"""Script to employ linkml-linter"""
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).parent.resolve()
LINTER_CONFIG = HERE.parent / ".linkml_linter.yaml"
SCHEMA_DIR = HERE.parent / "src" / "schema"


def run_linter(schema_yaml: Path):
    """Function to call linkml-linter"""
    try:
        subprocess.run(
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
    except subprocess.CalledProcessError as exc:
        print(f"Status : FAIL, {exc.returncode}, {exc.stdout}")
        sys.exit(1)


if __name__ == "__main__":
    run_linter(SCHEMA_DIR)

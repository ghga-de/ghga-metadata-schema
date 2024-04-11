#!/usr/bin/env python3

# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script to validate example datapack against the schemapack definition of ghga-metadata-model"""

import sys
from pathlib import Path

from schemapack import load_and_validate
from script_utils.cli import echo_success, run

HERE = Path(__file__).parent.parent.resolve()
SCHEMAPACK_PATH = HERE / "src" / "schema" / "submission.schemapack.yaml"
DATAPACK_PATH = HERE / "example_datapack" / "complete.datapack.yaml"


def validate_datapack():
    """
    function
    """

    try:
        load_and_validate(schemapack_path=SCHEMAPACK_PATH, datapack_path=DATAPACK_PATH)
        echo_success("Valid!")
    except Exception as exc:
        print(exc)
        sys.exit(1)


def main():
    """The main routine."""
    validate_datapack()


if __name__ == "__main__":
    run(main)

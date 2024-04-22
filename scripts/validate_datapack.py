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

"""Script to validate example datapack against the ghga-metadata-schemapack definition"""

from pathlib import Path

from schemapack import load_datapack, load_schemapack
from schemapack._internals.validation import SchemaPackValidator

ROOT = Path(__file__).parent.parent.resolve()
SCHEMAPACK_PATH = ROOT / "src" / "schema" / "submission.schemapack.yaml"
DATAPACK_PATH = ROOT / "example_data" / "complete.datapack.yaml"


my_datapack = load_datapack(DATAPACK_PATH)
my_schemapack = load_schemapack(SCHEMAPACK_PATH)
schemapack_validator = SchemaPackValidator(schemapack=my_schemapack)

schemapack_validator.validate(datapack=my_datapack)

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
#

"""A collection of CLI utilities"""

import typer


def echo_success(message: str):
    """Print a success message."""

    styled_message = typer.style(text=message, fg=typer.colors.GREEN)
    typer.echo(styled_message)


def echo_failure(message: str):
    """Print a failure message."""

    styled_message = typer.style(text=message, fg=typer.colors.RED)
    typer.echo(styled_message)


run = typer.run

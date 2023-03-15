#!/usr/bin/env python3

"""Update entity relation ship diagrams for LinkML yamls.
This script is configured by the yaml located at the CONFIG_FILE path specified in the
following.
"""

import sys
import subprocess
import difflib
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field
import yaml

from script_utils.cli import echo_failure, echo_success, run


HERE = Path(__file__).parent.resolve()
CONFIG_FILE = HERE.parent / ".erdiagrams.yaml"
SCHEMA_DIR = HERE.parent / "src" / "schema"
OUTPUT_FILE = HERE.parent / "docs" / "entity_relations.md"


class ErDiagramJob(BaseModel):
    """Model containing instructions to create an Entity Relationship Diagram."""

    title: str = Field(..., description="The title of the diagram.")
    description: str = Field(..., description="Description of the diagram.")
    model: str = Field(
        ...,
        description="The filename of the model file is targeted.",
    )
    classes: Optional[list[str]] = Field(
        None, description="Classes to include. If not specified all classes are shown."
    )
    tree_root: bool = Field(
        False,
        description="Whether or not to only show classes connected to the tree root.",
    )
    include_attributes: bool = Field(
        False, description="Whether or not to include attributes."
    )


def fix_enum_line(line: str):
    """Fix problem with enum line."""

    slot, _, target = line.partition(" enum ")
    fixed_slot = slot.strip().replace(" ", "_")
    return f"    string {fixed_slot}"


def fix_enum_problems(*, erd_diagram: str) -> str:
    """Names of enum slots are not in snake case causing problems. This fixes that."""

    return "\n".join(
        [
            fix_enum_line(line) if " enum " in line else line
            for line in erd_diagram.splitlines()
        ]
    )


def get_erd_command(*, job: ErDiagramJob) -> list[str]:
    """Get a command line to generate an ERD using the specified job."""

    schema_path = SCHEMA_DIR / job.model

    command = ["gen-erdiagram"]

    if job.tree_root:
        command.append("--structural")

    if not job.include_attributes:
        command.append("--exclude-attributes")

    if job.classes:
        command.append("--max-hops")
        command.append("0")

        for cls in job.classes:
            command.append("--classes")
            command.append(cls)

    command.append(str(schema_path))

    return command


def get_erd_diagram(*, job: ErDiagramJob) -> str:
    """Get a detailed ERD for the provided model.."""

    command = get_erd_command(job=job)

    with subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as process:
        stdout, stderr = process.communicate()

        if process.wait() != 0:
            raise RuntimeError(
                f"Could not generate erd diagram for model '{job.model}',"
                + f" the error was: {stderr.decode('utf-8')}"
            )

    erd_diagram = stdout.decode("utf-8")

    if job.include_attributes:
        erd_diagram = fix_enum_problems(erd_diagram=erd_diagram)

    return erd_diagram


def get_diagram_header(job: ErDiagramJob) -> str:
    """Get a title and description for the specified diagram job in markdown."""

    return f"## {job.title}\n\n{job.description}  \n\n"


def get_annotated_diagram(*, job: ErDiagramJob) -> str:
    """Get an ERD with a title and a description in markdown."""

    diagram_header = get_diagram_header(job=job)
    diagram = get_erd_diagram(job=job)

    return diagram_header + diagram


def generate_doc(*, jobs: list[ErDiagramJob]) -> str:
    """Returns a markdown-based doc that contains all erd diagram."""

    diagrams = [get_annotated_diagram(job=job) for job in jobs]

    return "# Entity Relationship Diagrams\n\n" + "\n\n".join(diagrams)


def write_doc(doc: str) -> None:
    """Write a doc to the corresponding markdown file."""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(doc)


def read_doc() -> str:
    """Read the current markdown file."""

    with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
        return file.read()


def get_jobs() -> list[ErDiagramJob]:
    """Read jobs from the config yaml."""

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        jobs = yaml.safe_load(file)

    return [ErDiagramJob(**job) for job in jobs]


def main(check: bool = False):
    """Update or check the current entity relationship diagram."""

    jobs = get_jobs()
    expected_doc = generate_doc(jobs=jobs)

    if check:
        observed_doc = read_doc()

        if expected_doc == observed_doc:
            echo_success("Entity relationship diagrams are up to date.")
            return

        print(f"Observed file differs from the expected one:")
        for line in difflib.unified_diff(
            expected_doc.splitlines(keepends=True),
            observed_doc.splitlines(keepends=True),
            fromfile="observed",
            tofile="expected",
        ):
            print("   ", line.rstrip())

        echo_failure("Entity relationship diagrams are not up to date.")
        sys.exit(1)

    write_doc(expected_doc)
    echo_success("Successfully updated the entity relationship diagram.")


if __name__ == "__main__":
    run(main)

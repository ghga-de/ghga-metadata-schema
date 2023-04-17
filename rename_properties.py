import typer
from pathlib import Path
import re
import stringcase


def rename_relation_slots(file: Path):
    text = file.read_text()

    matches: list[str] = re.findall(r"\w.*?:\n", text)

    for match in matches:
        corrected = match.replace(" ", "_")
        text = text.replace(match, corrected)

    file.write_text(text)


def snake_to_pascal_case(line: str):
    name = line.strip().replace(":", "")
    corrected_name = stringcase.pascalcase(name)
    return line.replace(name, corrected_name)


def rename_classes(file: Path):
    lines = file.read_text().splitlines()

    corrected_lines = []
    in_class = False
    for line in lines:
        if in_class:
            if "slots:" == line:
                in_class = False
                corrected_line = line
            else:
                if re.match(r"^  [a-zA-Z_]*?:$", line):
                    corrected_line = snake_to_pascal_case(line)
                else:
                    corrected_line = line
        else:
            if "enums:" == line:
                in_class = True
            corrected_line = line
        corrected_lines.append(corrected_line)

    text = "\n".join(corrected_lines)
    file.write_text(text)


def range_name_to_pascal(line: str):
    name = line.replace("range:", "").strip()
    corrected_name = stringcase.pascalcase(name.replace(" ", "_"))

    return line.replace(name, corrected_name)


def rename_ranges(file: Path):
    lines = file.read_text().splitlines()

    corrected_lines = [
        range_name_to_pascal(line) if "range:" in line else line for line in lines
    ]

    text = "\n".join(corrected_lines)
    file.write_text(text)


def is_a_name_to_pascal(line: str):
    name = line.replace("is_a:", "").strip()
    corrected_name = stringcase.pascalcase(name.replace(" ", "_"))

    return line.replace(name, corrected_name)


def rename_is_a(file: Path):
    lines = file.read_text().splitlines()

    corrected_lines = [
        is_a_name_to_pascal(line) if "is_a:" in line else line for line in lines
    ]

    text = "\n".join(corrected_lines)
    file.write_text(text)


if __name__ == "__main__":
    typer.run(rename_is_a)

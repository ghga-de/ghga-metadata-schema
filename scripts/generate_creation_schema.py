#!/usr/bin/env python3
"""
    This script generates a creation schema from the GHGA Metadata Schema.
    The creation schema is then used to generate artifacts that can be used 
    within the GHGA Microservices like the Metadata Repository Service and 
    the Metadata Transpiler Service.
"""
import copy
import typer
import ruamel.yaml
from typing import Dict, Set
from linkml_runtime.utils.schemaview import SchemaView
from ruamel.yaml.comments import CommentedMap


ROOT_CLASS = "named thing"
SLOTS_TO_RELAX: Set = {}
CLASS_SLOTS_TO_RELAX: Set = {
    "create dataset.has study", "create dataset.has experiment", "create dataset.has sample", "create dataset.has analysis"
}
SLOTS_TO_ENFORCE: Set = {"alias"}
CLASS_SLOTS_TO_ENFORCE: Set = {}
SLOTS_TO_REMOVE: Set = {"id", "creation date", "update date"}
CLASS_SLOTS_TO_REMOVE: Set = {}


def get_creation_classes(schemaview: SchemaView) -> Set[str]:
    """
    Get a list of classes for which to generate creation
    specific classes.

    Args:
        schemaview: The SchemaView instance of the schema

    Returns:
        A set of class names

    """
    classes = schemaview.class_descendants(ROOT_CLASS)
    creation_classes = set([x for x in classes if not schemaview.get_class(x).abstract])
    creation_classes.add("submission")
    return creation_classes


def adjust_slot_definitions(
    schema: Dict, creation_classes: Set[str], slots_to_relax, slots_to_enforce
) -> Dict:
    """
    Adjust slot definitions for all relevant slots that references a
    creation class in a given schema.

    Args:
        schema: The incoming schema
        creation_classes: A set of creation classes

    Returns:
        A dictionary of adjust slot definitions

    """
    adjusted_slots = CommentedMap()
    for slot_name, slot_def in schema["slots"].items():
        if slot_name.startswith("has ") and slot_name not in {"has attribute"}:
            new_slot_def = copy.deepcopy(slot_def)
            if "range" in new_slot_def and new_slot_def["range"] in schema["classes"]:
                if new_slot_def["range"] in creation_classes:
                    new_slot_def["range"] = f"create {new_slot_def['range']}"
            adjusted_slots[slot_name] = new_slot_def
        elif slot_name in {"main contact"}:
            new_slot_def = copy.deepcopy(slot_def)
            if "range" in new_slot_def and new_slot_def["range"] in schema["classes"]:
                if new_slot_def["range"] in creation_classes:
                    new_slot_def["range"] = f"create {new_slot_def['range']}"
            adjusted_slots[slot_name] = new_slot_def
        else:
            new_slot_def = copy.deepcopy(slot_def)
            adjusted_slots[slot_name] = new_slot_def
    return adjusted_slots

def adjust_class_definitions(
    schema: Dict, creation_classes: Set[str], slots_to_relax, slots_to_enforce
) -> Dict:
    """
    Adjust class definitions for all relevant classes that are considered
    as creation classes in a given schema.

    Args:
        schema: The incoming schema
        creation_classes: A set of creation classes

    Returns:
        A dictionary of adjust class definitions

    """
    adjusted_classes = CommentedMap()
    for cls_name, cls_def in schema["classes"].items():
        if cls_name in creation_classes:
            new_cls_def = copy.deepcopy(cls_def)
            if "is_a" in new_cls_def and new_cls_def["is_a"] in creation_classes:
                new_cls_def["is_a"] = f"create {new_cls_def['is_a']}"
            adjusted_classes[f"create {cls_name}"] = new_cls_def
            if "slot_usage" in new_cls_def:
                for slot_name, slot_def in new_cls_def["slot_usage"].items():
                    if slot_name in slots_to_relax:
                        if "required" in slot_def and slot_def["required"]:
                            slot_def["required"] = False
                    if slot_name in slots_to_enforce:
                        if "required" in slot_def and not slot_def["required"]:
                            slot_def["required"] = True
                    if "range" in slot_def:
                        if slot_def["range"] in schema["classes"]:
                            if slot_def["range"] in creation_classes:
                                slot_def["range"] = f"create {slot_def['range']}"
        else:
            new_cls_def = copy.deepcopy(cls_def)
            adjusted_classes[cls_name] = new_cls_def
    return adjusted_classes


def relax_slots(schema: Dict, slots: Set) -> None:
    """
    Given a schema and a set of slots, if the slot is
    marked as required in the schema then relax this constraint.

    Args:
        schema: A schema
        slots: A set of slots to relax

    """
    for slot in slots:
        slot_def = schema["slots"][slot]
        slot_def["required"] = False
        if slot == "id":
            slot_def["identifier"] = False


def relax_class_slots(schema: Dict, class_slots: Set) -> None:
    """
    Given a schema and a set of class specific slots, if the slot is
    marked as required for a class in the schema then relax this constraint.

    Args:
        schema: A schema
        slots: A set of class specific slots to relax

    """
    for class_slot in class_slots:
        (cls, slot) = class_slot.split(".")
        if cls and cls in schema["classes"]:
            cls_def = schema["classes"][cls]
            if "slot_usage" in cls_def and slot in cls_def["slot_usage"]:
                slot_def = cls_def["slot_usage"][slot]
                slot_def["required"] = False


def remove_slots(schema: Dict, slots: Set) -> None:
    """
    Given a schema and a set of slots, remove all occurrence
    of ``slots`` from the schema.

    Args:
        schema: A schema
        slots: A set of slots to remove

    """
    for slot in slots:
        if slot in schema["slots"]:
            del schema["slots"][slot]
        for cls_name, cls_def in schema["classes"].items():
            if "slots" in cls_def:
                if slot in cls_def["slots"]:
                    cls_def["slots"].remove(slot)
            if "slot_usage" in cls_def:
                if slot in cls_def["slot_usage"]:
                    del cls_def["slot_usage"][slot]


def remove_class_slots(schema: Dict, class_slots: Set) -> None:
    """
    Given a schema and a set of class specific slots, if the slot is
    is part of the class then remove the slot from the class.

    Args:
        schema: A schema
        slots: A set of class specific slots to remove

    """
    for class_slot in class_slots:
        (cls, slot) = class_slot.split(".")
        if cls and cls in schema["classes"]:
            cls_def = schema["classes"][cls]
            if "slot_usage" in cls_def and slot in cls_def["slot_usage"]:
                del cls_def[slot]
            if "slots" in cls_def and slot in cls_def["slots"]:
                cls_def.remove(slot)


def enforce_slots(schema: Dict, slots: Set) -> None:
    """
    Given a schema and a set of slots, if the slot is
    marked as not required in the schema then enforce the slot
    by marking it as required.

    Args:
        schema: A schema
        slots: A set of slots to relax

    """
    for slot in slots:
        slot_def = schema["slots"][slot]
        slot_def["required"] = True


def enforce_class_slots(schema: Dict, class_slots: Set) -> None:
    """
    Given a schema and a set of class specific slots, mark the slot
    as required for the given class.

    Args:
        schema: A schema
        slots: A set of class specific slots to enforce

    """
    for class_slot in class_slots:
        (cls, slot) = class_slot.split(".")
        if cls and cls in schema["classes"]:
            cls_def = schema["classes"][cls]
            if "slot_usage" in cls_def and slot in cls_def["slot_usage"]:
                slot_def = cls_def[slot]
                slot_def["required"] = True


def parse_schema(
    schema: Dict, schemaview: SchemaView, creation_classes, slots_to_relax, slots_to_enforce
) -> Dict:
    """
    Parse a given schema and generate a new schema with
    constraints that are relaxed and adjusted.

    Args:
        schema: The incoming schema as a dictionary
        schemaview: The SchemaView instance of the incoming schema
        creation_classes: A set of creation classes

    Returns:
        A new schema derived from the incoming schema

    """
    new_schema = CommentedMap()
    for k, v in schema.items():
        if k not in {"classes", "slots"}:
            new_schema[k] = v
    new_schema["comments"] = (
        f"This schema was autogenerated from"
        + f" the GHGA Metadata Schema {schema['version']} and is"
        + " intended solely for consumption by GHGA microservices."
    )
    new_schema["slots"] = adjust_slot_definitions(
        schema, creation_classes, slots_to_relax, slots_to_enforce
    )
    new_schema["classes"] = adjust_class_definitions(
        schema, creation_classes, slots_to_relax, slots_to_enforce
    )
    return new_schema


def main(schema_yaml: str = None, output: str = None):
    yaml = ruamel.yaml.YAML()
    schema = yaml.load(open(schema_yaml, "r"))
    schemaview = SchemaView(schema=schema_yaml)
    creation_classes = get_creation_classes(schemaview)
    if not output:
        output = "new-schema.yaml"

    new_schema = parse_schema(
        schema, schemaview, creation_classes, SLOTS_TO_RELAX, SLOTS_TO_ENFORCE
    )
    if SLOTS_TO_RELAX:
        relax_slots(new_schema, SLOTS_TO_RELAX)
    if CLASS_SLOTS_TO_RELAX:
        relax_class_slots(new_schema, CLASS_SLOTS_TO_RELAX)
    if SLOTS_TO_ENFORCE:
        enforce_slots(new_schema, SLOTS_TO_ENFORCE)
    if CLASS_SLOTS_TO_ENFORCE:
        enforce_class_slots(new_schema, CLASS_SLOTS_TO_ENFORCE)
    if SLOTS_TO_REMOVE:
        remove_slots(new_schema, SLOTS_TO_REMOVE)
    if CLASS_SLOTS_TO_REMOVE:
        remove_class_slots(new_schema, CLASS_SLOTS_TO_REMOVE)

    yaml.dump(new_schema, open(output, 'w'))
    print(
        f"Total classes: {len(schema['classes'])} (original) vs {len(new_schema['classes'])} (new)"
    )
    print(f"Total slots: {len(schema['slots'])} (original) vs {len(new_schema['slots'])} (new)")
    print(f"Total enums: {len(schema['enums'])} (original) vs {len(new_schema['enums'])} (new)")


if __name__ == "__main__":
    typer.run(main)

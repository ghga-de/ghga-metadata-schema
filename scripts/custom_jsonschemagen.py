import click
import jsonasobj
from ast import ClassDef
from typing import Optional, TextIO, Union
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinition
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.utils.formatutils import camelcase, underscore
from linkml.utils.generator import shared_arguments


NON_REFERENCE_SLOTS = {"has attribute", "has parameter", "has data use condition"}


class CustomJsonSchemaGenerator(JsonSchemaGenerator):
    """
    CustomJsonSchemaGenerator extends JsonSchemaGenerator and adds the ability
    to make references slots more permissible.

    This generator was written to get across the limitation of not
    being able to express a slot to be both inlined and not inlined.

    Note: This is a temporary solution until https://github.com/linkml/linkml/issues/664
    is resolved.
    """

    def __init__(
        self,
        schema: Union[str, TextIO, SchemaDefinition],
        top_class: Optional[str] = None,
        **kwargs
    ) -> None:
        super().__init__(schema=schema, top_class=top_class, **kwargs)
        self.reference_slots = set()
        for slot in self.schema.slots:
            slot_alias_name = self.aliased_slot_name(slot)
            if (
                slot_alias_name.startswith("has ") or slot_alias_name == "main contact"
            ) and slot_alias_name not in NON_REFERENCE_SLOTS:
                self.reference_slots.add(slot_alias_name)

    def visit_class_slot(self, cls: ClassDef, aliased_slot_name: str, slot: SlotDefinition) -> None:
        """
        Visit a class' slot.
        """
        super().visit_class_slot(cls, aliased_slot_name, slot)
        prop = self.clsobj.properties[underscore(aliased_slot_name)]
        if aliased_slot_name in self.reference_slots:
            if "type" in prop:
                if prop["type"] == "array":
                    self.fix_multivalued_slot(prop)
                else:
                    self.fix_singlevalued_slot(prop)
            else:
                self.fix_singlevalued_slot(prop)

        if (self.topCls is not None and camelcase(self.topCls) == camelcase(cls.name)) or (
            self.topCls is None and cls.tree_root
        ):
            self.schemaobj.properties[underscore(aliased_slot_name)] = prop

    def fix_singlevalued_slot(self, prop: jsonasobj.JsonObj) -> None:
        """
        Fix single-valued slot, whose range is a class, by changing its JSON Schema
        representation to include one of ref and string.
        """
        if "$ref" in prop:
            one_of_directive = [{"$ref": prop["$ref"]}]
            one_of_directive.append({"type": "string"})
            del prop["$ref"]
            prop["oneOf"] = one_of_directive
        elif "oneOf" in prop:
            one_of_directive = prop["oneOf"]
            one_of_directive.append({"type": "string"})

    def fix_multivalued_slot(self, prop: jsonasobj.JsonObj) -> None:
        """
        Fix multi-valued slot, whose range is a class, by changing its JSON Schema
        representation to include one of ref and string.
        """
        items = prop["items"]
        one_of_directive = [{"type": "string"}]
        if "$ref" in items:
            one_of_directive.append({"$ref": items["$ref"]})
            del items["$ref"]
            items["oneOf"] = one_of_directive
            prop["items"] = items
        elif "oneOf" in items:
            one_of_directive = items["oneOf"]
            one_of_directive.append({"type": "string"})


@shared_arguments(CustomJsonSchemaGenerator)
@click.command()
@click.option(
    "-i",
    "--inline",
    is_flag=True,
    help="""
Generate references to types rather than inlining them.
Note that declaring a slot as inlined: true will always inline the class
""",
)
@click.option(
    "-t",
    "--top-class",
    help="""
Top level class; slots of this class will become top level properties in the json-schema
""",
)
@click.option(
    "--not-closed/--closed",
    default=True,
    show_default=True,
    help="""
Set additionalProperties=False if closed otherwise true if not closed at the global level
""",
)
@click.option(
    "--include-range-class-descendants/--no-range-class-descendants",
    default=False,
    show_default=False,
    help="""
When handling range constraints, include all descendants of the range class instead of just the range class
""",
)
def cli(yamlfile, **kwargs):
    """Generate JSON Schema representation of a LinkML model (Modified for GHGA Metadata Schema)"""
    print(CustomJsonSchemaGenerator(yamlfile, **kwargs).serialize(**kwargs))


if __name__ == "__main__":
    cli()

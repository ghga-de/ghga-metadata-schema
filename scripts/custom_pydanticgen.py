import click
from copy import deepcopy
from typing import TextIO, Union
from jinja2 import Template
from linkml.generators.pydanticgen import PydanticGenerator, default_template, _get_pyrange
from linkml_runtime.linkml_model.meta import SchemaDefinition, ClassDefinition, Annotation
from linkml.utils.generator import shared_arguments
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.utils.formatutils import camelcase, underscore


NON_REFERENCE_SLOTS = {"has attribute", "has parameter", "has data use condition"}


class CustomPydanticGenerator(PydanticGenerator):
    """
    CustomPydanticGenerator extends PydanticGenerator and adds the ability
    to make references slots more permissible.

    This generator was written to get across the limitation of not
    being able to express a slot to be both inlined and not inlined.

    Note: This is a temporary solution until https://github.com/linkml/linkml/issues/664
    is resolved.
    """

    valid_formats = PydanticGenerator.valid_formats

    def __init__(
        self,
        schema: Union[str, TextIO, SchemaDefinition],
        template_file: str = None,
        allow_extra=False,
        format: str = valid_formats[0],
        genmeta: bool = False,
        gen_classvars: bool = True,
        gen_slots: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(
            schema=schema,
            template_file=template_file,
            allow_extra=allow_extra,
            format=format,
            genmeta=genmeta,
            gen_classvars=gen_classvars,
            gen_slots=gen_slots,
            **kwargs,
        )
        self.reference_slots = set()
        for slot in self.schema.slots:
            slot_alias_name = self.aliased_slot_name(slot)
            if (
                slot_alias_name.startswith("has ") or slot_alias_name == "main contact"
            ) and (slot_alias_name not in NON_REFERENCE_SLOTS):
                self.reference_slots.add(underscore(slot_alias_name))

    def serialize(self) -> str:
        """
        Serialize the schema to Pydantic models.

        The serialization is near identical to `PydanticGenerator.serialize`
        except for the following:
            - slots that are reference slots are made more permissible

        """
        sv = self.schemaview
        if self.template_file is not None:
            with open(self.template_file) as template_file:
                template_obj = Template(template_file.read())
        else:
            template_obj = Template(default_template)
        sv: SchemaView
        sv = self.schemaview
        schema = sv.schema
        pyschema = SchemaDefinition(
            id=schema.id, name=schema.name, description=schema.description.replace('"', '\\"')
        )
        enums = self.generate_enums(sv.all_enums())
        sorted_classes = self.sort_classes(list(sv.all_classes().values()))
        sorted_classes = [c for c in sorted_classes if c.class_uri != "linkml:Any"]
        for class_original in sorted_classes:
            class_def: ClassDefinition
            class_def = deepcopy(class_original)
            class_name = class_original.name
            class_def.name = camelcase(class_original.name)
            if class_def.is_a:
                class_def.is_a = camelcase(class_def.is_a)
            class_def.mixins = [camelcase(p) for p in class_def.mixins]
            if class_def.description:
                class_def.description = class_def.description.replace('"', '\\"')
            pyschema.classes[class_def.name] = class_def
            for attribute in list(class_def.attributes.keys()):
                del class_def.attributes[attribute]
            for sn in sv.class_slots(class_name):
                s = deepcopy(sv.induced_slot(sn, class_name))
                s.name = underscore(s.name)
                if s.description:
                    s.description = s.description.replace('"', '\\"')
                class_def.attributes[s.name] = s
                collection_key = None
                if s.range in sv.all_classes():
                    range_cls = sv.get_class(s.range)
                    if range_cls.class_uri == "linkml:Any":
                        pyrange = "Any"
                    elif s.inlined or sv.get_identifier_slot(range_cls.name) is None:
                        pyrange = f"{camelcase(s.range)}"
                        if (
                            sv.get_identifier_slot(range_cls.name) is not None
                            and not s.inlined_as_list
                        ):
                            collection_type = "str"
                    else:
                        pyrange = "str"
                elif s.range in sv.all_enums():
                    pyrange = f"{camelcase(s.range)}"
                elif s.range in sv.all_types():
                    t = sv.get_type(s.range)
                    pyrange = _get_pyrange(t, sv)
                elif s.range is None:
                    pyrange = "str"
                else:
                    raise Exception(f"range: {s.range}")
                if s.multivalued:
                    if collection_key is None:
                        pyrange = f"List[{pyrange}]"
                    else:
                        pyrange = f"Dict[{collection_key}, {pyrange}]"

                # Making reference slots more permissible
                if s.name in self.reference_slots:
                    if ("[str]" not in pyrange) and (pyrange != "str"):
                        pyrange = f"Union[{pyrange}, str]"

                if not s.required:
                    pyrange = f"Optional[{pyrange}]"
                ann = Annotation("python_range", pyrange)
                s.annotations[ann.tag] = ann
        code = template_obj.render(
            schema=pyschema,
            underscore=underscore,
            enums=enums,
            allow_extra=self.allow_extra,
            metamodel_version=self.schema.metamodel_version,
            version=self.schema.version,
        )
        return code


@shared_arguments(CustomPydanticGenerator)
@click.option("--template_file", help="Optional jinja2 template to use for class generation")
@click.command()
def cli(
    yamlfile,
    template_file=None,
    head=True,
    emit_metadata=False,
    genmeta=False,
    classvars=True,
    slots=True,
    **args,
):
    """Generate pydantic classes to represent a LinkML model"""
    gen = CustomPydanticGenerator(
        yamlfile,
        template_file=template_file,
        emit_metadata=head,
        genmeta=genmeta,
        gen_classvars=classvars,
        gen_slots=slots,
        **args,
    )
    print(gen.serialize())


if __name__ == "__main__":
    cli()

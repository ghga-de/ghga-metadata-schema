import click
from ghga_metadata_utils.generators.pydanticgen import GhgaPydanticGenerator
from linkml.utils.generator import shared_arguments


@shared_arguments(GhgaPydanticGenerator)
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
    gen = GhgaPydanticGenerator(
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

import click
from ghga_metadata_utils.generators.jsonschemagen import GhgaJsonSchemaGenerator
from linkml.utils.generator import shared_arguments


@shared_arguments(GhgaJsonSchemaGenerator)
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
    print(GhgaJsonSchemaGenerator(yamlfile, **kwargs).serialize(**kwargs))


if __name__ == "__main__":
    cli()

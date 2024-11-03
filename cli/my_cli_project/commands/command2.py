import click
from my_cli_project.services import service2

@click.command()
@click.argument('input')
def command(input):
    """Another command to process the input."""
    result = service2.process_input(input)
    click.echo(f"Another processed result: {result}")

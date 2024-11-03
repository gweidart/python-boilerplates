import click
from my_cli_project.services import service1

@click.command()
@click.argument('input')
def command(input):
    """Process the input."""
    result = service1.process_input(input)
    click.echo(f"Processed result: {result}")

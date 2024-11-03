import click
from my_cli_project.commands import command1, command2

@click.group()
def cli():
    """A simple CLI application."""
    pass

cli.add_command(command1.command)
cli.add_command(command2.command)

if __name__ == '__main__':
    cli()

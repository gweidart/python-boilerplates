import pytest
from click.testing import CliRunner
from my_cli_project.cli import cli

def test_command2():
    runner = CliRunner()
    result = runner.invoke(cli, ['command2', 'TEST'])
    assert result.exit_code == 0
    assert 'Another processed result: test' in result.output

import pytest
from click.testing import CliRunner
from my_cli_project.cli import cli

def test_command1():
    runner = CliRunner()
    result = runner.invoke(cli, ['command1', 'test'])
    assert result.exit_code == 0
    assert 'Processed result: TEST' in result.output

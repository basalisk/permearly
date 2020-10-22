import click.testing

from permearly import cli


def test_main_exits_cleanly():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0

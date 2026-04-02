import pytest
from click.testing import CliRunner
from community_sync import cli


def test_report_requires_org():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["report"])
    assert result.exit_code != 0


def test_summary_requires_repo():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["summary"])
    assert result.exit_code != 0

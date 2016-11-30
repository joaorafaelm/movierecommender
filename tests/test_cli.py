# coding=utf-8
import pytest
from click.testing import CliRunner
from movie_recommender import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 2


def test_cli_with_data(runner):
    result = runner.invoke(cli.main, ['tests/sample.json'])
    assert result.exit_code == 2


def test_cli_with_movies(runner):
    result = runner.invoke(cli.main, ['tests/sample.json', '1'])
    assert result.exit_code == 0
    assert not result.exception
    assert len(result.output.strip().split('\n')) == 3


def test_cli_max_recommendations(runner):
    result = runner.invoke(cli.main, ['tests/sample.json', '1', '--max-recommendations=2'])
    assert result.exit_code == 0
    assert not result.exception
    assert len(result.output.strip().split('\n')) <= 2

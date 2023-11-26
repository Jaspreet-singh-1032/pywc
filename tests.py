from click.testing import CliRunner
from main import main


def test_bytes_count():
    runner = CliRunner()
    result = runner.invoke(main, ["-c", "test.txt"])
    assert result.output.split()[0] == "342190"


def test_lines_count():
    runner = CliRunner()
    result = runner.invoke(main, ["-l", "test.txt"])
    assert result.output.split()[0] == "7145"


def test_words_count():
    runner = CliRunner()
    result = runner.invoke(main, ["-w", "test.txt"])
    assert result.output.split()[0] == "58164"


def test_characters_count():
    runner = CliRunner()
    result = runner.invoke(main, ["-m", "test.txt"])
    assert result.output.split()[0] == "339292"


def test_default_options():
    runner = CliRunner()
    result = runner.invoke(main, ["test.txt"])
    assert "7145 58164 342190" in result.output

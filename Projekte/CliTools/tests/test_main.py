import pytest
from typer import Exit

from cli_tools import __version__
from cli_tools.__main__ import typer_main, version_callback


def test_typer_main_without_arg(capsys):
    typer_main()
    captured = capsys.readouterr()
    assert "Python CLI Tools" in captured.out


def test_typer_version_callback_with_true_arg(capsys):
    with pytest.raises(Exit):
        version_callback(True)
    captured = capsys.readouterr()
    assert captured.out.startswith(f"Python CLI Tools (Version {__version__})")


def test_typer_version_callback_with_false_arg(capsys):
    version_callback(False)
    captured = capsys.readouterr()
    assert captured.out == ""

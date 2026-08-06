"""Basic tests for {{ cookiecutter.project_name }}."""

import pytest

from {{ cookiecutter.package_name }}.main import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    """Ensure main() runs without error and prints output."""
    main()
    captured = capsys.readouterr()
    assert "{{ cookiecutter.project_name }}" in captured.out

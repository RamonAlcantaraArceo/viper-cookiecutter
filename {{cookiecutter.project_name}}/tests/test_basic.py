"""Basic tests for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.main import main


def test_main_runs(capsys: object) -> None:
    """Ensure main() runs without error and prints output."""
    main()
    captured = capsys.readouterr()
    assert "{{ cookiecutter.project_name }}" in captured.out

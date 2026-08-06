# GitHub Copilot Instructions for {{ cookiecutter.project_name }}

This file provides guidance to GitHub Copilot for AI-assisted development in this project.

## Project Overview

- **Package**: `{{ cookiecutter.package_name }}`
- **Language**: Python 3.14
- **Dependency manager**: [uv](https://github.com/astral-sh/uv)
- **Linter/formatter**: [ruff](https://docs.astral.sh/ruff/)
- **Test framework**: [pytest](https://docs.pytest.org/)

## Coding Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) conventions.
- All code is linted and formatted with **ruff** (`line-length = 88`, `target-version = "py314"`).
- Enabled ruff rule sets: `E`, `F`, `I`, `UP`, `B`, `SIM`.
- Use type annotations on all public functions and methods.
- Prefer `pathlib.Path` over `os.path` for file system operations.
- Use f-strings for string formatting.

## Testing Expectations

- All new modules **must** have a corresponding test file under `tests/`.
- Test files must be named `test_<module_name>.py`.
- Use `pytest` fixtures and parametrize where appropriate.
- Aim for meaningful coverage — test behaviour, not implementation details.
- Do not mock unless I/O or external services are involved.

## Adding New Modules

When proposing a new module `src/{{ cookiecutter.package_name }}/foo.py`:

1. Create the module with a docstring describing its purpose.
2. Export public symbols in `src/{{ cookiecutter.package_name }}/__init__.py` if appropriate.
3. Create `tests/test_foo.py` with at least one test per public function.
4. Run `ruff check .` and `ruff format .` before committing.

## Template Structure

This project was generated from the **viper-cookiecutter** template. When extending:

- Keep source code under `src/{{ cookiecutter.package_name }}/`.
- Keep tests under `tests/`.
- Update `pyproject.toml` for new dependencies — use `uv pip install <pkg>` to add them.
- Do not add unrelated tooling or configuration files without discussion.

## CI/CD

{% if cookiecutter.use_github_actions == "yes" -%}
GitHub Actions CI runs on every push and pull request targeting `main`. The pipeline:

1. Sets up Python 3.14.
2. Installs **uv** and project dependencies.
3. Runs **ruff** for linting and format checking.
4. Runs **pytest** for tests.

Ensure all checks pass before merging.
{%- else -%}
No GitHub Actions workflow is configured for this project. Add one manually if needed.
{%- endif %}

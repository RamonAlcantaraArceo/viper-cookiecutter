# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Requirements

- Python 3.14+
- [uv](https://github.com/astral-sh/uv)

## Getting Started

### Create and activate a virtual environment

```bash
uv venv --seed
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
uv sync --all-extras --all-groups
```

To install using pip:

```bash
uv pip install -e ".[dev]"
```

## Running Tests

```bash
pytest
```

## Linting and Formatting

Run the linter:

```bash
ruff check .
```

Auto-fix issues:

```bash
ruff check --fix .
```

Format code:

```bash
ruff format .
```

## Project Structure

```
{{ cookiecutter.project_name }}/
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_basic.py
├── pyproject.toml
└── README.md
```

## Extending the Template

- Add new modules under `src/{{ cookiecutter.package_name }}/`.
- Add corresponding tests under `tests/`.
- Update `pyproject.toml` to add new dependencies under `[project.dependencies]` or `[project.optional-dependencies]`.

## Author

{{ cookiecutter.author_name }} <{{ cookiecutter.email }}>

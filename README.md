# viper-cookiecutter

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python 3.14 projects using **uv**, **pytest**, **ruff**, GitHub Actions CI, and GitHub Copilot configuration out of the box.

## Features

- 🐍 **Python 3.14** — latest language version
- ⚡ **uv** — fast dependency and virtual-environment management
- 🧪 **pytest** — testing with sensible defaults
- 🧹 **ruff** — fast linting and formatting (E, F, I, UP, B, SIM rules)
- 🤖 **GitHub Copilot** — `.github/copilot-instructions.md` pre-configured
- 🚀 **GitHub Actions CI** — optional workflow (push + PR triggers)
- 📦 **src layout** — clean package separation

## Requirements

- Python 3.9+ (to run Cookiecutter itself)
- [Cookiecutter](https://cookiecutter.readthedocs.io/) — `pip install cookiecutter`

## Usage

```bash
cookiecutter https://github.com/RamonAlcantaraArceo/viper-cookiecutter
```

You will be prompted for the following variables:

| Variable             | Default                        | Description                                   |
|----------------------|--------------------------------|-----------------------------------------------|
| `project_name`       | `my-project`                   | Human-readable project name (also directory)  |
| `package_name`       | `my_project`                   | Python package name (underscores)             |
| `description`        | `A short description…`         | One-line project description                  |
| `author_name`        | `Your Name`                    | Author full name                              |
| `email`              | `you@example.com`              | Author email                                  |
| `version`            | `0.1.0`                        | Initial version                               |
| `use_github_actions` | `yes`                          | Whether to include a GitHub Actions workflow  |

## Generated Project Layout

```
my-project/
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       └── ci.yml          # (if use_github_actions == "yes")
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_basic.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Working with a Generated Project

### Set up the environment

```bash
uv venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
uv pip install -e ".[dev]"
```

### Run tests

```bash
pytest
```

### Lint and format

```bash
ruff check .
ruff format .
```

## License

MIT

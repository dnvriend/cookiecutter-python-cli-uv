# {{ cookiecutter.project_name }} - Project Specification

## Goal

{{ cookiecutter.project_description }}

## What is {{ cookiecutter.project_name }}?

`{{ cookiecutter.cli_command }}` is a command-line utility built with modern Python tooling and best practices.

## Technical Requirements

### Runtime

- Python {{ cookiecutter.python_version }}+
{% if cookiecutter.use_mise -%}
- Installable globally with mise
{% endif -%}
- Cross-platform (macOS, Linux, Windows)

### Dependencies

- `click` - CLI framework

### Development Dependencies

- `ruff` - Linting and formatting
- `mypy` - Type checking
- `pytest` - Testing framework

## CLI Arguments

```bash
{{ cookiecutter.cli_command }} [OPTIONS]
```

### Options

- `--help` / `-h` - Show help message
- `--version` - Show version

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.package_name }}/
│   ├── __init__.py
│   ├── cli.py           # Click CLI entry point
│   └── utils.py         # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_utils.py
├── pyproject.toml       # Project configuration
├── README.md            # User documentation
├── CLAUDE.md            # This file
├── Makefile             # Development commands
{% if cookiecutter.license != "Not open source" -%}
├── LICENSE              # {{ cookiecutter.license }} License
{% endif -%}
{% if cookiecutter.use_mise -%}
├── .mise.toml           # mise configuration
{% endif -%}
└── .gitignore
```

## Code Style

- Type hints for all functions
- Docstrings for all public functions
- Follow PEP 8 via ruff
- {{ cookiecutter.line_length }} character line length
- Strict mypy checking

## Development Workflow

```bash
# Install dependencies
make install

# Run linting
make lint

# Format code
make format

# Type check
make typecheck

# Run tests
make test

# Run all checks
make check

# Full pipeline
make pipeline
```

## Installation Methods

### Global installation{% if cookiecutter.use_mise %} with mise{% endif %}

```bash
cd /path/to/{{ cookiecutter.project_slug }}
{% if cookiecutter.use_mise -%}
mise use -g python@{{ cookiecutter.python_version }}
{% endif -%}
uv sync
uv tool install .
```

After installation, `{{ cookiecutter.cli_command }}` command is available globally.

### Local development

```bash
uv sync
uv run {{ cookiecutter.cli_command }} [args]
```

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
- `bandit` - Security linting
- `pip-audit` - Dependency vulnerability scanning
- `gitleaks` - Secret detection (requires separate installation)

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

# Security scanning
make security-bandit       # Python security linting
make security-pip-audit    # Dependency CVE scanning
make security-gitleaks     # Secret detection
make security              # Run all security checks

# Run all checks (includes security)
make check

# Full pipeline (includes security)
make pipeline
```

## Security

The template includes three lightweight security tools:

1. **bandit** - Python code security linting
   - Detects: SQL injection, hardcoded secrets, unsafe functions
   - Speed: ~2-3 seconds

2. **pip-audit** - Dependency vulnerability scanning
   - Detects: Known CVEs in dependencies
   - Speed: ~2-3 seconds

3. **gitleaks** - Secret and API key detection
   - Detects: AWS keys, GitHub tokens, API keys, private keys
   - Speed: ~1 second
   - Requires: `brew install gitleaks` (macOS)

All security checks run automatically in `make check` and `make pipeline`.

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

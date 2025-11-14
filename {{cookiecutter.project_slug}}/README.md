# {{ cookiecutter.project_name }}

[![Python Version](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}+-blue.svg)](https://www.python.org/downloads/)
{% if cookiecutter.license != "Not open source" -%}
[![License: {{ cookiecutter.license }}](https://img.shields.io/badge/License-{{ cookiecutter.license }}-yellow.svg)](https://opensource.org/licenses/{{ cookiecutter.license }})
{% endif -%}
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://github.com/python/mypy)
[![AI Generated](https://img.shields.io/badge/AI-Generated-blueviolet.svg)](https://www.anthropic.com/claude)
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-5A67D8.svg)](https://www.anthropic.com/claude/code)

{{ cookiecutter.project_description }}

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
{% if cookiecutter.license != "Not open source" -%}
- [License](#license)
{% endif -%}
- [Author](#author)

## About

`{{ cookiecutter.cli_command }}` is a Python CLI tool built with modern tooling and best practices.

## Features

- ✅ Type-safe with mypy strict mode
- ✅ Linted with ruff
- ✅ Tested with pytest
- ✅ Modern Python tooling (uv, {% if cookiecutter.use_mise %}mise, {% endif %}click)

## Installation

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Install globally with uv
uv tool install .
```
{% if cookiecutter.use_mise %}
### Install with mise (recommended for development)

```bash
cd {{ cookiecutter.project_slug }}
mise trust
mise install
uv sync
uv tool install .
```
{% endif %}
### Verify installation

```bash
{{ cookiecutter.cli_command }} --version
```

## Usage

### Basic Usage

```bash
# Show help
{{ cookiecutter.cli_command }} --help

# Run the tool
{{ cookiecutter.cli_command }}
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Install dependencies
make install

# Show available commands
make help
```

### Available Make Commands

```bash
make install          # Install dependencies
make format           # Format code with ruff
make lint             # Run linting with ruff
make typecheck        # Run type checking with mypy
make test             # Run tests with pytest
make check            # Run all checks (lint, typecheck, test)
make pipeline         # Run full pipeline (format, lint, typecheck, test, build, install-global)
make build            # Build package
make run ARGS="..."   # Run {{ cookiecutter.cli_command }} locally
make clean            # Remove build artifacts
```

### Project Structure

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.package_name }}/    # Main package
│   ├── __init__.py
│   ├── cli.py          # CLI entry point
│   └── utils.py        # Utility functions
├── tests/              # Test suite
│   ├── __init__.py
│   └── test_utils.py
├── pyproject.toml      # Project configuration
├── Makefile            # Development commands
├── README.md           # This file
{% if cookiecutter.license != "Not open source" -%}
├── LICENSE             # {{ cookiecutter.license }} License
{% endif -%}
└── CLAUDE.md           # Development documentation
```

## Testing

Run the test suite:

```bash
# Run all tests
make test

# Run tests with verbose output
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_utils.py

# Run with coverage
uv run pytest tests/ --cov={{ cookiecutter.package_name }}
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the full pipeline (`make pipeline`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for public functions
- Format code with `ruff`
- Pass all linting and type checks
{% if cookiecutter.license != "Not open source" %}
## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.
{% endif %}
## Author

**{{ cookiecutter.author_name }}**
{% if cookiecutter.github_username %}
- GitHub: [@{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})
{% endif %}
## Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI framework
- Developed with [uv](https://github.com/astral-sh/uv) for fast Python tooling

---

**Generated with AI**

This project was generated using [Claude Code](https://www.anthropic.com/claude/code), an AI-powered development tool by [Anthropic](https://www.anthropic.com/). Claude Code assisted in creating the project structure, implementation, tests, documentation, and development tooling.

Made with ❤️ using Python {{ cookiecutter.python_version }}

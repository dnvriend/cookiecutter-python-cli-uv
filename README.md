# Cookiecutter Python CLI with uv

[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-D4AA00.svg)](https://github.com/cookiecutter/cookiecutter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Generated](https://img.shields.io/badge/AI-Generated-blueviolet.svg)](https://www.anthropic.com/claude)
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-5A67D8.svg)](https://www.anthropic.com/claude/code)

A modern Python CLI project template using **uv**, **mise**, **ruff**, **mypy**, and **pytest**.

## Features

- ✅ **Modern Tooling**: uv for package management, ruff for linting/formatting, mypy for type checking
- ✅ **Testing**: pytest with comprehensive test structure
- ✅ **Development Pipeline**: Makefile with common tasks (lint, test, format, typecheck, pipeline)
- ✅ **Type Safety**: Strict mypy configuration with full type hints
- ✅ **Documentation**: Professional README with badges, comprehensive CLAUDE.md spec
- ✅ **License Options**: MIT, Apache-2.0, BSD-3, GPL-3.0, or proprietary
- ✅ **Git Ready**: Automatic git initialization with initial commit
- ✅ **AI Attribution**: Module docstrings and README credit for AI-generated code
- ✅ **Optional mise**: Python version management with mise (optional)
- ✅ **PyPI Publishing**: GitHub Actions workflow for automated PyPI publishing with trusted publishing
- ✅ **Security Scanning**: bandit, pip-audit, and gitleaks integration

## Requirements

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) or [uvx](https://github.com/astral-sh/uv)
- Python 3.14+ (or your preferred version)

## Quick Start

### Using uvx (Recommended - No Installation)

```bash
uvx cookiecutter gh:dennisvriend/cookiecutter-python-cli-uv
```

### Using cookiecutter

```bash
# Install cookiecutter
pip install cookiecutter

# Or with uv
uv tool install cookiecutter

# Generate project
cookiecutter gh:dennisvriend/cookiecutter-python-cli-uv
```

### From Local Clone

```bash
# Clone the template
git clone https://github.com/dennisvriend/cookiecutter-python-cli-uv.git
cd cookiecutter-python-cli-uv

# Use the template
cookiecutter .
```

## Template Variables

When you run the template, you'll be prompted for these values:

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable project name | "My CLI Tool" |
| `project_slug` | Repository/package name (kebab-case) | Auto-derived from project_name |
| `package_name` | Python package name (snake_case) | Auto-derived from project_slug |
| `cli_command` | CLI command name | Same as project_slug |
| `project_description` | Short project description | "A Python CLI tool" |
| `author_name` | Your full name | "Dennis Vriend" |
| `author_email` | Your email (optional) | "" |
| `github_username` | GitHub username | "dennisvriend" |
| `python_version` | Python version | "3.14" |
| `use_mise` | Use mise for Python management | true |
| `license` | License choice | ["MIT", "Apache-2.0", "BSD-3", "GPL-3.0", "Not open source"] |
| `line_length` | Maximum line length | "100" |
| `version` | Initial version | "0.1.0" |

## Generated Project Structure

```
my-cli-tool/
├── my_cli_tool/              # Main package
│   ├── __init__.py           # Package initialization with version
│   ├── cli.py                # Click-based CLI entry point
│   └── utils.py              # Utility functions
├── tests/                    # Test suite
│   ├── __init__.py
│   └── test_utils.py         # Example tests
├── pyproject.toml            # Project configuration (uv, ruff, mypy)
├── Makefile                  # Development commands
├── README.md                 # Professional documentation with badges
├── LICENSE                   # Chosen license (if not proprietary)
├── CLAUDE.md                 # Project specification
├── .gitignore                # Python/IDE/tooling ignores
└── .mise.toml                # mise config (if use_mise=true)
```

## Using Your Generated Project

After generation:

```bash
# Navigate to project
cd my-cli-tool

# If using mise
mise trust
mise install

# Install dependencies
make install

# Run tests
make test

# Run full pipeline (format, lint, typecheck, test, build, install)
make pipeline

# Install globally
make install-global

# Use your CLI tool
my-cli-tool --help
```

## Available Make Commands

Generated projects include these Makefile targets:

```bash
make install          # Install dependencies with uv
make lint             # Run ruff linting
make format           # Format code with ruff
make typecheck        # Type check with mypy
make test             # Run pytest tests
make check            # Run lint, typecheck, and test
make pipeline         # Full pipeline: format, lint, typecheck, test, build, install-global
make build            # Build package
make clean            # Remove build artifacts
make run ARGS="..."   # Run CLI locally
make install-global   # Install globally with uv tool
make uninstall-global # Uninstall global installation
```

## Example Usage

### Basic CLI Tool

```bash
$ uvx cookiecutter gh:dennisvriend/cookiecutter-python-cli-uv

project_name [My CLI Tool]: File Converter
project_slug [file-converter]:
package_name [file_converter]:
cli_command [file-converter]:
project_description [A Python CLI tool]: Convert files between formats
author_name [Dennis Vriend]: John Doe
# ... continue with prompts

$ cd file-converter
$ make install
$ make test
$ make install-global
$ file-converter --help
```

### With Custom Values

```bash
$ cookiecutter gh:dennisvriend/cookiecutter-python-cli-uv \
    project_name="API Client" \
    author_name="Jane Smith" \
    license="Apache-2.0" \
    python_version="3.13"
```

### Non-Interactive Mode

```bash
$ cookiecutter gh:dennisvriend/cookiecutter-python-cli-uv --no-input
```

## Customization

### After Generation

The generated project is fully yours to customize:

1. **Add Dependencies**: Edit `pyproject.toml` dependencies section
2. **Modify CLI**: Update `cli.py` with your commands using Click decorators
3. **Add Features**: Create new modules in your package
4. **Extend Tests**: Add test files in `tests/` directory
5. **Update Docs**: Modify `README.md` and `CLAUDE.md`

### Template Customization

To customize the template itself:

1. Fork this repository
2. Modify templates in `{{cookiecutter.project_slug}}/`
3. Update `cookiecutter.json` for new variables
4. Test locally: `cookiecutter /path/to/your/fork`

## Philosophy

This template embodies these principles:

- **Modern Python**: Use latest tooling (uv, ruff, mypy)
- **Developer Experience**: Fast commands, clear errors, comprehensive docs
- **Type Safety**: Strict mypy, full type hints
- **Testing**: Easy to test, easy to extend
- **AI Transparency**: Clear attribution for AI-generated code
- **Professional**: Production-ready structure and documentation

## Comparison with Other Templates

| Feature | cookiecutter-python-cli-uv | cookiecutter-pypackage | python-blueprint |
|---------|---------------------------|----------------------|------------------|
| Package Manager | uv ✅ | pip | poetry |
| Version Manager | mise (optional) ✅ | pyenv | pyenv |
| Linter | ruff ✅ | flake8 | ruff |
| Formatter | ruff ✅ | black | ruff |
| Type Checker | mypy ✅ | mypy | mypy |
| CLI Framework | click ✅ | click | click |
| Test Framework | pytest ✅ | pytest | pytest |
| AI Attribution | Yes ✅ | No | No |
| Modern Makefile | Yes ✅ | Yes | Yes |

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test the template:
   ```bash
   cookiecutter . --no-input
   cd my-cli-tool
   make pipeline
   ```
5. Submit a pull request

## License

This template is licensed under the MIT License - see [LICENSE](LICENSE).

Projects generated from this template can use any license you choose during generation.

## Credits

**Created by Dennis Vriend**

- GitHub: [@dennisvriend](https://github.com/dennisvriend)

**Built with AI**

This template was created using [Claude Code](https://www.anthropic.com/claude/code), an AI-powered development tool by [Anthropic](https://www.anthropic.com/).

## Acknowledgments

- Inspired by [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- Built with modern Python tooling: [uv](https://github.com/astral-sh/uv), [ruff](https://github.com/astral-sh/ruff), [mypy](https://github.com/python/mypy)
- CLI framework: [Click](https://click.palletsprojects.com/)
- Version management: [mise](https://mise.jdx.dev/)

---

Made with ❤️ using Python and Claude Code

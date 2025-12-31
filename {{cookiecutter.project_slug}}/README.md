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
- [Multi-Level Verbosity Logging](#multi-level-verbosity-logging)
- [OpenTelemetry Observability](#opentelemetry-observability)
- [Shell Completion](#shell-completion)
- [Development](#development)
- [Testing](#testing)
- [Security](#security)
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
- 📊 Multi-level verbosity logging (-v/-vv/-vvv)
- 📡 OpenTelemetry observability (traces, metrics, logs)
- 🐚 Shell completion for bash, zsh, and fish
- 🔒 Security scanning with bandit, pip-audit, and gitleaks
- ✅ Modern Python tooling (uv, {% if cookiecutter.use_mise %}mise, {% endif %}typer)

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

# Run with verbose output
{{ cookiecutter.cli_command }} -v      # INFO level
{{ cookiecutter.cli_command }} -vv     # DEBUG level
{{ cookiecutter.cli_command }} -vvv    # TRACE level (includes library internals)
```

## Multi-Level Verbosity Logging

The CLI supports progressive verbosity levels for debugging and troubleshooting. All logs output to stderr, keeping stdout clean for data piping.

### Logging Levels

| Flag | Level | Output | Use Case |
|------|-------|--------|----------|
| (none) | WARNING | Errors and warnings only | Production, quiet mode |
| `-v` | INFO | + High-level operations | Normal debugging |
| `-vv` | DEBUG | + Detailed info, full tracebacks | Development, troubleshooting |
| `-vvv` | TRACE | + Library internals | Deep debugging |

### Examples

```bash
# Quiet mode - only errors and warnings
{{ cookiecutter.cli_command }}

# INFO - see operations and progress
{{ cookiecutter.cli_command }} -v
# Output:
# [INFO] {{ cookiecutter.cli_command }} started
# [INFO] {{ cookiecutter.cli_command }} completed

# DEBUG - see detailed information
{{ cookiecutter.cli_command }} -vv
# Output:
# [INFO] {{ cookiecutter.cli_command }} started
# [DEBUG] Running with verbose level: 2
# [INFO] {{ cookiecutter.cli_command }} completed

# TRACE - see library internals (configure in logging_config.py)
{{ cookiecutter.cli_command }} -vvv
```

### Customizing Library Logging

To enable DEBUG logging for third-party libraries at TRACE level (-vvv), edit `{{ cookiecutter.package_name }}/logging_config.py`:

```python
# Configure dependent library loggers at TRACE level (-vvv)
if verbose_count >= 3:
    logging.getLogger("requests").setLevel(logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.DEBUG)
    # Add your project-specific library loggers here
```

## OpenTelemetry Observability

The CLI supports OpenTelemetry for distributed tracing, metrics, and logs. Designed for integration with Grafana stack (Alloy, Tempo, Prometheus).

### Installation

```bash
# Install with telemetry support
pip install {{ cookiecutter.project_slug }}[telemetry]
# or with uv
uv add "{{ cookiecutter.project_slug }}[telemetry]"
```

### Quick Start

```bash
# Enable telemetry via CLI flag
{{ cookiecutter.cli_command }} --telemetry

# Or via environment variable
export OTEL_ENABLED=true
{{ cookiecutter.cli_command }}
```

### Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_ENABLED` | `false` | Enable telemetry |
| `OTEL_SERVICE_NAME` | `{{ cookiecutter.project_slug }}` | Service name in traces |
| `OTEL_EXPORTER_TYPE` | `console` | `console` or `otlp` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:4317` | OTLP endpoint |

### Production Setup (Grafana Alloy)

```bash
export OTEL_ENABLED=true
export OTEL_EXPORTER_TYPE=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://alloy:4317
{{ cookiecutter.cli_command }}
```

### Development Mode

```bash
# Console output with verbose logging
{{ cookiecutter.cli_command }} --telemetry -vv
```

See [CLAUDE.md](CLAUDE.md) for detailed usage patterns and Grafana Alloy configuration.

## Shell Completion

The CLI provides native shell completion for bash, zsh, and fish shells.

### Supported Shells

| Shell | Version Requirement | Status |
|-------|-------------------|--------|
| **Bash** | ≥ 4.4 | ✅ Supported |
| **Zsh** | Any recent version | ✅ Supported |
| **Fish** | ≥ 3.0 | ✅ Supported |
| **PowerShell** | Any version | ❌ Not Supported |

### Installation

#### Quick Setup (Temporary)

```bash
# Bash - active for current session only
eval "$({{ cookiecutter.cli_command }} completion generate bash)"

# Zsh - active for current session only
eval "$({{ cookiecutter.cli_command }} completion generate zsh)"

# Fish - active for current session only
{{ cookiecutter.cli_command }} completion generate fish | source
```

#### Permanent Setup (Recommended)

```bash
# Bash - add to ~/.bashrc
echo 'eval "$({{ cookiecutter.cli_command }} completion generate bash)"' >> ~/.bashrc
source ~/.bashrc

# Zsh - add to ~/.zshrc
echo 'eval "$({{ cookiecutter.cli_command }} completion generate zsh)"' >> ~/.zshrc
source ~/.zshrc

# Fish - save to completions directory
mkdir -p ~/.config/fish/completions
{{ cookiecutter.cli_command }} completion generate fish > ~/.config/fish/completions/{{ cookiecutter.cli_command }}.fish
```

#### File-based Installation (Better Performance)

For better shell startup performance, generate completion scripts to files:

```bash
# Bash
{{ cookiecutter.cli_command }} completion generate bash > ~/.{{ cookiecutter.cli_command }}-complete.bash
echo 'source ~/.{{ cookiecutter.cli_command }}-complete.bash' >> ~/.bashrc

# Zsh
{{ cookiecutter.cli_command }} completion generate zsh > ~/.{{ cookiecutter.cli_command }}-complete.zsh
echo 'source ~/.{{ cookiecutter.cli_command }}-complete.zsh' >> ~/.zshrc

# Fish (automatic loading from completions directory)
mkdir -p ~/.config/fish/completions
{{ cookiecutter.cli_command }} completion generate fish > ~/.config/fish/completions/{{ cookiecutter.cli_command }}.fish
```

### Usage

Once installed, completion works automatically:

```bash
# Tab completion for commands
{{ cookiecutter.cli_command }} <TAB>
# Shows: completion

# Tab completion for options
{{ cookiecutter.cli_command }} --<TAB>
# Shows: --verbose --version --help

# Tab completion for shell types
{{ cookiecutter.cli_command }} completion generate <TAB>
# Shows: bash zsh fish
```

### Getting Help

```bash
# View completion installation instructions
{{ cookiecutter.cli_command }} completion --help
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
make install                 # Install dependencies
make format                  # Format code with ruff
make lint                    # Run linting with ruff
make typecheck               # Run type checking with mypy
make test                    # Run tests with pytest
make security-bandit         # Python security linter
make security-pip-audit      # Dependency vulnerability scanner
make security-gitleaks       # Secret/API key detection
make security                # Run all security checks
make check                   # Run all checks (lint, typecheck, test, security)
make pipeline                # Run full pipeline (format, lint, typecheck, test, security, build, install-global)
make build                   # Build package
make run ARGS="..."          # Run {{ cookiecutter.cli_command }} locally
make clean                   # Remove build artifacts
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

## Security

The project includes lightweight security tools providing 80%+ coverage with fast scan times:

### Security Tools

| Tool | Purpose | Speed | Coverage |
|------|---------|-------|----------|
| **bandit** | Python code security linting | ⚡⚡ Fast | SQL injection, hardcoded secrets, unsafe functions |
| **pip-audit** | Dependency vulnerability scanning | ⚡⚡ Fast | Known CVEs in dependencies |
| **gitleaks** | Secret and API key detection | ⚡⚡⚡ Very Fast | Secrets in code and git history |

### Running Security Scans

```bash
# Run all security checks (~5-8 seconds)
make security

# Or run individually
make security-bandit       # Python security linting
make security-pip-audit    # Dependency CVE scanning
make security-gitleaks     # Secret detection
```

### Prerequisites

gitleaks must be installed separately:

```bash
# macOS
brew install gitleaks

# Linux
# See: https://github.com/gitleaks/gitleaks#installation
```

Security checks run automatically in `make check` and `make pipeline`.

### What's Protected

- ✅ AWS credentials (AKIA*, ASIA*, etc.)
- ✅ GitHub tokens (ghp_*, gho_*, etc.)
- ✅ API keys and secrets
- ✅ Private keys
- ✅ Slack tokens
- ✅ 100+ other secret types

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

- Built with [Typer](https://typer.tiangolo.com/) for CLI framework
- Developed with [uv](https://github.com/astral-sh/uv) for fast Python tooling

---

**Generated with AI**

This project was generated using [Claude Code](https://www.anthropic.com/claude/code), an AI-powered development tool by [Anthropic](https://www.anthropic.com/). Claude Code assisted in creating the project structure, implementation, tests, documentation, and development tooling.

Made with ❤️ using Python {{ cookiecutter.python_version }}

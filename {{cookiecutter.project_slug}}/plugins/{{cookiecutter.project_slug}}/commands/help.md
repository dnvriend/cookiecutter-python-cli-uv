---
description: Show help information for {{cookiecutter.project_slug}}
argument-hint: command
---

Display help information for {{cookiecutter.project_slug}} CLI commands.

## Usage

```bash
# Show general help
{{cookiecutter.project_slug}} --help

# Show command-specific help
{{cookiecutter.project_slug}} COMMAND --help

# Show version
{{cookiecutter.project_slug}} --version
```

## Arguments

- `COMMAND` (optional): Specific command to get help for
- `--help` / `-h`: Show help information
- `--version` / `-v`: Show version information

## Examples

```bash
# General help
{{cookiecutter.project_slug}} --help

# Command help
{{cookiecutter.project_slug}} search --help

# Version information
{{cookiecutter.project_slug}} --version
```

## Output

Displays usage information, available commands, and options.

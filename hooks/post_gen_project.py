#!/usr/bin/env python
"""Post-generation hook for cookiecutter template.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""
import os
import shutil
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove a file if it exists."""
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(full_path):
        os.remove(full_path)
        print(f"  Removed: {filepath}")


def remove_empty_file(filepath: str) -> None:
    """Remove a file if it's empty or only contains whitespace."""
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(full_path):
        with open(full_path, 'r') as f:
            content = f.read().strip()
        if not content:
            os.remove(full_path)
            print(f"  Removed empty: {filepath}")


def init_git() -> None:
    """Initialize git repository."""
    try:
        subprocess.run(['git', 'init', '-b', 'main'], check=True, capture_output=True)
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        subprocess.run(
            ['git', 'commit', '-m', 'Initial commit from cookiecutter-python-cli-uv'],
            check=True,
            capture_output=True
        )
        print("  ✓ Git repository initialized")
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed to initialize git repository: {e}", file=sys.stderr)
    except FileNotFoundError:
        print("  ✗ Git not found. Skipping git initialization.", file=sys.stderr)


def main() -> None:
    """Execute post-generation tasks."""
    print("\n" + "=" * 70)
    print("Post-generation cleanup...")
    print("=" * 70)

    # Remove .mise.toml if not using mise
    if not {{ cookiecutter.use_mise }}:
        remove_file('.mise.toml')

    # Remove LICENSE if not open source
    if "{{ cookiecutter.license }}" == "Not open source":
        remove_file('LICENSE')

    # Remove empty .mise.toml if it exists and is empty
    remove_empty_file('.mise.toml')

    print("\n" + "=" * 70)
    print("Initializing git repository...")
    print("=" * 70)
    init_git()

    print("\n" + "=" * 70)
    print("✓ Project {{ cookiecutter.project_name }} created successfully!")
    print("=" * 70)
    print("\nProject details:")
    print(f"  Name:        {{ cookiecutter.project_name }}")
    print(f"  Slug:        {{ cookiecutter.project_slug }}")
    print(f"  Package:     {{ cookiecutter.package_name }}")
    print(f"  Command:     {{ cookiecutter.cli_command }}")
    print(f"  Python:      {{ cookiecutter.python_version }}")
    print(f"  License:     {{ cookiecutter.license }}")
    print(f"  Author:      {{ cookiecutter.author_name }}")

    print("\n" + "=" * 70)
    print("Next steps:")
    print("=" * 70)
    print(f"  cd {{ cookiecutter.project_slug }}")
    {% if cookiecutter.use_mise -%}
    print("  mise trust")
    print("  mise install")
    {% endif -%}
    print("  make install")
    print("  make test")
    print("  make pipeline")
    print("\nHappy coding! 🚀")
    print("=" * 70)


if __name__ == '__main__':
    main()

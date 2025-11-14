"""CLI entry point for {{ cookiecutter.project_name }}.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import click

from {{ cookiecutter.package_name }}.utils import get_greeting


@click.command()
@click.version_option(version="{{ cookiecutter.version }}")
def main() -> None:
    """{{ cookiecutter.project_description }}"""
    click.echo(get_greeting())


if __name__ == "__main__":
    main()

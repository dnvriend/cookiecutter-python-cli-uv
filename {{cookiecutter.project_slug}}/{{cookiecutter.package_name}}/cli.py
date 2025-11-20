"""CLI entry point for {{ cookiecutter.project_name }}.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import click

from {{ cookiecutter.package_name }}.completion import completion_command
from {{ cookiecutter.package_name }}.logging_config import get_logger, setup_logging
from {{ cookiecutter.package_name }}.utils import get_greeting

logger = get_logger(__name__)


@click.group(invoke_without_command=True)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Enable verbose output (use -v for INFO, -vv for DEBUG, -vvv for TRACE)",
)
@click.version_option(version="{{ cookiecutter.version }}")
@click.pass_context
def main(ctx: click.Context, verbose: int) -> None:
    """{{ cookiecutter.project_description }}"""
    # Setup logging based on verbosity count
    setup_logging(verbose)

    # If no subcommand is provided, run the default behavior
    if ctx.invoked_subcommand is None:
        logger.info("{{ cookiecutter.cli_command }} started")
        logger.debug("Running with verbose level: %d", verbose)

        greeting = get_greeting()
        click.echo(greeting)

        logger.info("{{ cookiecutter.cli_command }} completed")


# Add completion subcommand
main.add_command(completion_command)


if __name__ == "__main__":
    main()

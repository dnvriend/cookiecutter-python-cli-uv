"""CLI entry point for {{ cookiecutter.project_name }}.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import atexit
from typing import Annotated

import typer

from {{ cookiecutter.package_name }}.completion import completion_app
from {{ cookiecutter.package_name }}.logging_config import get_logger, setup_logging
from {{ cookiecutter.package_name }}.telemetry import TelemetryConfig, TelemetryService, traced
from {{ cookiecutter.package_name }}.utils import get_greeting

logger = get_logger(__name__)

app = typer.Typer(invoke_without_command=True)


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        typer.echo("{{ cookiecutter.cli_command }} version {{ cookiecutter.version }}")
        raise typer.Exit()


def _shutdown_telemetry() -> None:
    """Shutdown telemetry on exit."""
    TelemetryService.get_instance().shutdown()


@traced("main")
def _run_main_command(verbose: int) -> None:
    """Execute main command logic with tracing."""
    logger.info("{{ cookiecutter.cli_command }} started")
    logger.debug("Running with verbose level: %d", verbose)

    greeting = get_greeting()
    typer.echo(greeting)

    logger.info("{{ cookiecutter.cli_command }} completed")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: Annotated[
        int,
        typer.Option(
            "--verbose",
            "-v",
            count=True,
            help="Enable verbose output (use -v for INFO, -vv for DEBUG, -vvv for TRACE)",
        ),
    ] = 0,
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit.",
        ),
    ] = None,
    telemetry: Annotated[
        bool,
        typer.Option(
            "--telemetry",
            envvar="OTEL_ENABLED",
            help="Enable OpenTelemetry observability.",
        ),
    ] = False,
) -> None:
    """{{ cookiecutter.project_description }}"""
    setup_logging(verbose)

    # Initialize telemetry
    config = TelemetryConfig.from_env()
    config.enabled = telemetry or config.enabled
    TelemetryService.get_instance().initialize(config)
    atexit.register(_shutdown_telemetry)

    if ctx.invoked_subcommand is None:
        _run_main_command(verbose)


app.add_typer(completion_app, name="completion")


if __name__ == "__main__":
    app()

"""The probullstats package CLI."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from enum import StrEnum, auto

import arrow

from probullstats import __name__ as program_name
from probullstats import __version__ as program_version
from probullstats import logger


class Formats(StrEnum):
    """Output file formats."""

    CSV = auto()
    TSV = auto()
    PSV = auto()
    XSV = auto()
    JSON = auto()


def command_placeholder(args: argparse.Namespace) -> list:
    """A placeholder until the actual command logic is written."""
    logger.info("Fake command handler called.")
    print(f"## {args.command}")  # noqa: T201
    print("Args:", args)  # noqa: T201

    # Commands will return a list of events, bulls, ...
    return []


def write_data(args: argparse.Namespace, data: list) -> int:
    """A placeholder until the actual output logic is written."""
    logger.info("Fake data output handler called.")
    if not data:
        msg = f'The "{args.command}" provided no data to write.'
        logger.error(f"Output Handler: {msg}")
        return 0

    logger.debug("Fake data output handler writing rows (not really).")
    return len(data)


def create_parser() -> argparse.ArgumentParser:
    """Create an input configuration parser.

    Returns:
        argparse.ArgumentParser: An input configuration parser.

    Examples:
        A parser can be used as is, have argument groups added, or have subparsers added.

        >>> parser = create_parser()
        >>> parser.parse_args(["--fail"])
        Namespace(fail=True)
    """
    parser = argparse.ArgumentParser(
        prog=program_name,
        description=(
            "Pull data from the ProBullStats website and collate raw data to create reports or do custom analysis."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s v{program_version}")
    parser.add_argument(
        "--format",
        choices=[fmt.value for fmt in Formats],
        type=Formats,
        default=Formats.CSV,
        help="Output format [default=%(default)s].",
    )
    parser.add_argument(
        "--output",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Write compiled results to file stream.",
    )
    parser.add_argument("-f", "--fail", action="store_true", help="Placeholder until real functionality implemented.")

    subcommand_parsers = parser.add_subparsers(
        help="Data anchor.  Use <cmd> --help for more info.",
        dest="command",
    )

    # To be used with:
    #  https://github.com/iterative/shtab
    # completion_parser = parser.add_subparsers("complete", help="Print shell completion.")

    events_parser = subcommand_parsers.add_parser("events", help="Select one or more events as the data anchor.")
    events_parser.add_argument("--after", type=date.fromisoformat, help="Retrieve events after this date: YYYY-MM-DD.")
    events_parser.add_argument(
        "--before",
        type=date.fromisoformat,
        default=arrow.now().date(),
        help="Retrieve events before this date. [default=%(default)s]",
    )
    events_parser.set_defaults(func=command_placeholder)

    bulls_parser = subcommand_parsers.add_parser("bulls", help="Select one or more events as the data anchor.")
    bulls_parser.set_defaults(func=command_placeholder)

    return parser


def main(args: argparse.Namespace) -> int:
    """Scriptable entrypoint.

    Args:
        args (argparse.Namespace): Parsed script configuration input.

    Returns:
        int: The returncode.  Zero for success, non-zero otherwise.

    Examples:
        >>> parser = create_parser()
        >>> args = parser.parse_args(["--fail"])
        >>> main(args)
        1
    """
    logger.info("Processing data request.")
    if args.fail:
        msg = "The '-f/--fail' switch was set."
        logger.debug(f"Raising exception: {msg}")
        raise RuntimeError(msg)
    # if not args.command:

    logger.debug(f"Invoking {args.command} command.")
    data = args.func(args)
    logger.info(f"Writing data about {args.command}.")
    lines_written = write_data(args, data)
    logger.debug(f"Processing complete - {lines_written} lines written.")

    # Return 1 if lines_written=0; 0 otherwise
    return int(not lines_written)


@logger.catch
def cli() -> None:
    """Main entrypoint for terminal execution."""
    parser = create_parser()
    args = parser.parse_args()

    # Configure log handler
    # logger.enable("probullstats")

    logger.trace("Log level enabled")
    logger.debug("Log level enabled.")
    logger.info("Log level enabled.")
    logger.success("Log level enabled.")
    logger.warning("Log level enabled.")
    logger.error("Log level enabled.")
    logger.critical("Log level enabled.")

    returncode = main(args)

    sys.exit(returncode)

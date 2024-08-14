"""Select one or more events as the anchor point for data collation."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import arrow

from probullstats import logger

if TYPE_CHECKING:
    from argparse import Namespace
    from argparse import _SubParsersAction as SubParser


def execute(args: Namespace) -> list:
    """A placeholder until the actual command logic is written."""
    logger.info(f"Fake {__name__} command handler called.")
    print(f"## {args.command} - {__name__}")  # noqa: T201
    print("Args:", args)  # noqa: T201

    # Commands will return a list of events, bulls, ...
    return []


def add_parser(subcommand_parser: SubParser) -> None:
    """Add command specific parameters to the given parser.

    Args:
        subcommand_parser (SubParser): A SubParser created by ArgumentParser.add_subparsers()
    """
    command = __name__.split(".")[-1]
    events_parser = subcommand_parser.add_parser(command, help=__doc__)
    events_parser.add_argument("--after", type=date.fromisoformat, help="Retrieve events after this date: YYYY-MM-DD.")
    events_parser.add_argument(
        "--before",
        type=date.fromisoformat,
        default=arrow.now().date(),
        help="Retrieve events before this date. [default=%(default)s]",
    )
    events_parser.set_defaults(func=execute)

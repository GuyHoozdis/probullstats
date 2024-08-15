"""Select one or more bulls as the anchor point for data collation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from probullstats import logger, models

if TYPE_CHECKING:
    from argparse import Namespace
    from argparse import _SubParsersAction as SubParser


def execute(args: Namespace) -> list[models.Bull]:
    """A placeholder until the actual command logic is written."""
    logger.info(f"Fake {__name__} command handler called.")
    print(f"## {args.command} - {__name__}")  # noqa: T201
    print("Args:", args)  # noqa: T201

    # Commands will return a list of events, bulls, ...
    return []


def add_parser(subcommand_parser: SubParser) -> None:  # type: ignore[type-arg]
    """Add command specific parameters to the given parser.

    Args:
        subcommand_parser (SubParser): _description_
    """
    command = __name__.split(".")[-1]
    bulls_parser = subcommand_parser.add_parser(command, help=__doc__)
    bulls_parser.add_argument("BullId", nargs="+", type=int, help="An Id defined by ProBullStats.")
    bulls_parser.set_defaults(func=execute)

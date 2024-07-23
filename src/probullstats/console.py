"""The probullstats package CLI."""

import sys

import argparse

from probullstats import __name__ as program_name, __version__ as program_version


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=program_name,
        description="Pull data from the ProBullStats website and collate raw data to create reports or do custom analysis.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s v{program_version}")

    return parser


def main(args: argparse.Namespace) -> int:
    return 0


def cli() -> None:
    parser = create_parser()
    args = parser.parse_args()

    # TODO: Catch unhandled exceptions here
    returncode = main(args)

    sys.exit(returncode)

"""Nox sessions"""

import nox
from nox.sessions import Session


# https://nox.thea.codes/en/stable/config.html#modifying-nox-s-behavior-in-the-noxfile
nox.options.stop_on_first_error = True
nox.options.error_on_external_run = True
# nox.options.sessions = "lint", "mypy", "rtfd", "xdoctests", "testsuite", "acceptance-tests"


SUPPORTED_PYTHON_VERSIONS = ["3.12", "3.11", "3.10", "3.9", "3.8"]
DEFAULT_PYTHON_VERSION = "3.11"
SOURCE_CODE_TARGETS = [
    "src/",
    "tests/suite/",
    "tests/features/steps/",
    "tests/features/environment.py",
    "noxfile.py",
    # "docs/conf.py",
]


# XXX: I wanted to try some things out.  Don't leave this available.
@nox.session(python=DEFAULT_PYTHON_VERSION)
def debug(session: Session) -> None:
    """Static analysis: lint, formatting, and type checking."""
    args = session.posargs
    if len(args) < 1:
        session.skip("You must provide the tool and command line args.")
    supported_tools = ["ruff", "mypy"]
    if args[0] not in supported_tools:
        session.skip(f"{args[0]} is not one of the supported tools: {supported_tools}")

    try:
        index = args.index("--targets")
        _ = args.pop(index)
        args += SOURCE_CODE_TARGETS
    except ValueError:
        pass

    session.log(f"It's running with args: {args}")
    session.run("poetry", "install", "--with=docs", external=True)
    session.run(*args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session: Session) -> None:
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("ruff", "check", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def style(session: Session) -> None:
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("ruff", "format", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session: Session) -> None:
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", external=True)
    session.run("mypy", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_plus(session: Session) -> None:
    """Static analysis: lint, formatting, and type checking."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.debug(args)
    # session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("poetry", "install", "--no-root", "--with=nox", external=True)
    session.run("ruff", "check", *args)
    session.run("ruff", "format", *args)
    session.run("mypy", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def docs(session: Session) -> None:
    """Generate the documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    session.run("poetry", "install", "--no-root", "--only=docs", external=True)
    session.run("sphinx-build", *args)


# @nox.session(python=DEFAULT_PYTHON_VERSION)
# def style(session: Session) -> None:
#     """Format code style."""
#     args = session.posargs or SOURCE_CODE_TARGETS
#     session.run("poetry", "install", "--no-root", "--only=test", external=True)
#     session.run("ruff", "format", *args)


# @nox.session(python=DEFAULT_PYTHON_VERSION)
# def mypy(session: Session) -> None:
#     """Static type checking using mypy."""
#     args = session.posargs or SOURCE_CODE_TARGETS
#     session.run("poetry", "install", "--no-root", "--only=test", external=True)
#     session.run("mypy", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def acceptance(session: Session) -> None:
    """Run acceptance tests."""
    args = session.posargs or ["./tests/features"]
    session.run("poetry", "install", "--only=test", external=True)
    session.run("behave", *args)

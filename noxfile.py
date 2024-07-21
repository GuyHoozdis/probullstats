"""Nox sessions"""

import nox
from nox.sessions import Session


# https://nox.thea.codes/en/stable/config.html#modifying-nox-s-behavior-in-the-noxfile
nox.options.stop_on_first_error = True
nox.options.error_on_external_run = True
# nox.options.sessions = "lint", "mypy", "rtfd", "xdoctests", "testsuite", "acceptance-tests"


DEFAULT_PYTHON_VERSION = "3.11"
SOURCE_CODE_TARGETS = [
    "src/",
    "tests/suite/",
    "tests/features/steps/",
    "tests/features/environment.py",
    "noxfile.py",
    # "docs/conf.py",
]


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session: Session) -> None:
    """Lint using ruff."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("ruff", "check", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def style(session: Session) -> None:
    """Format code style using ruff (w/ configuration compatible to Black defaults)."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("ruff", "format", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session: Session) -> None:
    """Static type checking using mypy."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("mypy", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def acceptance(session: Session) -> None:
    """Static type checking using mypy."""
    args = session.posargs or ["./tests/features"]
    session.run("poetry", "install", "--only=test", external=True)
    session.run("behave", *args)

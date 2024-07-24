"""Nox sessions"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

import nox

if TYPE_CHECKING:
    from nox.sessions import Session


SUPPORTED_PYTHON_VERSIONS = ["3.12", "3.11", "3.10", "3.9"]
DEFAULT_PYTHON_VERSION = os.environ.get("NOXFORCEPYTHON", "3.11")
SOURCE_CODE_TARGETS = [
    "src/",
    "tests/suite/",
    "tests/features/steps/",
    "tests/features/environment.py",
    "noxfile.py",
    # "docs/conf.py",
]


# https://nox.thea.codes/en/stable/config.html#modifying-nox-s-behavior-in-the-noxfile
nox.options.stop_on_first_error = False
nox.options.error_on_external_run = True
nox.options.sessions = (
    "code-quality",
    f"test-suite-{DEFAULT_PYTHON_VERSION}",
    f"acceptance-{DEFAULT_PYTHON_VERSION}",
)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session: Session) -> None:
    """Lint source code."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.log(f"Args: {args}")
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("ruff", "check", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def style(session: Session) -> None:
    """Format code style."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", "--only=test", external=True)
    session.run("ruff", "format", *args)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session: Session) -> None:
    """Static type checking using mypy."""
    args = session.posargs or SOURCE_CODE_TARGETS
    session.run("poetry", "install", "--no-root", external=True)
    session.run("mypy", *args)


@nox.session(name="code-quality", python=DEFAULT_PYTHON_VERSION)
def quality(session: Session) -> None:
    """Execute the lint, style, and mypy sessions."""
    session.notify("lint")
    session.notify("style")
    session.notify("mypy")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def docs(session: Session) -> None:
    """Generate the documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    session.run("poetry", "install", "--no-root", "--only=docs", external=True)
    session.run("sphinx-build", *args)


@nox.session(python=SUPPORTED_PYTHON_VERSIONS)
def acceptance(session: Session) -> None:
    """Run acceptance tests."""
    args = session.posargs or ["./tests/features"]
    session.run("poetry", "install", "--only=test", external=True)
    session.run("behave", *args)


@nox.session(name="test-suite", python=SUPPORTED_PYTHON_VERSIONS)
def suite(session: Session) -> None:
    """Static type checking using mypy."""
    args = session.posargs or ["discover", "./tests/suite"]
    session.run("poetry", "install", "--only=test", external=True)
    session.run("python", "-m", "testtools.run", *args)

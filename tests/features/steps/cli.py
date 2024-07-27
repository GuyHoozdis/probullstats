from __future__ import annotations

import re
import subprocess
from importlib.util import find_spec
from typing import Any

from behave import given, then, when


@given('the "{package}" application is installed')
def step_impl(context: Any, package: str) -> None:
    if not find_spec(package):
        msg = f"The {package} application is not installed or not on PATH."
        raise AssertionError(msg)
    context.package = package


@when('I execute "{script} --version" in a terminal or shell')
def step_impl(context: Any, script: str) -> None:
    context.completed = subprocess.run(args=[script, "--version"], stdout=subprocess.PIPE, check=False)
    context.script = script


@then("its version should be written to stdout")
def step_impl(context: Any) -> None:
    output = context.completed.stdout.decode("utf-8").strip()
    if not output:
        msg = "Nothing was written to stdout."
        raise AssertionError(msg)
    if not re.match(rf"{context.script} v[\d]\.[\d]\.[\d]", output):
        msg = f"{output} did not match expected version output."
        raise AssertionError(msg)


@then("it should indicate success to the executing shell")
def step_impl(context: Any) -> None:
    if context.completed.returncode != 0:
        msg = f"It indicated an error [{context.completed.returncode}]."
        raise AssertionError(msg)

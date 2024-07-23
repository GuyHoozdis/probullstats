# ruff: noqa: F811
import subprocess
import re

from behave import given, when, then


@given('the "ProBullStats" application is installed')
def step_impl(context):
    try:
        import probullstats

        _ = probullstats.__version__
    except ImportError as e:
        raise AssertionError("Is the application installed?") from e


@when('I execute "probullstats --version" in a terminal or shell')
def step_impl(context):
    context.completed = subprocess.run(args=["probullstats", "--version"], stdout=subprocess.PIPE)


@then("its version should be written to stdout")
def step_impl(context):
    output = context.completed.stdout.decode("utf-8").strip()
    assert output, "Nothing was written to stdout."
    assert re.match(r"probullstats v[\d]\.[\d]\.[\d]", output), f"{output} did not match expected version output."


@then("it should indicate success to the executing shell")
def step_impl(context):
    assert 0 == context.completed.returncode, f"It indicated an error [{context.completed.returncode}]."

# ruff: noqa: F811
import subprocess

from behave import given, when, then


@given('the "ProBullStats" application is installed')
def step_impl(context):
    try:
        import probullstats
    except ImportError as e:
        raise AssertionError("Is the application installed?") from e


@when('I execute "probullstats --help" in a terminal or shell')
def step_impl(context):
    context.completed = subprocess.run(args=['probullstats', '--help'], stdout=subprocess.PIPE)


@then("its usage should be written to stdout")
def step_impl(context):
    assert context.completed.stdout, "Nothing was written to stdout"
    context.attach('text/plain', context.completed.stdout)


@then("it should indicate success to the executing shell")
def step_impl(context):
    assert 0 == context.completed.returncode, f"It indicated an error [{context.completed.returncode}]"

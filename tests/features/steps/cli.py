# ruff: noqa: F811
from behave import given, when, then


@given('the "<application>" application is installed')
def step_impl(context):
    raise NotImplementedError(
        'STEP: Given the "<application>" application is installed'
    )


@when('I execute "<application> --help" in a terminal or shell')
def step_impl(context):
    raise NotImplementedError(
        'STEP: When I execute "<application> --help" in a terminal or shell'
    )


@then("I the application's usage is written to stdout")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then I the application's usage is written to stdout"
    )

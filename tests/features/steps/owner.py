from __future__ import annotations

from typing import Any

from behave import given, then, when


def format_exception_message(step: Any) -> str:
    return f"STEP: {step.step_type.capitalize()} {step.name}"


@given("a start date and end date")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@when("I request data about events")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@then("I am returned a list of events that occurred between those dates (inclusive)")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@then("the meta information for each event")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@given("the information that identifies one or more events")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@when("I request data about the bulls at those events")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@then("I am returned a list of events with the bull roster for each event")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@then("the meta information for each bull")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@when("I request data about all the outs for bulls at those events")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@then("I am returned a list of events with the list of outs for each event")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)


@then("the meta information for each out")
def step_impl(context: Any) -> None:
    msg = format_exception_message(context.step)
    raise NotImplementedError(msg)

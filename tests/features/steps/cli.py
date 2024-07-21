from behave import given, when, then


@given(u'the "<application>" application is installed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "<application>" application is installed')


@when(u'I execute "<application> --help" in a terminal or shell')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I execute "<application> --help" in a terminal or shell')


@then(u'I the application\'s usage is written to stdout')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I the application\'s usage is written to stdout')

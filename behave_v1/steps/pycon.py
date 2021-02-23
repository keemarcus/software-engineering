from behave import *

@given(u'we have navigated to python.org')
def step_impl(context):
    pass

@when(u'we search for "{topic}"')
def step_impl(context, topic):
    pass

@then(u'we get at least {number} of responses')
def step_impl(context, number):
    pass

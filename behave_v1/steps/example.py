from behave import *

import random

@given(u'we have loaded a random number generator')
def step_impl(context):
    random.seed()

@when(u'we ask for a random integer between {lower} and {upper}')
def step_impl(context,lower,upper):
    context.i = random.randint(int(lower), int(upper))

@then(u'we get an integer between {lower} and {upper}')
def step_impl(context, lower, upper):
    assert type(context.i) is int
    assert int(lower) <= context.i <= int(upper)

from behave import * 

import random

@given(u'we have loaded a random number generator')
def step_impl(context):
    random.seed()

@when(u'we ask for a random integer')
def step_impl(context):
    context.i = random.randint(0,1000)

@then(u'we get a random integer')
def step_impl(context):
    assert type(context.i) is int

@when(u'we ask for a random integer between {lower} and {upper}')
def step_impl(context, lower, upper):
    lower, upper = int(lower), int(upper)
    context.i = random.randint(lower,upper)

@then(u'we get a random integer beween {lower} and {upper}')
def step_impl(context, lower, upper):
    lower, upper = int(lower), int(upper)
    assert type(context.i) is int
    assert lower <= context.i <= upper

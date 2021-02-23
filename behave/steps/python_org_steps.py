from behave import * 

import requests
from bs4 import BeautifulSoup

@given(u'we have a web site at python.org')
def step_impl(context):
    result = requests.get("http://python.org")
    assert result.status_code == 200 

@when(u'we search for a "{topic}"')
def step_impl(context, topic):
    result = requests.get("https://www.python.org/search/?q=" + topic)
    assert result.status_code == 200 
    context.result = result

@when(u'we parse the resulting page')
def step_impl(context):
    context.page = BeautifulSoup(context.result.text, 'html.parser')

@then(u'we get at least {number} of responses')
def step_impl(context, number):
    number = int(number)
    main_content = context.page.find("section",class_="main-content")
    assert main_content, "Main content section not found"
    list_items = main_content.find_all("li")
    assert len(list_items) >= number

@then(u'the word "{topic}" appears on the page')
def step_impl(context, topic):
    assert topic in context.result.text
    main_content = context.page.find("section",class_="main-content")
    assert main_content, "Main content section not found"


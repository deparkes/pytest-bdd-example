from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.greeter.Greeter import Greeter

scenarios('../features/greeter.feature')


@pytest.fixture
def greeter():
    return Greeter()

@given(parsers.parse('a Greeter'))
def a_new_greeter():
    pass

@when(parsers.parse('I give my name as "{name}"'))
def i_give_my_name_as(greeter, name):
    greeter.my_name(name)

@then(parsers.parse('The greeter says Hello "{name}"'))
def the_greeter_says_hello(greeter, name):
    assert greeter.greet() ==  'Hello '+name
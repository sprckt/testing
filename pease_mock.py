#! /usr/bin/env python

import datetime
import sourcey
from unittest import mock


def add_time_to_simples():
    sourcey.divider("Mock with Functions")
    sourcey_result = sourcey.simples()
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"{dt} >>\t{sourcey_result}"

print(add_time_to_simples())

# Showing how mocks can beget more mocks
@mock.patch('sourcey.simples')
def mock_another_function(mock_replace_simples):
    # This prints out the MagicMock objects that the patch creates
    print(mock_replace_simples)
    print(sourcey.simples)
    sourcey_result = sourcey.simples()
    print(sourcey_result)    
    return

mock_another_function()


## Using mock return value to test how this works
@mock.patch('sourcey.simples')
def mock_with_return_value(mock_replace_simples):
    mock_replace_simples.return_value = "Another one bites the dust"
    sourcey_result = sourcey.simples()
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{dt} >>\t{sourcey_result}")

mock_with_return_value() 


# Using a side effect function to test this operaiton again
def side_effect_function():
    return "Holy Cow Batman"

@mock.patch('sourcey.simples')
def mock_with_side_effect(mock_replace_simples):
    mock_replace_simples.side_effect = side_effect_function
    sourcey_result = sourcey.simples()
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{dt} >>\t{sourcey_result}")

mock_with_side_effect()


####################################################
"""
Using Mocks with Classes now
"""

def use_class():
    inst = sourcey.SourceClass()
    sourcey.divider('Mock with classes')
    print(inst.explode())

use_class()


@mock.patch("sourcey.SourceClass")
def mock_use_class(mock_source_class):
    """
    Mock the entire class imported from Sourcey
    :return:
    """
    print(mock_source_class)
    print(sourcey.SourceClass)
    inst = sourcey.SourceClass()
    print('This creates an instance of the mock - so a new mock (and hence a new id')
    print(inst)
    print(mock_source_class.return_value)

mock_use_class()


@mock.patch("sourcey.SourceClass")
def mock_methods(mock_source_class):
    mock_source_class.return_value.explode.return_value = 'small boom'
    inst = sourcey.SourceClass()
    result = inst.explode()
    print('\nMocking what we get back from methods')
    print('mock_methods(): ' + result)

mock_methods()
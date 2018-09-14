#! /usr/bin/env python

import datetime
import sourcey
from unittest import mock

def add_time_to_simples():
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


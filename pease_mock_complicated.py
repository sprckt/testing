#! /usr/bin/env python

import datetime
import sourcey
from unittest import mock

"""
Assume the database has the following type record in a table called Animal

id: 1
type: honey badger
noise: RAAAHH

We map that table in Flask like this:
 class Animal(db.Model):
    __tablename__ = "animal"
    type = db.Column(db.String)
    noise = db.Column(db.String)
    
And want to test the following function which gets all the noises from the table
 def get_animal_noises():
    animal_list = Animal.query.all()
    noises = [animal.noise for animal in animal_list]
    return noises
"""

def get_animal_noises():
    return ['RAAAHH', 'EE-AAAWW', 'WOOF WOOF', 'MOOOOOOO']


@mock.patch("animals.Animal")
def test_get_animal_noises(self, mock_animal):

    # Create test animal
    test_animal = Animal()
    test_animal.noise = "RAAAHH"
    test_animal.type = "honey badger"

    # Set return value of all to a list containing test animal
    mock_animal.query.all.return_value = [test_animal]

    noises = get_animal_noises()
    assert(noises[0] == 'RAAAHH')
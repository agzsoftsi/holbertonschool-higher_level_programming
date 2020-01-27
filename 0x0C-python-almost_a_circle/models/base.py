#!/usr/bin/python3
"""Define a Base Module."""
import json


class Base:
    """Define a Base class. - Task 1"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance - Task 1."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of list_dictionaries - Task 15"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

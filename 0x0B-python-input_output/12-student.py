#!/usr/bin/python3
"""Module for Task12"""


class Student:
    """Student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to Retrieve specified attributes of a Student."""
        if attrs is None:
            return self.__dict__
        my_attrs = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                my_attrs[key] = val
        return my_attrs

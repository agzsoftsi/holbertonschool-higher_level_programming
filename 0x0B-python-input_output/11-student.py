#!/usr/bin/python3
"""Module for task11"""


class Student:
    """Student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To retrieve a dictionary of a Student."""
        return self.__dict__

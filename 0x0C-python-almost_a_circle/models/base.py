#!/usr/bin/python3
"""Define a Base Module."""


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

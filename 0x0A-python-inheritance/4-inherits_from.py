#!/usr/bin/python3
"""Module to task4."""


def inherits_from(obj, a_class):
    """Return True or false, if object is instance of class inherited."""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False

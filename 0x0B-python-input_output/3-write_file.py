#!/usr/bin/python3
"""Module for Task 3"""


def write_file(filename="", text=""):
    """Write a text in a file."""
    with open(filename, 'w') as f:
        return f.write(str(text))

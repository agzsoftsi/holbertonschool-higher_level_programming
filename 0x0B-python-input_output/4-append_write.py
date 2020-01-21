#!/usr/bin/python3
"""Module for Task4"""


def append_write(filename="", text=""):
    """To append text at the end of a file."""
    with open(filename, 'a') as f:
        return f.write(str(text))

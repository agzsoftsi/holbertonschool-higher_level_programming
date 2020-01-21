#!/usr/bin/python3
"""Mdoule Task 0"""


def read_file(filename=""):
    """To print the content of a text file."""
    with open(filename, 'r') as f:
        print(f.read(), end='')

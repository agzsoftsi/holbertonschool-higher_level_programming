#!/usr/bin/python3
"""Module for Task1 """


def number_of_lines(filename=""):
    """To count the number of lines in a file."""
    con = 0
    with open(filename, 'r') as f:
        for line in f:
            con += 1
    return con

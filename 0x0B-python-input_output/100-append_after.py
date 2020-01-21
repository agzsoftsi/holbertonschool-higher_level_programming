#!/usr/bin/python3
"""Module For Task100"""


def append_after(filename="", search_string="", new_string=""):
    """To append a line of text after line containing a specific string."""
    with open(filename, 'r') as f:
        newtext = f.readlines()

    with open(filename, 'w') as f:
        s = ''
        for line in newtext:
            s += line
            if search_string in line:
                s += new_string
        f.write(s)

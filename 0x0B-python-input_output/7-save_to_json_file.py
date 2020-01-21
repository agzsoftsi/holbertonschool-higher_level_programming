#!/usr/bin/python3
"""Module for Task7"""


def save_to_json_file(my_obj, filename):
    """To write an object to a file using JSON representation."""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

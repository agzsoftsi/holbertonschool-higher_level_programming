#!/usr/bin/python3
"""Module for Task8"""


def load_from_json_file(filename):
    """To create an object from a JSON file."""
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())

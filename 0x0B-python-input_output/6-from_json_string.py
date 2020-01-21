#!/usr/bin/python3
"""Module for Task6"""


def from_json_string(my_str):
    """to return an object represented by a JSON string."""
    import json
    return json.loads(my_str)

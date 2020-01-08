#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as carlos:
        print("Exception: " + carlos.args[0], file=sys.stderr)
        return False

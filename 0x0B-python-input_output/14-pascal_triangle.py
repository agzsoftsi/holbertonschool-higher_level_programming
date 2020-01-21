#!/usr/bin/python3
"""Module Task14.
"""


def pascal_triangle(n):
    """To Return a list of integers tp Pascal's triangle of n."""
    my_list = []
    if n <= 0:
        return my_list
    for con1 in range(1, n + 1):
        value = 1
        temp_list = []
        for con2 in range(1, con1 + 1):
            temp_list.append(str(value))
            value = value * (con1 - con2) // con2
        my_list.append(temp_list)
    return my_list

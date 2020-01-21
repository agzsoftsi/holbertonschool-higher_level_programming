#!/usr/bin/python3
"""Module for Task2."""


def read_lines(filename="", nb_lines=0):
    """To read n lines of a text file and print them."""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        con = 0
        for line in f:
            if con < nb_lines:
                print(line, end='')
            con += 1

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for n1, n2 in a_dictionary.items():
        if n2 == value:
            del a_dictionary[n1]
            return complex_delete(a_dictionary, value)
    return a_dictionary

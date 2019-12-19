#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic2 = {}
    for num in a_dictionary:
        dic2[num] = a_dictionary[num] * 2
    return dic2

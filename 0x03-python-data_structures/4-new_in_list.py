#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newl = my_list.copy()
    if idx < 0 or idx >= len(newl):
        return newl
    newl[idx] = element
    return newl

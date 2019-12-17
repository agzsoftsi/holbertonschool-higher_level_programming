#!/usr/bin/python3
def no_c(my_string):
    new = []
    for n in my_string:
        if n != 'c' and n != 'C':
            new.append(n)
    return ''.join(new)

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxim = my_list[0]
        for n in my_list:
            if n > maxim:
                maxim = n
        return maxim
    else:
        return None

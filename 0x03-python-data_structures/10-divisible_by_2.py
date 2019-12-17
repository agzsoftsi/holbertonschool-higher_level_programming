#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    multiple = []
    for n in my_list:
        if n % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)
    return multiple

#!/usr/bin/python3
def weight_average(my_list=[]):
    suma, weight = 0, 0
    if my_list is None or len(my_list) < 1:
        return 0
    for n in my_list:
        suma += (n[0] * n[1])
    for n in my_list:
        weight += n[1]
    return suma / weight

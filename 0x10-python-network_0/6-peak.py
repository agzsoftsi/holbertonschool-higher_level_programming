#!/usr/bin/python3
""" Task 6 - Function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] <= list_of_integers[mid + 1]:
            low = mid + 1
        elif list_of_integers[mid] <= list_of_integers[mid - 1]:
            high = mid - 1
        elif (list_of_integers[mid] >= list_of_integers[mid + 1] and
              list_of_integers[mid] >= list_of_integers[mid - 1]):
            return list_of_integers[mid]

    return list_of_integers[low]

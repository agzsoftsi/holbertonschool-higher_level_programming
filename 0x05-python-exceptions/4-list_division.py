#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for val in range(list_length):
        try:
            div = my_list_1[val] / my_list_2[val]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            newlist.append(div)
    return newlist

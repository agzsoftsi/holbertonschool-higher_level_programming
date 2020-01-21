#!/usr/bin/python3
"""Module for task9."""


from sys import argv

save_f = __import__('7-save_to_json_file').save_to_json_file
load_f = __import__('8-load_from_json_file').load_from_json_file

name_f = "add_item.json"

try:
    my_list = load_f(name_f)
except FileNotFoundError:
    my_list = []

for n in range(1, len(argv)):
    my_list.append(argv[n])
save_f(my_list, name_f)

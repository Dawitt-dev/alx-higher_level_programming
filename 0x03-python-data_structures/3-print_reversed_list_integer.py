#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        new_idx = len(my_list) - 1
        for i in range(len(my_list)):
            print("{:d}".format(my_list[new_idx]))
            new_idx -= 1

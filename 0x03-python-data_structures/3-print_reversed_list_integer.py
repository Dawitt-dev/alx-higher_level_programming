#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    re_list = my_list[::-1]
    for i in range(len(re_list)):
        print("{:d}".format(re_list[i]))

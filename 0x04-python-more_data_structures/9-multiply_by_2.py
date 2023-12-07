#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new_dic = {}
    for key, value in a_dictionary.items():
        a_new_dic[key] = value * 2
    return a_new_dic

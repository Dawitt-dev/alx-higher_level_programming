#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_dif = []
    for i in set_1:
        if i not in set_2:
            set_dif.append(i)
    for n in set_2:
        if n not in set_1:
            set_dif.append(n)
    return set_dif

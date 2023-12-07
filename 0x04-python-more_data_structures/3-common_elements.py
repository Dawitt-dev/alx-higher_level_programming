#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_com = []
    for i in set_1:
        for item in set_2:
            if item == i:
                set_com.append(item)
    return set_com

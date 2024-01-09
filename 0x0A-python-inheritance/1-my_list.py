#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """class inheriting from a list.


    Args:
        list which will be sorted.
    """
    def print_sorted(self):
        """prints a sorted list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

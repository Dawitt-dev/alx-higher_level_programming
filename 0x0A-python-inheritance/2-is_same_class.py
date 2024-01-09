#!/usr/bin/python3
"""Defining a function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly the same as instance.


    Args:
        obj (a_class): object for checking.
        a_class (type): type of type to be checked.


    Returns:
        True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False

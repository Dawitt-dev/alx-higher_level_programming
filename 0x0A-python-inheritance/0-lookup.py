#!/usr/bin/python3
""" Returns a function lookup """


def lookup(obj):
    """ function that returns a list


    Args:
        obj (class): object


    Returns:
        list object
    """
    return dir(obj)

#!/usr/bin/python3
"""Defines is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it is an instance of a class that inherited from,
    the specified class.

    Args:
    - obj: The object to be checked.
    - a_class: The class to compare with.

    Returns:
    - True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)

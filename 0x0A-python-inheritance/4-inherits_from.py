#!/usr/bin/python3
"""Defines inherits_from"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    from the specified class.

    Args:
    - obj: The object to be checked.
    - a_class: The class to compare with.

    Returns:
    - True if obj is an instance of a class that inherited, False otherwise.
    """
    return issubclass(type(obj), a_class)

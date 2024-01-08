#!/usr/bin/python3
"""
Function Definition: add_integer(a, b=98)
Description: Adds two integers or floats.

Parameters:
    a (int or float): The first value.
    b (int or float, optional): The second value. Defaults to 98.

Raises:
    TypeError: If a or b are not integers or floats.

Returns:
    int: The sum of a and b.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
        a (int or float): The first value.
        b (int or float, optional): The second value. Defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or float")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b


#!/usr/bin/phython3
"""
This module defines a Square class.
"""


class Square:
    """
    The Square is a representation of the square shape.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance on the class.


        Args:
            size (int): represents the size of the square.
        """
        self.__size = size
# 'print(__import__("1-square").__doc__)', prints the module docstring.
# 'print(__import__("0-square").Square.__doc__)', prints the class docstring.
# 'print(__import__("1-square").Square.__init__.__doc__)', prints the method.

#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    The Square is a representation of the square shape.


    Attributes:
        __size (int): The size of the square(private).
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the class.


        Args:
            size (int): represents the size of the square.Default 0.


        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculare and returns the area of the square.

        Returns:
            int: as the area of the square.
        """

        return self.__size ** 2

# 'print(__import__("1-square").__doc__)', prints the module docstring.
# 'print(__import__("0-square").Square.__doc__)', prints the class docstring.
# 'print(__import__("1-square").Square.__init__.__doc__)', prints the method.
# 'print(__import__("3-square").Square.area.__doc__)', print the area method.

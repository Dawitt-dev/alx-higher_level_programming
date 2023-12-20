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
        self.__size = size

    @property
    def size(self):
        """
        Getter for size.

        Returns:
            int: as size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Args:
            value(int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculare and returns the area of the square.

        Returns:
            int: as the area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints thes square.

        If size is equal to 0, empty line is printed.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# 'print(__import__("1-square").__doc__)', prints the module docstring.
# 'print(__import__("0-square").Square.__doc__)', prints the class docstring.
# 'print(__import__("1-square").Square.__init__.__doc__)', prints the method.
# 'print(__import__("4-square").Square.size.__doc__)', prints the property.
# 'print(__import__("4-square").Square.size.__set__.__doc__)',print the setter.
# 'print(__import__("3-square").Square.area.__doc__)', print the area method.
# 'print(__import__("5-square").Square.my_print.__doc__)',print the my_print.

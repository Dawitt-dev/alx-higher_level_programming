#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class that defined a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize an instance of the Rectangle class.


        Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.


        Args:
            value (int): The height value to set.


        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.


        Args:
             value (int): The width value to set.


        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculates the area of the rectangle.


        Returns:
            The current rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            The current rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

# 'print(__import__("0-rectangle").__doc__)', prints the module docstring.
# 'print(__import__("0-rectangle").Rectangle.__doc__)', prints the class docst
# >ring.
# 'print(__import__("0-rectangle").Rectangle.__init__.__doc__)', prints the me
# >thods docstring.

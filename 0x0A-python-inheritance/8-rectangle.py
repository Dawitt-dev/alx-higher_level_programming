#!/usr/bin/python3
"""Defines BaseGeometry"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    It serves as a base class for geometry-related classes.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
        - Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented.")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class, which inherits from BaseGeometry.

    It represents a rectangle with width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with specified width and height.

        Args:
        - width: Width of the rectangle (positive integer).
        - height: Height of the rectangle (positive integer).
        """
        self.__width = width
        self.integer_validator("width", width)

        self.__height = height
        self.integer_validator("height", height)

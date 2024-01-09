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

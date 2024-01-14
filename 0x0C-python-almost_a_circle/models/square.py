#!/usr/bin/python3
"""This module defines the square which inherits from the rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the square class.


    Attributes:
        width (int): width of the square.
        height (int): height of the square.
        x (int): x-axis of the square.
        y (int): y-axis of the square.
        id (int): id-number of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initiates the instance of the square.


        Args:
            size (int): width & height of the square.
            x (int): x-axis of the square.
            y (int): y-axis of the square.
            id (int): id-number of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retreives the size argument"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size argument.


        Args:
            value : size setter.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """The string representation of the square"""
        return (
                f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}"
            )

    def update(self, *args, **kwargs):
        """This public method assigns arguments to each attribute"""
        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representaion of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

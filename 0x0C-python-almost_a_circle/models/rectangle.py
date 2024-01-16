#!/usr/bin/python3
"""Defines the Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """This is a rectangle class, it inherits from Base.


    Attbutes:
        __width: the width of the rectangle.
        __height: the height of the rectangle.
        __x: the x-axis position of the rectangle.
        __y: the y-axis position of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle class.


        Args:
            width: width of the rectangle
            height: Height of the rectangle
            x: the x-axis position of the rectangle.
            y: the y-axis position of the rectangle.
            id: identification number of the rectangle.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.


        Args:
            value (int): The width value set.


        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less or equal to 0.
        """
        self.Positive_IntegerValidater(value, "width")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.


        Args:
            value (int): The height value set.


        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less or equal to 0.
        """
        self.Positive_IntegerValidater(value, "height")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x-axis value of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-axis value of the rectangle.


        Args:
            value: the x-axis value set.


        Raises:
            ValueError: if x is under 0.
        """
        self.Non_Negative_IntegerValidater(value, "x")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y-axis value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-axis value of the rectangle.


        Args:
            value: the x-axis value of the rectangle.


        Raises:
            ValueError: if y is under 0.
        """
        self.Non_Negative_IntegerValidater(value, "y")
        self.__y = value

    def Positive_IntegerValidater(self, value, attribute_name):
        """Checks if values are positive integers or not."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def Non_Negative_IntegerValidater(self, value, attribute_name):
        """Checks if values are non negative integers or not."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def area(self):
        """A public object method that calculate the area of the Rectangle.


        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """A public object method that prints Rectangle instance with char #.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """A method returning the string representation of the rectangle.
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """This method assigns argumments to each attribute"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

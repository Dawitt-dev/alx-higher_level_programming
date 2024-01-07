#!/usr/bin/python3
"""
Defines a class Rectangle.
"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        __width (int): An integer indicating the width of the rectangle object.
        __height (int): An integer indicating the height of the rectangle obj.

        number_of_instances (int): An integer indicating the number of objects

        print_symbol (str): A character used for representing the rectangle in
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize an instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width private attribute.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height private attribute.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

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

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The current rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The current rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character.

        Returns:
            str: The rectangle.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # Remove the last newline character
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Return a string representation of a Rectangle instance
        that is able to recreate a new instance.

        Returns:
            str: The rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when deleting an instance of the class.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the areas of two rectangles.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle larger in area, or rect_1 if are equal.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2

#!/usr/bin/python3
"""Defining the class student"""


class Student:
    """
    Defines students properties.

    Attributes:
        first_name (str): first name of a student.
        last_name (str): last name of a student.
        age (int): age of a student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of a student.


        Args:
            first_name (str): first name of a student.
            last_name (str): last name of a student.
            age (int): age of a student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student


        Returns:
            dict: dictionary representation of a student.
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attr,value in self.__dict__.items():
            if attr in attrs:
                new_dict[attr] = value
        return new_dict

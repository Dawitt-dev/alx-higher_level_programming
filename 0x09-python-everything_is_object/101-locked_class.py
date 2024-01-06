#!/usr/bin/python3
"""A locked class allowing only dynamic creation of the 'first_name' instance
    attribute."""


class LockedClass:
    """A locked class allowing only dynamic creation of the 'first_name'
    instance attribute.
    

    Attributes:
        first_name (str): first name of something.
    """
     __slots__ = ["first_name"]

     def __init__(self, first_name=""):
          """Creates new instances of Locked Class."""

         self.first_name = first_name

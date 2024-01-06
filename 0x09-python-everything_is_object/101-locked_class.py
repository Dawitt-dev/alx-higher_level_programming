#!/usr/bin/python3
"""A locked class allowing only dynamic creation of the 'first_name' instance
    attribute."""


class LockedClass:
    """A locked class allowing only dynamic creation of the 'first_name'
    instance attribute."""
     __slots__ = ["first_name"]

     def __init__(self, first_name=""):
         self.first_name = first_name

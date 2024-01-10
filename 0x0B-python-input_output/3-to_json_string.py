#!/usr/bin/python3
import json
"""Defines the to_json_string function"""


def to_json_string(my_obj):
    """returns the JSON representation of an object.


    Args:
        my_obj (str): the string object to be serialized.
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
"""Defines save_to_json_file funnction"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation


    Args:
        my_obj (str): the string object to be saved
        filename (str): the text file to be add on
    """
    with open(filename, "w", encoding="utf-8") as f:
        j = json.dumps(my_obj)
        return f.write(j)

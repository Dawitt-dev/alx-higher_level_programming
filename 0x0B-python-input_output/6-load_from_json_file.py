#!/usr/bin/python3
"""Defining load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file".


    Args:
        filename (str): file to be loaded from.
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)

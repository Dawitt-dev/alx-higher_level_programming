#!/usr/bin/python3
"""Defining the append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns the number of
    characters added


    Args:
        filename (str): the file to be added on.
        text (str): the text to be added on the file.


    Return:
        the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

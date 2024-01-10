#!/usr/bin/python3
"""Define the function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file  and returns the number of characters
    written.


    Args:
        filename (str): file to be written to.
        text (str): the text to be written to the file.


    Return:
        the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

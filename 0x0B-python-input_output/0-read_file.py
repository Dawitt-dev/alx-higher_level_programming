#!/usr/bin/python3
"""DEfining the function read_file"""


def read_file(filename=""):
    """Read a reads a text file and prints it.


    Args:
        filename (str): name of file to be read.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""Loads, adds and saves arguments in a phyton list"""
import json
import os.path
import sys


# Importing the save_to_json_file and load_from_json_file functions
SaveFile = __import__('5-save_to_json_file').save_to_json_file
LoadFile = __import__('6-load_from_json_file').load_from_json_file


# File path for add_item.json
file_path = 'add_item.json'


# Create an empty list or load existing list from add_item.json
if os.path.exists(file_path):
    my_list = LoadFile(file_path)
else:
    my_list = []


# Add command line arguments to the list
my_list.extend(sys.argv[1:])


# Save the updated list to add_item.json
SaveFile(my_list, file_path)

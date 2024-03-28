#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the \
   URL and displays the body of the response (decoded in utf-8).
"""
from urllib import request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as e:
        print("ERROR code: {}".format(e.code))

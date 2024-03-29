#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the \
    URL and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
        print(req.text)
    except:
        print('Error code: {}'.format(req.status_code))

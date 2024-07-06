#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the
passed URL with email as a parameter, and finally displays body of response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)
    print(response.text)

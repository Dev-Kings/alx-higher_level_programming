#!/usr/bin/python3
"""
Script that receives URL as argument, sends Request to the URL and displays
the value of X-Request-Id variable found in the header of response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))

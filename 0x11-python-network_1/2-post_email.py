#!/usr/bin/python3
"""
Script takes URL and an email, sends a POST request to the URL with the email
as parameter, and displays the body of the response, decoded in utf-8.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')  # Data is in bytes

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

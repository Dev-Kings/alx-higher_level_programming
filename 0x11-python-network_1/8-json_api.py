#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q. If no argument is given, set q="".
If the response body is properly JSON formatted and not empty,
display the id and name.
Otherwise:
    - Display "Not a valid JSON" if the JSON is invalid
    - Display "No result" if the JSON is empty
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

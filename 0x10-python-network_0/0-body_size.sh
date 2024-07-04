#!/bin/bash
# Send a request to the provided URL and display the size of the body of the response
curl -s "$1" -o /dev/null -w '%{size_download}\n'

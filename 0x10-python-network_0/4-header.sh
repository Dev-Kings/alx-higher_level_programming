#!/bin/bash
# Send a GET request to the provided URL with a custom header and display the body
curl -s -H "X-School-User-Id: 98" "$1"

#!/bin/bash
# Send a GET request to the provided URL
# If the status code is 200, display the body of the response
curl -s -o /dev/stdout -w "%{http_code}" "$1" | {
	read -r body
	read -r code
	if [ "$code" -eq 200 ]; then
		echo "$body"
	fi
}


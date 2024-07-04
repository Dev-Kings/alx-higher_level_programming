#!/bin/bash
# Send a GET request to URL, status code is 200, display the body of response
curl -s -w "%{http_code}" "$1" | { read body; read code; [ "$code" -eq 200 ] && echo "$body"; }

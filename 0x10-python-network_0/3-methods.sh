#!/bin/bash
# Sends an OPTIONS request to the provided URL and display the allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-

#!/bin/bash
# Script sending request to URL passed as an argument,then displays only the status code of the response.
curl -sI -w '%{http_code}' "$1" -o /dev/null

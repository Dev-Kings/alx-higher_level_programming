#!/bin/bash
# Script sending a JSON POST request to URL passed as 1st arg
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"

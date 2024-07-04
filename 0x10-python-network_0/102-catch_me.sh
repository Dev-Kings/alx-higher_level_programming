#!/bin/bash
# Script making a request to 0.0.0.0:5000/catch_me making the server respond with You got me!, in the body of the response
curl -X POST http://0.0.0.0:5000/catch_me -d '{"message":"You got me!"}' -H "Content-Type: application/json"

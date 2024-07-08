#!/bin/bash
# this script send a POST request to a passed URL and display the body of response with two varables.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

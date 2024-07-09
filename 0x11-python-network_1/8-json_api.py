#!/usr/bin/python3
"""
what this script does:
- takes the url and a alphabet
- sends a post request to the url with the letter as a parameter
"""
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./script.py <letter>")
        sys.exit(1)

    alpha = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": alpha}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")


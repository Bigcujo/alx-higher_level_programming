#!/usr/bin/python3
"""
what this scripts does:
- takes a Url and an email address
- sends a POST request to the Url with the email address
- only usin the requests and sys package
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)

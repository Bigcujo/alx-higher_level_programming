#!/usr/bin/python3
"""
this script does:
- takes in a URL and sends a request to it
- diplays the value of the response 
- using only the requests and sys psckage
"""
import requests
import sys

if __name__ == '__main__':
    URL = sys.argv[1]

    request = requests.get(URL)
    print(request.headers.get("X-Request-Id"))

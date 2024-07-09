#!/usr/bin/python3
"""A script that:
- takes a URL,
- sends a request to the passed URL and displays the value retrieved
- of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == '__main__':
    URL = sys.argv[1]

    request = urllib.request.Request(URL)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

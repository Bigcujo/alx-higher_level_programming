#!/usr/bin/python3
"""
what this script does:
- fetches resourse from https://alx-intranet.hbtn.io/status
- the response will be displayed with description
"""

import requests

if __name__ == '__main__':
    request_url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request_url.text)))
    print("\t- content: {}".format(request_url.text))

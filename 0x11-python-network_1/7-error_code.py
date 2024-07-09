#!/usr/bin/python3
"""
what this script does:
- sends a request to a URL and displays the response
- the packages used will be requests and sys
- any status code greater than 400 it prints Error code : <status_code>
"""

import sys
import requests

if __name__ == '__main__':
    URL = sys.argv[1]

    response = requests.get(URL)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

#!/usr/bin/python3
"""
what this script does :
- takes Github credentials (username and pass)
- gets the id using the GitHub API
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth1 = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    request = requests.get("https://api.github.com/user", auth=auth1)
    print(request.json().get("id"))

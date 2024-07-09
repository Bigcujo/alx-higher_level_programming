#!/usr/bin/python3
"""this script fethes data from the passes url 
- fetched from https://alx-intranet.hbtn.io/status
- using the package urllib
"""

if __name__ == "__main__":
    import urllib.request

    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body_response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_response)))
        print("\t- content: {}".format(body_response))
        print("\t- utf8 content: {}".format(body_response.decode("utf-8")))

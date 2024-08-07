#!/usr/bin/python3
""" A script that:
- takes in a URL
- sends a request to the URL
- displays the body of the response decoded in utf-8
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as erorr:
        print('Error code:', erorr.code)

#!/usr/bin/python3
"""sends a request to a URL and displays the body of the response
prints error code in case of an http error"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)

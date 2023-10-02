#!/usr/bin/python3
"""sends a request to a URL and displays the body of the response
prints error code in case of an http error"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    try:
        r = requests.get(url)
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code:", e)

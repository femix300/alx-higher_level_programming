#!/usr/bin/python3
"""A python string that fetches a url
and displays the value of the X-Request-Id
 variable found in the header of the response."""


if __name__ == '__main__':
    from urllib import request
    import sys

    url = sys.argv[1]
    with request.urlopen(url) as r:
        print(r.headers['X-Request-Id'])

#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request"""


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data)

    with request.urlopen(req) as r:
        body = r.read()
        print(body.decode('utf-8'))

#!/usr/bin/python3
"""A python string that fetches a url"""


if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))

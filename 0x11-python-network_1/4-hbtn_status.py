#!/usr/bin/python3
"""APython script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- utf8 content:", response.text)

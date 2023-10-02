#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        json_fmt = response.json()

        if isinstance(json_fmt, dict) and
        'id' in json_fmt and 'name' in json_fmt:
            print("[{}] {}".format(json_fmt['id'], json_fmt['name']))
        elif not json_fmt:
            print("No result")
        else:
            print("Not a valid JSON")
    except Exception:
        print("Not a valid JSON")

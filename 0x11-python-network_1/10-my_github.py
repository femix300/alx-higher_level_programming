#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    credentials = {'username': username, 'password': password}
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, password))
    user_data = r.json()
    user_id = user_data.get('id')
    print(user_id)

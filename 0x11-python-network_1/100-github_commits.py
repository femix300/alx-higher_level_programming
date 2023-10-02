#!/usr/bin/python3
"""A python script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""

if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    r = requests.get(url)
    data = r.json()

    try:
        for i in range(10):
            sha = data[i]['sha']
            author_name = data[i]['commit']['author']['name']
            print('{}: {}'.format(sha, author_name))
    except IndexError:
        pass

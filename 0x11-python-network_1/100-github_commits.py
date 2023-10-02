#!/usr/bin/python3
"""A python script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""

if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{repo_name}/{owner_name}/commits'
    params = {'per_page': 10}

    r = requests.get(url, params=params)
    data = r.json()

    for commit in data:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print('{}: {}'.format(sha, author_name))

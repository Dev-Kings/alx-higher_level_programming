#!/usr/bin/python3
"""
This script takes 2 arguments (repository name and owner name)
and lists the 10 most recent commits of the repository by the user
using the GitHub API.
Prints all commits by: <sha>: <author name> (one per line).
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)
    commits = response.json()[0:10]

    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")

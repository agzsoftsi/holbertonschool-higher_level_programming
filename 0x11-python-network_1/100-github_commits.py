#!/usr/bin/python3
"""
Task 100 -Use the Github API to list the 10 most recent commits
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    reqst = requests.get('https://api.github.com/repos/{}/{}/commits'
                         .format(argv[2], argv[1]))
    for commit in reqst.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))

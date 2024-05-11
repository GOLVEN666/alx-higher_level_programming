#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""
import sys
import requests

if __name__ == "__main__":
    try:
        username = sys.argv[2]
        repo_name = sys.argv[1]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repo_name)
        response = requests.get(commmits_url)
        json_obj = response.json()
        for a, obj in enumerate(json_obj):
            if a == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass

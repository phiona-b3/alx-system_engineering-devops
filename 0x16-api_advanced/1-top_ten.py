#!/usr/bin/python3
"""queries the reddit api and prints the titles"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    a = requests.get(base_url, headers=header, allow_redirects=False)

    if a.status_code != 200:
        print(None)
        return None
    try:
        theme = s.json()
    except Exception:
        print("Not a valid JSON")
        return 0

    try:
        requireddata = theme.get("data")
        children = requireddata.get("children")
        for child in children[:10]:
            data = child.get("data")
            print(data.get("title"))
    except Exception:
        return None

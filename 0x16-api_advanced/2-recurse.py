#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns the titles of all hot articles for a given subreddit"""
    base_url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
               subreddit, after)
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(base_url, headers=header, allow_redirects=False)

    if response:
        data = response.json().get('data')
        children = data.get('children')
        [hot_list.append(x.get('data').get('title')) for x in children]
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None

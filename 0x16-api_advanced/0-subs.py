#!/usr/bin/python3
"""queries the reddit api"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    try:
        base_url = 'https://www.reddit.com/r/'
        header = {'User-Agent': 'Mozilla/5.0'}
        r = request.get(base_url +
                        '{}/about.json'.format(subreddit), headers=header)
        return r.json().get('data').get('subscribers')
    except Exception:
        return 0

#!/usr/bin/python3

"""
Function that queries Reddit API and prints
the titles of the first 10 hot posts
listed for a given subreddit.
"""

import json
import requests


def top_ten(subreddit):
    """
    Return the first 10 hot posts listed for a given subreddit.
    """
    url = "(link unavailable)".format(subreddit)
    headers = {"User-Agent": "Chrome/51.0.2704.103"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)

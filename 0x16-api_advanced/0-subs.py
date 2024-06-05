#!/usr/bin/python3
"""Description of module"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers (not active
    users, total subscribers) for a given subreddit. If an invalid subreddit
    is given, the function should return 0.

    Hint: No authentication is necessary for most features of the Reddit API.
    If you’re getting errors related to Too Many Requests, ensure you’re
    setting a custom User-Agent.
    :param subreddit:
    :return: Number of subscribers or 0
    """
    url = "https://www.reddit.com/r/{sub}/about.json".format(sub=subreddit)
    headers = {
        'User-Agent': 'ALX API Fetcher',
    }
    info = requests.get(url, headers=headers, allow_redirects=False)
    if info.status_code == 200:
        data = info.json()
        return data.get("data").get("subscribers")
    return 0

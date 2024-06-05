#!/usr/bin/python3
"""Description of module"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{sub}/hot/.json".format(sub=subreddit)
    headers = {
        'User-Agent': 'ALX API Fetcher',
    }
    params = {
        "limit": 10
    }
    info = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if info.status_code == 200:
        data = info.json()
        [print(a.get("data").get("title")) for a in data.get("data").get(
            "children")]
    else:
        print('None')

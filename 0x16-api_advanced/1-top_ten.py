#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = f"(link unavailable)"
    headers = {"User-Agent": "Chrome/51.0.2704.103"}
    params = {"raw_json": 1}  # To avoid redirects

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)

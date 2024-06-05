#!/usr/bin/python3
"""
1-top_ten.py

This module defines a function to
fetch titles of the top 10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the top
    10 hot posts of a subreddit and
    prints their titles.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None
    """

    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit API Script v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"][:10]:
                print(post["data"]["title"])
        else:
            print("Subreddit not found or invalid response format.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Invalid JSON response: Missing key {e}")

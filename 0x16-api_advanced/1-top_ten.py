#!/usr/bin/python3
"""
1-top_ten.py

This module defines a function to
fetch titles of the top 10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches titles of the top 10 hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    Prints:
        None: If the subreddit is invalid or there's an error.
        Titles (str): Titles of the top 10 hot posts, one per line.
    """

    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    data = response.json()

    if "data" not in data or "children" not in data["data"]:
        print("Invalid subreddit or unable to fetch data.")
        return None

    posts = data["data"]["children"]
    for post in posts:
        print(post["data"]["title"])


if __name__ == "__main__":
    # Module is being run directly, not imported
    print("This module is intended to be imported, not run directly.")

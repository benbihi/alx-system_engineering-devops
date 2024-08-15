#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    headers = {'User-Agent': 'MyRedditApp/0.1 (by u/YourRedditUsername)'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Will raise an HTTPError

        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)

        return subscribers

    except requests.exceptions.RequestException:
        return 0

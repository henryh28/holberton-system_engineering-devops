#!/usr/bin/python3
import requests


def top_ten(subreddit):
    ''' Return first 10 hot posts for subreddit argument '''
    if not subreddit:
        print("None")

    req = requests.get("http://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit), headers={"User-Agent": "Holberton"}).json()

    hot_posts = req["data"]["children"]

    if len(hot_posts) <= 0:
        print("None")
    else:
        for post in hot_posts:
            print(post["data"]["title"])

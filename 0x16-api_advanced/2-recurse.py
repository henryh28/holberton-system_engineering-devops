#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], more=None):
    ''' Return all hot posts for a given subreddit '''
    if not subreddit:
        return None

    rq = requests.get("http://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, more), headers={"User-Agent": "Holberton"}).json()

    if (rq.get("error") == 404):
        return None

    more = rq["data"]["after"]
    hot_posts = rq["data"]["children"]

    if len(hot_posts) <= 0:
        return None
    else:
        for post in hot_posts:
            hot_list.append(post["data"]["title"])

    return recurse(subreddit, hot_list, more) if more else hot_list

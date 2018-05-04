#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    ''' Return number of subscribers to a subreddit passed as argument '''
    if not subreddit:
        return 0

    req = requests.get("http://www.reddit.com/r/{}/about.json".format(
        subreddit), headers={"User-Agent": "Holberton"}).json()
    return req.get("data").get("subscribers") or 0

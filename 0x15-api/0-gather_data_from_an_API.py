#!/usr/bin/python3
""" Return data from REST API """

from sys import argv
import requests


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, user_id)).json()

    total_tasks = requests.get("{}/todos?user_id={}".format(
        url, user_id)).json()
    done_tasks = requests.get("{}/todos?completed=true&userId={}".format(
        url, user_id)).json()

    print("Employee {} is done with tasks({}/{}):".format(user.get(
        "name"), len(done_tasks), len(total_tasks)))

    for task in done_tasks:
        print("\t", end="")
        print(task.get("title"))

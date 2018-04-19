#!/usr/bin/python3
""" Return data from REST API in CSV format """

import requests
from sys import argv
import json


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, user_id)).json()

    total_tasks = requests.get("{}/todos?user_id={}".format(
        url, user_id)).json()

    list_of_tasks = []
    for task in total_tasks:
        jsondata = {}
        jsondata["task"] = task.get("title")
        jsondata["completed"] = task.get("completed")
        jsondata["username"] = user.get("username")
        list_of_tasks.append(jsondata)

    user_json = {}
    user_json[user_id] = list_of_tasks

    with open("{}.json".format(user_id), "w") as savefile:
        json.dump(user_json, savefile)

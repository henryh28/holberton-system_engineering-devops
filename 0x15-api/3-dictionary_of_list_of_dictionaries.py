#!/usr/bin/python3
""" Return data from REST API in CSV format """

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users/".format(url)).json()
    results = {}

    for user in users:
        user_id = user.get("id")
        tasks = requests.get("{}/users/{}/todos".format(url, user_id)).json()
        list_of_tasks = []

        for task in tasks:
            jsondata = {}
            jsondata["task"] = task.get("title")
            jsondata["completed"] = task.get("completed")
            jsondata["username"] = user.get("username")
            list_of_tasks.append(jsondata)

        results[user_id] = list_of_tasks

    with open("todo_all_employees.json", "w") as savefile:
        json.dump(results, savefile)

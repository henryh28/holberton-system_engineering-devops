#!/usr/bin/python3
""" Return data from REST API in CSV format """

import requests
from sys import argv
import csv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, user_id)).json()

    total_tasks = requests.get("{}/todos?user_id={}".format(
        url, user_id)).json()

    with open("{}.csv".format(user_id), "w") as savefile:
        writer = csv.writer(savefile, quoting=csv.QUOTE_ALL)

        for task in total_tasks:
            writer.writerow([user_id, user.get("username"), task.get(
                "completed"), task.get("title")])

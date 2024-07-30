#!/usr/bin/python3
"""Task 1 solution"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos", params={"userId": userId}).json()
    username = user.get("username")

    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, username, t.get("completed"), t.get("title")]
         ) for t in todos]

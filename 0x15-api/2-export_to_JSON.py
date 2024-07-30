#!/usr/bin/python3
"""Task 1 solution"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos", params={"userId": userId}).json()
    username = user.get("username")

    with open("{}.json".format(userId), "w", newline="") as jsonfile:
        json.dump({userId: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
         } for t in todos]}, jsonfile)

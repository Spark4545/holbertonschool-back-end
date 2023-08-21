#!/usr/bin/python3
"""
description of script
"""
import json
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"missing employee id in arguments")
        sys.exit(1)
    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    username = data[0]["user"]["username"]
    USER_TASK = {EMPLOYEE_ID: []}
    for task in data:
        dict_task = {"task": task["title"], "completed": task["completed"],
                    "username": username}
        USER_TASK[EMPLOYEE_ID].append(dict_task)
    filename = f'{EMPLOYEE_ID}.json'
    with open(filename, 'w') as file:
        json.dump(USER_TASK, file)

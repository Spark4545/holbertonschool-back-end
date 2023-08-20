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

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todo",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    EMPLOYEE_NAME = data[0]["user"]["name"]
    NUMBER_OF_DONE_TASKS = len(data)
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])

    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        print("\t ", title)

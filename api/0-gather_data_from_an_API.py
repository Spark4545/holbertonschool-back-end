#!/usr/bin/python3
"""
description of script
"""
import requests
import sys


if __name__ == "__main__":

    ID = sys.argv[1]
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    URL_USER = "https://jsonplaceholder.typicode.com/users/" + ID
    RESULT = requests.get(URL_USER).json()
    EMPLOYEE_NAME = requests.get('name')
    TODOS = "https://jsonplaceholder.typicode.com/todos/"
    TASK = requests.get(TODOS).json()

    for item in TASK:
        if item.get('userID') == int(ID):
            if item.get('completed') is True:
                TASK_TITLE.append(item['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
    print(f'Employee {EMPLOYEE_NAME} is done with tasks'
          f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for title in TASK_TITLE:
        print(f'\t {title}')

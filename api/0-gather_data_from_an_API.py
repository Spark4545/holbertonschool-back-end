#!/usr/bin/python3
"""
description of script
"""
import requests
import sys


if __name__ == "__main__":
    EMPLOYEE_ID = str(sys.argv[1])
    TODO_API_URL = f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos'
    response = requests.get(TODO_API_URL)
    user_todo_list = response.json()

    completed_task_list = []
    for user_todo_dict in user_todo_list:
        if user_todo_dict.get('completed') is True:
            completed_task_list.append(user_todo_dict.get('title'))

    API_URL = f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}'
    response_ = requests.get(API_URL)
    user_dict = response.json()

    EMPLOYEE_NAME = user_dict.get('name')
    NUMBER_OF_DONE_TASKS = len(completed_task_list)
    TOTAL_NUMBER_OF_TASKS = len(user_todo_list)

    print(f'Employee {EMPLOYEE_NAME} is done with tasks'
          f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')

    for TASK_TITLE in completed_task_list:
        print(f'\t {TASK_TITLE}')

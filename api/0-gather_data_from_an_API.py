#!/usr/bin/python3
""" """
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}')
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    EMPLOYEE_NAME = user.json().get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for task in todos.json():
        if task.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
            TASK_TITLE.append(task.get('title'))
        else:
            TOTAL_NUMBER_OF_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print(f'\t {task}')

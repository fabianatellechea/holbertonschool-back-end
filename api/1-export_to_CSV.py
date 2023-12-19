#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}')
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    USERNAME = user.json().get('username')

    with open(f'{argv[1]}.csv', 'w') as f:
        for task in todos.json():
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            f.write('"{}","{}","{}","{}"\n'.
                    format(argv[1], USERNAME,
                           TASK_COMPLETED_STATUS, TASK_TITLE))

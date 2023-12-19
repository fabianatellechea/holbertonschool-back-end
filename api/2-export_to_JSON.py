#!/usr/bin/python3
""" Python script to export data in the JSON format. """
import json
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}')
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    USERNAME = user.json().get('username')

    tasks = []
    for task in todos.json():
        user_dict = {'task': task.get('title'),
                     'completed': task.get('completed'), 'username': USERNAME}
        tasks.append(user_dict)

    with open(f'{argv[1]}.json', 'w') as f:
        json.dump({argv[1]: tasks}, f)

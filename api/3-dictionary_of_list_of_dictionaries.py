#!/usr/bin/python3
""" Python script to export data in the JSON format. """
import json
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos')
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users')

    all_dict = {}
    for users in user.json():
        USERNAME = users.get('username')
        tasks = []
        for task in todos.json():
            if users.get('id') == task.get('userId'):
                user_dict = {'username': USERNAME,
                             'task': task.get('title'),
                             'completed': task.get('completed'),
                             }
                tasks.append(user_dict)
            all_dict[users.get('id')] = tasks

    with open(f'todo_all_employees.json', 'w') as f:
        json.dump(all_dict, f)

#!/usr/bin/python3
"""
    Python script that gathers data from the
    provided REST API and writes to a csv file
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    all_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(argv[1]))
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(argv[1]))
    name = name.json()
    name = name[0]["username"]
    all_todos = all_todos.json()
    file_name = "{}.json".format(argv[1])

    todo_list = {}
    todo_list[argv[1]] = []
    for x in all_todos:
        todo_list[argv[1]].append(
            {"task": x["title"], "completed": x["completed"], "username": name}
        )

    with open(file_name, 'w') as json_file:
        json.dump(todo_list, json_file)

#!/usr/bin/python3
"""
    Python script that gathers data from the
    provided REST API and writes to a json file
"""

if __name__ == "__main__":
    import json
    import requests

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    users = users.json()
    report = {}
    for user in users:
        all_todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(user["id"]))
        all_todo = all_todo.json()
        report[user["id"]] = []
        for x in all_todo:
            report[user["id"]].append(
                {"username": user["username"],
                    "task": x["title"], "completed": x["completed"]})

    with open("todo_all_employees.com", 'w') as report_file:
        json.dump(report, report_file)

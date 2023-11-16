#!/usr/bin/env python3
"""
    Python script that gathers data from the
    provided REST API
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) < 2:
        exit()
    completed = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
        .format(argv[1]))
    completed = completed.json()
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}"
        .format(argv[1]))
    name = name.json()
    """Calling .json"""
    name = name[0]["name"]
    remaining = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    remaining = len(remaining.json())
    completed_list = []
    for n in completed:
        completed_list.append("\t {}".format(n["title"]))
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), remaining))
    for x in completed_list:
        print(x)

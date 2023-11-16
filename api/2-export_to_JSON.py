#!/usr/bin/python3
"""
    Python script that gathers data from the
    provided REST API and writes to a csv file
"""

if __name__ == "__main__":
    import csv
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
    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for x in all_todos:
            writer.writerow([argv[1], name, x['completed'], x['title']])

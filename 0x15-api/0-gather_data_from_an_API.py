#!/usr/bin/python3
"""using REST API to solve a task"""
if __name__ == "__main__":
    import requests
    import sys

    user_id = int(sys.argv[1])
    user_info = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(user_id))

    try:
        tasks_json = tasks.json()
        complete = 0
        task_title = []

        for task in tasks_json:
            if task.get("completed") is True:
                complete += 1
                task_title.append(task.get("title"))

    except err:
        prinr("Not a valid JSON")

        print("Employee {} is done with tasks({}/{}):".format
              (name_employ, complete, len(tasks_json)))
        for title in task_title:
            print("\t {}".format(title))

#!/usr/bin/python3
"""using REST API to solve a task"""
if __name__ == "__main__":
    import requests
    import sys

    user_id = int(sys.argv[1])
    user_info = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(user_id))

    try:
        TOTAL_NUMBER_OF_TASKS = TASKS.json()
        NUMBER_OF_DONE_TASKS = 0
        TASK_TITLE = []

        for task in tasks_json:
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task.get("title"))

    except error:
        print("Not a valid JSON")

        print("Employee {} is done with tasks({}/{}):".format
              (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                  len(TOTAL_NUMBER_OF_TASKS)))
        for title in TASK_TITLE:
            print("\t {}".format(title))

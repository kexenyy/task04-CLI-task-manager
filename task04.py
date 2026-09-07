import argparse
import json

def add_task(tasks, title, due):
    task = {
        "title": title,
        "due": due,
        "status": "pending"
    }

    tasks.append(task)


def mark_done(tasks, number):
    if number >= 1 and number <= len(tasks):
        tasks[number - 1]["status"] = "done"
        return True

    return False


def filter_tasks(tasks, status=None, due=None):
    result = []

    for task in tasks:
        if status and task["status"] != status:
            continue

        if due and task["due"] != due:
            continue

        result.append(task)

    return result

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("--due", required=True)

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("number", type=int)

    filter_parser = subparsers.add_parser("filter")
    filter_parser.add_argument("--status")
    filter_parser.add_argument("--due")

    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == "add":
        add_task(tasks, args.title, args.due)
        save_tasks(tasks)
        print("Task added successfully!")

    elif args.command == "list":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task["title"], "-", task["due"], "-", task["status"])

    elif args.command == "done":
        if mark_done(tasks, args.number):
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif args.command == "filter":
        result = filter_tasks(tasks, args.status, args.due)

        for i, task in enumerate(result, start=1):
            print(i, task["title"], "-", task["due"], "-", task["status"])


if __name__ == "__main__":
    main()
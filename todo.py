import argparse
import sys

TODO_FILE = "todo_list.txt"

def main():
    parser = argparse.ArgumentParser(description="Todo List CLI")
    parser.add_argument('--add', metavar='TASK', type=str, help='Add a new task')
    parser.add_argument('--remove', metavar='TASK_NUMBER', type=int, help='Remove a task by its number')
    parser.add_argument('--list', action='store_true', help='List all tasks')

    args = parser.parse_args()

    # Placeholder for functions to handle tasks
    if args.add:
        add_task(args.add)
    elif args.remove is not None:
        remove_task(args.remove)
    elif args.list:
        list_tasks()
    else:
        parser.print_help()

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"Add {task} in file")

def remove_task(task_number):
    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
    if 0 <= task_number <= len(tasks):
        del tasks[task_number-1]
        with open(TODO_FILE, "w") as f:
            f.writelines(tasks)
        print(f"Task {task_number} removed.")
    else:
        print("Task number is out of range.")

def list_tasks():
    pass

if __name__ == "__main__":
    main()

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
    print(f"add {task} in file")

def remove_task(task_number):
    
    pass

def list_tasks():
    pass

if __name__ == "__main__":
    main()

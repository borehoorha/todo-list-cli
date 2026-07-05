"""
To-Do List Application (Command-Line)

A simple task manager that lets users add tasks, mark them as completed,
delete tasks, and view their list — all persisted to a local JSON file
so tasks survive between runs.
"""

import json
import os
import sys

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: could not read existing task file. Starting fresh.")
        return []


def save_tasks(tasks):
    """Persist the current task list to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f'Added: "{description}"')


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f'Marked as completed: "{tasks[index]["description"]}"')
    else:
        print("Invalid task number.")


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f'Deleted: "{removed["description"]}"')
    else:
        print("Invalid task number.")


def list_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i + 1}. {status} {task['description']}")
    print()


def show_menu():
    print("===== To-Do List =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("Task description cannot be empty.")
        elif choice == "3":
            list_tasks(tasks)
            try:
                index = int(input("Enter task number to mark complete: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            list_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()

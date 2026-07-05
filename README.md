# To-Do List Application (CLI)

A command-line task manager where users can add tasks, mark them as completed, delete tasks, and view their list. Tasks are saved to a local JSON file so they persist between runs.

## Features
- Add new tasks
- Mark tasks as completed
- Delete tasks
- View all tasks with completion status
- Persistent storage using `tasks.json` (auto-created on first run)

## Skills demonstrated
- Core data structures (list of dictionaries)
- File handling and JSON serialization
- Input validation and basic error handling

## How to run
```bash
python3 todo.py
```

## Example
```
===== To-Do List =====
1. View tasks
2. Add task
3. Mark task as completed
4. Delete task
5. Exit
Choose an option (1-5): 2
Enter task description: Buy groceries
Added: "Buy groceries"
```

## Notes
`tasks.json` is created automatically in the same folder the script is run from, and is excluded from version control via `.gitignore` since it's user-specific runtime data.
# todo-list-cli
# todo-list-cli
# todo-list-cli

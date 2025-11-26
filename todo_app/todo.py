import json
import os

DATA_FILE = "data.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

# View tasks
def view_tasks():
    tasks = load_tasks()
    
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} - {status}")
    print()

# Mark a task as completed
def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("\nTask marked as done.\n")
    else:
        print("\nInvalid task number.\n")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("\nTask deleted.\n")
    else:
        print("\nInvalid task number.\n")

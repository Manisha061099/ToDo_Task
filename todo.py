import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['description']} (Due: {task['due_date']})")

def add_task(tasks):
    description = input("Task description: ")
    due_date = input("Due date (YYYY-MM-DD): ")
    tasks.append({"description": description, "due_date": due_date, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        task_no = int(input("Task number to mark as complete: "))
        tasks[task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_no = int(input("Task number to delete: "))
        tasks.pop(task_no - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTodoCLI:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

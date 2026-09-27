import json


FILE_NAME = "tasks.json"


# -----------------------------
# Load tasks from JSON
# -----------------------------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# -----------------------------
# Save tasks to JSON
# -----------------------------
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Add Task
# -----------------------------
def add_task():
    task_title = input("Enter your task: ")

    if task_title.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": task_title,
        "completed": False
    })

    save_tasks()

    print("Task added successfully! ✓")


# -----------------------------
# View Tasks
# -----------------------------
def view_tasks():
    print("\n===== YOUR TASKS =====")

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "✓"
        else:
            status = " "

        print(f"{i}. [{status}] {task['title']}")


# -----------------------------
# Complete Task
# -----------------------------
def complete_task():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n===== TASKS =====")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']}")

    try:
        task_number = int(
            input("Enter task number to complete: ")
        )

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True

            save_tasks()

            print("Task completed successfully! ✓")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Delete Task
# -----------------------------
def delete_task():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n===== TASKS =====")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']}")

    try:
        task_number = int(
            input("Enter task number to delete: ")
        )

        if 1 <= task_number <= len(tasks):

            deleted_task = tasks.pop(task_number - 1)

            save_tasks()

            print(
                f"'{deleted_task['title']}' "
                "deleted successfully!"
            )

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

tasks = load_tasks()


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        complete_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        print("Goodbye! 👋")
        break

    else:

        print("Invalid choice. Please enter 1-5.")
import os
from datetime import datetime

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, date, status = line.strip().split("|")
                tasks.append({
                    "task": task,
                    "date": date,
                    "status": status
                })
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['date']}|{t['status']}\n")

tasks = load_tasks()

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark as Completed")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n--- TASKS ---")
        for i, t in enumerate(tasks):
            status_icon = "✔" if t["status"] == "Done" else "✘"
            print(f"{i+1}. {t['task']}")
            print(f"   Date: {t['date']}")
            print(f"   Status: {status_icon}")
            print("-" * 25)

def add_task():
    task = input("Enter task: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks.append({
        "task": task,
        "date": date,
        "status": "Pending"
    })
    save_tasks(tasks)
    print("Task added.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "Done"
            save_tasks(tasks)
            print("Task marked as completed ✔")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
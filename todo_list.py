import os
import json

tasks=[]

def add_task(description, priority=1):
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False,
        'priority': priority
    }
    tasks.append(task)

def view_tasks():
    for task in tasks:
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{task['id']}. {task['description']} - {status} (Priority: {task['priority']})")

def update_task(task_id, new_description=None, new_priority=None):
    for task in tasks:
        if task['id'] == task_id:
            if new_description:
                task['description'] = new_description
            if new_priority:
                task['priority'] = new_priority

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]


def save_tasks(filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f)


def load_tasks(filename='tasks.json'):
    global tasks
    with open(filename, 'r') as f:
        tasks = json.load(f)


def main():
    load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority: "))
            add_task(description, priority)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new description (or leave empty to keep current): ")
            new_priority = input("Enter new priority (or leave empty to keep current): ")
            update_task(task_id, new_description, new_priority)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '6':
            save_tasks()
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


import tkinter as tk

def add_task():
    # Implementation similar to the CLI function, but updating GUI elements
    pass

# Continue implementing other functions...

def main():
    root = tk.Tk()
    root.title("To-Do List")
    
    # Create and place GUI elements (buttons, labels, etc.)
    # ...
    
    root.mainloop()

if __name__ == "__main__":
    main()

import json
from model.model import predict_priority

FILE = "../data/tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    priority = predict_priority(task)
    #tasks.append({"tasks": task, "priority": None})
    
    tasks.append({
        "task": task,
        "priority": priority
    })

    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number")

def edit_task(index, new_task):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        tasks[index]["priority"] = predict_priority(new_task)
        save_tasks(tasks)
        print("Task updated")
    else:
        print("Invalid task number")

def list_tasks():
    #tasks = load_tasks()
    #for i, t in enumerate(tasks):
    #    print(f"{i+1}. {t['task']} (Priority: {t['priority']})")
    return load_tasks()
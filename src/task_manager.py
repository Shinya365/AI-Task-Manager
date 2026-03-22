import json

FILE = "data/tasks.json"

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
    tasks.append({"tasks": task, "priority": None})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['tasks']} (Priority: {t['priority']})")
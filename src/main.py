from src.task_manager import add_task, list_tasks

while True:
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter tasks: ")
        add_task(task)
    
    elif choice == "2":
        list_tasks()
    
    elif choice == "3":
        break
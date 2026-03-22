from src.task_manager import add_task, list_tasks, delete_task, edit_task

while True:
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter tasks: ")
        add_task(task)
    
    elif choice == "2":
        list_tasks()
    
    elif choice == "3":
        list_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    
    elif choice == "4":
        list_tasks()
        index = int(input("Enter task number to edit: ")) - 1
        new_task = input("Enter new task: ")
        edit_task(index, new_task)

    elif choice == "5":
        break
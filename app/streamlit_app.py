import streamlit as st
from src.task_manager import add_task, list_tasks, delete_task, edit_task

st.title("AI Task Manager")

menu = ["Add Task", "View Tasks", "Delete Task", "Edit Task"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Task":
    task = st.text_input("Enter task")
    if st.button("Add"):
        add_task(task)
        st.success("Task added!")

elif choice == "View Tasks":
    tasks = list_tasks()
    st.write(tasks)

elif choice == "Delete Task":
    index = st.number_input("Task number", min_value=1)
    if st.button("Delete"):
        delete_task(index - 1)
        st.success("Deleted")

elif choice == "Edit Task":
    index = st.number_input("Task number", min_value=1)
    new_task = st.text_input("New task")
    if st.button("Update"):
        edit_task(index - 1, new_task)
        st.success("Updated!")
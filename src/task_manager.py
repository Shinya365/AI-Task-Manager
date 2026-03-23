import sqlite3

conn = sqlite3.connect("data/database.db", check_same_thread=false)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    priority TEXT
)
""")
conn.commit()

def add_task(task):
    priority = predict_priority(task)
    cursor.execute("INSERT INTO tasks(task, priority) VALUES (?, ?)", (task, priority))
    conn.commit()

def list_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def delete_task(index):
    cursor.execute("DELETE FROM tasks WHERE id=?", (index,))
    conn.commit()

def edit_task(index, new_task):
    priority = predict_priority(new_task)
    cursor.execute("UPDATE tasks SET task=?, priority=? WHERE id=?", (new_task, priority, index))
    conn.commit()
    
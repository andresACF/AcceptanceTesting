# test_todo_list.py
from todo_list import TodoList

def test_add_task():
    todo_list = TodoList()
    todo_list.add_task("Buy groceries", "Buy vegetables and fruits", "2024-08-01", "High")
    assert "Buy groceries" in todo_list.list_tasks()

def test_mark_task_completed():
    todo_list = TodoList()
    todo_list.add_task("Buy groceries", "Buy vegetables and fruits", "2024-08-01", "High")
    todo_list.mark_task_completed("Buy groceries")
    assert "Status: Completed" in todo_list.list_tasks()

    
def test_clear_tasks():
    todo_list = TodoList()
    todo_list.add_task("Buy groceries", "Buy vegetables and fruits", "2024-08-01", "High")
    todo_list.clear_tasks()
    assert todo_list.list_tasks() == "The to-do list is empty."

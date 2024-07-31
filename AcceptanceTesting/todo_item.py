# todo_item.py

from datetime import datetime

class TodoItem:
    def __init__(self, title, description, due_date, priority, creator):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.creator = creator
        self.completed = False
        self.completed_at = None

    def mark_completed(self):
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        completion_time = f" (Completed at: {self.completed_at})" if self.completed_at else ""
        return (f"Task: {self.title}, Description: {self.description}, Due Date: {self.due_date}, "
                f"Priority: {self.priority}, Status: {status}{completion_time}, Created by: {self.creator}")

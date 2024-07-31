# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, description, due_date, priority, creator):
        self.tasks[title] = {
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'creator': creator,
            'status': 'Pending'  # Estado por defecto
        }

    def mark_task_completed(self, title):
        if title in self.tasks:
            self.tasks[title]['status'] = 'Completed'

    def list_tasks(self):
        if not self.tasks:
            return "The to-do list is empty."
        task_list = ""
        for title, details in self.tasks.items():
            task_list += (f"Task: {title}, Description: {details['description']}, "
                          f"Due Date: {details['due_date']}, Priority: {details['priority']}, "
                          f"Status: {details['status']}, Created by: {details['creator']}\n")
        return task_list.strip()

    def clear_tasks(self):
        self.tasks.clear()

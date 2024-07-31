# main.py
from todo_list import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ")
            creator = input("Enter your name: ")
            todo_list.add_task(title, description, due_date, priority, creator)
            print(f"Task '{title}' added successfully.")

        elif choice == "2":
            print("\nTasks in the To-Do List:")
            tasks = todo_list.list_tasks()
            print(tasks)

        elif choice == "3":
            title = input("Enter the title of the task to mark as completed: ")
            result = todo_list.mark_task_completed(title)
            print(result)

        elif choice == "4":
            confirmation = input("Are you sure you want to clear the entire to-do list? (yes/no): ")
            if confirmation.lower() == "yes":
                todo_list.clear_tasks()
                print("All tasks have been cleared.")
            else:
                print("Action cancelled.")

        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

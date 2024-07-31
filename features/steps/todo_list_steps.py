# features/steps/todo_list_steps.py

from behave import given, when, then
from todo_list import TodoList

@given('the to-do list is empty')
def step_given_to_do_list_is_empty(context):
    context.todo_list = TodoList()

@given('the to-do list contains tasks')
def step_given_to_do_list_contains_tasks(context):
    context.todo_list = TodoList()
    for row in context.table:
        title = row.get('Title')
        description = row.get('Description', '')
        due_date = row.get('Due Date', '')
        priority = row.get('Priority', '')
        creator = row.get('Creator', '')
        status = row.get('Status', 'Pending')
        context.todo_list.add_task(title, description, due_date, priority, creator)
        if status == 'Completed':  # Solo marca como completada si el estado es 'Completed'
            context.todo_list.mark_task_completed(title)

@when('the user adds a task "{title}" with the description "{description}" with due date "{due_date}" with priority "{priority}" created by "{creator}"')
def step_when_user_adds_task(context, title, description, due_date, priority, creator):
    context.todo_list.add_task(title, description, due_date, priority, creator)

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.output = context.todo_list.list_tasks()

@when('the user marks task "{title}" as completed')
def step_when_user_marks_task_as_completed(context, title):
    context.todo_list.mark_task_completed(title)

@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    context.todo_list.clear_tasks()

@then('the to-do list should contain "{title}" created by "{creator}"')
def step_then_to_do_list_should_contain_task(context, title, creator):
    tasks = context.todo_list.list_tasks()
    assert title in tasks and creator in tasks, f"Expected to find task '{title}' created by '{creator}', but got: {tasks}"

@then('the output should contain:')
def step_then_output_should_contain(context):
    expected_output = context.text.strip()
    assert expected_output in context.output.strip(), f"Expected output:\n{expected_output}\nBut got:\n{context.output.strip()}"

@then('the to-do list should show task "{title}" as completed')
def step_then_to_do_list_should_show_task_as_completed(context, title):
    tasks = context.todo_list.list_tasks()
    assert f"Task: {title}" in tasks and "Completed" in tasks, f"Expected task '{title}' to be marked as completed, but got: {tasks}"

@then('the to-do list should be empty')
def step_then_to_do_list_should_be_empty(context):
    tasks = context.todo_list.list_tasks()
    assert tasks == "The to-do list is empty.", f"Expected the to-do list to be empty, but got: {tasks}"

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_output = context.text.strip().replace("\r\n", "\n")
    actual_output = context.output.strip().replace("\r\n", "\n")
    assert expected_output == actual_output, f"Expected output:\n{expected_output}\nBut got:\n{actual_output}"

Feature: Manage a to-do list
  As a user
  I want to manage my tasks
  So that I can keep track of what I need to do

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with the description "Milk, Bread, Eggs" with due date "2024-08-01" with priority "High" created by "John Doe"
    Then the to-do list should contain "Buy groceries" created by "John Doe"

Scenario: List all tasks in the to-do list
  Given the to-do list contains tasks:
    | Title         | Description          | Due Date   | Priority | Creator    |
    | Buy groceries | Milk, Bread, Eggs    | 2024-08-01 | High     | John Doe   |
    | Pay bills     | Pay electricity bill | 2024-08-05 | Medium   | Jane Smith |
  When the user lists all tasks
  Then the output should contain:
    """
    Task: Buy groceries, Description: Milk, Bread, Eggs, Due Date: 2024-08-01, Priority: High, Status: Pending, Created by: John Doe
    Task: Pay bills, Description: Pay electricity bill, Due Date: 2024-08-05, Priority: Medium, Status: Pending, Created by: Jane Smith
    """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Title        | Description          | Due Date     | Priority | Creator    | Status  |
      | Buy groceries | Milk, Bread, Eggs    | 2024-08-01   | High     | John Doe   | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
  Given the to-do list contains tasks:
    | Title         |
    | Buy groceries |
    | Pay bills     |
  When the user clears the to-do list
  Then the to-do list should be empty


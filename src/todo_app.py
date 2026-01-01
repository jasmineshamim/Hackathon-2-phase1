"""
In-Memory Todo Console Application

A beginner-friendly task management application that demonstrates Python fundamentals
through practical implementation. Features include adding, viewing, updating, deleting,
and marking tasks as complete/incomplete.

All data is stored in-memory and lost when the application terminates.
No external dependencies required - uses Python standard library only.

Usage:
    python src/todo_app.py

Features:
    1. Add Task - Create new tasks with title and optional description
    2. View Tasks - Display all tasks sorted by ID
    3. Update Task - Modify title and/or description of existing tasks
    4. Delete Task - Remove tasks by ID
    5. Mark Complete/Incomplete - Toggle task status
    6. Exit - Terminate the application

Author: Generated with Claude Code
Version: 1.0.0
"""

# Global data storage (in-memory only)
task_store = {}  # Dictionary: {task_id: {"id": int, "title": str, "description": str, "status": str}}
next_task_id = 1  # Counter for generating unique task IDs


def get_user_input(prompt, allow_empty=False):
    """
    Get user input with optional empty validation.

    Args:
        prompt (str): The prompt message to display to the user
        allow_empty (bool): Whether to allow empty input (default: False)

    Returns:
        str: The user's input (stripped of leading/trailing whitespace)

    Note:
        If allow_empty is False and user provides empty input, will re-prompt.
    """
    while True:
        user_input = input(prompt).strip()
        if not allow_empty and not user_input:
            continue
        return user_input


def validate_title(title):
    """
    Validate and normalize task title.

    Args:
        title (str): The title to validate

    Returns:
        tuple: (validated_title, warning_message or None)

    Rules:
        - Must not be empty after stripping whitespace
        - Maximum 100 characters (truncates with warning if exceeded)
    """
    title = title.strip()

    if not title:
        return None, "Title cannot be empty"

    if len(title) > 100:
        title = title[:100]
        return title, "Title truncated to 100 characters"

    return title, None


def validate_description(description):
    """
    Validate and normalize task description.

    Args:
        description (str): The description to validate

    Returns:
        tuple: (validated_description, warning_message or None)

    Rules:
        - Can be empty (optional field)
        - Maximum 500 characters (truncates with warning if exceeded)
    """
    if len(description) > 500:
        description = description[:500]
        return description, "Description truncated to 500 characters"

    return description, None


def find_task(task_id):
    """
    Look up a task by ID with error handling.

    Args:
        task_id (int): The ID of the task to find

    Returns:
        dict or None: The task dictionary if found, None otherwise

    Note:
        Displays error message if task not found.
    """
    if task_id in task_store:
        return task_store[task_id]
    else:
        print(f"Task ID {task_id} not found")
        return None


def display_menu():
    """
    Display the main menu options.

    Shows all 6 available operations for the user to choose from.
    """
    print("\n" + "="*50)
    print("         TODO CONSOLE APPLICATION")
    print("="*50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print("="*50)


def add_task():
    """
    Add a new task with title and optional description.

    Prompts user for task details, validates input, generates unique ID,
    and stores the task with default status "Pending".

    User Story: US1 (Priority P1) - Add New Task
    """
    global next_task_id

    print("\n--- Add New Task ---")

    # Get and validate title
    while True:
        title_input = input("Enter task title: ").strip()
        validated_title, warning = validate_title(title_input)

        if validated_title is None:
            print(f"Error: {warning}")
            continue

        if warning:
            print(f"Warning: {warning}")

        break

    # Get and validate description
    description_input = input("Enter task description (optional, press Enter to skip): ")
    validated_description, warning = validate_description(description_input)

    if warning:
        print(f"Warning: {warning}")

    # Create task
    task = {
        "id": next_task_id,
        "title": validated_title,
        "description": validated_description,
        "status": "Pending"
    }

    # Store task
    task_store[next_task_id] = task
    next_task_id += 1

    # Confirmation
    print(f"\nSuccess! Task created with ID {task['id']}")
    print(f"Title: {task['title']}")
    print(f"Status: {task['status']}")


def view_tasks():
    """
    Display all tasks sorted by ID.

    Shows ID, title, description (or "[No description]"), and status
    for each task in a readable format.

    User Story: US2 (Priority P2) - View All Tasks
    """
    print("\n--- All Tasks ---")

    # Check if task store is empty
    if not task_store:
        print("\nNo tasks found. Add your first task to get started!")
        return

    # Get sorted task IDs
    sorted_ids = sorted(task_store.keys())

    # Display each task
    for task_id in sorted_ids:
        task = task_store[task_id]
        description = task["description"] if task["description"] else "[No description]"

        print("\n" + "-"*50)
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {description}")
        print(f"Status: {task['status']}")

    print("-"*50)
    print(f"\nTotal tasks: {len(task_store)}")


def update_task():
    """
    Update title and/or description of an existing task.

    Prompts user for task ID, validates existence, allows updating
    title and description while preserving ID and status.

    User Story: US3 (Priority P3) - Update Task Details
    """
    print("\n--- Update Task ---")

    # Get task ID
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Error: Please enter a valid number")
        return

    # Find task
    task = find_task(task_id)
    if not task:
        return

    # Display current task
    print(f"\nCurrent title: {task['title']}")
    print(f"Current description: {task['description'] if task['description'] else '[No description]'}")

    # Get and validate new title
    while True:
        title_input = input("\nEnter new title (or press Enter to keep current): ").strip()

        # If empty, keep current title
        if not title_input:
            new_title = task['title']
            break

        validated_title, warning = validate_title(title_input)

        if validated_title is None:
            print(f"Error: {warning}")
            continue

        if warning:
            print(f"Warning: {warning}")

        new_title = validated_title
        break

    # Get and validate new description
    description_input = input("Enter new description (or press Enter to keep current): ")

    # If empty, keep current description
    if not description_input:
        new_description = task['description']
    else:
        validated_description, warning = validate_description(description_input)
        if warning:
            print(f"Warning: {warning}")
        new_description = validated_description

    # Update task (preserving ID and status)
    task['title'] = new_title
    task['description'] = new_description

    # Confirmation
    print(f"\nSuccess! Task ID {task_id} updated")
    print(f"New title: {task['title']}")
    print(f"New description: {task['description'] if task['description'] else '[No description]'}")


def delete_task():
    """
    Delete a task by ID.

    Prompts user for task ID, validates existence, removes task from memory,
    and displays confirmation. Deleted IDs are never reused.

    User Story: US4 (Priority P4) - Delete Task
    """
    print("\n--- Delete Task ---")

    # Get task ID
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Error: Please enter a valid number")
        return

    # Find task
    task = find_task(task_id)
    if not task:
        return

    # Display task to be deleted
    print(f"\nTask to delete:")
    print(f"ID: {task['id']}")
    print(f"Title: {task['title']}")

    # Delete task
    del task_store[task_id]

    # Confirmation
    print(f"\nTask ID {task_id} deleted successfully")


def toggle_task_status():
    """
    Toggle task status between "Pending" and "Completed".

    Prompts user for task ID, validates existence, toggles status,
    and displays confirmation. Operation is idempotent.

    User Story: US5 (Priority P5) - Mark Task Complete/Incomplete
    """
    print("\n--- Mark Complete/Incomplete ---")

    # Get task ID
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Error: Please enter a valid number")
        return

    # Find task
    task = find_task(task_id)
    if not task:
        return

    # Display current status
    print(f"\nCurrent status: {task['status']}")

    # Toggle status
    if task['status'] == "Pending":
        task['status'] = "Completed"
    else:
        task['status'] = "Pending"

    # Confirmation
    print(f"\nTask ID {task_id} marked as {task['status']}")


def main():
    """
    Main application entry point and menu loop.

    Displays menu, handles user choice, dispatches to appropriate function,
    and continues until user chooses to exit.
    """
    print("\nWelcome to the In-Memory Todo Console Application!")
    print("All data is stored in memory and will be lost when you exit.")

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            toggle_task_status()
        elif choice == "6":
            print("\nThank you for using the Todo Console Application!")
            print("All tasks have been cleared from memory. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please try again.")
            print("Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

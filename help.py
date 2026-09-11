def help_message():
    help_text = """
Task Manager: Add, modify, remove, and show tasks in a file.
Usage:
  task.py <file> <command> [<args>] (see below for args)
  commands and args:
    add <details> [<label>]      Add a new task with the given details and optional label.
    modify <id> <details> [<label>]  Modify the task with the given id with new details and optional label.
    rm <id>                      Remove the task with the given id.
    show                         Show all tasks in the file.
    """
    return help_text
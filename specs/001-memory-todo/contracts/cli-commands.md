# CLI Commands for memory-todo

This document defines the command-line interface for the memory-todo application.

## `add`

Adds a new task to the to-do list.

-   **Usage**: `todo add --title <title> --description <description>`
-   **Arguments**:
    -   `--title <title>` (string, required): The title of the task.
    -   `--description <description>` (string, optional): A description for the task.
-   **Output**: A confirmation message with the new task's ID.

## `list`

Lists all tasks in the to-do list.

-   **Usage**: `todo list`
-   **Output**: A formatted table of all tasks, including their ID, status, title, and description.

## `update`

Updates the title or description of an existing task.

-   **Usage**: `todo update <id> [--title <title>] [--description <description>]`
-   **Arguments**:
    -   `<id>` (integer, required): The ID of the task to update.
    -   `--title <title>` (string, optional): The new title for the task.
    -   `--description <description>` (string, optional): The new description for the task.
-   **Output**: A confirmation message.

## `done`

Marks a task as complete or incomplete.

-   **Usage**: `todo done <id>`
-   **Arguments**:
    -   `<id>` (integer, required): The ID of the task to toggle.
-   **Output**: A confirmation message showing the new status of the task.

## `delete`

Deletes a task from the to-do list.

-   **Usage**: `todo delete <id>`
-   **Arguments**:
    -   `<id>` (integer, required): The ID of the task to delete.
-   **Output**: A confirmation message.

# memory-todo

A simple in-memory to-do list CLI application.

## Prerequisites

-   Python 3.13+
-   `uv` package manager

## Installation

1.  Clone the repository.
2.  Create a virtual environment: `uv venv`
3.  Activate the virtual environment: `source .venv/bin/activate` (on Linux/macOS) or `.venv\Scripts\Activate.ps1` (on Windows).
4.  Install dependencies: `uv pip install -r requirements.txt`

## Usage

The application is run from the command line.

```bash
python -m src.todo_app.main [command] [options]
```

### Commands

#### `add`

Adds a new task to the to-do list.

-   **Usage**: `python -m src.todo_app.main add --title <title> --description <description>`
-   **Arguments**:
    -   `--title <title>` (string, required): The title of the task.
    -   `--description <description>` (string, optional): A description for the task.

#### `list`

Lists all tasks in the to-do list.

-   **Usage**: `python -m src.todo_app.main list`

#### `update`

Updates the title or description of an existing task.

-   **Usage**: `python -m src.todo_app.main update <id> [--title <title>] [--description <description>]`
-   **Arguments**:
    -   `<id>` (integer, required): The ID of the task to update.
    -   `--title <title>` (string, optional): The new title for the task.
    -   `--description <description>` (string, optional): The new description for the task.

#### `done`

Marks a task as complete or incomplete.

-   **Usage**: `python -m src.todo_app.main done <id>`
-   **Arguments**:
    -   `<id>` (integer, required): The ID of the task to toggle.

#### `delete`

Deletes a task from the to-do list.

-   **Usage**: `python -m src.todo_app.main delete <id>`
-   **Arguments**:
    -   `<id>` (integer, required): The ID of the task to delete.

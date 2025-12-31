# Data Model for memory-todo

This document outlines the data model for the memory-todo application, based on the feature specification.

## Task Entity

The core entity of the application is the `Task`.

### Fields

| Field         | Type    | Description                               |
|---------------|---------|-------------------------------------------|
| `id`          | `int`   | A unique identifier for the task.         |
| `title`       | `str`   | The title of the task.                    |
| `description` | `str`   | A more detailed description of the task.  |
| `is_completed`| `bool`  | The completion status of the task.        |

### Relationships

The `Task` entity has no relationships with other entities in this version of the application.

### State Transitions

A `Task` can be in one of two states:
-   **Incomplete**: `is_completed` is `False`. This is the default state for a new task.
-   **Complete**: `is_completed` is `True`.

A task can transition from "Incomplete" to "Complete" and back.

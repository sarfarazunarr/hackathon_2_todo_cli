Generate the Specification for the memory-todo application.

Functional Requirements:

Add Task: User can provide a title and a description. Each task is assigned a unique integer ID automatically.

View Tasks: Display a formatted list/table of all tasks showing ID, Status (using icons like [ ] and [x]), Title, and Description.

Update Task: User can modify the title or description of an existing task by referencing its ID.

Mark Complete: User can toggle a task's status between "Complete" and "Incomplete" via ID.

Delete Task: User can remove a task from memory using its ID.

Data Model:

Task object: id (int), title (str), description (str), is_completed (bool).

CLI Interface:

The app should support commands like: add, list, update, delete, and done.
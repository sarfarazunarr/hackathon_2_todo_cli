Generate a Task List for implementing the memory-todo application based on the Constitution and Specification.

Implementation Steps:

Project Initialization: Use uv init to set up the project and configure Python 3.13.

Model Definition: Create the Task dataclass or Pydantic model in models.py.

Core Logic: Implement a TodoManager class in manager.py that handles the in-memory list and the 5 basic CRUD/Logic operations.

CLI Entry Point: Use argparse (or a similar lightweight library) in main.py to map terminal commands to TodoManager methods.

Spec Validation: Create a test suite using Spec-Kit Plus to verify that:

Tasks are correctly added to the list.

IDs increment correctly.

Updating a non-existent ID handles errors gracefully.

The "Mark Complete" toggle functions as expected.

Refinement: Ensure all outputs are formatted clearly for the console using simple ASCII or f-strings.
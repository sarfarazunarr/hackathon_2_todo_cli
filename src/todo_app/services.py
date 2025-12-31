import json
import os
from typing import List
from models import Task

JSON_FILE = "tasks.json"

class TaskService:
    """Manages tasks in memory with JSON file persistence."""

    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1
        self._load_tasks_from_file()

    def _load_tasks_from_file(self):
        """Loads tasks from the JSON file."""
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as f:
                tasks_data = json.load(f)
                self._tasks = [Task(**data) for data in tasks_data]
                if self._tasks:
                    self._next_id = max(task.id for task in self._tasks) + 1

    def _save_tasks_to_file(self):
        """Saves tasks to the JSON file."""
        with open(JSON_FILE, "w") as f:
            tasks_data = [task.__dict__ for task in self._tasks]
            json.dump(tasks_data, f, indent=4)

    def add_task(self, title: str, description: str) -> Task:
        """Adds a new task."""
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        self._save_tasks_to_file()
        return task

    def get_tasks(self) -> List[Task]:
        """Returns all tasks."""
        return self._tasks

    def get_task_by_id(self, task_id: int) -> Task | None:
        """Gets a task by its ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str | None, description: str | None) -> Task | None:
        """Updates a task."""
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            self._save_tasks_to_file()
        return task

    def toggle_task_completion(self, task_id: int) -> Task | None:
        """Toggles the completion status of a task."""
        task = self.get_task_by_id(task_id)
        if task:
            task.is_completed = not task.is_completed
            self._save_tasks_to_file()
        return task

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task."""
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            self._save_tasks_to_file()
            return True
        return False

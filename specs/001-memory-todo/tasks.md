---
description: "Task list for feature implementation"
---

# Tasks: memory-todo application

**Input**: Design documents from `/specs/001-memory-todo/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure in `src/todo_app/` and `tests/` per the implementation plan.
- [x] T002 Initialize `uv` environment by creating a `pyproject.toml` and a `.python-version` file.
- [x] T003 Create an empty `requirements.txt` file for dependencies.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T004 [P] Implement the `Task` data model in `src/todo_app/models.py`.
- [x] T005 Implement the core `TaskService` in `src/todo_app/services.py` to manage tasks in memory.

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Allow a user to add a new task.

**Independent Test**: Run `todo add --title "Test Task"` and verify it appears in `todo list`.

### Implementation for User Story 1

- [x] T006 [US1] Implement `add_task` method in `src/todo_app/services.py`.
- [x] T007 [US1] Implement the `add` command in `src/todo_app/main.py` to handle user input and call the service.

---

## Phase 4: User Story 2 - View Tasks (Priority: P2)

**Goal**: Allow a user to view all existing tasks.

**Independent Test**: Run `todo list` and verify it displays all tasks in a formatted table.

### Implementation for User Story 2

- [x] T008 [US2] Implement `get_tasks` method in `src/todo_app/services.py`.
- [x] T009 [US2] Implement the `list` command in `src/todo_app/main.py`.

---

## Phase 5: User Story 3 - Update Task (Priority: P3)

**Goal**: Allow a user to update an existing task.

**Independent Test**: Run `todo update 1 --title "New Title"` and verify the change in `todo list`.

### Implementation for User Story 3

- [x] T010 [US3] Implement `update_task` method in `src/todo_app/services.py`.
- [x] T011 [US3] Implement the `update` command in `src/todo_app/main.py`.

---

## Phase 6: User Story 4 - Mark Task as Complete (Priority: P4)

**Goal**: Allow a user to mark a task as complete.

**Independent Test**: Run `todo done 1` and verify the status changes in `todo list`.

### Implementation for User Story 4

- [x] T012 [US4] Implement `toggle_task_completion` method in `src/todo_app/services.py`.
- [x] T013 [US4] Implement the `done` command in `src/todo_app/main.py`.

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Allow a user to delete a task.

**Independent Test**: Run `todo delete 1` and verify the task is removed from `todo list`.

### Implementation for User Story 5

- [x] T014 [US5] Implement `delete_task` method in `src/todo_app/services.py`.
- [x] T015 [US5] Implement the `delete` command in `src/todo_app/main.py`.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T016 [P] Add user-friendly error handling for invalid task IDs or commands in `src/todo_app/main.py`.
- [x] T017 [P] Implement help messages for all CLI commands in `src/todo_app/main.py`.
- [x] T018 Write a comprehensive `README.md` with setup and usage instructions.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed before all other phases.
- **Foundational (Phase 2)** depends on Setup and blocks all user stories.
- **User Stories (Phases 3-7)** can be implemented in any order after the Foundational phase is complete, but following the priority order is recommended for an incremental MVP.
- **Polish (Phase 8)** can be done after all user stories are complete.

## Implementation Strategy

### MVP First (User Story 1 & 2)

1.  Complete Phase 1 & 2.
2.  Complete Phase 3 (Add Task) and Phase 4 (View Tasks).
3.  At this point, you have a basic, usable MVP.

### Incremental Delivery

After the MVP, add the remaining user stories one by one, testing each independently.

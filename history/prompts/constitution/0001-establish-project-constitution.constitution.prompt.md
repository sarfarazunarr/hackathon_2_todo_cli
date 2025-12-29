---
id: 0001
title: Establish Project Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: gemini
feature: none
branch: (unknown)
user: (unknown)
command: /sp.constitution @prompts/cons.md
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/tasks-template.md
tests:

---

## Prompt

Establish the Constitution for a CLI-based Todo application named memory-todo.

Core Principles:

Simplicity: The application must be lightweight and run entirely in the terminal.

State: Use in-memory storage only; no persistent database or file I/O is required for this version.

Clean Code: Follow PEP 8 standards, use type hinting throughout, and ensure modularity.

Tech Stack Constraints:

Language: Python 3.13+

Environment/Package Manager: uv

Development Tools: Claude Code and Spec-Kit Plus for spec-driven development.

Project Structure:

Follow a modern Python layout (e.g., src/todo_app/ for logic, tests/ for specs).

Entry point should be via todo_app.main:app

## Response snapshot

Constitution v1.0.0 established and templates updated.

## Outcome

- ✅ Impact: Established the foundational principles and constraints for the 'memory-todo' project. This creates a baseline for all future development and ensures consistency.
- 🧪 Tests: No tests were run.
- 📁 Files: 
  - Modified: .specify/memory/constitution.md (Created v1.0.0)
  - Modified: .specify/templates/plan-template.md (Aligned with new constitution)
  - Modified: .specify/templates/tasks-template.md (Aligned with new constitution)
- 🔁 Next prompts: '/sp.specify' to start defining a feature based on the new constitution.
- 🧠 Reflection: The process of creating a constitution and then propagating the changes to templates is a good way to enforce project standards from the beginning.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a

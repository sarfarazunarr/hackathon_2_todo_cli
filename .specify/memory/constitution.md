<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - PRINCIPLE_1: "Simplicity"
  - PRINCIPLE_2: "State"
  - PRINCIPLE_3: "Clean Code"
- Added sections:
  - "Tech Stack Constraints"
  - "Project Structure"
- Removed sections:
  - Principles 4, 5, 6 from template
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# memory-todo Constitution

## Core Principles

### Simplicity
The application must be lightweight and run entirely in the terminal.

### State
Use in-memory storage only; no persistent database or file I/O is required for this version.

### Clean Code
Follow PEP 8 standards, use type hinting throughout, and ensure modularity.

## Tech Stack Constraints

- **Language**: Python 3.13+
- **Environment/Package Manager**: uv
- **Development Tools**: Claude Code and Spec-Kit Plus for spec-driven development.

## Project Structure

- Follow a modern Python layout (e.g., `src/todo_app/` for logic, `tests/` for specs).
- Entry point should be via `todo_app.main:app`.

## Governance

All development must adhere to the principles and constraints outlined in this constitution. All pull requests and reviews must verify compliance with this constitution.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
# Quickstart for memory-todo

This document provides a quick overview of how to get started with the memory-todo application.

## Prerequisites

-   Python 3.13+
-   `uv` package manager

## Installation

1.  Clone the repository.
2.  Create a virtual environment: `uv venv`
3.  Activate the virtual environment: `source .venv/bin/activate` (on Linux/macOS) or `.venv\Scripts\Activate.ps1` (on Windows).
4.  Install dependencies: `uv pip install -r requirements.txt` (Note: `requirements.txt` will be created later).

## Running the application

The application is run from the command line.

```bash
python -m todo_app.main [command] [options]
```

See the `cli-commands.md` file in the `contracts` directory for a full list of commands and options.

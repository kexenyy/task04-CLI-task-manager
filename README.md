# task04-CLI-task-manager

A simple command-line task manager made with Python.

## Features

- Add tasks with a due date
- List all tasks
- Mark tasks as done
- Filter tasks by status
- Filter tasks by due date
- Stores tasks in a JSON file
- Includes pytest tests

## Installation

1. Make sure Python is installed.
2. Install pytest:

python -m pip install pytest

## Usage

Add a task:

python task04.py add "Finish Python assignment" --due 2026-09-10

List tasks:

python task04.py list

Mark a task as done:

python task04.py done 1

Filter by status:

python task04.py filter --status done

Filter by due date:

python task04.py filter --due 2026-09-10

## Run Tests

python -m pytest

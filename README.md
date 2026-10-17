## Project Repository

[View Expense Tracker on GitHub](https://github.com/durgeshdev264/expense-tracker)
# CLI Expense Tracker

A command-line expense tracking application built with Python. It allows users to record expenses, view expense history, and summarize spending by category.

## Features

- Add expenses with a description, amount, and category
- Validate expense descriptions, categories, and amounts
- Store expense records in a local JSON file
- Generate a list of recorded expenses
- Calculate total expenses
- Summarize expenses by category
- Handle invalid user input
- Run automated unit tests for validation logic

## Tech Stack

- **Language:** Python
- **Dependency and environment management:** uv
- **Storage:** JSON
- **Testing:** Python `unittest`
- **Editor:** Visual Studio Code

## Project Structure

```text
expense-tracker/
├── main.py
├── test_expenses.py
├── expenses.json
├── .gitignore
└── README.md
```

## Prerequisites

- Python
- uv
- Git (optional, for version control)

## Setup

Clone the repository:

```bash
git clone https://github.com/durgeshdev264/expense-tracker.git
cd expense-tracker
```

Run the application:

```bash
uv run python main.py
```

## Running Tests

Run the unit tests with:

```bash
uv run python -m unittest test_expenses
```

## Data Storage

Expense records are stored locally in `expenses.json`. The application reads and updates this file when expenses are added.

**Note:** Use sample data only. Do not store personal or financial information in a public repository.

## What I Learned

- Writing reusable Python functions
- Validating and converting user input
- Working with lists and dictionaries
- Reading and writing JSON files
- Handling exceptions
- Writing unit tests with `unittest`
- Using Git and GitHub for version control

## Future Improvements

- Add, edit, and delete expense records
- Filter expenses by date range
- Export reports to CSV
- Improve automated test coverage
- Add stronger validation for corrupted or unexpected stored data

## Author

Durgesh

GitHub: https://github.com/durgeshdev264

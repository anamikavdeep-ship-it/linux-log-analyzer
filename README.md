# Linux Log Analyzer

A Python-based log analysis project that reads server log files, counts log levels, and extracts error messages. This project also demonstrates Git version control, unit testing, and Continuous Integration (CI) using GitHub Actions.

## Project Overview

The goal of this project is to build a simple log analyzer and practise a development workflow that includes writing code, testing it, managing changes with Git, and automating checks through GitHub Actions.

## Features

- Reads server logs from a text file.
- Counts INFO, WARNING, and ERROR messages.
- Extracts and displays individual error messages.
- Generates a log analysis report in the terminal.
- Includes automated unit tests.
- Runs automated checks through GitHub Actions.

## Technologies Used

- Python 3.12
- Git and GitHub
- Python unittest
- GitHub Actions
- YAML
- Windows CMD for local development
- Ubuntu runner for CI

## Project Structure

```text
linux-log-analyzer/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── logs/
│   └── server.log
│
├── tests/
│   └── test_log_analyzer.py
│
├── .gitignore
├── log_analyzer.py
├── README.md
├── analysis-output.txt
└── terminal-history.txt
```

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/anamikavdeep-ship-it/linux-log-analyzer.git
```

Navigate into the project directory:

```bash
cd linux-log-analyzer
```

Run the log analyzer:

```bash
python log_analyzer.py
```

## Run Unit Tests

Execute the following command:

```bash
python -m unittest discover -s tests -v
```

The project currently includes two unit tests covering:
- Log-level counts.
- Extracted error messages.

## Sample Output

```text
===== LINUX LOG ANALYSIS REPORT =====
INFO messages: 5
WARNING messages: 2
ERROR messages: 3
Total log entries: 10

===== ERROR DETAILS =====
2026-11-05 09:07:45 ERROR Database connection failed
2026-11-05 09:12:10 ERROR Disk space critically low
2026-11-05 09:20:40 ERROR Application timeout
```

## Continuous Integration with GitHub Actions

A GitHub Actions workflow automatically runs when code is pushed to the `main` branch or when a pull request targets `main`.

The CI pipeline performs three checks:

1. **Python syntax validation** – checks the script using `py_compile`.
2. **Unit testing** – executes the automated tests using Python unittest.
3. **Script execution** – runs the log analyzer.

The workflow uses Python 3.12 on an Ubuntu runner.

## Git Concepts Practised

- Initializing a Git repository.
- Staging and committing changes.
- Creating and switching feature branches.
- Merging feature branches into main.
- Reviewing Git history.
- Connecting a local repository to GitHub.
- Pushing changes to a remote repository.
- Using `.gitignore`.

## Learning Outcomes

Through this project, I practised:

- Python file handling and log parsing.
- Writing reusable Python functions.
- Creating unit tests.
- Managing code using Git branches and commits.
- Automating code validation with GitHub Actions.
- Understanding the Continuous Integration workflow.

## Future Improvements

- Add support for custom log files.
- Generate reports automatically.
- Add date-based log filtering.
- Improve error handling and test coverage.

## Repository

[View the project on GitHub](https://github.com/anamikavdeep-ship-it/linux-log-analyzer)

## CI Failure Practice

This section is part of my hands-on practice with GitHub Actions,
CI troubleshooting, and automated testing.
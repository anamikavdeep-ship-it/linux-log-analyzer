\# Linux Log Analyzer



\## Project Overview

A beginner-friendly Python project that reads a server log file, identifies log levels, counts messages, and displays detailed error entries.



\## Features

\- Reads server logs from a text file.

\- Counts INFO, WARNING, and ERROR messages.

\- Displays individual error messages.

\- Generates a simple analysis report in the terminal.



\## Technologies Used

\- Python

\- Git

\- GitHub

\- Windows CMD (for development and testing)



\## Project Structure

```text

linux-log-analyzer/

│

├── logs/

│   └── server.log

│

├── reports/

│

└── log\_analyzer.py

```



\## How to Run



1\. Clone or download this repository.

2\. Open CMD in the project folder.

3\. Run:



```bash

python log\_analyzer.py

```



\## Sample Output



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



\## Git Concepts Practised

\- Initializing a Git repository

\- Staging and committing changes

\- Creating feature branches

\- Switching branches

\- Merging feature branches into main

\- Reviewing commit history



\## Learning Outcome

Built a practical log analysis tool while learning Python fundamentals and a real-world Git branching and merging workflow.



\*\*Project Status:\*\* Completed initial version. Further improvements planned.




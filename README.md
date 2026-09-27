# Student Performance Analyzer

A beginner-friendly, menu-driven Python project for managing student marks and reviewing class performance. It demonstrates modular programming, object-oriented design, input validation, JSON file storage, and simple NumPy/Pandas analysis.

## Problem statement

Keeping student marks in scattered notes makes it difficult to update records, calculate averages consistently, or understand class performance. This application stores each student's marks in one reusable JSON file and provides a small console interface for common tasks.

## Objectives

- Practice building a multi-module Python application.
- Use a `Student` class to represent student records.
- Validate data and handle expected errors with clear messages.
- Persist data between runs using JSON.
- Summarize marks with NumPy and Pandas.

## Features

- Add, view, search, update, and delete students.
- Calculate an individual average and grade.
- Analyze subject averages, score ranges, standard deviations, class average, pass/fail counts, and grade distribution.
- Reject duplicate IDs and invalid names or marks.
- Keep records in `data/students.json` between application runs.

## Technologies used

- Python 3.10 or newer
- NumPy
- Pandas
- JSON and `unittest` from the Python standard library

## Python concepts demonstrated

Variables and data types, lists and dictionaries, a tuple for subject marks, functions, classes and objects, constructors, methods, encapsulation through a service class, conditionals, loops, exceptions, custom validation, file handling, JSON, packages, NumPy arrays, and Pandas DataFrames.

## Project structure

```text
student-performance-analyzer/
├── main.py
├── models/
│   ├── __init__.py
│   └── student.py
├── services/
│   ├── __init__.py
│   └── student_service.py
├── utils/
│   ├── __init__.py
│   ├── validation.py
│   └── file_handler.py
├── analysis/
│   ├── __init__.py
│   └── analyzer.py
├── data/
│   └── students.json
├── tests/
│   ├── __init__.py
│   └── test_student.py
├── requirements.txt
└── .gitignore
```

## Installation

Open a terminal in the project folder. Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the application

```bash
python main.py
```

Choose a number from the menu. Marks can be whole numbers or decimals from 0 through 100. Student IDs use letters, numbers, hyphens, or underscores. Names support letters, spaces, apostrophes, and hyphens.

## Example usage

```text
=== Student Performance Analyzer ===
1. Add a student
2. View all students
3. Search for a student
4. Update student information
5. Delete a student
6. Calculate individual student average
7. Calculate individual student grade
8. Overall dataset analysis
9. Exit
Choose an option: 1
Student ID: STU-101
Name: Ada Lovelace
Python marks (0-100): 92
Mathematics marks (0-100): 88
AI/ML marks (0-100): 95
Added Ada Lovelace (grade A).
```

## Testing

Run the standard-library unit tests from the project folder:

```bash
python -m unittest discover -v
```

Tests cover student construction, average and grade calculations, mark validation, duplicate IDs, CRUD operations, and persistence using a temporary JSON file.

## NumPy and Pandas usage

`analysis/analyzer.py` builds a Pandas DataFrame from student objects and derives average and grade columns. It uses NumPy to calculate subject means, highest and lowest marks, standard deviations, and the overall average. Pandas provides row counts and grade distribution. An empty dataset produces a valid zero-valued summary.

## JSON data storage

Student records are saved as a JSON list at `data/students.json`. The file helper creates the file and parent folder when missing. If the JSON is invalid, it reports the read problem and lets the application continue with an empty in-memory list. Saving valid changes writes formatted JSON so it can be inspected by a beginner.

## Future improvements

- Add configurable grading thresholds and subject names.
- Export reports as CSV.
- Add sorting and filtering options.
- Add stricter recovery or backup behavior for damaged JSON files.

## GitHub usage

Initialize and publish the project using your own GitHub repository:

```bash
git init
git add .
git commit -m "Build Student Performance Analyzer"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-performance-analyzer.git
git push -u origin main
```

Replace the example remote with your repository URL. `.gitignore` excludes virtual environments, Python cache files, editor settings, and generated test artifacts. No credentials or API keys are needed.

# Python File Organizer

A command-line Python utility that automatically organizes files into folders based on their file extensions.

## Features

* Automatically creates folders if they don't exist
* Organizes files by extension
* Supports:

  * Text files (`.txt`)
  * PDF files (`.pdf`)
  * Python files (`.py`)
* Displays each file as it is moved

## Technologies Used

* Python 3
* `os` module
* `shutil` module

## How to Run

```bash
python3 file_organizer.py
```

When prompted, enter the path to the folder you want to organize.

Example:

```text
/Users/yourname/Desktop/TestFolder
```

## Example

Before:

```text
TestFolder/
├── notes.txt
├── report.pdf
├── hello.py
```

After:

```text
TestFolder/
├── Text Files/
│   └── notes.txt
├── PDF Files/
│   └── report.pdf
└── Python Files/
    └── hello.py
```

## What I Learned

* Working with files and directories using `os`
* Creating folders programmatically
* Moving files with `shutil`
* Using dictionaries to map file extensions to folders
* Automating repetitive tasks with Python

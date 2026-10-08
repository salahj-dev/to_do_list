<!-- # 📝 Python To-Do List CLI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Interface](https://img.shields.io/badge/Interface-CLI-orange)

A simple and lightweight **Command-Line To-Do List Manager** built with pure Python.

This project was created to practice Python fundamentals by building a real working application from scratch — without using AI to write the project code.

![Project Banner](./banner.png)

---

## ✨ Features

* ➕ **Add Task** — Add new tasks to the list.
* 👀 **View Tasks** — Display all tasks with their numbers.
* ✅ **Mark as Done** — Mark a task as completed.
* 🛑 **Prevent Double Marking** — A completed task cannot be marked again.
* 🗑️ **Delete Task** — Delete tasks using their index.
* 💾 **Save Tasks** — Save tasks to a text file.
* 📂 **Load Tasks** — Load previously saved tasks when starting the program.
* 🛡️ **Error Handling** — Handle invalid user input and invalid task indexes.
* 🚫 **Empty List Handling** — Prevent actions when there are no tasks.
* 🔢 **Input Validation** — Prevent invalid menu choices and invalid task numbers.
* ✏️ **Task Validation** — Prevent empty or invalid task input.

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash
python code.py
```

---

## 📋 Menu

```text
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit & Save
```

---

## 🧠 Problems I Solved

This project was not only about making a To-Do List. It was also about finding bugs, understanding why they happened, and fixing them.

### 1. ❌ Invalid Menu Input

The program could crash when the user entered something that was not a number.

**Solution:** Added `try/except` to handle `ValueError`.

---

### 2. 📭 Empty Task List

Some actions did not make sense when the task list was empty.

**Solution:** Added checks to detect when there are no tasks and display an appropriate message instead of continuing unnecessarily.

---

### 3. ✅ Double Marking Bug

A task could accidentally become:

```text
Learn Python ✅✅
```

**Solution:** Check the selected task itself before adding the check mark:

```python
if "✅" in taskes[task_num]:
    print("This task is already marked!")
else:
    taskes[task_num] += " ✅"
```

---

### 4. 🔢 Invalid Task Number

Entering a task number that does not exist could cause an `IndexError`.

**Solution:** Added validation and error handling for task indexes.

---

### 5. ➕ Invalid / Empty Task

The user could enter an empty task or invalid input.

**Solution:** Added validation before adding a task to the list.

---

### 6. ❓ Y/N Input Validation

The program needed to properly handle answers such as:

```text
Y
N
y
n
```

and reject unexpected answers.

**Solution:** Used validation loops with `while True`, `continue`, and `break` to control the input flow.

---

### 7. 💾 Save System

Tasks needed to remain available after closing the program.

**Solution:** Added file handling with:

```python
with open("Taskes.txt", "w", encoding="utf-8") as f:
```

and wrote the tasks to the file.

---

### 8. 📂 Load System

Saving the tasks was not enough. The program also needed to recover them when it started again.

**Solution:** Added a loading system that reads the saved tasks from `Taskes.txt` and puts them back into the task list.

---

### 9. 🔁 Loops & Program Flow

One of the biggest learning points was understanding how nested loops work.

I used:

* `while True`
* `for`
* `break`
* `continue`

to control menus, validation, and user input.

This helped me understand how to stop or restart a specific loop without stopping the entire program.

---

### 10. 🐛 Debugging

During development, several bugs appeared in the task marking, deleting, saving, loading, and input validation systems.

Instead of replacing the project with ready-made code, I worked through the problems and corrected them step by step.

---

## 🛠️ Python Concepts Used

This project uses Python fundamentals such as:

* Variables
* Lists
* Strings
* `if / elif / else`
* `while` loops
* `for` loops
* `break`
* `continue`
* `try / except`
* `ValueError`
* `IndexError`
* `enumerate()`
* `pop()`
* File handling
* `with open()`
* Reading and writing `.txt` files
* Basic input validation

---

## 📁 Project Structure

```text
TO-DO-LIST/
│
├── code.py
├── banner.png
├── README.md
└── Taskes.txt
```

> `Taskes.txt` is created/used by the program to store tasks.

---

## 🎯 Purpose of the Project

The main goal of this project was not to build a huge application.

The goal was to practice Python by building something functional from the ground up and learning how to solve problems when the code does not work as expected.

This project helped me understand that writing code is only one part of programming.

**Debugging, understanding errors, and solving problems are just as important.**

---

## 👨‍💻 Author

Made with ❤️ and a lot of debugging.

> **"I don't let AI code for me, I suffer to understand."** -->

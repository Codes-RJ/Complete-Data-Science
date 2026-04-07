# Python for Data Science 🐍

Welcome to the Python section! Python is the most popular programming language for data science. This section will take you from beginner to confident Python programmer.

---

## 📖 History of Python

Python was created by **Guido van Rossum** and first released in **1991**. The name comes from Monty Python, not the snake!

### Key Milestones
- **1991:** First release (version 0.9.0)
- **2000:** Python 2.0 released
- **2008:** Python 3.0 released (major overhaul, not backward compatible)
- **2020:** Python 2 officially retired
- **Today:** Python 3.8+ is standard for data science

### Why Python for Data Science?
- **Easy to learn:** Simple, readable syntax
- **Huge ecosystem:** Thousands of libraries
- **Community:** Massive global support
- **Versatility:** Web, data science, automation, AI
- **Industry adoption:** Google, Netflix, NASA, Spotify use Python

---

## 🎯 What is Python?

Python is a **high-level**, **interpreted**, **object-oriented** programming language known for its simplicity and readability.

### Key Characteristics
| Feature | Description |
|---------|-------------|
| **Interpreted** | Code runs line by line, no compilation needed |
| **Dynamically typed** | No need to declare variable types |
| **High-level** | Abstracts away complex details |
| **Batteries included** | Extensive standard library |
| **Cross-platform** | Works on Windows, Mac, Linux |

---

## 📚 What You'll Learn

- Python fundamentals (variables, data types, operators)
- Control flow and loops
- Functions and modules
- File handling and error management
- Object-oriented programming
- Advanced concepts for data science

---

## 📁 Section Structure

| File | Description |
|------|-------------|
| [01_tokens_and_barebones](./01_tokens_and_barebones) | Variables, keywords, comments ...etc |
| [02_data_types.md](./02_data_types.md) | Numbers, strings, lists, tuples, dictionaries, sets |
| [03_conditional_statements.md](./03_conditional_statements.md) | if-elif-else, ternary operators ... etc |
| [04_loop_statements.md](./04_loop_statements.md) | For loop, while loop, do while loop ...etc |
| [05_functions.md](./05_functions.md) | Defining functions, parameters, return values, scope |
| [06_modules_packages.md](./06_modules_packages.md) | Importing, creating modules, pip, virtual environments |
| [07_file_handling.md](./07_file_handling.md) | Reading/writing files, CSV, JSON |
| [08_error_exceptions.md](./08_error_exceptions.md) | Try-except, error handling, raising exceptions |
| [09_object_oriented_programming.md](./09_object_oriented_programming.md) | Classes, objects, inheritance, encapsulation |
| [10_list_comprehensions.md](./10_list_comprehensions.md) | Concise list creation, dictionary comprehensions |
| [11_lambda_functions.md](./11_lambda_functions.md) | Anonymous functions, map, filter, reduce |
| [12_iterators_generators.md](./12_iterators_generators.md) | Iterators, generators, yield |
| [13_decorators.md](./13_decorators.md) | Function decorators, use cases |
| [interview_questions.md](./interview_questions.md) | Common Python interview questions |

---

## 🎯 Prerequisites

- No prior programming experience needed
- A computer with Python installed (3.8 or higher)
- A code editor (VS Code recommended)
- Willingness to code along

---

## ⏱️ Estimated Time

- Reading and coding along: 15-20 hours
- Practice exercises: 10-15 hours
- Total: 25-35 hours

---

## 🚀 Setting Up Your Python Environment

### Step 1: Install Python

**Windows:**
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download Python 3.8 or higher
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Verify: Open Command Prompt, type `python --version`

**Mac:**
```bash
# Using Homebrew
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 2: Verify Installation
```bash
python --version
pip --version
```

---

## 🔧 Understanding Virtual Environments

### What is a Virtual Environment?
A virtual environment is an isolated Python environment that keeps dependencies separate for different projects. It prevents conflicts between package versions.

### Why Use Virtual Environments?
- **Isolation:** Each project has its own dependencies
- **Version control:** Different projects can use different package versions
- **Clean:** Avoids cluttering your system Python
- **Reproducibility:** Easy to recreate environments

### Creating a Virtual Environment

**Method 1: Using venv (built-in)**
```bash
# Navigate to your project folder
cd my_project

# Create virtual environment
python -m venv venv

# This creates a 'venv' folder with isolated Python
```

**Method 2: Using virtualenv (more features)**
```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv venv
```

### Activating Virtual Environment

| Platform | Command |
|----------|---------|
| **Windows (CMD)** | `venv\Scripts\activate.bat` |
| **Windows (PowerShell)** | `venv\Scripts\Activate.ps1` |
| **Mac/Linux** | `source venv/bin/activate` |

### After Activation
You'll see `(venv)` at the beginning of your terminal prompt:
```bash
(venv) user@computer:~/project$
```

### Deactivating
```bash
deactivate
```

### Managing Packages in Virtual Environment

```bash
# Install packages
pip install pandas numpy matplotlib

# List installed packages
pip list

# Export requirements
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Uninstall package
pip uninstall package_name
```

---

## 💻 Code Editors and IDEs

### VS Code (Recommended)
**Why VS Code?**
- Free and open source
- Excellent Python support
- Built-in terminal
- Git integration
- Jupyter notebook support

**Setup for Python:**
1. Download [VS Code](https://code.visualstudio.com/)
2. Install Python extension
3. Select Python interpreter (Ctrl+Shift+P → Python: Select Interpreter)
4. Open terminal (Ctrl+`)

### Jupyter Notebook
**Best for:** Data exploration, learning, sharing
```bash
# Install
pip install jupyter

# Launch
jupyter notebook
# or
jupyter lab
```

### PyCharm
**Best for:** Large projects, professional development
- Community edition is free
- Powerful debugging
- Integrated testing

### IDLE
- Comes with Python
- Good for beginners
- Simple interface

---

## 📦 Python Ecosystem for Data Science

### Core Libraries
| Library | Purpose |
|---------|---------|
| **NumPy** | Numerical computing, arrays |
| **Pandas** | Data manipulation, analysis |
| **Matplotlib** | Basic plotting |
| **Seaborn** | Statistical visualization |
| **Scikit-learn** | Machine learning |
| **TensorFlow/PyTorch** | Deep learning |

### Installation
```bash
# Install all at once
pip install numpy pandas matplotlib seaborn scikit-learn jupyter

# Or individually
pip install numpy
pip install pandas
```

---

## 🧠 Python Philosophy (The Zen of Python)

Run this in Python to see:
```python
import this
```

Key principles:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

---

## 🔍 Python Extensions for VS Code

Essential extensions:
1. **Python** (by Microsoft) - Core Python support
2. **Pylance** - Fast language server
3. **Jupyter** - Notebook support
4. **Python Indent** - Auto-indentation
5. **Better Comments** - Enhanced comment highlighting

---

## 📝 Python Syntax Basics

### Hello World
```python
print("Hello, Data Science!")
```

### Variables (No type declaration needed)
```python
name = "Alice"           # String
age = 25                 # Integer
height = 5.7             # Float
is_student = True        # Boolean
```

### Comments
```python
# Single line comment

"""
Multi-line comment
or docstring
"""
```

### Indentation (Python uses spaces, not braces!)
```python
if condition:
    # Indented block (4 spaces)
    print("This is inside")
# Back to normal
```

---

## 🎓 Learning Resources

### Official
- [Python.org](https://python.org) - Official documentation
- [Python Tutorial](https://docs.python.org/3/tutorial/) - Official tutorial

### Free Resources
- [W3Schools Python](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
- [Python for Everybody](https://www.py4e.com/)

### Practice Platforms
- [LeetCode](https://leetcode.com/) - Algorithm practice
- [HackerRank](https://www.hackerrank.com/) - Python challenges
- [Codewars](https://www.codewars.com/) - Gamified coding

---

## 🚀 How to Proceed

1. **Install Python** and set up virtual environment
2. **Install VS Code** and Python extensions
3. **Start with** [01_variables.md](./01_variables.md)
4. **Code along** with every example
5. **Complete exercises** at the end of each file
6. **Build mini-projects** as you learn
7. **Test knowledge** with interview questions

---

## ✅ Quick Test

After setup, run this to verify everything works:

```python
# test.py
import sys
print(f"Python version: {sys.version}")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("All imports successful!")
```

---

## ✏️ Reflection Questions

1. Why is Python popular for data science?
2. What is a virtual environment and why use it?
3. What's the difference between Python 2 and Python 3?
4. Which code editor will you use and why?

---

## 🎯 What You'll Be Able to Do After This Section

- Write Python scripts confidently
- Work with different data structures
- Create and use functions
- Handle errors gracefully
- Work with files
- Understand OOP concepts
- Manage packages with pip
- Use virtual environments
- Read and write Python code effectively

---

*Let's begin! Open [01_tokens_and_barebones](./01_tokens_and_barebones/README.md) to start your Python journey.*
# 📦 FUNCTIONS – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Functions?](#what-are-functions)
3. [Function Components](#function-components)
4. [Types of Functions](#types-of-functions)
5. [Quick Reference](#quick-reference)
6. [When to Use Functions](#when-to-use-functions)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Functions** are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs modular.

```python
# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

**Key Characteristics:**
- ✅ Reusable (write once, use many times)
- ✅ Modular (break complex problems into smaller pieces)
- ✅ Encapsulated (variables inside functions are local)
- ✅ Can accept inputs (parameters)
- ✅ Can return outputs (return values)

---

## 📖 What are Functions?

Functions are the building blocks of Python programs. They allow you to group code into logical, reusable units.

```python
# Function without parameters
def say_hello():
    print("Hello!")

# Function with parameters
def add(a, b):
    return a + b

# Function with default parameter
def greet(name="Guest"):
    return f"Hello, {name}"

# Function with multiple returns
def get_min_max(numbers):
    return min(numbers), max(numbers)
```

**Why Use Functions:**
- Avoid code duplication (DRY principle)
- Easier debugging and testing
- Better code organization
- Reusability across programs
- Separation of concerns

---

## 🔧 Function Components

| Component | Example | Description |
|-----------|---------|-------------|
| `def` keyword | `def my_func():` | Defines a function |
| Function name | `calculate_average` | Identifies the function |
| Parameters | `(a, b, c)` | Input values (optional) |
| Docstring | `"""Adds two numbers"""` | Documentation (optional) |
| Body | `return a + b` | Code to execute |
| Return | `return result` | Output value (optional) |

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate area of a rectangle.

    Args:
        length: Length of rectangle
        width: Width of rectangle

    Returns:
        Area of rectangle
    """
    return length * width
```

---

## 📚 Types of Functions

### 1. Built-in Functions

```python
# Python comes with many built-in functions
print("Hello")           # print()
len([1, 2, 3])          # len()
type(42)                # type()
sum([1, 2, 3])          # sum()
max([1, 2, 3])          # max()
min([1, 2, 3])          # min()
```

### 2. User-Defined Functions

```python
# Functions you create yourself
def square(x):
    return x ** 2

def is_even(n):
    return n % 2 == 0
```

### 3. Lambda Functions (Anonymous)

```python
# One-line functions without a name
square = lambda x: x ** 2
add = lambda a, b: a + b

# Often used with map/filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
```

### 4. Generator Functions

```python
# Functions that yield values instead of returning
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4
```

### 5. Recursive Functions

```python
# Functions that call themselves
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

## 📊 Quick Reference

### Function Syntax

```python
def function_name(parameter1, parameter2=default):
    """Docstring"""
    # Function body
    return value
```

### Parameter Types

| Type | Syntax | Example |
|------|--------|---------|
| Positional | `def f(a, b):` | `f(1, 2)` |
| Default | `def f(a, b=10):` | `f(5)` |
| `*args` | `def f(*args):` | `f(1,2,3)` |
| `**kwargs` | `def f(**kwargs):` | `f(x=1, y=2)` |
| Keyword-only | `def f(*, a, b):` | `f(a=1, b=2)` |

### Return Types

```python
# Single return
def add(a, b):
    return a + b

# Multiple returns (as tuple)
def get_name():
    return "Alice", 30  # Returns tuple

# No return (returns None)
def say_hello():
    print("Hello")  # Returns None
```

---

## 📁 When to Use Functions

| Use Case | Example | Why |
|----------|---------|-----|
| Repeated code | `calculate_tax(amount)` | Avoid duplication |
| Complex operations | `process_data(data)` | Break down complexity |
| Validation | `validate_email(email)` | Reusable checks |
| Calculations | `area_circle(radius)` | Mathematical formulas |
| Callbacks | `button.on_click(handler)` | Event handling |
| Data transformation | `format_date(date)` | Consistent formatting |

### Real-World Examples

```python
# Validation function
def is_valid_email(email):
    return '@' in email and '.' in email

# Data processing function
def clean_text(text):
    return text.strip().lower()

# Calculation function
def calculate_discount(price, percent):
    return price * (1 - percent / 100)

# API call function
def fetch_user(user_id):
    response = requests.get(f"/users/{user_id}")
    return response.json()
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `functions_basics.md` | Complete basics guide |
| `functions_advanced.md` | Closures, decorators, functools |
| `main_and_name.md` | `__main__` and `__name__` explained |
| `functional_tools.md` | `map()`, `filter()`, `reduce()`, `zip()` |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 🚀 Quick Start

```bash
# Start with basics
cat functions_basics.md

# Then learn advanced topics
cat functions_advanced.md

# Understand __main__
cat main_and_name.md

# Practice with exercises
cat exercises.md
```

---

## 💡 Quick Tips

```python
# ✅ DO: Use descriptive names
def calculate_average(scores):
    return sum(scores) / len(scores)

# ❌ DON'T: Use vague names
def f(x):
    return sum(x) / len(x)

# ✅ DO: Keep functions small
def validate_email(email):
    return '@' in email

# ❌ DON'T: Do too many things
def process_user(user):
    validate_email()
    save_to_db()
    send_email()

# ✅ DO: Use docstrings
def divide(a, b):
    """Divide a by b. Raises error if b is zero."""
    return a / b
```

---

## 📚 Next Steps

- Go to [01_functions_basics.md](01_functions_basics.md) for starting with understanding the functions.

---

## 🔗 Related Topics

- **Lambda Functions** – Anonymous one-liners
- **Decorators** – Functions that modify functions
- **Generators** – Functions that yield values
- **Recursion** – Functions that call themselves
- **Scope** – Local vs global variables
- **Modules** – Organizing functions into files

---

*Master functions to write organized, reusable, and maintainable code! 🐍✨*

---
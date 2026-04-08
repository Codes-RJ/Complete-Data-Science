# Comments in Python 💬

---

## What are Comments?

Comments are annotations in code that are ignored by the Python interpreter. They are meant for humans to read and understand the code better. Think of them as sticky notes you leave for yourself or other developers.

```python
# This is a comment - Python ignores this
print("Hello")  # This explains what the code does
```

---

## Why Comments are Important

### 1. Code Documentation
Comments explain what code does, why it exists, and how to use it.

### 2. Improved Readability
Well-commented code is easier to understand and maintain.

### 3. Debugging
Comments can temporarily disable code to isolate problems.

### 4. Collaboration
Team members understand each other's code faster.

### 5. Future Reference
Your future self will thank you for leaving comments.

### 6. Onboarding New Developers
New team members learn codebase faster with good comments.

---

## Types of Comments in Python

| Type | Syntax | Use Case |
|------|--------|----------|
| Single-line | `#` | Brief explanations |
| Inline | `#` after code | Explain specific lines |
| Multi-line | Triple quotes `""" """` | Long explanations, docstrings |
| Block | Multiple `#` lines | Detailed documentation |
| TODO | `# TODO:` | Mark pending work |
| FIXME | `# FIXME:` | Mark bugs to fix |
| Docstring | `""" """` at function/class start | API documentation |

---

## 1. Single-Line Comments

Start with `#` and continue to the end of the line.

```python
# This is a single-line comment
# Python ignores everything after the # symbol

# Calculate the area of a circle
radius = 5
area = 3.14159 * radius ** 2
print(area)

# You can have blank comments for spacing
#
# This helps organize code sections
#
```

---

## 2. Inline Comments

Comments placed on the same line as code.

```python
x = 10          # Initialize x with value 10
y = 20          # Initialize y with value 20
result = x + y  # Calculate sum

# Good inline comment - explains why
total = price * quantity  # Calculate total cost with tax included

# Bad inline comment - states the obvious
age = 25  # Set age to 25 (Don't do this)

# Multiple inline comments
name = "Alice"   # User's first name
age = 30         # User's age in years
city = "NYC"     # User's location
```

---

## 3. Multi-Line Comments

### Method 1: Multiple Single-Line Comments
```python
# This is a multi-line comment
# using multiple single-line comment symbols
# Each line must start with #
# This is the most common way

# This function calculates the factorial of a number
# It uses recursion to compute the result
# The base case is when n is 0 or 1
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Method 2: Triple Quotes (String Literal)
```python
"""
This is a multi-line comment using triple quotes.
Python ignores this string literal if not assigned.
This works but is technically a string, not a comment.
"""

"""
This function greets a user.
Parameters:
    name: The user's name
Returns:
    A greeting message
"""
def greet(name):
    return f"Hello, {name}"
```

**Note:** Triple quotes are actually string literals. They work as comments when not assigned to a variable, but they are not true comments.

---

## 4. Block Comments

Used to explain complex sections of code.

```python
# ============================================
# USER AUTHENTICATION SECTION
# ============================================
# This section handles user login and registration
# Includes password hashing and token generation
# ============================================

def login(username, password):
    # Validate credentials
    # Generate JWT token
    # Return user session
    pass

# --------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------
# Establish connection to PostgreSQL database
# Connection pool size: 10
# Timeout: 30 seconds
# --------------------------------------------
```

---

## 5. TODO Comments

Mark tasks that need to be completed.

```python
# TODO: Add error handling for invalid input
# TODO: Optimize this loop for better performance
# TODO: Update documentation after refactoring

def process_data(data):
    # TODO: Implement validation for empty data
    # FIXME: This function crashes with negative numbers
    # BUG: Returns wrong result for large datasets
    pass

# TODO(Alice): Review this logic
# TODO(@username): Add unit tests
# TODO(BUG-1234): Fix edge case when x is zero
```

---

## 6. FIXME and BUG Comments

Mark known issues that need fixing.

```python
# FIXME: This calculation is incorrect for negative values
# BUG: Memory leak when processing large files
# HACK: Temporary solution until refactoring

def calculate_average(numbers):
    # FIXME: Division by zero when list is empty
    return sum(numbers) / len(numbers)

# NOTE: This is a workaround for Python 3.7 compatibility
# XXX: This code is deprecated, remove in next version
```

---

## 7. Docstrings (Documentation Strings)

Special comments used to document functions, classes, and modules.

### Function Docstring
```python
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
        radius (float): The radius of the circle
    
    Returns:
        float: The area of the circle
    
    Example:
        >>> calculate_area(5)
        78.53975
    """
    return 3.14159 * radius ** 2

# Access docstring
help(calculate_area)
print(calculate_area.__doc__)
```

### Class Docstring
```python
class BankAccount:
    """
    A class representing a bank account.
    
    Attributes:
        owner (str): Name of the account owner
        balance (float): Current account balance
    
    Methods:
        deposit(amount): Add money to account
        withdraw(amount): Remove money from account
    """
    
    def __init__(self, owner, balance=0):
        """
        Initialize a new bank account.
        
        Args:
            owner (str): Account owner's name
            balance (float): Initial balance (default 0)
        """
        self.owner = owner
        self.balance = balance
```

### Module Docstring
```python
"""
This module provides mathematical utility functions.

Functions:
    add(a, b) - Returns sum of two numbers
    subtract(a, b) - Returns difference of two numbers
    multiply(a, b) - Returns product of two numbers

Author: Alice Johnson
Version: 1.0.0
Date: 2024-01-15
"""

def add(a, b):
    return a + b
```

---

## Comment Formats and Styles

### Section Headers
```python
# ============================================
# IMPORTS
# ============================================

import pandas as pd
import numpy as np

# ============================================
# CONFIGURATION
# ============================================

MAX_RETRIES = 3
TIMEOUT = 30

# ============================================
# HELPER FUNCTIONS
# ============================================

def helper():
    pass
```

### Parameter Documentation
```python
def create_user(name, age, email):
    # Parameters:
    #   name  - str: User's full name
    #   age   - int: User's age in years
    #   email - str: User's email address
    pass
```

### Algorithm Explanation
```python
def binary_search(arr, target):
    """
    Binary search algorithm implementation.
    
    Steps:
    1. Find middle element of sorted array
    2. If middle equals target, return index
    3. If target < middle, search left half
    4. If target > middle, search right half
    5. Repeat until element found or search space exhausted
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Target not found
```

---

## Commenting Best Practices

### ✅ DO:

```python
# Calculate total price including 10% tax
total = price * quantity * 1.10

# Check if user is eligible for discount
if age >= 65 or is_member:
    apply_discount()

# Temporary fix for API rate limiting
# Remove after backend update
time.sleep(1)

# TODO: Add validation for empty input
def process(data):
    pass
```

### ❌ DON'T:

```python
# Don't state the obvious
x = 5  # Set x to 5 (Don't do this)

# Don't write outdated comments
# This function adds two numbers (but it multiplies now)
def calculate(a, b):
    return a * b  # Actually multiplies

# Don't use comments instead of clear code
# Check if x is greater than 5 and less than 10
if x > 5 and x < 10:  # Code is already clear
    pass

# Don't write very long lines
# This is a very long comment that goes on and on and on and on and on and should probably be broken into multiple lines for better readability
```

---

## Commenting Out Code for Debugging

```python
# Temporarily disable code to test something
# result = complex_calculation(x, y)
result = simple_calculation(x, y)  # Testing alternative approach

# Comment out print statements during debugging
# print("Debug: Value of x is", x)
# print("Debug: Value of y is", y)

# Disable a whole block
"""
for i in range(100):
    process(i)
    update_database(i)
    send_notification(i)
"""

# Alternative: Use if False
if False:
    # This code won't run
    expensive_operation()
    database_update()
```

---

## Special Comment Tags

| Tag | Purpose |
|-----|---------|
| `# TODO:` | Task to complete |
| `# FIXME:` | Bug to fix |
| `# BUG:` | Known issue |
| `# HACK:` | Temporary workaround |
| `# NOTE:` | Important information |
| `# XXX:` | Danger or important |
| `# OPTIMIZE:` | Performance improvement needed |
| `# DEPRECATED:` | Code to remove |

```python
# TODO: Add input validation
# FIXME: Handle division by zero
# BUG: Returns wrong value for negative inputs
# HACK: Using sleep to bypass rate limit
# NOTE: This function is critical for authentication
# XXX: This code is not thread-safe
# OPTIMIZE: Reduce time complexity from O(n²) to O(n log n)
# DEPRECATED: Use new_process() instead
```

---

## Viewing Comments and Docstrings

```python
# Get docstring of a function
print(print.__doc__)
help(len)

# Get docstring of a module
import math
print(math.__doc__)

# Get docstring of a class
print(str.__doc__)

# Custom docstring
def my_function():
    """This is my custom docstring."""
    pass

print(my_function.__doc__)  # This is my custom docstring.
help(my_function)
```

---

## Practice Exercises

### Exercise 1: Add Comments
Add appropriate comments to this code:

```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    else:
        return "Overweight"
```

**Solution:**
```python
def calculate_bmi(weight, height):
    """
    Calculate BMI and return category.
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        str: BMI category (Underweight/Normal/Overweight)
    """
    # BMI formula: weight (kg) / height² (m²)
    bmi = weight / (height ** 2)
    
    # Categorize based on standard BMI ranges
    if bmi < 18.5:
        return "Underweight"   # Below healthy range
    elif bmi < 25:
        return "Normal"        # Healthy weight range
    else:
        return "Overweight"    # Above healthy range
```

### Exercise 2: Write Docstring
Write a docstring for this function:

```python
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
```

**Solution:**
```python
def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Parameters:
        numbers (list): A list of numeric values
    
    Returns:
        int or float: The largest value in the list
    
    Raises:
        IndexError: If the list is empty
    
    Example:
        >>> find_maximum([3, 7, 2, 9, 1])
        9
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
```

### Exercise 3: Add TODO Comments
Add TODO comments to mark improvements:

```python
def process_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data
```

**Solution:**
```python
def process_file(filename):
    # TODO: Add error handling for file not found
    # TODO: Support different file encodings
    # FIXME: Memory issue with large files
    # OPTIMIZE: Read file in chunks instead of all at once
    
    with open(filename, 'r') as file:
        data = file.read()
    return data
```

---

## Key Takeaways

- Comments explain code to humans, ignored by Python
- Single-line `#` is most common
- Triple quotes for docstrings and multi-line comments
- Use comments to explain WHY, not WHAT
- Keep comments updated with code changes
- Use TODO and FIXME to track pending work
- Good comments improve code maintainability
- Docstrings generate automatic documentation

---

## Next Steps

- Proceed to [02_data_types](/05_python/02_data_types/README.md) to learn about data types in Python
- Practice writing well-commented code

---

*"Code tells you how; comments tell you why."*
# 📘 CREATING MODULES – COMPLETE GUIDE

## 📌 Table of Contents
01. [What is a Module?](#what-is-a-module)
02. [Creating a Simple Module](#creating-a-simple-module)
03. [Using a Module](#using-a-module)
04. [Module Attributes](#module-attributes)
05. [`__name__` Variable](#__name__-variable)
06. [Module Search Path](#module-search-path)
07. [Reloading Modules](#reloading-modules)
08. [Real-World Examples](#real-world-examples)
09. [Common Pitfalls](#common-pitfalls)
10. [Practice Exercises](#practice-exercises)

---

## What is a Module?

A **module** is a single Python file (`.py`) that contains functions, classes, variables, and runnable code. Modules allow you to organize your code into reusable pieces.

```python
# mymodule.py - a simple module
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b
```

**Why Use Modules:**
- ✅ Reusability - write once, use many times
- ✅ Organization - group related code together
- ✅ Namespace management - avoid naming conflicts
- ✅ Maintainability - easier to debug and update
- ✅ Sharing - distribute your code to others

---

## Creating a Simple Module

### Step 1: Create a Python File

Create a file called `mymath.py`:

```python
# mymath.py
"""
My personal math module with useful functions.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to power b."""
    return a ** b

# Module constants
PI = 3.14159
E = 2.71828

# Module variable
_version = "1.0.0"
```

### Step 2: Use the Module

Create another file in the same directory:

```python
# main.py
import mymath

# Use functions from the module
print(mymath.add(5, 3))        # 8
print(mymath.multiply(4, 5))   # 20
print(mymath.PI)               # 3.14159

# Use with alias
result = mymath.divide(10, 2)
print(result)                  # 5.0
```

---

## Using a Module

### Different Import Styles

```python
# Style 1: Import entire module
import mymath
print(mymath.add(5, 3))

# Style 2: Import with alias
import mymath as mm
print(mm.add(5, 3))

# Style 3: Import specific items
from mymath import add, multiply
print(add(5, 3))
print(multiply(4, 5))

# Style 4: Import all (not recommended)
from mymath import *
print(add(5, 3))
print(PI)

# Style 5: Import with different name
from mymath import add as addition
print(addition(5, 3))
```

### Importing Multiple Items

```python
# Multiple imports
from mymath import add, subtract, multiply, divide

# Import with alias
from mymath import power as pow_func

# Import constants
from mymath import PI, E
```

---

## Module Attributes

Every module has special attributes that provide information about the module.

### Common Module Attributes

```python
# mymath.py
def add(a, b):
    return a + b

PI = 3.14159

# In another file
import mymath

# Module name
print(mymath.__name__)          # 'mymath'

# Module docstring
print(mymath.__doc__)           # 'My personal math module...'

# Module file path
print(mymath.__file__)          # '/path/to/mymath.py'

# Module dictionary (all attributes)
print(mymath.__dict__.keys())

# List all names in module
print(dir(mymath))
```

### Complete Example

```python
# mymodule.py
"""
This is my custom module.
It provides greeting functions.
"""

__version__ = "1.0.0"
__author__ = "Python Developer"

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def farewell(name):
    """Return a farewell message."""
    return f"Goodbye, {name}!"

# Module attributes
print(f"Module name: {__name__}")
print(f"Module docstring: {__doc__}")
print(f"Module version: {__version__}")
```

```python
# main.py
import mymodule

print(f"Module name: {mymodule.__name__}")      # mymodule
print(f"Module version: {mymodule.__version__}") # 1.0.0
print(f"Module author: {mymodule.__author__}")   # Python Developer
print(dir(mymodule))  # List all attributes
```

---

## `__name__` Variable

The `__name__` variable tells you how the module is being used.

### How `__name__` Works

```python
# mymodule.py
print(f"__name__ = {__name__}")

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("This runs only when executed directly")
    print(greet("World"))
```

**When run directly:**
```bash
python mymodule.py
# Output:
# __name__ = __main__
# This runs only when executed directly
# Hello, World!
```

**When imported:**
```python
import mymodule
# Output:
# __name__ = mymodule
# (No "This runs only..." message)
```

### The `if __name__ == "__main__"` Pattern

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test code - only runs when script is executed directly
if __name__ == "__main__":
    print("Testing calculator functions:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
```

**Benefits:**
- Module can be both imported and run as a script
- Test code doesn't run when imported
- Can include demo or self-test functionality

---

## Module Search Path

Python looks for modules in specific locations.

### `sys.path` - The Search Path

```python
import sys

# Print the module search path
for path in sys.path:
    print(path)

# Typical order:
# 1. Current directory
# 2. PYTHONPATH environment variable directories
# 3. Standard library directories
# 4. Site-packages directories
```

### Adding Custom Paths

```python
import sys

# Method 1: Append to sys.path
sys.path.append('/path/to/my/modules')
import mymodule

# Method 2: Insert at beginning (higher priority)
sys.path.insert(0, '/path/to/my/modules')

# Method 3: Set PYTHONPATH environment variable (outside Python)
# export PYTHONPATH="/path/to/my/modules:$PYTHONPATH"
```

### Module Search Order

```python
# Python searches for modules in this order:
# 1. Current directory
# 2. Directories in PYTHONPATH
# 3. Standard library directories
# 4. Site-packages (third-party modules)

# Check where a module was found
import math
print(math.__file__)  # Path to math module

import sys
print(sys.path)       # All search paths
```

---

## Reloading Modules

If you modify a module after importing, you need to reload it.

### Using `importlib.reload()`

```python
# mymodule.py (initial version)
def greet():
    return "Hello"
```

```python
# main.py
import mymodule

print(mymodule.greet())  # Hello

# Modify mymodule.py to return "Hi" instead of "Hello"
# Then reload:

import importlib
importlib.reload(mymodule)

print(mymodule.greet())  # Hi
```

### When Reload is Needed

```python
# During development
import mymodule
import importlib

# After editing mymodule.py
importlib.reload(mymodule)

# In Jupyter/IPython notebooks
# %load_ext autoreload
# %autoreload 2
```

---

## Real-World Examples

### Example 1: String Utilities Module

```python
# string_utils.py
"""
String manipulation utilities module.
"""

__version__ = "1.0.0"
__author__ = "Python Developer"

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def count_vowels(s):
    """Count vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Check if string is palindrome."""
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

def capitalize_words(s):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in s.split())

def remove_duplicates(s):
    """Remove duplicate characters while preserving order."""
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    # Demo / test code
    print("Testing string_utils module:")
    print(f"reverse_string('hello'): {reverse_string('hello')}")
    print(f"count_vowels('hello'): {count_vowels('hello')}")
    print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
    print(f"capitalize_words('hello world'): {capitalize_words('hello world')}")
    print(f"remove_duplicates('hello'): {remove_duplicates('hello')}")
```

```python
# main.py
import string_utils as su

text = "A man a plan a canal panama"
print(f"Original: {text}")
print(f"Reversed: {su.reverse_string(text)}")
print(f"Vowels: {su.count_vowels(text)}")
print(f"Palindrome: {su.is_palindrome(text)}")
```

### Example 2: Data Validation Module

```python
# validators.py
"""
Data validation functions module.
"""

import re

__all__ = ['validate_email', 'validate_phone', 'validate_age', 'validate_required']

def validate_email(email):
    """Validate email format."""
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """Validate phone number (10 digits)."""
    if not phone:
        return False
    digits = ''.join(filter(str.isdigit, phone))
    return len(digits) == 10

def validate_age(age):
    """Validate age (0-150)."""
    try:
        age = int(age)
        return 0 <= age <= 150
    except (ValueError, TypeError):
        return False

def validate_required(value):
    """Check if required field has value."""
    return bool(value and str(value).strip())

def validate_username(username):
    """Validate username (alphanumeric + underscore, 3-20 chars)."""
    if not username:
        return False
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return bool(re.match(pattern, username))

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

if __name__ == "__main__":
    print("Testing validators module:")
    print(f"validate_email('user@example.com'): {validate_email('user@example.com')}")
    print(f"validate_phone('555-123-4567'): {validate_phone('555-123-4567')}")
    print(f"validate_age(25): {validate_age(25)}")
    print(f"validate_username('john_doe'): {validate_username('john_doe')}")
    print(f"validate_password('Str0ngP@ss'): {validate_password('Str0ngP@ss')}")
```

```python
# main.py
from validators import *

# Validate user input
email = "alice@example.com"
phone = "555-123-4567"
age = 30
username = "alice123"

print(f"Email valid: {validate_email(email)}")
print(f"Phone valid: {validate_phone(phone)}")
print(f"Age valid: {validate_age(age)}")
print(f"Username valid: {validate_username(username)}")
```

### Example 3: Configuration Module

```python
# config.py
"""
Configuration settings module.
"""

import os
import json

# Default configuration
DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp",
        "user": "admin",
        "password": "secret"
    }
}

# Current configuration
_config = DEFAULT_CONFIG.copy()

def load_config(filepath):
    """Load configuration from JSON file."""
    global _config
    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            _config = _merge_config(_config, user_config)
        return True
    except FileNotFoundError:
        print(f"Config file {filepath} not found, using defaults")
        return False
    except json.JSONDecodeError:
        print(f"Error parsing {filepath}")
        return False

def _merge_config(default, override):
    """Deep merge two dictionaries."""
    result = default.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _merge_config(result[key], value)
        else:
            result[key] = value
    return result

def get(key, default=None):
    """Get configuration value using dot notation."""
    keys = key.split('.')
    value = _config
    for k in keys:
        if isinstance(value, dict):
            value = value.get(k)
            if value is None:
                return default
        else:
            return default
    return value

def set_config(key, value):
    """Set configuration value using dot notation."""
    global _config
    keys = key.split('.')
    target = _config
    for k in keys[:-1]:
        if k not in target:
            target[k] = {}
        target = target[k]
    target[keys[-1]] = value

def get_all():
    """Get all configuration."""
    return _config.copy()

def reset():
    """Reset to default configuration."""
    global _config
    _config = DEFAULT_CONFIG.copy()

if __name__ == "__main__":
    print("Testing config module:")
    print(f"host: {get('host')}")
    print(f"port: {get('port')}")
    print(f"database.host: {get('database.host')}")
    
    set_config("debug", True)
    print(f"debug: {get('debug')}")
    
    print(f"All config: {get_all()}")
```

```python
# main.py
import config

# Load configuration
config.load_config("settings.json")

# Use configuration
host = config.get("host")
port = config.get("port")
db_host = config.get("database.host")

print(f"Server running on {host}:{port}")
print(f"Database at {db_host}")

# Update configuration
config.set_config("debug", True)
```

---

## Common Pitfalls

### Pitfall 1: Circular Imports

```python
# module_a.py
import module_b

def func_a():
    return module_b.func_b()

# module_b.py
import module_a

def func_b():
    return module_a.func_a()

# This creates a circular import!
```

**Solution:** Restructure code or import inside function.

### Pitfall 2: Importing with `*` (Wildcard)

```python
# ❌ Bad - pollutes namespace
from math import *
print(sqrt(25))  # Works, but where did sqrt come from?

# ✅ Good - explicit imports
from math import sqrt
print(sqrt(25))

# ✅ Good - import module
import math
print(math.sqrt(25))
```

### Pitfall 3: Module Name Conflicts

```python
# ❌ Don't name your module same as built-in
# math.py (your custom module)
def add(a, b):
    return a + b

# main.py
import math  # This imports YOUR math.py, not built-in!
print(math.sqrt(25))  # AttributeError!
```

### Pitfall 4: Forgetting `if __name__ == "__main__"`

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# Test code runs when imported!
print(greet("World"))  # This prints on import!

# ✅ Fix
if __name__ == "__main__":
    print(greet("World"))  # Only runs when executed directly
```

---

## Practice Exercises

### Beginner Level

1. **Simple Greeting Module**
   ```python
   # Create a module called greetings.py with:
   # - say_hello(name) function
   # - say_goodbye(name) function
   # - DEFAULT_GREETING constant
   ```

2. **Math Utilities Module**
   ```python
   # Create a module called math_utils.py with:
   # - is_even(n)
   # - is_odd(n)
   # - is_prime(n)
   ```

3. **Temperature Module**
   ```python
   # Create a module called temp.py with:
   # - celsius_to_fahrenheit(c)
   # - fahrenheit_to_celsius(f)
   ```

### Intermediate Level

4. **String Utilities Module**
   ```python
   # Create a module with string functions:
   # - count_words(text)
   # - most_common_word(text)
   # - average_word_length(text)
   ```

5. **List Utilities Module**
   ```python
   # Create a module with list functions:
   # - chunk_list(lst, size)
   # - flatten_list(nested_list)
   # - unique_preserve_order(lst)
   ```

6. **File Utilities Module**
   ```python
   # Create a module for file operations:
   # - read_file(filename)
   # - write_file(filename, content)
   # - append_file(filename, content)
   ```

### Advanced Level

7. **Configuration Module**
   ```python
   # Create a config module that:
   # - Loads from JSON file
   # - Supports nested keys with dot notation
   # - Has default values
   ```

8. **Logging Module**
   ```python
   # Create a logging module with:
   # - Different log levels (INFO, WARNING, ERROR)
   # - Log to file or console
   # - Timestamp on each log entry
   ```

9. **Data Validator Module**
   ```python
   # Create a validation module with:
   # - Multiple validator functions
   # - Schema validation
   # - Error message collection
   ```

---

## Quick Reference Card

```python
# Create a module (save as mymodule.py)
def my_function():
    return "Hello"

PI = 3.14159

if __name__ == "__main__":
    print("Testing...")

# Import module
import mymodule
import mymodule as mm
from mymodule import my_function
from mymodule import my_function as mf
from mymodule import *

# Module attributes
mymodule.__name__      # Module name
mymodule.__file__      # File path
mymodule.__doc__       # Docstring
dir(mymodule)          # List attributes

# Reload module
import importlib
importlib.reload(mymodule)

# Module search path
import sys
sys.path               # List of paths
sys.path.append("/my/path")
```

---

## Next Step

- Move to [02_import_statement.md](02_import_statement.md) to learn advanced import techniques.

---

*Master modules to organize your code effectively! 🐍✨*
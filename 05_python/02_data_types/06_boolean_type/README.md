# ✓ BOOLEAN TYPE (bool) – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Booleans?](#what-are-booleans)
3. [Quick Reference](#quick-reference)
4. [Truthy and Falsy Values](#truthy-and-falsy-values)
5. [Boolean Operations](#boolean-operations)
6. [Comparison Operators](#comparison-operators)
7. [When to Use Booleans](#when-to-use-booleans)
8. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Booleans** represent one of two values: `True` or `False`. They are the foundation of logical operations and control flow in Python.

| Feature | Description | Example |
|---------|-------------|---------|
| **Type** | `bool` | `True`, `False` |
| **Values** | Two possible values | `True` or `False` |
| **Mutable?** | ❌ Immutable | Cannot be changed |
| **Subclass of** | `int` | `True == 1`, `False == 0` |
| **Use Case** | Conditions, flags, comparisons | `if is_valid:` |

```python
# Examples of booleans
is_active = True
is_deleted = False
has_permission = True

# Boolean expressions
result = 10 > 5        # True
is_equal = (5 == 5)    # True
is_valid = name != ""  # False if empty string
```

**Key Characteristics:**
- ✅ Only two values: `True` and `False`
- ✅ Subclass of `int` (`True` = 1, `False` = 0)
- ✅ Used in conditional statements (`if`, `while`)
- ✅ Results of comparison operators
- ✅ Can be combined with logical operators (`and`, `or`, `not`)

---

## ✓ What are Booleans?

Booleans are named after George Boole, who developed Boolean algebra. In Python, `bool` is a subclass of `int`.

```python
# Boolean values
is_true = True
is_false = False

# Check type
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# Boolean as integer (subclass of int)
print(issubclass(bool, int))  # True
print(int(True))    # 1
print(int(False))   # 0
print(True + True)  # 2
print(True * 10)    # 10

# Boolean from other types
print(bool(1))      # True
print(bool(0))      # False
print(bool("hello")) # True
print(bool(""))     # False
```

---

## 📊 Quick Reference

### Creating Booleans

```python
# Direct assignment
is_active = True
is_deleted = False

# From comparison operators
is_greater = 10 > 5      # True
is_equal = 5 == 5        # True
is_valid = "yes" != "no" # True

# From bool() constructor
print(bool(1))       # True
print(bool(0))       # False
print(bool("text"))  # True
print(bool(""))      # False
print(bool([1,2]))   # True
print(bool([]))      # False
print(bool(None))    # False
```

### Boolean Operations

```python
# Logical AND (both must be True)
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Logical OR (at least one True)
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Logical NOT (negation)
print(not True)         # False
print(not False)        # True
```

### Comparison Operators

```python
a, b = 10, 20

# Equality
print(a == b)   # False
print(a == 10)  # True

# Inequality
print(a != b)   # True
print(a != 10)  # False

# Greater than / Less than
print(a > b)    # False
print(a < b)    # True
print(a >= 10)  # True
print(a <= 5)   # False
```

---

## 🔍 Truthy and Falsy Values

In Python, every value can be evaluated as `True` or `False` in a boolean context.

### Falsy Values (Evaluate to False)

```python
# These all evaluate to False
print(bool(None))      # False
print(bool(False))     # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False
print(bool(""))        # False (empty string)
print(bool([]))        # False (empty list)
print(bool(()))        # False (empty tuple)
print(bool({}))        # False (empty dict)
print(bool(set()))     # False (empty set)
print(bool(range(0)))  # False (empty range)
```

### Truthy Values (Evaluate to True)

```python
# These all evaluate to True
print(bool(True))      # True
print(bool(1))         # True
print(bool(-1))        # True
print(bool(3.14))      # True
print(bool("hello"))   # True
print(bool([1, 2]))    # True
print(bool((1, 2)))    # True
print(bool({"a": 1}))  # True
print(bool({1, 2}))    # True
```

### Using Truthy/Falsy in Conditions

```python
# ✅ Pythonic way - use truthy/falsy directly
name = "Alice"
if name:  # Checks if name is not empty
    print(f"Hello, {name}")

# ❌ Less Pythonic - unnecessary comparison
if name != "":
    print(f"Hello, {name}")

# ✅ Check if list is empty
items = []
if not items:  # True if empty
    print("No items found")

# ❌ Less Pythonic
if len(items) == 0:
    print("No items found")

# ✅ Check if value exists
value = get_value()
if value:
    print(f"Value: {value}")
else:
    print("No value")

# Real use: Default values
name = user_input or "Guest"  # If user_input empty, use "Guest"
```

---

## 🔗 Boolean Operations

### `and` Operator

Returns `True` only if **both** operands are `True`.

```python
# Truth table
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Short-circuit evaluation (stops at first False)
def check_true():
    print("Checking True")
    return True

def check_false():
    print("Checking False")
    return False

result = check_false() and check_true()  # Only check_false() runs
# Output: Checking False

# Real use: Multiple conditions
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")

# Chaining and
if all([condition1, condition2, condition3]):
    print("All conditions met")
```

### `or` Operator

Returns `True` if **at least one** operand is `True`.

```python
# Truth table
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Short-circuit evaluation (stops at first True)
def check_true():
    print("Checking True")
    return True

def check_false():
    print("Checking False")
    return False

result = check_true() or check_false()  # Only check_true() runs
# Output: Checking True

# Real use: Default values
name = input("Enter name: ") or "Guest"
print(f"Hello, {name}")

# Real use: Multiple conditions
if user.is_admin or user.is_moderator or user.is_owner:
    print("Has elevated privileges")

# Chaining or
if any([condition1, condition2, condition3]):
    print("At least one condition met")
```

### `not` Operator

Returns the opposite boolean value.

```python
# Basic usage
print(not True)     # False
print(not False)    # True
print(not 10 > 5)   # False
print(not 10 < 5)   # True

# Real use: Negating conditions
is_weekend = False
if not is_weekend:
    print("Time for work")

# Real use: Checking if empty
items = []
if not items:
    print("List is empty")

# Real use: Toggle boolean flag
is_active = True
is_active = not is_active  # False
is_active = not is_active  # True
```

### Operator Precedence

```python
# Order: not > and > or
# not has highest precedence, then and, then or

# Without parentheses
result = True or False and not False
# Evaluated as: True or (False and (not False))
# = True or (False and True)
# = True or False
# = True

# With parentheses for clarity
result = True or (False and (not False))
print(result)  # True

# Better: Use parentheses for clarity
if (user.is_active and user.has_permission) or user.is_admin:
    print("Access granted")
```

---

## 📁 When to Use Booleans

| Use Case | Example | Why |
|----------|---------|-----|
| **Flags/States** | `is_active = True` | Track binary states |
| **Conditions** | `if user.is_authenticated:` | Control flow |
| **Loop control** | `while running:` | Control loops |
| **Function returns** | `def is_valid(data):` | Indicate success/failure |
| **Feature toggles** | `DEBUG = False` | Enable/disable features |
| **Validation results** | `is_email_valid = True` | Validation status |
| **Settings** | `notifications_enabled = True` | User preferences |

### Real-World Examples

```python
# User authentication
is_authenticated = True
is_admin = False

if is_authenticated and is_admin:
    print("Access admin panel")
elif is_authenticated:
    print("Access user dashboard")
else:
    print("Please login")

# Form validation
def validate_form(data):
    is_name_valid = bool(data.get('name'))
    is_email_valid = '@' in data.get('email', '')
    is_age_valid = 0 < data.get('age', 0) < 150
    
    return all([is_name_valid, is_email_valid, is_age_valid])

form_data = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
if validate_form(form_data):
    print("Form is valid")
else:
    print("Form has errors")

# Feature flags
DEBUG = True
CACHE_ENABLED = False

if DEBUG:
    print("Running in debug mode")
    log_level = "DEBUG"
else:
    log_level = "INFO"

# Loop control
is_processing = True
count = 0
while is_processing and count < 10:
    count += 1
    if count == 5:
        is_processing = False
    print(f"Processing {count}")

# Function returns
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
print(is_prime(20))  # False
```

---

## 💡 Common Patterns

### Toggle Boolean Flag

```python
# Method 1: Direct assignment
is_active = True
is_active = not is_active  # Toggle

# Method 2: Using XOR
is_active ^= True

# Method 3: In function
def toggle(flag):
    return not flag

is_active = toggle(is_active)
```

### Multiple Conditions

```python
# Check all conditions (AND)
if condition1 and condition2 and condition3:
    print("All true")

# Check any condition (OR)
if condition1 or condition2 or condition3:
    print("At least one true")

# Using all() and any()
conditions = [condition1, condition2, condition3]
if all(conditions):
    print("All true")
if any(conditions):
    print("At least one true")
```

### Default Values

```python
# Using or for defaults
name = user_input or "Guest"
value = cached_value or compute_value()
config = user_config or default_config

# Using if-else
name = user_input if user_input else "Guest"

# Using ternary operator
name = user_input if user_input else "Guest"
status = "Active" if is_active else "Inactive"
```

---

## 📚 Next Steps

After understanding boolean basics:
1. Open `booleans.md` for detailed boolean operations

---

## 🔗 Related Topics

- **Conditional Statements** – `if`, `elif`, `else`
- **Loops** – `while` loops use boolean conditions
- **Comparison Operators** – `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators** – `and`, `or`, `not`
- **Truthy/Falsy** – All values have boolean equivalents

---

## 💡 Quick Tips

```python
# ✅ DO: Use truthy/falsy directly
if name:
    print(name)

# ❌ DON'T: Compare to True/False unnecessarily
if name == True:  # Wrong!
    print(name)

# ✅ DO: Use boolean variables for flags
is_valid = check_validation()
if is_valid:
    process()

# ❌ DON'T: Repeat complex conditions
if check_validation():
    process()  # Works but less readable for repeated use

# ✅ DO: Use any() and all() for multiple conditions
if any([cond1, cond2, cond3]):
    print("At least one true")

# ✅ DO: Use ternary for simple assignments
status = "Active" if is_active else "Inactive"
```

---

*Master booleans for logical operations and control flow! 🐍✨*
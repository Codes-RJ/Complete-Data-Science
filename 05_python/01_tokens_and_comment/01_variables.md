# Variables in Python 📦

## What is a Variable?

A variable is a container that stores data in memory. Think of it as a labeled box where you can put values and retrieve them later by using the label. They are also known as **Identifiers**.

```python
# Variable assignment
name = "Alice"
age = 25
height = 5.7
```

Here, the 'name', 'age' and 'height' are "Identifiers" and the values 'Alice', '25', and '5.7' are "Literals".

---

## Variable Naming Rules

### Rules (Must Follow)
1. **Start with letter or underscore:** `name`, `_private`, `Name123`
2. **Cannot start with number:** ❌ `1name`
3. **Only letters, numbers, underscore:** ❌ `user-name`, ❌ `user name`
4. **Case-sensitive:** `name` and `Name` are different
5. **Cannot use keywords:** ❌ `if`, `for`, `while`, `class`

### Python Keywords (Reserved Words)

| | | Keywords | | |
|--------|----------|----------|----------|---------|
for      | while    | if       | elif     | else
True     | False    | break    | continue | None
not      | and      | or       | pass     | def
return   | lambda   | try      | except   | finally
import   | from     | as       | class    | is
in       | await    | yield    | with     | del
nonlocal | global   | except   | 

### Naming Conventions (Best Practices)

| Convention | Example | When to Use |
|------------|---------|-------------|
| **snake_case** | `customer_name` | Variables, functions |
| **PascalCase** | `CustomerAccount` | Class names |
| **UPPER_CASE** | `MAX_VALUE` | Constants |
| **_single** | `_private` | Internal use |

```python
# Good variable names
customer_name = "John"
total_price = 99.99
is_active = True
MAX_RETRIES = 3

# Bad variable names
x = "John"              # Not descriptive
customer-name = "John"  # Hyphen not allowed
2nd_customer = "John"   # Cannot start with number
```

---

## Variable Assignment

### Basic Assignment
```python
# Single variable
x = 10
name = "Python"

# Multiple variables at once
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Same value to multiple variables
x = y = z = 100
print(x)  # 100
print(y)  # 100
print(z)  # 100
```

### Swapping Variables
```python
# Python makes swapping easy
a = 5
b = 10
a, b = b, a
print(a)  # 10
print(b)  # 5
```

---

## Dynamic Typing

Python is dynamically typed - you don't need to declare variable types. The type is determined at runtime.

```python
# Variable can change type
x = 10          # x is int
print(type(x))  # <class 'int'>

x = "Hello"     # x is now string
print(type(x))  # <class 'str'>

x = 3.14        # x is now float
print(type(x))  # <class 'float'>
```

---

## Type Hints (Optional - Python 3.5+)

Type hints improve code readability and help with IDE autocomplete, but Python doesn't enforce them.

```python
# With type hints
name: str = "Alice"
age: int = 25
height: float = 5.7
is_active: bool = True

# Function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

## Variable Scope

### Local vs Global Variables

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

my_function()
# print(local_var)  # Error! Local variable not accessible outside
print(global_var)   # Displays : I'm global
```

### Modifying Global Variables
```python
counter = 0

def increment():
    global counter  # Need global keyword to modify
    counter += 1

increment()
print(counter)  # 1
```

---

## Constants

Python doesn't have true constants, but by convention, uppercase names indicate constants.

```python
# Constants (by convention)
PI = 3.14159
MAX_CONNECTIONS = 100
DATABASE_URL = "localhost:5432"

# Can still be modified, but shouldn't
PI = 3.14  # Allowed but against convention
```

---

## Memory Management

### Variable References
Variables in Python are references to objects in memory.

```python
x = [1, 2, 3]
y = x          # y references the same list
y.append(4)
print(x)       # [1, 2, 3, 4] - x also changed!

# To create a copy
z = x.copy()   # Creates new list
z.append(5)
print(x)       # [1, 2, 3, 4] - unchanged
print(z)       # [1, 2, 3, 4, 5]
```

### Identity vs Equality
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True (same value)
print(a is b)    # False (different objects)
print(a is c)    # True (same object)
```

---

## Deleting Variables

```python
x = 10
print(x)  # 10

del x
# print(x)  # Error! x is deleted
```

---

## Common Variable Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `age = 25` | Whole numbers |
| `float` | `price = 19.99` | Decimal numbers |
| `str` | `name = "Alice"` | Text |
| `bool` | `is_valid = True` | True/False |
| `list` | `colors = ["red", "blue"]` | Ordered collection |
| `tuple` | `point = (10, 20)` | Immutable collection |
| `dict` | `person = {"name": "John"}` | Key-value pairs |
| `set` | `unique = {1, 2, 3}` | Unique values |
| `None` | `result = None` | No value |

---

## Best Practices

### ✅ DO:
- Use descriptive variable names
- Follow snake_case convention
- Use constants for fixed values
- Keep variable scope minimal
- Initialize variables before use

```python
# Good
customer_name = "Alice"
total_amount = 250.00
is_premium_customer = True
MAX_RETRY_COUNT = 3
```

### ❌ DON'T:
- Use single letters (except loops)
- Use reserved keywords
- Create vague names
- Use camelCase for variables (reserve for classes)

```python
# Bad
a = "Alice"           # Not descriptive
cust = "Alice"        # Abbreviation unclear
CustomerName = "Alice"  # Use snake_case for variables
```

---

## Practice Exercises

### Exercise 1: Variable Assignment
Create variables for:
- Your name
- Your age
- Your height
- Are you a student?
Print them all.

```python
# Solution
name = "Your Name"
age = 25
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

### Exercise 2: Swapping
Swap the values of two variables without using a third variable.

```python
# Solution
a = 10
b = 20
print(f"Before: a={a}, b={b}")

a, b = b, a
print(f"After: a={a}, b={b}")
```

### Exercise 3: Type Checking
Create variables of different types and print their types.

```python
# Solution
x = 42
y = 3.14
z = "Hello"
w = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(w))  # <class 'bool'>
```

### Exercise 4: Variable Scope
Write a function that modifies a global variable.

```python
# Solution
score = 0

def add_points(points):
    global score
    score += points
    print(f"Added {points}. Total: {score}")

add_points(10)
add_points(5)
print(f"Final score: {score}")
```

---

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `NameError: name 'x' is not defined` | Variable used before assignment | Assign value first |
| `SyntaxError: invalid syntax` | Variable name starts with number | Start with letter or underscore |
| `IndentationError` | Inconsistent indentation | Use 4 spaces consistently |

---

## Key Takeaways

- Variables store data with meaningful names
- Follow naming rules and conventions
- Python is dynamically typed
- Use `global` to modify global variables inside functions
- Descriptive names make code self-documenting

---

## Next Steps

- Proceed to [02_keywords.md](./02_keywords.md) to explore different keywords in depth
- Practice using keywords along with variables to apply some features / specifications to the code

---
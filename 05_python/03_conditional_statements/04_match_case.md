# 📘 MATCH-CASE STATEMENT – COMPLETE GUIDE

## 📌 Table of Contents
01. [What is Match-Case?](#what-is-match-case)
02. [Basic Syntax](#basic-syntax)
03. [Matching Literals](#matching-literals)
04. [Matching Patterns](#matching-patterns)
05. [Guard Clauses (if conditions)](#guard-clauses-if-conditions)
06. [Matching Sequences](#matching-sequences)
07. [Matching Dictionaries](#matching-dictionaries)
08. [Matching Classes](#matching-classes)
09. [Using OR Patterns](#using-or-patterns)
10. [Wildcard and Capture Patterns](#wildcard-and-capture-patterns)
11. [Real-World Examples](#real-world-examples)
12. [Match-Case vs if-elif-else](#match-case-vs-if-elif-else)
13. [Common Pitfalls](#common-pitfalls)
14. [Practice Exercises](#practice-exercises)

---

## What is Match-Case?

**Match-case** (also called structural pattern matching) is a powerful feature introduced in Python 3.10. It allows you to match values against patterns, similar to switch-case in other languages but much more powerful.

```python
# Basic match-case
def get_day_name(day_num):
    match day_num:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(get_day_name(3))  # Wednesday
```

**Key Features:**
- ✅ More readable than long if-elif chains
- ✅ Can match against literals, variables, sequences, dictionaries, classes
- ✅ Supports pattern capturing and unpacking
- ✅ Can add guard conditions (if)
- ✅ Available in Python 3.10 and above

---

## Basic Syntax

### Syntax Structure

```python
match value:
    case pattern1:
        # code block 1
    case pattern2:
        # code block 2
    case _:
        # default block (wildcard)
```

### Simple Examples

```python
# HTTP status codes
def handle_status(code):
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(handle_status(200))  # OK
print(handle_status(404))  # Not Found
print(handle_status(418))  # Unknown Status
```

---

## Matching Literals

Match-case works with literal values like integers, strings, booleans, and None.

### Integers

```python
def describe_number(n):
    match n:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return f"Number {n}"

print(describe_number(2))  # Two
print(describe_number(10)) # Number 10
```

### Strings

```python
def get_command_action(command):
    match command.lower():
        case "start":
            return "Starting the system..."
        case "stop":
            return "Stopping the system..."
        case "restart":
            return "Restarting the system..."
        case "status":
            return "Checking system status..."
        case "help":
            return "Available commands: start, stop, restart, status, help"
        case _:
            return f"Unknown command: {command}"

print(get_command_action("start"))   # Starting the system...
print(get_command_action("help"))    # Available commands...
print(get_command_action("invalid")) # Unknown command: invalid
```

### Booleans and None

```python
def handle_value(value):
    match value:
        case True:
            return "Value is True"
        case False:
            return "Value is False"
        case None:
            return "Value is None"
        case _:
            return f"Value is {value}"

print(handle_value(True))   # Value is True
print(handle_value(None))   # Value is None
print(handle_value(42))     # Value is 42
```

---

## Matching Patterns

### Using Variables (Capture Patterns)

You can capture the matched value into a variable.

```python
def greet(name):
    match name:
        case "Alice":
            return "Hello, Alice!"
        case "Bob":
            return "Hi, Bob!"
        case other:
            return f"Welcome, {other}!"

print(greet("Alice"))   # Hello, Alice!
print(greet("Charlie")) # Welcome, Charlie!
```

### Using OR Patterns

Match multiple patterns with `|` (pipe).

```python
def is_weekend(day):
    match day.lower():
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return None

print(is_weekend("saturday"))  # True
print(is_weekend("monday"))    # False
print(is_weekend("invalid"))   # None

# With numbers
def number_type(n):
    match n:
        case 0 | 1 | 2 | 3 | 4 | 5:
            return "Small number"
        case 6 | 7 | 8 | 9:
            return "Medium number"
        case _:
            return "Large number"

print(number_type(3))   # Small number
print(number_type(7))   # Medium number
print(number_type(100)) # Large number
```

---

## Guard Clauses (if conditions)

Add additional conditions to patterns using `if`.

```python
def classify_number(n):
    match n:
        case n if n > 0:
            return "Positive"
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"

print(classify_number(5))   # Positive
print(classify_number(-3))  # Negative
print(classify_number(0))   # Zero

# With range checks
def get_age_group(age):
    match age:
        case age if age < 0:
            return "Invalid age"
        case age if age < 13:
            return "Child"
        case age if age < 20:
            return "Teenager"
        case age if age < 65:
            return "Adult"
        case age if age < 120:
            return "Senior"
        case _:
            return "Invalid age"

print(get_age_group(10))  # Child
print(get_age_group(25))  # Adult
print(get_age_group(70))  # Senior
```

---

## Matching Sequences

Match against lists, tuples, and other sequences.

### Matching Lists

```python
def process_list(lst):
    match lst:
        case []:
            return "Empty list"
        case [x]:
            return f"Single element: {x}"
        case [x, y]:
            return f"Two elements: {x} and {y}"
        case [x, y, z]:
            return f"Three elements: {x}, {y}, {z}"
        case [x, *rest]:
            return f"First element: {x}, remaining {len(rest)} elements"

print(process_list([]))           # Empty list
print(process_list([1]))          # Single element: 1
print(process_list([1, 2]))       # Two elements: 1 and 2
print(process_list([1, 2, 3]))    # Three elements: 1, 2, 3
print(process_list([1, 2, 3, 4])) # First element: 1, remaining 3 elements
```

### Matching Tuples

```python
def process_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(process_point((0, 0)))    # Origin
print(process_point((0, 5)))    # On Y-axis at y=5
print(process_point((5, 0)))    # On X-axis at x=5
print(process_point((3, 4)))    # Point at (3, 4)
```

### Matching with Rest Patterns

```python
def process_scores(scores):
    match scores:
        case []:
            return "No scores"
        case [first, *rest]:
            return f"First: {first}, Others: {rest}"
        case _:
            return "Invalid"

print(process_scores([85, 90, 88, 92]))  # First: 85, Others: [90, 88, 92]

# Ignoring elements with underscore
def get_first_two(lst):
    match lst:
        case [a, b, *_]:
            return f"First two: {a}, {b}"
        case [a]:
            return f"Only one element: {a}"
        case []:
            return "Empty list"

print(get_first_two([1, 2, 3, 4, 5]))  # First two: 1, 2
print(get_first_two([1, 2]))           # First two: 1, 2
print(get_first_two([1]))              # Only one element: 1
```

---

## Matching Dictionaries

Match against dictionary patterns.

### Basic Dictionary Matching

```python
def process_config(config):
    match config:
        case {"debug": True}:
            return "Debug mode enabled"
        case {"debug": False}:
            return "Debug mode disabled"
        case {"port": port}:
            return f"Port set to {port}"
        case {"host": host, "port": port}:
            return f"Host: {host}, Port: {port}"
        case _:
            return "Unknown configuration"

print(process_config({"debug": True}))           # Debug mode enabled
print(process_config({"port": 8080}))            # Port set to 8080
print(process_config({"host": "localhost", "port": 8080}))  # Host: localhost, Port: 8080
```

### Matching with Defaults

```python
def get_server_config(config):
    match config:
        case {"host": host, "port": port}:
            return f"Server running at {host}:{port}"
        case {"host": host}:
            return f"Server running at {host}:8080 (default port)"
        case {"port": port}:
            return f"Server running at localhost:{port}"
        case _:
            return "Server running at localhost:8080 (default)"

print(get_server_config({"host": "example.com", "port": 9090}))  # example.com:9090
print(get_server_config({"host": "example.com"}))                # example.com:8080
print(get_server_config({"port": 9090}))                         # localhost:9090
print(get_server_config({}))                                     # localhost:8080
```

---

## Matching Classes

Match against class instances.

### Basic Class Matching

```python
class Point:
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    __match_args__ = ("center", "radius")
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def describe_shape(shape):
    match shape:
        case Point(x=0, y=0):
            return "Origin point"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case Circle(center=Point(x, y), radius=r):
            return f"Circle at ({x}, {y}) with radius {r}"
        case _:
            return "Unknown shape"

point = Point(3, 4)
circle = Circle(Point(0, 0), 5)

print(describe_shape(point))   # Point at (3, 4)
print(describe_shape(circle))  # Circle at (0, 0) with radius 5
```

### Using `__match_args__`

```python
class Rectangle:
    __match_args__ = ("width", "height")
    def __init__(self, width, height):
        self.width = width
        self.height = height

def describe_rect(rect):
    match rect:
        case Rectangle(0, 0):
            return "Zero-sized rectangle"
        case Rectangle(w, h) if w == h:
            return f"Square of size {w}"
        case Rectangle(w, h):
            return f"Rectangle {w}x{h}"

rect1 = Rectangle(0, 0)
rect2 = Rectangle(5, 5)
rect3 = Rectangle(10, 20)

print(describe_rect(rect1))  # Zero-sized rectangle
print(describe_rect(rect2))  # Square of size 5
print(describe_rect(rect3))  # Rectangle 10x20
```

---

## Using OR Patterns

Combine multiple patterns with `|`.

```python
def validate_input(value):
    match value:
        case 0 | 1 | 2 | 3 | 4 | 5:
            return "Small number"
        case 6 | 7 | 8 | 9:
            return "Medium number"
        case "yes" | "y" | "true" | "1":
            return "Affirmative"
        case "no" | "n" | "false" | "0":
            return "Negative"
        case _:
            return "Other"

print(validate_input(3))     # Small number
print(validate_input(7))     # Medium number
print(validate_input("yes")) # Affirmative
print(validate_input("no"))  # Negative
```

---

## Wildcard and Capture Patterns

### Wildcard `_` (Ignore)

```python
def process_tuple(t):
    match t:
        case (x, y, _):
            return f"First two: {x}, {y}"
        case (x, _):
            return f"First: {x}"
        case _:
            return "Unknown pattern"

print(process_tuple((1, 2, 3)))    # First two: 1, 2
print(process_tuple((1, 2)))       # First: 1
print(process_tuple((1,)))         # Unknown pattern
```

### Capture Pattern (Variable)

```python
def parse_command(cmd):
    match cmd.split():
        case ["quit"]:
            return "Exiting..."
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Sum: {int(x) + int(y)}"
        case ["help"]:
            return "Commands: quit, hello <name>, add <x> <y>"
        case _:
            return "Unknown command"

print(parse_command("hello Alice"))    # Hello, Alice!
print(parse_command("add 5 3"))        # Sum: 8
print(parse_command("quit"))           # Exiting...
```

---

## Real-World Examples

### Example 1: HTTP Request Handler

```python
class Request:
    def __init__(self, method, path, headers=None, body=None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.body = body

class Response:
    def __init__(self, status_code, body, headers=None):
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}

def handle_request(request):
    match request:
        case Request(method="GET", path="/"):
            return Response(200, "Welcome to the homepage")
        
        case Request(method="GET", path=f"/users/{user_id}"):
            return Response(200, f"User {user_id} details")
        
        case Request(method="GET", path="/about"):
            return Response(200, "About page")
        
        case Request(method="POST", path="/users"):
            return Response(201, "User created")
        
        case Request(method="DELETE", path=f"/users/{user_id}"):
            return Response(200, f"User {user_id} deleted")
        
        case Request(method=method, path=path):
            return Response(404, f"Cannot {method} {path}")
        
        case _:
            return Response(400, "Invalid request")

# Test
req1 = Request("GET", "/")
req2 = Request("GET", "/users/123")
req3 = Request("POST", "/users")
req4 = Request("PUT", "/unknown")

print(f"GET /: {handle_request(req1).body}")
print(f"GET /users/123: {handle_request(req2).body}")
print(f"POST /users: {handle_request(req3).body}")
print(f"PUT /unknown: {handle_request(req4).body}")
```

### Example 2: Command Line Interface Parser

```python
def parse_command_line(args):
    match args:
        case ["run", filename]:
            return f"Running script: {filename}"
        
        case ["run", filename, "--verbose" | "-v"]:
            return f"Running script: {filename} (verbose mode)"
        
        case ["run", filename, "--output", output_file]:
            return f"Running script: {filename}, output to {output_file}"
        
        case ["test"]:
            return "Running all tests"
        
        case ["test", module]:
            return f"Running tests for module: {module}"
        
        case ["test", module, "--coverage"]:
            return f"Running tests for {module} with coverage"
        
        case ["install", package]:
            return f"Installing package: {package}"
        
        case ["install", *packages]:
            return f"Installing packages: {', '.join(packages)}"
        
        case ["uninstall", package]:
            return f"Uninstalling package: {package}"
        
        case ["help"] | ["--help"] | ["-h"]:
            return """
Commands:
  run <file>              - Run a script
  run <file> --verbose   - Run with verbose output
  run <file> --output <f> - Run with output file
  test                    - Run all tests
  test <module>          - Test specific module
  test <module> --coverage - Test with coverage
  install <package>      - Install package
  install <pkg1> <pkg2>  - Install multiple packages
  uninstall <package>    - Uninstall package
  help                   - Show this help
"""
        
        case _:
            return "Unknown command. Use 'help' for available commands."

# Test
print(parse_command_line(["run", "script.py"]))
print(parse_command_line(["run", "script.py", "--verbose"]))
print(parse_command_line(["install", "numpy", "pandas", "matplotlib"]))
print(parse_command_line(["test", "utils", "--coverage"]))
print(parse_command_line(["help"]))
```

### Example 3: Expression Evaluator

```python
def evaluate(expr):
    match expr:
        # Numbers
        case int(x) | float(x):
            return x
        
        # Basic arithmetic
        case ("+", a, b):
            return evaluate(a) + evaluate(b)
        
        case ("-", a, b):
            return evaluate(a) - evaluate(b)
        
        case ("*", a, b):
            return evaluate(a) * evaluate(b)
        
        case ("/", a, b):
            return evaluate(a) / evaluate(b)
        
        # Unary operations
        case ("neg", a):
            return -evaluate(a)
        
        # Power
        case ("pow", a, b):
            return evaluate(a) ** evaluate(b)
        
        # Comparisons
        case (">", a, b):
            return evaluate(a) > evaluate(b)
        
        case ("<", a, b):
            return evaluate(a) < evaluate(b)
        
        case ("==", a, b):
            return evaluate(a) == evaluate(b)
        
        # Variable (just return value)
        case name if isinstance(name, str):
            return f"Variable: {name}"
        
        case _:
            return f"Unknown expression: {expr}"

# Test
print(evaluate(42))                        # 42
print(evaluate(("+", 5, 3)))               # 8
print(evaluate(("*", ("+", 2, 3), 4)))     # 20
print(evaluate(("pow", 2, 3)))             # 8
print(evaluate((">", 10, 5)))              # True
print(evaluate(("neg", 5)))                # -5
```

### Example 4: JSON Response Parser

```python
def handle_api_response(response):
    match response:
        # Success response
        case {"status": "success", "data": data}:
            return f"Success: {data}"
        
        case {"status": "success", "message": msg}:
            return f"Success: {msg}"
        
        # Error responses
        case {"status": "error", "code": 404, "message": msg}:
            return f"Not Found: {msg}"
        
        case {"status": "error", "code": 400, "errors": errors}:
            return f"Bad Request: {errors}"
        
        case {"status": "error", "code": 500}:
            return "Internal Server Error"
        
        case {"status": "error", "message": msg}:
            return f"Error: {msg}"
        
        # Paginated response
        case {"data": items, "page": page, "total": total}:
            return f"Page {page} of {total}: {len(items)} items"
        
        # Empty response
        case {"data": []}:
            return "Empty response"
        
        case {"data": None}:
            return "No data"
        
        case _:
            return "Unknown response format"

# Test
responses = [
    {"status": "success", "data": {"user": "Alice"}},
    {"status": "error", "code": 404, "message": "User not found"},
    {"status": "error", "code": 400, "errors": ["Invalid email", "Password too short"]},
    {"data": [1, 2, 3], "page": 2, "total": 10},
    {"data": []},
    {"status": "error", "message": "Something went wrong"},
]

for resp in responses:
    print(handle_api_response(resp))
```

### Example 5: File Type Detector

```python
def detect_file_type(filename, content=None):
    match filename.split('.'), content:
        # Images
        case [name, "jpg" | "jpeg" | "png" | "gif" | "bmp"], _:
            return "Image file"
        
        # Documents
        case [name, "pdf"], _:
            return "PDF document"
        
        case [name, "doc" | "docx"], _:
            return "Word document"
        
        case [name, "xls" | "xlsx"], _:
            return "Excel spreadsheet"
        
        case [name, "txt"], _:
            return "Text file"
        
        case [name, "md"], _:
            return "Markdown file"
        
        # Code files
        case [name, "py"], content if b"def " in content or b"class " in content:
            return "Python code file"
        
        case [name, "py"], _:
            return "Python script"
        
        case [name, "js"], _:
            return "JavaScript file"
        
        case [name, "html" | "htm"], _:
            return "HTML file"
        
        case [name, "css"], _:
            return "CSS file"
        
        case [name, "json"], _:
            return "JSON file"
        
        # Archives
        case [name, "zip"], _:
            return "ZIP archive"
        
        case [name, "tar" | "gz" | "bz2"], _:
            return "Compressed archive"
        
        # Executables
        case [name, "exe" | "msi"], _:
            return "Windows executable"
        
        case [name, "app" | "dmg"], _:
            return "Mac application"
        
        case [name, "sh" | "bash"], _:
            return "Shell script"
        
        # No extension
        case [name], _:
            return "File with no extension"
        
        case _, _:
            return "Unknown file type"

# Test
files = [
    "image.png",
    "document.pdf",
    "script.py",
    "archive.zip",
    "README.md",
    "noextension",
    "unknown.xyz",
]

for file in files:
    print(f"{file:15} -> {detect_file_type(file)}")
```

---

## Match-Case vs if-elif-else

### Comparison

```python
# Using if-elif-else
def get_grade_if(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Using match-case
def get_grade_match(score):
    match score:
        case s if s >= 90:
            return "A"
        case s if s >= 80:
            return "B"
        case s if s >= 70:
            return "C"
        case s if s >= 60:
            return "D"
        case _:
            return "F"

# When to use which
```

### When to Use Match-Case

| Use Case | Match-Case | if-elif-else |
|----------|------------|--------------|
| Simple value matching | ✅ Excellent | ⚠️ Verbose |
| Pattern matching (lists, dicts) | ✅ Excellent | ❌ Not possible |
| Multiple values in one case | ✅ OR patterns | ❌ Multiple conditions |
| Structural unpacking | ✅ Excellent | ❌ Not possible |
| Complex conditions | ⚠️ Guard clauses | ✅ Clear |
| Python < 3.10 | ❌ Not available | ✅ Always works |

---

## Common Pitfalls

### Pitfall 1: Python Version

```python
# match-case requires Python 3.10+
import sys

if sys.version_info < (3, 10):
    print("match-case requires Python 3.10 or higher")
else:
    # Use match-case
    pass
```

### Pitfall 2: Variable Capture Confusion

```python
# ❌ Variable captures any value
def process(value):
    match value:
        case x:  # This captures ANY value!
            return f"Captured: {x}"
        case _:
            return "Never reached"

print(process(42))   # Captured: 42
print(process("hi")) # Captured: hi

# ✅ Use specific literals or wildcard
def process(value):
    match value:
        case 42:
            return "The answer"
        case "hi":
            return "Greeting"
        case _:
            return "Other"
```

### Pitfall 3: Order of Patterns Matters

```python
def describe(n):
    match n:
        case n if n > 0:    # This matches first
            return "Positive"
        case 0:              # Never reached for positive numbers
            return "Zero"
        case _:
            return "Negative"

print(describe(0))   # Positive? (0 > 0 is False, so goes to next)
# Actually 0 > 0 is False, so it continues to case 0

# Better order
def describe(n):
    match n:
        case 0:
            return "Zero"
        case n if n > 0:
            return "Positive"
        case _:
            return "Negative"
```

### Pitfall 4: Using Underscore as Variable

```python
# ❌ _ is not a regular variable (it's a wildcard)
def process(t):
    match t:
        case (_, y):  # _ ignores first element
            return y

print(process((1, 2)))  # 2

# ✅ Use variable name to capture
def process(t):
    match t:
        case (x, y):
            return x, y
```

---

## Practice Exercises

### Beginner Level

1. **Day of Week**
   ```python
   # Use match-case to return day name from number 1-7
   ```

2. **HTTP Status Messages**
   ```python
   # Return message for status codes: 200, 201, 400, 404, 500
   ```

3. **Simple Calculator**
   ```python
   # Match operator: '+', '-', '*', '/'
   ```

### Intermediate Level

4. **Command Parser**
   ```python
   # Parse commands: "quit", "hello NAME", "add X Y"
   ```

5. **Shape Area Calculator**
   ```python
   # Match circle, rectangle, triangle patterns
   ```

6. **Configuration Parser**
   ```python
   # Match dictionary patterns for different configs
   ```

### Advanced Level

7. **Expression Evaluator**
   ```python
   # Evaluate nested arithmetic expressions
   ```

8. **JSON Validator**
   ```python
   # Validate JSON structure using match-case
   ```

9. **Protocol Parser**
   ```python
   # Parse network protocol messages
   ```

---

## Quick Reference Card

```python
# Basic syntax
match value:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default

# Literal matching
case 42:
case "hello":
case True:
case None:

# OR pattern
case 1 | 2 | 3:
case "yes" | "y" | "true":

# Capture variable
case x:  # captures any value

# Guard clause
case x if x > 0:

# Sequence matching
case [a, b]:
case [first, *rest]:
case (x, y):

# Dictionary matching
case {"key": value}:
case {"host": host, "port": port}:

# Class matching
case Point(x=0, y=0):
case Rectangle(w, h) if w == h:

# Wildcard (ignore)
case _:  # matches anything
case [_, y]:  # ignores first element
```

## Next Step

- Move to [exercises.md](exercises.md) for practising.

---

*Master match-case for powerful pattern matching in Python 3.10+! 🐍✨*

---
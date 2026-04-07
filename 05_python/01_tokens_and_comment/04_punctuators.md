# Punctuators in Python 🔣

---

## What are Punctuators?

Punctuators are symbols that have special syntactic meaning in Python. They help structure the code and define the language's grammar. Think of them as the punctuation marks of programming.

```python
# Punctuators in action
name = "Alice"     # = is a punctuator
if x > 5:          # : and > are punctuators
    print(name)    # () and . are punctuators
```

---

## List of Python Punctuators

| Punctuator | Name | Purpose |
|------------|------|---------|
| `=` | Assignment Operator | Assigns value to variable |
| `+` | Plus | Addition or concatenation |
| `-` | Minus | Subtraction |
| `*` | Asterisk | Multiplication |
| `/` | Slash | Division |
| `//` | Double Slash | Floor division |
| `%` | Percent | Modulus |
| `**` | Double Asterisk | Exponentiation |
| `==` | Equal To | Comparison |
| `!=` | Not Equal | Comparison |
| `>` | Greater Than | Comparison |
| `<` | Less Than | Comparison |
| `>=` | Greater or Equal | Comparison |
| `<=` | Less or Equal | Comparison |
| `&` | Ampersand | Bitwise AND |
| `\|` | Pipe | Bitwise OR |
| `^` | Caret | Bitwise XOR |
| `~` | Tilde | Bitwise NOT |
| `<<` | Double Less | Left shift |
| `>>` | Double Greater | Right shift |
| `and` | Logical AND | Logical operation |
| `or` | Logical OR | Logical operation |
| `not` | Logical NOT | Logical operation |
| `in` | Membership | Checks existence |
| `is` | Identity | Checks object identity |
| `(` `)` | Parentheses | Grouping, function calls |
| `[` `]` | Brackets | Lists, indexing |
| `{` `}` | Braces | Dictionaries, sets |
| `,` | Comma | Separates items |
| `.` | Dot | Attribute access |
| `:` | Colon | Indicates block start |
| `;` | Semicolon | Statement separator |
| `@` | At | Decorators |
| `->` | Arrow | Return type hint |
| `...` | Ellipsis | Placeholder |
| `"` `'` | Quotes | String literals |
| `#` | Hash | Comments |
| `\` | Backslash | Line continuation |
| `_` | Underscore | Temporary variable |

---

## 1. Assignment Punctuators

### `=` (Assignment)
Assigns a value to a variable.

```python
# Basic assignment
name = "Alice"
age = 25
pi = 3.14159

# Multiple assignment
x = y = z = 10
a, b, c = 1, 2, 3
```

### Compound Assignment Operators
```python
x = 5
x += 3   # Same as x = x + 3
x -= 2   # Same as x = x - 2
x *= 4   # Same as x = x * 4
x /= 2   # Same as x = x / 2
x //= 3  # Same as x = x // 3
x %= 2   # Same as x = x % 2
x **= 2  # Same as x = x ** 2
```

---

## 2. Arithmetic Punctuators

```python
# Basic arithmetic
sum = 10 + 5        # Addition
difference = 10 - 5 # Subtraction
product = 10 * 5    # Multiplication
quotient = 10 / 3   # Division (float) = 3.333
floor_div = 10 // 3 # Floor division = 3
remainder = 10 % 3  # Modulus = 1
power = 2 ** 3      # Exponentiation = 8

# With different types
text = "Hello" + " " + "World"  # String concatenation
repeated = "Ha" * 3              # String repetition = "HaHaHa"
```

---

## 3. Comparison Punctuators

```python
x = 10
y = 20

print(x == y)   # False (equal to)
print(x != y)   # True (not equal to)
print(x > y)    # False (greater than)
print(x < y)    # True (less than)
print(x >= 10)  # True (greater than or equal)
print(x <= 5)   # False (less than or equal)
```

---

## 4. Logical Punctuators

```python
# and - both must be True
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")

# or - at least one must be True
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work")

# not - reverses boolean
is_raining = False
if not is_raining:
    print("Go outside")
```

---

## 5. Bitwise Punctuators

```python
# Bitwise operations (works on binary representation)
a = 5      # 0101
b = 3      # 0011

print(a & b)   # 0001 = 1 (AND)
print(a | b)   # 0111 = 7 (OR)
print(a ^ b)   # 0110 = 6 (XOR)
print(~a)      # -6 (NOT)
print(a << 1)  # 1010 = 10 (left shift)
print(a >> 1)  # 0010 = 2 (right shift)
```

---

## 6. Membership & Identity Punctuators

### `in` and `not in`
```python
# Membership testing
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# With strings
text = "Hello World"
print("Hello" in text)  # True
```

### `is` and `is not`
```python
# Identity testing (same object in memory)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (same object)
print(a is c)      # False (different objects)
print(a is not c)  # True

# With None (common use)
result = None
if result is None:
    print("No result")
```

---

## 7. Delimiters (Brackets, Braces, Parentheses)

### `(` `)` Parentheses
```python
# Function calls
print("Hello")
len("Python")

# Grouping expressions
result = (10 + 5) * 2  # 30 (without parentheses would be 20)

# Tuples
point = (10, 20)
single_item = (5,)  # Comma needed for single item tuple

# Function definitions
def greet(name):
    return f"Hello, {name}"
```

### `[` `]` Brackets
```python
# Lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Indexing and slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[0])     # 10 (first element)
print(numbers[-1])    # 50 (last element)
print(numbers[1:4])   # [20, 30, 40] (slicing)

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### `{` `}` Braces
```python
# Dictionaries (key-value pairs)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person["name"])  # Alice

# Sets (unique values)
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Dictionary and set comprehensions
squares_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
even_set = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

---

## 8. `:` (Colon)

```python
# Indicates start of code block
if x > 5:
    print("x is greater than 5")

# For loops
for i in range(3):
    print(i)

# While loops
while count < 5:
    print(count)
    count += 1

# Function definitions
def my_function():
    pass

# Class definitions
class MyClass:
    pass

# Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]

# Dictionary keys (not a punctuator but uses colon)
person = {"name": "Alice"}
```

---

## 9. `.` (Dot Operator)

```python
# Attribute access
import math
print(math.pi)       # 3.14159
print(math.sqrt(16)) # 4.0

# Method calls
text = "hello"
print(text.upper())  # "HELLO"
print(text.capitalize())  # "Hello"

# String methods
name = "Alice"
print(name.lower())  # "alice"

# List methods
numbers = [1, 2, 3]
numbers.append(4)
numbers.sort()
```

---

## 10. `,` (Comma)

```python
# Separating items in lists
fruits = ["apple", "banana", "mango"]

# Separating items in tuples
point = (10, 20)
coordinates = 10, 20  # Tuple without parentheses

# Multiple variable assignment
a, b, c = 1, 2, 3

# Function arguments
def add(a, b, c):
    return a + b + c

result = add(1, 2, 3)

# Print with multiple items
print("Hello", "World", 123)  # Hello World 123

# Single element tuple (needs comma)
single = (5,)  # Tuple, not integer
```

---

## 11. `;` (Semicolon)

Allows multiple statements on one line (not recommended for readability).

```python
# Multiple statements on one line
x = 5; y = 10; z = x + y

# Not recommended - use separate lines instead
x = 5
y = 10
z = x + y

# Sometimes used in interactive sessions
import math; print(math.sqrt(25))
```

---

## 12. `@` (At Symbol - Decorators)

```python
# Decorator syntax
def timer(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@timer
def my_function():
    print("Hello")

my_function()
# Output:
# Start
# Hello
# End

# Class decorators
@dataclass
class Person:
    name: str
    age: int
```

---

## 13. `->` (Arrow - Return Type Hint)

```python
# Function with return type annotation
def greet(name: str) -> str:
    return f"Hello, {name}"

def divide(a: float, b: float) -> float:
    return a / b

def get_user(id: int) -> dict | None:
    return {"id": id, "name": "Alice"}
```

---

## 14. `...` (Ellipsis)

```python
# Placeholder for incomplete code
def future_function():
    ...

# In NumPy for slicing multiple dimensions
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[..., 0])  # Select all first elements

# Type hints
from typing import Tuple
def process_data() -> Tuple[int, ...]:
    return (1, 2, 3, 4)
```

---

## 15. Quotes (`"` `'`)

```python
# Single quotes
name = 'Alice'

# Double quotes
message = "Hello World"

# Triple quotes for multi-line strings
long_text = """
This is a
multi-line
string
"""

# Docstrings
def my_function():
    """This is a docstring explaining the function."""
    pass

# Quotes inside quotes
text = "He said 'Hello'"
another = 'She said "Hi"'
```

---

## 16. `#` (Hash - Comments)

```python
# This is a single line comment

# Comments are ignored by Python
x = 5  # This is an inline comment

"""
Multi-line comment (actually a string literal)
But commonly used for multi-line comments
"""

def add(a, b):
    # This comment explains the function
    return a + b  # Return the sum
```

---

## 17. `\` (Backslash - Line Continuation)

```python
# Continuing a long line
long_variable = 10 + 20 + 30 + \
                40 + 50 + 60

# In strings (escape character)
path = "C:\\Users\\Name\\Documents"
quote = "She said \"Hello\""
new_line = "Line1\nLine2"

# Line continuation in lists
my_list = [1, 2, 3, 4, \
           5, 6, 7, 8]
```

---

## 18. `_` (Underscore)

```python
# Temporary/discard variable
for _ in range(5):
    print("Hello")  # Loop runs 5 times, no need for index

# Unpacking with discard
a, b, _ = (1, 2, 3)  # a=1, b=2, third value discarded

# In interactive interpreter (holds last result)
# >>> 5 + 3
# 8
# >>> _ * 2
# 16

# Separating large numbers (Python 3.6+)
million = 1_000_000
hex_value = 0xFF_FF_FF

# Private naming convention
_private_variable = "should not be accessed directly"
```

---

## Complete Quick Reference Table

| Punctuator | Name | Common Use |
|------------|------|------------|
| `=` | Assignment | Variable assignment |
| `+ - * /` | Arithmetic | Math operations |
| `== != > < >= <=` | Comparison | Value comparison |
| `and or not` | Logical | Boolean logic |
| `in` | Membership | Check existence |
| `is` | Identity | Object comparison |
| `()` | Parentheses | Functions, grouping |
| `[]` | Brackets | Lists, indexing |
| `{}` | Braces | Dicts, sets |
| `:` | Colon | Block start, slicing |
| `.` | Dot | Attribute access |
| `,` | Comma | Separating items |
| `@` | At | Decorators |
| `->` | Arrow | Return type hint |
| `#` | Hash | Comments |
| `_` | Underscore | Temporary variable |
| `" '` | Quotes | Strings |
| `\` | Backslash | Escape, continuation |

---

## Practice Exercises

### Exercise 1: Identify the Punctuators
Identify all punctuators in this code:
```python
def calculate(x, y):
    result = (x + y) * 2
    return result

print(calculate(5, 3))
```

**Solution:** `=`, `(`, `)`, `:`, `+`, `*`, `return`, `.`

### Exercise 2: Use Different Punctuators
Write code using at least 10 different punctuators.

```python
# Solution
def process_numbers(numbers):  # : ( ), def
    total = 0                   # =
    for num in numbers:         # for, in, :
        total += num            # +=
    average = total / len(numbers)  # /, ., ()
    return average              # return

my_list = [1, 2, 3, 4, 5]      # [ ], =, ,
result = process_numbers(my_list)  # =, ., ()
print(f"Average: {result}")     # ., (), {, }, ","
```

---

## Key Takeaways

- Punctuators give structure and meaning to Python code
- Different punctuators serve different purposes
- Some punctuators work in pairs ((), [], {})
- Whitespace around punctuators improves readability
- Using the right punctuator is essential for correct syntax

---

## Next Steps

- Proceed to [05_comments.md](./05_comments.md) to learn about if-else and loops
- Practice writing code using various punctuators

---

*"Punctuators are the traffic signals of code - they direct the flow and structure."*
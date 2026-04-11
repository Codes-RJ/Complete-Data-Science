# 📘 FUNCTIONS BASICS – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Functions?](#what-are-functions)
2. [Defining and Calling Functions](#defining-and-calling-functions)
3. [Function Parameters](#function-parameters)
4. [Return Values](#return-values)
5. [Scope and Lifetime](#scope-and-lifetime)
6. [Docstrings](#docstrings)
7. [Type Hints (Annotations)](#type-hints-annotations)
8. [Real-World Examples](#real-world-examples)
9. [Common Pitfalls](#common-pitfalls)
10. [Practice Exercises](#practice-exercises)

---

## What are Functions?

**Functions** are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs modular.

```python
# Simple function
def greet():
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    return a + b

# Calling functions
greet()                    # Hello, World!
greet_person("Alice")      # Hello, Alice!
result = add(5, 3)         # 8
```

**Why Functions Matter:**
- Reusability (write once, use many times)
- Modularity (break complex problems into smaller pieces)
- Maintainability (fix bugs in one place)
- Readability (clear, descriptive names)
- Testing (test each function independently)

---

## Defining and Calling Functions

### Basic Definition

```python
# Basic function - no parameters, no return
def say_hello():
    print("Hello!")

# Function with one parameter
def square(x):
    return x ** 2

# Function with multiple parameters
def rectangle_area(length, width):
    return length * width

# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling functions
say_hello()                    # Hello!
result = square(5)             # 25
area = rectangle_area(10, 5)   # 50
greet("Alice")                 # Hello, Alice!
greet()                        # Hello, Guest!
```

### Function Naming Rules

```python
# Valid function names
def my_function(): pass
def myFunction(): pass        # Camel case (less common)
def _private(): pass          # Convention for private
def function123(): pass
def function_name(): pass     # Snake case (recommended)

# Invalid function names
# def 123function(): pass      # Cannot start with number
# def my-function(): pass      # Cannot use hyphen
# def def(): pass              # Cannot use keyword
```

### Calling Functions

```python
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else None

# Positional arguments (order matters)
result = calculate(10, 5, "add")        # 15

# Keyword arguments (order doesn't matter)
result = calculate(a=10, b=5, operation="multiply")  # 50

# Mixed (positional first, then keyword)
result = calculate(10, 5, operation="subtract")  # 5

# Wrong order
# result = calculate(operation="add", 10, 5)  # SyntaxError!
```

---

## Function Parameters

### Positional Parameters

```python
def introduce(name, age, city):
    print(f"I'm {name}, {age} years old, from {city}")

# Must provide all arguments in correct order
introduce("Alice", 30, "New York")  # Correct
# introduce(30, "Alice", "New York")  # Wrong order!
```

### Default Parameters

```python
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")                      # Hello, Alice!
greet("Bob", "Hi")                  # Hi, Bob!
greet("Charlie", "Hey", "?")        # Hey, Charlie?
greet("David", punctuation="!!")    # Hello, David!!

# Default parameters must come after non-default
# def func(default="value", required):  # SyntaxError!
```

### Keyword Arguments

```python
def create_profile(name, age, city, job):
    return f"{name}, {age}, from {city}, works as {job}"

# Call with keyword arguments (order doesn't matter)
profile = create_profile(
    job="Engineer",
    name="Alice",
    city="New York",
    age=30
)
print(profile)  # Alice, 30, from New York, works as Engineer
```

### Variable Arguments (`*args`)

Collects extra positional arguments as a tuple.

```python
def sum_all(*args):
    """Sum any number of arguments"""
    return sum(args)

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100
print(sum_all())                  # 0

# With other parameters
def print_info(title, *args):
    print(f"Title: {title}")
    print(f"Additional: {args}")

print_info("Main", 1, 2, 3, "hello")
# Title: Main
# Additional: (1, 2, 3, 'hello')

# Unpacking lists with *
numbers = [1, 2, 3, 4, 5]
result = sum_all(*numbers)  # Unpacks list to arguments
print(result)  # 15
```

### Variable Keyword Arguments (`**kwargs`)

Collects extra keyword arguments as a dictionary.

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC

# With other parameters
def create_user(username, **kwargs):
    user = {"username": username}
    user.update(kwargs)
    return user

user = create_user("alice123", email="alice@example.com", age=30, is_active=True)
print(user)
# {'username': 'alice123', 'email': 'alice@example.com', 'age': 30, 'is_active': True}

# Unpacking dictionaries with **
defaults = {"host": "localhost", "port": 8080}
config = {**defaults, "debug": True}
print(config)  # {'host': 'localhost', 'port': 8080, 'debug': True}
```

### Combined Parameters (Order Matters)

```python
def complex_function(
    required,           # Positional
    default="default",  # Default
    *args,              # Variable positional
    **kwargs            # Variable keyword
):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("req", 1, 2, 3, name="Alice", age=30)
# Required: req
# Default: 1
# Args: (2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
```

### Keyword-Only Arguments

```python
# Arguments after * are keyword-only
def connect(host, port, *, timeout=30, ssl=False):
    print(f"Connecting to {host}:{port}")
    print(f"Timeout: {timeout}, SSL: {ssl}")

connect("localhost", 8080)                    # OK
connect("localhost", 8080, timeout=60)        # OK
connect("localhost", 8080, ssl=True)          # OK
# connect("localhost", 8080, 60, True)        # Error! Must use keywords

# All arguments after * are keyword-only
def configure(*, host, port, debug=False):
    print(f"Host: {host}, Port: {port}, Debug: {debug}")

configure(host="localhost", port=8080)  # OK
# configure("localhost", 8080)           # Error!
```

---

## Return Values

### Single Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Functions without return return None
def say_hello():
    print("Hello")

result = say_hello()
print(result)  # None
```

### Multiple Return Values (Tuples)

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Unpack returned tuple
minimum, maximum = get_min_max([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 5

# As tuple
result = get_min_max([1, 2, 3])
print(result)  # (1, 3)

# Real example: Divide with remainder
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")  # 17 ÷ 5 = 3 remainder 2
```

### Returning Multiple Types

```python
def process_data(data):
    if not data:
        return None
    if isinstance(data, list):
        return sum(data) / len(data)
    if isinstance(data, dict):
        return sum(data.values()) / len(data)
    return data

print(process_data([1, 2, 3, 4, 5]))        # 3.0
print(process_data({"a": 10, "b": 20}))     # 15.0
print(process_data([]))                     # None
```

### Early Returns (Guard Clauses)

```python
def calculate_discount(price, is_member, coupon=None):
    # Guard clauses - return early
    if price <= 0:
        return 0
    
    if not is_member and not coupon:
        return 0
    
    discount = 0
    
    if is_member:
        discount = 0.10
        if price >= 100:
            discount += 0.05
    
    if coupon == "SAVE20":
        discount = max(discount, 0.20)
    elif coupon == "SAVE10":
        discount = max(discount, 0.10)
    
    return min(discount, 0.50)  # Cap at 50%

print(calculate_discount(50, True))              # 0.1
print(calculate_discount(150, True))             # 0.15
print(calculate_discount(50, False))             # 0
print(calculate_discount(50, True, "SAVE20"))    # 0.2
```

---

## Scope and Lifetime

### Local Scope

Variables defined inside a function are local to that function.

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # 10
# print(x)  # NameError: x is not defined
```

### Global Scope

Variables defined outside any function are global.

```python
x = 10  # Global variable

def print_global():
    print(x)  # Can access global

def modify_global():
    global x  # Need global keyword to modify
    x = 20

print_global()     # 10
modify_global()
print_global()     # 20
```

### Enclosing Scope (Nested Functions)

```python
def outer_function(x):
    def inner_function(y):
        return x + y  # Can access x from outer
    return inner_function

add_five = outer_function(5)
result = add_five(3)
print(result)  # 8

# Modifying enclosing variable
def counter():
    count = 0
    def increment():
        nonlocal count  # Need nonlocal to modify
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

### Built-in Scope

Python looks for names in this order: Local → Enclosing → Global → Built-in.

```python
def my_function():
    len = 5  # Shadows built-in len()
    # print(len("hello"))  # Error! len is now 5, not function
```

### LEGB Rule

| Scope | Description |
|-------|-------------|
| **L**ocal | Inside current function |
| **E**nclosing | Inside enclosing functions |
| **G**lobal | At module level |
| **B**uilt-in | Python's built-in names |

```python
x = "global"  # Global

def outer():
    x = "enclosing"  # Enclosing
    
    def inner():
        x = "local"  # Local
        print(x)
    
    inner()

outer()  # local
```

---

## Docstrings

Docstrings document what a function does.

### Single-line Docstring

```python
def square(n):
    """Return the square of a number."""
    return n ** 2

print(square.__doc__)  # Return the square of a number.
help(square)           # Shows docstring
```

### Multi-line Docstring

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle

    Examples:
        >>> calculate_area(5, 3)
        15
        >>> calculate_area(2.5, 4)
        10.0
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

### Docstring Formats

```python
# Google style
def greet(name, greeting="Hello"):
    """Greet a person.

    Args:
        name (str): Person's name
        greeting (str, optional): Greeting to use. Defaults to "Hello".

    Returns:
        str: Formatted greeting message
    """
    return f"{greeting}, {name}!"

# NumPy/SciPy style
def greet(name, greeting="Hello"):
    """
    Greet a person.

    Parameters
    ----------
    name : str
        Person's name
    greeting : str, optional
        Greeting to use (default is "Hello")

    Returns
    -------
    str
        Formatted greeting message
    """
    return f"{greeting}, {name}!"

# Sphinx style
def greet(name, greeting="Hello"):
    """
    Greet a person.

    :param name: Person's name
    :type name: str
    :param greeting: Greeting to use
    :type greeting: str
    :return: Formatted greeting message
    :rtype: str
    """
    return f"{greeting}, {name}!"
```

---

## Type Hints (Annotations)

Type hints indicate expected types (Python 3.5+).

### Basic Type Hints

```python
# Variable annotations
name: str = "Alice"
age: int = 30
prices: list[float] = [19.99, 29.99]

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process(numbers: list[int]) -> list[int]:
    return [n * 2 for n in numbers]
```

### Optional and Union Types

```python
from typing import Optional, Union

# Optional (can be None)
def find_user(user_id: int) -> Optional[dict]:
    if user_id in database:
        return database[user_id]
    return None

# Union (multiple possible types)
def process(value: Union[int, float, str]) -> str:
    return str(value)

# Python 3.10+ alternative
def process(value: int | float | str) -> str:
    return str(value)
```

### Type Hints with Default Values

```python
def connect(
    host: str,
    port: int = 8080,
    timeout: float = 30.0,
    ssl: bool = False
) -> bool:
    print(f"Connecting to {host}:{port}")
    return True
```

---

## Real-World Examples

### Example 1: Input Validation Functions

```python
def validate_email(email: str) -> bool:
    """Validate email format"""
    if '@' not in email:
        return False
    local, domain = email.split('@')
    if not local or not domain:
        return False
    if '.' not in domain:
        return False
    return True

def validate_phone(phone: str) -> bool:
    """Validate phone number (10 digits)"""
    digits = ''.join(filter(str.isdigit, phone))
    return len(digits) == 10

def validate_age(age: int) -> bool:
    """Validate age (0-150)"""
    return isinstance(age, int) and 0 <= age <= 150

# Usage
email = "user@example.com"
phone = "555-123-4567"
age = 25

print(f"Email valid: {validate_email(email)}")
print(f"Phone valid: {validate_phone(phone)}")
print(f"Age valid: {validate_age(age)}")
```

### Example 2: Data Processing Functions

```python
def clean_text(text: str) -> str:
    """Clean and normalize text"""
    return text.strip().lower()

def extract_numbers(text: str) -> list[int]:
    """Extract all numbers from text"""
    import re
    return [int(n) for n in re.findall(r'\d+', text)]

def calculate_average(numbers: list[float]) -> float:
    """Calculate average of numbers"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def format_currency(amount: float, currency: str = "$") -> str:
    """Format amount as currency"""
    return f"{currency}{amount:,.2f}"

# Usage
text = "  Hello World 123 and 456  "
cleaned = clean_text(text)
print(f"Cleaned: '{cleaned}'")

numbers = extract_numbers(text)
print(f"Numbers: {numbers}")

avg = calculate_average(numbers)
print(f"Average: {avg}")

price = format_currency(1234.56)
print(f"Price: {price}")
```

### Example 3: String Utility Functions

```python
def is_palindrome(s: str) -> bool:
    """Check if string is palindrome"""
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

def count_vowels(s: str) -> int:
    """Count vowels in string"""
    vowels = set('aeiou')
    return sum(1 for char in s.lower() if char in vowels)

def reverse_words(s: str) -> str:
    """Reverse order of words in string"""
    words = s.split()
    return ' '.join(reversed(words))

def capitalize_words(s: str) -> str:
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())

# Usage
text = "A man a plan a canal panama"
print(f"Palindrome: {is_palindrome(text)}")
print(f"Vowel count: {count_vowels(text)}")

sentence = "Hello World Python"
print(f"Reversed words: {reverse_words(sentence)}")
print(f"Capitalized: {capitalize_words(sentence)}")
```

### Example 4: Math Utility Functions

```python
def is_prime(n: int) -> bool:
    """Check if number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    """Calculate factorial"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a: int, b: int) -> int:
    """Find greatest common divisor"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Find least common multiple"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# Usage
print(f"Is 17 prime? {is_prime(17)}")
print(f"Factorial of 5: {factorial(5)}")
print(f"GCD of 48 and 18: {gcd(48, 18)}")
print(f"LCM of 12 and 18: {lcm(12, 18)}")
```

### Example 5: List Processing Functions

```python
def find_max(numbers: list) -> int:
    """Find maximum value without using max()"""
    if not numbers:
        raise ValueError("List is empty")
    
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def find_min(numbers: list) -> int:
    """Find minimum value without using min()"""
    if not numbers:
        raise ValueError("List is empty")
    
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def remove_duplicates(lst: list) -> list:
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def chunk_list(lst: list, size: int) -> list[list]:
    """Split list into chunks of specified size"""
    return [lst[i:i + size] for i in range(0, len(lst), size)]

# Usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Max: {find_max(numbers)}")
print(f"Min: {find_min(numbers)}")
print(f"Unique: {remove_duplicates(numbers)}")
print(f"Chunks of 3: {chunk_list(numbers, 3)}")
```

---

## Common Pitfalls

### Pitfall 1: Mutable Default Arguments

```python
# ❌ WRONG - Mutable default persists
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] (unexpected!)

# ✅ CORRECT - Use None as default
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [2] (correct!)
```

### Pitfall 2: Variable Scope Confusion

```python
# ❌ WRONG - Modifying global without global keyword
x = 10
def increment():
    x += 1  # UnboundLocalError!

# ✅ CORRECT - Use global keyword
def increment():
    global x
    x += 1

# ✅ CORRECT - Pass as parameter
def increment(x):
    return x + 1
```

### Pitfall 3: Returning vs Printing

```python
# ❌ Prints but doesn't return
def add(a, b):
    print(a + b)

result = add(5, 3)  # None
print(result)       # None

# ✅ Returns value
def add(a, b):
    return a + b

result = add(5, 3)  # 8
print(result)       # 8
```

### Pitfall 4: Using `=` Instead of `==` in Conditions

```python
# ❌ WRONG - Assignment instead of comparison
def is_even(n):
    if n % 2 = 0:  # SyntaxError!
        return True
    return False

# ✅ CORRECT
def is_even(n):
    if n % 2 == 0:
        return True
    return False
```

---

## Practice Exercises

### Beginner Level

1. **Greeting Function**
   ```python
   # Write function that takes name and returns greeting
   # Example: greet("Alice") -> "Hello, Alice!"
   ```

2. **Area Calculator**
   ```python
   # Write functions for circle, rectangle, triangle area
   # circle_area(radius), rectangle_area(l, w), triangle_area(b, h)
   ```

3. **Even/Odd Checker**
   ```python
   # Function that returns True if number is even
   # Example: is_even(4) -> True, is_even(5) -> False
   ```

4. **Max of Three**
   ```python
   # Function that returns maximum of three numbers
   # Example: max_of_three(5, 2, 8) -> 8
   ```

5. **String Reverser**
   ```python
   # Function that reverses a string
   # Example: reverse("hello") -> "olleh"
   ```

### Intermediate Level

6. **Prime Number Checker**
   ```python
   # Function that returns True if number is prime
   # Example: is_prime(17) -> True, is_prime(20) -> False
   ```

7. **List Statistics**
   ```python
   # Function that returns min, max, sum, average of list
   # Example: stats([1,2,3,4,5]) -> (1,5,15,3.0)
   ```

8. **Palindrome Checker**
   ```python
   # Function that checks if string is palindrome
   # Ignore spaces and case
   # Example: is_palindrome("A man a plan a canal panama") -> True
   ```

9. **Word Counter**
   ```python
   # Function that counts word frequencies in text
   # Example: word_count("hello world hello") -> {"hello": 2, "world": 1}
   ```

10. **Calculator Function**
    ```python
    # Function that takes operation and numbers
    # Example: calculate("add", 1, 2, 3) -> 6
    ```

### Advanced Level

11. **Function Pipeline**
    ```python
    # Create function that chains multiple functions
    # Example: pipeline([double, square, half], 5) -> ((5*2)^2)/2
    ```

12. **Memoization Decorator**
    ```python
    # Create decorator that caches function results
    # Example: @cache def fib(n): ...
    ```

13. **Validation Decorator**
    ```python
    # Create decorator that validates arguments
    # Example: @validate(lambda x: x > 0) def sqrt(x): ...
    ```

---

## Quick Reference Card

```python
# Function definition
def func_name(params):
    """Docstring"""
    # body
    return value

# Parameter types
def f(pos1, pos2): pass           # Positional
def f(pos1, default="val"): pass  # Default
def f(*args): pass                # Variable positional
def f(**kwargs): pass             # Variable keyword
def f(*, kwonly): pass            # Keyword-only

# Return values
return value          # Single
return val1, val2     # Multiple (tuple)

# Scope
global x              # Modify global
nonlocal x            # Modify enclosing

# Docstring
def f():
    """Single line."""
    pass

def f():
    """
    Multi-line docstring.
    
    Args:
        param: Description
    
    Returns:
        Description
    """
    pass

# Type hints
def f(name: str, age: int) -> bool:
    pass

# Common patterns
if __name__ == "__main__":
    main()
```

## Next Step

- Go to [02_functions_advanced.md](02_functions_advanced.md) to understand the advanced topics and methodologies of functions.

---

*Master functions to write organized, reusable, and maintainable code! 🐍✨*

---
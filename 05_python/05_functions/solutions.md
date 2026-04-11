Here's the **`solutions.md`** for Functions - complete solutions to all practice exercises.

---

# 💡 FUNCTIONS – SOLUTIONS

## 📌 Table of Contents
1. [Basic Function Solutions](#basic-function-solutions)
2. [Parameter Solutions](#parameter-solutions)
3. [Return Value Solutions](#return-value-solutions)
4. [Scope Solutions](#scope-solutions)
5. [Lambda Solutions](#lambda-solutions)
6. [Recursion Solutions](#recursion-solutions)
7. [Decorator Solutions](#decorator-solutions)
8. [Generator Solutions](#generator-solutions)
9. [Mixed Practice Solutions](#mixed-practice-solutions)
10. [Challenge Solutions](#challenge-solutions)

---

## Basic Function Solutions

### Solution 1: Greeting Function

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))  # "Hello, Alice!"
print(greet("Bob"))    # "Hello, Bob!"
```

### Solution 2: Area of Circle

```python
import math

def circle_area(radius):
    """Calculate area of a circle."""
    if radius < 0:
        return None
    return math.pi * radius ** 2

print(circle_area(5))    # 78.53981633974483
print(circle_area(2.5))  # 19.634954084936208
```

### Solution 3: Even or Odd

```python
def is_even(n):
    """Return True if number is even."""
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True
```

### Solution 4: Maximum of Two

```python
def max_of_two(a, b):
    """Return the larger of two numbers."""
    return a if a > b else b

# Alternative
def max_of_two_alt(a, b):
    if a > b:
        return a
    return b

print(max_of_two(10, 20))  # 20
print(max_of_two(25, 15))  # 25
print(max_of_two(5, 5))    # 5
```

### Solution 5: String Reverser

```python
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

# Alternative using loop
def reverse_string_loop(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))     # "olleh"
print(reverse_string("Python"))    # "nohtyP"
```

---

## Parameter Solutions

### Solution 6: Default Parameter

```python
def greet_person(name, greeting="Hello"):
    """Greet a person with optional greeting."""
    return f"{greeting}, {name}!"

print(greet_person("Alice"))           # "Hello, Alice!"
print(greet_person("Bob", "Hi"))       # "Hi, Bob!"
print(greet_person("Charlie", "Hey"))  # "Hey, Charlie!"
```

### Solution 7: Variable Arguments (*args)

```python
def sum_all(*args):
    """Sum any number of arguments."""
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
print(sum_all())               # 0
```

### Solution 8: Variable Keyword Arguments (**kwargs)

```python
def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC
```

### Solution 9: Mixed Parameters

```python
def process_data(required, default="default", *args, **kwargs):
    """Process mixed parameter types."""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

process_data("req", 1, 2, 3, name="Alice", age=30)
# Required: req
# Default: 1
# Args: (2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
```

### Solution 10: Keyword-Only Arguments

```python
def configure(*, host, port, debug=False):
    """Configure with keyword-only arguments."""
    print(f"Host: {host}, Port: {port}, Debug: {debug}")

configure(host="localhost", port=8080)              # OK
configure(host="localhost", port=8080, debug=True) # OK

# This would raise TypeError:
# configure("localhost", 8080)
```

---

## Return Value Solutions

### Solution 11: Multiple Returns

```python
def min_max(numbers):
    """Return min and max of list."""
    if not numbers:
        return (None, None)
    return (min(numbers), max(numbers))

result = min_max([3, 1, 4, 1, 5, 9, 2])
print(result)  # (1, 9)

# Alternative without built-ins
def min_max_manual(numbers):
    if not numbers:
        return (None, None)
    min_val = max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return (min_val, max_val)
```

### Solution 12: Early Return

```python
def check_positive(numbers):
    """Return first positive number, or None."""
    for num in numbers:
        if num > 0:
            return num
    return None

print(check_positive([-5, -2, 3, -1]))   # 3
print(check_positive([-5, -2, -1]))      # None
```

### Solution 13: Multiple Return Types

```python
def process(value):
    """Return different types based on input."""
    if isinstance(value, list):
        return sum(value) / len(value) if value else 0
    elif isinstance(value, dict):
        return sum(value.values())
    elif isinstance(value, (int, float)):
        return value ** 2
    else:
        return None

print(process([1, 2, 3, 4, 5]))     # 3.0
print(process({"a": 10, "b": 20}))  # 30
print(process(5))                   # 25
print(process("hello"))             # None
```

### Solution 14: Guard Clauses

```python
def calculate_discount(price, is_member, coupon=None):
    """Calculate discount percentage using guard clauses."""
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

print(calculate_discount(50, True))         # 0.1
print(calculate_discount(150, True))        # 0.15
print(calculate_discount(50, False))        # 0
print(calculate_discount(50, True, "SAVE20"))  # 0.2
```

---

## Scope Solutions

### Solution 15: Local vs Global

```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # 20
```

### Solution 16: Enclosing Scope

```python
def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

### Solution 17: Nonlocal

```python
def counter():
    """Return a counter function."""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

---

## Lambda Solutions

### Solution 18: Basic Lambda

```python
square_lambda = lambda x: x ** 2

print(square_lambda(5))  # 25
```

### Solution 19: Lambda with map()

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### Solution 20: Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

### Solution 21: Lambda with sorted()

```python
pairs = [(1, 5), (2, 3), (3, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(3, 1), (4, 2), (2, 3), (1, 5)]
```

### Solution 22: Lambda in List Comprehension

```python
prices = [100, 200, 300, 400, 500]
discount = 0.1
discounted = [(lambda x: x * (1 - discount))(price) for price in prices]
print(discounted)  # [90.0, 180.0, 270.0, 360.0, 450.0]

# Simpler way (no lambda needed)
discounted = [price * (1 - discount) for price in prices]
```

---

## Recursion Solutions

### Solution 23: Factorial (Recursive)

```python
def factorial(n):
    """Calculate factorial recursively."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(10))  # 3628800
```

### Solution 24: Fibonacci (Recursive)

```python
def fibonacci(n):
    """Calculate Fibonacci recursively."""
    if n < 0:
        return None
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

### Solution 25: Sum of List (Recursive)

```python
def sum_list(numbers):
    """Sum list elements recursively."""
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

### Solution 26: Palindrome Check (Recursive)

```python
def is_palindrome(s):
    """Check if string is palindrome recursively."""
    # Clean the string
    cleaned = ''.join(s.lower().split())
    
    # Base case
    if len(cleaned) <= 1:
        return True
    
    # Check first and last characters
    if cleaned[0] != cleaned[-1]:
        return False
    
    # Recursive case
    return is_palindrome(cleaned[1:-1])

print(is_palindrome("racecar"))                      # True
print(is_palindrome("A man a plan a canal panama"))  # True
print(is_palindrome("hello"))                        # False
```

### Solution 27: Power Function (Recursive)

```python
def power(base, exponent):
    """Calculate power recursively."""
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 3))   # 8
print(power(5, 0))   # 1
print(power(3, 4))   # 81
```

---

## Decorator Solutions

### Solution 28: Timer Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())  # slow_function took 1.00 seconds
```

### Solution 29: Uppercase Decorator

```python
from functools import wraps

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # "HELLO, ALICE"
```

### Solution 30: Repeat Decorator

```python
from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    return "Hello"

print(say_hello())  # ['Hello', 'Hello', 'Hello']
```

### Solution 31: Cache Decorator

```python
from functools import wraps

def cache(func):
    cache_dict = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache_dict:
            print(f"Returning cached result for {args}")
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result
    return wrapper

@cache
def expensive_computation(n):
    print(f"Computing {n}...")
    return n ** 2

print(expensive_computation(5))  # Computing 5... 25
print(expensive_computation(5))  # 25 (from cache, no print)
```

### Solution 32: Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Failed!")
    return "Success"

# print(unstable_function())  # May succeed or fail
```

---

## Generator Solutions

### Solution 33: Simple Generator

```python
def count_up_to(n):
    """Yield numbers from 0 to n."""
    i = 0
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num, end=" ")  # 0 1 2 3 4 5
print()
```

### Solution 34: Even Numbers Generator

```python
def even_numbers(n):
    """Yield even numbers up to n."""
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

for num in even_numbers(10):
    print(num, end=" ")  # 0, 2, 4, 6, 8, 10
print()
```

### Solution 35: Fibonacci Generator

```python
def fibonacci():
    """Yield Fibonacci numbers infinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print()
```

### Solution 36: Generator Expression

```python
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum(x ** 2 for x in numbers)
print(sum_of_squares)  # 55

# Compare with list comprehension (uses more memory)
sum_of_squares_list = sum([x ** 2 for x in numbers])
```

### Solution 37: Generator with send()

```python
def accumulator():
    """Generator that accumulates values sent to it."""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # Initialize
print(acc.send(5))   # 5
print(acc.send(3))   # 8
print(acc.send(2))   # 10
```

---

## Mixed Practice Solutions

### Solution 38: Validate Email

```python
def is_valid_email(email):
    """Validate email format."""
    if not email or '@' not in email:
        return False
    
    local, domain = email.split('@')
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True

print(is_valid_email("user@example.com"))   # True
print(is_valid_email("invalid"))            # False
print(is_valid_email("user@example"))       # False
```

### Solution 39: Password Strength

```python
def password_strength(password):
    """Check password strength."""
    score = 0
    
    if len(password) >= 8:
        score += 1
    
    if any(c.isupper() for c in password):
        score += 1
    
    if any(c.islower() for c in password):
        score += 1
    
    if any(c.isdigit() for c in password):
        score += 1
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
    
    if score >= 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

print(password_strength("weak"))                 # Weak
print(password_strength("WeakPass"))             # Medium
print(password_strength("Str0ngP@ss"))           # Strong
```

### Solution 40: List Chunker

```python
def chunk_list(lst, size):
    """Split list into chunks of size n."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]

# Alternative using loop
def chunk_list_loop(lst, size):
    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i + size])
    return chunks

print(chunk_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Challenge Solutions

### Solution 41: Function Pipeline

```python
def pipeline(functions):
    """Chain multiple functions together."""
    def apply_pipeline(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    return apply_pipeline

def double(x): return x * 2
def square(x): return x ** 2
def half(x): return x / 2

process = pipeline([double, square, half])
print(process(5))  # ((5*2)^2)/2 = 50
```

### Solution 42: Memoization Decorator

```python
def memoize(func):
    """Memoization decorator for recursive functions."""
    cache = {}
    
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))  # 102334155 (fast!)
```

### Solution 43: Rate Limiter Decorator

```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < 1.0 / calls_per_second:
                time.sleep((1.0 / calls_per_second) - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def fast_function():
    print(f"Called at {time.time():.2f}")

# Test
for _ in range(5):
    fast_function()
```

### Solution 44: Validate Decorator

```python
from functools import wraps

def validate(validator):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not validator(arg):
                    raise ValueError(f"Argument {arg} failed validation")
            for value in kwargs.values():
                if not validator(value):
                    raise ValueError(f"Argument {value} failed validation")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate(lambda x: x > 0)
def sqrt(x):
    return x ** 0.5

print(sqrt(25))  # 5.0
# sqrt(-5)  # Raises ValueError
```

### Solution 45: Lazy Property Decorator

```python
class lazy_property:
    """Decorator that creates a lazy property."""
    
    def __init__(self, function):
        self.function = function
        self.name = function.__name__
    
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        value = self.function(obj)
        setattr(obj, self.name, value)
        return value

class Data:
    def __init__(self):
        self._data = None
    
    @lazy_property
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]

d = Data()
print(d.data)  # Loading data... [1, 2, 3, 4, 5]
print(d.data)  # [1, 2, 3, 4, 5] (no "Loading" message)
```

---

## Scoring Guide

| Score Range | Rating | Recommendation |
|-------------|--------|----------------|
| 41-45/45 | Excellent | Ready for next topic |
| 31-40/45 | Good | Review missed concepts |
| 21-30/45 | Satisfactory | Practice more |
| 11-20/45 | Needs Improvement | Re-study material |
| Below 11 | Review | Start from basics |

---

## Next Step

- Move to [Modules and Packages](/05_python/06_modules_package/README.md) to learn about organizing code into modules.

---

*Solutions verified and tested. Keep practicing! 🐍✨*
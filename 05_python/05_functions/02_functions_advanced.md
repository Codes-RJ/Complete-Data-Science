# 📘 FUNCTIONS ADVANCED – COMPLETE GUIDE

## 📌 Table of Contents
1. [Nested Functions](#nested-functions)
2. [Closures](#closures)
3. [Decorators](#decorators)
4. [Generators](#generators)
5. [Functools Module](#functools-module)
6. [Function Attributes](#function-attributes)
7. [Real-World Examples](#real-world-examples)
8. [Common Pitfalls](#common-pitfalls)
9. [Practice Exercises](#practice-exercises)

---

## Nested Functions

Functions defined inside other functions are called nested functions.

### Basic Nested Functions

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# inner_function is only accessible inside outer_function
add_five = outer_function(5)
result = add_five(3)
print(result)  # 8

# Cannot call inner_function directly
# inner_function(3)  # NameError!
```

### Why Use Nested Functions?

```python
# 1. Encapsulation - hide helper functions
def process_data(data):
    def clean(item):
        return item.strip().lower()
    
    def validate(item):
        return len(item) > 0
    
    result = []
    for item in data:
        cleaned = clean(item)
        if validate(cleaned):
            result.append(cleaned)
    return result

data = ["  Hello  ", "", "  World  ", "  ", "Python"]
print(process_data(data))  # ['hello', 'world', 'python']

# 2. Factory functions
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Nonlocal Variables

The `nonlocal` keyword allows modifying variables in enclosing scopes.

```python
def counter():
    count = 0
    
    def increment():
        nonlocal count  # Without this, count would be local
        count += 1
        return count
    
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3

# Without nonlocal (read-only access)
def read_counter():
    count = 0
    
    def read():
        return count  # OK - reading only
    
    return read

r = read_counter()
print(r())  # 0
```

### Multiple Nested Levels

```python
def outer():
    x = 10
    
    def middle():
        y = 20
        
        def inner():
            nonlocal x, y  # Can access both outer and middle
            x += 1
            y += 1
            return x, y
        
        return inner
    
    return middle()

func = outer()
print(func())  # (11, 21)
print(func())  # (12, 22)
```

---

## Closures

A **closure** is a nested function that remembers variables from its enclosing scope even after the outer function has finished executing.

### What is a Closure?

```python
def make_power(exponent):
    def power(base):
        return base ** exponent
    return power

square = make_power(2)
cube = make_power(3)

print(square(5))   # 25
print(cube(5))     # 125

# Check closure
print(square.__closure__)      # (<cell at 0x...: int object at 0x...>,)
print(square.__closure__[0].cell_contents)  # 2
```

### Closure vs Regular Function

```python
# Using closure
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))   # 8
print(add10(3))  # 13

# Using class (alternative)
class Adder:
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

add5_class = Adder(5)
print(add5_class(3))  # 8
```

### Practical Closure Examples

```python
# 1. Function with configuration
def configure_logger(prefix, level="INFO"):
    def logger(message):
        print(f"[{level}] {prefix}: {message}")
    return logger

error_logger = configure_logger("ERROR", "ERROR")
info_logger = configure_logger("APP")

error_logger("Database connection failed")  # [ERROR] ERROR: Database connection failed
info_logger("Server started")               # [INFO] APP: Server started

# 2. Counter with different starting points
def make_counter(start=0, step=1):
    count = start
    def counter():
        nonlocal count
        current = count
        count += step
        return current
    return counter

count_by_1 = make_counter(0, 1)
count_by_2 = make_counter(10, 2)

for _ in range(5):
    print(count_by_1(), end=" ")  # 0 1 2 3 4
print()
for _ in range(5):
    print(count_by_2(), end=" ")  # 10 12 14 16 18
print()

# 3. Memoization (caching) with closure
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))  # Fast due to caching
```

### Checking if a Function is a Closure

```python
def is_closure(func):
    return hasattr(func, '__closure__') and func.__closure__ is not None

def outer(x):
    def inner(y):
        return x + y
    return inner

def regular(y):
    return y

closure_func = outer(5)
print(is_closure(closure_func))  # True
print(is_closure(regular))       # False
```

---

## Decorators

Decorators are functions that modify the behavior of other functions.

### Basic Decorator

```python
# Simple decorator
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

print(slow_function())  # slow_function took 1.0012 seconds
```

### Decorator Syntax

```python
# These two are equivalent:

# Using @ syntax
@timer
def my_func():
    pass

# Without @ syntax
def my_func():
    pass
my_func = timer(my_func)
```

### Decorators with Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']
```

### Multiple Decorators

```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation
@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # HELLO, ALICE!!!
# Order matters: @uppercase then @exclamation

# Without decorators (equivalent)
def greet(name):
    return f"Hello, {name}"
greet = exclamation(uppercase(greet))
```

### Preserving Function Metadata with `wraps`

```python
from functools import wraps

# Without wraps - metadata is lost
def decorator_bad(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@decorator_bad
def say_hello():
    """Say hello docstring"""
    print("Hello")

print(say_hello.__name__)     # wrapper (not say_hello)
print(say_hello.__doc__)      # Wrapper docstring (not original)

# With wraps - preserves metadata
def decorator_good(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@decorator_good
def say_hello():
    """Say hello docstring"""
    print("Hello")

print(say_hello.__name__)     # say_hello
print(say_hello.__doc__)      # Say hello docstring
```

### Real-World Decorators

```python
# 1. Logging decorator
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(5, 3)
# Calling add with args=(5, 3), kwargs={}
# add returned 8

# 2. Authentication decorator
def require_auth(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_profile(user):
    return f"Profile of {user['name']}"

user1 = {"name": "Alice", "is_authenticated": True}
user2 = {"name": "Bob", "is_authenticated": False}

print(view_profile(user1))  # Profile of Alice
# view_profile(user2)  # PermissionError!

# 3. Retry decorator
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
                    import time
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_network_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success!"

# 4. Cache decorator (LRU)
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(n):
    print(f"Computing {n}...")
    return n ** 2

print(expensive_computation(5))  # Computing 5... 25
print(expensive_computation(5))  # 25 (from cache)

# 5. Rate limiter decorator
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
def api_call():
    print(f"API called at {time.time():.2f}")

for _ in range(5):
    api_call()
```

---

## Generators

Generators are functions that yield values one at a time, preserving state between calls.

### Basic Generator

```python
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Using generator
for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4

# Convert to list
numbers = list(count_up_to(5))
print(numbers)  # [0, 1, 2, 3, 4]
```

### Generator vs List

```python
# List (stores all in memory)
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator (yields one at a time)
def squares_generator(n):
    for i in range(n):
        yield i ** 2

# Memory usage difference
import sys
list_squares = squares_list(10000)
gen_squares = squares_generator(10000)

print(f"List size: {sys.getsizeof(list_squares)} bytes")
print(f"Generator size: {sys.getsizeof(gen_squares)} bytes")
# Generator is much smaller!
```

### Generator Methods

```python
def counter():
    i = 0
    while True:
        received = yield i
        if received is not None:
            i = received
        else:
            i += 1

gen = counter()

# Using next()
print(next(gen))      # 0
print(next(gen))      # 1
print(next(gen))      # 2

# Using send()
print(gen.send(10))   # Set to 10, then yield
print(next(gen))      # 11
print(next(gen))      # 12

# Using throw()
try:
    gen.throw(ValueError("Something went wrong"))
except ValueError as e:
    print(f"Caught: {e}")

# Using close()
gen.close()
# next(gen)  # StopIteration
```

### Generator Expressions

```python
# List comprehension (creates list)
squares_list = [x**2 for x in range(10)]

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(10))

print(type(squares_list))  # <class 'list'>
print(type(squares_gen))   # <class 'generator'>

# Memory efficient for large data
large_gen = (x**2 for x in range(10000000))  # OK
# large_list = [x**2 for x in range(10000000)]  # Memory error!

# Generator expressions in functions
total = sum(x**2 for x in range(1000))  # No extra list created
print(total)  # 332833500
```

### Real-World Generators

```python
# 1. Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # 0 1 1 2 3 5 8 13 21 34
print()

# 2. Read large file line by line
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

# for line in read_large_file('huge_file.txt'):
#     process(line)

# 3. Infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

import itertools
for num in itertools.islice(infinite_sequence(), 10):
    print(num, end=" ")  # 0 1 2 3 4 5 6 7 8 9
print()

# 4. Pagination generator
def paginate(items, page_size):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

items = list(range(1, 101))
for page in paginate(items, 10):
    print(f"Page: {page}")

# 5. Pipeline with generators
def read_numbers():
    for i in range(10):
        yield i

def square(numbers):
    for n in numbers:
        yield n ** 2

def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

pipeline = filter_even(square(read_numbers()))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

---

## Functools Module

The `functools` module provides higher-order functions that operate on other functions.

### `partial` – Fix Arguments

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create specialized functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))   # 25
print(cube(5))     # 125

# With positional arguments
def multiply(a, b, c):
    return a * b * c

double = partial(multiply, 2)  # Fix first argument
triple = partial(multiply, 3)

print(double(4, 5))   # 2 * 4 * 5 = 40
print(triple(4, 5))   # 3 * 4 * 5 = 60

# Real use: API calls with fixed base URL
def request(base_url, endpoint, method="GET"):
    print(f"{method} {base_url}/{endpoint}")

github_api = partial(request, "https://api.github.com")
github_api("users/octocat")  # GET https://api.github.com/users/octocat
```

### `lru_cache` – Memoization

```python
from functools import lru_cache

# Without cache (slow)
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

# With cache (fast)
@lru_cache(maxsize=128)
def fibonacci_fast(n):
    if n <= 1:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)

import time

start = time.time()
print(fibonacci_fast(40))
print(f"With cache: {time.time() - start:.4f}s")

start = time.time()
print(fibonacci_slow(40))
print(f"Without cache: {time.time() - start:.4f}s")

# Cache info
print(fibonacci_fast.cache_info())
# CacheInfo(hits=38, misses=41, maxsize=128, currsize=41)
```

### `wraps` – Preserve Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Without this, metadata is lost
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """Original docstring"""
    print("Hello")

print(my_function.__name__)  # my_function (not wrapper)
print(my_function.__doc__)   # Original docstring (not Wrapper docstring)
```

### `singledispatch` – Function Overloading

```python
from functools import singledispatch

@singledispatch
def process(value):
    """Default implementation"""
    return f"Unknown type: {type(value).__name__}"

@process.register(int)
def _(value):
    return f"Processing integer: {value}"

@process.register(float)
def _(value):
    return f"Processing float: {value}"

@process.register(str)
def _(value):
    return f"Processing string: {value}"

@process.register(list)
def _(value):
    return f"Processing list of length {len(value)}"

@process.register(dict)
def _(value):
    return f"Processing dict with {len(value)} keys"

print(process(42))           # Processing integer: 42
print(process(3.14))         # Processing float: 3.14
print(process("hello"))      # Processing string: hello
print(process([1, 2, 3]))    # Processing list of length 3
print(process({"a": 1}))     # Processing dict with 1 keys
print(process(True))         # Unknown type: bool
```

### `reduce` – Cumulative Operations

```python
from functools import reduce

# Sum of numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Maximum value
max_val = reduce(lambda x, y: x if x > y else y, numbers)
print(max_val)  # 5

# String concatenation
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: f"{x} {y}", words)
print(sentence)  # Hello World Python

# With initial value
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115

# Real use: Flatten list
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, list_of_lists)
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

### `cmp_to_key` – Old-Style Comparison

```python
from functools import cmp_to_key

# Old-style comparison function (returns -1, 0, 1)
def compare(a, b):
    # Sort by length, then alphabetically
    if len(a) != len(b):
        return len(a) - len(b)
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

words = ["python", "java", "c", "go", "rust", "c++"]
sorted_words = sorted(words, key=cmp_to_key(compare))
print(sorted_words)  # ['c', 'go', 'c++', 'java', 'rust', 'python']
```

### `total_ordering` – Complete Comparison Methods

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age

alice = Person("Alice", 30)
bob = Person("Bob", 25)
charlie = Person("Charlie", 30)

print(alice > bob)    # True (from __lt__)
print(alice == charlie)  # True (from __eq__)
print(bob <= alice)   # True (from __lt__ and __eq__)
```

---

## Function Attributes

Functions have several built-in attributes.

### Common Function Attributes

```python
def my_function(a: int, b: int = 10) -> str:
    """This is a docstring"""
    return f"{a + b}"

# Function metadata
print(my_function.__name__)       # my_function
print(my_function.__doc__)        # This is a docstring
print(my_function.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'str'>}
print(my_function.__defaults__)   # (10,)
print(my_function.__code__)       # Code object
print(my_function.__module__)     # __main__

# Custom attributes (can be added)
my_function.version = "1.0"
my_function.author = "Python"
print(my_function.version)  # 1.0
print(my_function.author)   # Python
```

### Code Object Attributes

```python
def example(a, b, c=10):
    x = a + b
    return x * c

code = example.__code__
print(f"co_argcount: {code.co_argcount}")      # Number of arguments
print(f"co_varnames: {code.co_varnames}")      # Variable names
print(f"co_consts: {code.co_consts}")          # Constants
print(f"co_names: {code.co_names}")            # Names used
```

---

## Real-World Examples

### Example 1: Retry Decorator with Backoff

```python
import time
import random
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1, backoff_factor=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = base_delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_retries - 1:
                        raise
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator

@retry_with_backoff(max_retries=5, base_delay=0.5, backoff_factor=2)
def unreliable_api():
    if random.random() < 0.7:
        raise ConnectionError("API request failed")
    return "Success!"

# print(unreliable_api())
```

### Example 2: Pipeline with Closures

```python
class Pipeline:
    def __init__(self):
        self.steps = []
    
    def add(self, func):
        self.steps.append(func)
        return self
    
    def execute(self, data):
        result = data
        for step in self.steps:
            result = step(result)
        return result

# Create pipeline
pipeline = Pipeline()
pipeline.add(lambda x: x * 2)
pipeline.add(lambda x: x + 10)
pipeline.add(lambda x: f"Result: {x}")

print(pipeline.execute(5))  # Result: 20

# With closures
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

def make_adder(amount):
    def adder(x):
        return x + amount
    return adder

pipeline = Pipeline()
pipeline.add(make_multiplier(3))
pipeline.add(make_adder(5))
pipeline.add(lambda x: f"Final: {x}")

print(pipeline.execute(10))  # Final: 35
```

### Example 3: Event System with Decorators

```python
class EventBus:
    def __init__(self):
        self._listeners = {}
    
    def on(self, event_name):
        def decorator(func):
            if event_name not in self._listeners:
                self._listeners[event_name] = []
            self._listeners[event_name].append(func)
            return func
        return decorator
    
    def emit(self, event_name, *args, **kwargs):
        if event_name in self._listeners:
            for listener in self._listeners[event_name]:
                listener(*args, **kwargs)
    
    def off(self, event_name, func):
        if event_name in self._listeners:
            self._listeners[event_name].remove(func)

bus = EventBus()

@bus.on("user_login")
def send_welcome_email(username):
    print(f"Sending welcome email to {username}")

@bus.on("user_login")
def log_login(username):
    print(f"Login recorded for {username}")

@bus.on("user_logout")
def log_logout(username):
    print(f"Logout recorded for {username}")

bus.emit("user_login", "alice")
# Sending welcome email to alice
# Login recorded for alice

bus.emit("user_logout", "alice")
# Logout recorded for alice
```

### Example 4: Rate Limiter with Closures

```python
import time
from collections import deque
from functools import wraps

def rate_limit(max_calls, time_window):
    def decorator(func):
        calls = deque()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Remove old calls
            while calls and calls[0] < now - time_window:
                calls.popleft()
            
            # Check limit
            if len(calls) >= max_calls:
                sleep_time = time_window - (now - calls[0])
                print(f"Rate limit exceeded. Waiting {sleep_time:.2f}s")
                time.sleep(sleep_time)
            
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, time_window=5)
def api_request(user_id):
    print(f"Processing request for user {user_id} at {time.time():.2f}")

# Simulate requests
for i in range(10):
    api_request(i)
    time.sleep(0.5)
```

### Example 5: Cached Property Decorator

```python
class cached_property:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value

class Database:
    def __init__(self):
        self._data = None
    
    @cached_property
    def data(self):
        print("Loading data from database...")
        # Simulate expensive operation
        time.sleep(2)
        return [1, 2, 3, 4, 5]

db = Database()
print(db.data)  # Loading data... [1, 2, 3, 4, 5]
print(db.data)  # [1, 2, 3, 4, 5] (cached)
```

---

## Common Pitfalls

### Pitfall 1: Forgetting `nonlocal`

```python
# ❌ WRONG - Trying to modify enclosing variable
def counter():
    count = 0
    def increment():
        count += 1  # UnboundLocalError!
        return count
    return increment

# ✅ CORRECT - Use nonlocal
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

### Pitfall 2: Decorator Without `@wraps`

```python
# ❌ WRONG - Loses function metadata
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_func():
    """Important docstring"""
    pass

print(my_func.__name__)  # wrapper (not my_func)
print(my_func.__doc__)   # None (lost)

# ✅ CORRECT - Use @wraps
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Pitfall 3: Generator Exhaustion

```python
# ❌ WRONG - Generator can only be used once
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(list(g))  # [1, 2, 3]
print(list(g))  # [] (exhausted)

# ✅ CORRECT - Create new generator each time
for _ in range(2):
    g = gen()
    print(list(g))  # [1, 2, 3] each time
```

### Pitfall 4: Late Binding in Closures

```python
# ❌ WRONG - All functions use the last value
functions = []
for i in range(3):
    functions.append(lambda: i)

for f in functions:
    print(f())  # 2, 2, 2 (not 0, 1, 2)

# ✅ CORRECT - Capture current value
functions = []
for i in range(3):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())  # 0, 1, 2
```

---

## Practice Exercises

### Beginner Level

1. **Nested Function**
   ```python
   # Create function that returns a nested function
   # Example: make_power(3)(2) -> 8
   ```

2. **Simple Decorator**
   ```python
   # Create decorator that prints "Before" and "After"
   ```

3. **Generator for Even Numbers**
   ```python
   # Create generator that yields even numbers up to n
   ```

### Intermediate Level

4. **Memoization Decorator**
   ```python
   # Create decorator that caches results
   # Test with fibonacci
   ```

5. **Retry Decorator**
   ```python
   # Create decorator that retries failed function
   # Configurable max attempts and delay
   ```

6. **Pipeline with Generators**
   ```python
   # Create pipeline of generators
   # Example: read -> filter -> map -> output
   ```

### Advanced Level

7. **Dependency Injection Decorator**
   ```python
   # Create decorator that injects dependencies
   # Example: @inject(db=Database, cache=Cache)
   ```

8. **Circuit Breaker Decorator**
   ```python
   # Create decorator that stops calling after failures
   # Reset after timeout period
   ```

9. **Async Wrapper**
   ```python
   # Create decorator that makes sync function async
   # Run in thread pool
   ```

---

## Quick Reference Card

```python
# Nested functions
def outer(x):
    def inner(y):
        return x + y
    return inner

# Closures
def make_adder(x):
    return lambda y: x + y

# Decorators
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

# Generators
def generator():
    for i in range(10):
        yield i

# functools
from functools import partial, lru_cache, wraps, singledispatch, reduce

# Function attributes
func.__name__
func.__doc__
func.__annotations__
func.__defaults__
```

## Next Steps

- Go to [03_main_and_name.md](03_main_and_name.md) for understanding the '__main__' and '__name__' you saw earlier.

---

*Master advanced functions to write powerful, flexible Python code! 🐍✨*
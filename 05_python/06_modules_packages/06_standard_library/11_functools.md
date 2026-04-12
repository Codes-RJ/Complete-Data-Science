# 📘 FUNCTOOLS MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Functools?](#what-is-functools)
2. [`partial` – Fix Arguments](#partial--fix-arguments)
3. [`partialmethod` – Partial for Methods](#partialmethod--partial-for-methods)
4. [`wraps` – Preserve Metadata](#wraps--preserve-metadata)
5. [`lru_cache` – Memoization](#lru_cache--memoization)
6. [`cache` – Simple Cache](#cache--simple-cache)
7. [`cached_property` – Lazy Properties](#cached_property--lazy-properties)
8. [`reduce` – Cumulative Operations](#reduce--cumulative-operations)
9. [`singledispatch` – Generic Functions](#singledispatch--generic-functions)
10. [`total_ordering` – Complete Comparisons](#total_ordering--complete-comparisons)
11. [`update_wrapper` – Update Wrapper](#update_wrapper--update-wrapper)
12. [`cmp_to_key` – Old-Style Comparison](#cmp_to_key--old-style-comparison)
13. [Real-World Examples](#real-world-examples)
14. [Practice Exercises](#practice-exercises)

---

## What is Functools?

The `functools` module provides higher-order functions that act on or return other functions. It's essential for functional programming in Python.

```python
from functools import partial, wraps, lru_cache, reduce

# partial - fix arguments
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(5))  # 25

# lru_cache - memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# reduce - cumulative operations
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15
```

**Key Benefits:**
- ✅ Create specialized functions from generic ones
- ✅ Cache function results for performance
- ✅ Preserve function metadata in decorators
- ✅ Implement function overloading
- ✅ Reduce boilerplate code

---

## `partial` – Fix Arguments

`partial` creates a new function with some arguments pre-filled.

### Basic Usage

```python
from functools import partial

def power(base, exponent):
    """Raise base to exponent power"""
    return base ** exponent

# Fix exponent to 2
square = partial(power, exponent=2)
print(square(5))   # 25
print(square(10))  # 100

# Fix base to 2
powers_of_2 = partial(power, 2)
print(powers_of_2(3))   # 8
print(powers_of_2(5))   # 32

# Fix multiple arguments
def greet(greeting, name, punctuation):
    return f"{greeting}, {name}{punctuation}"

say_hello = partial(greet, "Hello", punctuation="!")
print(say_hello("Alice"))  # Hello, Alice!
```

### Practical Partial Examples

```python
from functools import partial

# Creating specialized functions
import math

sqrt = partial(pow, exp=0.5)
print(sqrt(16))  # 4.0

# API calls with fixed base URL
import requests

get_github = partial(requests.get, 'https://api.github.com')
# response = get_github('/users/octocat')

# Logging with fixed level
import logging

info_log = partial(logging.info, extra={'source': 'app'})
# info_log("Application started")

# Sorting with custom key
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

sort_by_grade = partial(sorted, key=lambda x: x['grade'])
sorted_students = sort_by_grade(students)
print(sorted_students)

# Map with fixed function
double = partial(lambda x: x * 2)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

---

## `partialmethod` – Partial for Methods

Similar to `partial` but for class methods.

```python
from functools import partialmethod

class Calculator:
    def power(self, base, exponent):
        return base ** exponent
    
    square = partialmethod(power, exponent=2)
    cube = partialmethod(power, exponent=3)

calc = Calculator()
print(calc.square(5))  # 25
print(calc.cube(5))    # 125

# With default arguments
class Logger:
    def __init__(self, level="INFO"):
        self.level = level
    
    def log(self, message, level=None):
        level = level or self.level
        print(f"[{level}] {message}")
    
    debug = partialmethod(log, level="DEBUG")
    error = partialmethod(log, level="ERROR")
    warning = partialmethod(log, level="WARNING")

logger = Logger()
logger.debug("Debug message")   # [DEBUG] Debug message
logger.error("Error message")   # [ERROR] Error message
```

---

## `wraps` – Preserve Metadata

`wraps` is a decorator that preserves function metadata when creating decorators.

### Without wraps (Problem)

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """Say hello docstring"""
    print("Hello")

print(say_hello.__name__)  # wrapper (lost original name)
print(say_hello.__doc__)   # Wrapper docstring (lost original doc)
```

### With wraps (Solution)

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """Say hello docstring"""
    print("Hello")

print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)   # Say hello docstring
```

### Practical wraps Example

```python
from functools import wraps
import time

def timer(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

def log(func):
    """Decorator to log function calls"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timer
@log
def add(a, b):
    """Add two numbers"""
    return a + b

# Metadata is preserved
print(add.__name__)  # add
print(add.__doc__)   # Add two numbers
print(add(5, 3))
# Calling add with args=(5, 3), kwargs={}
# add returned 8
# add took 0.0000s
```

---

## `lru_cache` – Memoization

`lru_cache` caches function results based on arguments (Least Recently Used).

### Basic Usage

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    """Calculate Fibonacci number with caching"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call (computes)
print(fibonacci(35))  # 9227465

# Second call (returns from cache)
print(fibonacci(35))  # Instant

# Cache info
print(fibonacci.cache_info())
# CacheInfo(hits=34, misses=36, maxsize=128, currsize=36)
```

### LRU Cache Examples

```python
from functools import lru_cache
import time

@lru_cache(maxsize=3)
def expensive_function(n):
    """Simulate expensive computation"""
    print(f"Computing {n}...")
    time.sleep(1)
    return n ** 2

# Fill cache
print(expensive_function(1))  # Computing 1... 1
print(expensive_function(2))  # Computing 2... 4
print(expensive_function(3))  # Computing 3... 9

# Cache hit (uses cached values)
print(expensive_function(2))  # 4 (from cache)

# Add new item (LRU removes oldest)
print(expensive_function(4))  # Computing 4... 16
# Now 1 is removed (least recently used)

print(expensive_function(1))  # Computing 1... (recomputed)

# Clear cache
expensive_function.cache_clear()
print(expensive_function.cache_info())
# CacheInfo(hits=0, misses=0, maxsize=3, currsize=0)
```

### Real-World Caching Examples

```python
from functools import lru_cache
import requests

@lru_cache(maxsize=100)
def get_user(user_id):
    """Get user from API with caching"""
    print(f"Fetching user {user_id} from API...")
    # Simulate API call
    return {"id": user_id, "name": f"User{user_id}"}

print(get_user(1))  # Fetches
print(get_user(1))  # From cache
print(get_user(2))  # Fetches

# Database query caching
@lru_cache(maxsize=1000)
def get_products(category, min_price=0, max_price=float('inf')):
    """Get products with caching"""
    print(f"Querying database for category={category}, price={min_price}-{max_price}")
    # Simulate database query
    return [{"id": 1, "name": "Product1", "price": 100}]

get_products("electronics", 0, 500)
get_products("electronics", 0, 500)  # Cached

# With unbounded cache
@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))  # 3628800
print(factorial.cache_info())
```

---

## `cache` – Simple Cache

Python 3.9+ introduced `@cache` as a simpler version of `lru_cache(maxsize=None)`.

```python
from functools import cache

@cache
def fibonacci(n):
    """Calculate Fibonacci with unbounded cache"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # 354224848179261915075

# Same as lru_cache with maxsize=None
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fibonacci(n): ...
```

---

## `cached_property` – Lazy Properties

`cached_property` computes a property once and caches the result.

```python
from functools import cached_property

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def processed_data(self):
        """Expensive processing, computed once"""
        print("Processing data...")
        # Simulate expensive operation
        return [x * 2 for x in self.data]
    
    @cached_property
    def statistics(self):
        """Calculate statistics, computed once"""
        print("Calculating statistics...")
        data = self.processed_data  # Uses cached property
        return {
            'sum': sum(data),
            'mean': sum(data) / len(data),
            'max': max(data),
            'min': min(data)
        }

# Usage
processor = DataProcessor([1, 2, 3, 4, 5])
print(processor.processed_data)  # Processing data... [2, 4, 6, 8, 10]
print(processor.processed_data)  # [2, 4, 6, 8, 10] (cached, no processing)

print(processor.statistics)  # Calculating statistics... {'sum': 30, 'mean': 6.0, ...}
print(processor.statistics)  # From cache

# Delete cached value to recompute
del processor.processed_data
print(processor.processed_data)  # Processing data... (recomputed)
```

---

## `reduce` – Cumulative Operations

`reduce` applies a function cumulatively to the items of an iterable.

```python
from functools import reduce

# Sum of numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
max_val = reduce(lambda x, y: x if x > y else y, numbers)
print(max_val)  # 5

# String concatenation
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: f"{x} {y}", words)
print(sentence)  # Hello World Python

# With initial value
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115

# Flatten list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, list_of_lists)
print(flattened)  # [1, 2, 3, 4, 5, 6]

# Build dictionary
pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = reduce(lambda d, p: {**d, p[0]: p[1]}, pairs, {})
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}
```

---

## `singledispatch` – Generic Functions

`singledispatch` implements function overloading based on the type of the first argument.

### Basic Usage

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

# Usage
print(process(42))           # Processing integer: 42
print(process(3.14))         # Processing float: 3.14
print(process("hello"))      # Processing string: hello
print(process([1, 2, 3]))    # Processing list of length 3
print(process({"a": 1}))     # Processing dict with 1 keys
print(process(True))         # Unknown type: bool
```

### Registering Multiple Types

```python
from functools import singledispatch

@singledispatch
def serialize(obj):
    raise TypeError(f"Can't serialize {type(obj)}")

@serialize.register(str)
def _(obj):
    return f'"{obj}"'

@serialize.register(int)
@serialize.register(float)
def _(obj):
    return str(obj)

@serialize.register(list)
def _(obj):
    items = [serialize(item) for item in obj]
    return f"[{', '.join(items)}]"

@serialize.register(dict)
def _(obj):
    items = [f'{serialize(k)}: {serialize(v)}' for k, v in obj.items()]
    return f"{{{', '.join(items)}}}"

# Usage
print(serialize("hello"))     # "hello"
print(serialize(42))          # 42
print(serialize([1, 2, 3]))   # [1, 2, 3]
print(serialize({"name": "Alice", "age": 30}))
# {"name": "Alice", "age": 30}
```

### Registering with Classes

```python
from functools import singledispatch

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

@singledispatch
def make_sound(animal):
    return "Unknown animal sound"

@make_sound.register(Dog)
def _(animal):
    return "Woof!"

@make_sound.register(Cat)
def _(animal):
    return "Meow!"

print(make_sound(Dog()))  # Woof!
print(make_sound(Cat()))  # Meow!
```

---

## `total_ordering` – Complete Comparisons

`total_ordering` fills in missing comparison methods based on `__eq__` and one other comparison.

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
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Now all comparison operators work
alice = Person("Alice", 30)
bob = Person("Bob", 25)
charlie = Person("Charlie", 30)

print(alice > bob)     # True (provided by total_ordering)
print(alice < bob)     # False
print(alice == charlie) # True
print(alice >= bob)    # True
print(alice <= bob)    # False

# Without total_ordering, you'd need to define all methods
# __eq__, __lt__, __le__, __gt__, __ge__
```

---

## `update_wrapper` – Update Wrapper

`update_wrapper` manually updates a wrapper function's metadata.

```python
from functools import update_wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    # Manually update wrapper
    update_wrapper(wrapper, func)
    return wrapper

@my_decorator
def say_hello():
    """Say hello function"""
    print("Hello")

print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)   # Say hello function

# Equivalent to using @wraps
```

---

## `cmp_to_key` – Old-Style Comparison

`cmp_to_key` converts old-style comparison functions to key functions for sorting.

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

# Sort by custom logic
def compare_numbers(a, b):
    # Sort by absolute value, then by sign
    if abs(a) != abs(b):
        return abs(a) - abs(b)
    return b - a  # Positive first

numbers = [5, -3, 2, -7, 1, -1, 4]
sorted_numbers = sorted(numbers, key=cmp_to_key(compare_numbers))
print(sorted_numbers)  # [1, -1, 2, -3, 4, 5, -7]
```

---

## Real-World Examples

### Example 1: API Client with Caching

```python
from functools import lru_cache, wraps
import requests
import time

class APIClient:
    def __init__(self, base_url, cache_ttl=300):
        self.base_url = base_url
        self.cache_ttl = cache_ttl
        self._cache = {}
        self._cache_time = {}
    
    def _is_cache_valid(self, key):
        if key not in self._cache_time:
            return False
        return time.time() - self._cache_time[key] < self.cache_ttl
    
    def get(self, endpoint, use_cache=True):
        """GET request with caching"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        if use_cache and self._is_cache_valid(url):
            print(f"Cache hit for {url}")
            return self._cache[url]
        
        print(f"Fetching {url}")
        response = requests.get(url)
        data = response.json()
        
        if use_cache:
            self._cache[url] = data
            self._cache_time[url] = time.time()
        
        return data
    
    def clear_cache(self):
        """Clear all cache"""
        self._cache.clear()
        self._cache_time.clear()

# Usage (simulated)
client = APIClient("https://api.github.com")
# data = client.get("/users/octocat")
# data = client.get("/users/octocat")  # From cache
```

### Example 2: Function Registry with singledispatch

```python
from functools import singledispatch
import json
import csv

class DataSerializer:
    @singledispatch
    @staticmethod
    def serialize(data):
        raise TypeError(f"Cannot serialize {type(data)}")
    
    @serialize.register(dict)
    @staticmethod
    def _serialize_dict(data):
        return json.dumps(data)
    
    @serialize.register(list)
    @staticmethod
    def _serialize_list(data):
        return json.dumps(data)
    
    @serialize.register(str)
    @staticmethod
    def _serialize_str(data):
        return data
    
    @serialize.register(int)
    @serialize.register(float)
    @staticmethod
    def _serialize_number(data):
        return str(data)
    
    @serialize.register(tuple)
    @staticmethod
    def _serialize_tuple(data):
        return ','.join(str(x) for x in data)

class DataDeserializer:
    @singledispatch
    @staticmethod
    def deserialize(data, target_type):
        raise TypeError(f"Cannot deserialize to {target_type}")
    
    @deserialize.register(dict)
    @staticmethod
    def _deserialize_dict(data):
        return json.loads(data) if isinstance(data, str) else data
    
    @deserialize.register(list)
    @staticmethod
    def _deserialize_list(data):
        return json.loads(data) if isinstance(data, str) else data
    
    @deserialize.register(str)
    @staticmethod
    def _deserialize_str(data):
        return str(data)
    
    @deserialize.register(int)
    @staticmethod
    def _deserialize_int(data):
        return int(data)
    
    @deserialize.register(float)
    @staticmethod
    def _deserialize_float(data):
        return float(data)

# Usage
serializer = DataSerializer()
deserializer = DataDeserializer()

data = {"name": "Alice", "age": 30}
serialized = serializer.serialize(data)
print(f"Serialized: {serialized}")

deserialized = deserializer.deserialize(serialized, dict)
print(f"Deserialized: {deserialized}")

# Different types
print(serializer.serialize([1, 2, 3]))  # [1, 2, 3]
print(serializer.serialize(42))         # 42
print(serializer.serialize((1, 2, 3)))  # 1,2,3
```

### Example 3: Performance Optimization with LRU Cache

```python
from functools import lru_cache
import time
import random

class DataProcessor:
    def __init__(self):
        self.query_count = 0
    
    @lru_cache(maxsize=1000)
    def expensive_query(self, query_params):
        """Expensive database query with caching"""
        self.query_count += 1
        print(f"Executing query #{self.query_count}: {query_params}")
        # Simulate expensive operation
        time.sleep(0.5)
        return {
            'params': query_params,
            'result': random.randint(1, 1000),
            'timestamp': time.time()
        }
    
    def get_stats(self):
        """Get cache statistics"""
        return {
            'query_count': self.query_count,
            'cache_info': self.expensive_query.cache_info(),
            'cache_clear': self.expensive_query.cache_clear
        }

# Usage
processor = DataProcessor()

# First calls (cache misses)
for i in range(5):
    processor.expensive_query(f"query_{i % 3}")

# Repeated calls (cache hits)
for i in range(5):
    processor.expensive_query(f"query_{i % 3}")

print(f"Total queries executed: {processor.query_count}")
print(f"Cache info: {processor.expensive_query.cache_info()}")
```

### Example 4: Partial Application for Data Processing

```python
from functools import partial
import math

class DataPipeline:
    @staticmethod
    def transform(data, operations):
        """Apply sequence of operations to data"""
        result = data
        for op in operations:
            result = op(result)
        return result
    
    @staticmethod
    def create_normalizer(min_val, max_val):
        """Create normalization function"""
        def normalize(x):
            return (x - min_val) / (max_val - min_val)
        return normalize
    
    @staticmethod
    def create_scaler(factor):
        """Create scaling function"""
        return partial(lambda x, f: x * f, factor=factor)
    
    @staticmethod
    def create_rounder(decimals=2):
        """Create rounding function"""
        return partial(lambda x, d: round(x, d), d=decimals)

# Create processing pipeline
normalize = DataPipeline.create_normalizer(0, 100)
scale = DataPipeline.create_scaler(2)
round_result = DataPipeline.create_rounder(2)

# Process single value
value = 75
processed = DataPipeline.transform(value, [normalize, scale, round_result])
print(f"Original: {value} -> Processed: {processed}")

# Process list of values
values = [10, 25, 50, 75, 90]
results = [DataPipeline.transform(v, [normalize, scale, round_result]) for v in values]
print(f"Original: {values}")
print(f"Processed: {results}")

# Create specialized functions
normalize_score = DataPipeline.create_normalizer(0, 100)
double_score = DataPipeline.create_scaler(2)
round_score = DataPipeline.create_rounder(1)

process_score = partial(DataPipeline.transform, operations=[normalize_score, double_score, round_score])

scores = [45, 67, 89, 34, 78]
processed_scores = list(map(process_score, scores))
print(f"Processed scores: {processed_scores}")
```

### Example 5: Generic Function for Data Validation

```python
from functools import singledispatch
from datetime import datetime

class Validator:
    @singledispatch
    @staticmethod
    def validate(value):
        """Default validation"""
        return True, "Valid"
    
    @validate.register(str)
    @staticmethod
    def _(value):
        if not value:
            return False, "String cannot be empty"
        if len(value) > 255:
            return False, "String too long (max 255)"
        return True, "Valid"
    
    @validate.register(int)
    @staticmethod
    def _(value):
        if value < 0:
            return False, "Integer cannot be negative"
        if value > 10**9:
            return False, "Integer too large"
        return True, "Valid"
    
    @validate.register(float)
    @staticmethod
    def _(value):
        if math.isnan(value):
            return False, "Cannot be NaN"
        if math.isinf(value):
            return False, "Cannot be infinite"
        return True, "Valid"
    
    @validate.register(list)
    @staticmethod
    def _(value):
        if len(value) > 1000:
            return False, "List too large (max 1000 items)"
        for item in value:
            valid, msg = Validator.validate(item)
            if not valid:
                return False, f"Invalid item: {msg}"
        return True, "Valid"
    
    @validate.register(dict)
    @staticmethod
    def _(value):
        if len(value) > 100:
            return False, "Dict too large (max 100 keys)"
        for k, v in value.items():
            valid, msg = Validator.validate(k)
            if not valid:
                return False, f"Invalid key: {msg}"
            valid, msg = Validator.validate(v)
            if not valid:
                return False, f"Invalid value for key '{k}': {msg}"
        return True, "Valid"
    
    @validate.register(datetime)
    @staticmethod
    def _(value):
        if value > datetime.now():
            return False, "Date cannot be in the future"
        return True, "Valid"

# Usage
print(Validator.validate("hello"))     # (True, 'Valid')
print(Validator.validate(""))          # (False, 'String cannot be empty')
print(Validator.validate(42))          # (True, 'Valid')
print(Validator.validate(-5))          # (False, 'Integer cannot be negative')
print(Validator.validate([1, 2, 3]))   # (True, 'Valid')
print(Validator.validate([1, "", 3]))  # (False, 'Invalid item: String cannot be empty')
```

---

## Practice Exercises

### Beginner Level

1. **Partial Function**
   ```python
   # Create a partial function that multiplies by 2
   ```

2. **LRU Cache**
   ```python
   # Cache Fibonacci function results
   ```

3. **Reduce Sum**
   ```python
   # Calculate sum of list using reduce
   ```

### Intermediate Level

4. **Timer Decorator**
   ```python
   # Create timer decorator that preserves metadata
   ```

5. **Generic Serializer**
   ```python
   # Use singledispatch to serialize different types
   ```

6. **Cached Property**
   ```python
   # Implement lazy loading using cached_property
   ```

### Advanced Level

7. **API Client with Cache**
   ```python
   # Build API client with TTL cache using lru_cache
   ```

8. **Data Pipeline**
   ```python
   # Create data processing pipeline using partial
   ```

9. **Validation System**
   ```python
   # Build generic validation using singledispatch
   ```

---

## Quick Reference Card

```python
from functools import partial, wraps, lru_cache, cache, cached_property, reduce, singledispatch, total_ordering, update_wrapper, cmp_to_key

# Partial application
partial(func, *args, **kwargs)          # Fix arguments
partialmethod(func, *args, **kwargs)    # Fix method arguments

# Decorators
@wraps(func)                            # Preserve metadata
@lru_cache(maxsize=128)                 # Cache with LRU
@cache                                  # Simple cache (3.9+)
@cached_property                        # Lazy property
@total_ordering                         # Complete comparisons

# Functional tools
reduce(func, iterable, initial=None)    # Cumulative operation
@singledispatch                         # Generic functions
cmp_to_key(func)                        # Convert comparison to key

# Wrapper utilities
update_wrapper(wrapper, wrapped)        # Update wrapper metadata
```

---

## Next Step

- Move to [12_statistics.md](12_statistics.md) to learn about statistical functions.

---

*Master functools for powerful functional programming in Python! 🐍✨*
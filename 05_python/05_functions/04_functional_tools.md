# 📘 FUNCTIONAL TOOLS – COMPLETE GUIDE

## 📌 Table of Contents
1. [Introduction to Functional Tools](#introduction-to-functional-tools)
2. [`map()` Function](#map-function)
3. [`filter()` Function](#filter-function)
4. [`reduce()` Function](#reduce-function)
5. [`zip()` Function](#zip-function)
6. [`enumerate()` Function](#enumerate-function)
7. [`sorted()` Function](#sorted-function)
8. [`any()` and `all()` Functions](#any-and-all-functions)
9. [`zip_longest()` from itertools](#zip_longest-from-itertools)
10. [`accumulate()` from itertools](#accumulate-from-itertools)
11. [Real-World Examples](#real-world-examples)
12. [Common Pitfalls](#common-pitfalls)
13. [Practice Exercises](#practice-exercises)

---

## Introduction to Functional Tools

Python provides several built-in functions that support functional programming paradigms. These tools allow you to process data in a declarative, expressive way without explicit loops.

```python
# Traditional loop
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)

# Functional approach
squared = list(map(lambda x: x ** 2, numbers))
```

**Why Functional Tools:**
- More concise and readable
- Often faster than manual loops
- Work well with lambda functions
- Enable lazy evaluation (generators)
- Compose operations easily

---

## `map()` Function

`map()` applies a function to every item in an iterable and returns an iterator.

### Basic Syntax

```python
map(function, iterable)
map(function, iterable1, iterable2, ...)  # Multiple iterables
```

### Basic Examples

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# Convert to uppercase
words = ["hello", "world", "python"]
upper_words = map(str.upper, words)
print(list(upper_words))  # ['HELLO', 'WORLD', 'PYTHON']

# With multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
sums = map(lambda x, y: x + y, a, b)
print(list(sums))  # [5, 7, 9]

# Convert strings to integers
str_nums = ["1", "2", "3", "4", "5"]
int_nums = map(int, str_nums)
print(list(int_nums))  # [1, 2, 3, 4, 5]
```

### Map with User-Defined Functions

```python
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Map with class method
class Calculator:
    @staticmethod
    def square(x):
        return x ** 2

squared = list(map(Calculator.square, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### Map with Multiple Iterables

```python
# Element-wise addition
list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]

result = map(lambda a, b, c: a + b + c, list1, list2, list3)
print(list(result))  # [111, 222, 333]

# Element-wise multiplication
prices = [10, 20, 30]
quantities = [2, 3, 1]
totals = map(lambda p, q: p * q, prices, quantities)
print(list(totals))  # [20, 60, 30]

# Stops at shortest iterable
short = [1, 2]
long = [10, 20, 30, 40]
result = map(lambda x, y: x + y, short, long)
print(list(result))  # [11, 22] (stops at 2)
```

### Map with None (Identity Function)

```python
# Using None as function returns the iterable itself
numbers = [1, 2, 3, 4, 5]
result = map(None, numbers)  # In Python 2, but not in Python 3

# In Python 3, use identity function
result = map(lambda x: x, numbers)
print(list(result))  # [1, 2, 3, 4, 5]
```

### Map Returns Iterator (Lazy Evaluation)

```python
# map returns an iterator, not a list
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)

print(type(squared))  # <class 'map'>

# Convert to list when needed
squared_list = list(squared)
print(squared_list)  # [1, 4, 9, 16, 25]

# Iterator can only be used once
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]
print(list(squared))  # [] (exhausted)
```

---

## `filter()` Function

`filter()` constructs an iterator from elements of an iterable for which a function returns true.

### Basic Syntax

```python
filter(function, iterable)
# function should return True/False
```

### Basic Examples

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6, 8, 10]

# Filter strings with length > 3
words = ["cat", "dog", "elephant", "bird", "fox"]
long_words = filter(lambda w: len(w) > 3, words)
print(list(long_words))  # ['elephant', 'bird']

# Filter positive numbers
numbers = [-5, -2, 0, 3, 7, -1, 4]
positives = filter(lambda x: x > 0, numbers)
print(list(positives))  # [3, 7, 4]
```

### Filter with None (Remove Falsy Values)

```python
# Using None removes falsy values
values = [0, 1, False, True, "", "hello", None, [], [1, 2]]
truthy = filter(None, values)
print(list(truthy))  # [1, True, 'hello', [1, 2]]

# Equivalent to
truthy = [v for v in values if v]
```

### Filter with User-Defined Functions

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 51)
primes = filter(is_prime, numbers)
print(list(primes))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# With class method
class StringFilter:
    @staticmethod
    def has_vowel(s):
        return any(c in 'aeiou' for c in s.lower())

words = ["hello", "why", "sky", "apple", "fly"]
with_vowels = filter(StringFilter.has_vowel, words)
print(list(with_vowels))  # ['hello', 'apple']
```

### Filter with Multiple Conditions

```python
data = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 22, "active": True},
]

# Filter active users over 18
active_adults = filter(lambda x: x["active"] and x["age"] >= 18, data)
print(list(active_adults))
# [{'name': 'Alice', 'age': 25, 'active': True},
#  {'name': 'Diana', 'age': 22, 'active': True}]
```

---

## `reduce()` Function

`reduce()` applies a function cumulatively to the items of an iterable, reducing it to a single value.

### Basic Syntax

```python
from functools import reduce

reduce(function, iterable)
reduce(function, iterable, initializer)
```

### Basic Examples

```python
from functools import reduce

# Sum of all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
max_val = reduce(lambda x, y: x if x > y else y, numbers)
print(max_val)  # 5

# Find minimum
min_val = reduce(lambda x, y: x if x < y else y, numbers)
print(min_val)  # 1
```

### Reduce with Initializer

```python
from functools import reduce

# Sum with initial value
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115

# Product with initial value
product = reduce(lambda x, y: x * y, numbers, 10)
print(product)  # 1200

# Works with empty iterable
empty = []
result = reduce(lambda x, y: x + y, empty, 0)
print(result)  # 0 (no error)
```

### Complex Reduce Examples

```python
from functools import reduce

# Flatten list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, list_of_lists)
print(flattened)  # [1, 2, 3, 4, 5, 6]

# Concatenate strings
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: f"{x} {y}", words)
print(sentence)  # "Hello World Python"

# Find second largest number
numbers = [5, 2, 8, 1, 9, 3]
def second_largest(acc, x):
    largest, second = acc
    if x > largest:
        return (x, largest)
    elif x > second:
        return (largest, x)
    return (largest, second)

largest, second = reduce(second_largest, numbers, (float('-inf'), float('-inf')))
print(f"Second largest: {second}")  # 8

# Build dictionary from list
pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = reduce(lambda d, p: {**d, p[0]: p[1]}, pairs, {})
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}
```

---

## `zip()` Function

`zip()` aggregates elements from multiple iterables into tuples.

### Basic Syntax

```python
zip(iterable1, iterable2, ...)
```

### Basic Examples

```python
# Zip two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
pairs = zip(names, ages)
print(list(pairs))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Zip three lists
cities = ["NYC", "LA", "Chicago"]
zipped = zip(names, ages, cities)
print(list(zipped))
# [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

# Stops at shortest iterable
short = [1, 2]
long = [10, 20, 30]
result = zip(short, long)
print(list(result))  # [(1, 10), (2, 20)] (stops at 2)
```

### Unzipping with `zip(*)`

```python
# Zip to combine
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(zipped)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unzip to separate
unzipped_names, unzipped_ages = zip(*zipped)
print(unzipped_names)  # ('Alice', 'Bob', 'Charlie')
print(unzipped_ages)   # (25, 30, 35)
```

### Creating Dictionaries with Zip

```python
# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
dictionary = dict(zip(keys, values))
print(dictionary)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# With more lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = dict(zip(names, scores))
print(grades)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}
```

### Looping with Zip

```python
# Iterate over multiple lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# With enumerate
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i+1}. {name}: {score}")
# 1. Alice: 85
# 2. Bob: 92
# 3. Charlie: 78
```

---

## `enumerate()` Function

`enumerate()` adds a counter to an iterable.

### Basic Syntax

```python
enumerate(iterable, start=0)
```

### Basic Examples

```python
# Basic enumeration
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry

# Convert to list
enum_list = list(enumerate(fruits))
print(enum_list)  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### Enumerate with Dictionary

```python
# Convert list to dictionary with index as key
fruits = ["apple", "banana", "cherry"]
indexed = dict(enumerate(fruits))
print(indexed)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

# With start offset
indexed = dict(enumerate(fruits, 1))
print(indexed)  # {1: 'apple', 2: 'banana', 3: 'cherry'}
```

---

## `sorted()` Function

`sorted()` returns a new sorted list from an iterable.

### Basic Syntax

```python
sorted(iterable, key=None, reverse=False)
```

### Basic Examples

```python
# Sort numbers
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Sort strings (alphabetical)
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)
print(sorted_words)  # ['apple', 'banana', 'cherry', 'date']

# Reverse order
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  # [9, 5, 4, 3, 2, 1, 1]
```

### Sorting with Key

```python
# Sort by length
words = ["python", "java", "c", "go", "rust"]
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)  # ['c', 'go', 'java', 'rust', 'python']

# Sort by last character
sorted_by_last = sorted(words, key=lambda x: x[-1])
print(sorted_by_last)  # ['java', 'c', 'python', 'go', 'rust']

# Sort dictionary by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_by_score = sorted(scores.items(), key=lambda x: x[1])
print(sorted_by_score)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort by multiple keys
students = [
    ("Alice", 85, "A"),
    ("Bob", 85, "B"),
    ("Charlie", 92, "A"),
]
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
print(sorted_students)
# [('Alice', 85, 'A'), ('Bob', 85, 'B'), ('Charlie', 92, 'A')]
```

---

## `any()` and `all()` Functions

### `any()` – At Least One True

```python
# Returns True if at least one element is truthy
print(any([True, False, False]))   # True
print(any([False, False, False]))  # False
print(any([1, 0, 0]))              # True
print(any([0, 0, 0]))              # False
print(any([]))                     # False

# Real use: Check if any condition met
numbers = [1, 2, 3, 4, 5]
has_even = any(n % 2 == 0 for n in numbers)
print(has_even)  # True

# Check if any string is empty
strings = ["hello", "", "world"]
has_empty = any(s == "" for s in strings)
print(has_empty)  # True
```

### `all()` – All True

```python
# Returns True only if all elements are truthy
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([1, 2, 3]))             # True
print(all([1, 0, 3]))             # False
print(all([]))                    # True (vacuously true)

# Real use: Check if all conditions met
numbers = [2, 4, 6, 8, 10]
all_even = all(n % 2 == 0 for n in numbers)
print(all_even)  # True

# Check if all strings have length > 0
strings = ["hello", "world", "python"]
all_non_empty = all(len(s) > 0 for s in strings)
print(all_non_empty)  # True
```

---

## `zip_longest()` from itertools

`zip_longest()` zips iterables, filling missing values with a fillvalue.

```python
from itertools import zip_longest

# Regular zip stops at shortest
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')]

# zip_longest continues with fillvalue
print(list(zip_longest(a, b)))  # [(1, 'a'), (2, 'b'), (3, None)]

# Custom fillvalue
print(list(zip_longest(a, b, fillvalue='X')))  # [(1, 'a'), (2, 'b'), (3, 'X')]

# Multiple iterables
c = ['x', 'y', 'z', 'w']
result = zip_longest(a, b, c, fillvalue='-')
print(list(result))
# [(1, 'a', 'x'), (2, 'b', 'y'), (3, '-', 'z'), ('-', '-', 'w')]
```

---

## `accumulate()` from itertools

`accumulate()` makes an iterator that returns accumulated sums (or other binary functions).

```python
from itertools import accumulate

# Running sum
numbers = [1, 2, 3, 4, 5]
running_sum = list(accumulate(numbers))
print(running_sum)  # [1, 3, 6, 10, 15]

# Running product
import operator
running_product = list(accumulate(numbers, operator.mul))
print(running_product)  # [1, 2, 6, 24, 120]

# Running max
running_max = list(accumulate([3, 1, 4, 1, 5], max))
print(running_max)  # [3, 3, 4, 4, 5]

# With custom function
def running_average(acc, x):
    count, total = acc
    count += 1
    total += x
    return (count, total)

result = list(accumulate([10, 20, 30, 40], running_average, initial=(0, 0)))
averages = [total/count for count, total in result[1:]]
print(averages)  # [10.0, 15.0, 20.0, 25.0]
```

---

## Real-World Examples

### Example 1: Data Processing Pipeline

```python
def process_data(data):
    """Complete data processing pipeline using functional tools"""
    
    # Filter out invalid entries
    valid = filter(lambda x: x.get('value') is not None, data)
    
    # Extract and convert values
    values = map(lambda x: float(x['value']), valid)
    
    # Calculate statistics
    from functools import reduce
    
    def stats(acc, x):
        count, total = acc
        return (count + 1, total + x)
    
    count, total = reduce(stats, values, (0, 0))
    
    if count == 0:
        return None
    
    return {
        'count': count,
        'sum': total,
        'average': total / count,
        'min': min(values) if count > 0 else None,
        'max': max(values) if count > 0 else None,
    }

# Sample data
data = [
    {'id': 1, 'value': '10.5'},
    {'id': 2, 'value': None},
    {'id': 3, 'value': '20.3'},
    {'id': 4, 'value': '15.7'},
    {'id': 5, 'value': None},
]

result = process_data(data)
print(f"Count: {result['count']}")
print(f"Sum: {result['sum']}")
print(f"Average: {result['average']:.2f}")
```

### Example 2: Matrix Operations

```python
def matrix_multiply(A, B):
    """Multiply two matrices using functional tools"""
    # Transpose B for easier multiplication
    B_T = list(zip(*B))
    
    # Multiply matrices
    result = [
        [sum(a * b for a, b in zip(row, col)) for col in B_T]
        for row in A
    ]
    return result

def matrix_transpose(matrix):
    """Transpose matrix using zip"""
    return list(zip(*matrix))

def matrix_sum(matrix):
    """Sum all elements in matrix using reduce"""
    from functools import reduce
    flat = reduce(lambda x, y: x + y, matrix, [])
    return sum(flat)

def matrix_map(func, matrix):
    """Apply function to each element"""
    return [list(map(func, row)) for row in matrix]

# Example
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nA × B:")
product = matrix_multiply(A, B)
for row in product:
    print(row)

print("\nTranspose of A:")
transpose = matrix_transpose(A)
for row in transpose:
    print(row)

print(f"\nSum of all elements in A: {matrix_sum(A)}")

print("\nMatrix A * 2:")
doubled = matrix_map(lambda x: x * 2, A)
for row in doubled:
    print(row)
```

### Example 3: Log File Analyzer

```python
import re
from functools import reduce
from collections import Counter

def parse_log_line(line):
    """Parse a single log line"""
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)'
    match = re.match(pattern, line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return None

def analyze_logs(log_lines):
    """Analyze log data using functional tools"""
    
    # Parse all lines
    parsed = map(parse_log_line, log_lines)
    
    # Filter out None (invalid lines)
    valid = filter(None, parsed)
    
    # Group by log level
    levels = map(lambda x: x['level'], valid)
    
    # Count occurrences
    level_counts = Counter(levels)
    
    # Find error messages
    errors = filter(lambda x: x['level'] == 'ERROR', parsed)
    error_messages = list(map(lambda x: x['message'], errors))
    
    # Calculate statistics
    total_lines = len(log_lines)
    valid_lines = len(list(valid))
    
    return {
        'total_lines': total_lines,
        'valid_lines': valid_lines,
        'level_counts': dict(level_counts),
        'errors': error_messages[:10]  # First 10 errors
    }

# Sample log data
log_data = [
    "2024-01-15 10:00:00 [INFO] Server started",
    "2024-01-15 10:00:05 [INFO] User login: alice",
    "2024-01-15 10:00:10 [ERROR] Database connection failed",
    "2024-01-15 10:00:15 [WARNING] High memory usage",
    "2024-01-15 10:00:20 [INFO] User logout: alice",
    "2024-01-15 10:00:25 [ERROR] File not found: config.txt",
    "invalid log line",
    "2024-01-15 10:00:30 [INFO] Server shutdown",
]

results = analyze_logs(log_data)
print(f"Total lines: {results['total_lines']}")
print(f"Valid lines: {results['valid_lines']}")
print(f"Level counts: {results['level_counts']}")
print(f"First 2 errors: {results['errors'][:2]}")
```

### Example 4: Student Grade Processor

```python
from functools import reduce

class GradeProcessor:
    @staticmethod
    def calculate_averages(grades):
        """Calculate average for each student"""
        return {
            name: sum(scores) / len(scores)
            for name, scores in grades.items()
        }
    
    @staticmethod
    def get_top_students(grades, n=3):
        """Get top n students by average"""
        averages = GradeProcessor.calculate_averages(grades)
        sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_students[:n])
    
    @staticmethod
    def get_failing_students(grades, passing=60):
        """Get students with average below passing"""
        averages = GradeProcessor.calculate_averages(grades)
        failing = filter(lambda x: x[1] < passing, averages.items())
        return dict(failing)
    
    @staticmethod
    def class_average(grades):
        """Calculate class average"""
        all_grades = reduce(lambda x, y: x + y, grades.values(), [])
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    @staticmethod
    def grade_distribution(grades):
        """Get grade distribution (A, B, C, D, F)"""
        averages = GradeProcessor.calculate_averages(grades)
        
        def get_letter(score):
            if score >= 90: return 'A'
            if score >= 80: return 'B'
            if score >= 70: return 'C'
            if score >= 60: return 'D'
            return 'F'
        
        letters = map(get_letter, averages.values())
        distribution = {}
        for letter in letters:
            distribution[letter] = distribution.get(letter, 0) + 1
        
        return distribution

# Sample data
grades = {
    "Alice": [85, 90, 88, 92],
    "Bob": [75, 80, 78, 82],
    "Charlie": [45, 50, 55, 60],
    "Diana": [95, 98, 92, 96],
    "Eve": [65, 70, 68, 72],
}

print("Student Averages:")
averages = GradeProcessor.calculate_averages(grades)
for name, avg in averages.items():
    print(f"  {name}: {avg:.2f}")

print(f"\nTop 3 Students: {GradeProcessor.get_top_students(grades)}")
print(f"Failing Students: {GradeProcessor.get_failing_students(grades)}")
print(f"Class Average: {GradeProcessor.class_average(grades):.2f}")
print(f"Grade Distribution: {GradeProcessor.grade_distribution(grades)}")
```

---

## Common Pitfalls

### Pitfall 1: Exhausting Iterators

```python
# ❌ WRONG - Iterator can only be used once
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]
print(list(squared))  # [] (exhausted!)

# ✅ CORRECT - Create new iterator each time
numbers = [1, 2, 3, 4, 5]
squared = lambda: map(lambda x: x ** 2, numbers)
print(list(squared()))  # [1, 4, 9, 16, 25]
print(list(squared()))  # [1, 4, 9, 16, 25]

# ✅ OR convert to list
squared_list = list(map(lambda x: x ** 2, numbers))
print(squared_list)  # [1, 4, 9, 16, 25]
print(squared_list)  # [1, 4, 9, 16, 25]
```

### Pitfall 2: Forgetting to Import reduce

```python
# ❌ WRONG - reduce is not built-in
# result = reduce(lambda x, y: x + y, [1, 2, 3])  # NameError!

# ✅ CORRECT - Import from functools
from functools import reduce
result = reduce(lambda x, y: x + y, [1, 2, 3])
```

### Pitfall 3: Lazy Evaluation Surprises

```python
# ❌ WRONG - Generator not evaluated yet
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
numbers.append(6)  # Modified after map
print(list(doubled))  # [2, 4, 6, 8, 10, 12] (includes 6!)

# ✅ CORRECT - Convert to list immediately if needed
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
numbers.append(6)
print(doubled)  # [2, 4, 6, 8, 10] (no change)
```

---

## Practice Exercises

### Beginner Level

1. **Square Numbers with Map**
   ```python
   # Use map to square list of numbers
   # Example: [1,2,3,4,5] -> [1,4,9,16,25]
   ```

2. **Filter Even Numbers**
   ```python
   # Use filter to keep only even numbers
   # Example: [1,2,3,4,5,6] -> [2,4,6]
   ```

3. **Sum with Reduce**
   ```python
   # Use reduce to sum list of numbers
   # Example: [1,2,3,4,5] -> 15
   ```

### Intermediate Level

4. **Zip to Create Dictionary**
   ```python
   # Use zip to combine two lists into dictionary
   # Example: keys=['a','b'], values=[1,2] -> {'a':1,'b':2}
   ```

5. **Filter and Map Pipeline**
   ```python
   # Filter numbers > 5, then square them
   # Example: [1,6,2,7,3,8] -> [36,49,64]
   ```

6. **Any/All Validators**
   ```python
   # Use any/all to validate list of conditions
   # Check if any number > 10, all numbers > 0
   ```

### Advanced Level

7. **Data Pipeline**
   ```python
   # Create pipeline: filter -> map -> reduce
   # Process list of dictionaries
   ```

8. **Matrix Transpose**
   ```python
   # Implement matrix transpose using zip
   # Example: [[1,2],[3,4]] -> [[1,3],[2,4]]
   ```

9. **Log Analyzer**
   ```python
   # Use map/filter/reduce to analyze log file
   # Count errors, warnings, info
   ```

---

## Quick Reference Card

```python
# map
map(func, iterable)                    # Apply function to all items
map(func, iter1, iter2)                # With multiple iterables

# filter
filter(func, iterable)                 # Keep items where func returns True
filter(None, iterable)                 # Remove falsy values

# reduce (from functools)
reduce(func, iterable)                 # Reduce to single value
reduce(func, iterable, initial)        # With initial value

# zip
zip(iter1, iter2, ...)                 # Combine iterables
zip(*zipped)                           # Unzip

# enumerate
enumerate(iterable)                    # Add counter starting at 0
enumerate(iterable, start)             # Start from custom value

# sorted
sorted(iterable)                       # Return new sorted list
sorted(iterable, key=func)             # Sort by key
sorted(iterable, reverse=True)         # Sort descending

# any/all
any(iterable)                          # True if any truthy
all(iterable)                          # True if all truthy

# itertools
from itertools import zip_longest, accumulate
zip_longest(*iter, fillvalue=None)     # Zip with fill value
accumulate(iterable)                   # Running sums
```

---

*Master functional tools to write concise, expressive, and efficient Python code! 🐍✨*

---
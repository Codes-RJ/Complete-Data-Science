# 📘 PYTHON DATA TYPES – COMPLETE MASTER GUIDE

## 📌 Table of Contents
1.  [Overview](#overview)
2.  [Why Data Types Matter](#why-data-types-matter)
3.  [Complete Type Hierarchy](#complete-type-hierarchy)
4.  [Quick Reference Table](#quick-reference-table)
5.  [Folder Structure](#folder-structure)
6.  [How to Use This Guide](#how-to-use-this-guide)
7.  [Prerequisites](#prerequisites)
8.  [Learning Path](#learning-path)
9.  [Real-World Applications](#real-world-applications)
10. [Common Pitfalls](#common-pitfalls)
11. [Performance Considerations](#performance-considerations)
12. [Best Practices](#best-practices)
13. [Next Steps](#next-steps)

---

## 📖 Overview

**Data types** are the foundation of Python programming. They define:
- What kind of data a variable can store
- What operations can be performed on that data
- How much memory is allocated
- How the data behaves in different contexts

Python is **dynamically typed** (no need to declare types explicitly) but **strongly typed** (types are enforced strictly).

### Key Characteristics of Python Data Types:

| Characteristic | Description | Example |
|----------------|-------------|---------|
| **Dynamic** | Type is determined at runtime | `x = 5` (int), `x = "hello"` (str) |
| **Strong** | No implicit type conversion between unrelated types | `"5" + 3` → TypeError |
| **Mutable** | Can be changed after creation | `list`, `dict`, `set` |
| **Immutable** | Cannot be changed after creation | `int`, `str`, `tuple` |

---

## 🎯 Why Data Types Matter

### 1. **Memory Efficiency**
```python
# Different types use different memory
import sys
print(f"int: {sys.getsizeof(1)} bytes")      # 28 bytes
print(f"float: {sys.getsizeof(1.0)} bytes")  # 24 bytes
print(f"str: {sys.getsizeof('a')} bytes")    # 50 bytes
```

### 2. **Performance Optimization**
```python
# Choosing the right type affects speed
import timeit

# Fast: Using int for counting
int_time = timeit.timeit('sum(range(1000))', number=10000)

# Slow: Using str for counting (don't do this!)
str_time = timeit.timeit('sum(map(int, map(str, range(1000))))', number=10000)

print(f"int: {int_time:.4f}s")
print(f"str: {str_time:.4f}s")
```

### 3. **Code Correctness**
```python
# Type errors catch bugs early
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# This will fail with TypeError
# calculate_average("123")  # Uncomment to see error

# But this works
print(calculate_average([1, 2, 3, 4, 5]))  # 3.0
```

### 4. **API Design & Documentation**
```python
# Type hints make code self-documenting
def process_user_data(
    user_id: int,
    name: str,
    scores: list[float],
    metadata: dict[str, any]
) -> dict[str, any]:
    """Clear what types each parameter expects"""
    return {"status": "success", "user_id": user_id}
```

---

## 🏗️ Complete Type Hierarchy

```
Python Data Types
│
├── Numeric Types
│   ├── int (Integer)
│   │   ├── Unlimited precision
│   │   ├── Supports binary, octal, hex
│   │   └── Bitwise operations
│   │
│   ├── float (Floating-point)
│   │   ├── IEEE 754 double precision
│   │   ├── Supports scientific notation
│   │   └── Special values: inf, -inf, nan
│   │
│   └── complex (Complex numbers)
│       ├── Real and imaginary parts
│       ├── Mathematical operations
│       └── Used in engineering & physics
│
├── Text Type
│   └── str (String)
│       ├── Immutable sequence of Unicode
│       ├── Extensive string methods
│       ├── Formatting capabilities
│       └── Slicing and indexing
│
├── Sequence Types
│   ├── list (Mutable sequence)
│   │   ├── Dynamic sizing
│   │   ├── Heterogeneous elements
│   │   └── Rich set of methods
│   │
│   ├── tuple (Immutable sequence)
│   │   ├── Fixed size
│   │   ├── Hashable (can be dict keys)
│   │   └── Memory efficient
│   │
│   └── range (Arithmetic progression)
│       ├── Memory efficient
│       ├── Used in loops
│       └── Supports slicing
│
├── Set Types
│   ├── set (Mutable set)
│   │   ├── Unordered unique elements
│   │   ├── Mathematical set operations
│   │   └── Fast membership testing
│   │
│   └── frozenset (Immutable set)
│       ├── Hashable
│       ├── Can be dict key
│       └── Thread-safe
│
├── Mapping Type
│   └── dict (Dictionary)
│       ├── Key-value pairs
│       ├── Hash-based lookup (O(1))
│       ├── Ordered (Python 3.7+)
│       └── Dynamic sizing
│
├── Boolean Type
│   └── bool (Boolean)
│       ├── True / False
│       ├── Subclass of int
│       └── Used in conditions
│
├── Binary Types
│   ├── bytes (Immutable bytes)
│   │   ├── Fixed-size binary data
│   │   ├── Used in I/O operations
│   │   └── Supports buffer protocol
│   │
│   ├── bytearray (Mutable bytes)
│   │   ├── Modify in-place
│   │   └── Memory efficient
│   │
│   └── memoryview (Buffer view)
│       ├── No copying of data
│       └── Efficient slicing
│
└── None Type
    └── NoneType
        ├── Single value: None
        ├── Represents absence of value
        └── Used as default return
```

---

## 📊 Quick Reference Table

| Type | Mutability | Ordered | Syntax Example | Use Case |
|------|------------|---------|----------------|----------|
| **int** | Immutable | N/A | `x = 42` | Counting, indexing |
| **float** | Immutable | N/A | `x = 3.14` | Measurements, science |
| **complex** | Immutable | N/A | `x = 3+4j` | Engineering, physics |
| **str** | Immutable | Yes | `x = "Hello"` | Text processing |
| **list** | Mutable | Yes | `x = [1,2,3]` | Dynamic collections |
| **tuple** | Immutable | Yes | `x = (1,2,3)` | Fixed collections |
| **range** | Immutable | Yes | `x = range(5)` | Loop iteration |
| **set** | Mutable | No | `x = {1,2,3}` | Unique elements |
| **frozenset** | Immutable | No | `x = frozenset([1,2,3])` | Hashable sets |
| **dict** | Mutable | Yes* | `x = {'a':1}` | Key-value mapping |
| **bool** | Immutable | N/A | `x = True` | Conditions |
| **bytes** | Immutable | Yes | `x = b'hello'` | Binary data |
| **bytearray** | Mutable | Yes | `x = bytearray(b'hello')` | Mutable binary |
| **NoneType** | Immutable | N/A | `x = None` | Null value |

*Ordered since Python 3.7 (insertion order preserved)

---

## 📁 Folder Structure

```
02_data_types/
│
├── README.md                          # ← YOU ARE HERE
│
├── 01_numeric_types/
│   ├── README.md
│   ├── 01_integers.py                 # Complete int guide
│   ├── 02_floats.py                   # Complete float guide
│   └── 03_complex_numbers.py          # Complete complex guide
│
├── 02_text_type/
│   ├── README.md
│   ├── strings.py                     # Complete str guide
│   └── string_methods.py              # All 40+ methods
│
├── 03_sequence_types/
│   ├── README.md
│   ├── 01_lists.py                    # Complete list guide
│   ├── 02_tuples.py                   # Complete tuple guide
│   └── 03_ranges.py                   # Complete range guide
│
├── 04_set_types/
│   ├── README.md
│   ├── 01_sets.py                     # Complete set guide
│   └── 02_frozensets.py               # Complete frozenset guide
│
├── 05_mapping_type/
│   ├── README.md
│   ├── dictionaries.py                # Complete dict guide
│   └── dict_methods.py                # All dict methods
│
├── 06_boolean_type/
│   ├── README.md
│   └── booleans.py                    # Complete bool guide
│
├── 07_binary_types/
│   ├── README.md
│   ├── 01_bytes.py                    # Complete bytes guide
│   ├── 02_bytearray.py                # Complete bytearray guide
│   └── 03_memoryview.py               # Complete memoryview guide
│
├── 08_none_type/
│   ├── README.md
│   └── none_type.py                   # Complete None guide
│
├── 09_type_conversion/
│   ├── README.md
│   ├── explicit_conversion.py         # int(), str(), list(), etc.
│   └── implicit_conversion.py         # Automatic conversion
│
├── 10_real_world_projects/
│   ├── banking_system.py              # Uses int, float, dict
│   ├── student_manager.py             # Uses list, dict, set
│   ├── inventory_system.py            # Uses dict, list, tuple
│   └── contact_book.py                # Uses dict, list, str
│
└── PRACTICE_EXERCISES.md              # Mixed practice sheet
```

---

## ⚠️ Common Pitfalls & Solutions

### Pitfall 1: Float Precision Issues
```python
# ❌ WRONG - Expecting exact decimal math
if 0.1 + 0.2 == 0.3:
    print("Equal")  # This won't print!

# ✅ CORRECT - Use tolerance
if abs((0.1 + 0.2) - 0.3) < 1e-10:
    print("Equal")  # This works

# ✅ BETTER - Use Decimal for currency
from decimal import Decimal
if Decimal('0.1') + Decimal('0.2') == Decimal('0.3'):
    print("Equal")  # Perfect!
```

### Pitfall 2: Mutable Default Arguments
```python
# ❌ WRONG - Mutable default persists
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  ← Unexpected!

# ✅ CORRECT - Use None as default
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [2]  ← Correct!
```

### Pitfall 3: Modifying List While Iterating
```python
# ❌ WRONG - Skips elements
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)  # [1, 3, 5] - Works here, but risky

# ✅ CORRECT - Iterate over copy
numbers = [1, 2, 3, 4, 5]
for i in numbers[:]:  # Slice copy
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)  # [1, 3, 5]

# ✅ BETTER - Use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [i for i in numbers if i % 2 != 0]
print(numbers)  # [1, 3, 5]
```

### Pitfall 4: Tuple Unpacking Errors
```python
# ❌ WRONG - Wrong number of elements
t = (1, 2)
# a, b, c = t  # ValueError!

# ✅ CORRECT - Match number of variables
a, b = t

# ✅ OR use * for remaining
a, *rest = (1, 2, 3, 4)
print(a, rest)  # 1 [2, 3, 4]
```

### Pitfall 5: Set vs Dictionary Syntax
```python
# ❌ WRONG - Empty set looks like dict
empty = {}  # This is a dict, not a set!

# ✅ CORRECT - Empty set
empty_set = set()

# ✅ CORRECT - Set with values
fruits = {'apple', 'banana', 'cherry'}  # Set (no colons)

# ✅ CORRECT - Dict with values
person = {'name': 'John', 'age': 30}    # Dict (has colons)
```

---

## ⚡ Performance Considerations

### Memory Usage Comparison
```python
import sys

data = [1, 2, 3, 4, 5]

print(f"list: {sys.getsizeof(data)} bytes")
print(f"tuple: {sys.getsizeof(tuple(data))} bytes")
print(f"set: {sys.getsizeof(set(data))} bytes")

# Typical output (Python 3.12):
# list: 104 bytes
# tuple: 80 bytes
# set: 216 bytes
```

### Speed Comparison
```python
import timeit

# List vs Set for membership testing
haystack_list = list(range(10000))
haystack_set = set(range(10000))

list_time = timeit.timeit('5000 in haystack_list', 
                          globals=globals(), number=10000)
set_time = timeit.timeit('5000 in haystack_set', 
                         globals=globals(), number=10000)

print(f"List membership: {list_time:.4f}s")
print(f"Set membership: {set_time:.4f}s")
# Set is MUCH faster for 'in' operations!
```

### When to Use Each Type

| Use Case | Best Type | Why |
|----------|-----------|-----|
| Need fast lookups | `set`, `dict` | O(1) average complexity |
| Need ordered data | `list`, `tuple` | Preserves insertion order |
| Data never changes | `tuple` | Immutable, hashable, memory efficient |
| Need unique elements | `set` | Automatically handles duplicates |
| Key-value mapping | `dict` | Fast lookups by key |
| Text manipulation | `str` | Rich string methods |
| Numeric calculations | `int`, `float` | Direct CPU operations |
| Binary data | `bytes`, `bytearray` | Efficient I/O |

---

## 💡 Best Practices

### 1. **Use Type Hints (Python 3.5+)**
```python
from typing import List, Dict, Optional

def process_data(
    user_id: int,
    names: List[str],
    config: Optional[Dict[str, any]] = None
) -> Dict[str, any]:
    """Clear type expectations"""
    return {"status": "success"}
```

### 2. **Check Types Explicitly**
```python
# Good - Check before operation
def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")
    return a + b

# Better - Let it fail naturally (EAFP)
def add_numbers(a, b):
    return a + b  # Will raise TypeError if wrong types
```

### 3. **Use Appropriate Types**
```python
# Bad - Using list for unique items
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

# Good - Using set
unique_items = set(items)
```

### 4. **Prefer Immutable When Possible**
```python
# Good - Immutable for constants
DAYS_OF_WEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

# Bad - Mutable for constants (risk of modification)
DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
```

### 5. **Use F-Strings for Formatting (Python 3.6+)**
```python
name = "Alice"
age = 30

# Old way
print("{} is {} years old".format(name, age))

# Better way (f-strings)
print(f"{name} is {age} years old")

# Even with expressions
print(f"{name.upper()} will be {age + 10} in 10 years")
```

---

*Happy Coding! 🐍✨*

---
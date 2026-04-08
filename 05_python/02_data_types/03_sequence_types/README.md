# 📊 SEQUENCE TYPES – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Three Sequence Types](#three-sequence-types)
3. [Quick Comparison](#quick-comparison)
4. [Common Operations](#common-operations)
5. [When to Use Each](#when-to-use-each)
6. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Sequence types** are used to store collections of items in a specific order. Python provides three built-in sequence types:

| Type | Description | Example | Mutability |
|------|-------------|---------|------------|
| **list** | Dynamic array, can change size | `[1, 2, 3]` | ✅ Mutable |
| **tuple** | Fixed-size, cannot change | `(1, 2, 3)` | ❌ Immutable |
| **range** | Arithmetic progression of integers | `range(5)` | ❌ Immutable |

**Key Characteristics:**
- ✅ Ordered (items have positions)
- ✅ Indexable (access by position)
- ✅ Iterable (can loop through)
- ✅ Support slicing (`[start:end:step]`)

```python
# Examples of sequences
fruits = ["apple", "banana", "cherry"]  # list
colors = ("red", "green", "blue")       # tuple
numbers = range(1, 10, 2)               # range (1,3,5,7,9)
```

---

## 🎯 Three Sequence Types

### 1. **list** – Mutable Sequence

Lists are **mutable** - you can add, remove, or modify items after creation.

```python
# Creating lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

# Modifying lists
fruits = ["apple", "banana"]
fruits.append("cherry")     # Add to end
fruits.insert(1, "orange")  # Insert at position
fruits.remove("banana")     # Remove item
fruits[0] = "grape"         # Change item

print(fruits)  # ['grape', 'orange', 'cherry']
```

### 2. **tuple** – Immutable Sequence

Tuples are **immutable** - once created, they cannot be changed.

```python
# Creating tuples
empty = ()
point = (10, 20)
single = (5,)           # Note: comma required
mixed = (1, "hello", 3.14)

# Accessing (same as lists)
print(point[0])    # 10
print(point[1])    # 20

# Cannot modify!
# point[0] = 15    # TypeError!

# Useful for fixed data
colors = ("red", "green", "blue")
rgb = (255, 128, 0)
```

### 3. **range** – Arithmetic Progression

Range generates numbers on demand (memory efficient).

```python
# Creating ranges
r1 = range(5)        # 0, 1, 2, 3, 4
r2 = range(2, 8)     # 2, 3, 4, 5, 6, 7
r3 = range(1, 10, 2) # 1, 3, 5, 7, 9
r4 = range(10, 0, -2) # 10, 8, 6, 4, 2

# Convert to list to see values
print(list(r1))  # [0, 1, 2, 3, 4]
print(list(r3))  # [1, 3, 5, 7, 9]

# Check membership
print(5 in range(10))    # True
print(10 in range(10))   # False
```

---

## 📊 Quick Comparison

| Feature | list | tuple | range |
|---------|------|-------|-------|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `range(5)` |
| **Mutable?** | ✅ Yes | ❌ No | ❌ No |
| **Ordered?** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Heterogeneous?** | ✅ Yes | ✅ Yes | ❌ No (ints only) |
| **Memory Usage** | High | Medium | Very Low |
| **Speed** | Moderate | Fast | Very Fast |
| **Use as dict key?** | ❌ No | ✅ Yes | ✅ Yes |
| **Methods** | Many (append, extend, etc.) | Few (count, index) | Few (count, index) |

### Memory Comparison

```python
import sys

my_list = list(range(1000))
my_tuple = tuple(range(1000))
my_range = range(1000)

print(f"list size:   {sys.getsizeof(my_list)} bytes")
print(f"tuple size:  {sys.getsizeof(my_tuple)} bytes")
print(f"range size:  {sys.getsizeof(my_range)} bytes")

# Typical output:
# list size:   8856 bytes
# tuple size:  8048 bytes
# range size:  48 bytes (always small!)
```

---

## 🔧 Common Operations

### Operations That Work on All Sequences

```python
# All sequences support these operations

# Indexing (access by position)
s = [10, 20, 30, 40, 50]
print(s[0])    # 10 (first)
print(s[-1])   # 50 (last)

# Slicing [start:end:step]
print(s[1:4])    # [20, 30, 40]
print(s[:3])     # [10, 20, 30]
print(s[2:])     # [30, 40, 50]
print(s[::2])    # [10, 30, 50]
print(s[::-1])   # [50, 40, 30, 20, 10] (reverse)

# Length
print(len(s))    # 5

# Membership
print(30 in s)   # True
print(100 in s)  # False

# Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)     # [1, 2, 3, 4]

# Repetition
print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2]

# Iteration
for item in [1, 2, 3]:
    print(item)    # 1, 2, 3

# Unpacking
x, y, z = [1, 2, 3]
print(x, y, z)     # 1 2 3

# Count occurrences
print([1, 2, 2, 3].count(2))  # 2

# Find index
print([10, 20, 30].index(20))  # 1
```

### List-Specific Operations (Mutable)

```python
fruits = ["apple", "banana"]

# Adding items
fruits.append("cherry")           # Add to end
fruits.insert(1, "orange")        # Insert at position
fruits.extend(["grape", "kiwi"])  # Add multiple

# Removing items
fruits.remove("banana")            # Remove by value
popped = fruits.pop()              # Remove last
popped = fruits.pop(1)             # Remove at index
fruits.clear()                     # Remove all

# Modifying
fruits[0] = "mango"                # Change by index
fruits[1:3] = ["pear", "plum"]     # Replace slice

# Sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort()                     # Sort in place
numbers.sort(reverse=True)         # Sort descending
numbers.reverse()                  # Reverse order

# Copying
new_list = fruits.copy()           # Shallow copy
```

### Tuple-Specific Operations (Immutable)

```python
# Tuples have fewer methods (only count and index)
t = (1, 2, 2, 3, 4)

print(t.count(2))    # 2 (count occurrences)
print(t.index(3))    # 3 (find first index)

# Tuple packing and unpacking
point = 10, 20       # Packing (parentheses optional)
x, y = point         # Unpacking

# Single element tuple (note the comma!)
single = (5,)        # Correct
not_tuple = (5)      # This is just an int!

# Named tuples (for self-documenting code)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)      # 10 20
```

### Range-Specific Operations

```python
# Creating ranges
r = range(10)              # 0 to 9
r = range(5, 10)           # 5 to 9
r = range(0, 10, 2)        # 0, 2, 4, 6, 8
r = range(10, 0, -2)       # 10, 8, 6, 4, 2

# Convert to list (to see values)
print(list(range(5)))      # [0, 1, 2, 3, 4]

# Check properties
print(r.start)   # 0 (start value)
print(r.stop)    # 10 (stop value)
print(r.step)    # 2 (step value)

# Membership is efficient (no need to generate all numbers)
print(5 in range(1000000))      # True (fast!)
print(1000000 in range(1000000)) # False (fast!)

# Length
print(len(range(0, 100, 5)))    # 20
```

---

## 📁 When to Use Each

| Use Case | Best Type | Why |
|----------|-----------|-----|
| Collection that changes size | `list` | Mutable, dynamic |
| Fixed data that never changes | `tuple` | Immutable, hashable, memory efficient |
| Dictionary keys | `tuple` | Hashable (lists aren't) |
| Function returning multiple values | `tuple` | Standard convention |
| Looping with numbers | `range` | Memory efficient, fast |
| Need to add/remove frequently | `list` | Dynamic sizing |
| Need to sort or reverse | `list` | Has sort/reverse methods |
| Configuration data | `tuple` | Prevents accidental changes |
| Large numeric sequences | `range` | Doesn't store all values |
| Multi-dimensional data | `list` of `list`s | Nested mutable structures |

### Real-World Examples

```python
# list - Dynamic collections
shopping_cart = []           # Start empty
shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.remove("apple")

# tuple - Fixed data
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
RGB_RED = (255, 0, 0)

# range - Looping
for i in range(100):         # Memory efficient
    print(i)

for i in range(1, 11):       # 1 to 10
    print(f"Table of {i}")

# Tuple as dict key
locations = {}
locations[(40.7128, -74.0060)] = "New York"  # Valid
# locations[[40.7128, -74.0060]] = "NY"     # TypeError!
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `01_lists.md` | Complete list guide with all methods |
| `02_tuples.md` | Complete tuple guide with all methods |
| `03_ranges.md` | Complete range guide with all methods |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 🚀 Quick Start

```bash
# Open the detailed guides
cat 01_lists.md
cat 02_tuples.md
cat 03_ranges.md
```

---

## 🔄 Conversion Between Types

```python
# List ↔ Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)      # (1, 2, 3)
back_to_list = list(my_tuple)  # [1, 2, 3]

# Range → List (to see values)
my_range = range(5)
my_list = list(my_range)       # [0, 1, 2, 3, 4]

# List → Range (only if evenly spaced)
# Not directly possible, but you can create new range
if len(my_list) > 1:
    step = my_list[1] - my_list[0]
    my_range = range(my_list[0], my_list[-1] + 1, step)
```

---

## 📚 Next Steps

After understanding sequence basics:
1. Open `01_lists.md` for detailed list methods
2. Open `02_tuples.md` for tuple patterns
3. Open `03_ranges.md` for efficient looping
4. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Strings** – Sequence of characters
- **Dictionaries** – Key-value mappings
- **Sets** – Unordered unique collections
- **Arrays** – For numeric arrays (array module)

---

## 💡 Quick Tips

```python
# Create empty list properly
my_list = []           # ✅ Correct
my_list = list()       # ✅ Also correct

# Create empty tuple
my_tuple = ()          # ✅ Correct
my_tuple = tuple()     # ✅ Also correct

# Single element tuple (don't forget comma!)
single = (5,)          # ✅ Tuple with one element
not_tuple = (5)        # ❌ This is an int!

# Copy lists properly
new = old[:]           # ✅ Slice copy
new = old.copy()       # ✅ Copy method
new = old              # ❌ This is a reference!

# Check if list is empty
if not my_list:        # ✅ Pythonic
    print("Empty")

# Iterate with index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")
```

---

*Master sequences to handle collections of data efficiently! 🐍✨*
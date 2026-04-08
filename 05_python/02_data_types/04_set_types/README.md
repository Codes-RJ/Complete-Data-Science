# 🔢 SET TYPES – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Two Set Types](#two-set-types)
3. [Quick Comparison](#quick-comparison)
4. [Common Operations](#common-operations)
5. [Set Operations (Mathematics)](#set-operations-mathematics)
6. [When to Use Each](#when-to-use-each)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Set types** are unordered collections of unique elements. They are optimized for membership testing and mathematical set operations.

| Type | Description | Example | Mutability |
|------|-------------|---------|------------|
| **set** | Mutable, unordered, unique elements | `{1, 2, 3}` | ✅ Mutable |
| **frozenset** | Immutable version of set | `frozenset([1, 2, 3])` | ❌ Immutable |

**Key Characteristics:**
- ✅ Unordered (no index positions)
- ✅ Unique elements (no duplicates)
- ✅ Fast membership testing (O(1))
- ✅ Support mathematical operations (union, intersection, etc.)
- ❌ Cannot contain mutable elements (lists, dicts, sets)

```python
# Examples of sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}
empty = set()  # NOT {} (that's a dict!)

# Frozenset (immutable)
immutable = frozenset([1, 2, 3])
```

---

## 🎯 Two Set Types

### 1. **set** – Mutable Set

Sets are **mutable** - you can add, remove, or modify elements.

```python
# Creating sets
empty = set()                    # Empty set (not {})
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 3])       # From list
from_string = set("hello")       # {'h', 'e', 'l', 'o'}

# Modifying sets
fruits = {"apple", "banana"}
fruits.add("cherry")             # Add element
fruits.remove("banana")          # Remove element (raises error if missing)
fruits.discard("grape")          # Remove if exists (no error)
popped = fruits.pop()            # Remove and return arbitrary element
fruits.clear()                   # Remove all elements

print(fruits)  # {'apple', 'cherry'}
```

### 2. **frozenset** – Immutable Set

Frozensets are **immutable** - once created, they cannot be changed.

```python
# Creating frozensets
empty = frozenset()
numbers = frozenset([1, 2, 3, 4, 5])
fruits = frozenset({"apple", "banana", "cherry"})

# Cannot modify!
# fruits.add("date")     # AttributeError!
# fruits.remove("apple") # AttributeError!

# Can be used as dictionary keys
locations = {
    frozenset([40.7128, -74.0060]): "New York",
    frozenset([34.0522, -118.2437]): "Los Angeles"
}

print(locations[frozenset([40.7128, -74.0060])])  # "New York"
```

---

## 📊 Quick Comparison

| Feature | set | frozenset |
|---------|-----|-----------|
| **Syntax** | `{1, 2, 3}` | `frozenset([1, 2, 3])` |
| **Mutable?** | ✅ Yes | ❌ No |
| **Ordered?** | ❌ No | ❌ No |
| **Hashable?** | ❌ No | ✅ Yes |
| **Use as dict key?** | ❌ No | ✅ Yes |
| **Empty creation** | `set()` | `frozenset()` |
| **Memory Usage** | Moderate | Slightly less |
| **Methods** | Many (add, remove, etc.) | Few (union, intersection, etc.) |

### Memory Comparison

```python
import sys

my_set = set(range(1000))
my_frozenset = frozenset(range(1000))

print(f"set size: {sys.getsizeof(my_set)} bytes")
print(f"frozenset size: {sys.getsizeof(my_frozenset)} bytes")

# Typical output:
# set size: 16448 bytes
# frozenset size: 16448 bytes (similar)
```

---

## 🔧 Common Operations

### Operations That Work on Both Set Types

```python
s = {1, 2, 3, 4, 5}

# Length
print(len(s))           # 5

# Membership (fast O(1))
print(3 in s)           # True
print(10 in s)          # False

# Iteration (order not guaranteed)
for item in s:
    print(item)         # 1,2,3,4,5 (in any order)

# Copy
s2 = s.copy()           # Shallow copy

# Check subset/superset
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True
print(a.isdisjoint({5,6})) # True (no common elements)

# Convert to other types
print(list(s))          # [1, 2, 3, 4, 5]
print(tuple(s))         # (1, 2, 3, 4, 5)
```

### Set-Specific Operations (Mutable)

```python
s = {1, 2, 3}

# Adding elements
s.add(4)                # {1, 2, 3, 4}
s.update([5, 6, 7])     # {1, 2, 3, 4, 5, 6, 7}

# Removing elements
s.remove(3)             # {1, 2, 4, 5, 6, 7} (error if missing)
s.discard(10)           # No error if missing
popped = s.pop()        # Removes arbitrary element
s.clear()               # Empty set

# Set operations (in-place)
s = {1, 2, 3}
t = {3, 4, 5}
s.update(t)             # Union: {1, 2, 3, 4, 5}
s.intersection_update(t) # Intersection: {3}
s.difference_update(t)   # Difference: {1, 2}
s.symmetric_difference_update(t) # Symmetric difference: {1, 2, 4, 5}
```

---

## 🔢 Set Operations (Mathematics)

### Mathematical Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all elements from both)
print(a | b)                    # {1, 2, 3, 4, 5, 6}
print(a.union(b))               # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(a & b)                    # {3, 4}
print(a.intersection(b))        # {3, 4}

# Difference (elements in a but not in b)
print(a - b)                    # {1, 2}
print(a.difference(b))          # {1, 2}

# Symmetric Difference (elements in either, but not both)
print(a ^ b)                    # {1, 2, 5, 6}
print(a.symmetric_difference(b)) # {1, 2, 5, 6}
```

### Visual Examples

```python
# Union - combine sets
fruits = {"apple", "banana"}
citrus = {"orange", "lemon"}
all_fruits = fruits | citrus
print(all_fruits)  # {'apple', 'banana', 'orange', 'lemon'}

# Intersection - find common elements
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common = set1 & set2
print(common)  # {3, 4}

# Difference - find unique elements
python = {"Python", "Java", "C++", "JavaScript"}
java = {"Java", "Kotlin", "Scala"}
only_python = python - java
print(only_python)  # {'Python', 'C++', 'JavaScript'}

# Symmetric difference - find elements not in both
a = {1, 2, 3}
b = {3, 4, 5}
exclusive = a ^ b
print(exclusive)  # {1, 2, 4, 5}
```

---

## 📁 When to Use Each

| Use Case | Best Type | Why |
|----------|-----------|-----|
| Remove duplicates | `set` | Automatically handles duplicates |
| Fast membership testing | `set` | O(1) lookup |
| Mathematical set operations | `set` | Union, intersection, etc. |
| Dictionary keys | `frozenset` | Hashable (set is not) |
| Immutable configuration | `frozenset` | Cannot be changed accidentally |
| Need to add/remove elements | `set` | Mutable |
| Set of sets | `frozenset` | Sets can't contain mutable sets |

### Real-World Examples

```python
# Remove duplicates from list
numbers = [1, 2, 3, 2, 4, 3, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5]

# Find common friends
user1_friends = {"Alice", "Bob", "Charlie"}
user2_friends = {"Bob", "David", "Eve"}
common_friends = user1_friends & user2_friends
print(common_friends)  # {'Bob'}

# Find unique visitors
visitors = []
visitors.append("user1")
visitors.append("user2")
visitors.append("user1")
unique_visitors = set(visitors)
print(unique_visitors)  # {'user1', 'user2'}

# Check if list has duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 4]))     # False
print(has_duplicates([1, 2, 3, 2]))     # True

# Set as dictionary key (using frozenset)
cache = {}
cache[frozenset([1, 2, 3])] = "Result for {1,2,3}"
print(cache[frozenset([1, 2, 3])])  # "Result for {1,2,3}"
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `01_sets.md` | Complete set guide with all methods |
| `02_frozensets.md` | Complete frozenset guide |

---

## 🚀 Quick Start

```bash
# Open the detailed guides
cat 01_sets.md
cat 02_frozensets.md
```

---

## 🔄 Conversion Between Types

```python
# Set ↔ Frozenset
my_set = {1, 2, 3}
my_frozenset = frozenset(my_set)     # frozenset({1, 2, 3})
back_to_set = set(my_frozenset)      # {1, 2, 3}

# List ↔ Set (removes duplicates)
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)                # {1, 2, 3}
back_to_list = list(my_set)          # [1, 2, 3]

# String ↔ Set (unique characters)
my_string = "hello"
char_set = set(my_string)            # {'h', 'e', 'l', 'o'}
back_to_string = ''.join(char_set)   # "helo" (order not preserved)
```

---

## 💡 Quick Tips

```python
# Create empty set properly
my_set = set()      # ✅ Correct
my_set = {}         # ❌ This is a dict!

# Remove duplicates while preserving order (Python 3.7+)
def unique_preserve_order(lst):
    return list(dict.fromkeys(lst))

print(unique_preserve_order([1, 2, 3, 2, 4, 3, 5]))  # [1, 2, 3, 4, 5]

# Check subset efficiently
if {1, 2}.issubset({1, 2, 3}):
    print("Is subset")  # This prints

# Find common elements between multiple sets
sets = [{1, 2}, {2, 3}, {2, 4}]
common = set.intersection(*sets)
print(common)  # {2}

# Check if two lists have any common elements
def have_common(list1, list2):
    return not set(list1).isdisjoint(set(list2))

print(have_common([1, 2, 3], [3, 4, 5]))  # True
print(have_common([1, 2, 3], [4, 5, 6]))  # False
```

---

## 📚 Next Steps

After understanding set basics:
1. Open `01_sets.md` for detailed set methods
2. Open `02_frozensets.md` for immutable sets
3. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Lists** – Ordered, allows duplicates
- **Dictionaries** – Key-value mappings
- **Tuples** – Immutable sequences

---

*Master sets for efficient unique element storage and mathematical operations! 🐍✨*
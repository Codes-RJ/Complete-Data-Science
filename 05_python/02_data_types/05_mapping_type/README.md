# 📖 MAPPING TYPE (dict) – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Dictionaries?](#what-are-dictionaries)
3. [Quick Reference](#quick-reference)
4. [Common Operations](#common-operations)
5. [When to Use Dictionaries](#when-to-use-dictionaries)
6. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Dictionaries** are mutable, ordered collections of key-value pairs. They are one of the most powerful and commonly used data structures in Python.

| Feature | Description | Example |
|---------|-------------|---------|
| **Type** | `dict` | `{"name": "Alice", "age": 30}` |
| **Mutable?** | ✅ Yes | Can add, remove, modify |
| **Ordered?** | ✅ Yes | Maintains insertion order (Python 3.7+) |
| **Keys** | Immutable types | `str`, `int`, `tuple`, etc. |
| **Values** | Any type | Any Python object |
| **Lookup Speed** | O(1) average | Very fast |

```python
# Examples of dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
scores = {"math": 95, "science": 87, "history": 92}
nested = {"user": {"name": "Bob", "email": "bob@example.com"}}
```

**Key Characteristics:**
- ✅ Key-value pairs for fast lookups
- ✅ Keys must be immutable (strings, numbers, tuples)
- ✅ Values can be any type (including other dicts)
- ✅ Maintain insertion order (Python 3.7+)
- ✅ Dynamic size (grow and shrink as needed)
- ✅ Extremely fast membership testing (O(1))

---

## 📖 What are Dictionaries?

Dictionaries store data in **key-value pairs**, where each key is unique and maps to a value.

```python
# Basic dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Accessing values
print(student["name"])     # "John Doe"
print(student["age"])      # 20

# Modifying values
student["gpa"] = 3.9
student["year"] = "Junior"  # Adding new key-value pair

# Different value types
mixed = {
    "name": "Alice",
    "age": 25,
    "grades": [85, 90, 88],
    "address": {"city": "NYC", "zip": 10001},
    "is_active": True
}
```

---

## 📊 Quick Reference

### Dictionary Creation

```python
# Empty dictionary
empty = {}
empty = dict()

# With values
person = {"name": "Alice", "age": 30}
person = dict(name="Alice", age=30)
person = dict([("name", "Alice"), ("age", 30)])

# From keys with default values
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)  # {"a": 0, "b": 0, "c": 0}
```

### Accessing Values

```python
person = {"name": "Alice", "age": 30}

# Direct access (raises KeyError if missing)
print(person["name"])      # "Alice"

# Using get() (returns None or default if missing)
print(person.get("city"))          # None
print(person.get("city", "NYC"))   # "NYC"

# Using setdefault() (returns value, sets default if missing)
city = person.setdefault("city", "Unknown")  # Returns "Unknown", adds to dict
```

### Adding and Modifying

```python
person = {"name": "Alice"}

# Add or update
person["age"] = 30          # Add new key-value
person["name"] = "Bob"      # Update existing

# Update with another dictionary
person.update({"city": "NYC", "age": 31})

# Update with key-value pairs
person.update(phone="123-4567", email="bob@example.com")
```

### Removing Items

```python
person = {"name": "Alice", "age": 30, "city": "NYC", "job": "Engineer"}

# pop() - remove and return value (raises KeyError if missing)
age = person.pop("age")           # Returns 30

# popitem() - remove and return last inserted item (LIFO)
key, value = person.popitem()     # Returns ("job", "Engineer")

# del statement
del person["city"]                 # Removes key

# clear() - remove all items
person.clear()                     # {}
```

### Dictionary Views

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Keys view
keys = person.keys()        # dict_keys(['name', 'age', 'city'])

# Values view
values = person.values()    # dict_values(['Alice', 30, 'NYC'])

# Items view (key-value pairs)
items = person.items()      # dict_items([('name', 'Alice'), ('age', 30), ('city', 'NYC')])

# Views are dynamic - they update when dict changes
person["job"] = "Engineer"
print(keys)    # dict_keys(['name', 'age', 'city', 'job'])
```

---

## 🔧 Common Operations

### Looping Through Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Loop through keys
for key in person:
    print(f"{key}: {person[key]}")

# Loop through keys (explicit)
for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs (recommended)
for key, value in person.items():
    print(f"{key}: {value}")
```

### Membership Testing

```python
person = {"name": "Alice", "age": 30}

# Check if key exists (fast O(1))
print("name" in person)     # True
print("city" in person)     # False

# Check if value exists (slower O(n))
print("Alice" in person.values())   # True
print(25 in person.values())        # False
```

### Dictionary Length

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(len(person))  # 3
```

### Copying Dictionaries

```python
original = {"a": 1, "b": 2, "c": {"d": 3}}

# Shallow copy
shallow = original.copy()
shallow = dict(original)
shallow = original | {}  # Python 3.9+

# Deep copy (for nested structures)
import copy
deep = copy.deepcopy(original)
```

### Dictionary Comprehension

```python
# Squares as values
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Merging Dictionaries (Python 3.9+)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using | operator (creates new dict)
merged = dict1 | dict2
print(merged)  # {"a": 1, "b": 2, "c": 3, "d": 4}

# Using |= operator (updates dict1)
dict1 |= dict2
print(dict1)   # {"a": 1, "b": 2, "c": 3, "d": 4}

# For older Python versions
merged = {**dict1, **dict2}
```

---

## 📁 When to Use Dictionaries

| Use Case | Example | Why |
|----------|---------|-----|
| **Lookup tables** | `phonebook = {"Alice": "555-1234"}` | Fast O(1) lookups |
| **Caching** | `cache = {"url": "response"}` | Key-based storage |
| **Configuration** | `config = {"debug": True, "port": 8080}` | Key-value settings |
| **Counting frequencies** | `counts = {"a": 3, "b": 2}` | Efficient counting |
| **JSON data** | `data = {"name": "John", "age": 30}` | Natural representation |
| **Mapping IDs to objects** | `users = {1: user1, 2: user2}` | ID-based lookup |
| **Grouping data** | `groups = {"A": [1,2], "B": [3,4]}` | Categorization |

### Real-World Examples

```python
# Phone book (name -> number)
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
print(phonebook["Alice"])  # "555-1234"

# Configuration settings
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "database": {
        "name": "myapp_db",
        "user": "admin",
        "password": "secret"
    }
}

# Counting frequencies
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Grouping items
students = [
    ("Alice", "Math"), ("Bob", "Science"), ("Charlie", "Math"),
    ("David", "Science"), ("Eve", "Math")
]
by_subject = {}
for name, subject in students:
    if subject not in by_subject:
        by_subject[subject] = []
    by_subject[subject].append(name)
print(by_subject)  # {'Math': ['Alice', 'Charlie', 'Eve'], 'Science': ['Bob', 'David']}
```

---

## ⚡ Performance Characteristics

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Access `d[key]` | O(1) average | Very fast |
| Assignment `d[key] = value` | O(1) average | Very fast |
| Deletion `del d[key]` | O(1) average | Very fast |
| Membership `key in d` | O(1) average | Very fast |
| Iteration | O(n) | Linear time |
| Copy | O(n) | Creates new dict |
| `dict()` constructor | O(n) | From iterable |

```python
import timeit

# Dictionary lookup is extremely fast
d = {i: i**2 for i in range(10000)}

lookup_time = timeit.timeit('d[5000]', globals=globals(), number=1000000)
print(f"Dictionary lookup: {lookup_time:.4f}s")

# Much faster than list search
lst = list(range(10000))
list_time = timeit.timeit('5000 in lst', globals=globals(), number=10000)
dict_time = timeit.timeit('5000 in d', globals=globals(), number=10000)
print(f"List membership: {list_time:.4f}s")
print(f"Dict membership: {dict_time:.4f}s")
print(f"Dict is {list_time/dict_time:.0f}x faster!")
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `dictionaries.md` | Complete dictionary guide with all methods |
| `dict_methods.md` | All dictionary methods with examples |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 🚀 Quick Start

```bash
# Open the detailed guides
cat dictionaries.md
cat dict_methods.md
```

---

## 🔄 Type Conversion

```python
# List of tuples to dict
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Two lists to dict
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Dict to list of tuples
items = list(d.items())
print(items)  # [('a', 1), ('b', 2), ('c', 3)]

# Dict to JSON string
import json
json_str = json.dumps(d)
print(json_str)  # '{"a": 1, "b": 2, "c": 3}'
```

---

## 💡 Quick Tips

```python
# Use get() to avoid KeyError
value = d.get("missing_key", "default")

# Use setdefault() for default values
counts = {}
counts["a"] = counts.setdefault("a", 0) + 1

# Use defaultdict for automatic defaults
from collections import defaultdict
counts = defaultdict(int)
counts["a"] += 1  # No KeyError!

# Use Counter for counting frequencies
from collections import Counter
text = "hello world"
freq = Counter(text)
print(freq)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Use OrderedDict if order matters (Python <3.7)
from collections import OrderedDict

# Use ChainMap for multiple dictionaries
from collections import ChainMap
defaults = {"a": 1, "b": 2}
overrides = {"b": 3}
merged = ChainMap(overrides, defaults)
print(merged["b"])  # 3 (from overrides)
print(merged["a"])  # 1 (from defaults)
```

---

## 📚 Next Steps

After understanding dictionary basics:
1. Open `dictionaries.md` for detailed methods
2. Open `dict_methods.md` for all methods reference
3. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Lists** – Ordered sequences
- **Sets** – Unique unordered collections
- **JSON** – Data interchange format
- **DefaultDict** – Auto-default dictionaries
- **Counter** – Counting dictionary

---

*Master dictionaries for fast, flexible key-value storage! 🐍✨*

---
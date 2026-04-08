# 📚 DICTIONARY METHODS – COMPLETE REFERENCE

## 📌 Table of Contents
1. [Method Categories](#method-categories)
2. [All Dictionary Methods](#all-dictionary-methods)
3. [Method Details with Examples](#method-details-with-examples)
4. [Comparison Chart](#comparison-chart)
5. [Quick Reference Table](#quick-reference-table)

---

## 📖 Method Categories

| Category | Methods |
|----------|---------|
| **Access** | `get()`, `setdefault()`, `[]` |
| **Add/Update** | `update()`, `|=` (3.9+), `setdefault()` |
| **Remove** | `pop()`, `popitem()`, `clear()`, `del` |
| **Views** | `keys()`, `values()`, `items()` |
| **Copy** | `copy()` |
| **Creation** | `fromkeys()` |
| **Other** | `len()`, `in`, `iter()` |

---

## 🔧 All Dictionary Methods

### `clear()`
Removes all items from the dictionary.

```python
d = {"a": 1, "b": 2, "c": 3}
d.clear()
print(d)  # {}

# Real use: Reset dictionary for reuse
cache = {"url1": "data1", "url2": "data2"}
# Process cache...
cache.clear()  # Ready for new data
```

### `copy()`
Returns a shallow copy of the dictionary.

```python
original = {"a": 1, "b": {"c": 2}}
shallow = original.copy()

print(shallow)  # {'a': 1, 'b': {'c': 2}}
print(original is shallow)  # False (different objects)

# Nested objects are shared
shallow["b"]["c"] = 99
print(original)  # {'a': 1, 'b': {'c': 99}} (changed!)

# Alternative copies
copy1 = original.copy()
copy2 = dict(original)
copy3 = original | {}  # Python 3.9+

# Deep copy for nested structures
import copy
deep = copy.deepcopy(original)
```

### `fromkeys(iterable, value=None)`
Creates a new dictionary from iterable with specified value.

```python
# Create with default value None
keys = ["a", "b", "c"]
d = dict.fromkeys(keys)
print(d)  # {'a': None, 'b': None, 'c': None}

# Create with custom default value
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}

# With different iterable types
print(dict.fromkeys("abc", 1))     # {'a': 1, 'b': 1, 'c': 1}
print(dict.fromkeys(range(3), 0))  # {0: 0, 1: 0, 2: 0}

# Real use: Initialize counters
counters = dict.fromkeys(["apple", "banana", "cherry"], 0)
counters["apple"] += 1
print(counters)  # {'apple': 1, 'banana': 0, 'cherry': 0}

# Warning: Same mutable object shared
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)
print(d)  # {'a': [1], 'b': [1]} (both share same list!)

# Fix: Use comprehension for mutable defaults
d = {k: [] for k in ["a", "b"]}
d["a"].append(1)
print(d)  # {'a': [1], 'b': []}
```

### `get(key[, default])`
Returns value for key if exists, else default (None if not specified).

```python
person = {"name": "Alice", "age": 30}

# Get existing key
print(person.get("name"))      # "Alice"
print(person.get("age"))       # 30

# Get missing key (returns None, no error)
print(person.get("city"))      # None
print(person.get("country"))   # None

# Get with custom default
print(person.get("city", "Unknown"))     # "Unknown"
print(person.get("country", "USA"))      # "USA"

# Real use: Safe counting
counts = {}
counts["apple"] = counts.get("apple", 0) + 1
counts["apple"] = counts.get("apple", 0) + 1
counts["banana"] = counts.get("banana", 0) + 1
print(counts)  # {'apple': 2, 'banana': 1}

# Real use: Safe nested access
data = {"user": {"name": "Alice"}}
city = data.get("user", {}).get("address", {}).get("city", "Unknown")
print(city)  # "Unknown"
```

### `items()`
Returns a view of key-value pairs (tuples).

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Get items view
items = person.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'NYC')])
print(type(items))  # <class 'dict_items'>

# Iterate through items (recommended)
for key, value in items:
    print(f"{key}: {value}")

# Convert to list
items_list = list(items)
print(items_list)  # [('name', 'Alice'), ('age', 30), ('city', 'NYC')]

# View is dynamic
person["job"] = "Engineer"
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'NYC'), ('job', 'Engineer')])

# Membership testing
print(("name", "Alice") in items)   # True
print(("name", "Bob") in items)     # False

# Real use: Unpacking in loops
for key, value in person.items():
    print(f"{key.upper()}: {value}")

# Real use: Creating list of tuples for JSON
import json
json_data = json.dumps(list(person.items()))
print(json_data)  # '[["name", "Alice"], ["age", 30], ...]'
```

### `keys()`
Returns a view of dictionary keys.

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Get keys view
keys = person.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])
print(type(keys))  # <class 'dict_keys'>

# Iterate through keys
for key in keys:
    print(key)  # name, age, city

# Convert to list
key_list = list(keys)
print(key_list)  # ['name', 'age', 'city']

# View is dynamic
person["job"] = "Engineer"
print(keys)  # dict_keys(['name', 'age', 'city', 'job'])

# Membership testing (fast O(1))
print("name" in keys)     # True
print("country" in keys)  # False

# Real use: Check required keys
required_keys = {"name", "age", "city"}
if required_keys.issubset(person.keys()):
    print("All required fields present")

# Real use: Iterate sorted keys
for key in sorted(person.keys()):
    print(f"{key}: {person[key]}")
```

### `pop(key[, default])`
Removes and returns value for specified key. Raises KeyError if key missing and no default.

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Remove existing key
age = person.pop("age")
print(age)      # 30
print(person)   # {'name': 'Alice', 'city': 'NYC'}

# Remove with default (no error if missing)
country = person.pop("country", "Not found")
print(country)  # "Not found"
print(person)   # {'name': 'Alice', 'city': 'NYC'}

# Remove without default (raises error if missing)
try:
    person.pop("missing")
except KeyError:
    print("Key not found!")

# Real use: Process and remove from dict
queue = {"task1": "pending", "task2": "pending", "task3": "completed"}
while queue:
    key, value = queue.popitem()  # Alternative: pop arbitrary
    print(f"Processing {key}: {value}")

# Real use: Remove and get value safely
def pop_safely(d, key, default=None):
    return d.pop(key, default)

counts = {"a": 1, "b": 2}
value = pop_safely(counts, "c", 0)
print(value)  # 0
print(counts)  # {'a': 1, 'b': 2}
```

### `popitem()`
Removes and returns the last inserted key-value pair (LIFO). Raises KeyError if empty.

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Remove last inserted item
key, value = person.popitem()
print(f"Removed: {key}={value}")  # Removed: city=NYC
print(person)  # {'name': 'Alice', 'age': 30}

# Remove another
key, value = person.popitem()
print(f"Removed: {key}={value}")  # Removed: age=30
print(person)  # {'name': 'Alice'}

# KeyError if empty
empty = {}
try:
    empty.popitem()
except KeyError:
    print("Cannot pop from empty dict")

# Real use: LIFO processing (stack)
stack = {"task1": "data1", "task2": "data2", "task3": "data3"}
while stack:
    key, value = stack.popitem()
    print(f"Processing {key}: {value}")
# Output order: task3, task2, task1

# Real use: Process in reverse insertion order
history = {"step1": "action1", "step2": "action2", "step3": "action3"}
# Undo operations in reverse order
while history:
    step, action = history.popitem()
    print(f"Undoing {step}: {action}")
```

### `setdefault(key[, default])`
Returns value if key exists, otherwise sets key to default and returns default.

```python
person = {"name": "Alice", "age": 30}

# Key exists - returns value, doesn't change dict
name = person.setdefault("name", "Unknown")
print(name)    # "Alice"
print(person)  # {'name': 'Alice', 'age': 30}

# Key missing - sets default and returns it
city = person.setdefault("city", "New York")
print(city)    # "New York"
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Another missing key
country = person.setdefault("country", "USA")
print(country)  # "USA"
print(person)   # {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Real use: Grouping items
groups = {}
items = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]

for category, item in items:
    groups.setdefault(category, []).append(item)

print(groups)  # {'fruit': ['apple', 'banana'], 'veg': ['carrot']}

# Real use: Counting with defaultdict alternative
counts = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    counts[word] = counts.setdefault(word, 0) + 1
print(counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Real use: Building nested dictionaries
nested = {}
nested.setdefault("user", {}).setdefault("profile", {}).setdefault("name", "Anonymous")
print(nested)  # {'user': {'profile': {'name': 'Anonymous'}}}
```

### `update([other])`
Updates dictionary with key-value pairs from another dictionary or iterable.

```python
person = {"name": "Alice", "age": 30}

# Update with another dictionary
updates = {"age": 31, "city": "New York"}
person.update(updates)
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Update with list of tuples
person.update([("job", "Engineer"), ("salary", 75000)])
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer', 'salary': 75000}

# Update with keyword arguments
person.update(country="USA", phone="555-1234")
print(person)  # {... 'country': 'USA', 'phone': '555-1234'}

# Update with zip of two lists
keys = ["department", "manager"]
values = ["IT", "Bob"]
person.update(zip(keys, values))
print(person)  # {... 'department': 'IT', 'manager': 'Bob'}

# Real use: Merging configurations
default_config = {"host": "localhost", "port": 8080, "debug": False}
user_config = {"port": 9090, "debug": True}
default_config.update(user_config)
print(default_config)  # {'host': 'localhost', 'port': 9090, 'debug': True}

# Real use: Updating from user input
settings = {"theme": "dark", "language": "en"}
user_prefs = {"theme": "light"}  # User changed theme
settings.update(user_prefs)
print(settings)  # {'theme': 'light', 'language': 'en'}
```

### `values()`
Returns a view of dictionary values.

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Get values view
values = person.values()
print(values)  # dict_values(['Alice', 30, 'NYC'])
print(type(values))  # <class 'dict_values'>

# Iterate through values
for value in values:
    print(value)  # Alice, 30, NYC

# Convert to list
value_list = list(values)
print(value_list)  # ['Alice', 30, 'NYC']

# View is dynamic
person["job"] = "Engineer"
print(values)  # dict_values(['Alice', 30, 'NYC', 'Engineer'])

# Membership testing (slower than keys)
print("Alice" in values)  # True
print("Bob" in values)    # False

# Real use: Sum all numeric values
scores = {"math": 95, "science": 87, "history": 92}
total = sum(scores.values())
average = total / len(scores)
print(f"Total: {total}, Average: {average:.1f}")  # Total: 274, Average: 91.3

# Real use: Find maximum value
max_score = max(scores.values())
print(f"Highest score: {max_score}")  # Highest score: 95

# Real use: Count occurrences of values
counts = {}
for value in scores.values():
    counts[value] = counts.get(value, 0) + 1
print(counts)  # {95: 1, 87: 1, 92: 1}
```

### `|` and `|=` Operators (Python 3.9+)
Merge dictionaries using union operator.

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merge into new dictionary (|)
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1)   # {'a': 1, 'b': 2} (unchanged)

# Update in place (|=)
dict1 |= dict2
print(dict1)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# With overlapping keys (later overwrites earlier)
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
print(d1 | d2)  # {'a': 1, 'b': 99, 'c': 3}

# Merge multiple dictionaries
d3 = {"d": 4, "e": 5}
merged = d1 | d2 | d3
print(merged)  # {'a': 1, 'b': 99, 'c': 3, 'd': 4, 'e': 5}

# Real use: Combining configurations
default = {"theme": "dark", "language": "en"}
user = {"theme": "light"}
settings = default | user
print(settings)  # {'theme': 'light', 'language': 'en'}

# Real use: Creating new dict from multiple sources
sources = [{"a": 1}, {"b": 2}, {"c": 3}]
combined = {}
for source in sources:
    combined |= source
print(combined)  # {'a': 1, 'b': 2, 'c': 3}
```

---

## 📊 Comparison Chart

### Method Behavior Comparison

| Method | Returns | Modifies Dict | KeyError | Use Case |
|--------|---------|---------------|----------|----------|
| `d[key]` | Value | No | Yes | Direct access when key exists |
| `get()` | Value or default | No | No | Safe access with fallback |
| `setdefault()` | Value | Yes (if missing) | No | Get with automatic default |
| `pop()` | Value | Yes | Optional | Remove and get value |
| `popitem()` | (key, value) | Yes | Yes (if empty) | Remove last item |
| `update()` | None | Yes | No | Merge dictionaries |
| `clear()` | None | Yes | No | Remove all items |
| `copy()` | New dict | No | No | Create shallow copy |

### View Behavior Comparison

| View | Returns | Dynamic | Iterable | Convert to |
|------|---------|---------|----------|------------|
| `keys()` | Keys view | ✅ Yes | ✅ Yes | `list()` |
| `values()` | Values view | ✅ Yes | ✅ Yes | `list()` |
| `items()` | (key, value) view | ✅ Yes | ✅ Yes | `list()` |

---

## 📋 Quick Reference Table

| Method | Syntax | Description | Example | Result |
|--------|--------|-------------|---------|--------|
| `clear()` | `d.clear()` | Removes all items | `d.clear()` | `{}` |
| `copy()` | `d.copy()` | Shallow copy | `d.copy()` | New dict |
| `fromkeys()` | `dict.fromkeys(iter, val)` | New dict from keys | `dict.fromkeys('ab',0)` | `{'a':0,'b':0}` |
| `get()` | `d.get(k, default)` | Safe access | `d.get('x',0)` | Value or default |
| `items()` | `d.items()` | Key-value pairs | `d.items()` | `dict_items` view |
| `keys()` | `d.keys()` | Keys view | `d.keys()` | `dict_keys` view |
| `pop()` | `d.pop(k, default)` | Remove and return | `d.pop('a')` | Removed value |
| `popitem()` | `d.popitem()` | Remove last item | `d.popitem()` | `(key, value)` |
| `setdefault()` | `d.setdefault(k, default)` | Get or set | `d.setdefault('x',0)` | Value |
| `update()` | `d.update(other)` | Merge dict | `d.update({'a':1})` | `None` |
| `values()` | `d.values()` | Values view | `d.values()` | `dict_values` view |
| `\|` (3.9+) | `d1 \| d2` | Merge new dict | `d1 \| d2` | New merged dict |
| `\|=` (3.9+) | `d1 \|= d2` | Merge in place | `d1 \|= d2` | `None` |
| `len()` | `len(d)` | Number of items | `len(d)` | Integer |
| `in` | `k in d` | Key membership | `'a' in d` | Boolean |

---

## 🎯 Method Selection Guide

### When to use each method:

```python
# Use d[key] when:
# - You're sure the key exists
# - You want KeyError if missing
value = d["existing_key"]

# Use get() when:
# - Key might be missing
# - You have a default value
value = d.get("maybe_missing", default)

# Use setdefault() when:
# - You want to set default if missing AND use the value
value = d.setdefault("key", [])

# Use update() when:
# - Merging multiple dictionaries
# - Updating with multiple key-value pairs
d.update({"a": 1, "b": 2})

# Use pop() when:
# - You need the value after removal
# - You want to handle missing keys
value = d.pop("key", default)

# Use popitem() when:
# - Processing items in LIFO order
# - You don't care which item is removed
key, value = d.popitem()

# Use items() when:
# - Looping through key-value pairs (most common)
for k, v in d.items():
    process(k, v)

# Use keys() when:
# - You only need keys
# - Checking required fields
if "required" in d.keys():
    ...

# Use values() when:
# - You only need values
# - Calculating statistics
total = sum(d.values())
```

---

## 💡 Pro Tips

```python
# 1. Chain get() for nested access
value = d.get("a", {}).get("b", {}).get("c", "default")

# 2. Use setdefault() for building nested structures
nested = {}
nested.setdefault("level1", {}).setdefault("level2", []).append("value")

# 3. Use update() with zip() for two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {}
d.update(zip(keys, values))

# 4. Use popitem() for LIFO processing
while d:
    key, value = d.popitem()
    process(key, value)

# 5. Use | operator for simple merges (3.9+)
merged = default_config | user_config

# 6. Use dictionary comprehension for transformations
doubled = {k: v*2 for k, v in d.items()}

# 7. Use Counter for counting (from collections)
from collections import Counter
freq = Counter("hello world")

# 8. Use defaultdict for automatic defaults
from collections import defaultdict
grouped = defaultdict(list)
for item in items:
    grouped[category].append(item)
```

---

*Master dictionary methods for efficient key-value operations! 🐍✨*
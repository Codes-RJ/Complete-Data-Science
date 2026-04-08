# ⚫ NONE TYPE – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What is None?](#what-is-none)
3. [Common Use Cases](#common-use-cases)
4. [None vs Other Falsy Values](#none-vs-other-falsy-values)
5. [Checking for None](#checking-for-none)
6. [When to Use None](#when-to-use-none)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**None** is a singleton object in Python that represents the absence of a value. It is the sole instance of the `NoneType` class.

| Feature | Description | Example |
|---------|-------------|---------|
| **Type** | `NoneType` | `type(None)` |
| **Value** | Only one: `None` | `None` |
| **Mutability** | Immutable | Cannot be changed |
| **Singleton** | Only one instance | All `None` are the same object |
| **Falsy** | Evaluates to `False` | `bool(None)` is `False` |

```python
# Examples of None
x = None
result = function_that_returns_nothing()
value = get_value() or None

print(type(None))     # <class 'NoneType'>
print(None is None)   # True (singleton)
print(bool(None))     # False (falsy)
```

**Key Characteristics:**
- ✅ Represents "no value" or "null"
- ✅ Singleton (only one instance exists)
- ✅ Falsy in boolean contexts
- ✅ Commonly used as default value for optional parameters
- ✅ Used as sentinel for missing data
- ✅ Cannot be instantiated (only `None` itself)

---

## ⚫ What is None?

None is Python's way of saying "nothing" or "no value". It's similar to `null` in other languages.

```python
# None is a singleton
a = None
b = None
print(a is b)      # True (same object)
print(id(a))       # Same memory address
print(id(b))       # Same memory address

# None is the only instance of NoneType
print(type(None))  # <class 'NoneType'>

# Cannot create new None
try:
    n = NoneType()
except NameError:
    print("NoneType is not directly accessible")

# None is falsy
if None:
    print("This won't print")
else:
    print("None is falsy")
```

---

## 📁 Common Use Cases

### 1. Function Returns (No Return Statement)

```python
# Functions without return return None
def say_hello(name):
    print(f"Hello, {name}")

result = say_hello("Alice")
print(result)  # None

# Explicitly returning None
def do_nothing():
    return None

print(do_nothing())  # None
```

### 2. Default Arguments for Mutable Types

```python
# ❌ WRONG - Mutable default argument
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(add_item_bad(1))  # [1]
print(add_item_bad(2))  # [1, 2] (unexpected!)

# ✅ CORRECT - Use None as default
def add_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_good(1))  # [1]
print(add_item_good(2))  # [2] (correct!)
```

### 3. Optional Parameters

```python
def greet(name, greeting=None):
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}!"

print(greet("Alice"))           # "Hello, Alice!"
print(greet("Bob", "Hi"))       # "Hi, Bob!"
print(greet("Charlie", None))   # "Hello, Charlie!"
```

### 4. Sentinel for Missing Values

```python
def find_user(users, name):
    for user in users:
        if user['name'] == name:
            return user
    return None  # Not found

users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
user = find_user(users, 'Charlie')

if user is None:
    print("User not found")
else:
    print(f"Found: {user}")
```

### 5. Initializing Variables

```python
# Initialize variable to None before assignment
result = None
data = None
connection = None

# Later, check if assigned
if result is None:
    print("Result not computed yet")
```

### 6. Removing Dictionary Keys

```python
# Using pop with default None
value = my_dict.pop('missing_key', None)
if value is None:
    print("Key didn't exist")
```

---

## ⚖️ None vs Other Falsy Values

```python
# All these are falsy, but different
values = [None, False, 0, 0.0, "", [], (), {}]

for val in values:
    print(f"{repr(val):6} -> bool: {bool(val)}")

# None is NOT the same as other falsy values
print(None == False)   # False
print(None == 0)       # False
print(None == "")      # False
print(None == [])      # False

# Use 'is' to check for None (not ==)
x = None
print(x is None)       # True (correct)
print(x == None)       # True (works but not recommended)
```

### When to Use Which

```python
# Use None for: Missing/optional values
def get_user(id):
    if id not in database:
        return None  # User doesn't exist

# Use False for: Boolean false state
is_active = False

# Use 0 for: Numeric zero
count = 0

# Use "" for: Empty string
name = ""

# Use [] for: Empty list
items = []
```

---

## 🔍 Checking for None

### The Right Way: `is` and `is not`

```python
x = None

# ✅ CORRECT - Use 'is' to check for None
if x is None:
    print("x is None")

if x is not None:
    print("x is not None")

# ⚠️ WORKS BUT NOT RECOMMENDED - Using ==
if x == None:
    print("Works but not Pythonic")

# ❌ WRONG - Comparing boolean
if not x:
    print("This also works but is ambiguous")
    print("Because None is falsy, but so are 0, '', []")
```

### Why Use `is` Instead of `==`?

```python
# 'is' checks identity (same object)
# '==' checks equality (same value)

# Since None is a singleton, 'is' is more precise
class AlwaysEqual:
    def __eq__(self, other):
        return True

weird = AlwaysEqual()
print(weird == None)   # True (but weird is not None)
print(weird is None)   # False (correct)

# 'is' is also slightly faster
import timeit
time_eq = timeit.timeit('x == None', setup='x=None', number=10000000)
time_is = timeit.timeit('x is None', setup='x=None', number=10000000)
print(f"== : {time_eq:.4f}s")
print(f"is : {time_is:.4f}s")
```

---

## 📁 When to Use None

| Use Case | Example | Why |
|----------|---------|-----|
| Optional parameters | `def func(x=None)` | Default for optional args |
| Missing data | `return None` | Indicates no value |
| Initialization | `result = None` | Placeholder before assignment |
| Sentinel value | `sentinel = None` | Special marker |
| Removing dict keys | `d.pop(k, None)` | Safe removal |
| Function returns | No explicit return | Implicitly returns None |

### Real-World Examples

```python
# 1. Optional configuration
def connect_to_db(host, port=None):
    if port is None:
        port = 5432  # Default port
    return f"Connected to {host}:{port}"

print(connect_to_db("localhost"))        # localhost:5432
print(connect_to_db("localhost", 8080))  # localhost:8080

# 2. Cache system
cache = {}

def get_from_cache(key):
    return cache.get(key)  # Returns None if not found

def set_in_cache(key, value):
    cache[key] = value

value = get_from_cache("user_123")
if value is None:
    print("Cache miss, loading from database...")
    value = load_from_database("user_123")
    set_in_cache("user_123", value)

# 3. Tree structure
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value)
    inorder_traversal(node.right)

# 4. Lazy initialization
class DatabaseConnection:
    def __init__(self):
        self._connection = None
    
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._create_connection()
        return self._connection
    
    def _create_connection(self):
        print("Creating connection...")
        return "DB Connection"

db = DatabaseConnection()
print(db.connection)  # Creates connection
print(db.connection)  # Uses existing
```

---

## 💡 Common Patterns

### Default Value Pattern

```python
# Using None as default, then assigning
def process(data, config=None):
    if config is None:
        config = {"timeout": 30, "retry": 3}
    return process_with_config(data, config)

# Single line default (be careful with mutable types)
def process(data, config=None):
    config = config or {"timeout": 30, "retry": 3}
    return process_with_config(data, config)
```

### Sentinel Pattern

```python
# Custom sentinel object
_sentinel = object()

def get_value(key, default=_sentinel):
    if key in cache:
        return cache[key]
    if default is _sentinel:
        raise KeyError(f"Key {key} not found")
    return default

# None is a valid value
cache = {"user": None}
value = get_value("user", "default")  # Returns None (not default)
```

### Optional Chaining (Python 3.8+)

```python
# Before (verbose)
if obj is not None and obj.attr is not None:
    value = obj.attr.value
else:
    value = None

# Using walrus operator (Python 3.8+)
if (obj is not None) and ((attr := obj.attr) is not None):
    value = attr.value
else:
    value = None
```

---

## 📚 Next Steps

After understanding None basics:
1. Open `none_type.md` for detailed examples
2. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Optional Values** – Using `Optional` type hint
- **Default Parameters** – Using None as default
- **Sentinel Objects** – Creating unique sentinels
- **Null Object Pattern** – Alternative to None
- **Optional Chaining** – Safe attribute access

---

## 💡 Quick Tips

```python
# ✅ DO: Use 'is' to check for None
if value is None:
    handle_missing()

# ✅ DO: Use None for optional parameters
def func(required, optional=None):
    pass

# ✅ DO: Return None for missing values
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None

# ❌ DON'T: Compare None with ==
if value == None:  # Use 'is' instead
    pass

# ❌ DON'T: Use None as boolean
if not value:  # Ambiguous (0, "", [] also falsy)
    pass

# ✅ DO: Explicit None check
if value is None:
    pass
```

---

*Master None for handling missing and optional values! 🐍✨*
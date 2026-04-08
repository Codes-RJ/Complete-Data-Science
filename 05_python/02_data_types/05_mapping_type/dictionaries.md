# 📘 DICTIONARIES (dict) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Dictionaries?](#what-are-dictionaries)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Values](#accessing-values)
4. [Adding and Modifying](#adding-and-modifying)
5. [Removing Items](#removing-items)
6. [Dictionary Methods](#dictionary-methods)
7. [Looping Through Dictionaries](#looping-through-dictionaries)
8. [Dictionary Comprehensions](#dictionary-comprehensions)
9. [Nested Dictionaries](#nested-dictionaries)
10. [Real-World Examples](#real-world-examples)
11. [Common Pitfalls](#common-pitfalls)
12. [Performance Tips](#performance-tips)
13. [Practice Exercises](#practice-exercises)

---

## 📖 What are Dictionaries?

**Dictionaries** are mutable, ordered collections of key-value pairs. They provide O(1) average time complexity for lookups, insertions, and deletions.

```python
# Examples of dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
scores = {"math": 95, "science": 87, "history": 92}
nested = {"user": {"name": "Bob", "email": "bob@example.com"}}
mixed = {1: "one", "two": 2, (1, 2): "tuple key"}
```

**Key Features:**
- ✅ Key-value pairs for fast lookups
- ✅ Keys must be immutable (strings, numbers, tuples)
- ✅ Values can be any type (including other dicts)
- ✅ Maintain insertion order (Python 3.7+)
- ✅ Dynamic size (grow and shrink as needed)
- ✅ Extremely fast membership testing (O(1))

---

## 🎯 Creating Dictionaries

### Method 1: Curly Braces `{}`

```python
# Empty dictionary
empty = {}
print(empty)  # {}

# Dictionary with items
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Mixed key types
mixed = {1: "one", "two": 2, (1, 2): "tuple key"}
print(mixed)  # {1: 'one', 'two': 2, (1, 2): 'tuple key'}
```

### Method 2: `dict()` Constructor

```python
# From keyword arguments
person = dict(name="Alice", age=30, city="New York")
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# From list of tuples
pairs = [("name", "Alice"), ("age", 30), ("city", "New York")]
person = dict(pairs)
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# From zip of two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Empty dictionary
empty = dict()
print(empty)  # {}
```

### Method 3: `fromkeys()` Class Method

```python
# Create dict with default value None
keys = ["a", "b", "c"]
d = dict.fromkeys(keys)
print(d)  # {'a': None, 'b': None, 'c': None}

# Create dict with custom default value
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}

# Real use: Initialize counters
counters = dict.fromkeys(["apple", "banana", "cherry"], 0)
counters["apple"] += 1
print(counters)  # {'apple': 1, 'banana': 0, 'cherry': 0}
```

### Method 4: Dictionary Comprehension

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

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}
```

---

## 🔍 Accessing Values

### Direct Access `d[key]`

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access existing key
print(person["name"])  # "Alice"
print(person["age"])   # 30

# KeyError if key doesn't exist
try:
    print(person["country"])
except KeyError:
    print("Key not found!")
```

### `get(key[, default])` – Safe Access

```python
person = {"name": "Alice", "age": 30}

# Returns None if key missing (no error)
print(person.get("city"))        # None
print(person.get("country"))     # None

# Returns default value if key missing
print(person.get("city", "Unknown"))     # "Unknown"
print(person.get("country", "USA"))      # "USA"

# Returns value if key exists
print(person.get("name", "Unknown"))     # "Alice"

# Real use: Safe counting
counts = {}
counts["apple"] = counts.get("apple", 0) + 1
counts["apple"] = counts.get("apple", 0) + 1
counts["banana"] = counts.get("banana", 0) + 1
print(counts)  # {'apple': 2, 'banana': 1}
```

### `setdefault(key[, default])` – Get with Default Assignment

```python
person = {"name": "Alice", "age": 30}

# If key exists, returns value
name = person.setdefault("name", "Unknown")
print(name)    # "Alice"
print(person)  # {'name': 'Alice', 'age': 30} (unchanged)

# If key missing, sets default and returns it
city = person.setdefault("city", "New York")
print(city)    # "New York"
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Real use: Grouping items
groups = {}
items = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]

for category, item in items:
    groups.setdefault(category, []).append(item)

print(groups)  # {'fruit': ['apple', 'banana'], 'veg': ['carrot']}
```

---

## ✏️ Adding and Modifying

### Direct Assignment

```python
person = {"name": "Alice"}

# Add new key-value pair
person["age"] = 30
print(person)  # {'name': 'Alice', 'age': 30}

# Update existing value
person["name"] = "Bob"
print(person)  # {'name': 'Bob', 'age': 30}

# Add multiple at once
person["city"] = "NYC"
person["job"] = "Engineer"
print(person)  # {'name': 'Bob', 'age': 30, 'city': 'NYC', 'job': 'Engineer'}
```

### `update([other])` – Merge Dictionaries

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

# Real use: Merging configurations
default_config = {"host": "localhost", "port": 8080, "debug": False}
user_config = {"port": 9090, "debug": True}
default_config.update(user_config)
print(default_config)  # {'host': 'localhost', 'port': 9090, 'debug': True}
```

### Merge Operator `|` and `|=` (Python 3.9+)

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
```

---

## 🗑️ Removing Items

### `pop(key[, default])` – Remove and Return Value

```python
person = {"name": "Alice", "age": 30, "city": "NYC", "job": "Engineer"}

# Remove existing key
age = person.pop("age")
print(age)      # 30
print(person)   # {'name': 'Alice', 'city': 'NYC', 'job': 'Engineer'}

# Remove with default (no error if missing)
country = person.pop("country", "Not found")
print(country)  # "Not found"
print(person)   # Unchanged

# KeyError if missing and no default
try:
    person.pop("missing")
except KeyError:
    print("Key not found!")

# Real use: Process and remove
queue = {"task1": "pending", "task2": "pending", "task3": "completed"}
while queue:
    key, value = queue.popitem()  # Remove arbitrary item
    print(f"Processing {key}: {value}")
```

### `popitem()` – Remove and Return Last Item (LIFO)

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Removes and returns last inserted item
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

# Real use: LIFO processing
stack = {"task1": "data1", "task2": "data2", "task3": "data3"}
while stack:
    key, value = stack.popitem()
    print(f"Processing {key}: {value}")
```

### `del` Statement

```python
person = {"name": "Alice", "age": 30, "city": "NYC", "job": "Engineer"}

# Delete specific key
del person["age"]
print(person)  # {'name': 'Alice', 'city': 'NYC', 'job': 'Engineer'}

# Delete multiple keys
del person["city"], person["job"]
print(person)  # {'name': 'Alice'}

# KeyError if missing
try:
    del person["missing"]
except KeyError:
    print("Key not found!")

# Delete entire dictionary
del person
# print(person)  # NameError: name 'person' is not defined
```

### `clear()` – Remove All Items

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}
person.clear()
print(person)  # {}

# Real use: Reset dictionary for reuse
cache = {"url1": "data1", "url2": "data2"}
# Process cache...
cache.clear()  # Ready for new data
```

---

## 📚 Dictionary Methods

### `copy()` – Shallow Copy

```python
original = {"a": 1, "b": 2, "c": {"d": 3}}

# Shallow copy
shallow = original.copy()
print(shallow)  # {'a': 1, 'b': 2, 'c': {'d': 3}}

# Modifying shallow copy doesn't affect original at top level
shallow["a"] = 99
print(original)  # {'a': 1, 'b': 2, 'c': {'d': 3}} (unchanged)

# But nested objects are shared
shallow["c"]["d"] = 99
print(original)  # {'a': 1, 'b': 2, 'c': {'d': 99}} (changed!)

# Alternative shallow copies
copy1 = original.copy()
copy2 = dict(original)
copy3 = original | {}  # Python 3.9+

# Deep copy for nested structures
import copy
deep = copy.deepcopy(original)
deep["c"]["d"] = 100
print(original)  # {'a': 1, 'b': 2, 'c': {'d': 99}} (unchanged)
```

### `keys()` – View of Keys

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

# Keys view is dynamic (updates when dict changes)
person["job"] = "Engineer"
print(keys)  # dict_keys(['name', 'age', 'city', 'job'])

# Membership testing is fast
print("name" in keys)   # True
print("country" in keys) # False
```

### `values()` – View of Values

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Get values view
values = person.values()
print(values)  # dict_values(['Alice', 30, 'NYC'])

# Iterate through values
for value in values:
    print(value)  # Alice, 30, NYC

# Convert to list
value_list = list(values)
print(value_list)  # ['Alice', 30, 'NYC']

# Values view is dynamic
person["job"] = "Engineer"
print(values)  # dict_values(['Alice', 30, 'NYC', 'Engineer'])

# Membership testing (slower than keys)
print("Alice" in values)  # True
print("Bob" in values)    # False
```

### `items()` – View of Key-Value Pairs

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Get items view
items = person.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'NYC')])

# Iterate through key-value pairs (recommended)
for key, value in items:
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 30
# city: NYC

# Convert to list of tuples
items_list = list(items)
print(items_list)  # [('name', 'Alice'), ('age', 30), ('city', 'NYC')]

# Items view is dynamic
person["job"] = "Engineer"
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'NYC'), ('job', 'Engineer')])

# Membership testing
print(("name", "Alice") in items)   # True
print(("name", "Bob") in items)     # False
```

### `len()` – Number of Items

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(len(person))  # 3

empty = {}
print(len(empty))   # 0
```

### `in` and `not in` – Membership Testing

```python
person = {"name": "Alice", "age": 30}

# Check keys (fast O(1))
print("name" in person)      # True
print("city" in person)      # False
print("age" not in person)   # False

# Check values (slower O(n))
print("Alice" in person.values())   # True
print(25 in person.values())        # False
```

---

## 🔄 Looping Through Dictionaries

### Loop Through Keys

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Method 1: Direct iteration (keys)
for key in person:
    print(f"{key}: {person[key]}")

# Method 2: Explicit keys()
for key in person.keys():
    print(f"{key}: {person[key]}")

# Method 3: Sorted keys
for key in sorted(person.keys()):
    print(f"{key}: {person[key]}")
```

### Loop Through Values

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Loop through values only
for value in person.values():
    print(value)
# Output: Alice, 30, NYC

# With index (not recommended)
for i, value in enumerate(person.values()):
    print(f"Value {i}: {value}")
```

### Loop Through Key-Value Pairs (Recommended)

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Best practice
for key, value in person.items():
    print(f"{key}: {value}")

# With condition
for key, value in person.items():
    if isinstance(value, int):
        print(f"{key} is a number: {value}")

# Sorted by key
for key, value in sorted(person.items()):
    print(f"{key}: {value}")

# Sorted by value
for key, value in sorted(person.items(), key=lambda x: x[1]):
    print(f"{key}: {value}")

# Reverse order
for key, value in reversed(person.items()):
    print(f"{key}: {value}")
```

### While Loop (Not Common)

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Convert to list for while loop
items = list(person.items())
i = 0
while i < len(items):
    key, value = items[i]
    print(f"{key}: {value}")
    i += 1
```

---

## 🔄 Dictionary Comprehensions

### Basic Comprehension

```python
# Squares
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

### Transformations

```python
# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Apply function to values
numbers = {"a": 1, "b": 2, "c": 3}
doubled = {k: v*2 for k, v in numbers.items()}
print(doubled)  # {'a': 2, 'b': 4, 'c': 6}

# Filter items
person = {"name": "Alice", "age": 30, "city": "NYC", "job": "Engineer"}
strings_only = {k: v for k, v in person.items() if isinstance(v, str)}
print(strings_only)  # {'name': 'Alice', 'city': 'NYC', 'job': 'Engineer'}

# Conditional values
scores = {"Alice": 85, "Bob": 45, "Charlie": 92, "David": 58}
grades = {name: "Pass" if score >= 60 else "Fail" for name, score in scores.items()}
print(grades)  # {'Alice': 'Pass', 'Bob': 'Fail', 'Charlie': 'Pass', 'David': 'Fail'}
```

### Nested Comprehensions

```python
# Flatten nested dictionary
nested = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
flattened = {f"{outer}_{inner}": value 
             for outer, inner_dict in nested.items() 
             for inner, value in inner_dict.items()}
print(flattened)  # {'a_x': 1, 'a_y': 2, 'b_x': 3, 'b_y': 4}

# Matrix to dictionary
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_dict = {(i, j): matrix[i][j] 
               for i in range(3) 
               for j in range(3)}
print(matrix_dict)  # {(0,0):1, (0,1):2, (0,2):3, (1,0):4, ...}
```

---

## 🪆 Nested Dictionaries

### Creating Nested Dictionaries

```python
# Direct creation
user = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    },
    "contacts": {
        "email": "alice@example.com",
        "phone": "555-1234"
    }
}

# Building dynamically
user = {}
user["name"] = "Alice"
user["address"] = {}
user["address"]["street"] = "123 Main St"
user["address"]["city"] = "New York"
```

### Accessing Nested Values

```python
user = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

# Direct access
print(user["address"]["city"])  # "New York"

# Safe access with get()
city = user.get("address", {}).get("city", "Unknown")
print(city)  # "New York"

# Using try/except
try:
    print(user["address"]["country"])
except KeyError:
    print("Key not found")
```

### Modifying Nested Values

```python
user = {
    "name": "Alice",
    "address": {"city": "New York"}
}

# Update nested value
user["address"]["city"] = "Boston"
print(user)  # {'name': 'Alice', 'address': {'city': 'Boston'}}

# Add nested key
user["address"]["zip"] = "02101"
print(user)  # {'name': 'Alice', 'address': {'city': 'Boston', 'zip': '02101'}}

# Add nested dictionary
user["contacts"] = {}
user["contacts"]["email"] = "alice@example.com"
```

### Looping Through Nested Dictionaries

```python
user = {
    "name": "Alice",
    "address": {"street": "123 Main St", "city": "NYC"},
    "contacts": {"email": "alice@example.com", "phone": "555-1234"}
}

# Recursive function to print all keys
def print_nested(d, indent=0):
    for key, value in d.items():
        print("  " * indent + f"{key}:")
        if isinstance(value, dict):
            print_nested(value, indent + 1)
        else:
            print("  " * (indent + 1) + str(value))

print_nested(user)
# Output:
# name:
#   Alice
# address:
#   street:
#     123 Main St
#   city:
#     NYC
# contacts:
#   email:
#     alice@example.com
#   phone:
#     555-1234
```

---

## 🌍 Real-World Examples

### Example 1: Phone Book Application

```python
class PhoneBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone, email=None):
        """Add or update contact"""
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Added/Updated: {name}")
    
    def get_contact(self, name):
        """Get contact by name"""
        return self.contacts.get(name, "Contact not found")
    
    def delete_contact(self, name):
        """Delete contact by name"""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted: {name}")
        else:
            print("Contact not found")
    
    def search_by_phone(self, phone):
        """Search contact by phone number"""
        for name, details in self.contacts.items():
            if details["phone"] == phone:
                return name, details
        return None, "Not found"
    
    def list_all(self):
        """List all contacts"""
        if not self.contacts:
            print("Phone book is empty")
            return
        
        print("\n" + "=" * 40)
        print("PHONE BOOK")
        print("=" * 40)
        for name, details in sorted(self.contacts.items()):
            print(f"Name: {name}")
            print(f"  Phone: {details['phone']}")
            if details['email']:
                print(f"  Email: {details['email']}")
            print("-" * 40)
    
    def get_statistics(self):
        """Get phone book statistics"""
        total = len(self.contacts)
        with_email = sum(1 for c in self.contacts.values() if c['email'])
        
        return {
            'total_contacts': total,
            'with_email': with_email,
            'without_email': total - with_email
        }

# Usage
pb = PhoneBook()

# Add contacts
pb.add_contact("Alice", "555-1234", "alice@example.com")
pb.add_contact("Bob", "555-5678")
pb.add_contact("Charlie", "555-9012", "charlie@example.com")
pb.add_contact("Diana", "555-3456")

# List all
pb.list_all()

# Search
print("\nSearching for Bob:")
print(pb.get_contact("Bob"))

print("\nSearching by phone 555-9012:")
name, details = pb.search_by_phone("555-9012")
print(f"Found: {name} - {details}")

# Statistics
stats = pb.get_statistics()
print(f"\nStatistics: {stats}")

# Delete contact
pb.delete_contact("Bob")
pb.list_all()
```

### Example 2: Student Gradebook

```python
class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = set()
    
    def add_student(self, student_id, name):
        """Add new student"""
        if student_id not in self.students:
            self.students[student_id] = {
                'name': name,
                'grades': {},
                'attendance': []
            }
            print(f"Added student: {name} (ID: {student_id})")
        else:
            print(f"Student {student_id} already exists")
    
    def add_grade(self, student_id, course, grade):
        """Add grade for student"""
        if student_id not in self.students:
            print(f"Student {student_id} not found")
            return
        
        self.students[student_id]['grades'][course] = grade
        self.courses.add(course)
        print(f"Added grade {grade} for {self.students[student_id]['name']} in {course}")
    
    def record_attendance(self, student_id, date, present=True):
        """Record attendance"""
        if student_id not in self.students:
            print(f"Student {student_id} not found")
            return
        
        self.students[student_id]['attendance'].append({
            'date': date,
            'present': present
        })
        status = "Present" if present else "Absent"
        print(f"Marked {self.students[student_id]['name']} as {status} on {date}")
    
    def get_student_average(self, student_id):
        """Calculate student's average grade"""
        if student_id not in self.students:
            return None
        
        grades = self.students[student_id]['grades'].values()
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
    def get_class_average(self, course):
        """Calculate class average for a course"""
        total = 0
        count = 0
        
        for student in self.students.values():
            if course in student['grades']:
                total += student['grades'][course]
                count += 1
        
        return total / count if count > 0 else 0
    
    def get_honors_roll(self, min_average=85):
        """Get students with average above threshold"""
        honors = []
        for sid, student in self.students.items():
            avg = self.get_student_average(sid)
            if avg >= min_average:
                honors.append((student['name'], avg))
        
        return sorted(honors, key=lambda x: x[1], reverse=True)
    
    def get_attendance_report(self, student_id):
        """Get attendance report for student"""
        if student_id not in self.students:
            return None
        
        attendance = self.students[student_id]['attendance']
        total = len(attendance)
        if total == 0:
            return {'present': 0, 'absent': 0, 'percentage': 0}
        
        present = sum(1 for a in attendance if a['present'])
        absent = total - present
        percentage = (present / total) * 100
        
        return {
            'total_days': total,
            'present': present,
            'absent': absent,
            'percentage': round(percentage, 1)
        }
    
    def generate_report_card(self, student_id):
        """Generate full report card"""
        if student_id not in self.students:
            print("Student not found")
            return
        
        student = self.students[student_id]
        avg = self.get_student_average(student_id)
        attendance = self.get_attendance_report(student_id)
        
        print("=" * 50)
        print(f"REPORT CARD: {student['name']} (ID: {student_id})")
        print("=" * 50)
        
        print("\nGRADES:")
        for course, grade in sorted(student['grades'].items()):
            letter = self._get_letter_grade(grade)
            print(f"  {course}: {grade} ({letter})")
        
        print(f"\nOverall Average: {avg:.1f} ({self._get_letter_grade(avg)})")
        
        if attendance:
            print(f"\nATTENDANCE:")
            print(f"  Present: {attendance['present']} days")
            print(f"  Absent: {attendance['absent']} days")
            print(f"  Attendance Rate: {attendance['percentage']}%")
        
        print("=" * 50)
    
    def _get_letter_grade(self, score):
        """Convert numeric score to letter grade"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

# Usage
gb = Gradebook()

# Add students
gb.add_student(1001, "Alice Johnson")
gb.add_student(1002, "Bob Smith")
gb.add_student(1003, "Charlie Brown")

# Add grades
gb.add_grade(1001, "Math", 95)
gb.add_grade(1001, "Science", 88)
gb.add_grade(1001, "History", 92)

gb.add_grade(1002, "Math", 78)
gb.add_grade(1002, "Science", 82)
gb.add_grade(1002, "History", 75)

gb.add_grade(1003, "Math", 65)
gb.add_grade(1003, "Science", 70)
gb.add_grade(1003, "History", 68)

# Record attendance
gb.record_attendance(1001, "2024-01-15", True)
gb.record_attendance(1001, "2024-01-16", True)
gb.record_attendance(1001, "2024-01-17", False)

# Generate reports
gb.generate_report_card(1001)
gb.generate_report_card(1002)

# Class averages
print("\n" + "=" * 40)
print("CLASS AVERAGES")
print("=" * 40)
for course in ['Math', 'Science', 'History']:
    avg = gb.get_class_average(course)
    print(f"{course}: {avg:.1f}")

# Honors roll
honors = gb.get_honors_roll(80)
print(f"\nHONORS ROLL (Average ≥ 80):")
for name, avg in honors:
    print(f"  {name}: {avg:.1f}")
```

### Example 3: Cache System with LRU

```python
from collections import OrderedDict
import time

class LRUCache:
    """Least Recently Used Cache using OrderedDict"""
    
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.hits = 0
        self.misses = 0
    
    def get(self, key):
        """Get value from cache"""
        if key not in self.cache:
            self.misses += 1
            return None
        
        # Move to end (most recently used)
        value = self.cache.pop(key)
        self.cache[key] = value
        self.hits += 1
        return value
    
    def put(self, key, value):
        """Put value in cache"""
        if key in self.cache:
            # Remove old entry
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)
        
        # Add new entry (most recently used)
        self.cache[key] = value
    
    def clear(self):
        """Clear cache"""
        self.cache.clear()
        self.hits = 0
        self.misses = 0
    
    def get_stats(self):
        """Get cache statistics"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        
        return {
            'size': len(self.cache),
            'capacity': self.capacity,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f"{hit_rate:.1f}%"
        }
    
    def display(self):
        """Display cache contents"""
        print("\n" + "=" * 40)
        print("CACHE CONTENTS (Most recent first)")
        print("=" * 40)
        for key, value in reversed(self.cache.items()):
            print(f"  {key}: {value}")
        print("=" * 40)

# Simulate expensive operation
def expensive_operation(x):
    print(f"Computing for {x}...")
    time.sleep(0.5)  # Simulate heavy computation
    return x ** 2

# Usage
cache = LRUCache(capacity=3)

# Simulate repeated calls
test_values = [1, 2, 3, 2, 4, 1, 5, 2, 3, 4, 5, 1]

print("SIMULATING CACHE OPERATIONS")
print("=" * 40)

for value in test_values:
    result = cache.get(value)
    if result is None:
        # Not in cache, compute and store
        result = expensive_operation(value)
        cache.put(value, result)
        print(f"  Result: {result} (CACHE MISS)")
    else:
        print(f"  Result: {result} (CACHE HIT)")
    
    print(f"Cache stats: {cache.get_stats()}")
    cache.display()
    print()

print("\nFINAL STATISTICS:")
print(cache.get_stats())
```

### Example 4: Configuration Manager

```python
import json
from typing import Any, Dict

class ConfigManager:
    def __init__(self, config_file=None):
        self.config = {}
        self.defaults = {}
        self.watchers = {}
        
        if config_file:
            self.load_from_file(config_file)
    
    def set_defaults(self, defaults: Dict[str, Any]):
        """Set default configuration values"""
        self.defaults = defaults.copy()
        self._apply_defaults()
    
    def _apply_defaults(self):
        """Apply defaults to current config"""
        for key, value in self.defaults.items():
            if key not in self.config:
                self.config[key] = value
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        # Check if key has dot notation (nested)
        if '.' in key:
            return self._get_nested(key, default)
        
        return self.config.get(key, default)
    
    def _get_nested(self, key: str, default=None):
        """Get nested configuration value"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        if '.' in key:
            self._set_nested(key, value)
        else:
            self.config[key] = value
        
        # Notify watchers
        self._notify_watchers(key, value)
    
    def _set_nested(self, key: str, value: Any):
        """Set nested configuration value"""
        keys = key.split('.')
        target = self.config
        
        # Navigate to parent
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        
        # Set value
        target[keys[-1]] = value
    
    def update(self, updates: Dict[str, Any]):
        """Update multiple configuration values"""
        for key, value in updates.items():
            self.set(key, value)
    
    def delete(self, key: str):
        """Delete configuration key"""
        if '.' in key:
            self._delete_nested(key)
        elif key in self.config:
            del self.config[key]
    
    def _delete_nested(self, key: str):
        """Delete nested configuration key"""
        keys = key.split('.')
        target = self.config
        
        for k in keys[:-1]:
            if k not in target:
                return
            target = target[k]
        
        if keys[-1] in target:
            del target[keys[-1]]
    
    def watch(self, key: str, callback):
        """Watch for changes to a configuration key"""
        if key not in self.watchers:
            self.watchers[key] = []
        self.watchers[key].append(callback)
    
    def _notify_watchers(self, key: str, value: Any):
        """Notify watchers of changes"""
        if key in self.watchers:
            for callback in self.watchers[key]:
                callback(key, value)
    
    def load_from_file(self, filename: str):
        """Load configuration from JSON file"""
        try:
            with open(filename, 'r') as f:
                self.config = json.load(f)
            print(f"Loaded config from {filename}")
        except FileNotFoundError:
            print(f"Config file {filename} not found, using defaults")
        except json.JSONDecodeError:
            print(f"Error parsing {filename}")
    
    def save_to_file(self, filename: str):
        """Save configuration to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"Saved config to {filename}")
    
    def get_all(self):
        """Get all configuration values"""
        return self.config.copy()
    
    def reset(self):
        """Reset to defaults"""
        self.config = self.defaults.copy()
    
    def display(self):
        """Display configuration"""
        print("=" * 50)
        print("CURRENT CONFIGURATION")
        print("=" * 50)
        self._display_dict(self.config)
        print("=" * 50)
    
    def _display_dict(self, d, indent=0):
        """Recursively display dictionary"""
        for key, value in d.items():
            if isinstance(value, dict):
                print("  " * indent + f"{key}:")
                self._display_dict(value, indent + 1)
            else:
                print("  " * indent + f"{key}: {value}")

# Usage
config = ConfigManager()

# Set defaults
config.set_defaults({
    "app": {
        "name": "MyApp",
        "version": "1.0.0",
        "debug": False
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
})

# Add watcher
def on_config_change(key, value):
    print(f"⚡ CONFIG CHANGED: {key} = {value}")

config.watch("app.debug", on_config_change)
config.watch("database.port", on_config_change)

# Modify configuration
config.set("app.debug", True)
config.set("database.port", 5433)
config.set("database.user", "admin")
config.set("database.password", "secret")

# Get values
print(f"App name: {config.get('app.name')}")
print(f"Debug mode: {config.get('app.debug')}")
print(f"Database port: {config.get('database.port')}")
print(f"Missing key: {config.get('missing.key', 'default')}")

# Display all
config.display()

# Save to file
config.save_to_file("config.json")
```

### Example 5: Word Frequency Counter

```python
from collections import defaultdict, Counter
import re
import string

class WordFrequency:
    def __init__(self):
        self.frequencies = {}
        self.total_words = 0
        self.unique_words = 0
    
    def add_text(self, text):
        """Add text to analyze"""
        # Clean text
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Split into words
        words = text.split()
        
        for word in words:
            if word not in self.frequencies:
                self.frequencies[word] = 0
                self.unique_words += 1
            self.frequencies[word] += 1
            self.total_words += 1
    
    def get_frequency(self, word):
        """Get frequency of specific word"""
        return self.frequencies.get(word.lower(), 0)
    
    def get_most_common(self, n=10):
        """Get n most common words"""
        sorted_words = sorted(
            self.frequencies.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_words[:n]
    
    def get_least_common(self, n=10):
        """Get n least common words"""
        sorted_words = sorted(
            self.frequencies.items(),
            key=lambda x: x[1]
        )
        return sorted_words[:n]
    
    def get_words_by_length(self, length):
        """Get words of specific length"""
        return {
            word: count
            for word, count in self.frequencies.items()
            if len(word) == length
        }
    
    def get_statistics(self):
        """Get frequency statistics"""
        if not self.frequencies:
            return {}
        
        counts = list(self.frequencies.values())
        
        return {
            'total_words': self.total_words,
            'unique_words': self.unique_words,
            'max_frequency': max(counts),
            'min_frequency': min(counts),
            'avg_frequency': self.total_words / self.unique_words,
            'most_common_word': max(self.frequencies.items(), key=lambda x: x[1])[0],
            'least_common_word': min(self.frequencies.items(), key=lambda x: x[1])[0]
        }
    
    def search_by_pattern(self, pattern):
        """Search words by pattern (regex)"""
        regex = re.compile(pattern)
        return {
            word: count
            for word, count in self.frequencies.items()
            if regex.search(word)
        }
    
    def generate_report(self):
        """Generate frequency report"""
        stats = self.get_statistics()
        
        print("=" * 50)
        print("WORD FREQUENCY REPORT")
        print("=" * 50)
        print(f"Total Words: {stats['total_words']:,}")
        print(f"Unique Words: {stats['unique_words']:,}")
        print(f"Average Frequency: {stats['avg_frequency']:.2f}")
        print(f"Most Common: '{stats['most_common_word']}' ({stats['max_frequency']} times)")
        print(f"Least Common: '{stats['least_common_word']}' ({stats['min_frequency']} time)")
        
        print("\nTOP 10 MOST COMMON WORDS:")
        print("-" * 30)
        for i, (word, count) in enumerate(self.get_most_common(10), 1):
            percentage = (count / stats['total_words']) * 100
            bar = '█' * int(percentage / 2)
            print(f"{i:2}. '{word}' -> {count:4} times ({percentage:.1f}%) {bar}")
        
        print("\nWORD LENGTH DISTRIBUTION:")
        print("-" * 30)
        length_stats = {}
        for word in self.frequencies:
            length = len(word)
            length_stats[length] = length_stats.get(length, 0) + 1
        
        for length in sorted(length_stats.keys()):
            count = length_stats[length]
            bar = '█' * int(count / max(length_stats.values()) * 30)
            print(f"Length {length:2}: {count:3} words {bar}")
        
        print("=" * 50)

# Usage
wf = WordFrequency()

# Sample text
sample_text = """
Python is a powerful programming language. Python is great for data science.
Data science uses Python extensively. Python has a simple syntax that makes it easy to learn.
Many companies use Python for their backend systems. Python's community is very active.
Python continues to evolve with new features. Learning Python is a valuable skill.
"""

print("Analyzing text...")
wf.add_text(sample_text)

# Get specific word frequency
print(f"\nFrequency of 'python': {wf.get_frequency('python')}")
print(f"Frequency of 'data': {wf.get_frequency('data')}")
print(f"Frequency of 'science': {wf.get_frequency('science')}")

# Most common words
print("\nMost common words:")
for word, count in wf.get_most_common(5):
    print(f"  {word}: {count}")

# Search by pattern
print("\nWords starting with 'p':")
for word, count in wf.search_by_pattern('^p').items():
    print(f"  {word}: {count}")

# Words by length
print("\nWords of length 3:")
for word, count in wf.get_words_by_length(3).items():
    print(f"  {word}: {count}")

# Generate full report
wf.generate_report()
```

### Example 6: Graph Representation and Search

```python
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # node -> set of neighbors
    
    def add_node(self, node):
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = set()
    
    def add_edge(self, node1, node2, bidirectional=True):
        """Add an edge between nodes"""
        self.add_node(node1)
        self.add_node(node2)
        
        self.graph[node1].add(node2)
        if bidirectional:
            self.graph[node2].add(node1)
    
    def remove_edge(self, node1, node2, bidirectional=True):
        """Remove edge between nodes"""
        if node1 in self.graph:
            self.graph[node1].discard(node2)
        if bidirectional and node2 in self.graph:
            self.graph[node2].discard(node1)
    
    def remove_node(self, node):
        """Remove node and all its edges"""
        if node in self.graph:
            # Remove edges from other nodes
            for neighbor in self.graph[node]:
                self.graph[neighbor].discard(node)
            # Remove the node
            del self.graph[node]
    
    def get_neighbors(self, node):
        """Get neighbors of a node"""
        return self.graph.get(node, set())
    
    def bfs(self, start, target=None):
        """Breadth-First Search"""
        visited = set()
        queue = deque([start])
        parent = {start: None}
        
        while queue:
            node = queue.popleft()
            
            if node not in visited:
                visited.add(node)
                
                if target and node == target:
                    # Reconstruct path
                    path = []
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]
                
                for neighbor in self.graph.get(node, set()):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        if neighbor not in parent:
                            parent[neighbor] = node
        
        return visited if not target else None
    
    def dfs(self, start, target=None):
        """Depth-First Search"""
        visited = set()
        stack = [start]
        parent = {start: None}
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                
                if target and node == target:
                    # Reconstruct path
                    path = []
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]
                
                for neighbor in self.graph.get(node, set()):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        if neighbor not in parent:
                            parent[neighbor] = node
        
        return visited if not target else None
    
    def has_path(self, start, target):
        """Check if path exists between nodes"""
        return self.bfs(start, target) is not None
    
    def find_shortest_path(self, start, target):
        """Find shortest path between nodes"""
        return self.bfs(start, target)
    
    def get_connected_components(self):
        """Get connected components"""
        visited = set()
        components = []
        
        for node in self.graph:
            if node not in visited:
                component = self.bfs(node)
                visited.update(component)
                components.append(component)
        
        return components
    
    def get_degree(self, node):
        """Get degree of node"""
        return len(self.graph.get(node, set()))
    
    def get_node_count(self):
        """Get total number of nodes"""
        return len(self.graph)
    
    def get_edge_count(self):
        """Get total number of edges"""
        total = 0
        for neighbors in self.graph.values():
            total += len(neighbors)
        return total // 2  # Each edge counted twice
    
    def display(self):
        """Display graph"""
        print("=" * 50)
        print("GRAPH")
        print("=" * 50)
        print(f"Nodes: {self.get_node_count()}")
        print(f"Edges: {self.get_edge_count()}")
        
        for node in sorted(self.graph.keys()):
            neighbors = sorted(self.graph[node])
            print(f"{node}: {neighbors}")
        
        components = self.get_connected_components()
        print(f"\nConnected Components: {len(components)}")
        for i, comp in enumerate(components, 1):
            print(f"  Component {i}: {sorted(comp)}")
        
        print("=" * 50)

# Usage
g = Graph()

# Build a social network graph
g.add_edge("Alice", "Bob")
g.add_edge("Alice", "Charlie")
g.add_edge("Bob", "Charlie")
g.add_edge("Bob", "David")
g.add_edge("Charlie", "Eve")
g.add_edge("David", "Eve")
g.add_edge("Frank", "Grace")  # Separate component

print("SOCIAL NETWORK GRAPH")
g.display()

# Find paths
print("\nPATH FINDING")
print("-" * 40)

start, target = "Alice", "Eve"
path = g.find_shortest_path(start, target)
print(f"Shortest path from {start} to {target}: {path}")

print(f"Has path from Alice to Frank? {g.has_path('Alice', 'Frank')}")

# Node degrees
print(f"\nDegree of Alice: {g.get_degree('Alice')}")
print(f"Degree of Bob: {g.get_degree('Bob')}")
print(f"Degree of Frank: {g.get_degree('Frank')}")

# BFS traversal
print(f"\nBFS from Alice: {g.bfs('Alice')}")
print(f"DFS from Alice: {g.dfs('Alice')}")

# Add more connections
g.add_edge("Eve", "Frank")  # Connect the components
print("\nAfter connecting components:")
print(f"Has path from Alice to Frank? {g.has_path('Alice', 'Frank')}")

g.display()
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Using Mutable Objects as Keys

```python
# ❌ WRONG - Lists are mutable
d = {}
# d[[1, 2]] = "value"  # TypeError!

# ❌ WRONG - Dictionaries are mutable
# d[{"a": 1}] = "value"  # TypeError!

# ✅ CORRECT - Use tuples instead
d = {(1, 2): "value"}
print(d[(1, 2)])  # "value"

# ✅ CORRECT - Use frozenset for set keys
d = {frozenset([1, 2]): "value"}
print(d[frozenset([1, 2])])  # "value"
```

### Pitfall 2: KeyError When Accessing Missing Keys

```python
person = {"name": "Alice"}

# ❌ WRONG - Raises KeyError
# age = person["age"]

# ✅ CORRECT - Use get()
age = person.get("age", 0)
print(age)  # 0

# ✅ CORRECT - Check first
if "age" in person:
    age = person["age"]
else:
    age = 0

# ✅ CORRECT - Use try/except
try:
    age = person["age"]
except KeyError:
    age = 0
```

### Pitfall 3: Modifying Dictionary While Iterating

```python
# ❌ WRONG - Modifying during iteration
d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#     if key == "b":
#         del d[key]  # RuntimeError!

# ✅ CORRECT - Iterate over copy
d = {"a": 1, "b": 2, "c": 3}
for key in list(d.keys()):
    if key == "b":
        del d[key]
print(d)  # {'a': 1, 'c': 3}

# ✅ CORRECT - Use dictionary comprehension
d = {"a": 1, "b": 2, "c": 3}
d = {k: v for k, v in d.items() if k != "b"}
print(d)  # {'a': 1, 'c': 3}
```

### Pitfall 4: Shallow Copy with Nested Dictionaries

```python
original = {"a": 1, "b": {"c": 2}}

# ❌ WRONG - Shallow copy
shallow = original.copy()
shallow["b"]["c"] = 99
print(original)  # {'a': 1, 'b': {'c': 99}} (changed!)

# ✅ CORRECT - Deep copy
import copy
deep = copy.deepcopy(original)
deep["b"]["c"] = 100
print(original)  # {'a': 1, 'b': {'c': 99}} (unchanged)
```

---

## ⚡ Performance Tips

### Dictionary vs List Lookup

```python
import timeit

# Dictionary lookup is O(1) - very fast
d = {i: i**2 for i in range(10000)}
dict_time = timeit.timeit('d[5000]', globals=globals(), number=1000000)

# List lookup is O(n) - slower
lst = list(range(10000))
list_time = timeit.timeit('5000 in lst', globals=globals(), number=100000)

print(f"Dict lookup (1M ops): {dict_time:.4f}s")
print(f"List lookup (100K ops): {list_time:.4f}s")
```

### Use DefaultDict for Counting

```python
from collections import defaultdict

# ❌ SLOWER - Manual checking
counts = {}
items = [1, 2, 3, 2, 1, 1, 2, 3, 1]
for item in items:
    if item not in counts:
        counts[item] = 0
    counts[item] += 1

# ✅ FASTER - Using defaultdict
counts = defaultdict(int)
for item in items:
    counts[item] += 1

# ✅ FASTEST - Using Counter
from collections import Counter
counts = Counter(items)
```

### Use get() for Safe Access

```python
# ❌ SLOWER - Multiple lookups
if key in d:
    value = d[key]
else:
    value = default

# ✅ FASTER - Single lookup
value = d.get(key, default)
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Phone Directory**
   ```python
   # Create a phone directory (name -> number)
   # Add, find, delete contacts
   ```

2. **Word Counter**
   ```python
   # Count frequency of words in a sentence
   # Use dictionary to store word counts
   ```

3. **Gradebook**
   ```python
   # Store student grades (name -> list of grades)
   # Calculate average for each student
   ```

### Intermediate Level

4. **Inventory System**
   ```python
   # Track products (name -> {price, quantity})
   # Add, remove, update, search products
   ```

5. **Cache Implementation**
   ```python
   # Implement simple cache with expiration
   # Store computed results with timestamps
   ```

6. **Group By Function**
   ```python
   # Group list of items by a key function
   # Example: group people by age
   ```

### Advanced Level

7. **JSON Config Manager**
   ```python
   # Load/save configuration from JSON
   # Support nested keys with dot notation
   ```

8. **Graph Implementation**
   ```python
   # Implement graph using adjacency dictionary
   # BFS, DFS, shortest path algorithms
   ```

9. **LRU Cache**
   ```python
   # Implement Least Recently Used cache
   # O(1) get and put operations
   ```

---

## 📚 Quick Reference Card

```python
# Creation
d = {}                           # Empty dict
d = {"a": 1, "b": 2}            # With items
d = dict(a=1, b=2)              # From kwargs
d = dict([("a",1), ("b",2)])   # From pairs
d = dict(zip(keys, values))     # From two lists
d = {k: v for k, v in ...}      # Comprehension

# Access
d[key]                          # Get (KeyError if missing)
d.get(key, default)             # Safe get
d.setdefault(key, default)      # Get with default assignment

# Add/Update
d[key] = value                  # Add or update
d.update(other_dict)            # Merge
d1 | d2                         # Merge (3.9+)

# Remove
del d[key]                      # Delete key
d.pop(key)                      # Remove and return
d.popitem()                     # Remove last item
d.clear()                       # Remove all

# Views
d.keys()                        # Keys view
d.values()                      # Values view
d.items()                       # Items view

# Membership
key in d                        # Check key
value in d.values()             # Check value

# Looping
for key in d:                   # Loop keys
for value in d.values():        # Loop values
for k, v in d.items():          # Loop pairs (recommended)

# Length
len(d)                          # Number of items

# Copy
d.copy()                        # Shallow copy
copy.deepcopy(d)                # Deep copy
```

---

*Master dictionaries for fast, flexible key-value storage! 🐍✨*
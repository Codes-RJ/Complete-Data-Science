# 📘 LISTS (list) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Lists?](#what-are-lists)
2. [Creating Lists](#creating-lists)
3. [Accessing Elements](#accessing-elements)
4. [List Slicing](#list-slicing)
5. [All List Methods](#all-list-methods)
6. [List Operations](#list-operations)
7. [List Comprehensions](#list-comprehensions)
8. [Nested Lists](#nested-lists)
9. [Real-World Examples](#real-world-examples)
10. [Common Pitfalls](#common-pitfalls)
11. [Performance Tips](#performance-tips)
12. [Practice Exercises](#practice-exercises)

---

## 📖 What are Lists?

**Lists** are ordered, mutable collections that can hold items of any type. They are one of the most versatile and commonly used data structures in Python.

```python
# Examples of lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
empty = []
```

**Key Features:**
- ✅ Ordered (items maintain position)
- ✅ Mutable (can change, add, remove items)
- ✅ Heterogeneous (different types can mix)
- ✅ Dynamic (size can change)
- ✅ Indexable (access by position)
- ✅ Iterable (can loop through)
- ✅ Supports slicing

---

## 🎯 Creating Lists

### Method 1: Square Brackets

```python
# Empty list
empty = []

# List with items
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Method 2: `list()` Constructor

```python
# From string
print(list("hello"))     # ['h', 'e', 'l', 'l', 'o']

# From tuple
print(list((1, 2, 3)))   # [1, 2, 3]

# From range
print(list(range(5)))    # [0, 1, 2, 3, 4]

# From set
print(list({1, 2, 3}))   # [1, 2, 3] (order not guaranteed)

# From dictionary (keys only)
print(list({'a': 1, 'b': 2}))  # ['a', 'b']

# Empty list
empty = list()
```

### Method 3: List Comprehensions

```python
# Squares of numbers 0-9
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

### Method 4: Using `*` Operator

```python
# Repeat list
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

# Repeat nested list (be careful!)
matrix = [[0] * 3] * 3  # Creates references to same list!
print(matrix)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] (all rows changed!)

# Correct way for nested lists
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 🔍 Accessing Elements

### Indexing (Positive and Negative)

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0 to len-1)
print(fruits[0])   # "apple"
print(fruits[2])   # "cherry"
print(fruits[4])   # "elderberry"

# Negative indexing (-1 to -len)
print(fruits[-1])  # "elderberry" (last)
print(fruits[-2])  # "date"
print(fruits[-5])  # "apple" (first)

# IndexError if out of range
# print(fruits[10])  # IndexError!
```

### Slicing `[start:end:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:5])    # [2, 3, 4] (start inclusive, end exclusive)
print(numbers[:5])     # [0, 1, 2, 3, 4] (from start)
print(numbers[5:])     # [5, 6, 7, 8, 9] (to end)
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (full copy)

# With step
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (every 2nd starting at 1)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# Negative indices in slicing
print(numbers[-5:-2])  # [5, 6, 7]
print(numbers[-3:])    # [7, 8, 9]

# Slicing with out-of-range indices (safe)
print(numbers[2:100])  # [2, 3, 4, 5, 6, 7, 8, 9] (truncates)
print(numbers[100:])   # [] (empty list)
```

### Iterating Through Lists

```python
fruits = ["apple", "banana", "cherry"]

# Simple iteration
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# With index using range
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
# Output: 0: apple, 1: banana, 2: cherry

# With index using enumerate (recommended)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Output: 0: apple, 1: banana, 2: cherry

# With index starting from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
# Output: 1: apple, 2: banana, 3: cherry

# Reverse iteration
for fruit in reversed(fruits):
    print(fruit)
# Output: cherry, banana, apple

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## 📚 All List Methods

### Adding Elements

#### `append(x)`
Adds an item to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Appending different types
mixed = [1, 2]
mixed.append("hello")
mixed.append(True)
print(mixed)  # [1, 2, 'hello', True]

# Real use: Building list dynamically
numbers = []
for i in range(5):
    numbers.append(i**2)
print(numbers)  # [0, 1, 4, 9, 16]
```

#### `insert(i, x)`
Inserts an item at a given position.

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # ['apple', 'banana', 'cherry']

# Insert at beginning
fruits.insert(0, "date")
print(fruits)  # ['date', 'apple', 'banana', 'cherry']

# Insert at end (same as append)
fruits.insert(len(fruits), "elderberry")
print(fruits)  # ['date', 'apple', 'banana', 'cherry', 'elderberry']

# Insert with negative index
fruits.insert(-1, "fig")
print(fruits)  # ['date', 'apple', 'banana', 'cherry', 'fig', 'elderberry']
```

#### `extend(iterable)`
Extends the list by appending all items from the iterable.

```python
# Extend with list
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)  # [1, 2, 3, 4, 5, 6]

# Extend with tuple
a = [1, 2, 3]
a.extend((4, 5, 6))
print(a)  # [1, 2, 3, 4, 5, 6]

# Extend with string (adds each character)
a = ["a", "b"]
a.extend("cd")
print(a)  # ['a', 'b', 'c', 'd']

# Extend with range
a = [1, 2, 3]
a.extend(range(4, 7))
print(a)  # [1, 2, 3, 4, 5, 6]

# Real use: Combining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

# Difference between extend and append
a = [1, 2, 3]
a.append([4, 5])  # Adds as single element
print(a)  # [1, 2, 3, [4, 5]]

b = [1, 2, 3]
b.extend([4, 5])  # Adds each element
print(b)  # [1, 2, 3, 4, 5]
```

### Removing Elements

#### `remove(x)`
Removes the first occurrence of the specified value.

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana'] (removes first only)

# ValueError if item not found
try:
    fruits.remove("grape")
except ValueError:
    print("Item not found")

# Real use: Remove specific value
def remove_all(lst, value):
    while value in lst:
        lst.remove(value)
    return lst

numbers = [1, 2, 3, 2, 4, 2, 5]
remove_all(numbers, 2)
print(numbers)  # [1, 3, 4, 5]
```

#### `pop(i=-1)`
Removes and returns the item at the specified index (default last).

```python
fruits = ["apple", "banana", "cherry", "date"]

# Pop last item
popped = fruits.pop()
print(popped)   # "date"
print(fruits)   # ['apple', 'banana', 'cherry']

# Pop at specific index
popped = fruits.pop(1)
print(popped)   # "banana"
print(fruits)   # ['apple', 'cherry']

# Pop from empty list raises IndexError
empty = []
# empty.pop()  # IndexError!

# Real use: Implement stack (LIFO)
stack = []
stack.append(1)  # Push
stack.append(2)  # Push
stack.append(3)  # Push
print(stack.pop())  # 3 (Pop)
print(stack.pop())  # 2 (Pop)
print(stack)        # [1]

# Real use: Implement queue (FIFO) - not efficient for large lists
queue = [1, 2, 3]
front = queue.pop(0)  # Removes first element (O(n) operation)
print(front)  # 1
```

#### `clear()`
Removes all items from the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # []

# Alternative ways
numbers = [1, 2, 3]
numbers[:] = []  # Slice assignment
numbers = []     # Creates new list (doesn't modify original)

# Real use: Reset list for reuse
tasks = ["task1", "task2", "task3"]
# Process tasks...
tasks.clear()  # Ready for new tasks
```

### Modifying Elements

#### Direct Assignment

```python
fruits = ["apple", "banana", "cherry"]
fruits[0] = "date"
print(fruits)  # ['date', 'banana', 'cherry']

# Assign to slice
fruits[1:3] = ["elderberry", "fig"]
print(fruits)  # ['date', 'elderberry', 'fig']

# Replace slice with different length
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10, 20]  # Removes 2,3,4 and inserts 10,20
print(numbers)  # [1, 10, 20, 5]

# Delete slice
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []
print(numbers)  # [1, 5]
```

### Searching and Counting

#### `index(x[, start[, end]])`
Returns the index of the first occurrence of the specified value.

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

print(fruits.index("banana"))     # 1
print(fruits.index("banana", 2))  # 3 (search from index 2)
print(fruits.index("banana", 2, 4))  # 3 (search between 2 and 4)

# ValueError if not found
try:
    fruits.index("grape")
except ValueError:
    print("Not found")

# Real use: Find all positions
def find_all(lst, value):
    positions = []
    start = 0
    while True:
        try:
            pos = lst.index(value, start)
            positions.append(pos)
            start = pos + 1
        except ValueError:
            break
    return positions

numbers = [1, 2, 3, 2, 4, 2, 5]
print(find_all(numbers, 2))  # [1, 3, 5]
```

#### `count(x)`
Returns the number of occurrences of the specified value.

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers.count(2))   # 3
print(numbers.count(10))  # 0

# Real use: Find duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

def find_duplicates(lst):
    return {x for x in lst if lst.count(x) > 1}

numbers = [1, 2, 3, 2, 4, 2, 5, 3]
print(find_duplicates(numbers))  # {2, 3}
```

### Sorting and Reversing

#### `sort(key=None, reverse=False)`
Sorts the list in place (modifies original).

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# Ascending order
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# Sorting strings (lexicographic)
words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry', 'date']

# Sorting with key function
words.sort(key=len)  # Sort by length
print(words)  # ['date', 'apple', 'banana', 'cherry']

# Sort by second element of tuple
pairs = [(1, 5), (2, 3), (3, 1), (4, 2)]
pairs.sort(key=lambda x: x[1])  # Sort by second element
print(pairs)  # [(3, 1), (4, 2), (2, 3), (1, 5)]

# Sort with custom key (case-insensitive)
words = ["banana", "Apple", "cherry", "Date"]
words.sort(key=str.lower)
print(words)  # ['Apple', 'banana', 'cherry', 'Date']

# Sort with multiple criteria
students = [
    ('Alice', 85),
    ('Bob', 75),
    ('Charlie', 85),
    ('David', 75)
]
students.sort(key=lambda x: (x[1], x[0]))  # Sort by grade, then name
print(students)  # [('Bob', 75), ('David', 75), ('Alice', 85), ('Charlie', 85)]
```

#### `reverse()`
Reverses the order of the list in place.

```python
fruits = ["apple", "banana", "cherry", "date"]
fruits.reverse()
print(fruits)  # ['date', 'cherry', 'banana', 'apple']

# Alternative using slicing (creates new list)
fruits = ["apple", "banana", "cherry", "date"]
reversed_fruits = fruits[::-1]
print(reversed_fruits)  # ['date', 'cherry', 'banana', 'apple']
print(fruits)  # Original unchanged

# Real use: Palindrome check
def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))  # True
print(is_palindrome([1, 2, 3, 4, 5]))  # False
```

### Copying

#### `copy()`
Returns a shallow copy of the list.

```python
original = [1, 2, 3]
shallow_copy = original.copy()

print(shallow_copy)  # [1, 2, 3]
print(original is shallow_copy)  # False (different objects)

# Alternative ways to copy
copy1 = original[:]        # Slice copy
copy2 = list(original)     # Constructor
copy3 = original.copy()    # Copy method

# Shallow copy with nested lists (creates new outer list, but inner lists are shared)
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] (original changed!)

# Deep copy for nested structures
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]] (original unchanged)
```

---

## ⚡ List Operations

### Concatenation (`+`)

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]

# Creates new list (doesn't modify original)
print(a)  # [1, 2, 3] (unchanged)
print(b)  # [4, 5, 6] (unchanged)
```

### Repetition (`*`)

```python
a = [1, 2]
b = a * 3
print(b)  # [1, 2, 1, 2, 1, 2]

# Creates new list
print(a)  # [1, 2] (unchanged)
```

### Membership (`in`, `not in`)

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)     # True
print("grape" in fruits)      # False
print("apple" not in fruits)  # False

# Real use: Check before operation
if "banana" in fruits:
    fruits.remove("banana")
```

### Comparison Operators

```python
# Lexicographic comparison
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 4]

print(a == b)  # True
print(a == c)  # False
print(a < c)   # True (compares element by element)

# Works with strings
words1 = ["apple", "banana"]
words2 = ["apple", "cherry"]
print(words1 < words2)  # True ("banana" < "cherry")
```

### Built-in Functions with Lists

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

print(len(numbers))      # 7 (number of elements)
print(max(numbers))      # 9 (maximum value)
print(min(numbers))      # 1 (minimum value)
print(sum(numbers))      # 25 (sum of all elements)
print(sorted(numbers))   # [1, 1, 2, 3, 4, 5, 9] (new sorted list)
print(reversed(numbers)) # <list_reverseiterator> (use list() to see)
print(list(reversed(numbers)))  # [2, 9, 5, 1, 4, 1, 3]

# any() and all()
bool_list = [True, False, True]
print(any(bool_list))  # True (at least one True)
print(all(bool_list))  # False (not all True)

# zip() - combine lists
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
pairs = list(zip(names, ages))
print(pairs)  # [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
```

---

## 🔄 List Comprehensions

### Basic Syntax

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (same result)
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With Condition

```python
# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Numbers greater than 5
filtered = [x for x in range(10) if x > 5]
print(filtered)  # [6, 7, 8, 9]
```

### With If-Else

```python
# Replace odd numbers with -1
result = [x if x % 2 == 0 else -1 for x in range(10)]
print(result)  # [0, -1, 2, -1, 4, -1, 6, -1, 8, -1]
```

### Nested Comprehensions

```python
# Flatten matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create matrix
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Cartesian product
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = [(c, s) for c in colors for s in sizes]
print(products)  # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

### Real-World Examples

```python
# Extract first letters
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)  # ['a', 'b', 'c']

# Filter strings by length
words = ["a", "ab", "abc", "abcd", "abcde"]
long_words = [word for word in words if len(word) >= 3]
print(long_words)  # ['abc', 'abcd', 'abcde']

# Convert list of strings to integers
str_nums = ["1", "2", "3", "4", "5"]
int_nums = [int(s) for s in str_nums]
print(int_nums)  # [1, 2, 3, 4, 5]

# Remove duplicates while preserving order
def unique_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

numbers = [1, 2, 3, 2, 4, 3, 5]
print(unique_preserve_order(numbers))  # [1, 2, 3, 4, 5]
```

---

## 🪆 Nested Lists

### Creating Nested Lists

```python
# 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0])      # [1, 2, 3]
print(matrix[0][0])   # 1
print(matrix[1][2])   # 6
print(matrix[2][1])   # 8

# Modifying elements
matrix[1][1] = 99
print(matrix)  # [[1, 2, 3], [4, 99, 6], [7, 8, 9]]

# Iterating through nested lists
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# Output:
# 1 2 3
# 4 99 6
# 7 8 9

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

### Operations on Nested Lists

```python
# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Sum of all elements
total = sum(sum(row) for row in matrix)
print(total)  # 45

# Maximum element
max_val = max(max(row) for row in matrix)
print(max_val)  # 9

# Flatten nested list
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

deep_nested = [1, [2, 3], [4, [5, 6]], 7]
print(flatten(deep_nested))  # [1, 2, 3, 4, 5, 6, 7]
```

---

## 🌍 Real-World Examples

### Example 1: Todo List Manager

```python
class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed = []
    
    def add_task(self, task):
        """Add a new task"""
        self.tasks.append(task)
        print(f"✅ Added: {task}")
    
    def remove_task(self, index):
        """Remove task by index"""
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"❌ Removed: {removed}")
        else:
            print("Invalid task number")
    
    def complete_task(self, index):
        """Mark task as completed"""
        if 0 <= index < len(self.tasks):
            completed_task = self.tasks.pop(index)
            self.completed.append(completed_task)
            print(f"🎉 Completed: {completed_task}")
        else:
            print("Invalid task number")
    
    def show_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No pending tasks!")
            return
        
        print("\n📋 PENDING TASKS:")
        print("-" * 30)
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")
        print("-" * 30)
    
    def show_completed(self):
        """Display completed tasks"""
        if not self.completed:
            print("No completed tasks yet!")
            return
        
        print("\n✅ COMPLETED TASKS:")
        print("-" * 30)
        for i, task in enumerate(self.completed):
            print(f"{i+1}. {task}")
        print("-" * 30)
    
    def clear_all(self):
        """Clear all tasks"""
        confirm = input("Clear all tasks? (yes/no): ")
        if confirm.lower() == "yes":
            self.tasks.clear()
            self.completed.clear()
            print("All tasks cleared!")

# Usage
todo = TodoList()

# Add tasks
todo.add_task("Buy groceries")
todo.add_task("Write Python code")
todo.add_task("Exercise")
todo.add_task("Read book")

# Show tasks
todo.show_tasks()

# Complete a task
todo.complete_task(1)  # Complete "Write Python code"

# Show updated lists
todo.show_tasks()
todo.show_completed()

# Remove a task
todo.remove_task(0)  # Remove first task

todo.show_tasks()
```

### Example 2: Student Grade Manager

```python
class GradeManager:
    def __init__(self):
        self.students = []
        self.grades = []
    
    def add_student(self, name, *scores):
        """Add student with scores"""
        self.students.append(name)
        self.grades.append(list(scores))
        print(f"Added {name} with scores: {scores}")
    
    def add_score(self, name, score):
        """Add score for existing student"""
        if name in self.students:
            index = self.students.index(name)
            self.grades[index].append(score)
            print(f"Added {score} to {name}")
        else:
            print(f"Student {name} not found")
    
    def calculate_average(self, name):
        """Calculate average for a student"""
        if name in self.students:
            index = self.students.index(name)
            scores = self.grades[index]
            if scores:
                avg = sum(scores) / len(scores)
                return round(avg, 2)
            return 0
        return None
    
    def get_class_average(self):
        """Calculate class average"""
        all_scores = [score for student_grades in self.grades for score in student_grades]
        if all_scores:
            return round(sum(all_scores) / len(all_scores), 2)
        return 0
    
    def get_top_students(self, n=3):
        """Get top n students by average"""
        averages = []
        for i, student in enumerate(self.students):
            avg = self.calculate_average(student)
            averages.append((student, avg))
        
        averages.sort(key=lambda x: x[1], reverse=True)
        return averages[:n]
    
    def get_failing_students(self, passing_grade=60):
        """Get students with average below passing grade"""
        failing = []
        for i, student in enumerate(self.students):
            avg = self.calculate_average(student)
            if avg and avg < passing_grade:
                failing.append((student, avg))
        return failing
    
    def generate_report(self):
        """Generate complete grade report"""
        print("=" * 60)
        print("STUDENT GRADE REPORT")
        print("=" * 60)
        
        for i, student in enumerate(self.students):
            scores = self.grades[i]
            avg = self.calculate_average(student)
            letter = self._get_letter_grade(avg)
            
            print(f"\n📚 {student}")
            print(f"   Scores: {scores}")
            print(f"   Average: {avg}")
            print(f"   Grade: {letter}")
        
        print("\n" + "-" * 60)
        print(f"Class Average: {self.get_class_average()}")
        
        top = self.get_top_students(3)
        print(f"\n🏆 Top Students:")
        for i, (name, avg) in enumerate(top, 1):
            print(f"   {i}. {name} - {avg}")
        
        failing = self.get_failing_students()
        if failing:
            print(f"\n⚠️ Failing Students:")
            for name, avg in failing:
                print(f"   {name} - {avg}")
        
        print("=" * 60)
    
    def _get_letter_grade(self, avg):
        """Convert numeric average to letter grade"""
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

# Usage
manager = GradeManager()

# Add students
manager.add_student("Alice", 85, 90, 88, 92)
manager.add_student("Bob", 75, 80, 78)
manager.add_student("Charlie", 65, 70, 68, 72)
manager.add_student("Diana", 95, 98, 92, 96)

# Add more scores
manager.add_score("Bob", 82)
manager.add_score("Charlie", 75)

# Generate report
manager.generate_report()
```

### Example 3: Shopping Cart System

```python
class ShoppingCart:
    def __init__(self):
        self.items = []  # List of (product, price, quantity)
    
    def add_item(self, product, price, quantity=1):
        """Add item to cart"""
        self.items.append([product, price, quantity])
        print(f"Added {quantity}x {product} (${price:.2f} each)")
    
    def remove_item(self, product):
        """Remove all occurrences of product"""
        removed = 0
        self.items = [item for item in self.items if item[0] != product]
        print(f"Removed all {product}")
    
    def update_quantity(self, product, quantity):
        """Update quantity of product"""
        for item in self.items:
            if item[0] == product:
                item[2] = quantity
                print(f"Updated {product} quantity to {quantity}")
                return
        print(f"{product} not found in cart")
    
    def calculate_total(self):
        """Calculate total price"""
        total = sum(item[1] * item[2] for item in self.items)
        return round(total, 2)
    
    def apply_discount(self, percentage):
        """Apply percentage discount to total"""
        total = self.calculate_total()
        discount = total * (percentage / 100)
        new_total = total - discount
        return round(new_total, 2)
    
    def get_summary(self):
        """Get cart summary"""
        if not self.items:
            return "Cart is empty"
        
        summary = []
        summary.append("=" * 50)
        summary.append("SHOPPING CART")
        summary.append("=" * 50)
        summary.append(f"{'Product':<20} {'Price':<10} {'Qty':<5} {'Total':<10}")
        summary.append("-" * 50)
        
        for product, price, qty in self.items:
            total = price * qty
            summary.append(f"{product:<20} ${price:<9.2f} {qty:<5} ${total:<9.2f}")
        
        summary.append("-" * 50)
        summary.append(f"{'TOTAL':<20} {'':<10} {'':<5} ${self.calculate_total():<9.2f}")
        summary.append("=" * 50)
        
        return "\n".join(summary)
    
    def clear_cart(self):
        """Clear all items"""
        self.items.clear()
        print("Cart cleared")

# Usage
cart = ShoppingCart()

# Add items
cart.add_item("Laptop", 999.99, 1)
cart.add_item("Mouse", 29.99, 2)
cart.add_item("Keyboard", 79.99, 1)
cart.add_item("USB Cable", 9.99, 3)

# Show cart
print(cart.get_summary())

# Update quantity
cart.update_quantity("Mouse", 3)

# Apply discount
print(f"\nTotal with 10% discount: ${cart.apply_discount(10):.2f}")

# Remove item
cart.remove_item("USB Cable")

# Show final cart
print(cart.get_summary())
```

### Example 4: Stack Implementation

```python
class Stack:
    """Stack implementation using list (LIFO)"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped: {item}")
            return item
        print("Stack is empty!")
        return None
    
    def peek(self):
        """Return top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return stack size"""
        return len(self.items)
    
    def clear(self):
        """Clear all items"""
        self.items.clear()
        print("Stack cleared")
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.items):
                print(f"  {item}")

# Example: Undo/Redo system
class Editor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()
    
    def write(self, text):
        """Write text (push to undo stack)"""
        self.undo_stack.push(self.text)
        self.text += text
        self.redo_stack.clear()
        print(f"Current text: '{self.text}'")
    
    def undo(self):
        """Undo last action"""
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.text)
            self.text = self.undo_stack.pop()
            print(f"Undo: '{self.text}'")
        else:
            print("Nothing to undo")
    
    def redo(self):
        """Redo last undone action"""
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.text)
            self.text = self.redo_stack.pop()
            print(f"Redo: '{self.text}'")
        else:
            print("Nothing to redo")

# Test editor
editor = Editor()
editor.write("Hello ")
editor.write("World")
editor.undo()
editor.redo()
editor.write("!")
editor.undo()
editor.undo()
```

### Example 5: Queue Implementation

```python
from collections import deque

class Queue:
    """Queue implementation using collections.deque (FIFO)"""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to end of queue"""
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            item = self.items.popleft()
            print(f"Dequeued: {item}")
            return item
        print("Queue is empty!")
        return None
    
    def front(self):
        """Return front item without removing"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def rear(self):
        """Return rear item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return queue size"""
        return len(self.items)
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front to rear):")
            for item in self.items:
                print(f"  {item}")

# Example: Print Queue
class PrintQueue:
    def __init__(self):
        self.queue = Queue()
        self.printed = []
    
    def submit_job(self, document, pages):
        """Submit print job"""
        job = {'document': document, 'pages': pages}
        self.queue.enqueue(job)
        print(f"Submitted: {document} ({pages} pages)")
    
    def process_job(self):
        """Process next print job"""
        if not self.queue.is_empty():
            job = self.queue.dequeue()
            print(f"Printing: {job['document']}...")
            self.printed.append(job)
            return job
        print("No jobs to process")
        return None
    
    def show_queue(self):
        """Show pending jobs"""
        print(f"\nPending jobs: {self.queue.size()}")
        self.queue.display()
    
    def show_history(self):
        """Show printed jobs"""
        print("\nPrinted jobs:")
        for job in self.printed:
            print(f"  {job['document']} ({job['pages']} pages)")

# Test print queue
printer = PrintQueue()
printer.submit_job("Resume.pdf", 2)
printer.submit_job("Report.docx", 10)
printer.submit_job("Photo.jpg", 1)
printer.show_queue()
printer.process_job()
printer.process_job()
printer.show_queue()
printer.show_history()
```

### Example 6: Matrix Operations

```python
class Matrix:
    def __init__(self, data):
        """Initialize matrix with 2D list"""
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __str__(self):
        """String representation of matrix"""
        result = []
        for row in self.data:
            result.append("  ".join(f"{val:4}" for val in row))
        return "\n".join(result)
    
    def add(self, other):
        """Matrix addition"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    
    def subtract(self, other):
        """Matrix subtraction"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    
    def multiply(self, other):
        """Matrix multiplication"""
        if self.cols != other.rows:
            raise ValueError("Number of columns of first must equal rows of second")
        
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
             for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    
    def transpose(self):
        """Matrix transpose"""
        result = [
            [self.data[i][j] for i in range(self.rows)]
            for j in range(self.cols)
        ]
        return Matrix(result)
    
    def determinant(self):
        """Calculate determinant (for 2x2 and 3x3)"""
        if self.rows != self.cols:
            raise ValueError("Determinant only for square matrices")
        
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        elif self.rows == 3:
            a, b, c = self.data[0]
            d, e, f = self.data[1]
            g, h, i = self.data[2]
            return (a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h)
        else:
            raise ValueError("Determinant only for 2x2 and 3x3 matrices")
    
    def scalar_multiply(self, scalar):
        """Multiply matrix by scalar"""
        result = [
            [val * scalar for val in row]
            for row in self.data
        ]
        return Matrix(result)

# Usage
print("MATRIX OPERATIONS")
print("=" * 40)

# Create matrices
A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Addition
print("\nA + B:")
print(A.add(B))

# Subtraction
print("\nA - B:")
print(A.subtract(B))

# Transpose
print("\nTranspose of A:")
print(A.transpose())

# Scalar multiplication
print("\nA * 2:")
print(A.scalar_multiply(2))

# Determinant
C = Matrix([[1, 2], [3, 4]])
print(f"\nDeterminant of [[1,2],[3,4]] = {C.determinant()}")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Modifying List While Iterating

```python
# ❌ WRONG - Skipping elements
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)  # [1, 3, 5] - Works here but risky!

# ❌ WRONG - Index shift issues
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers.pop(i)  # IndexError or wrong removal!
print(numbers)

# ✅ CORRECT - Iterate over copy
numbers = [1, 2, 3, 4, 5]
for i in numbers[:]:
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)  # [1, 3, 5]

# ✅ CORRECT - Use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [i for i in numbers if i % 2 != 0]
print(numbers)  # [1, 3, 5]

# ✅ CORRECT - Iterate backwards
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
print(numbers)  # [1, 3, 5]
```

### Pitfall 2: Copying Lists (Shallow vs Deep)

```python
# ❌ WRONG - Just creates reference
original = [1, 2, 3]
copy = original
copy[0] = 99
print(original)  # [99, 2, 3] (original changed!)

# ✅ CORRECT - Shallow copy
original = [1, 2, 3]
copy = original.copy()
copy[0] = 99
print(original)  # [1, 2, 3] (unchanged)
print(copy)      # [99, 2, 3]

# ⚠️ Shallow copy with nested lists
original = [[1, 2], [3, 4]]
copy = original.copy()
copy[0][0] = 99
print(original)  # [[99, 2], [3, 4]] (nested list changed!)

# ✅ CORRECT - Deep copy for nested structures
import copy
original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 99
print(original)   # [[1, 2], [3, 4]] (unchanged)
print(deep_copy)  # [[99, 2], [3, 4]]
```

### Pitfall 3: Using Mutable Default Arguments

```python
# ❌ WRONG - Mutable default persists
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] (unexpected!)

# ✅ CORRECT - Use None as default
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [2] (correct)
```

### Pitfall 4: List Multiplication with Mutable Objects

```python
# ❌ WRONG - All rows reference same list
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] (all changed!)

# ✅ CORRECT - Create independent rows
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### Pitfall 5: Index Errors

```python
fruits = ["apple", "banana", "cherry"]

# ❌ WRONG - Index out of range
# print(fruits[3])  # IndexError!

# ✅ CORRECT - Check length first
if len(fruits) > 3:
    print(fruits[3])
else:
    print("Index out of range")

# ✅ CORRECT - Use try/except
try:
    print(fruits[3])
except IndexError:
    print("Index out of range")
```

---

## ⚡ Performance Tips

### List vs Other Data Structures

```python
import timeit

# Membership testing
haystack_list = list(range(10000))
haystack_set = set(range(10000))

list_time = timeit.timeit('5000 in haystack_list', globals=globals(), number=10000)
set_time = timeit.timeit('5000 in haystack_set', globals=globals(), number=10000)

print(f"List membership: {list_time:.4f}s")
print(f"Set membership: {set_time:.4f}s")
# Set is MUCH faster for 'in' operations!
```

### Efficient List Operations

```python
# ❌ SLOW - Repeated concatenation
result = []
for i in range(1000):
    result = result + [i]  # Creates new list each time

# ✅ FAST - Using append
result = []
for i in range(1000):
    result.append(i)

# ✅ FASTEST - List comprehension
result = [i for i in range(1000)]

# ❌ SLOW - Using pop(0) for queue
queue = list(range(1000))
for _ in range(1000):
    item = queue.pop(0)  # O(n) operation

# ✅ FAST - Use deque from collections
from collections import deque
queue = deque(range(1000))
for _ in range(1000):
    item = queue.popleft()  # O(1) operation
```

### Preallocate List Size

```python
# ❌ SLOW - Growing list dynamically
result = []
for i in range(10000):
    result.append(i)

# ✅ FASTER - Preallocate with known size
result = [0] * 10000
for i in range(10000):
    result[i] = i
```

---

## 📝 Practice Exercises

### Beginner Level

1. **List Reversal**
   ```python
   # Write a function to reverse a list without using [::-1]
   # Example: [1,2,3,4] → [4,3,2,1]
   ```

2. **Find Maximum and Minimum**
   ```python
   # Find max and min without using built-in functions
   # Example: [3,1,4,1,5] → max=5, min=1
   ```

3. **Remove Duplicates**
   ```python
   # Remove duplicates while preserving order
   # Example: [1,2,3,2,4,3,5] → [1,2,3,4,5]
   ```

### Intermediate Level

4. **Rotate List**
   ```python
   # Rotate list by k positions
   # Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]
   ```

5. **Merge Sorted Lists**
   ```python
   # Merge two sorted lists into one sorted list
   # Example: [1,3,5] + [2,4,6] → [1,2,3,4,5,6]
   ```

6. **Find Pairs with Sum**
   ```python
   # Find all pairs that sum to target
   # Example: [1,2,3,4,5], target=5 → [(1,4), (2,3)]
   ```

### Advanced Level

7. **Longest Consecutive Sequence**
   ```python
   # Find longest consecutive sequence in unsorted list
   # Example: [100,4,200,1,3,2] → [1,2,3,4] (length 4)
   ```

8. **Product of Array Except Self**
   ```python
   # Return list where each element is product of all other elements
   # Example: [1,2,3,4] → [24,12,8,6]
   ```

9. **Spiral Matrix**
   ```python
   # Traverse matrix in spiral order
   # Example: [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]
   ```

---

## 📚 Quick Reference Card

```python
# Creation
lst = []                    # Empty list
lst = [1, 2, 3]            # With values
lst = list(range(5))       # From iterable

# Adding
lst.append(x)              # Add to end
lst.insert(i, x)           # Insert at index
lst.extend(iterable)       # Add multiple

# Removing
lst.remove(x)              # Remove first occurrence
lst.pop()                  # Remove and return last
lst.pop(i)                 # Remove and return at index
lst.clear()                # Remove all

# Accessing
lst[i]                     # Get item
lst[i] = x                 # Set item
lst[i:j]                   # Slice

# Searching
lst.index(x)               # Find index
lst.count(x)               # Count occurrences
x in lst                   # Check membership

# Sorting
lst.sort()                 # Sort in place
lst.sort(reverse=True)     # Sort descending
lst.sort(key=func)         # Sort with key
sorted(lst)                # Return new sorted list

# Other
lst.reverse()              # Reverse in place
len(lst)                   # Get length
lst.copy()                 # Shallow copy
max(lst), min(lst)         # Min/max
sum(lst)                   # Sum of elements
```

---

*Master lists to handle collections of data efficiently! 🐍✨*
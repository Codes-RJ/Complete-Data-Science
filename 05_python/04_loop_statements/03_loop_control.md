# 📘 LOOP CONTROL – BREAK, CONTINUE, ELSE

## 📌 Table of Contents
1. [Introduction to Loop Control](#introduction-to-loop-control)
2. [The `break` Statement](#the-break-statement)
3. [The `continue` Statement](#the-continue-statement)
4. [The `else` Clause in Loops](#the-else-clause-in-loops)
5. [Combining Control Statements](#combining-control-statements)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

---

## Introduction to Loop Control

Python provides three statements to control loop execution:

| Statement | Effect | Use Case |
|-----------|--------|----------|
| `break` | Exits the loop completely | Found what you're looking for |
| `continue` | Skips to next iteration | Skip invalid/undesired items |
| `else` | Executes if loop completes without `break` | Search with fallback |

```python
# break - exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)  # 0,1,2,3,4

# continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0,1,3,4

# else - runs if no break
for i in range(5):
    print(i)
else:
    print("Loop completed")  # Runs
```

---

## The `break` Statement

`break` immediately exits the loop, skipping any remaining iterations.

### Basic break

```python
# Break in for loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Break in while loop
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1  # 0,1,2,3,4

# Break in infinite loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

### Searching with break

```python
# Find first occurrence
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 40

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")

# Output:
# Checking 10...
# Checking 20...
# Checking 30...
# Found 40!

# Find first even number
numbers = [3, 5, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
# Output: First even number: 8
```

### break in Nested Loops

```python
# break only exits the innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=1, j=0
# i=2, j=0

# To break out of multiple loops, use a flag
found = False
for i in range(5):
    for j in range(5):
        if i == 2 and j == 3:
            found = True
            break
        print(f"({i},{j})", end=" ")
    if found:
        break
    print()
# Output: (0,0) (0,1) (0,2) (0,3) (0,4) (1,0) (1,1) (1,2) (1,3) (1,4)
```

---

## The `continue` Statement

`continue` skips the rest of the current iteration and moves to the next one.

### Basic continue

```python
# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# Skip vowels
text = "Hello World"
for char in text:
    if char.lower() in 'aeiou':
        continue
    print(char, end='')  # Hll Wrld
print()

# Skip negative numbers
numbers = [10, -5, 20, -3, 30, -1, 40]
positive_sum = 0
for num in numbers:
    if num < 0:
        continue
    positive_sum += num
print(f"Sum of positives: {positive_sum}")  # 100
```

### continue in while Loop

```python
# Skip even numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# Process only valid inputs
valid_inputs = []
while len(valid_inputs) < 3:
    user_input = input(f"Enter input {len(valid_inputs)+1}: ")
    if not user_input.strip():
        print("Input cannot be empty. Try again.")
        continue
    valid_inputs.append(user_input)
print(f"Valid inputs: {valid_inputs}")
```

---

## The `else` Clause in Loops

The `else` block executes when the loop completes normally (without encountering a `break`).

### Basic else

```python
# For loop with else (no break)
for i in range(5):
    print(i)
else:
    print("Loop completed without break")
# Output: 0,1,2,3,4, Loop completed without break

# For loop with else (with break)
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")
# Output: 0,1,2

# While loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed")
```

### Search Pattern with else

```python
# Search with else (not found case)
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")

find_item([1, 2, 3, 4, 5], 3)  # Found 3
find_item([1, 2, 3, 4, 5], 7)  # 7 not found

# Check if all numbers are even
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print("Not all numbers are even")
        break
else:
    print("All numbers are even")  # Prints

numbers = [2, 4, 5, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print("Not all numbers are even")
        break
else:
    print("All numbers are even")  # Doesn't print
```

### Prime Number Checker

```python
def is_prime(n):
    """Check if number is prime using for-else"""
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}")
            break
    else:
        print(f"{n} is prime")
        return True
    return False

is_prime(17)  # 17 is prime
is_prime(20)  # 20 is divisible by 2
is_prime(97)  # 97 is prime
```

---

## Combining Control Statements

### break and continue Together

```python
# Process numbers, skip negatives, stop at zero
numbers = [5, -2, 8, -1, 0, 7, 3]
for num in numbers:
    if num == 0:
        print("Found zero, stopping")
        break
    if num < 0:
        print(f"Skipping negative: {num}")
        continue
    print(f"Processing: {num}")
# Output:
# Processing: 5
# Skipping negative: -2
# Processing: 8
# Skipping negative: -1
# Found zero, stopping

# Find first positive even number
numbers = [-5, -2, 3, 7, 8, 10, -1]
for num in numbers:
    if num <= 0:
        continue
    if num % 2 == 0:
        print(f"First positive even: {num}")
        break
else:
    print("No positive even number found")
# Output: First positive even: 8
```

### Nested Loop Control

```python
# Break inner loop, continue outer
for i in range(3):
    print(f"Outer {i}")
    for j in range(5):
        if j == 2:
            break
        print(f"  Inner {j}")
# Output:
# Outer 0
#   Inner 0
#   Inner 1
# Outer 1
#   Inner 0
#   Inner 1
# Outer 2
#   Inner 0
#   Inner 1

# Skip inner loop entirely
for i in range(3):
    if i == 1:
        continue
    print(f"Outer {i}")
    for j in range(3):
        print(f"  Inner {j}")
# Output:
# Outer 0
#   Inner 0
#   Inner 1
#   Inner 2
# Outer 2
#   Inner 0
#   Inner 1
#   Inner 2
```

---

## Real-World Examples

### Example 1: Search in List of Dictionaries

```python
def find_user(users, user_id):
    """Find user by ID using for-else pattern"""
    for user in users:
        if user['id'] == user_id:
            print(f"Found user: {user['name']}")
            return user
    else:
        print(f"User with ID {user_id} not found")
        return None

# Sample data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

# Search
user = find_user(users, 2)  # Found user: Bob
user = find_user(users, 5)  # User with ID 5 not found
```

### Example 2: Input Validation with Max Attempts

```python
def get_valid_age(max_attempts=3):
    """Get valid age with retry limit"""
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        try:
            age = int(input(f"Attempt {attempts}/{max_attempts} - Enter age: "))
            if 1 <= age <= 120:
                print(f"Age {age} accepted")
                return age
            else:
                print("Age must be between 1 and 120")
        except ValueError:
            print("Please enter a valid number")
        
        if attempts == max_attempts:
            print(f"Max attempts ({max_attempts}) reached. Using default age 18.")
            return 18
        
        continue

# Usage
age = get_valid_age()
print(f"Final age: {age}")
```

### Example 3: Data Cleaner with Skip

```python
class DataCleaner:
    @staticmethod
    def clean_numbers(numbers):
        """Remove None, skip negatives, stop at zero"""
        cleaned = []
        
        for num in numbers:
            if num is None:
                print("Skipping None")
                continue
            if num < 0:
                print(f"Skipping negative: {num}")
                continue
            if num == 0:
                print("Found zero, stopping")
                break
            cleaned.append(num)
        
        return cleaned
    
    @staticmethod
    def clean_strings(strings):
        """Remove empty strings and strip whitespace"""
        cleaned = []
        
        for s in strings:
            if s is None:
                continue
            s = s.strip()
            if not s:
                continue
            cleaned.append(s)
        
        return cleaned
    
    @staticmethod
    def clean_dictionary(data, required_keys):
        """Filter dictionary to only include required keys"""
        cleaned = {}
        
        for key in required_keys:
            if key in data:
                cleaned[key] = data[key]
            else:
                print(f"Warning: Missing key '{key}'")
        
        return cleaned

# Usage
numbers = [5, -2, None, 8, 0, 7, -1, 10]
cleaned = DataCleaner.clean_numbers(numbers)
print(f"Cleaned numbers: {cleaned}")
# Output: Cleaning... Cleaned numbers: [5, 8]

strings = ["  hello  ", "", None, "  world  ", "  ", "python"]
cleaned = DataCleaner.clean_strings(strings)
print(f"Cleaned strings: {cleaned}")
# Output: Cleaned strings: ['hello', 'world', 'python']

data = {"name": "Alice", "age": 30, "temp": "value"}
required = ["name", "age", "email"]
cleaned = DataCleaner.clean_dictionary(data, required)
print(f"Cleaned dict: {cleaned}")
# Output: Warning: Missing key 'email', Cleaned dict: {'name': 'Alice', 'age': 30}
```

### Example 4: Menu System with Break

```python
class MenuApp:
    def __init__(self):
        self.items = []
    
    def display_menu(self):
        print("\n" + "=" * 40)
        print("MAIN MENU")
        print("=" * 40)
        print("1. Add item")
        print("2. View items")
        print("3. Search item")
        print("4. Delete item")
        print("5. Exit")
        print("=" * 40)
    
    def add_item(self):
        while True:
            item = input("Enter item (or 'cancel' to abort): ").strip()
            if item.lower() == 'cancel':
                print("Operation cancelled")
                return
            if not item:
                print("Item cannot be empty. Try again.")
                continue
            self.items.append(item)
            print(f"Added: {item}")
            break
    
    def view_items(self):
        if not self.items:
            print("No items found")
            return
        
        print("\nCurrent items:")
        for i, item in enumerate(self.items, 1):
            print(f"  {i}. {item}")
        print(f"Total: {len(self.items)} items")
    
    def search_item(self):
        if not self.items:
            print("No items to search")
            return
        
        search_term = input("Enter search term: ").lower()
        results = []
        
        for item in self.items:
            if search_term in item.lower():
                results.append(item)
        
        if results:
            print(f"\nFound {len(results)} item(s):")
            for item in results:
                print(f"  - {item}")
        else:
            print("No matching items found")
    
    def delete_item(self):
        if not self.items:
            print("No items to delete")
            return
        
        self.view_items()
        while True:
            try:
                choice = input("Enter item number to delete (or 'cancel'): ")
                if choice.lower() == 'cancel':
                    print("Operation cancelled")
                    return
                
                index = int(choice) - 1
                if 0 <= index < len(self.items):
                    removed = self.items.pop(index)
                    print(f"Deleted: {removed}")
                    break
                else:
                    print("Invalid item number")
            except ValueError:
                print("Please enter a valid number")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.view_items()
            elif choice == '3':
                self.search_item()
            elif choice == '4':
                self.delete_item()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

# Usage
app = MenuApp()
# app.run()  # Uncomment to run
```

### Example 5: File Processing with Break/Continue

```python
class FileProcessor:
    @staticmethod
    def read_until_empty(filename):
        """Read file until empty line found"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip() == '':
                        print("Empty line found, stopping")
                        break
                    print(f"Processing: {line.strip()}")
                else:
                    print("End of file reached, no empty line found")
        except FileNotFoundError:
            print(f"File {filename} not found")
    
    @staticmethod
    def skip_comments(filename):
        """Read file skipping comment lines"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip().startswith('#'):
                        print(f"Skipping comment: {line.strip()}")
                        continue
                    print(f"Data: {line.strip()}")
        except FileNotFoundError:
            print(f"File {filename} not found")
    
    @staticmethod
    def process_log_file(filename):
        """Process log file, stop on error, skip warnings"""
        errors = []
        
        try:
            with open(filename, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if '[ERROR]' in line:
                        errors.append((line_num, line))
                        print(f"ERROR found at line {line_num}, stopping")
                        break
                    
                    if '[WARNING]' in line:
                        print(f"Skipping warning at line {line_num}")
                        continue
                    
                    print(f"Processing: {line}")
                
                else:
                    print(f"No errors found. Total warnings: {len(errors)}")
        
        except FileNotFoundError:
            print(f"File {filename} not found")
        
        return errors

# Create sample file
sample_content = """[INFO] Server started
[WARNING] High memory usage
[INFO] User logged in
[ERROR] Database connection failed
[INFO] Server shutdown
"""

with open('sample.log', 'w') as f:
    f.write(sample_content)

# Process the file
processor = FileProcessor()
print("Reading until empty line:")
processor.read_until_empty('sample.log')

print("\nSkipping comments:")
processor.skip_comments('sample.log')

print("\nProcessing log file:")
errors = processor.process_log_file('sample.log')
print(f"Errors found: {errors}")

# Clean up
import os
os.remove('sample.log')
```

---

## Common Pitfalls

### Pitfall 1: break in Wrong Loop

```python
# break only breaks the innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"({i},{j})")
# Output: (0,0) (1,0) (2,0)

# Use flag to break outer loop
found = False
for i in range(3):
    if found:
        break
    for j in range(3):
        if j == 1:
            found = True
            break
        print(f"({i},{j})")
```

### Pitfall 2: continue Skipping Update

```python
# ❌ Infinite loop - continue skips increment
i = 0
while i < 10:
    if i % 2 == 0:
        continue  # i never increments for even numbers
    print(i)
    i += 1

# ✅ Move increment before continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# ✅ Or increment in both branches
i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
```

### Pitfall 3: else with break Confusion

```python
# else runs only when NO break occurs
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't run because break occurred")
# Output: 0,1,2

# For empty iterable, else runs
for i in []:
    print(i)
else:
    print("Empty iterable - else runs")  # Prints
```

---

## Practice Exercises

### Beginner Level

1. **Stop at Zero**
   ```python
   # Print numbers until zero is encountered
   # Example: [5, 2, 0, 7, 3] -> 5, 2
   ```

2. **Skip Even Numbers**
   ```python
   # Print only odd numbers, skip evens
   # Example: [1,2,3,4,5] -> 1,3,5
   ```

3. **Search with else**
   ```python
   # Find target in list, print "Found" or "Not found"
   ```

### Intermediate Level

4. **First Positive Even**
   ```python
   # Find first positive even number, stop when found
   ```

5. **Process Until Invalid**
   ```python
   # Keep asking for numbers until negative entered
   ```

6. **Skip Comments**
   ```python
   # Print lines that don't start with '#'
   ```

### Advanced Level

7. **Nested Break**
   ```python
   # Find first occurrence in 2D list, break both loops
   ```

8. **Retry with Max Attempts**
   ```python
   # Ask for password with max attempts using break/else
   ```

9. **File Parser**
   ```python
   # Parse file, skip empty lines, stop at [END] marker
   ```

---

## Quick Reference Card

```python
# break - exit loop completely
for item in iterable:
    if condition:
        break

# continue - skip to next iteration
for item in iterable:
    if condition:
        continue
    # process item

# else - runs if no break
for item in iterable:
    if condition:
        break
else:
    # runs only if loop completes without break

# Combined patterns
# Search with else
for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")

# Skip and stop
for item in items:
    if skip_condition:
        continue
    if stop_condition:
        break
    process(item)

# Nested loop break
found = False
for outer in iterable1:
    for inner in iterable2:
        if condition:
            found = True
            break
    if found:
        break
```

---

## Next Step

- Move to [04_nested_loops.md](04_nested_loops.md) to understand loops inside loops and work with multi-dimensional data.

---

*Master break, continue, and else to have fine-grained control over your loops! 🐍✨*
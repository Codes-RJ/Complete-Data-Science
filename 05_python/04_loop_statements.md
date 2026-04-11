Here's the **complete, all-in-one `LOOPS.md`** file - covering everything about loops in Python.

---

# 🔄 LOOPS – COMPLETE GUIDE

## 📌 Table of Contents
1. [Introduction to Loops](#introduction-to-loops)
2. [The `for` Loop](#the-for-loop)
3. [The `while` Loop](#the-while-loop)
4. [Loop Control Statements](#loop-control-statements)
5. [Nested Loops](#nested-loops)
6. [Loop Else Clause](#loop-else-clause)
7. [Common Patterns](#common-patterns)
8. [Real-World Examples](#real-world-examples)
9. [Common Pitfalls](#common-pitfalls)
10. [Performance Tips](#performance-tips)
11. [Practice Exercises](#practice-exercises)

---

## Introduction to Loops

**Loops** allow you to execute a block of code repeatedly. Python provides two types of loops: `for` loops (iterate over sequences) and `while` loops (iterate while condition is true).

```python
# for loop - iterate over a sequence
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# for loop - iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop - iterate while condition is true
count = 0
while count < 5:
    print(count)
    count += 1
```

**Why Loops Matter:**
- Automate repetitive tasks
- Process collections of data
- Implement algorithms that require repetition
- Reduce code duplication
- Handle user input until valid

---

## The `for` Loop

The `for` loop iterates over a sequence (list, tuple, string, range, etc.).

### Basic Syntax

```python
for variable in iterable:
    # Code block to execute for each item
    statement1
    statement2
```

### Iterating Over Different Types

```python
# Over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Over tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# Over string
for char in "Python":
    print(char)

# Over dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Iterate keys
for key in person:
    print(key)

# Iterate values
for value in person.values():
    print(value)

# Iterate key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Over set
unique_nums = {1, 2, 3, 4, 5}
for num in unique_nums:
    print(num)

# Over range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Using `enumerate()` for Index

```python
# Without index
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# With index using range
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (recommended)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start index from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")

# Real use: Processing with index
scores = [85, 90, 78, 92, 88]
for i, score in enumerate(scores, 1):
    print(f"Student {i}: {score}")
```

### Using `zip()` for Multiple Sequences

```python
# Iterate over multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Unequal lengths (stops at shortest)
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
for a, b in zip(list1, list2):
    print(f"{a} -> {b}")  # Only 3 iterations

# Use zip_longest for unequal lengths
from itertools import zip_longest
for a, b in zip_longest(list1, list2, fillvalue='?'):
    print(f"{a} -> {b}")
```

### Using `sorted()` for Ordered Iteration

```python
# Unsorted list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Iterate in sorted order
for num in sorted(numbers):
    print(num)  # 1, 1, 2, 3, 4, 5, 9

# Descending order
for num in sorted(numbers, reverse=True):
    print(num)  # 9, 5, 4, 3, 2, 1, 1

# Sort by custom key
words = ["banana", "apple", "cherry", "date"]
for word in sorted(words, key=len):
    print(word)  # apple, date, banana, cherry

# Sort dictionary by keys
person = {"name": "Alice", "age": 30, "city": "NYC"}
for key in sorted(person.keys()):
    print(f"{key}: {person[key]}")

# Sort dictionary by values
for key, value in sorted(person.items(), key=lambda x: x[1]):
    print(f"{key}: {value}")
```

### Using `reversed()` for Reverse Iteration

```python
# Reverse list
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)  # cherry, banana, apple

# Reverse range
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0

# Reverse string
for char in reversed("Python"):
    print(char)  # n, o, h, t, y, P

# Reverse without creating new list
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])
```

---

## The `while` Loop

The `while` loop executes a block of code repeatedly as long as a condition is `True`.

### Basic Syntax

```python
while condition:
    # Code block to execute while condition is True
    statement1
    statement2
```

### Basic Examples

```python
# Simple counter
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0, 1, 2, 3, 4

# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
# Output: 5, 4, 3, 2, 1, Blast off!

# Sum of numbers
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of 1 to 10: {total}")  # 55

# User input until valid
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
```

### Infinite Loops and Breaking

```python
# Infinite loop (use with break)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")

# Game loop
score = 0
playing = True
while playing:
    # Game logic here
    score += 1
    if score >= 10:
        playing = False
print(f"Final score: {score}")

# Server loop (conceptual)
server_running = True
while server_running:
    # Handle requests
    # Check for shutdown signal
    if should_shutdown:
        server_running = False
```

### While with Complex Conditions

```python
# Multiple conditions
x = 0
y = 10
while x < 5 and y > 5:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1

# While with boolean flag
is_processing = True
data = [1, 2, 3, 4, 5]
index = 0
while is_processing and index < len(data):
    if data[index] == 3:
        is_processing = False
    else:
        print(f"Processing {data[index]}")
    index += 1

# While with sentinel value
numbers = []
user_input = input("Enter a number (or 'done' to finish): ")
while user_input != 'done':
    numbers.append(int(user_input))
    user_input = input("Enter a number (or 'done' to finish): ")
print(f"Sum: {sum(numbers)}")
```

---

## Loop Control Statements

### `break` – Exit Loop Completely

```python
# Exit loop when condition met
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Search and stop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")

# While loop with break
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Real use: Find first even number
numbers = [1, 3, 5, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
```

### `continue` – Skip Current Iteration

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

# Process only positive numbers
numbers = [10, -5, 20, -3, 30, -1, 40]
positive_sum = 0
for num in numbers:
    if num < 0:
        continue
    positive_sum += num
print(f"Sum of positives: {positive_sum}")

# Skip empty strings
words = ["hello", "", "world", "", "python"]
for word in words:
    if not word:
        continue
    print(word.upper())
```

### `pass` – Placeholder (Does Nothing)

```python
# Placeholder for future code
for i in range(10):
    if i % 2 == 0:
        pass  # TODO: Handle even numbers
    else:
        print(f"Odd: {i}")

# In while loop
count = 0
while count < 5:
    if count == 3:
        pass  # Will implement later
    else:
        print(count)
    count += 1

# For empty loop (not recommended)
for i in range(1000000):
    pass  # Just wasting time
```

---

## Nested Loops

Loops inside other loops. The inner loop completes all iterations for each iteration of the outer loop.

### Basic Nested Loops

```python
# Simple nested loop
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end='')
    print()  # New line after each row

# Triangle pattern
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
# Output:
# *
# **
# ***
# ****
# *****

# Reverse triangle
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
# Output:
# *****
# ****
# ***
# **
# *
```

### Nested Loops with Lists

```python
# Matrix operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print matrix
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
# Output: 1 2 3
#        4 5 6
#        7 8 9

# Sum of all elements
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum: {total}")  # 45

# Find maximum
max_val = matrix[0][0]
for row in matrix:
    for element in row:
        if element > max_val:
            max_val = element
print(f"Max: {max_val}")  # 9

# Transpose matrix
rows = 3
cols = 3
transpose = [[0 for _ in range(rows)] for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print("Transpose:")
for row in transpose:
    print(row)
```

### Nested Loops with Break

```python
# Breaking out of nested loops
found = False
for i in range(5):
    for j in range(5):
        if i == 2 and j == 3:
            found = True
            break
        print(f"({i},{j})", end=' ')
    if found:
        break
    print()

# Using else with nested loops
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Found at ({i},{j})")
            break
    else:
        continue
    break
```

---

## Loop Else Clause

The `else` clause executes after the loop completes normally (without `break`).

### For Loop with Else

```python
# Loop completes normally
for i in range(5):
    print(i)
else:
    print("Loop completed without break")
# Output: 0,1,2,3,4, Loop completed without break

# Loop with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")
# Output: 0,1,2

# Search example
def find_number(numbers, target):
    for num in numbers:
        if num == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")

find_number([1, 2, 3, 4, 5], 3)  # Found 3
find_number([1, 2, 3, 4, 5], 7)  # 7 not found

# Prime number checker
def is_prime(n):
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
```

### While Loop with Else

```python
# While loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed")

# While loop with break
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("This won't print")

# User input with else
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted")
        break
    attempts -= 1
    print(f"Wrong. {attempts} attempts left")
else:
    print("Access denied. Account locked.")
```

---

## Common Patterns

### Pattern 1: Accumulator Pattern

```python
# Sum of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# Product of numbers
product = 1
for num in numbers:
    product *= num
print(f"Product: {product}")

# String concatenation
words = ["Hello", "World", "Python"]
sentence = ""
for word in words:
    sentence += word + " "
print(sentence.strip())

# List building
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)
```

### Pattern 2: Filter Pattern

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)

# Filter strings by length
words = ["a", "ab", "abc", "abcd", "abcde"]
long_words = []
for word in words:
    if len(word) >= 3:
        long_words.append(word)
print(long_words)

# Filter dictionary
scores = {"Alice": 85, "Bob": 45, "Charlie": 92, "David": 58}
passing = {}
for name, score in scores.items():
    if score >= 60:
        passing[name] = score
print(passing)
```

### Pattern 3: Mapping Pattern

```python
# Transform list
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled)

# Convert to uppercase
words = ["hello", "world", "python"]
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(upper_words)

# Dictionary transformation
prices = {"apple": 0.5, "banana": 0.3, "cherry": 0.8}
with_tax = {}
for item, price in prices.items():
    with_tax[item] = price * 1.08
print(with_tax)
```

### Pattern 4: Early Exit Pattern

```python
# Find first occurrence
def find_first(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

print(find_first([1, 2, 3, 4, 5], 3))  # 2
print(find_first([1, 2, 3, 4, 5], 7))  # -1

# Check if any condition met
def has_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
    return False

print(has_even([1, 3, 5, 7]))   # False
print(has_even([1, 2, 3, 4]))   # True

# Check if all condition met
def all_positive(numbers):
    for num in numbers:
        if num <= 0:
            return False
    return True

print(all_positive([1, 2, 3, 4]))   # True
print(all_positive([1, -2, 3, 4]))  # False
```

### Pattern 5: Parallel Processing Pattern

```python
# Using zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Multiple lists
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} from {city}")

# Index-based
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")
```

### Pattern 6: Flattening Pattern

```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flatten with condition
matrix = [[1, 2], [3, 4, 5], [6, 7]]
flattened = []
for row in matrix:
    for item in row:
        if item % 2 == 0:
            flattened.append(item)
print(flattened)  # [2, 4, 6]
```

---

## Real-World Examples

### Example 1: Student Grade Processor

```python
class GradeProcessor:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, grades):
        """Add a student with their grades"""
        self.students.append({
            'name': name,
            'grades': grades
        })
    
    def calculate_averages(self):
        """Calculate average for each student"""
        results = []
        for student in self.students:
            grades = student['grades']
            if grades:
                average = sum(grades) / len(grades)
            else:
                average = 0
            
            results.append({
                'name': student['name'],
                'average': round(average, 2),
                'grades': grades
            })
        return results
    
    def get_top_performers(self, threshold=85):
        """Get students with average above threshold"""
        averages = self.calculate_averages()
        top = []
        for student in averages:
            if student['average'] >= threshold:
                top.append(student)
        return sorted(top, key=lambda x: x['average'], reverse=True)
    
    def get_failing_students(self, passing_grade=60):
        """Get students with average below passing grade"""
        averages = self.calculate_averages()
        failing = []
        for student in averages:
            if student['average'] < passing_grade:
                failing.append(student)
        return sorted(failing, key=lambda x: x['average'])
    
    def generate_report(self):
        """Generate full grade report"""
        print("=" * 60)
        print("GRADE REPORT")
        print("=" * 60)
        
        for student in self.students:
            name = student['name']
            grades = student['grades']
            avg = sum(grades) / len(grades) if grades else 0
            
            # Determine letter grade
            if avg >= 90:
                letter = 'A'
            elif avg >= 80:
                letter = 'B'
            elif avg >= 70:
                letter = 'C'
            elif avg >= 60:
                letter = 'D'
            else:
                letter = 'F'
            
            print(f"\n{name}:")
            print(f"  Grades: {grades}")
            print(f"  Average: {avg:.2f}")
            print(f"  Grade: {letter}")
            
            # Show individual grade comments
            for i, grade in enumerate(grades, 1):
                if grade >= 90:
                    comment = "Excellent!"
                elif grade >= 80:
                    comment = "Good job!"
                elif grade >= 70:
                    comment = "Satisfactory"
                else:
                    comment = "Needs improvement"
                print(f"    Assignment {i}: {grade} - {comment}")
        
        # Class statistics
        all_grades = []
        for student in self.students:
            all_grades.extend(student['grades'])
        
        if all_grades:
            print("\n" + "-" * 40)
            print("CLASS STATISTICS:")
            print(f"  Total Students: {len(self.students)}")
            print(f"  Class Average: {sum(all_grades) / len(all_grades):.2f}")
            print(f"  Highest Grade: {max(all_grades)}")
            print(f"  Lowest Grade: {min(all_grades)}")
        
        print("=" * 60)

# Usage
processor = GradeProcessor()

# Add students
processor.add_student("Alice", [85, 90, 88, 92])
processor.add_student("Bob", [75, 80, 78, 82])
processor.add_student("Charlie", [45, 50, 55, 60])
processor.add_student("Diana", [95, 98, 92, 96])

# Generate report
processor.generate_report()

# Get top performers
print("\n" + "=" * 60)
print("TOP PERFORMERS (Average ≥ 85):")
top = processor.get_top_performers(85)
for student in top:
    print(f"  {student['name']}: {student['average']}")

# Get failing students
print("\n" + "=" * 60)
print("FAILING STUDENTS (Average < 60):")
failing = processor.get_failing_students(60)
for student in failing:
    print(f"  {student['name']}: {student['average']}")
```

### Example 2: Shopping Cart System

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
        print(f"Added {quantity}x {name} (${price:.2f} each)")
    
    def remove_item(self, name):
        """Remove all occurrences of item"""
        initial_count = len(self.items)
        self.items = [item for item in self.items if item['name'] != name]
        removed = initial_count - len(self.items)
        print(f"Removed {removed} item(s) of {name}")
    
    def update_quantity(self, name, quantity):
        """Update quantity of item"""
        for item in self.items:
            if item['name'] == name:
                item['quantity'] = quantity
                print(f"Updated {name} quantity to {quantity}")
                return
        print(f"{name} not found in cart")
    
    def calculate_total(self):
        """Calculate total price"""
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return round(total, 2)
    
    def apply_discount(self, discount_percent):
        """Apply percentage discount to total"""
        total = self.calculate_total()
        discount = total * (discount_percent / 100)
        return round(total - discount, 2)
    
    def get_item_count(self):
        """Get total number of items (counting quantity)"""
        count = 0
        for item in self.items:
            count += item['quantity']
        return count
    
    def get_unique_items_count(self):
        """Get number of unique items"""
        return len(self.items)
    
    def display_cart(self):
        """Display cart contents"""
        if not self.items:
            print("Cart is empty")
            return
        
        print("\n" + "=" * 60)
        print("SHOPPING CART")
        print("=" * 60)
        print(f"{'Item':<20} {'Price':<10} {'Qty':<5} {'Total':<10}")
        print("-" * 60)
        
        for item in self.items:
            item_total = item['price'] * item['quantity']
            print(f"{item['name']:<20} ${item['price']:<9.2f} {item['quantity']:<5} ${item_total:<9.2f}")
        
        print("-" * 60)
        print(f"{'TOTAL':<20} {'':<10} {'':<5} ${self.calculate_total():<9.2f}")
        print("=" * 60)
    
    def checkout(self):
        """Process checkout"""
        if not self.items:
            print("Cannot checkout: Cart is empty")
            return False
        
        print("\n" + "=" * 60)
        print("CHECKOUT")
        print("=" * 60)
        
        # Display final cart
        self.display_cart()
        
        # Apply any discounts
        discount = 0
        apply_discount = input("Apply discount? (y/n): ").lower()
        if apply_discount == 'y':
            discount_percent = float(input("Enter discount percentage: "))
            discount = discount_percent
            final_total = self.apply_discount(discount_percent)
            print(f"Discount applied: {discount_percent}%")
        else:
            final_total = self.calculate_total()
        
        print(f"Final total: ${final_total:.2f}")
        
        # Process payment
        while True:
            try:
                payment = float(input("Enter payment amount: $"))
                if payment >= final_total:
                    change = payment - final_total
                    print(f"Payment accepted. Change: ${change:.2f}")
                    print("Thank you for shopping!")
                    
                    # Clear cart after successful checkout
                    self.items.clear()
                    return True
                else:
                    print(f"Insufficient payment. Need ${final_total - payment:.2f} more.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        return False

# Usage
cart = ShoppingCart()

# Add items
cart.add_item("Laptop", 999.99, 1)
cart.add_item("Mouse", 29.99, 2)
cart.add_item("Keyboard", 79.99, 1)
cart.add_item("USB Cable", 9.99, 3)

# Display cart
cart.display_cart()

# Update quantity
cart.update_quantity("Mouse", 3)

# Display updated cart
cart.display_cart()

# Remove item
cart.remove_item("USB Cable")

# Final cart
cart.display_cart()

print(f"\nTotal items: {cart.get_item_count()}")
print(f"Unique items: {cart.get_unique_items_count()}")
print(f"Cart total: ${cart.calculate_total()}")

# Checkout (commented for demo)
# cart.checkout()
```

### Example 3: Number Guessing Game

```python
import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100, max_attempts=7):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = None
        self.attempts = 0
        self.game_over = False
    
    def start_new_game(self):
        """Start a new game"""
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        self.game_over = False
        print(f"\nNew game started!")
        print(f"Guess a number between {self.min_num} and {self.max_num}")
        print(f"You have {self.max_attempts} attempts")
    
    def make_guess(self, guess):
        """Make a guess"""
        if self.game_over:
            print("Game is over. Start a new game.")
            return False
        
        if guess < self.min_num or guess > self.max_num:
            print(f"Please guess between {self.min_num} and {self.max_num}")
            return False
        
        self.attempts += 1
        remaining = self.max_attempts - self.attempts
        
        if guess == self.secret_number:
            print(f"🎉 Correct! You guessed it in {self.attempts} attempts!")
            self.game_over = True
            return True
        elif guess < self.secret_number:
            print(f"Too low! {remaining} attempts remaining")
        else:
            print(f"Too high! {remaining} attempts remaining")
        
        if self.attempts >= self.max_attempts:
            print(f"Game over! The number was {self.secret_number}")
            self.game_over = True
        
        return False
    
    def play(self):
        """Play the game"""
        self.start_new_game()
        
        while not self.game_over:
            try:
                guess = int(input(f"Attempt {self.attempts + 1}: "))
                if self.make_guess(guess):
                    break
            except ValueError:
                print("Please enter a valid number")
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again == 'y':
            self.play()
        else:
            print("Thanks for playing!")

# Usage
game = NumberGuessingGame(min_num=1, max_num=50, max_attempts=5)
# game.play()  # Uncomment to play

# Simulated game for demo
print("NUMBER GUESSING GAME SIMULATION")
print("=" * 40)

game = NumberGuessingGame(1, 20, 4)
game.secret_number = 15  # Set for demo
game.start_new_game()

guesses = [10, 12, 14, 15]  # Winning sequence
for guess in guesses:
    print(f"\nAttempt {game.attempts + 1}: {guess}")
    if game.make_guess(guess):
        break
```

### Example 4: Password Validator with Multiple Rules

```python
class PasswordValidator:
    def __init__(self):
        self.rules = []
        self.common_passwords = [
            "password", "123456", "qwerty", "admin", "letmein",
            "welcome", "monkey", "dragon", "master", "login"
        ]
    
    def add_rule(self, rule_func, message):
        """Add a validation rule"""
        self.rules.append((rule_func, message))
    
    def validate(self, password):
        """Validate password against all rules"""
        errors = []
        
        for rule_func, message in self.rules:
            if not rule_func(password):
                errors.append(message)
        
        return len(errors) == 0, errors
    
    def check_strength(self, password):
        """Check password strength and return score"""
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
            feedback.append("✓ Excellent length (12+ characters)")
        elif len(password) >= 8:
            score += 1
            feedback.append("✓ Good length (8-11 characters)")
        else:
            feedback.append("✗ Too short (<8 characters)")
        
        # Uppercase check
        if any(c.isupper() for c in password):
            score += 1
            feedback.append("✓ Has uppercase letters")
        else:
            feedback.append("✗ Missing uppercase letters")
        
        # Lowercase check
        if any(c.islower() for c in password):
            score += 1
            feedback.append("✓ Has lowercase letters")
        else:
            feedback.append("✗ Missing lowercase letters")
        
        # Digit check
        if any(c.isdigit() for c in password):
            score += 1
            feedback.append("✓ Has numbers")
        else:
            feedback.append("✗ Missing numbers")
        
        # Special character check
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if any(c in special_chars for c in password):
            score += 1
            feedback.append("✓ Has special characters")
        else:
            feedback.append("✗ Missing special characters")
        
        # Common password check
        if password.lower() in self.common_passwords:
            score -= 2
            feedback.append("✗ Common password detected")
        
        # Sequence check
        if self._has_sequences(password):
            score -= 1
            feedback.append("✗ Contains sequential characters (abc, 123, etc.)")
        
        # Repeated characters check
        if self._has_repeated_chars(password):
            score -= 1
            feedback.append("✗ Contains repeated characters (aaa, 111, etc.)")
        
        # Determine strength
        if score >= 6:
            strength = "VERY STRONG"
        elif score >= 4:
            strength = "STRONG"
        elif score >= 2:
            strength = "WEAK"
        else:
            strength = "VERY WEAK"
        
        return {
            'score': max(0, score),
            'max_score': 7,
            'strength': strength,
            'feedback': feedback
        }
    
    def _has_sequences(self, password):
        """Check for sequential characters"""
        password_lower = password.lower()
        
        # Check for abc sequences
        for i in range(len(password_lower) - 2):
            if (ord(password_lower[i+1]) - ord(password_lower[i]) == 1 and
                ord(password_lower[i+2]) - ord(password_lower[i+1]) == 1):
                return True
        
        # Check for 123 sequences
        for i in range(len(password_lower) - 2):
            if password_lower[i:i+3].isdigit():
                if (int(password_lower[i+1]) - int(password_lower[i]) == 1 and
                    int(password_lower[i+2]) - int(password_lower[i+1]) == 1):
                    return True
        
        return False
    
    def _has_repeated_chars(self, password):
        """Check for repeated characters"""
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                return True
        return False
    
    def suggest_improvements(self, password):
        """Suggest improvements for weak passwords"""
        suggestions = []
        
        if len(password) < 8:
            suggestions.append(f"Add {8 - len(password)} more characters")
        
        if not any(c.isupper() for c in password):
            suggestions.append("Add an uppercase letter")
        
        if not any(c.islower() for c in password):
            suggestions.append("Add a lowercase letter")
        
        if not any(c.isdigit() for c in password):
            suggestions.append("Add a number")
        
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            suggestions.append(f"Add a special character ({special_chars[:10]}...)")
        
        if password.lower() in self.common_passwords:
            suggestions.append("Avoid common passwords")
        
        return suggestions

# Usage
validator = PasswordValidator()

# Add custom rules
def has_no_username(password):
    return "username" not in password.lower()

def has_no_password_word(password):
    return "password" not in password.lower()

validator.add_rule(has_no_username, "Password should not contain 'username'")
validator.add_rule(has_no_password_word, "Password should not contain 'password'")

print("PASSWORD VALIDATOR")
print("=" * 50)

# Test passwords
test_passwords = [
    "weak",
    "Password123",
    "StrongP@ssw0rd!",
    "123456",
    "password123",
    "MySecureP@ssw0rd2024!",
    "abc123",
    "username123",
]

for pwd in test_passwords:
    print(f"\nPassword: {pwd}")
    
    # Check strength
    result = validator.check_strength(pwd)
    print(f"Strength: {result['strength']} (Score: {result['score']}/{result['max_score']})")
    
    # Show feedback
    for fb in result['feedback']:
        print(f"  {fb}")
    
    # Show suggestions for weak passwords
    if result['score'] < 4:
        suggestions = validator.suggest_improvements(pwd)
        if suggestions:
            print("  Suggestions:")
            for sug in suggestions:
                print(f"    💡 {sug}")
    
    # Validate against rules
    is_valid, errors = validator.validate(pwd)
    if not is_valid:
        print("  Rule violations:")
        for error in errors:
            print(f"    ❌ {error}")
```

---

## Common Pitfalls

### Pitfall 1: Infinite Loops

```python
# ❌ Infinite loop (condition never becomes False)
count = 0
while count < 5:
    print(count)
    # Missing count += 1

# ✅ Correct
count = 0
while count < 5:
    print(count)
    count += 1

# ❌ Off-by-one causing infinite loop
count = 5
while count > 0:
    print(count)
    count += 1  # Should be count -= 1

# ✅ Correct
count = 5
while count > 0:
    print(count)
    count -= 1
```

### Pitfall 2: Modifying List While Iterating

```python
# ❌ WRONG - Modifying list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Causes skipping
print(numbers)  # [1, 3, 5] - Works but risky

# ✅ CORRECT - Iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [1, 3, 5]

# ✅ CORRECT - Use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]

# ✅ CORRECT - Iterate backwards
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
print(numbers)  # [1, 3, 5]
```

### Pitfall 3: Off-by-One Errors

```python
# ❌ Wrong range (excludes last element)
for i in range(1, 5):
    print(i)  # 1,2,3,4 (not 5)

# ✅ Correct
for i in range(1, 6):
    print(i)  # 1,2,3,4,5

# ❌ Wrong index access
items = ['a', 'b', 'c']
for i in range(len(items)):
    print(items[i+1])  # IndexError on last iteration

# ✅ Correct
for i in range(len(items) - 1):
    print(items[i+1])

# ❌ While loop off-by-one
count = 1
while count < 5:
    print(count)  # 1,2,3,4
    count += 1

# ✅ Correct (if you want 1-5)
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Pitfall 4: Forgetting to Reset Loop Variable

```python
# ❌ Wrong - Variable not reset
total = 0
for i in range(5):
    total += i
print(total)  # 10

# Later in code (total still 10)
for i in range(5, 10):
    total += i  # Continues from previous total
print(total)  # 10 + 35 = 45 (unexpected)

# ✅ Correct - Reset variable
total = 0
for i in range(5, 10):
    total += i
print(total)  # 35
```

---

## Performance Tips

### Use List Comprehensions Instead of Loops

```python
# ❌ Slower - Traditional loop
squares = []
for i in range(1000):
    squares.append(i ** 2)

# ✅ Faster - List comprehension
squares = [i ** 2 for i in range(1000)]

# ❌ Slower - Loop with condition
evens = []
for i in range(1000):
    if i % 2 == 0:
        evens.append(i)

# ✅ Faster - Comprehension with condition
evens = [i for i in range(1000) if i % 2 == 0]
```

### Use Built-in Functions

```python
# ❌ Slower - Manual sum
total = 0
for num in numbers:
    total += num

# ✅ Faster - Built-in sum
total = sum(numbers)

# ❌ Slower - Manual max
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num

# ✅ Faster - Built-in max
max_val = max(numbers)
```

### Avoid Repeated Calculations

```python
# ❌ Slow - Recalculating length each iteration
for i in range(len(my_list)):
    for j in range(len(my_list)):
        # len(my_list) calculated many times
        pass

# ✅ Fast - Store in variable
n = len(my_list)
for i in range(n):
    for j in range(n):
        pass
```

---

## Practice Exercises

### Beginner Level

1. **Sum of Numbers**
   ```python
   # Calculate sum of numbers from 1 to n using for loop
   ```

2. **Print Pattern**
   ```python
   # Print triangle pattern using nested loops
   # *
   # **
   # ***
   ```

3. **Even Numbers**
   ```python
   # Print all even numbers from 1 to 50
   ```

4. **Factorial**
   ```python
   # Calculate factorial using while loop
   ```

5. **Reverse String**
   ```python
   # Reverse a string using loop
   ```

### Intermediate Level

6. **Prime Numbers**
   ```python
   # Find all prime numbers up to n
   ```

7. **Fibonacci Sequence**
   ```python
   # Generate first n Fibonacci numbers
   ```

8. **List Operations**
   ```python
   # Find min, max, sum, average using loops (no built-ins)
   ```

9. **Matrix Multiplication**
   ```python
   # Multiply two matrices using nested loops
   ```

10. **Bubble Sort**
    ```python
    # Implement bubble sort using nested loops
    ```

### Advanced Level

11. **Binary Search**
    ```python
    # Implement binary search using while loop
    ```

12. **Anagram Finder**
    ```python
    # Find all anagrams in a list of words
    ```

13. **Longest Substring**
    ```python
    # Find longest substring without repeating characters
    ```

14. **Word Search**
    ```python
    # Search for word in 2D grid (word search puzzle)
    ```

15. **Sudoku Validator**
    ```python
    # Validate Sudoku board using nested loops
    ```

---

## Quick Reference Card

```python
# For loop
for item in iterable:
    # code

# For with enumerate
for i, item in enumerate(iterable):
    # code

# For with zip
for a, b in zip(iterable1, iterable2):
    # code

# For with range
for i in range(stop):
for i in range(start, stop):
for i in range(start, stop, step):

# While loop
while condition:
    # code

# Infinite loop
while True:
    if condition:
        break

# Loop control
break       # Exit loop completely
continue    # Skip to next iteration
pass        # Do nothing (placeholder)

# Loop else
for item in iterable:
    if condition:
        break
else:
    # Executes if no break occurred

# Nested loops
for i in range(3):
    for j in range(3):
        # code

# List comprehension
[expr for item in iterable]
[expr for item in iterable if condition]

# Dictionary comprehension
{key_expr: value_expr for item in iterable}

# Set comprehension
{expr for item in iterable}

# Generator expression
(expr for item in iterable)  # Memory efficient
```

## Next Step

- Go to [05_functions](./05_functions/README.md) to i=understand creation and usage of functions in Python.

---

*Master loops to automate repetitive tasks efficiently! 🐍✨*
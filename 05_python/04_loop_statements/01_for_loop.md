# 📘 FOR LOOP – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is a For Loop?](#what-is-a-for-loop)
2. [For Loop Syntax](#for-loop-syntax)
3. [Iterating Over Different Types](#iterating-over-different-types)
4. [The range() Function](#the-range-function)
5. [Using enumerate()](#using-enumerate)
6. [Using zip()](#using-zip)
7. [Using sorted() and reversed()](#using-sorted-and-reversed)
8. [For Loop with else](#for-loop-with-else)
9. [Real-World Examples](#real-world-examples)
10. [Common Pitfalls](#common-pitfalls)
11. [Practice Exercises](#practice-exercises)

---

## What is a For Loop?

A **for loop** is used to iterate over a sequence (list, tuple, string, range, dictionary, etc.) and execute a block of code for each item.

```python
# Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

**Key Characteristics:**
- ✅ Iterates over any iterable object
- ✅ Automatically handles the end of sequence
- ✅ No need to manage index variables
- ✅ Cleaner and less error-prone than while loops for sequences

---

## For Loop Syntax

### Basic Syntax

```python
for variable in iterable:
    # Code block to execute for each item
    statement1
    statement2
```

### Examples

```python
# Simple for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# With multiple statements
for fruit in ["apple", "banana", "cherry"]:
    print(f"Fruit: {fruit}")
    print(f"Length: {len(fruit)}")
    print("-" * 10)

# Using the loop variable
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    double = num * 2
    print(f"{num} doubled is {double}")
```

---

## Iterating Over Different Types

### Iterating Over Lists

```python
# List of strings
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# List of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")  # 15

# List of mixed types
mixed = [1, "hello", 3.14, True]
for item in mixed:
    print(f"{item} is {type(item).__name__}")
```

### Iterating Over Tuples

```python
# Tuple of colors
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# Tuple of coordinates
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x={x}, y={y}")

# Tuple unpacking
person = ("Alice", 30, "Engineer")
for value in person:
    print(value)
```

### Iterating Over Strings

```python
# String characters
text = "Python"
for char in text:
    print(char)  # P, y, t, h, o, n

# Count vowels
text = "Hello World"
vowel_count = 0
for char in text.lower():
    if char in 'aeiou':
        vowel_count += 1
print(f"Vowels: {vowel_count}")  # 3
```

### Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterate over keys (default)
for key in person:
    print(f"Key: {key}")

# Iterate over keys (explicit)
for key in person.keys():
    print(f"Key: {key}")

# Iterate over values
for value in person.values():
    print(f"Value: {value}")

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Modify values while iterating (use caution)
for key in person.keys():
    person[key] = str(person[key]) if key == "age" else person[key]
print(person)
```

### Iterating Over Sets

```python
# Sets are unordered
unique_numbers = {3, 1, 4, 1, 5, 9, 2}
for num in unique_numbers:
    print(num)  # Order may vary

# Sorted iteration
for num in sorted(unique_numbers):
    print(num)  # 1, 2, 3, 4, 5, 9
```

---

## The range() Function

`range()` generates a sequence of numbers efficiently.

### Basic range() Usage

```python
# Single argument: range(stop) - 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Two arguments: range(start, stop) - start to stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# Three arguments: range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

# Negative step (countdown)
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

# Reverse without negative step
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0
```

### Practical range() Examples

```python
# Sum of first n numbers
n = 100
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n}: {total}")  # 5050

# Even numbers
for i in range(0, 20, 2):
    print(i, end=" ")  # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
print()

# Odd numbers
for i in range(1, 20, 2):
    print(i, end=" ")  # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
print()

# Multiplication table
number = 5
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

# Iterating over list indices (not recommended, but possible)
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

---

## Using enumerate()

`enumerate()` adds a counter to an iterable, returning index-value pairs.

### Basic enumerate()

```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate (old way)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (Pythonic way)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start index from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
```

### Practical enumerate() Examples

```python
# Find index of element
fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"
for i, fruit in enumerate(fruits):
    if fruit == target:
        print(f"Found '{target}' at index {i}")
        break

# Create dictionary from list with indices
fruits = ["apple", "banana", "cherry"]
indexed = {i: fruit for i, fruit in enumerate(fruits)}
print(indexed)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

# Process with index and value
scores = [85, 90, 78, 92, 88]
for i, score in enumerate(scores, 1):
    print(f"Student {i}: {score}")
```

---

## Using zip()

`zip()` iterates over multiple sequences in parallel.

### Basic zip()

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Iterate over two lists together
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Three lists
cities = ["NYC", "LA", "Chicago"]
for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) from {city}")
```

### Handling Different Lengths

```python
# zip stops at the shortest iterable
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")  # David is not printed

# Use zip_longest from itertools for full iteration
from itertools import zip_longest
for name, age in zip_longest(names, ages, fillvalue="Unknown"):
    print(f"{name}: {age}")
```

### Practical zip() Examples

```python
# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Calculate element-wise sum
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
sums = [a + b for a, b in zip(list1, list2)]
print(sums)  # [11, 22, 33, 44, 55]

# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = list(zip(*matrix))
print(transpose)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

---

## Using sorted() and reversed()

### sorted() – Iterate in Sorted Order

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# Ascending order
for num in sorted(numbers):
    print(num, end=" ")  # 1, 1, 2, 3, 4, 5, 9
print()

# Descending order
for num in sorted(numbers, reverse=True):
    print(num, end=" ")  # 9, 5, 4, 3, 2, 1, 1
print()

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

### reversed() – Iterate in Reverse Order

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

## For Loop with else

The `else` block executes after the loop completes normally (without a `break`).

### Basic else

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
```

### Practical else Examples

```python
# Search for item
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
    print("All numbers are even")

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

---

## Real-World Examples

### Example 1: Student Grade Processor

```python
class GradeProcessor:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, grades):
        self.students.append({"name": name, "grades": grades})
    
    def calculate_averages(self):
        results = []
        for student in self.students:
            name = student["name"]
            grades = student["grades"]
            average = sum(grades) / len(grades) if grades else 0
            results.append({"name": name, "average": round(average, 2)})
        return results
    
    def get_top_performers(self, n=3):
        averages = self.calculate_averages()
        sorted_students = sorted(averages, key=lambda x: x["average"], reverse=True)
        return sorted_students[:n]
    
    def generate_report(self):
        print("=" * 50)
        print("GRADE REPORT")
        print("=" * 50)
        
        for student in self.students:
            name = student["name"]
            grades = student["grades"]
            avg = sum(grades) / len(grades) if grades else 0
            
            # Determine letter grade
            if avg >= 90:
                letter = "A"
            elif avg >= 80:
                letter = "B"
            elif avg >= 70:
                letter = "C"
            elif avg >= 60:
                letter = "D"
            else:
                letter = "F"
            
            print(f"\n{name}:")
            print(f"  Grades: {grades}")
            print(f"  Average: {avg:.2f} ({letter})")
            
            # Individual grade comments
            for i, grade in enumerate(grades, 1):
                if grade >= 90:
                    comment = "Excellent"
                elif grade >= 80:
                    comment = "Good"
                elif grade >= 70:
                    comment = "Satisfactory"
                else:
                    comment = "Needs improvement"
                print(f"    Assignment {i}: {grade} - {comment}")
        
        print("\n" + "=" * 50)

# Usage
processor = GradeProcessor()
processor.add_student("Alice", [85, 90, 88, 92])
processor.add_student("Bob", [75, 80, 78, 82])
processor.add_student("Charlie", [95, 98, 92, 96])
processor.generate_report()

print("\nTop Performers:")
for student in processor.get_top_performers(2):
    print(f"  {student['name']}: {student['average']}")
```

### Example 2: Data Filter and Transform

```python
class DataProcessor:
    @staticmethod
    def filter_numbers(numbers, condition):
        """Filter numbers based on condition function"""
        result = []
        for num in numbers:
            if condition(num):
                result.append(num)
        return result
    
    @staticmethod
    def transform_numbers(numbers, transform_func):
        """Transform each number using function"""
        result = []
        for num in numbers:
            result.append(transform_func(num))
        return result
    
    @staticmethod
    def process_students(students):
        """Process student data with multiple operations"""
        processed = []
        
        for student in students:
            name = student["name"]
            scores = student["scores"]
            
            # Calculate statistics
            total = sum(scores)
            average = total / len(scores)
            max_score = max(scores)
            min_score = min(scores)
            
            # Determine status
            if average >= 90:
                status = "Excellent"
            elif average >= 75:
                status = "Good"
            elif average >= 60:
                status = "Pass"
            else:
                status = "Needs Improvement"
            
            processed.append({
                "name": name,
                "average": round(average, 2),
                "total": total,
                "max": max_score,
                "min": min_score,
                "status": status
            })
        
        return processed

# Usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = DataProcessor.filter_numbers(numbers, lambda x: x % 2 == 0)
print(f"Even numbers: {evens}")

# Filter numbers greater than 5
greater_than_5 = DataProcessor.filter_numbers(numbers, lambda x: x > 5)
print(f"Numbers > 5: {greater_than_5}")

# Transform: square each number
squares = DataProcessor.transform_numbers(numbers, lambda x: x ** 2)
print(f"Squares: {squares}")

# Process students
students = [
    {"name": "Alice", "scores": [85, 90, 88, 92]},
    {"name": "Bob", "scores": [75, 80, 78, 82]},
    {"name": "Charlie", "scores": [95, 98, 92, 96]},
    {"name": "Diana", "scores": [65, 70, 68, 72]},
]

results = DataProcessor.process_students(students)
print("\nStudent Results:")
for result in results:
    print(f"  {result['name']}: Avg={result['average']}, Status={result['status']}")
```

### Example 3: Shopping Cart Total

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return round(total, 2)
    
    def apply_discount(self, discount_percent):
        total = self.calculate_total()
        discount = total * (discount_percent / 100)
        return round(total - discount, 2)
    
    def get_item_count(self):
        count = 0
        for item in self.items:
            count += item["quantity"]
        return count
    
    def display_cart(self):
        if not self.items:
            print("Cart is empty")
            return
        
        print("\n" + "=" * 50)
        print("SHOPPING CART")
        print("=" * 50)
        print(f"{'Item':<20} {'Price':<10} {'Qty':<5} {'Total':<10}")
        print("-" * 50)
        
        for item in self.items:
            item_total = item["price"] * item["quantity"]
            print(f"{item['name']:<20} ${item['price']:<9.2f} {item['quantity']:<5} ${item_total:<9.2f}")
        
        print("-" * 50)
        print(f"{'TOTAL':<20} {'':<10} {'':<5} ${self.calculate_total():<9.2f}")
        print("=" * 50)
    
    def find_expensive_items(self, threshold):
        expensive = []
        for item in self.items:
            if item["price"] > threshold:
                expensive.append(item["name"])
        return expensive

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99, 1)
cart.add_item("Mouse", 29.99, 2)
cart.add_item("Keyboard", 79.99, 1)
cart.add_item("USB Cable", 9.99, 3)

cart.display_cart()
print(f"\nTotal items: {cart.get_item_count()}")
print(f"Subtotal: ${cart.calculate_total()}")
print(f"After 10% discount: ${cart.apply_discount(10)}")
print(f"Expensive items (> $50): {cart.find_expensive_items(50)}")
```

### Example 4: Pattern Generation

```python
class PatternGenerator:
    @staticmethod
    def triangle(n):
        """Print triangle pattern"""
        for i in range(1, n + 1):
            print('*' * i)
    
    @staticmethod
    def reverse_triangle(n):
        """Print reverse triangle pattern"""
        for i in range(n, 0, -1):
            print('*' * i)
    
    @staticmethod
    def pyramid(n):
        """Print pyramid pattern"""
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    @staticmethod
    def diamond(n):
        """Print diamond pattern"""
        # Top half
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
        # Bottom half
        for i in range(n - 1, 0, -1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)
    
    @staticmethod
    def number_pyramid(n):
        """Print number pyramid"""
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            numbers = ' '.join(str(x) for x in range(1, i + 1))
            print(spaces + numbers)
    
    @staticmethod
    def multiplication_table(n):
        """Print multiplication table"""
        # Header
        print("    ", end="")
        for i in range(1, n + 1):
            print(f"{i:4}", end="")
        print("\n    " + "-" * (n * 4))
        
        # Rows
        for i in range(1, n + 1):
            print(f"{i:2} |", end="")
            for j in range(1, n + 1):
                print(f"{i * j:4}", end="")
            print()

# Usage
print("TRIANGLE:")
PatternGenerator.triangle(5)

print("\nREVERSE TRIANGLE:")
PatternGenerator.reverse_triangle(5)

print("\nPYRAMID:")
PatternGenerator.pyramid(5)

print("\nDIAMOND:")
PatternGenerator.diamond(5)

print("\nNUMBER PYRAMID:")
PatternGenerator.number_pyramid(5)

print("\nMULTIPLICATION TABLE:")
PatternGenerator.multiplication_table(10)
```

---

## Common Pitfalls

### Pitfall 1: Modifying List While Iterating

```python
# ❌ WRONG - Modifying list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Causes skipping
print(numbers)  # [1, 3, 5] (unreliable)

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
```

### Pitfall 2: Off-by-One Errors with range()

```python
# ❌ WRONG - Excludes last element
for i in range(1, 5):
    print(i)  # 1,2,3,4 (not 5)

# ✅ CORRECT - Include stop value
for i in range(1, 6):
    print(i)  # 1,2,3,4,5

# ❌ WRONG - Wrong step direction
for i in range(5, 1):
    print(i)  # Nothing (empty)

# ✅ CORRECT - Use negative step
for i in range(5, 1, -1):
    print(i)  # 5,4,3,2
```

### Pitfall 3: Modifying Dictionary While Iterating

```python
# ❌ WRONG - Modifying dict size during iteration
person = {"name": "Alice", "age": 30, "city": "NYC"}
for key in person:
    if key == "age":
        del person[key]  # RuntimeError!

# ✅ CORRECT - Iterate over list of keys
for key in list(person.keys()):
    if key == "age":
        del person[key]
print(person)  # {'name': 'Alice', 'city': 'NYC'}
```

---

## Practice Exercises

### Beginner Level

1. **Print Numbers**
   ```python
   # Print numbers from 1 to 10 using for loop
   ```

2. **Sum of List**
   ```python
   # Calculate sum of all numbers in a list using for loop
   ```

3. **Print Each Character**
   ```python
   # Print each character of a string on a new line
   ```

4. **Even Numbers**
   ```python
   # Print all even numbers from 1 to 50 using range()
   ```

5. **Multiplication Table**
   ```python
   # Print multiplication table for a given number
   ```

### Intermediate Level

6. **Find Maximum**
   ```python
   # Find maximum number in a list without using max()
   ```

7. **Count Vowels**
   ```python
   # Count vowels in a string using for loop
   ```

8. **Reverse List**
   ```python
   # Reverse a list without using [::-1] or reverse()
   ```

9. **List Comprehension**
   ```python
   # Use list comprehension to create list of squares
   ```

10. **Dictionary from Lists**
    ```python
    # Create dictionary from two lists using zip()
    ```

### Advanced Level

11. **Prime Number Finder**
    ```python
    # Find all prime numbers up to n using nested loops
    ```

12. **Matrix Addition**
    ```python
    # Add two matrices using nested loops
    ```

13. **Word Frequency**
    ```python
    # Count frequency of each word in a sentence using dictionary
    ```

---

## Quick Reference Card

```python
# Basic for loop
for item in iterable:
    # code

# With range
for i in range(stop):
for i in range(start, stop):
for i in range(start, stop, step):

# With enumerate
for i, item in enumerate(iterable):
for i, item in enumerate(iterable, start):

# With zip
for a, b in zip(iter1, iter2):

# With sorted
for item in sorted(iterable):
for item in sorted(iterable, reverse=True):

# With reversed
for item in reversed(iterable):

# With else
for item in iterable:
    if condition:
        break
else:
    # Runs if no break

# List comprehension
[expr for item in iterable]
[expr for item in iterable if condition]

# Dictionary comprehension
{key_expr: value_expr for item in iterable}

# Set comprehension
{expr for item in iterable}
```

---

## Next Step

- Move to [02_while_loop.md](02_while_loop.md) to understand the while loop and learn when to use it for condition-based iteration.

---

*Master the for loop to iterate through sequences efficiently! 🐍✨*
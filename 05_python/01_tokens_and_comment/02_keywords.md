# Keywords in Python 📦

---

## What are Keywords?

They are pre-defined words with special meaning to the language compiler or interpreter. Think of it as reserved words that serve a special purpose and must not be used as normal identifiers.

---

## Python Keywords Grouped by Category

### 1. Conditional Keywords (if, elif, else)

```python
# if - tests a condition
age = 18
if age >= 18:
    print("You can vote")

# elif - checks another condition
score = 75
if score >= 90:
    print("A")
elif score >= 70:
    print("B")

# else - runs if all conditions are false
temperature = 15
if temperature > 25:
    print("Hot")
else:
    print("Cool")
```

---

### 2. Loop Keywords (for, while, break, continue, pass)

```python
# for - iterates over a sequence
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# while - runs while condition is true
count = 1
while count <= 3:
    print(count)
    count += 1

# break - exits loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0,1,2,3,4

# continue - skips to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0,1,3,4

# pass - does nothing (placeholder)
def my_function():
    pass  # To be implemented later
```

---

### 3. Function Keywords (def, return, yield, lambda)

```python
# def - defines a function
def greet(name):
    return f"Hello, {name}"

# return - returns a value from function
def add(a, b):
    return a + b

result = add(5, 3)  # 8

# yield - returns generator value (pauses function)
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)  # 1,2,3

# lambda - creates anonymous function
square = lambda x: x ** 2
print(square(5))  # 25
```

---

### 4. Exception Handling Keywords (try, except, finally, raise, assert)

```python
# try and except - handle errors
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# finally - always executes
try:
    x = 10 / 2
except:
    print("Error")
finally:
    print("This always runs")  # Prints even if no error

# raise - manually trigger an exception
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

# assert - tests condition, raises error if false
x = 10
assert x > 0, "x must be positive"  # Passes
y = -5
assert y > 0, "y must be positive"  # AssertionError
```

---

### 5. Logical Operators (and, or, not)

```python
# and - True only if both are true
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")

# or - True if at least one is true
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today")

# not - reverses boolean value
is_raining = False
if not is_raining:
    print("Go outside")
```

---

### 6. Membership & Identity Keywords (in, not in, is, is not)

```python
# in - checks if value exists in sequence
fruits = ["apple", "banana", "mango"]
if "banana" in fruits:
    print("Found banana")

# not in - checks if value does NOT exist
if "grape" not in fruits:
    print("Grape not found")

# is - checks if same object (identity)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True (same object)
print(a is c)   # False (different objects)

# is not - checks if different objects
print(a is not c)  # True
```

---

### 7. Value Keywords (True, False, None)

```python
# True - boolean true value
is_active = True
if is_active:
    print("User is active")

# False - boolean false value
is_deleted = False
if not is_deleted:
    print("Item exists")

# None - represents no value/null
result = None
if result is None:
    print("No value")
```

---

### 8. Scope Keywords (global, nonlocal)

```python
# global - modify global variable inside function
counter = 0
def increment():
    global counter
    counter += 1
increment()
print(counter)  # 1

# nonlocal - modify variable from outer scope
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 20
outer()
```

---

### 9. Class & Object Keywords (class, del)

```python
# class - defines a class (blueprint)
class Car:
    def __init__(self, brand):
        self.brand = brand

my_car = Car("Toyota")
print(my_car.brand)  # Toyota

# del - deletes an object or reference
x = 10
del x
# print(x)  # Error! x is deleted

my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # [1, 3]
```

---

### 10. Import Keywords (import, from, as)

```python
# import - imports an entire module
import math
print(math.sqrt(16))  # 4.0

# from - imports specific parts from module
from math import sqrt, pi
print(sqrt(25))   # 5.0
print(pi)         # 3.14159

# as - gives alias/nickname to module
import numpy as np
arr = np.array([1, 2, 3])  # Using 'np' instead of 'numpy'
```

---

### 11. Resource Management (with)

```python
# with - auto-closes resources (file, database, etc.)
# Without with (need to close manually)
file = open("test.txt", "w")
file.write("Hello")
file.close()

# With with (auto closes)
with open("test.txt", "w") as file:
    file.write("Hello")
# No need to close - automatically handled
```

---

### 12. Asynchronous Keywords (async, await)

```python
# async - declares async function
# await - waits for async result

import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(2)  # await - waits here
    print("Done!")
    return "Data"

async def main():
    result = await fetch_data()  # await - waits for completion
    print(result)

# To run: asyncio.run(main())
```

---

## Complete Quick Reference Table

| Category | Keywords |
|----------|----------|
| **Conditional** | if, elif, else |
| **Loops** | for, while, break, continue, pass |
| **Functions** | def, return, yield, lambda |
| **Exception Handling** | try, except, finally, raise, assert |
| **Logical Operators** | and, or, not |
| **Membership & Identity** | in, not in, is, is not |
| **Values** | True, False, None |
| **Scope** | global, nonlocal |
| **Class & Object** | class, del |
| **Import** | import, from, as |
| **Resource Management** | with |
| **Asynchronous** | async, await |

---

## Key Takeaways

- Keywords are reserved words with special meanings
- Cannot use keywords as variable names
- Related keywords work together (if-elif-else, try-except-finally)
- Use `keyword.kwlist` to see all keywords in your Python version

---

## Next Steps

- Proceed to [03_operators.md](./03_operators.md) to explore data types in depth
- Practice using keywords with variables to apply features to your code

---

*"Keywords are the grammar of Python - learn them to speak the language fluently."*
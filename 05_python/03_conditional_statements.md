# 🔀 CONDITIONAL STATEMENTS – COMPLETE GUIDE

## 📌 Table of Contents
1. [Introduction to Conditionals](#introduction-to-conditionals)
2. [The `if` Statement](#the-if-statement)
3. [The `if-else` Statement](#the-if-else-statement)
4. [The `if-elif-else` Statement](#the-if-elif-else-statement)
5. [Nested Conditionals](#nested-conditionals)
6. [Ternary Operator (Conditional Expression)](#ternary-operator-conditional-expression)
7. [Truthy and Falsy Values](#truthy-and-falsy-values)
8. [Comparison Operators](#comparison-operators)
9. [Logical Operators](#logical-operators)
10. [Membership and Identity Operators](#membership-and-identity-operators)
11. [Common Patterns and Best Practices](#common-patterns-and-best-practices)
12. [Real-World Examples](#real-world-examples)
13. [Common Pitfalls](#common-pitfalls)
14. [Practice Exercises](#practice-exercises)

---

## Introduction to Conditionals

**Conditional statements** allow your program to make decisions and execute different code blocks based on whether certain conditions are `True` or `False`.

```python
# The simplest conditional
age = 18
if age >= 18:
    print("You can vote!")

# With else clause
temperature = 30
if temperature > 25:
    print("It's hot outside")
else:
    print("It's cool outside")

# Multiple conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

**Why Conditionals Matter:**
- Make programs intelligent and responsive
- Handle different scenarios and edge cases
- Control program flow based on user input
- Validate data before processing
- Implement business logic and rules

---

## The `if` Statement

The simplest conditional - executes a block of code only if the condition evaluates to `True`.

### Basic Syntax

```python
if condition:
    # Code block (indented by 4 spaces)
    statement1
    statement2
    # ... more statements
```

### Examples

```python
# Single condition
x = 10
if x > 5:
    print("x is greater than 5")

# Multiple statements in block
score = 85
if score >= 60:
    print("You passed!")
    print("Congratulations!")
    print("Keep up the good work!")

# With expressions
number = 42
if number % 2 == 0:
    print(f"{number} is even")

# With boolean variables
is_raining = True
if is_raining:
    print("Take an umbrella")
    print("Wear a raincoat")

# With function calls
def is_weekend(day):
    return day in ['Saturday', 'Sunday']

if is_weekend('Saturday'):
    print("Time to relax!")
```

---

## The `if-else` Statement

Executes one block if condition is `True`, another block if condition is `False`.

### Basic Syntax

```python
if condition:
    # Executes when condition is True
    statement_true
else:
    # Executes when condition is False
    statement_false
```

### Examples

```python
# Basic if-else
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Real example: Password validation
password = "secret123"
if len(password) >= 8:
    print("Password is strong")
else:
    print("Password is too short")

# Number classification
number = 5
if number > 0:
    print("Positive")
else:
    print("Negative or zero")

# User input validation
user_input = input("Enter yes/no: ")
if user_input.lower() == "yes":
    print("You agreed")
else:
    print("You did not agree")

# Multiple statements in each block
temperature = 35
if temperature > 30:
    print("It's hot!")
    print("Stay hydrated")
    print("Use sunscreen")
else:
    print("It's pleasant")
    print("Enjoy the weather")
```

---

## The `if-elif-else` Statement

Handles multiple conditions in sequence. The first condition that evaluates to `True` executes its block, then skips the rest.

### Basic Syntax

```python
if condition1:
    # Executes if condition1 is True
    block1
elif condition2:
    # Executes if condition1 is False and condition2 is True
    block2
elif condition3:
    # Executes if condition1 and condition2 are False and condition3 is True
    block3
else:
    # Executes if all conditions are False
    block_else
```

### Examples

```python
# Grade calculator
score = 85

if score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory"
elif score >= 60:
    grade = "D"
    message = "Need improvement"
else:
    grade = "F"
    message = "Failed"

print(f"Score: {score}, Grade: {grade}, Message: {message}")

# Day of week
day_number = 3

if day_number == 1:
    day_name = "Monday"
elif day_number == 2:
    day_name = "Tuesday"
elif day_number == 3:
    day_name = "Wednesday"
elif day_number == 4:
    day_name = "Thursday"
elif day_number == 5:
    day_name = "Friday"
elif day_number == 6:
    day_name = "Saturday"
elif day_number == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid day"

print(f"Day {day_number} is {day_name}")

# BMI Calculator
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f}, Category: {category}")

# Shipping cost calculator
total = 150
shipping = 0

if total >= 100:
    shipping = 0
    method = "Free Shipping"
elif total >= 50:
    shipping = 5.99
    method = "Standard Shipping"
elif total >= 25:
    shipping = 3.99
    method = "Economy Shipping"
else:
    shipping = 1.99
    method = "Basic Shipping"

print(f"Total: ${total}, Shipping: ${shipping}, Method: {method}")
```

---

## Nested Conditionals

Conditionals inside other conditionals. Useful for complex logic with multiple dependent conditions.

### Basic Syntax

```python
if outer_condition:
    # Outer block
    if inner_condition:
        # Inner block
        statement
    else:
        # Inner else
        statement_else
else:
    # Outer else
    statement_outer
```

### Examples

```python
# Age and license check
age = 25
has_license = True

if age >= 18:
    print("Age check passed")
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")

# Discount calculator with nested conditions
is_member = True
purchase_amount = 150
years_member = 3

if is_member:
    if years_member >= 5:
        discount = 0.25
    elif years_member >= 3:
        discount = 0.20
    else:
        discount = 0.10
    
    if purchase_amount >= 100:
        discount += 0.05
else:
    if purchase_amount >= 200:
        discount = 0.10
    elif purchase_amount >= 100:
        discount = 0.05
    else:
        discount = 0

print(f"Discount: {discount * 100}%")

# Login system
username = "admin"
password = "secret123"
captcha = "ABC12"

if username == "admin":
    print("Username correct")
    if password == "secret123":
        print("Password correct")
        if captcha == "ABC12":
            print("Login successful!")
            print("Welcome admin")
        else:
            print("Invalid captcha")
    else:
        print("Invalid password")
else:
    print("Username not found")

# Better way using logical operators (less nesting)
if username == "admin" and password == "secret123" and captcha == "ABC12":
    print("Login successful!")
else:
    print("Login failed")
```

---

## Ternary Operator (Conditional Expression)

A one-line shorthand for if-else statements.

### Basic Syntax

```python
# Syntax
value_if_true if condition else value_if_false

# Traditional if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary equivalent
status = "Adult" if age >= 18 else "Minor"
```

### Examples

```python
# Basic usage
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# With numbers
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result)  # Positive

# In function returns
def get_discount(is_member):
    return 0.20 if is_member else 0.05

print(get_discount(True))   # 0.2
print(get_discount(False))  # 0.05

# In print statement
x = 5
print("Even" if x % 2 == 0 else "Odd")  # Odd

# With multiple expressions
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)  # B

# Assign based on condition
is_weekend = True
message = "Relax!" if is_weekend else "Work hard!"
print(message)  # Relax!

# In list comprehensions
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Nested ternary (use sparingly - can be hard to read)
x = 5
result = "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(result)  # Positive
```

---

## Truthy and Falsy Values

In Python, every value has an inherent boolean value.

### Falsy Values (Evaluate to False)

```python
# All these evaluate to False
falsy_values = [
    None,
    False,
    0,
    0.0,
    0j,
    "",
    [],
    (),
    {},
    set(),
    range(0)
]

for val in falsy_values:
    print(f"{repr(val):10} -> {bool(val)}")

# Output:
# None       -> False
# False      -> False
# 0          -> False
# 0.0        -> False
# 0j         -> False
# ''         -> False
# []         -> False
# ()         -> False
# {}         -> False
# set()      -> False
# range(0)   -> False
```

### Truthy Values (Evaluate to True)

```python
# All these evaluate to True
truthy_values = [
    True,
    1,
    -1,
    3.14,
    "hello",
    " ",
    "False",
    [1, 2],
    (1, 2),
    {"a": 1},
    {1, 2},
    range(1)
]

for val in truthy_values:
    print(f"{repr(val):10} -> {bool(val)}")

# Output:
# True       -> True
# 1          -> True
# -1         -> True
# 3.14       -> True
# 'hello'    -> True
# ' '        -> True
# 'False'    -> True
# [1, 2]     -> True
# (1, 2)     -> True
# {'a': 1}   -> True
# {1, 2}     -> True
# range(1)   -> True
```

### Using Truthy/Falsy in Conditions

```python
# ✅ Pythonic - Direct truthy check
name = "Alice"
if name:
    print(f"Hello, {name}")  # Prints
else:
    print("Name is empty")

# ❌ Unnecessary comparison
if name != "":
    print(f"Hello, {name}")

# Check if list is empty
items = []
if not items:
    print("No items found")  # Prints

# Check if value exists
value = get_value()
if value:
    process(value)
else:
    use_default()

# Default value using or
name = user_input or "Guest"

# Check if number is non-zero
count = 5
if count:
    print(f"Count: {count}")  # Prints

# Multiple truthy checks
if user and user.is_active and user.has_permission:
    grant_access()
```

---

## Comparison Operators

Operators that compare values and return boolean results.

### Complete List

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 3` | `False` |

### Examples

```python
# Numeric comparisons
x = 10
y = 20

print(f"x == y: {x == y}")  # False
print(f"x != y: {x != y}")  # True
print(f"x > y: {x > y}")    # False
print(f"x < y: {x < y}")    # True
print(f"x >= 10: {x >= 10}") # True
print(f"x <= 5: {x <= 5}")   # False

# String comparisons (lexicographic)
print("apple" == "apple")    # True
print("apple" != "banana")   # True
print("apple" < "banana")    # True ('a' < 'b')
print("Apple" < "apple")     # True (ASCII: A=65, a=97)

# Mixed type comparisons
print(5 == 5.0)     # True
print(5 == "5")     # False (different types)
print(True == 1)    # True
print(False == 0)   # True

# Chaining comparisons (Python specific)
x = 5
print(1 < x < 10)   # True (equivalent to 1 < x and x < 10)
print(1 < x < 4)    # False
print(x == 5 == 5)  # True

# Real example: Range check
age = 25
if 18 <= age <= 65:
    print("Working age")
else:
    print("Not working age")
```

---

## Logical Operators

Combine multiple conditions.

### Complete List

| Operator | Meaning | Truth Table |
|----------|---------|-------------|
| `and` | Both must be True | `True and True = True`, else `False` |
| `or` | At least one must be True | `False or False = False`, else `True` |
| `not` | Negation | `not True = False`, `not False = True` |

### Examples with `and`

```python
# Both conditions must be True
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")  # Prints

# Multiple and conditions
if age >= 18 and age <= 65 and has_license:
    print("Working age driver")

# Truth table
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Short-circuit evaluation
def check_true():
    print("Checking True")
    return True

def check_false():
    print("Checking False")
    return False

result = check_false() and check_true()  # Only check_false() runs
# Output: Checking False
```

### Examples with `or`

```python
# At least one condition must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Stay home")  # Prints

# Multiple or conditions
user_type = "premium"
if user_type == "admin" or user_type == "moderator" or user_type == "premium":
    print("Special access")

# Truth table
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Short-circuit evaluation
result = check_true() or check_false()  # Only check_true() runs
# Output: Checking True

# Default values using or
name = user_input or "Guest"
value = cached_value or compute_value()
```

### Examples with `not`

```python
# Negation
is_raining = False

if not is_raining:
    print("Go outside")  # Prints

# Double negation
print(not True)     # False
print(not False)    # True
print(not not True) # True

# With comparisons
x = 5
if not x > 10:
    print("x is not greater than 10")

# Checking emptiness
items = []
if not items:
    print("List is empty")

# Toggle boolean
is_active = True
is_active = not is_active  # False
is_active = not is_active  # True
```

### Operator Precedence

```python
# Order: not > and > or
# not has highest precedence, then and, then or

# Without parentheses
result = True or False and not False
# Evaluated as: True or (False and (not False))
# = True or (False and True)
# = True or False
# = True

# With parentheses (clearer)
result = True or (False and (not False))
print(result)  # True

# Complex example
age = 25
is_member = True
has_coupon = False

if age >= 18 and is_member or has_coupon:
    # Equivalent to: (age >= 18 and is_member) or has_coupon
    print("Discount applies")

# Use parentheses for clarity
if (age >= 18 and is_member) or has_coupon:
    print("Discount applies")
```

---

## Membership and Identity Operators

### Membership Operators (`in`, `not in`)

Check if a value exists in a sequence.

```python
# With strings
text = "Hello World"
if "World" in text:
    print("Found 'World'")  # Prints

if "Python" not in text:
    print("'Python' not found")  # Prints

# With lists
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in stock")

# With tuples
colors = ("red", "green", "blue")
if "yellow" not in colors:
    print("Yellow not available")

# With dictionaries (checks keys)
user = {"name": "Alice", "age": 30}
if "name" in user:
    print(f"Name: {user['name']}")

# Check values
if "Alice" in user.values():
    print("Alice found")

# Multiple membership checks
vowels = "aeiou"
char = "a"
if char in vowels:
    print(f"{char} is a vowel")

# Real example: Command parser
command = input("Enter command: ")
if command in ["quit", "exit", "q"]:
    print("Goodbye!")
    exit()
elif command in ["help", "?"]:
    print("Available commands: quit, help, list")
```

### Identity Operators (`is`, `is not`)

Check if two variables refer to the same object.

```python
# None checking (most common use)
x = None
if x is None:
    print("x is None")  # Prints

if x is not None:
    print("x has value")

# Boolean singletons
flag = True
if flag is True:
    print("Flag is True")  # Works but not recommended

# Better to use direct check
if flag:
    print("Flag is True")

# String interning (may work but don't rely on it)
a = "hello"
b = "hello"
print(a is b)  # May be True (implementation detail)

# Use == for value comparison
print(a == b)  # Always correct

# Custom objects
class Person:
    pass

p1 = Person()
p2 = Person()
p3 = p1

print(p1 is p2)  # False (different objects)
print(p1 is p3)  # True (same object)

# Real use: Checking sentinel values
_sentinel = object()
def get_value(key, default=_sentinel):
    if key in cache:
        return cache[key]
    if default is _sentinel:
        raise KeyError(f"Key {key} not found")
    return default
```

---

## Common Patterns and Best Practices

### Pattern 1: Guard Clauses (Early Returns)

```python
# Without guard clauses (nested)
def process_user(user):
    if user:
        if user.get('name'):
            if user.get('email'):
                return f"Processing {user['name']}"
            else:
                return "Missing email"
        else:
            return "Missing name"
    else:
        return "No user provided"

# With guard clauses (cleaner)
def process_user(user):
    if not user:
        return "No user provided"
    if not user.get('name'):
        return "Missing name"
    if not user.get('email'):
        return "Missing email"
    
    return f"Processing {user['name']}"
```

### Pattern 2: Truthy/Falsy Checks

```python
# ✅ Pythonic
if name:
    print(f"Hello, {name}")

if not items:
    print("No items")

if count:
    print(f"Count: {count}")

# ❌ Unnecessary comparisons
if name != "":
    print(f"Hello, {name}")

if len(items) == 0:
    print("No items")

if count != 0:
    print(f"Count: {count}")
```

### Pattern 3: Multiple Conditions

```python
# Using and/or
if age >= 18 and has_license and not is_suspended:
    print("Can drive")

# Using any() for multiple conditions
conditions = [condition1, condition2, condition3]
if any(conditions):
    print("At least one true")

# Using all() for multiple conditions
if all(conditions):
    print("All true")

# Using in for multiple equality checks
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Weekday")
elif day in ["Saturday", "Sunday"]:
    print("Weekend")
```

### Pattern 4: Chained Comparisons

```python
# ✅ Pythonic
if 0 < x < 10:
    print("x is between 0 and 10")

if 18 <= age <= 65:
    print("Working age")

# ❌ Traditional (more verbose)
if x > 0 and x < 10:
    print("x is between 0 and 10")
```

### Pattern 5: Dictionary Mapping Instead of Multiple If-Elif

```python
# ❌ Many elifs (hard to maintain)
def get_day_name(day_num):
    if day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    # ... many more
    else:
        return "Invalid"

# ✅ Dictionary mapping (cleaner)
def get_day_name(day_num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day_num, "Invalid")

# For functions as values
def handle_admin():
    return "Admin access"

def handle_user():
    return "User access"

def handle_guest():
    return "Guest access"

handlers = {
    "admin": handle_admin,
    "user": handle_user,
    "guest": handle_guest
}

def process_role(role):
    handler = handlers.get(role, handle_guest)
    return handler()
```

### Pattern 6: Short-Circuit Evaluation

```python
# Using or for defaults
name = user_input or "Guest"

# Using and for conditional execution
debug and print("Debug message")

# Safe attribute access
if user and user.is_active and user.has_permission:
    grant_access()

# Lazy evaluation
result = cached_result or expensive_computation()
```

---

## Real-World Examples

### Example 1: Ticket Pricing System

```python
def calculate_ticket_price(age, is_student, is_senior, day_of_week):
    """Calculate ticket price based on various factors"""
    base_price = 20.00
    
    # Age-based discounts
    if age < 5:
        return 0.00  # Free for toddlers
    elif age < 12:
        discount = 0.50  # 50% off for children
    elif age >= 65:
        discount = 0.40  # 40% off for seniors
    elif is_senior:
        discount = 0.30  # 30% off for seniors (alternate)
    else:
        discount = 0.00
    
    # Student discount
    if is_student and not (age < 12 or age >= 65):
        discount = max(discount, 0.25)  # 25% off for students
    
    # Weekend pricing
    if day_of_week in ["Saturday", "Sunday"]:
        if discount > 0:
            discount = max(discount, 0.10)  # At least 10% off on weekends
        else:
            discount = 0.05  # 5% off for regular customers on weekends
    
    # Special events
    is_special_event = day_of_week == "Friday" and age >= 18
    if is_special_event:
        base_price = 25.00
        discount = max(discount, 0.10)
    
    # Calculate final price
    final_price = base_price * (1 - discount)
    
    # Determine ticket type
    if age < 5:
        ticket_type = "Free Toddler"
    elif age < 12:
        ticket_type = "Child"
    elif is_senior or age >= 65:
        ticket_type = "Senior"
    elif is_student:
        ticket_type = "Student"
    else:
        ticket_type = "Adult"
    
    return {
        'ticket_type': ticket_type,
        'original_price': base_price,
        'discount_percent': discount * 100,
        'final_price': round(final_price, 2)
    }

# Test cases
customers = [
    {'age': 3, 'is_student': False, 'is_senior': False, 'day': "Monday"},
    {'age': 10, 'is_student': True, 'is_senior': False, 'day': "Monday"},
    {'age': 25, 'is_student': True, 'is_senior': False, 'day': "Wednesday"},
    {'age': 35, 'is_student': False, 'is_senior': False, 'day': "Saturday"},
    {'age': 70, 'is_student': False, 'is_senior': True, 'day': "Sunday"},
    {'age': 30, 'is_student': False, 'is_senior': False, 'day': "Friday"},
]

for customer in customers:
    result = calculate_ticket_price(**customer)
    print(f"\nAge: {customer['age']}, Student: {customer['is_student']}, Day: {customer['day']}")
    print(f"  Type: {result['ticket_type']}")
    print(f"  Original: ${result['original_price']}")
    print(f"  Discount: {result['discount_percent']}%")
    print(f"  Final: ${result['final_price']}")
```

### Example 2: Login and Authorization System

```python
class AuthorizationSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "admin", "active": True},
            "alice": {"password": "alice123", "role": "user", "active": True},
            "bob": {"password": "bob123", "role": "user", "active": False},
            "moderator": {"password": "mod123", "role": "moderator", "active": True}
        }
        self.max_attempts = 3
        self.lockout_time = 300  # seconds
        self.failed_attempts = {}
    
    def authenticate(self, username, password):
        """Authenticate user"""
        # Check if username exists
        if username not in self.users:
            return False, "Username not found"
        
        user = self.users[username]
        
        # Check if account is locked
        if username in self.failed_attempts:
            attempts, lock_time = self.failed_attempts[username]
            import time
            if time.time() - lock_time < self.lockout_time:
                return False, f"Account locked. Try again later."
        
        # Check if account is active
        if not user["active"]:
            return False, "Account is deactivated"
        
        # Check password
        if user["password"] == password:
            # Reset failed attempts on success
            if username in self.failed_attempts:
                del self.failed_attempts[username]
            return True, "Login successful"
        
        # Track failed attempts
        if username not in self.failed_attempts:
            self.failed_attempts[username] = [1, time.time()]
        else:
            attempts, _ = self.failed_attempts[username]
            attempts += 1
            if attempts >= self.max_attempts:
                import time
                self.failed_attempts[username] = [attempts, time.time()]
                return False, f"Account locked due to too many failed attempts"
            self.failed_attempts[username] = [attempts, time.time()]
        
        remaining = self.max_attempts - self.failed_attempts[username][0]
        return False, f"Invalid password. {remaining} attempts remaining"
    
    def check_permission(self, username, required_role, resource, action):
        """Check if user has permission for action"""
        # First authenticate (in real system, would check session)
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        
        # Check if user is active
        if not user["active"]:
            return False, "Account inactive"
        
        # Role-based access
        role = user["role"]
        
        # Admin has all permissions
        if role == "admin":
            return True, "Access granted (admin)"
        
        # Moderator permissions
        if role == "moderator":
            if action in ["read", "delete"]:
                return True, "Access granted (moderator)"
            else:
                return False, f"Moderators cannot {action}"
        
        # Regular user permissions
        if role == "user":
            if action == "read" and resource != "admin_panel":
                return True, "Access granted (user)"
            elif action == "write" and resource == "profile":
                return True, "Access granted (user)"
            else:
                return False, f"Users cannot {action} {resource}"
        
        return False, "Unknown role"

# Test the system
auth = AuthorizationSystem()

print("LOGIN SYSTEM")
print("=" * 50)

# Test authentication
test_users = [
    ("alice", "alice123"),
    ("alice", "wrong"),
    ("bob", "bob123"),
    ("admin", "admin123"),
    ("unknown", "pass"),
]

for username, password in test_users:
    success, message = auth.authenticate(username, password)
    status = "✅" if success else "❌"
    print(f"{status} {username}: {message}")

print("\n" + "=" * 50)
print("PERMISSION CHECKING")
print("=" * 50)

# Test permissions
tests = [
    ("alice", "read", "profile", "read"),
    ("alice", "write", "profile", "write"),
    ("alice", "delete", "user", "delete"),
    ("moderator", "read", "post", "read"),
    ("moderator", "write", "post", "write"),
    ("admin", "delete", "anything", "delete"),
]

for username, resource, action, _ in tests:
    success, message = auth.check_permission(username, None, resource, action)
    status = "✅" if success else "❌"
    print(f"{status} {username} - {action} {resource}: {message}")
```

### Example 3: Grade Calculator with Weighted Scores

```python
def calculate_grade(assignments, exams, participation, extra_credit=0):
    """
    Calculate final grade with weighted categories
    assignments: list of scores (weight: 40%)
    exams: list of scores (weight: 50%)
    participation: score (weight: 10%)
    extra_credit: bonus points
    """
    # Calculate assignment average
    if assignments:
        assignment_avg = sum(assignments) / len(assignments)
    else:
        assignment_avg = 0
    
    # Calculate exam average
    if exams:
        exam_avg = sum(exams) / len(exams)
    else:
        exam_avg = 0
    
    # Calculate weighted score
    final_score = (
        assignment_avg * 0.40 +
        exam_avg * 0.50 +
        participation * 0.10
    ) + extra_credit
    
    # Cap at 100
    if final_score > 100:
        final_score = 100
    
    # Determine letter grade
    if final_score >= 97:
        letter = "A+"
        gpa = 4.0
        remark = "Excellent!"
    elif final_score >= 93:
        letter = "A"
        gpa = 4.0
        remark = "Excellent!"
    elif final_score >= 90:
        letter = "A-"
        gpa = 3.7
        remark = "Great work!"
    elif final_score >= 87:
        letter = "B+"
        gpa = 3.3
        remark = "Good job!"
    elif final_score >= 83:
        letter = "B"
        gpa = 3.0
        remark = "Good job!"
    elif final_score >= 80:
        letter = "B-"
        gpa = 2.7
        remark = "Satisfactory"
    elif final_score >= 77:
        letter = "C+"
        gpa = 2.3
        remark = "Satisfactory"
    elif final_score >= 73:
        letter = "C"
        gpa = 2.0
        remark = "Need improvement"
    elif final_score >= 70:
        letter = "C-"
        gpa = 1.7
        remark = "Need improvement"
    elif final_score >= 67:
        letter = "D+"
        gpa = 1.3
        remark = "Below average"
    elif final_score >= 63:
        letter = "D"
        gpa = 1.0
        remark = "Below average"
    elif final_score >= 60:
        letter = "D-"
        gpa = 0.7
        remark = "Failing"
    else:
        letter = "F"
        gpa = 0.0
        remark = "Failed"
    
    # Determine if student passes
    if final_score >= 60:
        status = "PASS"
    else:
        status = "FAIL"
    
    return {
        'score': round(final_score, 2),
        'letter': letter,
        'gpa': gpa,
        'status': status,
        'remark': remark,
        'assignment_avg': round(assignment_avg, 2),
        'exam_avg': round(exam_avg, 2)
    }

# Test cases
students = [
    {
        'name': 'Alice',
        'assignments': [85, 90, 88, 92],
        'exams': [88, 91],
        'participation': 95,
        'extra_credit': 2
    },
    {
        'name': 'Bob',
        'assignments': [75, 80, 78, 82],
        'exams': [72, 78],
        'participation': 70,
        'extra_credit': 0
    },
    {
        'name': 'Charlie',
        'assignments': [95, 98, 92, 96],
        'exams': [94, 97],
        'participation': 100,
        'extra_credit': 5
    },
    {
        'name': 'Diana',
        'assignments': [65, 70, 68, 72],
        'exams': [55, 60],
        'participation': 80,
        'extra_credit': 0
    },
]

print("GRADE CALCULATOR")
print("=" * 60)

for student in students:
    result = calculate_grade(
        student['assignments'],
        student['exams'],
        student['participation'],
        student.get('extra_credit', 0)
    )
    
    print(f"\n{student['name']}:")
    print(f"  Assignments Avg: {result['assignment_avg']}")
    print(f"  Exams Avg: {result['exam_avg']}")
    print(f"  Final Score: {result['score']}")
    print(f"  Letter Grade: {result['letter']} (GPA: {result['gpa']})")
    print(f"  Status: {result['status']}")
    print(f"  Remark: {result['remark']}")
```

### Example 4: Shipping Calculator with Multiple Rules

```python
class ShippingCalculator:
    def __init__(self):
        self.shipping_rates = {
            'ground': {'base': 5.99, 'per_kg': 0.50, 'free_threshold': 50},
            'express': {'base': 12.99, 'per_kg': 1.00, 'free_threshold': 100},
            'overnight': {'base': 24.99, 'per_kg': 2.00, 'free_threshold': 200}
        }
    
    def calculate_shipping(self, weight, destination, method='ground', is_member=False, promo_code=None):
        """
        Calculate shipping cost based on various factors
        """
        # Validate inputs
        if weight <= 0:
            return {'error': 'Invalid weight'}
        
        if method not in self.shipping_rates:
            return {'error': f'Unknown shipping method: {method}'}
        
        # Get base rate
        rates = self.shipping_rates[method]
        base_cost = rates['base'] + (weight * rates['per_kg'])
        
        # Apply free shipping threshold
        if base_cost >= rates['free_threshold']:
            base_cost = 0
            free_shipping = True
        else:
            free_shipping = False
        
        # Apply member discount
        member_discount = 0
        if is_member:
            if method == 'ground':
                member_discount = 0.15  # 15% off
            elif method == 'express':
                member_discount = 0.10  # 10% off
            else:
                member_discount = 0.05  # 5% off
        
        # Apply promo code
        promo_discount = 0
        if promo_code:
            if promo_code == 'SHIP20':
                promo_discount = 0.20  # 20% off
            elif promo_code == 'FIRST10':
                promo_discount = 0.10  # 10% off
            elif promo_code == 'FREESHIP' and base_cost > 0:
                promo_discount = 1.00  # 100% off (free shipping)
        
        # Apply the best discount (not cumulative)
        discount = max(member_discount, promo_discount)
        
        # Calculate final cost
        final_cost = base_cost * (1 - discount)
        
        # Apply location surcharge
        location_surcharge = {
            'hawaii': 15.00,
            'alaska': 20.00,
            'international': 25.00,
            'domestic': 0.00
        }
        
        # Determine location category
        if destination.lower() in ['hi', 'hawaii']:
            location = 'hawaii'
        elif destination.lower() in ['ak', 'alaska']:
            location = 'alaska'
        elif destination.lower() in ['us', 'usa', 'continental']:
            location = 'domestic'
        else:
            location = 'international'
        
        final_cost += location_surcharge[location]
        
        # Round to 2 decimals
        final_cost = round(final_cost, 2)
        
        # Determine delivery time
        if method == 'overnight':
            delivery_days = 1
        elif method == 'express':
            delivery_days = 2
        else:
            if location == 'domestic':
                delivery_days = 5
            else:
                delivery_days = 10
        
        return {
            'method': method,
            'base_cost': round(base_cost, 2),
            'discount_applied': discount * 100,
            'final_cost': final_cost,
            'free_shipping': free_shipping,
            'delivery_days': delivery_days,
            'location_surcharge': location_surcharge[location],
            'location': location
        }

# Test the calculator
calculator = ShippingCalculator()

# Test scenarios
orders = [
    {'weight': 2, 'destination': 'US', 'method': 'ground', 'is_member': False},
    {'weight': 10, 'destination': 'US', 'method': 'ground', 'is_member': True},
    {'weight': 3, 'destination': 'US', 'method': 'express', 'is_member': False},
    {'weight': 25, 'destination': 'US', 'method': 'ground', 'is_member': False, 'promo': 'SHIP20'},
    {'weight': 5, 'destination': 'HI', 'method': 'ground', 'is_member': False},
    {'weight': 100, 'destination': 'US', 'method': 'ground', 'is_member': True},
]

print("SHIPPING CALCULATOR")
print("=" * 60)

for i, order in enumerate(orders, 1):
    result = calculator.calculate_shipping(
        weight=order['weight'],
        destination=order['destination'],
        method=order.get('method', 'ground'),
        is_member=order.get('is_member', False),
        promo_code=order.get('promo')
    )
    
    print(f"\nOrder {i}:")
    print(f"  Weight: {order['weight']} kg")
    print(f"  Destination: {order['destination']}")
    print(f"  Method: {result['method']}")
    print(f"  Member: {order.get('is_member', False)}")
    if order.get('promo'):
        print(f"  Promo: {order['promo']}")
    print(f"  Base Cost: ${result['base_cost']}")
    print(f"  Discount: {result['discount_applied']}%")
    print(f"  Location: {result['location']}")
    print(f"  Surcharge: ${result['location_surcharge']}")
    print(f"  Final Cost: ${result['final_cost']}")
    print(f"  Delivery: {result['delivery_days']} days")
    if result['free_shipping']:
        print(f"  🎉 Free Shipping Applied!")
```

---

## Common Pitfalls

### Pitfall 1: Using `=` Instead of `==`

```python
# ❌ WRONG - Assignment instead of comparison
x = 5
if x = 10:  # SyntaxError!
    print("x is 10")

# ✅ CORRECT
if x == 10:
    print("x is 10")
```

### Pitfall 2: Comparing to True/False Unnecessarily

```python
# ❌ Unnecessary comparison
if is_valid == True:
    process()

# ✅ Direct check
if is_valid:
    process()

# ❌ Unnecessary comparison
if is_valid == False:
    process()

# ✅ Direct check
if not is_valid:
    process()
```

### Pitfall 3: Using `is` Instead of `==`

```python
# ❌ Wrong - Use is for identity, not value
if user_input is "yes":
    print("Yes")

# ✅ Correct - Use == for value comparison
if user_input == "yes":
    print("Yes")

# ✅ Use is for None
if value is None:
    print("No value")
```

### Pitfall 4: Forgetting Colon

```python
# ❌ Missing colon
if x > 5  # SyntaxError!
    print("x > 5")

# ✅ Correct
if x > 5:
    print("x > 5")
```

### Pitfall 5: Wrong Indentation

```python
# ❌ Wrong indentation
if x > 5:
print("x > 5")  # IndentationError!

# ✅ Correct
if x > 5:
    print("x > 5")
```

---

## Practice Exercises

### Beginner Level

1. **Even or Odd**
   ```python
   # Write a program that checks if a number is even or odd
   ```

2. **Positive, Negative, or Zero**
   ```python
   # Classify a number as positive, negative, or zero
   ```

3. **Vowel or Consonant**
   ```python
   # Check if a character is a vowel or consonant
   ```

4. **Leap Year Checker**
   ```python
   # Determine if a year is a leap year
   ```

5. **Maximum of Three Numbers**
   ```python
   # Find the largest of three numbers using conditionals
   ```

### Intermediate Level

6. **Grade Calculator**
   ```python
   # Convert numeric score to letter grade (A-F)
   ```

7. **Ticket Price Calculator**
   ```python
   # Calculate ticket price based on age and student status
   ```

8. **Simple Calculator**
   ```python
   # Perform basic arithmetic based on operator input
   ```

9. **Triangle Type**
   ```python
   # Determine if triangle is equilateral, isosceles, or scalene
   ```

10. **Shipping Cost Calculator**
    ```python
    # Calculate shipping cost based on weight and distance
    ```

### Advanced Level

11. **Date Validator**
    ```python
    # Validate if a date (day, month, year) is valid
    ```

12. **Rock Paper Scissors**
    ```python
    # Determine winner between two players
    ```

13. **Quadratic Equation Solver**
    ```python
    # Solve quadratic equation and determine root types
    ```

14. **Bank Account Classifier**
    ```python
    # Classify bank account based on balance and transaction history
    ```

15. **Eligibility Checker**
    ```python
    # Check eligibility for loan based on multiple criteria
    ```

---

## Quick Reference Card

```python
# if statement
if condition:
    # code

# if-else
if condition:
    # code
else:
    # code

# if-elif-else
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Ternary operator
value = true_value if condition else false_value

# Comparison operators
==, !=, >, <, >=, <=

# Logical operators
and, or, not

# Membership operators
in, not in

# Identity operators
is, is not

# Chained comparisons
if 0 < x < 10:
    # code

# Truthy values
True, non-zero numbers, non-empty strings, non-empty collections

# Falsy values
False, None, 0, 0.0, "", [], (), {}, set()

# Common patterns
if value:           # Check if truthy
if not value:       # Check if falsy
if value is None:   # Check for None
if value == True:   # Avoid this
if value:           # Use this instead
```

## Next Step

- Next, move to [04_loop_statements.md](04_loop_statements.md) for understanding `Loops` ie `How to repeat a single code block multiple times`.
- Understand loops to add more functionality to code and repetitiveness.

---

*Master conditionals to control the flow of your programs! 🐍✨*
# 📘 BOOLEANS (bool) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Booleans?](#what-are-booleans)
2. [Creating Booleans](#creating-booleans)
3. [Boolean Operations](#boolean-operations)
4. [Comparison Operators](#comparison-operators)
5. [Truthy and Falsy Values](#truthy-and-falsy-values)
6. [Boolean in Control Flow](#boolean-in-control-flow)
7. [Boolean Functions](#boolean-functions)
8. [Short-Circuit Evaluation](#short-circuit-evaluation)
9. [Real-World Examples](#real-world-examples)
10. [Common Pitfalls](#common-pitfalls)
11. [Performance Tips](#performance-tips)
12. [Practice Exercises](#practice-exercises)

---

## 📖 What are Booleans?

**Booleans** represent one of two values: `True` or `False`. They are a subclass of `int` and are fundamental to logical operations and control flow.

```python
# Boolean values
is_true = True
is_false = False

# Check type
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# Boolean is subclass of int
print(issubclass(bool, int))  # True
print(isinstance(True, int))  # True
print(isinstance(False, int)) # True

# Boolean as integer
print(int(True))    # 1
print(int(False))   # 0
print(True + True)  # 2
print(True * 10)    # 10
print(False - 5)    # -5

# Boolean values are singletons
print(True is True)     # True
print(False is False)   # True
```

---

## 🎯 Creating Booleans

### Method 1: Direct Assignment

```python
# Direct boolean assignment
is_active = True
is_deleted = False
has_permission = True

# Using uppercase T and F (case-sensitive)
# true = True   # NameError! Must be True/False
```

### Method 2: From Comparison Operators

```python
# Numeric comparisons
print(10 > 5)     # True
print(10 < 5)     # False
print(10 == 10)   # True
print(10 != 5)    # True
print(10 >= 10)   # True
print(10 <= 5)    # False

# String comparisons
print("hello" == "hello")   # True
print("hello" != "world")   # True
print("apple" < "banana")   # True (lexicographic)
print("A" < "a")            # True (ASCII order)

# Mixed type comparisons
print(5 == 5.0)     # True
print(5 == "5")     # False (different types)
print(True == 1)    # True
print(False == 0)   # True
```

### Method 3: Using `bool()` Constructor

```python
# From numeric types
print(bool(1))      # True
print(bool(0))      # False
print(bool(-1))     # True
print(bool(3.14))   # True
print(bool(0.0))    # False
print(bool(0j))     # False

# From strings
print(bool("hello"))    # True
print(bool(""))         # False
print(bool("False"))    # True (non-empty string)
print(bool(" "))        # True (space is a character)

# From collections
print(bool([1, 2, 3]))  # True
print(bool([]))         # False
print(bool((1, 2)))     # True
print(bool(()))         # False
print(bool({"a": 1}))   # True
print(bool({}))         # False
print(bool({1, 2}))     # True
print(bool(set()))      # False

# From None
print(bool(None))       # False

# From boolean (returns same value)
print(bool(True))       # True
print(bool(False))      # False
```

### Method 4: From Logical Operations

```python
# Logical operations return booleans
result = (5 > 3) and (10 > 5)   # True
result = (5 > 3) or (5 < 3)     # True
result = not (5 > 3)            # False

# Using any() and all()
numbers = [1, 2, 3, 4, 5]
print(any(n > 10 for n in numbers))   # False
print(all(n > 0 for n in numbers))    # True
```

---

## 🔗 Boolean Operations

### `and` Operator

Returns `True` only if both operands are `True`.

```python
# Truth table
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# With expressions
x = 10
y = 20
print(x > 5 and y > 15)   # True
print(x > 15 and y > 15)  # False

# Chaining and
a, b, c = True, True, True
print(a and b and c)  # True

# Real use: Multiple conditions
age = 25
has_license = True
has_insurance = True

if age >= 18 and has_license and has_insurance:
    print("Can drive")
```

### `or` Operator

Returns `True` if at least one operand is `True`.

```python
# Truth table
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# With expressions
x = 10
y = 20
print(x > 15 or y > 15)   # True
print(x > 15 or y > 25)   # False

# Chaining or
a, b, c = False, False, True
print(a or b or c)  # True

# Real use: Default values
name = input("Enter name: ") or "Guest"
print(f"Hello, {name}")

# Real use: Multiple acceptable conditions
user_type = "premium"
if user_type == "admin" or user_type == "moderator" or user_type == "premium":
    print("Access granted")
```

### `not` Operator

Returns the opposite boolean value.

```python
# Basic negation
print(not True)     # False
print(not False)    # True

# With expressions
x = 10
print(not x > 5)    # False
print(not x > 15)   # True

# Double negation
print(not not True)   # True
print(not not False)  # False

# Real use: Negating conditions
is_weekend = False
if not is_weekend:
    print("Time for work")

# Real use: Checking emptiness
items = []
if not items:
    print("List is empty")

# Real use: Toggle flag
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

# With parentheses for clarity
result = True or (False and (not False))
print(result)  # True

# Complex example
a, b, c = True, False, True
result = a or b and c
# = True or (False and True)
# = True or False
# = True

# Better: Use parentheses for clarity
result = a or (b and c)

# Example with comparisons
age = 25
has_permit = False
result = age >= 16 and not has_permit or has_permit
# = (age >= 16 and (not has_permit)) or has_permit
# = (True and True) or False
# = True
```

---

## 📐 Comparison Operators

### Equality and Inequality

```python
# Equal to (==)
print(5 == 5)       # True
print(5 == 3)       # False
print("hello" == "hello")  # True

# Not equal to (!=)
print(5 != 3)       # True
print(5 != 5)       # False
print("hello" != "world")  # True

# With different types
print(5 == 5.0)     # True
print(5 == "5")     # False
print(True == 1)    # True
print(False == 0)   # True

# Chaining comparisons (Python-specific)
x = 5
print(1 < x < 10)   # True (equivalent to 1 < x and x < 10)
print(1 < x < 4)    # False
```

### Relational Operators

```python
# Greater than (>)
print(10 > 5)       # True
print(5 > 10)       # False
print(5 > 5)        # False

# Less than (<)
print(5 < 10)       # True
print(10 < 5)       # False
print(5 < 5)        # False

# Greater than or equal to (>=)
print(5 >= 5)       # True
print(10 >= 5)      # True
print(3 >= 5)       # False

# Less than or equal to (<=)
print(5 <= 5)       # True
print(3 <= 5)       # True
print(10 <= 5)      # False

# String comparisons (lexicographic)
print("apple" < "banana")   # True ('a' < 'b')
print("Apple" < "apple")    # True (ASCII: A=65, a=97)
print("abc" < "abcd")       # True (shorter string)
```

### Identity Operators

```python
# is - checks if same object
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)   # False (different objects)
print(a is c)   # True (same object)
print(a is not b)  # True

# Boolean singletons
print(True is True)     # True
print(False is False)   # True

# None is singleton
x = None
print(x is None)        # True
print(x is not None)    # False

# Use is for None, not ==
# if x is None:  # Correct
# if x == None:  # Avoid
```

---

## 🔍 Truthy and Falsy Values

### Falsy Values (Evaluate to False)

```python
# All these evaluate to False in boolean context
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

for value in falsy_values:
    print(f"{repr(value):10} -> {bool(value)}")

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
# All these evaluate to True in boolean context
truthy_values = [
    True,
    1,
    -1,
    3.14,
    -3.14,
    "hello",
    " ",
    "False",
    [1, 2],
    (1, 2),
    {"a": 1},
    {1, 2},
    range(1)
]

for value in truthy_values:
    print(f"{repr(value):10} -> {bool(value)}")

# Output:
# True       -> True
# 1          -> True
# -1         -> True
# 3.14       -> True
# -3.14      -> True
# 'hello'    -> True
# ' '        -> True
# 'False'    -> True
# [1, 2]     -> True
# (1, 2)     -> True
# {'a': 1}   -> True
# {1, 2}     -> True
# range(1)   -> True
```

### Using Truthy/Falsy in Practice

```python
# ✅ Pythonic: Direct truthy check
name = "Alice"
if name:
    print(f"Hello, {name}")

# ❌ Unnecessary comparison
if name != "":
    print(f"Hello, {name}")

# ✅ Check if list is empty
items = []
if not items:
    print("No items")

# ❌ Less Pythonic
if len(items) == 0:
    print("No items")

# ✅ Check if value exists
value = get_value()
if value:
    process(value)
else:
    use_default()

# ✅ Default value using or
name = user_input or "Guest"

# ✅ Multiple checks
if user and user.is_active and user.has_permission:
    grant_access()
```

---

## 🎮 Boolean in Control Flow

### If Statements

```python
# Basic if
if condition:
    do_something()

# If-else
if condition:
    do_if_true()
else:
    do_if_false()

# If-elif-else
if condition1:
    do_1()
elif condition2:
    do_2()
elif condition3:
    do_3()
else:
    do_default()

# Nested if
if outer_condition:
    if inner_condition:
        do_both()
    else:
        do_only_outer()

# Real example
def check_access(user):
    if user.is_admin:
        return "Full access"
    elif user.is_moderator:
        return "Moderate access"
    elif user.is_authenticated:
        return "Read-only access"
    else:
        return "No access"
```

### While Loops

```python
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1

# While with boolean flag
is_running = True
count = 0
while is_running:
    count += 1
    if count == 10:
        is_running = False
    print(count)

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# While with continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # Only odd numbers
```

### Ternary Operator (Conditional Expression)

```python
# Syntax: value_if_true if condition else value_if_false

# Basic usage
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

# Multiple conditions
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)  # "B"

# With function calls
def get_discount(is_member):
    return 0.2 if is_member else 0.05

# In print statement
print("Valid" if is_valid else "Invalid")

# In list comprehension
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

## 🔧 Boolean Functions

### `bool()` – Convert to Boolean

```python
# Convert various types to boolean
print(bool(1))       # True
print(bool(0))       # False
print(bool("hi"))    # True
print(bool(""))      # False
print(bool([1]))     # True
print(bool([]))      # False
print(bool(None))    # False

# Custom class with __bool__ method
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __bool__(self):
        return self.value > 0

obj1 = MyClass(5)
obj2 = MyClass(-1)
print(bool(obj1))   # True
print(bool(obj2))   # False
```

### `all()` – Check if All Are True

```python
# Returns True if all elements are truthy
print(all([True, True, True]))     # True
print(all([True, False, True]))    # False
print(all([1, 2, 3]))              # True
print(all([1, 0, 3]))              # False
print(all([]))                     # True (vacuously true)

# With generator expression
numbers = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in numbers))  # True

# Real use: Validate all fields
def validate_user(user):
    required_fields = ['name', 'email', 'age']
    return all(field in user for field in required_fields)

user = {'name': 'Alice', 'email': 'alice@example.com', 'age': 30}
print(validate_user(user))  # True
```

### `any()` – Check if Any Are True

```python
# Returns True if at least one element is truthy
print(any([True, False, False]))   # True
print(any([False, False, False]))  # False
print(any([1, 0, 0]))              # True
print(any([0, 0, 0]))              # False
print(any([]))                     # False

# With generator expression
numbers = [1, 3, 5, 7, 8]
print(any(n % 2 == 0 for n in numbers))  # True

# Real use: Check if any condition met
def has_permission(user):
    return any([
        user.is_admin,
        user.is_moderator,
        user.is_owner
    ])
```

### `isinstance()` – Type Checking

```python
# Check if object is of certain type
print(isinstance(True, bool))     # True
print(isinstance(1, bool))        # False
print(isinstance(True, int))      # True (bool is subclass of int)

# Check multiple types
print(isinstance(5, (int, float)))  # True
print(isinstance(3.14, (int, float)))  # True

# Real use: Type validation
def process_value(value):
    if isinstance(value, bool):
        return "Boolean"
    elif isinstance(value, (int, float)):
        return "Number"
    elif isinstance(value, str):
        return "String"
    else:
        return "Other"
```

### `issubclass()` – Class Hierarchy Check

```python
# Check if class is subclass of another
print(issubclass(bool, int))    # True
print(issubclass(bool, object)) # True
print(issubclass(int, bool))    # False

# Real use: Check type hierarchy
class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
```

---

## ⚡ Short-Circuit Evaluation

### `and` Short-Circuit

```python
# and stops at first False value

def check_true():
    print("Checking True")
    return True

def check_false():
    print("Checking False")
    return False

# Second function never called
result = check_false() and check_true()
print(f"Result: {result}")
# Output:
# Checking False
# Result: False

# First function returns False, second not evaluated
result = False and expensive_operation()  # expensive_operation not called
```

### `or` Short-Circuit

```python
# or stops at first True value

def check_true():
    print("Checking True")
    return True

def check_false():
    print("Checking False")
    return False

# Second function never called
result = check_true() or check_false()
print(f"Result: {result}")
# Output:
# Checking True
# Result: True

# First function returns True, second not evaluated
result = True or expensive_operation()  # expensive_operation not called
```

### Practical Short-Circuit Uses

```python
# Safe attribute access
if user and user.is_active and user.has_permission:
    grant_access()

# Default values (using or)
name = user_input or "Guest"
value = cached_value or compute_value()

# Guard conditions
if not data or len(data) == 0:
    return default_value

# Lazy evaluation
def get_data():
    print("Fetching data...")
    return expensive_computation()

result = cached_result or get_data()  # get_data only called if cached_result is falsy

# Conditional execution
debug and print("Debug message")  # Only prints if debug is True
```

---

## 🌍 Real-World Examples

### Example 1: User Authentication System

```python
class User:
    def __init__(self, username, password, is_active=True, is_admin=False):
        self.username = username
        self.password = password
        self.is_active = is_active
        self.is_admin = is_admin
        self.login_attempts = 0
        self.is_locked = False
    
    def authenticate(self, password):
        """Authenticate user"""
        if self.is_locked:
            return False, "Account is locked"
        
        if not self.is_active:
            return False, "Account is inactive"
        
        if self.password == password:
            self.login_attempts = 0
            return True, "Login successful"
        
        self.login_attempts += 1
        if self.login_attempts >= 3:
            self.is_locked = True
            return False, "Account locked due to too many attempts"
        
        return False, f"Invalid password. {3 - self.login_attempts} attempts remaining"
    
    def has_access(self, resource):
        """Check if user has access to resource"""
        if not self.is_active or self.is_locked:
            return False
        
        if self.is_admin:
            return True
        
        # Regular user access logic
        return resource in ["read", "profile"]

class AuthenticationSystem:
    def __init__(self):
        self.users = {}
        self.session_active = False
        self.current_user = None
    
    def register(self, username, password, is_admin=False):
        """Register new user"""
        if username in self.users:
            return False, "Username already exists"
        
        if not username or not password:
            return False, "Username and password required"
        
        self.users[username] = User(username, password, is_admin=is_admin)
        return True, "Registration successful"
    
    def login(self, username, password):
        """Login user"""
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        success, message = user.authenticate(password)
        
        if success:
            self.session_active = True
            self.current_user = user
        
        return success, message
    
    def logout(self):
        """Logout current user"""
        self.session_active = False
        self.current_user = None
        return True, "Logged out"
    
    def check_permission(self, resource):
        """Check if current user has permission"""
        if not self.session_active or not self.current_user:
            return False
        
        return self.current_user.has_access(resource)

# Usage
auth = AuthenticationSystem()

# Register users
auth.register("alice", "pass123")
auth.register("bob", "bobpass")
auth.register("admin", "admin123", is_admin=True)

# Login attempts
print("=" * 50)
print("LOGIN ATTEMPTS")
print("=" * 50)

# Successful login
success, msg = auth.login("alice", "pass123")
print(f"Alice login: {msg}")

# Check permissions
print(f"Alice can read: {auth.check_permission('read')}")
print(f"Alice can write: {auth.check_permission('write')}")
print(f"Alice can delete: {auth.check_permission('delete')}")

# Logout
auth.logout()

# Failed login attempts (lock account)
print("\n" + "-" * 30)
for i in range(4):
    success, msg = auth.login("bob", "wrong")
    print(f"Bob attempt {i+1}: {msg}")
    if "locked" in msg:
        break

# Admin login
print("\n" + "-" * 30)
auth.login("admin", "admin123")
print(f"Admin can read: {auth.check_permission('read')}")
print(f"Admin can write: {auth.check_permission('write')}")
print(f"Admin can delete: {auth.check_permission('delete')}")
```

### Example 2: Form Validator

```python
class FormValidator:
    def __init__(self):
        self.errors = []
        self.is_valid = True
    
    def validate_required(self, value, field_name):
        """Check if field has value"""
        if not value:
            self.errors.append(f"{field_name} is required")
            self.is_valid = False
            return False
        return True
    
    def validate_email(self, email):
        """Basic email validation"""
        if not email:
            return True  # Skip if not required
        
        has_at = '@' in email
        has_dot = '.' in email.split('@')[-1] if has_at else False
        is_valid = has_at and has_dot and len(email) > 5
        
        if not is_valid:
            self.errors.append("Invalid email format")
            self.is_valid = False
        
        return is_valid
    
    def validate_range(self, value, field_name, min_val, max_val):
        """Check if value is within range"""
        if value is None:
            return True
        
        if not (min_val <= value <= max_val):
            self.errors.append(f"{field_name} must be between {min_val} and {max_val}")
            self.is_valid = False
            return False
        return True
    
    def validate_length(self, value, field_name, min_len, max_len):
        """Check string length"""
        if not value:
            return True
        
        if not (min_len <= len(value) <= max_len):
            self.errors.append(f"{field_name} must be {min_len}-{max_len} characters")
            self.is_valid = False
            return False
        return True
    
    def validate_pattern(self, value, pattern, field_name):
        """Check if value matches pattern (regex)"""
        import re
        if not value:
            return True
        
        if not re.match(pattern, value):
            self.errors.append(f"{field_name} has invalid format")
            self.is_valid = False
            return False
        return True
    
    def validate_match(self, value1, value2, field_name):
        """Check if two values match"""
        if value1 != value2:
            self.errors.append(f"{field_name} values do not match")
            self.is_valid = False
            return False
        return True
    
    def validate_phone(self, phone):
        """Validate phone number"""
        if not phone:
            return True
        
        # Remove non-digits
        digits = ''.join(filter(str.isdigit, phone))
        is_valid = len(digits) == 10
        
        if not is_valid:
            self.errors.append("Phone number must be 10 digits")
            self.is_valid = False
        
        return is_valid
    
    def get_errors(self):
        """Get all validation errors"""
        return self.errors
    
    def is_valid_form(self):
        """Check if form is valid"""
        return self.is_valid

# Usage
def validate_registration_form(data):
    validator = FormValidator()
    
    # Validate required fields
    validator.validate_required(data.get('username'), "Username")
    validator.validate_required(data.get('email'), "Email")
    validator.validate_required(data.get('password'), "Password")
    
    # Validate lengths
    validator.validate_length(data.get('username'), "Username", 3, 20)
    validator.validate_length(data.get('password'), "Password", 6, 50)
    
    # Validate email
    if data.get('email'):
        validator.validate_email(data['email'])
    
    # Validate age
    validator.validate_range(data.get('age'), "Age", 18, 120)
    
    # Validate phone
    validator.validate_phone(data.get('phone'))
    
    # Validate password match
    validator.validate_match(
        data.get('password'),
        data.get('confirm_password'),
        "Password"
    )
    
    return validator

# Test data
test_forms = [
    {
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'pass123',
        'confirm_password': 'pass123',
        'age': 25,
        'phone': '555-123-4567'
    },
    {
        'username': 'a',
        'email': 'invalid-email',
        'password': '123',
        'confirm_password': '456',
        'age': 15,
        'phone': '123'
    },
    {
        'username': '',
        'email': '',
        'password': '',
        'confirm_password': '',
        'age': None,
        'phone': ''
    }
]

print("=" * 50)
print("FORM VALIDATION RESULTS")
print("=" * 50)

for i, form_data in enumerate(test_forms, 1):
    print(f"\nFORM {i}:")
    print(f"Data: {form_data}")
    
    validator = validate_registration_form(form_data)
    
    if validator.is_valid_form():
        print("✅ FORM IS VALID")
    else:
        print("❌ FORM HAS ERRORS:")
        for error in validator.get_errors():
            print(f"   - {error}")
```

### Example 3: Feature Flag System

```python
class FeatureFlags:
    def __init__(self):
        self.flags = {
            'dark_mode': False,
            'beta_features': False,
            'analytics': True,
            'debug_mode': False,
            'cache_enabled': True,
            'new_ui': False
        }
        self.user_overrides = {}
    
    def is_enabled(self, feature, user_id=None):
        """Check if feature is enabled"""
        # Check user-specific override first
        if user_id and user_id in self.user_overrides:
            if feature in self.user_overrides[user_id]:
                return self.user_overrides[user_id][feature]
        
        # Check global flag
        return self.flags.get(feature, False)
    
    def enable(self, feature, user_id=None):
        """Enable feature"""
        if user_id:
            if user_id not in self.user_overrides:
                self.user_overrides[user_id] = {}
            self.user_overrides[user_id][feature] = True
        else:
            self.flags[feature] = True
    
    def disable(self, feature, user_id=None):
        """Disable feature"""
        if user_id:
            if user_id not in self.user_overrides:
                self.user_overrides[user_id] = {}
            self.user_overrides[user_id][feature] = False
        else:
            self.flags[feature] = False
    
    def get_enabled_features(self, user_id=None):
        """Get all enabled features"""
        enabled = []
        for feature in self.flags:
            if self.is_enabled(feature, user_id):
                enabled.append(feature)
        return enabled
    
    def get_percentage_enabled(self):
        """Get percentage of features enabled"""
        if not self.flags:
            return 0
        enabled_count = sum(1 for f in self.flags if self.flags[f])
        return (enabled_count / len(self.flags)) * 100

# Usage
flags = FeatureFlags()

print("=" * 50)
print("FEATURE FLAG SYSTEM")
print("=" * 50)

# Check features
print("\nGLOBAL FEATURES:")
for feature in flags.flags:
    status = "✅ ENABLED" if flags.is_enabled(feature) else "❌ DISABLED"
    print(f"  {feature}: {status}")

print(f"\nEnabled features: {flags.get_enabled_features()}")
print(f"Percentage enabled: {flags.get_percentage_enabled():.1f}%")

# Enable features
print("\n" + "-" * 30)
print("ENABLING FEATURES:")
flags.enable('dark_mode')
flags.enable('beta_features')
print(f"Dark mode enabled: {flags.is_enabled('dark_mode')}")
print(f"Beta features enabled: {flags.is_enabled('beta_features')}")

# User-specific overrides
print("\n" + "-" * 30)
print("USER-SPECIFIC OVERRIDES:")
flags.disable('dark_mode', user_id='alice')
flags.enable('new_ui', user_id='alice')

print(f"Alice - Dark mode: {flags.is_enabled('dark_mode', 'alice')}")
print(f"Alice - New UI: {flags.is_enabled('new_ui', 'alice')}")
print(f"Bob - Dark mode: {flags.is_enabled('dark_mode', 'bob')}")

# Feature-dependent logic
print("\n" + "-" * 30)
print("FEATURE-DEPENDENT BEHAVIOR:")

def render_ui(user_id):
    if flags.is_enabled('new_ui', user_id):
        return "Rendering NEW UI"
    else:
        return "Rendering OLD UI"

def log_analytics(event):
    if flags.is_enabled('analytics'):
        print(f"Logging analytics: {event}")

print(f"Alice UI: {render_ui('alice')}")
print(f"Bob UI: {render_ui('bob')}")

log_analytics("page_view")
```

### Example 4: Permission Checker

```python
class PermissionChecker:
    def __init__(self):
        self.user_roles = {}
        self.role_permissions = {
            'admin': {'read', 'write', 'delete', 'manage_users', 'manage_roles'},
            'moderator': {'read', 'delete', 'ban_users'},
            'editor': {'read', 'write', 'publish'},
            'viewer': {'read'}
        }
    
    def assign_role(self, user_id, role):
        """Assign role to user"""
        if role not in self.role_permissions:
            return False, f"Role '{role}' does not exist"
        
        if user_id not in self.user_roles:
            self.user_roles[user_id] = set()
        
        self.user_roles[user_id].add(role)
        return True, f"Assigned {role} to {user_id}"
    
    def has_permission(self, user_id, permission):
        """Check if user has specific permission"""
        if user_id not in self.user_roles:
            return False
        
        user_permissions = set()
        for role in self.user_roles[user_id]:
            user_permissions.update(self.role_permissions.get(role, set()))
        
        return permission in user_permissions
    
    def has_any_permission(self, user_id, permissions):
        """Check if user has any of the permissions"""
        return any(self.has_permission(user_id, p) for p in permissions)
    
    def has_all_permissions(self, user_id, permissions):
        """Check if user has all permissions"""
        return all(self.has_permission(user_id, p) for p in permissions)
    
    def get_user_permissions(self, user_id):
        """Get all permissions for user"""
        if user_id not in self.user_roles:
            return set()
        
        permissions = set()
        for role in self.user_roles[user_id]:
            permissions.update(self.role_permissions.get(role, set()))
        
        return permissions
    
    def can_access_resource(self, user_id, resource, action):
        """Check if user can perform action on resource"""
        # Admin has full access
        if self.has_permission(user_id, 'manage_users'):
            return True
        
        # Check specific permission
        permission = f"{action}_{resource}"
        return self.has_permission(user_id, permission)

# Usage
checker = PermissionChecker()

# Assign roles
checker.assign_role('alice', 'admin')
checker.assign_role('bob', 'editor')
checker.assign_role('charlie', 'viewer')
checker.assign_role('david', 'moderator')

print("=" * 50)
print("PERMISSION CHECKER")
print("=" * 50)

users = ['alice', 'bob', 'charlie', 'david']

for user in users:
    print(f"\n{user.upper()}:")
    print(f"  Roles: {checker.user_roles.get(user, 'None')}")
    print(f"  Permissions: {checker.get_user_permissions(user)}")
    print(f"  Has 'read': {checker.has_permission(user, 'read')}")
    print(f"  Has 'write': {checker.has_permission(user, 'write')}")
    print(f"  Has 'delete': {checker.has_permission(user, 'delete')}")
    print(f"  Has 'ban_users': {checker.has_permission(user, 'ban_users')}")
    print(f"  Has 'read' or 'write': {checker.has_any_permission(user, ['read', 'write'])}")
    print(f"  Has 'read' and 'write': {checker.has_all_permissions(user, ['read', 'write'])}")

print("\n" + "-" * 30)
print("ACCESS CONTROL:")

def check_access(user_id, resource, action):
    if checker.has_permission(user_id, 'manage_users'):
        print(f"  {user_id} (admin): Full access to {resource}")
    elif checker.has_permission(user_id, f"{action}_{resource}"):
        print(f"  {user_id}: Can {action} {resource}")
    else:
        print(f"  {user_id}: Cannot {action} {resource}")

check_access('alice', 'user', 'delete')
check_access('bob', 'article', 'publish')
check_access('charlie', 'article', 'write')
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Using `is` Instead of `==`

```python
# ❌ WRONG - Using is for value comparison
value = True
if value is True:  # Works but not recommended for booleans
    print("True")

# ✅ CORRECT - Use == for value comparison
if value == True:
    print("True")

# ✅ BETTER - Use direct boolean check
if value:
    print("True")

# ❌ WRONG - is works for True/False but not for other truthy values
if "hello" is True:  # False! "hello" is truthy but not True
    print("This won't print")

# ✅ CORRECT - Use direct check
if "hello":
    print("This will print")
```

### Pitfall 2: Comparing to True/False Unnecessarily

```python
# ❌ Unnecessary comparison
if is_valid == True:
    process()

# ✅ Direct boolean check
if is_valid:
    process()

# ❌ Unnecessary comparison for falsy
if is_valid == False:
    process()

# ✅ Direct boolean check
if not is_valid:
    process()
```

### Pitfall 3: Truthy/Falsy Confusion

```python
# These are all truthy
print(bool(1))      # True
print(bool(-1))     # True
print(bool("False")) # True
print(bool([0]))    # True

# These are all falsy
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False

# Be careful with empty strings
name = ""
if name:
    print("Has name")  # Won't print
else:
    print("No name")   # Will print

# Be careful with zero
count = 0
if count:
    print("Has items")  # Won't print
else:
    print("No items")   # Will print
```

### Pitfall 4: Short-Circuit Surprises

```python
# and returns the first falsy value or last truthy value
result = 0 and 100
print(result)  # 0 (not False!)

result = 5 and 10
print(result)  # 10 (not True!)

# or returns the first truthy value or last falsy value
result = 5 or 10
print(result)  # 5 (not True!)

result = 0 or None
print(result)  # None (not False!)

# Use bool() if you need actual boolean
result = bool(5 and 10)
print(result)  # True

# Use in conditions directly (works fine)
if 5 and 10:
    print("Both truthy")  # This works
```

---

## ⚡ Performance Tips

### Boolean Operations Are Fast

```python
import timeit

# Direct boolean check is fastest
def check_direct(value):
    return value

def check_comparison(value):
    return value == True

def check_identity(value):
    return value is True

# Boolean operations are very fast
time_direct = timeit.timeit('check_direct(True)', globals=globals(), number=10000000)
time_comparison = timeit.timeit('check_comparison(True)', globals=globals(), number=10000000)
time_identity = timeit.timeit('check_identity(True)', globals=globals(), number=10000000)

print(f"Direct: {time_direct:.4f}s (fastest)")
print(f"Comparison: {time_comparison:.4f}s")
print(f"Identity: {time_identity:.4f}s")
```

### Use `any()` and `all()` for Multiple Conditions

```python
# ❌ SLOWER - Multiple or conditions
if cond1 or cond2 or cond3 or cond4 or cond5:
    pass

# ✅ FASTER - Using any()
conditions = [cond1, cond2, cond3, cond4, cond5]
if any(conditions):
    pass

# ❌ SLOWER - Multiple and conditions
if cond1 and cond2 and cond3 and cond4 and cond5:
    pass

# ✅ FASTER - Using all()
if all(conditions):
    pass
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Even/Odd Checker**
   ```python
   # Write function that returns True if number is even
   # Example: is_even(4) → True, is_even(5) → False
   ```

2. **Vowel Checker**
   ```python
   # Check if character is a vowel (a, e, i, o, u)
   # Example: is_vowel('a') → True, is_vowel('b') → False
   ```

3. **Leap Year Checker**
   ```python
   # Check if year is leap year
   # Leap year: divisible by 4, not by 100 unless also by 400
   ```

### Intermediate Level

4. **Password Validator**
   ```python
   # Check password strength (length, uppercase, lowercase, digits, special)
   # Return boolean and list of missing requirements
   ```

5. **Prime Number Checker**
   ```python
   # Check if number is prime
   # Return True if prime, False otherwise
   ```

6. **Palindrome Checker**
   ```python
   # Check if string reads same forwards and backwards
   # Example: "racecar" → True, "hello" → False
   ```

### Advanced Level

7. **Sudoku Validator**
   ```python
   # Check if Sudoku board is valid
   # Rows, columns, and 3x3 boxes must have unique 1-9
   ```

8. **Bracket Matcher**
   ```python
   # Check if brackets in expression are properly matched
   # Example: "{[()]}" → True, "{[(])}" → False
   ```

9. **Truth Table Generator**
   ```python
   # Generate truth table for logical expressions
   # Support and, or, not operations
   ```

---

## 📚 Quick Reference Card

```python
# Boolean values
True                    # Boolean true
False                   # Boolean false

# Boolean operations
a and b                 # Logical AND (short-circuits)
a or b                  # Logical OR (short-circuits)
not a                   # Logical NOT

# Comparison operators
a == b                  # Equal to
a != b                  # Not equal to
a > b                   # Greater than
a < b                   # Less than
a >= b                  # Greater than or equal to
a <= b                  # Less than or equal to
a is b                  # Same object
a is not b              # Different objects

# Truthy values
True, 1, -1, 3.14, "text", [1], (1,), {1:1}, {1}, range(1)

# Falsy values
False, 0, 0.0, 0j, "", [], (), {}, set(), None, range(0)

# Boolean functions
bool(x)                 # Convert to boolean
all(iterable)           # True if all truthy
any(iterable)           # True if any truthy

# Conditional expression
value_if_true if condition else value_if_false

# Common patterns
if condition:           # Check if truthy
if not condition:       # Check if falsy
if condition1 and condition2:  # Both true
if condition1 or condition2:   # At least one true
```

---

*Master booleans for logical operations and control flow! 🐍✨*
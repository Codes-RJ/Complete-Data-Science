Here's the **`03_ternary_operator.md`** file - complete guide to ternary operators (conditional expressions) in Python.

---

# 📘 TERNARY OPERATOR – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Ternary Operator?](#what-is-the-ternary-operator)
2. [Basic Syntax](#basic-syntax)
3. [Ternary with Different Types](#ternary-with-different-types)
4. [Nested Ternary Operators](#nested-ternary-operators)
5. [Ternary with Functions](#ternary-with-functions)
6. [Ternary in List Comprehensions](#ternary-in-list-comprehensions)
7. [Ternary vs Traditional if-else](#ternary-vs-traditional-if-else)
8. [Real-World Examples](#real-world-examples)
9. [Common Pitfalls](#common-pitfalls)
10. [Practice Exercises](#practice-exercises)

---

## What is the Ternary Operator?

The **ternary operator** (also called conditional expression) is a one-line shorthand for an `if-else` statement. It's called "ternary" because it takes three operands.

```python
# Traditional if-else
if condition:
    result = value_if_true
else:
    result = value_if_false

# Ternary operator (one line)
result = value_if_true if condition else value_if_false
```

**Key Characteristics:**
- ✅ Concise one-line conditional
- ✅ Returns a value (can be assigned)
- ✅ Can be nested (but use sparingly)
- ✅ Executes faster than if-else in some cases
- ⚠️ Can reduce readability if overused

---

## Basic Syntax

### Syntax

```python
value_if_true if condition else value_if_false
```

### Simple Examples

```python
# Basic assignment
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# With numbers
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result)  # Positive

# With expressions
a, b = 5, 10
max_value = a if a > b else b
print(max_value)  # 10

# In print statement
x = 5
print("Even" if x % 2 == 0 else "Odd")  # Odd

# With multiple conditions
age = 25
has_license = True
can_drive = "Yes" if age >= 18 and has_license else "No"
print(can_drive)  # Yes
```

### Ternary vs Traditional if-else

```python
# Traditional if-else (4 lines)
if score >= 60:
    result = "Pass"
else:
    result = "Fail"

# Ternary operator (1 line)
result = "Pass" if score >= 60 else "Fail"

# Both produce same result
print(result)
```

---

## Ternary with Different Types

### With Strings

```python
name = "Alice"
greeting = "Hello" if name else "Guest"
print(greeting)  # Hello

# With string methods
text = "hello"
result = text.upper() if len(text) > 3 else text
print(result)  # HELLO

# Conditional string formatting
price = 100
message = f"Expensive: ${price}" if price > 50 else f"Cheap: ${price}"
print(message)  # Expensive: $100
```

### With Numbers

```python
# Absolute value
x = -5
abs_x = x if x >= 0 else -x
print(abs_x)  # 5

# Clamp value between min and max
value = 150
min_val, max_val = 0, 100
clamped = min_val if value < min_val else max_val if value > max_val else value
print(clamped)  # 100

# Sign of number
x = -10
sign = "positive" if x > 0 else "negative" if x < 0 else "zero"
print(sign)  # negative
```

### With Lists

```python
# Check if list is empty
my_list = [1, 2, 3]
result = my_list if my_list else "Empty"
print(result)  # [1, 2, 3]

empty_list = []
result = empty_list if empty_list else "Empty"
print(result)  # Empty

# First element or default
first = my_list[0] if my_list else None
print(first)  # 1

# List length comparison
list1, list2 = [1, 2], [1, 2, 3]
longer = list1 if len(list1) > len(list2) else list2
print(longer)  # [1, 2, 3]
```

### With Dictionaries

```python
# Get value or default
data = {"name": "Alice"}
value = data.get("name") if "name" in data else "Unknown"
print(value)  # Alice

# Update dictionary based on condition
is_valid = True
result = {"status": "success"} if is_valid else {"status": "error"}
print(result)  # {'status': 'success'}

# Conditional dictionary merge
defaults = {"theme": "dark", "font": "Arial"}
user_prefs = {"theme": "light"}
merged = {**defaults, **user_prefs} if user_prefs else defaults
print(merged)  # {'theme': 'light', 'font': 'Arial'}
```

---

## Nested Ternary Operators

Nested ternaries allow multiple conditions in one line.

### Basic Nesting

```python
# Grade calculator with nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(grade)  # B

# Number classification
x = 5
result = "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(result)  # Positive

# Age classification
age = 25
category = "Child" if age < 13 else "Teen" if age < 20 else "Adult" if age < 65 else "Senior"
print(category)  # Adult
```

### Readable Nesting (with parentheses)

```python
# Using parentheses for clarity
score = 85
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print(grade)  # B

# Temperature classification
temp = 75
feeling = (
    "Hot" if temp > 85 else
    "Warm" if temp > 70 else
    "Cool" if temp > 55 else
    "Cold"
)
print(feeling)  # Warm
```

### When to Avoid Nesting

```python
# ❌ Too complex - hard to read
result = "A" if x > 10 else "B" if x > 5 else "C" if x > 0 else "D" if x > -5 else "E"

# ✅ Better - use traditional if-elif-else
if x > 10:
    result = "A"
elif x > 5:
    result = "B"
elif x > 0:
    result = "C"
elif x > -5:
    result = "D"
else:
    result = "E"
```

---

## Ternary with Functions

### Returning from Functions

```python
def get_status(score):
    return "Pass" if score >= 60 else "Fail"

print(get_status(85))  # Pass
print(get_status(45))  # Fail

def min_value(a, b):
    return a if a < b else b

print(min_value(10, 20))  # 10

def absolute_value(x):
    return x if x >= 0 else -x

print(absolute_value(-5))  # 5
```

### Calling Functions in Ternary

```python
def process_success(data):
    return f"Processed: {data}"

def process_error(error):
    return f"Error: {error}"

is_valid = True
data = "user_data"
result = process_success(data) if is_valid else process_error("Invalid data")
print(result)  # Processed: user_data

# With function arguments
def calculate_bonus(salary, performance):
    return salary * 0.2 if performance == "excellent" else salary * 0.1 if performance == "good" else 0

print(calculate_bonus(50000, "excellent"))  # 10000.0
print(calculate_bonus(50000, "good"))       # 5000.0
print(calculate_bonus(50000, "poor"))       # 0
```

### Lambda with Ternary

```python
# Lambda function using ternary
max_func = lambda a, b: a if a > b else b
print(max_func(10, 20))  # 20

min_func = lambda a, b: a if a < b else b
print(min_func(10, 20))  # 10

absolute = lambda x: x if x >= 0 else -x
print(absolute(-7))  # 7

# In map() with ternary
numbers = [1, -2, 3, -4, 5]
absolute_numbers = list(map(lambda x: x if x >= 0 else -x, numbers))
print(absolute_numbers)  # [1, 2, 3, 4, 5]
```

---

## Ternary in List Comprehensions

### Basic Usage

```python
# Replace even numbers with "Even", odd with "Odd"
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Absolute values
numbers = [-5, 3, -2, 7, -1]
abs_values = [n if n >= 0 else -n for n in numbers]
print(abs_values)  # [5, 3, 2, 7, 1]

# Categorize ages
ages = [12, 18, 25, 65, 70]
categories = ["Child" if age < 18 else "Adult" if age < 65 else "Senior" for age in ages]
print(categories)  # ['Child', 'Adult', 'Adult', 'Adult', 'Senior']
```

### Complex Examples

```python
# Multiple conditions in comprehension
scores = [85, 45, 92, 58, 77]
grades = [
    "A" if s >= 90 else
    "B" if s >= 80 else
    "C" if s >= 70 else
    "D" if s >= 60 else
    "F"
    for s in scores
]
print(grades)  # ['B', 'F', 'A', 'F', 'C']

# With function call
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 11)
labels = ["Prime" if is_prime(n) else "Composite" for n in numbers]
print(labels)  # ['Composite', 'Prime', 'Prime', 'Composite', 'Prime', 'Composite', 'Prime', 'Composite', 'Composite', 'Composite']

# Nested list comprehension with ternary
matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
abs_matrix = [[abs_val if abs_val >= 0 else -abs_val for abs_val in row] for row in matrix]
print(abs_matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Ternary vs Traditional if-else

### Performance Comparison

```python
import timeit

# Traditional if-else
def traditional(x):
    if x > 0:
        return "Positive"
    else:
        return "Non-positive"

# Ternary operator
def ternary(x):
    return "Positive" if x > 0 else "Non-positive"

# Performance test
traditional_time = timeit.timeit(lambda: traditional(5), number=1000000)
ternary_time = timeit.timeit(lambda: ternary(5), number=1000000)

print(f"Traditional: {traditional_time:.4f}s")
print(f"Ternary: {ternary_time:.4f}s")
print(f"Ternary is {traditional_time/ternary_time:.2f}x faster")
```

### Readability Comparison

```python
# ✅ Good use of ternary (simple condition)
status = "Active" if is_active else "Inactive"

# ✅ Good use of ternary (assignment)
max_value = a if a > b else b

# ❌ Bad use of ternary (complex condition)
result = process_data(data) if validate(data) and check_permission(user) and data_available else handle_error()

# ✅ Better as traditional if-else
if validate(data) and check_permission(user) and data_available:
    result = process_data(data)
else:
    result = handle_error()
```

### When to Use Ternary

| Use Case | Recommendation | Example |
|----------|---------------|---------|
| Simple assignment | ✅ Yes | `status = "OK" if valid else "Error"` |
| Return value | ✅ Yes | `return a if a > b else b` |
| Print statement | ✅ Yes | `print("Yes" if condition else "No")` |
| List comprehension | ✅ Yes | `[x if x>0 else 0 for x in numbers]` |
| Complex logic | ❌ No | Use traditional if-elif-else |
| Multiple conditions | ❌ No | Use traditional if-elif-else |
| Side effects | ❌ No | Use traditional if-else |

---

## Real-World Examples

### Example 1: User Status Display

```python
class User:
    def __init__(self, name, age, is_active, last_login):
        self.name = name
        self.age = age
        self.is_active = is_active
        self.last_login = last_login

def get_user_status(user):
    """Get user status badge using ternary operators"""
    
    # Age category
    age_group = "Minor" if user.age < 18 else "Adult" if user.age < 65 else "Senior"
    
    # Activity status
    activity = "Active" if user.is_active else "Inactive"
    
    # Recent activity
    from datetime import datetime, timedelta
    days_since_login = (datetime.now() - user.last_login).days
    recent = "Recent" if days_since_login < 7 else "Inactive" if days_since_login < 30 else "Long absent"
    
    # Combine status
    status = f"{age_group} | {activity} | {recent}"
    
    return status

# Test users
from datetime import datetime, timedelta

users = [
    User("Alice", 25, True, datetime.now() - timedelta(days=3)),
    User("Bob", 16, True, datetime.now() - timedelta(days=10)),
    User("Charlie", 70, False, datetime.now() - timedelta(days=45)),
    User("Diana", 30, True, datetime.now() - timedelta(days=1)),
]

print("USER STATUS DASHBOARD")
print("=" * 50)

for user in users:
    status = get_user_status(user)
    print(f"{user.name:10} | {status}")
```

### Example 2: Price Calculator with Discounts

```python
class PriceCalculator:
    @staticmethod
    def calculate(price, quantity, is_member, coupon_code, is_bulk):
        """Calculate final price with multiple discounts using ternary"""
        
        # Base price
        subtotal = price * quantity
        
        # Member discount
        member_discount = 0.15 if is_member else 0.05 if coupon_code else 0
        subtotal_after_member = subtotal * (1 - member_discount)
        
        # Bulk discount
        bulk_discount = 0.10 if is_bulk and quantity >= 10 else 0
        subtotal_after_bulk = subtotal_after_member * (1 - bulk_discount)
        
        # Coupon discount (applied after other discounts)
        coupon_value = 20 if coupon_code == "SAVE20" else 10 if coupon_code == "SAVE10" else 0
        final_price = subtotal_after_bulk - coupon_value if coupon_value else subtotal_after_bulk
        
        # Ensure price is not negative
        final_price = final_price if final_price > 0 else 0
        
        # Format results
        discount_summary = {
            "member": f"{member_discount * 100:.0f}%" if member_discount else "None",
            "bulk": f"{bulk_discount * 100:.0f}%" if bulk_discount else "None",
            "coupon": f"${coupon_value}" if coupon_value else "None"
        }
        
        return {
            'subtotal': round(subtotal, 2),
            'final_price': round(final_price, 2),
            'saved': round(subtotal - final_price, 2),
            'discounts': discount_summary
        }

# Test cases
test_cases = [
    {"price": 100, "quantity": 1, "is_member": True, "coupon_code": "", "is_bulk": False},
    {"price": 50, "quantity": 3, "is_member": False, "coupon_code": "SAVE10", "is_bulk": False},
    {"price": 25, "quantity": 10, "is_member": True, "coupon_code": "SAVE20", "is_bulk": True},
    {"price": 30, "quantity": 2, "is_member": False, "coupon_code": "", "is_bulk": False},
]

print("PRICE CALCULATOR")
print("=" * 60)

for i, test in enumerate(test_cases, 1):
    result = PriceCalculator.calculate(**test)
    print(f"\nOrder {i}:")
    print(f"  Subtotal: ${result['subtotal']}")
    print(f"  Discounts: Member: {result['discounts']['member']}, Bulk: {result['discounts']['bulk']}, Coupon: {result['discounts']['coupon']}")
    print(f"  Final Price: ${result['final_price']}")
    print(f"  You Saved: ${result['saved']}")
```

### Example 3: Form Field Validator

```python
class FormValidator:
    @staticmethod
    def validate_field(value, field_type, required=True, min_len=None, max_len=None):
        """Validate form field using ternary operators"""
        
        # Required check
        if required and not value:
            return "Field is required"
        
        # Type validation
        if value:
            type_valid = (
                isinstance(value, str) if field_type == "string" else
                isinstance(value, int) if field_type == "integer" else
                isinstance(value, float) if field_type == "float" else
                isinstance(value, bool) if field_type == "boolean" else
                isinstance(value, list) if field_type == "list" else
                True
            )
            
            if not type_valid:
                return f"Must be {field_type} type"
        
        # Length validation for strings
        if field_type == "string" and value:
            len_valid = (
                "Valid" if min_len is None or len(value) >= min_len else f"Minimum {min_len} characters"
            )
            if len_valid != "Valid":
                return len_valid
            
            len_valid = (
                "Valid" if max_len is None or len(value) <= max_len else f"Maximum {max_len} characters"
            )
            if len_valid != "Valid":
                return len_valid
        
        # Range validation for numbers
        if field_type in ["integer", "float"] and value is not None:
            range_valid = (
                "Valid" if min_len is None or value >= min_len else f"Minimum value is {min_len}"
            )
            if range_valid != "Valid":
                return range_valid
            
            range_valid = (
                "Valid" if max_len is None or value <= max_len else f"Maximum value is {max_len}"
            )
            if range_valid != "Valid":
                return range_valid
        
        return "Valid"

# Test the validator
print("FORM VALIDATOR")
print("=" * 50)

test_fields = [
    {"value": "", "field_type": "string", "required": True},
    {"value": "John", "field_type": "string", "required": True, "min_len": 2, "max_len": 10},
    {"value": "A", "field_type": "string", "min_len": 2},
    {"value": 25, "field_type": "integer", "required": True, "min_len": 18, "max_len": 65},
    {"value": 15, "field_type": "integer", "min_len": 18},
    {"value": 3.14, "field_type": "float"},
    {"value": "not_number", "field_type": "integer"},
]

for test in test_fields:
    result = FormValidator.validate_field(**test)
    status = "✓" if result == "Valid" else "✗"
    print(f"{status} {test['value']:12} -> {result}")
```

### Example 4: Data Transformation Pipeline

```python
class DataTransformer:
    @staticmethod
    def transform_value(value, transform_type):
        """Transform value based on type using ternary"""
        
        # Type conversion
        converted = (
            str(value) if transform_type == "string" else
            int(value) if transform_type == "integer" and value is not None else
            float(value) if transform_type == "float" and value is not None else
            bool(value) if transform_type == "boolean" else
            value
        )
        
        # Apply formatting
        formatted = (
            converted.lower() if transform_type == "string" and isinstance(converted, str) else
            f"${converted:.2f}" if transform_type == "currency" else
            f"{converted}%" if transform_type == "percentage" else
            converted
        )
        
        return formatted
    
    @staticmethod
    def process_row(row, schema):
        """Process entire row using ternary in comprehension"""
        return {
            field: DataTransformer.transform_value(
                row.get(field), 
                rules.get("type", "string")
            )
            for field, rules in schema.items()
        }

# Schema definition
schema = {
    "name": {"type": "string"},
    "age": {"type": "integer"},
    "score": {"type": "float"},
    "active": {"type": "boolean"},
    "salary": {"type": "currency"},
    "completion": {"type": "percentage"}
}

# Sample data
data_rows = [
    {"name": "ALICE", "age": "25", "score": "85.5", "active": "true", "salary": 50000, "completion": 0.85},
    {"name": "BOB", "age": "30", "score": "92.3", "active": "false", "salary": 60000, "completion": 0.92},
    {"name": "CHARLIE", "age": "invalid", "score": "78.9", "active": "yes", "salary": 55000, "completion": 0.78},
]

print("DATA TRANSFORMATION PIPELINE")
print("=" * 60)

for i, row in enumerate(data_rows, 1):
    print(f"\nRow {i}:")
    original = row
    transformed = DataTransformer.process_row(row, schema)
    
    for key in schema:
        print(f"  {key:10} : {original.get(key):15} -> {transformed[key]}")
```

---

## Common Pitfalls

### Pitfall 1: Forgetting the else Clause

```python
# ❌ SyntaxError - missing else
# result = "True" if condition  # SyntaxError!

# ✅ Correct - must have else
result = "True" if condition else "False"
```

### Pitfall 2: Using Ternary for Side Effects

```python
# ❌ Bad - ternary for side effects
print("Hello") if condition else print("Goodbye")

# ✅ Better - use traditional if-else
if condition:
    print("Hello")
else:
    print("Goodbye")
```

### Pitfall 3: Too Complex Nesting

```python
# ❌ Unreadable
result = "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D" if x > 60 else "F"

# ✅ Better - use traditional if-elif-else
if x > 90:
    result = "A"
elif x > 80:
    result = "B"
elif x > 70:
    result = "C"
elif x > 60:
    result = "D"
else:
    result = "F"
```

### Pitfall 4: Precedence Issues

```python
# ❌ Wrong - operator precedence
x = 5
result = "Even" if x % 2 == 0 else "Odd" + " number"  # "Odd number" only for Odd

# ✅ Correct - use parentheses
result = "Even" if x % 2 == 0 else "Odd" + " number"
# Or better:
result = ("Even" if x % 2 == 0 else "Odd") + " number"
```

---

## Practice Exercises

### Beginner Level

1. **Max of Two**
   ```python
   # Use ternary to return larger of two numbers
   # Example: 5, 10 -> 10
   ```

2. **Even or Odd Label**
   ```python
   # Return "Even" if number is even, "Odd" if odd
   # Example: 4 -> "Even", 7 -> "Odd"
   ```

3. **Absolute Value**
   ```python
   # Return absolute value using ternary
   # Example: -5 -> 5, 3 -> 3
   ```

### Intermediate Level

4. **Grade Letter**
   ```python
   # Convert score to letter grade using nested ternary
   # 90+ = A, 80+ = B, 70+ = C, 60+ = D, else F
   ```

5. **List Transformation**
   ```python
   # Use ternary in list comprehension
   # Convert negatives to 0, keep positives
   # Example: [-5, 3, -2, 7] -> [0, 3, 0, 7]
   ```

6. **Discount Calculator**
   ```python
   # Apply discount based on membership and amount
   # Members get 10% off, non-members get 5% off if amount > 100
   ```

### Advanced Level

7. **Nested Ternary with Functions**
   ```python
   # Create function that returns different messages based on score
   # Use nested ternary
   ```

8. **Data Cleaner**
   ```python
   # Use ternary in comprehension to clean data
   # Replace None with 0, empty string with "N/A"
   ```

9. **Conditional Formatter**
   ```python
   # Format numbers: add $ for currency, % for percentage
   # Based on format type parameter using ternary
   ```

---

## Quick Reference Card

```python
# Basic ternary
value = true_value if condition else false_value

# With expressions
value = (a + b) if condition else (c - d)

# Nested ternary (use parentheses for clarity)
value = (
    value1 if condition1 else
    value2 if condition2 else
    value3
)

# In return statement
def func(x):
    return "Positive" if x > 0 else "Negative"

# In lambda
f = lambda x: "Even" if x % 2 == 0 else "Odd"

# In list comprehension
result = [x if x > 0 else 0 for x in numbers]

# In print
print("Yes" if condition else "No")

# Assignment with ternary
x = a if a > b else b

# Function call
result = func_true() if condition else func_false()
```

## Next Step

- Go to [04_match_case.md](04_match_case.md) for understanding about match case statements.

---

*Master the ternary operator for concise conditional expressions! 🐍✨*
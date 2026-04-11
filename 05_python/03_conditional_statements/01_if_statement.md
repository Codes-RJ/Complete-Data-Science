# 📘 IF STATEMENTS – COMPLETE GUIDE

## 📌 Table of Contents
1. [The `if` Statement](#the-if-statement)
2. [The `if-else` Statement](#the-if-else-statement)
3. [The `if-elif-else` Statement](#the-if-elif-else-statement)
4. [Multiple Conditions with `and`/`or`](#multiple-conditions-with-andor)
5. [Chained Comparisons](#chained-comparisons)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

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

### One-liner if (Not Recommended)

```python
# Allowed but not recommended for readability
if x > 5: print("x is greater than 5")

# Better to use multiple lines
if x > 5:
    print("x is greater than 5")
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
    warning = "You may need to gain weight"
elif bmi < 25:
    category = "Normal weight"
    warning = "Keep it up!"
elif bmi < 30:
    category = "Overweight"
    warning = "Consider exercising more"
else:
    category = "Obese"
    warning = "Please consult a doctor"

print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")
print(f"Advice: {warning}")

# Shipping cost calculator
total = 150

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

print(f"Total: ${total}")
print(f"Shipping: ${shipping}")
print(f"Method: {method}")
```

---

## Multiple Conditions with `and`/`or`

Combine multiple conditions using logical operators.

### Using `and` (Both must be True)

```python
age = 25
has_license = True
has_insurance = True

# All conditions must be True
if age >= 18 and has_license and has_insurance:
    print("Can drive legally")

# Multiple and conditions
score = 85
attendance = 90
if score >= 60 and attendance >= 75:
    print("Course passed")

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

### Using `or` (At least one must be True)

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")

# Multiple or conditions
user_type = "premium"
if user_type == "admin" or user_type == "moderator" or user_type == "premium":
    print("Special access granted")

# Short-circuit evaluation
result = check_true() or check_false()  # Only check_true() runs
# Output: Checking True
```

### Combining `and` and `or`

```python
age = 25
is_member = True
has_coupon = False

# Use parentheses for clarity
if (age >= 18 and is_member) or has_coupon:
    print("Discount applies")

# Without parentheses (different meaning)
if age >= 18 and (is_member or has_coupon):
    print("Discount applies")

# Complex example
if (age >= 18 and age <= 65) and (is_member or has_coupon) and not is_suspended:
    print("Eligible for promotion")
```

---

## Chained Comparisons

Python allows chaining comparison operators for cleaner code.

### Basic Chaining

```python
x = 5

# Traditional way
if x > 0 and x < 10:
    print("x between 0 and 10")

# Chained (Pythonic)
if 0 < x < 10:
    print("x between 0 and 10")

# Multiple comparisons
if 0 < x < 10 < 20 < 30:
    print("All true")

# With other operators
if 0 < x <= 10:
    print("x between 1 and 10 inclusive")
```

### Examples

```python
# Age check
age = 25
if 18 <= age <= 65:
    print("Working age")

# Temperature check
temp = 22
if 15 <= temp <= 25:
    print("Comfortable temperature")

# Value range
score = 85
if 0 <= score <= 100:
    print("Valid score")

# Multiple variables
a, b, c = 5, 10, 15
if a < b < c:
    print("Increasing order")

# Not equal in chain
if a != b != c:
    print("All different")  # Note: a and c could be equal!
```

---

## Real-World Examples

### Example 1: Ticket Pricing System

```python
def calculate_ticket_price(age, is_student, is_senior, day_of_week):
    """Calculate ticket price based on various factors"""
    base_price = 20.00
    
    # Age-based pricing
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
        discount = max(discount, 0.25)
    
    # Weekend pricing
    if day_of_week in ["Saturday", "Sunday"]:
        if discount > 0:
            discount = max(discount, 0.10)
        else:
            discount = 0.05
    
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
]

print("TICKET PRICING SYSTEM")
print("=" * 50)

for customer in customers:
    result = calculate_ticket_price(**customer)
    print(f"\nAge: {customer['age']}, Student: {customer['is_student']}, Day: {customer['day']}")
    print(f"  Type: {result['ticket_type']}")
    print(f"  Original: ${result['original_price']}")
    print(f"  Discount: {result['discount_percent']}%")
    print(f"  Final: ${result['final_price']}")
```

### Example 2: Login System

```python
class LoginSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "admin", "active": True},
            "alice": {"password": "alice123", "role": "user", "active": True},
            "bob": {"password": "bob123", "role": "user", "active": False},
        }
        self.max_attempts = 3
        self.failed_attempts = {}
    
    def authenticate(self, username, password):
        """Authenticate user"""
        # Check if username exists
        if username not in self.users:
            return False, "Username not found"
        
        user = self.users[username]
        
        # Check if account is locked
        if username in self.failed_attempts:
            attempts = self.failed_attempts[username]
            if attempts >= self.max_attempts:
                return False, "Account locked. Too many failed attempts."
        
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
            self.failed_attempts[username] = 1
        else:
            self.failed_attempts[username] += 1
        
        remaining = self.max_attempts - self.failed_attempts[username]
        return False, f"Invalid password. {remaining} attempts remaining"
    
    def check_permission(self, username, action):
        """Check if user has permission for action"""
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        role = user["role"]
        
        if role == "admin":
            return True, "Access granted (admin)"
        elif role == "moderator" and action in ["read", "delete"]:
            return True, "Access granted (moderator)"
        elif role == "user" and action == "read":
            return True, "Access granted (user)"
        else:
            return False, f"Access denied. {role} cannot {action}"

# Test the system
login = LoginSystem()

print("LOGIN SYSTEM")
print("=" * 40)

# Test authentication
test_users = [
    ("alice", "alice123"),
    ("alice", "wrong"),
    ("bob", "bob123"),
    ("admin", "admin123"),
]

for username, password in test_users:
    success, message = login.authenticate(username, password)
    status = "✓" if success else "✗"
    print(f"{status} {username}: {message}")

# Test permissions
print("\n" + "=" * 40)
print("PERMISSION CHECKING")
print("=" * 40)

tests = [
    ("alice", "read"),
    ("alice", "delete"),
    ("admin", "delete"),
]

for username, action in tests:
    success, message = login.check_permission(username, action)
    status = "✓" if success else "✗"
    print(f"{status} {username} - {action}: {message}")
```

### Example 3: Grade Calculator

```python
def calculate_grade(assignments, exams, participation, extra_credit=0):
    """
    Calculate final grade with weighted categories
    assignments: 40%, exams: 50%, participation: 10%
    """
    # Calculate averages
    if assignments:
        assignment_avg = sum(assignments) / len(assignments)
    else:
        assignment_avg = 0
    
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
        'remark': remark
    }

# Test cases
students = [
    {"name": "Alice", "assignments": [85, 90, 88, 92], "exams": [88, 91], "participation": 95, "extra": 2},
    {"name": "Bob", "assignments": [75, 80, 78, 82], "exams": [72, 78], "participation": 70, "extra": 0},
    {"name": "Charlie", "assignments": [95, 98, 92, 96], "exams": [94, 97], "participation": 100, "extra": 5},
    {"name": "Diana", "assignments": [65, 70, 68, 72], "exams": [55, 60], "participation": 80, "extra": 0},
]

print("GRADE CALCULATOR")
print("=" * 60)

for student in students:
    result = calculate_grade(
        student['assignments'],
        student['exams'],
        student['participation'],
        student['extra']
    )
    
    print(f"\n{student['name']}:")
    print(f"  Final Score: {result['score']}")
    print(f"  Letter Grade: {result['letter']} (GPA: {result['gpa']})")
    print(f"  Status: {result['status']}")
    print(f"  Remark: {result['remark']}")
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

### Pitfall 3: Forgetting Colon

```python
# ❌ Missing colon
if x > 5  # SyntaxError!
    print("x > 5")

# ✅ Correct
if x > 5:
    print("x > 5")
```

### Pitfall 4: Wrong Indentation

```python
# ❌ Wrong indentation
if x > 5:
print("x > 5")  # IndentationError!

# ✅ Correct
if x > 5:
    print("x > 5")
```

### Pitfall 5: Dangling Else (Which if does else belong to?)

```python
x = 5
y = 10

# else belongs to the nearest if
if x > 0:
    if y > 0:
        print("Both positive")
else:  # This belongs to the outer if!
    print("x is not positive")

# Use explicit blocks for clarity
if x > 0:
    if y > 0:
        print("Both positive")
    else:
        print("x positive, y not")
else:
    print("x is not positive")
```

---

## Practice Exercises

### Beginner Level

1. **Even or Odd**
   ```python
   # Write a program that checks if a number is even or odd
   # Example: 4 → "Even", 7 → "Odd"
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
   # Leap year: divisible by 4, not by 100 unless also by 400
   ```

5. **Maximum of Three Numbers**
   ```python
   # Find the largest of three numbers using if-elif-else
   ```

### Intermediate Level

6. **Grade Calculator**
   ```python
   # Convert numeric score (0-100) to letter grade (A-F)
   ```

7. **Ticket Price Calculator**
   ```python
   # Calculate ticket price based on age and student status
   ```

8. **Triangle Type**
   ```python
   # Determine if triangle is equilateral, isosceles, or scalene
   ```

9. **Shipping Cost Calculator**
   ```python
   # Calculate shipping cost based on weight and distance
   ```

10. **Discount Calculator**
    ```python
    # Apply different discounts based on total amount and membership
    ```

### Advanced Level

11. **Date Validator**
    ```python
    # Validate if a date (day, month, year) is valid
    # Consider leap years and days in each month
    ```

12. **Quadratic Equation Solver**
    ```python
    # Solve quadratic equation ax² + bx + c = 0
    # Determine real, repeated, or complex roots
    ```

13. **Bank Account Classifier**
    ```python
    # Classify bank account based on balance and transaction history
    # Different interest rates for different balance ranges
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

# Comparison operators
==, !=, >, <, >=, <=

# Logical operators
and, or, not

# Chained comparisons
if 0 < x < 10:
    # code

# Common patterns
if value:           # Check if truthy
if not value:       # Check if falsy
if value is None:   # Check for None
```

## Next Step

- Go to [02_nested_conditionals.md](02_nested_conditionals.md) for understanding about nested conditional statements.

---

*Master if statements to control the flow of your programs! 🐍✨*

---
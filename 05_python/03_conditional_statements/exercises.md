# 📝 CONDITIONAL STATEMENTS – PRACTICE EXERCISES

## 📌 Table of Contents
1. [Beginner Exercises](#beginner-exercises)
2. [Intermediate Exercises](#intermediate-exercises)
3. [Advanced Exercises](#advanced-exercises)
4. [Solutions](#solutions)

---

## Beginner Exercises

### Exercise 1: Even or Odd
Write a program that checks if a number is even or odd.

```python
def check_even_odd(num):
    # Your code here
    pass

# Test cases
print(check_even_odd(4))   # Should print: Even
print(check_even_odd(7))   # Should print: Odd
print(check_even_odd(0))   # Should print: Even
```

### Exercise 2: Positive, Negative, or Zero
Classify a number as positive, negative, or zero.

```python
def classify_number(num):
    # Your code here
    pass

# Test cases
print(classify_number(5))    # Positive
print(classify_number(-3))   # Negative
print(classify_number(0))    # Zero
```

### Exercise 3: Maximum of Two Numbers
Find the maximum of two numbers without using `max()`.

```python
def max_of_two(a, b):
    # Your code here
    pass

# Test cases
print(max_of_two(10, 20))   # 20
print(max_of_two(25, 15))   # 25
print(max_of_two(5, 5))     # 5
```

### Exercise 4: Vowel or Consonant
Check if a character is a vowel or consonant.

```python
def is_vowel(char):
    # Your code here
    pass

# Test cases
print(is_vowel('a'))   # True
print(is_vowel('b'))   # False
print(is_vowel('E'))   # True (should handle uppercase)
```

### Exercise 5: Leap Year Checker
Determine if a year is a leap year.
- Divisible by 4
- Not divisible by 100, unless also divisible by 400

```python
def is_leap_year(year):
    # Your code here
    pass

# Test cases
print(is_leap_year(2020))   # True
print(is_leap_year(2021))   # False
print(is_leap_year(1900))   # False
print(is_leap_year(2000))   # True
```

---

## Intermediate Exercises

### Exercise 6: Grade Calculator
Convert numeric score to letter grade.

| Score | Grade |
|-------|-------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |

```python
def get_grade(score):
    # Your code here
    pass

# Test cases
print(get_grade(95))   # A
print(get_grade(85))   # B
print(get_grade(75))   # C
print(get_grade(65))   # D
print(get_grade(55))   # F
print(get_grade(105))  # Invalid score
```

### Exercise 7: Ticket Price Calculator
Calculate ticket price based on age and student status.

| Category | Price |
|----------|-------|
| Child (under 12) | $5 |
| Student (with ID) | $8 |
| Adult (12-64) | $12 |
| Senior (65+) | $6 |

```python
def calculate_ticket_price(age, is_student=False):
    # Your code here
    pass

# Test cases
print(calculate_ticket_price(8))           # $5
print(calculate_ticket_price(20, True))    # $8
print(calculate_ticket_price(30))          # $12
print(calculate_ticket_price(70))          # $6
```

### Exercise 8: Triangle Type
Determine if triangle is equilateral, isosceles, or scalene.

```python
def triangle_type(a, b, c):
    # Your code here
    pass

# Test cases
print(triangle_type(5, 5, 5))     # Equilateral
print(triangle_type(5, 5, 3))     # Isosceles
print(triangle_type(3, 4, 5))     # Scalene
print(triangle_type(1, 1, 3))     # Not a triangle
```

### Exercise 9: Shipping Cost Calculator
Calculate shipping cost based on weight and distance.

| Weight (kg) | Local | National | International |
|-------------|-------|----------|---------------|
| < 1 | $2 | $5 | $10 |
| 1-5 | $5 | $10 | $20 |
| > 5 | $10 | $20 | $35 |

```python
def calculate_shipping(weight, destination):
    # destination: "local", "national", "international"
    # Your code here
    pass

# Test cases
print(calculate_shipping(0.5, "local"))        # $2
print(calculate_shipping(3, "national"))       # $10
print(calculate_shipping(10, "international")) # $35
```

### Exercise 10: Discount Calculator
Apply discounts based on total amount and membership.

| Condition | Discount |
|-----------|----------|
| Member and total > $100 | 20% |
| Member only | 10% |
| Non-member and total > $100 | 5% |
| Non-member | 0% |

```python
def calculate_discount(total, is_member):
    # Your code here
    pass

# Test cases
print(calculate_discount(150, True))   # 20% off -> $120
print(calculate_discount(50, True))    # 10% off -> $45
print(calculate_discount(150, False))  # 5% off -> $142.5
print(calculate_discount(50, False))   # 0% off -> $50
```

---

## Advanced Exercises

### Exercise 11: Date Validator
Validate if a date (day, month, year) is valid.
- Consider days in each month
- Consider leap years for February

```python
def is_valid_date(day, month, year):
    # Your code here
    pass

# Test cases
print(is_valid_date(31, 1, 2024))   # True (January has 31 days)
print(is_valid_date(31, 4, 2024))   # False (April has 30 days)
print(is_valid_date(29, 2, 2024))   # True (leap year)
print(is_valid_date(29, 2, 2023))   # False (not leap year)
print(is_valid_date(15, 13, 2024))  # False (invalid month)
```

### Exercise 12: Quadratic Equation Solver
Solve quadratic equation ax² + bx + c = 0.
- Calculate discriminant: D = b² - 4ac
- If D > 0: two real roots
- If D = 0: one real root
- If D < 0: complex roots

```python
def solve_quadratic(a, b, c):
    # Your code here
    pass

# Test cases
print(solve_quadratic(1, -5, 6))    # Two real roots: 2.0 and 3.0
print(solve_quadratic(1, 2, 1))     # One real root: -1.0
print(solve_quadratic(1, 0, 1))     # Complex roots
print(solve_quadratic(0, 2, 4))     # Linear equation: -2.0
```

### Exercise 13: Rock Paper Scissors
Determine winner between two players.

```python
def rock_paper_scissors(player1, player2):
    # Options: "rock", "paper", "scissors"
    # Rules: rock beats scissors, scissors beats paper, paper beats rock
    # Your code here
    pass

# Test cases
print(rock_paper_scissors("rock", "scissors"))     # Player 1 wins
print(rock_paper_scissors("paper", "rock"))        # Player 1 wins
print(rock_paper_scissors("scissors", "paper"))    # Player 1 wins
print(rock_paper_scissors("rock", "paper"))        # Player 2 wins
print(rock_paper_scissors("rock", "rock"))         # Tie
```

### Exercise 14: Bank Account Classifier
Classify bank account based on balance.

| Balance | Type | Interest Rate |
|---------|------|---------------|
| < 0 | Overdrawn | 0% |
| 0 - 1000 | Basic | 1% |
| 1001 - 10000 | Standard | 2% |
| 10001 - 50000 | Premium | 3% |
| > 50000 | Platinum | 5% |

```python
def classify_account(balance):
    # Your code here
    pass

# Test cases
print(classify_account(-100))    # Overdrawn, 0%
print(classify_account(500))      # Basic, 1%
print(classify_account(5000))     # Standard, 2%
print(classify_account(25000))    # Premium, 3%
print(classify_account(100000))   # Platinum, 5%
```

### Exercise 15: Password Strength Checker
Check password strength based on criteria:
- Length >= 8 (1 point)
- Contains uppercase (1 point)
- Contains lowercase (1 point)
- Contains digit (1 point)
- Contains special character (1 point)

```python
def check_password_strength(password):
    # Your code here
    # Return: "Very Weak", "Weak", "Medium", "Strong", "Very Strong"
    pass

# Test cases
print(check_password_strength("weak"))           # Very Weak
print(check_password_strength("WeakPass"))       # Weak
print(check_password_strength("WeakPass1"))      # Medium
print(check_password_strength("Str0ngP@ss"))     # Strong
print(check_password_strength("V3ry$tr0ngP@ss")) # Very Strong
```

---

## Solutions

### Solution 1: Even or Odd

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# One-liner using ternary
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
```

### Solution 2: Positive, Negative, or Zero

```python
def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Using ternary (nested)
def classify_number(num):
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
```

### Solution 3: Maximum of Two Numbers

```python
def max_of_two(a, b):
    if a >= b:
        return a
    else:
        return b

# Using ternary
def max_of_two(a, b):
    return a if a >= b else b
```

### Solution 4: Vowel or Consonant

```python
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

# Alternative
def is_vowel(char):
    return char.lower() in 'aeiou'
```

### Solution 5: Leap Year Checker

```python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# One-liner
def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
```

### Solution 6: Grade Calculator

```python
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

### Solution 7: Ticket Price Calculator

```python
def calculate_ticket_price(age, is_student=False):
    if age < 12:
        return 5
    elif age >= 65:
        return 6
    elif is_student:
        return 8
    else:
        return 12
```

### Solution 8: Triangle Type

```python
def triangle_type(a, b, c):
    # Check if triangle is valid
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
```

### Solution 9: Shipping Cost Calculator

```python
def calculate_shipping(weight, destination):
    # Determine base cost by weight
    if weight < 1:
        base_cost = 2
    elif weight <= 5:
        base_cost = 5
    else:
        base_cost = 10
    
    # Apply destination multiplier
    if destination == "local":
        return base_cost
    elif destination == "national":
        return base_cost + 3
    elif destination == "international":
        if weight < 1:
            return 10
        elif weight <= 5:
            return 20
        else:
            return 35
    else:
        return "Invalid destination"
```

### Solution 10: Discount Calculator

```python
def calculate_discount(total, is_member):
    if is_member:
        if total > 100:
            discount = 0.20
        else:
            discount = 0.10
    else:
        if total > 100:
            discount = 0.05
        else:
            discount = 0
    
    final_price = total * (1 - discount)
    return round(final_price, 2)
```

### Solution 11: Date Validator

```python
def is_valid_date(day, month, year):
    # Validate month
    if month < 1 or month > 12:
        return False
    
    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year
    def is_leap(y):
        return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    
    # Adjust February for leap year
    if month == 2 and is_leap(year):
        days_in_month[1] = 29
    
    # Validate day
    return 1 <= day <= days_in_month[month - 1]
```

### Solution 12: Quadratic Equation Solver

```python
import math

def solve_quadratic(a, b, c):
    # Linear equation
    if a == 0:
        if b == 0:
            return "No solution"
        else:
            return f"Linear equation: x = {-c / b}"
    
    # Quadratic equation
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1:.2f} and {root2:.2f}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root:.2f}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return f"Complex roots: {real:.2f} ± {imag:.2f}i"
```

### Solution 13: Rock Paper Scissors

```python
def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "Tie"
    
    # Winning combinations
    wins = {
        ("rock", "scissors"): "Player 1 wins",
        ("scissors", "paper"): "Player 1 wins",
        ("paper", "rock"): "Player 1 wins"
    }
    
    if (player1, player2) in wins:
        return wins[(player1, player2)]
    else:
        return "Player 2 wins"
```

### Solution 14: Bank Account Classifier

```python
def classify_account(balance):
    if balance < 0:
        return "Overdrawn", "0%"
    elif balance <= 1000:
        return "Basic", "1%"
    elif balance <= 10000:
        return "Standard", "2%"
    elif balance <= 50000:
        return "Premium", "3%"
    else:
        return "Platinum", "5%"
```

### Solution 15: Password Strength Checker

```python
def check_password_strength(password):
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    
    # Uppercase check
    if any(c.isupper() for c in password):
        score += 1
    
    # Lowercase check
    if any(c.islower() for c in password):
        score += 1
    
    # Digit check
    if any(c.isdigit() for c in password):
        score += 1
    
    # Special character check
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
    
    # Determine strength
    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"
```

---

## Evaluation Criteria

| Score | Rating |
|-------|--------|
| 15/15 | Excellent |
| 12-14/15 | Good |
| 9-11/15 | Satisfactory |
| 6-8/15 | Needs Improvement |
| Below 6 | Review the material |

## Next Step

- Move to [solutions.md](solutions.md) for seeing results.

---

*Practice makes perfect! Complete all exercises to master conditional statements! 🐍✨*
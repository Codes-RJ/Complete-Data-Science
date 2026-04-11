# 💡 CONDITIONAL STATEMENTS – SOLUTIONS

## 📌 Table of Contents
1. [Beginner Solutions](#beginner-solutions)
2. [Intermediate Solutions](#intermediate-solutions)
3. [Advanced Solutions](#advanced-solutions)

---

## Beginner Solutions

### Solution 1: Even or Odd

```python
def check_even_odd(num):
    """Check if a number is even or odd."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# One-liner using ternary operator
def check_even_odd_ternary(num):
    return "Even" if num % 2 == 0 else "Odd"

# Test cases
print(check_even_odd(4))   # Even
print(check_even_odd(7))   # Odd
print(check_even_odd(0))   # Even
```

### Solution 2: Positive, Negative, or Zero

```python
def classify_number(num):
    """Classify number as positive, negative, or zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Using nested ternary (less readable but shorter)
def classify_number_ternary(num):
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

# Test cases
print(classify_number(5))    # Positive
print(classify_number(-3))   # Negative
print(classify_number(0))    # Zero
```

### Solution 3: Maximum of Two Numbers

```python
def max_of_two(a, b):
    """Find the maximum of two numbers."""
    if a >= b:
        return a
    else:
        return b

# Using ternary operator
def max_of_two_ternary(a, b):
    return a if a >= b else b

# Test cases
print(max_of_two(10, 20))   # 20
print(max_of_two(25, 15))   # 25
print(max_of_two(5, 5))     # 5
```

### Solution 4: Vowel or Consonant

```python
def is_vowel(char):
    """Check if a character is a vowel."""
    vowels = 'aeiouAEIOU'
    return char in vowels

# Alternative: convert to lowercase first
def is_vowel_v2(char):
    return char.lower() in 'aeiou'

# Test cases
print(is_vowel('a'))   # True
print(is_vowel('b'))   # False
print(is_vowel('E'))   # True
```

### Solution 5: Leap Year Checker

```python
def is_leap_year(year):
    """Determine if a year is a leap year."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# One-liner using logical operators
def is_leap_year_short(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Test cases
print(is_leap_year(2020))   # True
print(is_leap_year(2021))   # False
print(is_leap_year(1900))   # False
print(is_leap_year(2000))   # True
```

---

## Intermediate Solutions

### Solution 6: Grade Calculator

```python
def get_grade(score):
    """Convert numeric score to letter grade."""
    # Validate input
    if score < 0 or score > 100:
        return "Invalid score"
    
    # Determine grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Alternative using if-elif-else with range checking
def get_grade_v2(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid score"

# Test cases
print(get_grade(95))   # A
print(get_grade(85))   # B
print(get_grade(75))   # C
print(get_grade(65))   # D
print(get_grade(55))   # F
print(get_grade(105))  # Invalid score
```

### Solution 7: Ticket Price Calculator

```python
def calculate_ticket_price(age, is_student=False):
    """Calculate ticket price based on age and student status."""
    if age < 12:
        return 5
    elif age >= 65:
        return 6
    elif is_student:
        return 8
    else:
        return 12

# Alternative with nested conditions
def calculate_ticket_price_v2(age, is_student=False):
    if age < 12:
        price = 5
    elif age >= 65:
        price = 6
    else:
        if is_student:
            price = 8
        else:
            price = 12
    return price

# Test cases
print(calculate_ticket_price(8))           # 5
print(calculate_ticket_price(20, True))    # 8
print(calculate_ticket_price(30))          # 12
print(calculate_ticket_price(70))          # 6
```

### Solution 8: Triangle Type

```python
def triangle_type(a, b, c):
    """Determine triangle type or if it's a valid triangle."""
    # Check if triangle is valid
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    
    # Check for negative or zero sides
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"
    
    # Determine triangle type
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Alternative with sorted sides
def triangle_type_v2(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "Not a triangle"
    if sides[0] == sides[1] == sides[2]:
        return "Equilateral"
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return "Isosceles"
    return "Scalene"

# Test cases
print(triangle_type(5, 5, 5))     # Equilateral
print(triangle_type(5, 5, 3))     # Isosceles
print(triangle_type(3, 4, 5))     # Scalene
print(triangle_type(1, 1, 3))     # Not a triangle
```

### Solution 9: Shipping Cost Calculator

```python
def calculate_shipping(weight, destination):
    """Calculate shipping cost based on weight and destination."""
    # Validate destination
    valid_destinations = ["local", "national", "international"]
    if destination not in valid_destinations:
        return "Invalid destination"
    
    # Validate weight
    if weight <= 0:
        return "Invalid weight"
    
    # Calculate base cost by weight
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
    else:  # international
        if weight < 1:
            return 10
        elif weight <= 5:
            return 20
        else:
            return 35

# Alternative using dictionary
def calculate_shipping_v2(weight, destination):
    rates = {
        "local": {0: 2, 1: 5, 2: 10},
        "national": {0: 5, 1: 10, 2: 20},
        "international": {0: 10, 1: 20, 2: 35}
    }
    
    # Determine weight tier
    if weight < 1:
        tier = 0
    elif weight <= 5:
        tier = 1
    else:
        tier = 2
    
    return rates.get(destination, {}).get(tier, "Invalid")

# Test cases
print(calculate_shipping(0.5, "local"))        # 2
print(calculate_shipping(3, "national"))       # 10
print(calculate_shipping(10, "international")) # 35
```

### Solution 10: Discount Calculator

```python
def calculate_discount(total, is_member):
    """Calculate final price after discount."""
    # Calculate discount percentage
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
    
    # Calculate final price
    final_price = total * (1 - discount)
    
    # Return rounded to 2 decimal places
    return round(final_price, 2)

# Alternative using nested ternary
def calculate_discount_ternary(total, is_member):
    discount = 0.20 if is_member and total > 100 else 0.10 if is_member else 0.05 if total > 100 else 0
    return round(total * (1 - discount), 2)

# Test cases
print(calculate_discount(150, True))   # 120.0
print(calculate_discount(50, True))    # 45.0
print(calculate_discount(150, False))  # 142.5
print(calculate_discount(50, False))   # 50.0
```

---

## Advanced Solutions

### Solution 11: Date Validator

```python
def is_valid_date(day, month, year):
    """Validate if a date is valid."""
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
    if day < 1 or day > days_in_month[month - 1]:
        return False
    
    # Validate year (optional, can be any reasonable range)
    if year < 1 or year > 9999:
        return False
    
    return True

# Alternative using calendar module
import calendar

def is_valid_date_v2(day, month, year):
    try:
        calendar.datetime.date(year, month, day)
        return True
    except ValueError:
        return False

# Test cases
print(is_valid_date(31, 1, 2024))   # True
print(is_valid_date(31, 4, 2024))   # False
print(is_valid_date(29, 2, 2024))   # True
print(is_valid_date(29, 2, 2023))   # False
print(is_valid_date(15, 13, 2024))  # False
```

### Solution 12: Quadratic Equation Solver

```python
import math

def solve_quadratic(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0."""
    # Handle linear equation (a = 0)
    if a == 0:
        if b == 0:
            return "No solution"
        else:
            x = -c / b
            return f"Linear equation: x = {x:.2f}"
    
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate roots based on discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        # Order roots for consistent output
        root1, root2 = sorted([root1, root2])
        return f"Two real roots: {root1:.2f} and {root2:.2f}"
    
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root:.2f}"
    
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return f"Complex roots: {real:.2f} ± {imag:.2f}i"

# Test cases
print(solve_quadratic(1, -5, 6))    # Two real roots: 2.00 and 3.00
print(solve_quadratic(1, 2, 1))     # One real root: -1.00
print(solve_quadratic(1, 0, 1))     # Complex roots: 0.00 ± 1.00i
print(solve_quadratic(0, 2, 4))     # Linear equation: x = -2.00
```

### Solution 13: Rock Paper Scissors

```python
def rock_paper_scissors(player1, player2):
    """Determine winner of Rock Paper Scissors."""
    # Normalize input
    player1 = player1.lower()
    player2 = player2.lower()
    
    # Validate input
    valid_choices = ["rock", "paper", "scissors"]
    if player1 not in valid_choices or player2 not in valid_choices:
        return "Invalid choice"
    
    # Check for tie
    if player1 == player2:
        return "Tie"
    
    # Define winning combinations
    if (player1 == "rock" and player2 == "scissors"):
        return "Player 1 wins"
    elif (player1 == "scissors" and player2 == "paper"):
        return "Player 1 wins"
    elif (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

# Alternative using dictionary
def rock_paper_scissors_v2(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()
    
    wins = {
        ("rock", "scissors"): "Player 1 wins",
        ("scissors", "paper"): "Player 1 wins",
        ("paper", "rock"): "Player 1 wins",
    }
    
    if player1 == player2:
        return "Tie"
    return wins.get((player1, player2), "Player 2 wins")

# Test cases
print(rock_paper_scissors("rock", "scissors"))     # Player 1 wins
print(rock_paper_scissors("paper", "rock"))        # Player 1 wins
print(rock_paper_scissors("scissors", "paper"))    # Player 1 wins
print(rock_paper_scissors("rock", "paper"))        # Player 2 wins
print(rock_paper_scissors("rock", "rock"))         # Tie
```

### Solution 14: Bank Account Classifier

```python
def classify_account(balance):
    """Classify bank account based on balance."""
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

# Alternative with interest rate calculation
def classify_account_with_interest(balance):
    if balance < 0:
        account_type = "Overdrawn"
        rate = 0
    elif balance <= 1000:
        account_type = "Basic"
        rate = 0.01
    elif balance <= 10000:
        account_type = "Standard"
        rate = 0.02
    elif balance <= 50000:
        account_type = "Premium"
        rate = 0.03
    else:
        account_type = "Platinum"
        rate = 0.05
    
    interest = balance * rate
    return account_type, f"{rate * 100:.0f}%", f"${interest:.2f}"

# Test cases
print(classify_account(-100))    # Overdrawn, 0%
print(classify_account(500))     # Basic, 1%
print(classify_account(5000))    # Standard, 2%
print(classify_account(25000))   # Premium, 3%
print(classify_account(100000))  # Platinum, 5%

# Test with interest calculation
print(classify_account_with_interest(5000))
# ('Standard', '2%', '$100.00')
```

### Solution 15: Password Strength Checker

```python
def check_password_strength(password):
    """Check password strength based on multiple criteria."""
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
    special_count = sum(1 for c in password if c in special_chars)
    if special_count >= 2:
        score += 2
        feedback.append("✓ Has multiple special characters")
    elif special_count == 1:
        score += 1
        feedback.append("✓ Has a special character")
    else:
        feedback.append("✗ Missing special characters")
    
    # Determine strength
    if score <= 2:
        strength = "Very Weak"
        color = "🔴"
    elif score <= 4:
        strength = "Weak"
        color = "🟡"
    elif score <= 6:
        strength = "Medium"
        color = "🟠"
    elif score <= 8:
        strength = "Strong"
        color = "🟢"
    else:
        strength = "Very Strong"
        color = "💪"
    
    return {
        'strength': strength,
        'score': score,
        'max_score': 9,
        'color': color,
        'feedback': feedback
    }

# Simplified version for basic exercise
def check_password_strength_simple(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
    
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

# Test cases
print(check_password_strength_simple("weak"))           # Very Weak
print(check_password_strength_simple("WeakPass"))       # Weak
print(check_password_strength_simple("WeakPass1"))      # Medium
print(check_password_strength_simple("Str0ngP@ss"))     # Strong
print(check_password_strength_simple("V3ry$tr0ngP@ss")) # Very Strong

# Detailed test
print("\n" + "=" * 50)
print("PASSWORD STRENGTH DETAILED REPORT")
print("=" * 50)

test_passwords = [
    "weak",
    "WeakPass",
    "WeakPass1",
    "Str0ngP@ss",
    "V3ry$tr0ngP@ssw0rd!"
]

for pwd in test_passwords:
    result = check_password_strength(pwd)
    print(f"\nPassword: {pwd}")
    print(f"Strength: {result['color']} {result['strength']} (Score: {result['score']}/{result['max_score']})")
    print("Feedback:")
    for fb in result['feedback']:
        print(f"  {fb}")
```

---

## Scoring Guide

| Score Range | Rating | Recommendation |
|-------------|--------|----------------|
| 15/15 | Excellent | Ready for next topic |
| 12-14/15 | Good | Review missed concepts |
| 9-11/15 | Satisfactory | Practice more |
| 6-8/15 | Needs Improvement | Re-study material |
| Below 6 | Review | Start from basics |

## Next Step

- Move to [Loops](/05_python/04_loop_statements/README.md) for understanding about them in-depth and to understand the need of repititiveness of statements.

---

*Solutions verified and tested. Keep practicing! 🐍✨*
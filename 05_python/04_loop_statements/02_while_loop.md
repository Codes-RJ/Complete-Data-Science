# 📘 WHILE LOOP – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is a While Loop?](#what-is-a-while-loop)
2. [While Loop Syntax](#while-loop-syntax)
3. [Basic Examples](#basic-examples)
4. [Infinite Loops](#infinite-loops)
5. [While with else](#while-with-else)
6. [User Input Validation](#user-input-validation)
7. [Sentinel Values](#sentinel-values)
8. [While vs For Loop](#while-vs-for-loop)
9. [Real-World Examples](#real-world-examples)
10. [Common Pitfalls](#common-pitfalls)
11. [Practice Exercises](#practice-exercises)

---

## What is a While Loop?

A **while loop** repeatedly executes a block of code as long as a given condition is `True`. It's ideal when you don't know how many iterations you need in advance.

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

**Key Characteristics:**
- ✅ Condition checked before each iteration
- ✅ Continues until condition becomes `False`
- ✅ Great for unknown iteration counts
- ✅ Can become infinite if condition never becomes `False`
- ✅ Requires manual update of loop variables

---

## While Loop Syntax

### Basic Syntax

```python
while condition:
    # Code block to execute while condition is True
    statement1
    statement2
    # Update condition (important!)
```

### Examples

```python
# Simple counter
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Sum of numbers
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of 1 to 10: {total}")  # 55

# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Print even numbers
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print()
```

---

## Basic Examples

### Number Operations

```python
# Factorial
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")  # 120

# Reverse a number
num = 12345
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"Reversed: {reversed_num}")  # 54321

# Sum of digits
num = 12345
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(f"Sum of digits: {digit_sum}")  # 15

# Count digits
num = 12345
count = 0
while num > 0:
    count += 1
    num //= 10
print(f"Number of digits: {count}")  # 5
```

### Pattern Printing

```python
# Right triangle
n = 5
i = 1
while i <= n:
    print('*' * i)
    i += 1

# Reverse triangle
i = n
while i > 0:
    print('*' * i)
    i -= 1

# Number pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
```

---

## Infinite Loops

Infinite loops run forever unless broken with `break`.

### Creating Infinite Loops

```python
# while True (most common)
while True:
    print("This runs forever")
    # Must have break somewhere

# while 1 (also works)
while 1:
    print("Also infinite")

# while condition that never becomes False
x = 5
while x > 0:
    print(x)
    # Missing x -= 1 -> infinite loop
```

### Breaking Out of Infinite Loops

```python
# Using break
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Using user input
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    print(f"You entered: {user_input}")

# Game loop
score = 0
playing = True
while playing:
    # Game logic
    score += 1
    if score >= 10:
        playing = False
print(f"Final score: {score}")
```

---

## While with else

The `else` block executes when the loop condition becomes `False` (not when broken with `break`).

### Basic else

```python
# Loop completes normally
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed without break")

# Loop with break
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("This won't print")
```

### Practical else Examples

```python
# Search for item
def find_item(items, target):
    i = 0
    while i < len(items):
        if items[i] == target:
            print(f"Found {target} at index {i}")
            break
        i += 1
    else:
        print(f"{target} not found")

find_item([1, 2, 3, 4, 5], 3)  # Found 3
find_item([1, 2, 3, 4, 5], 7)  # 7 not found

# Check if all numbers are positive
numbers = [5, -2, 8, 3, 1]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        print(f"Found negative: {numbers[i]}")
        break
    i += 1
else:
    print("All numbers are positive")

# Password attempt limit
max_attempts = 3
attempts = 0
password = "secret"

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    attempts += 1
    print(f"Wrong password. {max_attempts - attempts} attempts left")
else:
    print("Access denied. Account locked.")
```

---

## User Input Validation

While loops are perfect for validating user input.

### Basic Input Validation

```python
# Validate number range
while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            break
        print("Age must be between 1 and 120")
    except ValueError:
        print("Please enter a valid number")

print(f"Age: {age}")

# Validate yes/no response
while True:
    response = input("Continue? (y/n): ").lower()
    if response in ['y', 'yes', 'n', 'no']:
        break
    print("Please enter y or n")

if response in ['y', 'yes']:
    print("Continuing...")
else:
    print("Exiting...")
```

### Advanced Validation

```python
def get_valid_email():
    """Get and validate email address"""
    while True:
        email = input("Enter email address: ")
        
        # Basic validation
        if '@' not in email:
            print("Email must contain @")
            continue
        if '.' not in email.split('@')[-1]:
            print("Email must contain domain (e.g., .com)")
            continue
        if len(email) < 5:
            print("Email too short")
            continue
        
        return email

def get_valid_phone():
    """Get and validate phone number"""
    while True:
        phone = input("Enter phone number (10 digits): ")
        
        # Remove non-digits
        digits = ''.join(filter(str.isdigit, phone))
        
        if len(digits) != 10:
            print("Phone number must have exactly 10 digits")
            continue
        
        return digits

def get_valid_choice(options):
    """Get valid choice from options"""
    while True:
        print(f"\nOptions: {', '.join(options)}")
        choice = input("Enter your choice: ").lower()
        
        if choice in options:
            return choice
        print(f"Invalid choice. Please choose from: {', '.join(options)}")

# Usage
email = get_valid_email()
phone = get_valid_phone()
print(f"Email: {email}, Phone: {phone}")

choice = get_valid_choice(['yes', 'no', 'maybe'])
print(f"You chose: {choice}")
```

---

## Sentinel Values

A sentinel is a special value that signals the end of input.

### Basic Sentinel Pattern

```python
# Sum numbers until user enters 0
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Sum: {total}")

# Collect names until 'quit'
names = []
while True:
    name = input("Enter a name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    if name:
        names.append(name)
print(f"Names: {names}")
```

### Advanced Sentinel Examples

```python
# Grade collector
grades = []
while True:
    grade = input("Enter grade (or 'done' to finish): ")
    if grade.lower() == 'done':
        break
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Grade must be between 0 and 100")
    except ValueError:
        print("Please enter a number or 'done'")

if grades:
    average = sum(grades) / len(grades)
    print(f"Average grade: {average:.2f}")
    print(f"Highest: {max(grades)}")
    print(f"Lowest: {min(grades)}")
else:
    print("No grades entered")

# Shopping cart
cart = []
while True:
    item = input("Enter item (or 'checkout' to finish): ")
    if item.lower() == 'checkout':
        break
    
    try:
        price = float(input(f"Enter price for {item}: $"))
        cart.append({"item": item, "price": price})
    except ValueError:
        print("Invalid price")

total = sum(item["price"] for item in cart)
print(f"\nShopping Cart Total: ${total:.2f}")
for item in cart:
    print(f"  {item['item']}: ${item['price']:.2f}")
```

---

## While vs For Loop

### Comparison Table

| Aspect | For Loop | While Loop |
|--------|----------|------------|
| **Use case** | Known number of iterations | Unknown number of iterations |
| **Syntax** | `for item in iterable:` | `while condition:` |
| **Initialization** | Automatic | Manual |
| **Update** | Automatic | Manual |
| **Risk** | Low | Infinite loop risk |
| **Best for** | Sequences, ranges | User input, game loops |

### When to Use While

```python
# ✅ Good for while - unknown iterations
def guess_number():
    secret = 42
    guess = None
    while guess != secret:
        guess = int(input("Guess the number: "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
    print("Correct!")

# ✅ Good for while - waiting for condition
import random
rolls = 0
while rolls < 3:
    dice = random.randint(1, 6)
    print(f"Rolled: {dice}")
    if dice == 6:
        rolls += 1
    else:
        rolls = 0
print("Got three 6's in a row!")

# ✅ Good for while - processing until done
def process_queue():
    queue = ["task1", "task2", "task3"]
    while queue:
        task = queue.pop(0)
        print(f"Processing: {task}")
```

### When to Use For

```python
# ✅ Good for for - known sequence
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# ✅ Good for for - range with known count
for i in range(10):
    print(i)

# ✅ Good for for - iterating through collection
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ❌ Bad - using while for sequence (verbose, error-prone)
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## Real-World Examples

### Example 1: Number Guessing Game

```python
import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100, max_attempts=7):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = None
        self.attempts = 0
    
    def start(self):
        """Start a new game"""
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        print(f"\n🎲 NUMBER GUESSING GAME")
        print(f"Guess a number between {self.min_num} and {self.max_num}")
        print(f"You have {self.max_attempts} attempts")
        
        while self.attempts < self.max_attempts:
            try:
                guess = int(input(f"\nAttempt {self.attempts + 1}: "))
                self.attempts += 1
                
                if guess < self.min_num or guess > self.max_num:
                    print(f"Please guess between {self.min_num} and {self.max_num}")
                    continue
                
                if guess == self.secret_number:
                    print(f"🎉 CORRECT! You guessed it in {self.attempts} attempts!")
                    return True
                elif guess < self.secret_number:
                    print("Too low!")
                else:
                    print("Too high!")
                
                remaining = self.max_attempts - self.attempts
                if remaining > 0:
                    print(f"Attempts remaining: {remaining}")
                
            except ValueError:
                print("Please enter a valid number")
        
        print(f"\n💀 GAME OVER! The number was {self.secret_number}")
        return False
    
    def play_again(self):
        """Ask to play again"""
        while True:
            response = input("\nPlay again? (y/n): ").lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            print("Please enter y or n")

# Usage
game = NumberGuessingGame(1, 50, 5)
while True:
    game.start()
    if not game.play_again():
        print("Thanks for playing!")
        break
```

### Example 2: ATM Simulator

```python
class ATM:
    def __init__(self, pin="1234", balance=1000):
        self.pin = pin
        self.balance = balance
        self.max_attempts = 3
        self.is_authenticated = False
    
    def authenticate(self):
        """Authenticate user with PIN"""
        attempts = 0
        while attempts < self.max_attempts and not self.is_authenticated:
            pin_input = input("Enter your PIN: ")
            if pin_input == self.pin:
                self.is_authenticated = True
                print("Authentication successful!")
                return True
            else:
                attempts += 1
                remaining = self.max_attempts - attempts
                if remaining > 0:
                    print(f"Wrong PIN. {remaining} attempts remaining")
                else:
                    print("Too many failed attempts. Card blocked.")
        return False
    
    def check_balance(self):
        """Display current balance"""
        print(f"\nCurrent balance: ${self.balance:.2f}")
    
    def deposit(self):
        """Deposit money"""
        while True:
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be positive")
                    continue
                self.balance += amount
                print(f"Deposited ${amount:.2f}")
                print(f"New balance: ${self.balance:.2f}")
                return True
            except ValueError:
                print("Please enter a valid amount")
    
    def withdraw(self):
        """Withdraw money"""
        while True:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be positive")
                    continue
                if amount > self.balance:
                    print(f"Insufficient funds. Balance: ${self.balance:.2f}")
                    continue
                if amount > 500:
                    print("Daily withdrawal limit is $500")
                    continue
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}")
                print(f"New balance: ${self.balance:.2f}")
                return True
            except ValueError:
                print("Please enter a valid amount")
    
    def run(self):
        """Run ATM main loop"""
        if not self.authenticate():
            return
        
        while True:
            print("\n" + "=" * 40)
            print("ATM MENU")
            print("=" * 40)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("=" * 40)
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Usage
atm = ATM(pin="1234", balance=1000)
atm.run()
```

### Example 3: Menu-Driven Program

```python
class MenuSystem:
    def __init__(self):
        self.data = []
    
    def display_menu(self):
        print("\n" + "=" * 40)
        print("MAIN MENU")
        print("=" * 40)
        print("1. Add item")
        print("2. View all items")
        print("3. Search item")
        print("4. Delete item")
        print("5. Clear all")
        print("6. Exit")
        print("=" * 40)
    
    def add_item(self):
        item = input("Enter item to add: ").strip()
        if item:
            self.data.append(item)
            print(f"Added: {item}")
        else:
            print("Item cannot be empty")
    
    def view_items(self):
        if not self.data:
            print("No items found")
            return
        
        print("\nCurrent items:")
        for i, item in enumerate(self.data, 1):
            print(f"  {i}. {item}")
        print(f"Total: {len(self.data)} items")
    
    def search_item(self):
        if not self.data:
            print("No items to search")
            return
        
        search_term = input("Enter search term: ").lower()
        results = [item for item in self.data if search_term in item.lower()]
        
        if results:
            print(f"\nFound {len(results)} item(s):")
            for item in results:
                print(f"  - {item}")
        else:
            print("No matching items found")
    
    def delete_item(self):
        if not self.data:
            print("No items to delete")
            return
        
        self.view_items()
        try:
            index = int(input("Enter item number to delete: ")) - 1
            if 0 <= index < len(self.data):
                removed = self.data.pop(index)
                print(f"Deleted: {removed}")
            else:
                print("Invalid item number")
        except ValueError:
            print("Please enter a valid number")
    
    def clear_all(self):
        confirm = input("Are you sure you want to clear all items? (y/n): ")
        if confirm.lower() == 'y':
            self.data.clear()
            print("All items cleared")
        else:
            print("Operation cancelled")
    
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
                self.clear_all()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

# Usage
menu = MenuSystem()
menu.run()
```

### Example 4: Password Generator with Validation

```python
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        """Generate random password"""
        pool = self.lowercase
        if use_upper:
            pool += self.uppercase
        if use_digits:
            pool += self.digits
        if use_symbols:
            pool += self.symbols
        
        if not pool:
            return "Error: No character types selected"
        
        password = []
        for _ in range(length):
            password.append(random.choice(pool))
        
        # Ensure at least one of each selected type
        if use_upper and not any(c in self.uppercase for c in password):
            password[0] = random.choice(self.uppercase)
        if use_digits and not any(c in self.digits for c in password):
            password[1] = random.choice(self.digits)
        if use_symbols and not any(c in self.symbols for c in password):
            password[2] = random.choice(self.symbols)
        
        random.shuffle(password)
        return ''.join(password)
    
    def check_strength(self, password):
        """Check password strength"""
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
            feedback.append("✓ Excellent length")
        elif len(password) >= 8:
            score += 1
            feedback.append("✓ Good length")
        else:
            feedback.append("✗ Too short")
        
        # Character variety
        if any(c in self.uppercase for c in password):
            score += 1
            feedback.append("✓ Has uppercase")
        else:
            feedback.append("✗ Missing uppercase")
        
        if any(c in self.digits for c in password):
            score += 1
            feedback.append("✓ Has numbers")
        else:
            feedback.append("✗ Missing numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
            feedback.append("✓ Has special characters")
        else:
            feedback.append("✗ Missing special characters")
        
        # Strength rating
        if score >= 5:
            strength = "VERY STRONG"
        elif score >= 3:
            strength = "STRONG"
        elif score >= 2:
            strength = "WEAK"
        else:
            strength = "VERY WEAK"
        
        return strength, score, feedback
    
    def run(self):
        """Run interactive password generator"""
        print("\n" + "=" * 50)
        print("PASSWORD GENERATOR")
        print("=" * 50)
        
        while True:
            print("\n1. Generate password")
            print("2. Check password strength")
            print("3. Exit")
            
            choice = input("\nEnter choice: ")
            
            if choice == '1':
                while True:
                    try:
                        length = int(input("Password length (8-32): "))
                        if 8 <= length <= 32:
                            break
                        print("Length must be between 8 and 32")
                    except ValueError:
                        print("Please enter a valid number")
                
                use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
                use_digits = input("Include numbers? (y/n): ").lower() == 'y'
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                
                password = self.generate(length, use_upper, use_digits, use_symbols)
                strength, score, feedback = self.check_strength(password)
                
                print(f"\nGenerated Password: {password}")
                print(f"Strength: {strength} (Score: {score}/5)")
                for fb in feedback:
                    print(f"  {fb}")
            
            elif choice == '2':
                password = input("Enter password to check: ")
                strength, score, feedback = self.check_strength(password)
                print(f"\nStrength: {strength} (Score: {score}/5)")
                for fb in feedback:
                    print(f"  {fb}")
            
            elif choice == '3':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice")

# Usage
generator = PasswordGenerator()
generator.run()
```

---

## Common Pitfalls

### Pitfall 1: Infinite Loop

```python
# ❌ INFINITE LOOP - condition never becomes False
count = 0
while count < 5:
    print(count)
    # Missing count += 1

# ✅ CORRECT - Update condition
count = 0
while count < 5:
    print(count)
    count += 1

# ❌ INFINITE LOOP - wrong condition update
count = 5
while count > 0:
    print(count)
    count += 1  # Should be count -= 1

# ✅ CORRECT
count = 5
while count > 0:
    print(count)
    count -= 1
```

### Pitfall 2: Forgetting to Handle User Input

```python
# ❌ No validation - could crash
while True:
    num = int(input("Enter number: "))  # ValueError if not number
    if num == 0:
        break

# ✅ CORRECT - Handle exceptions
while True:
    try:
        num = int(input("Enter number: "))
        if num == 0:
            break
    except ValueError:
        print("Please enter a valid number")
```

### Pitfall 3: Off-by-One Errors

```python
# ❌ WRONG - One extra iteration
count = 0
while count <= 5:  # Runs 6 times (0-5)
    print(count)
    count += 1

# ✅ CORRECT
count = 0
while count < 5:  # Runs 5 times (0-4)
    print(count)
    count += 1
```

---

## Practice Exercises

### Beginner Level

1. **Countdown Timer**
   ```python
   # Print numbers from 10 down to 1 using while loop
   ```

2. **Sum of Numbers**
   ```python
   # Calculate sum of numbers from 1 to n using while loop
   ```

3. **Multiplication Table**
   ```python
   # Print multiplication table using while loop
   ```

4. **Even Numbers**
   ```python
   # Print all even numbers up to n using while loop
   ```

5. **Factorial**
   ```python
   # Calculate factorial using while loop
   ```

### Intermediate Level

6. **Number Guessing Game**
   ```python
   # Create number guessing game with while loop
   ```

7. **Reverse Number**
   ```python
   # Reverse a number using while loop
   ```

8. **Sum of Digits**
   ```python
   # Calculate sum of digits using while loop
   ```

9. **Palindrome Checker**
   ```python
   # Check if number is palindrome using while loop
   ```

10. **User Input Validation**
    ```python
    # Keep asking until user enters valid age (1-120)
    ```

### Advanced Level

11. **ATM Simulator**
    ```python
    # Create ATM with PIN validation and transaction menu
    ```

12. **Menu-Driven Program**
    ```python
    # Create menu system that runs until user chooses exit
    ```

13. **Password Generator**
    ```python
    # Generate passwords until user quits
    ```

---

## Quick Reference Card

```python
# Basic while loop
while condition:
    # code
    # update condition

# Infinite loop
while True:
    # code
    if exit_condition:
        break

# While with else
while condition:
    # code
else:
    # runs if no break

# Common patterns
# Counter
i = 0
while i < n:
    # code
    i += 1

# User input
while True:
    user_input = input("Enter value: ")
    if valid(user_input):
        break

# Sentinel
while True:
    value = get_input()
    if value == sentinel:
        break
    process(value)

# Processing queue
while queue:
    item = queue.pop()
    process(item)
```

---

## Next Step

- Move to [03_loop_control.md](03_loop_control.md) to understand break, continue, and else statements for finer loop control.

---

*Master the while loop for condition-based iteration and user input handling! 🐍✨*
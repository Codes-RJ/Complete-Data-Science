# 📘 INTEGERS (int) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Integers?](#what-are-integers)
2. [Creating Integers](#creating-integers)
3. [All Integer Methods](#all-integer-methods)
4. [Bitwise Operations](#bitwise-operations)
5. [Mathematical Operations](#mathematical-operations)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

---

## 📖 What are Integers?

**Integers** are whole numbers (positive, negative, or zero) without decimal points.

```python
# Examples of integers
positive = 42
negative = -7
zero = 0
large = 1_000_000_000  # Underscores for readability
```

**Key Features:**
- ✅ Unlimited precision (no overflow)
- ✅ Immutable (cannot be changed)
- ✅ Hashable (can be used as dict keys)
- ✅ Supports multiple bases (binary, octal, hex)

---

## 🎯 Creating Integers

### Method 1: Direct Assignment

```python
# Standard decimal
x = 42
print(x)  # 42

# Binary (0b prefix)
binary = 0b101010  # 42 in binary
print(binary)      # 42

# Octal (0o prefix)
octal = 0o52       # 42 in octal
print(octal)       # 42

# Hexadecimal (0x prefix)
hexadecimal = 0x2A  # 42 in hex
print(hexadecimal)  # 42
```

### Method 2: Using `int()` Constructor

```python
# From float (truncates)
print(int(3.14))    # 3
print(int(3.99))    # 3
print(int(-3.14))   # -3

# From string
print(int("42"))     # 42
print(int("-42"))    # -42

# From string with base
print(int("101010", 2))  # 42 (binary)
print(int("52", 8))      # 42 (octal)
print(int("2A", 16))     # 42 (hex)

# From boolean
print(int(True))    # 1
print(int(False))   # 0
```

### Method 3: Using Underscores (Python 3.6+)

```python
# Makes large numbers readable
million = 1_000_000
binary = 0b1111_0000_1111_0000
hex_color = 0xFF_FF_FF

print(million)   # 1000000
```

---

## 🔧 All Integer Methods

### 1. `bit_length()` – Returns bits needed to represent number

```python
# Count bits required
x = 42  # binary: 101010 (6 bits)
print(x.bit_length())  # 6

x = 255  # binary: 11111111 (8 bits)
print(x.bit_length())  # 8

x = 1
print(x.bit_length())  # 1

x = 0
print(x.bit_length())  # 0

# Real use: Finding minimum bits for storage
numbers = [1, 7, 15, 31, 63, 127]
for n in numbers:
    print(f"{n:3d} needs {n.bit_length():2d} bits")
```

**Output:**
```
  1 needs  1 bits
  7 needs  3 bits
 15 needs  4 bits
 31 needs  5 bits
 63 needs  6 bits
127 needs  7 bits
```

### 2. `to_bytes()` – Convert integer to bytes

```python
# Basic conversion
num = 1024
bytes_val = num.to_bytes(2, byteorder='big')
print(bytes_val)  # b'\x04\x00'

# Different byte orders
print(num.to_bytes(2, 'big'))     # b'\x04\x00'
print(num.to_bytes(2, 'little'))  # b'\x00\x04'

# With signed numbers
negative = -1024
signed_bytes = negative.to_bytes(2, 'big', signed=True)
print(signed_bytes)  # b'\xfb\xff'

# Real use: Network packet creation
packet_id = 12345
packet_id_bytes = packet_id.to_bytes(2, 'big')
print(f"Packet ID bytes: {packet_id_bytes}")  # b'09'
```

### 3. `from_bytes()` – Convert bytes to integer (class method)

```python
# Convert bytes back to integer
bytes_data = b'\x04\x00'
num = int.from_bytes(bytes_data, byteorder='big')
print(num)  # 1024

# Different byte orders
bytes_little = b'\x00\x04'
num = int.from_bytes(bytes_little, byteorder='little')
print(num)  # 1024

# Signed conversion
signed_bytes = b'\xfb\xff'
num = int.from_bytes(signed_bytes, 'big', signed=True)
print(num)  # -1024

# Real use: Network packet parsing
received_bytes = b'\x30\x39'  # 12345 in network order
packet_id = int.from_bytes(received_bytes, 'big')
print(f"Received packet ID: {packet_id}")  # 12345
```

### 4. `as_integer_ratio()` – Returns numerator/denominator

```python
# For integers, ratio is (int, 1)
x = 42
print(x.as_integer_ratio())  # (42, 1)

# Real use: Fraction representation
from fractions import Fraction
value = 5
frac = Fraction(*value.as_integer_ratio())
print(f"{value} = {frac.numerator}/{frac.denominator}")  # 5 = 5/1
```

### 5. `conjugate()` – Returns self (for complex compatibility)

```python
# For integers, just returns the number itself
x = 42
print(x.conjugate())  # 42

# Useful when writing generic numeric code
def process_number(n):
    if hasattr(n, 'conjugate'):
        return n.conjugate()
    return n
```

---

## ⚡ Bitwise Operations

Bitwise operations work only on integers (not floats or complex).

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(f"a = {a} ({bin(a)})")
print(f"b = {b} ({bin(b)})")
print()

# AND (&) - Both bits must be 1
print(f"a & b = {a & b} ({bin(a & b)})")  # 0001 = 1

# OR (|) - At least one bit is 1
print(f"a | b = {a | b} ({bin(a | b)})")  # 0111 = 7

# XOR (^) - Bits are different
print(f"a ^ b = {a ^ b} ({bin(a ^ b)})")  # 0110 = 6

# NOT (~) - Inverts all bits
print(f"~a = {~a} ({bin(~a)})")  # -6

# Left Shift (<<) - Shift bits left (multiply by 2^n)
print(f"a << 1 = {a << 1} ({bin(a << 1)})")  # 1010 = 10
print(f"a << 2 = {a << 2} ({bin(a << 2)})")  # 10100 = 20

# Right Shift (>>) - Shift bits right (divide by 2^n)
print(f"a >> 1 = {a >> 1} ({bin(a >> 1)})")  # 0010 = 2
print(f"a >> 2 = {a >> 2} ({bin(a >> 2)})")  # 0001 = 1
```

**Output:**
```
a = 5 (0b101)
b = 3 (0b11)

a & b = 1 (0b1)
a | b = 7 (0b111)
a ^ b = 6 (0b110)
~a = -6 (-0b110)
a << 1 = 10 (0b1010)
a << 2 = 20 (0b10100)
a >> 1 = 2 (0b10)
a >> 2 = 1 (0b1)
```

---

## 📐 Mathematical Operations

### Basic Arithmetic

```python
a, b = 15, 4

print(f"{a} + {b} = {a + b}")   # 19
print(f"{a} - {b} = {a - b}")   # 11
print(f"{a} * {b} = {a * b}")   # 60
print(f"{a} / {b} = {a / b}")   # 3.75 (returns float)
print(f"{a} // {b} = {a // b}") # 3 (floor division)
print(f"{a} % {b} = {a % b}")   # 3 (modulus)
print(f"{a} ** {b} = {a ** b}") # 50625 (power)
```

### Comparison Operations

```python
a, b = 10, 20

print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} < {b}: {a < b}")    # True
print(f"{a} > {b}: {a > b}")    # False
print(f"{a} <= {b}: {a <= b}")  # True
print(f"{a} >= {b}: {a >= b}")  # False
```

### Built-in Functions

```python
numbers = [-5, 0, 42, -10, 7]

print(f"Sum: {sum(numbers)}")          # 34
print(f"Max: {max(numbers)}")          # 42
print(f"Min: {min(numbers)}")          # -10
print(f"Absolute: {abs(-42)}")         # 42
print(f"Power: {pow(2, 3)}")           # 8
print(f"Divmod: {divmod(15, 4)}")      # (3, 3) (quotient, remainder)
```

---

## 🌍 Real-World Examples

### Example 1: ATM PIN Validation System

```python
correct_pin = 1234
max_attempts = 3
attempts = 0
account_locked = False

print("Welcome to Python Bank ATM")
print("-" * 30)

while attempts < max_attempts and not account_locked:
    try:
        pin = int(input("Enter your 4-digit PIN: "))
        
        if pin == correct_pin:
            print("✅ Access granted!")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Wrong PIN! {remaining} attempt(s) remaining")
            else:
                print("❌ Too many failed attempts! Account locked!")
                account_locked = True
    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Output:
# Welcome to Python Bank ATM
# ------------------------------
# Enter your 4-digit PIN: 1111
# ❌ Wrong PIN! 2 attempt(s) remaining
# Enter your 4-digit PIN: 1234
# ✅ Access granted!
# 1. Check Balance
# 2. Withdraw
# 3. Deposit
```

### Example 2: Permission System (Linux-style)

```python
# Permission flags
READ = 1      # 001 (binary)
WRITE = 2     # 010
EXECUTE = 4   # 100

# Grant permissions (using OR)
user_permissions = READ | WRITE  # 1|2 = 3 (011)

print(f"User permissions: {user_permissions} (binary: {bin(user_permissions)})")
print("\nChecking permissions:")
print("-" * 30)

# Check permissions (using AND)
if user_permissions & READ:
    print("✓ Read permission granted")
else:
    print("✗ Read permission denied")

if user_permissions & WRITE:
    print("✓ Write permission granted")
else:
    print("✗ Write permission denied")

if user_permissions & EXECUTE:
    print("✓ Execute permission granted")
else:
    print("✗ Execute permission denied")

# Add execute permission
user_permissions |= EXECUTE
print(f"\nAfter adding execute: {user_permissions} (binary: {bin(user_permissions)})")
print("✓ Execute permission granted")

# Remove write permission
user_permissions &= ~WRITE
print(f"\nAfter removing write: {user_permissions} (binary: {bin(user_permissions)})")
print("✗ Write permission revoked")
```

**Output:**
```
User permissions: 3 (binary: 0b11)

Checking permissions:
------------------------------
✓ Read permission granted
✓ Write permission granted
✗ Execute permission denied

After adding execute: 7 (binary: 0b111)
✓ Execute permission granted

After removing write: 5 (binary: 0b101)
✗ Write permission revoked
```

### Example 3: Prime Number Checker

```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Find all primes up to 100
print("Prime numbers up to 100:")
print("-" * 30)

primes = []
for num in range(1, 101):
    if is_prime(num):
        primes.append(num)
        print(f"{num:3d} is PRIME ✨")
    else:
        print(f"{num:3d} is composite")

print("-" * 30)
print(f"Total primes found: {len(primes)}")
print(f"Primes list: {primes}")
```

### Example 4: Binary Counter with Bit Operations

```python
def binary_counter(n):
    """Display numbers from 0 to n in binary"""
    max_bits = n.bit_length()
    
    print(f"Counting from 0 to {n}:")
    print("=" * 40)
    
    for i in range(n + 1):
        binary = bin(i)[2:].zfill(max_bits)  # Remove '0b' and pad
        parity = "even" if i % 2 == 0 else "odd"
        print(f"{i:3d} | {binary} | {parity} | bit_length: {i.bit_length():2d}")

binary_counter(15)
```

**Output:**
```
Counting from 0 to 15:
========================================
  0 | 0000 | even | bit_length:  0
  1 | 0001 | odd  | bit_length:  1
  2 | 0010 | even | bit_length:  2
  3 | 0011 | odd  | bit_length:  2
  4 | 0100 | even | bit_length:  3
  5 | 0101 | odd  | bit_length:  3
  6 | 0110 | even | bit_length:  3
  7 | 0111 | odd  | bit_length:  3
  8 | 1000 | even | bit_length:  4
  9 | 1001 | odd  | bit_length:  4
 10 | 1010 | even | bit_length:  4
 11 | 1011 | odd  | bit_length:  4
 12 | 1100 | even | bit_length:  4
 13 | 1101 | odd  | bit_length:  4
 14 | 1110 | even | bit_length:  4
 15 | 1111 | odd  | bit_length:  4
```

### Example 5: Age Group Classifier

```python
def classify_age(age):
    """Classify age into groups"""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# Process multiple ages
ages = [5, 12, 15, 18, 25, 35, 45, 60, 65, 75, 100]

print("Age Classification Report")
print("=" * 40)

for age in ages:
    category = classify_age(age)
    
    # Additional messages based on category
    if category == "Child":
        message = "🎮 Eligible for kids activities"
    elif category == "Teenager":
        message = "📱 Can have social media"
    elif category == "Adult":
        message = "💼 Eligible to vote and work"
    else:  # Senior
        message = "🎫 Eligible for senior discounts"
    
    print(f"Age {age:3d}: {category:10s} - {message}")
```

**Output:**
```
Age Classification Report
========================================
Age   5: Child      - 🎮 Eligible for kids activities
Age  12: Child      - 🎮 Eligible for kids activities
Age  15: Teenager   - 📱 Can have social media
Age  18: Teenager   - 📱 Can have social media
Age  25: Adult      - 💼 Eligible to vote and work
Age  35: Adult      - 💼 Eligible to vote and work
Age  45: Adult      - 💼 Eligible to vote and work
Age  60: Senior     - 🎫 Eligible for senior discounts
Age  65: Senior     - 🎫 Eligible for senior discounts
Age  75: Senior     - 🎫 Eligible for senior discounts
Age 100: Senior     - 🎫 Eligible for senior discounts
```

### Example 6: Factorial Calculator

```python
def factorial_iterative(n):
    """Calculate factorial iteratively"""
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial recursively"""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Compare both methods
numbers = [0, 5, 7, 10, 15]

print("Factorial Calculator")
print("=" * 50)
print(f"{'n':3s} | {'Iterative':15s} | {'Recursive':15s} | {'Digits':6s}")
print("-" * 50)

for n in numbers:
    iter_fact = factorial_iterative(n)
    rec_fact = factorial_recursive(n)
    digits = len(str(iter_fact))
    
    print(f"{n:3d} | {iter_fact:15,} | {rec_fact:15,} | {digits:6d}")

# Large factorial (Python handles big numbers)
n = 20
large_fact = factorial_iterative(n)
print(f"\n{n}! = {large_fact:,}")
print(f"Number of digits: {len(str(large_fact))}")
```

**Output:**
```
Factorial Calculator
==================================================
n   | Iterative       | Recursive       | Digits
--------------------------------------------------
  0 |               1 |               1 |      1
  5 |             120 |             120 |      3
  7 |           5,040 |           5,040 |      4
 10 |       3,628,800 |       3,628,800 |      7
 15 |   1,307,674,368,000 |   1,307,674,368,000 |     13

20! = 2,432,902,008,176,640,000
Number of digits: 19
```

### Example 7: Even/Odd Analyzer

```python
def analyze_numbers(numbers):
    """Analyze a list of numbers"""
    even_count = 0
    odd_count = 0
    even_sum = 0
    odd_sum = 0
    even_list = []
    odd_list = []
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
            even_sum += num
            even_list.append(num)
        else:
            odd_count += 1
            odd_sum += num
            odd_list.append(num)
    
    return {
        'even_count': even_count,
        'odd_count': odd_count,
        'even_sum': even_sum,
        'odd_sum': odd_sum,
        'even_list': even_list,
        'odd_list': odd_list
    }

# Test data
data = [23, 45, 12, 67, 89, 34, 56, 78, 91, 44, 100, 37, 28, 55, 82]

results = analyze_numbers(data)

print("Number Analysis Report")
print("=" * 50)
print(f"Total numbers: {len(data)}")
print(f"Even numbers: {results['even_count']}")
print(f"Odd numbers: {results['odd_count']}")
print(f"Even sum: {results['even_sum']}")
print(f"Odd sum: {results['odd_sum']}")
print(f"Even average: {results['even_sum']/results['even_count']:.2f}")
print(f"Odd average: {results['odd_sum']/results['odd_count']:.2f}")
print(f"\nEven numbers: {results['even_list']}")
print(f"Odd numbers: {results['odd_list']}")

# Find largest even and odd
if results['even_list']:
    print(f"\nLargest even: {max(results['even_list'])}")
if results['odd_list']:
    print(f"Largest odd: {max(results['odd_list'])}")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Division Always Returns Float

```python
# ❌ WRONG - Expecting integer division
result = 5 / 2
print(result)  # 2.5, not 2!

# ✅ CORRECT - Use // for integer division
result = 5 // 2
print(result)  # 2

# ✅ CORRECT - Use int() to truncate
result = int(5 / 2)
print(result)  # 2
```

### Pitfall 2: Integer Overflow Doesn't Exist (That's Good!)

```python
# In other languages, this would overflow
# In Python, it works perfectly
huge_number = 10 ** 1000  # 1 followed by 1000 zeros
print(f"Number of digits: {len(str(huge_number))}")  # 1001 digits

# You can work with arbitrarily large numbers
print(huge_number % 7)  # Works fine!
```

### Pitfall 3: Modulus with Negative Numbers

```python
# Python's modulo returns positive remainder
print(10 % 3)   # 1
print(-10 % 3)  # 2 (not -1!)

# For negative numbers, remainder = divisor - abs(remainder)
print(-10 % 3)  # 2 because 3 - 1 = 2

# Use math.fmod for C-like behavior
import math
print(math.fmod(-10, 3))  # -1.0
```

### Pitfall 4: Comparing int with bool

```python
# bool is subclass of int (True=1, False=0)
print(True == 1)   # True
print(False == 0)  # True

# This can cause subtle bugs
def count_items(items):
    return len(items)

items = [1, 2, 3]
if count_items(items) == True:  # Works but confusing
    print("Has items")

# ✅ Better
if count_items(items):
    print("Has items")
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Even or Odd Checker**
   ```python
   # Write a program that checks if a number is even or odd
   # Use both modulus (%) and bitwise (&) methods
   ```

2. **Sum of Digits**
   ```python
   # Calculate sum of digits of a number
   # Example: 123 → 1+2+3 = 6
   ```

3. **Reverse Number**
   ```python
   # Reverse digits of a number
   # Example: 12345 → 54321
   ```

### Intermediate Level

4. **Palindrome Number**
   ```python
   # Check if a number reads the same backward and forward
   # Example: 12321 is palindrome, 12345 is not
   ```

5. **Fibonacci Sequence**
   ```python
   # Generate first n Fibonacci numbers
   # 0, 1, 1, 2, 3, 5, 8, 13, ...
   ```

6. **GCD Calculator**
   ```python
   # Find Greatest Common Divisor using Euclidean algorithm
   # Example: gcd(48, 18) = 6
   ```

### Advanced Level

7. **Prime Factor Finder**
   ```python
   # Find all prime factors of a number
   # Example: 84 → 2, 2, 3, 7
   ```

8. **Perfect Number Checker**
   ```python
   # Perfect number = sum of divisors equals the number
   # Example: 6 = 1+2+3, 28 = 1+2+4+7+14
   ```

9. **Bit Manipulation Utilities**
   ```python
   # Create functions to:
   # - Count set bits (1s) in binary representation
   # - Check if number is power of 2
   # - Swap two numbers without temporary variable
   ```

---

## 🔗 Next Steps

After mastering integers:
1. Move to `02_floats.md` for decimal numbers
2. Learn `03_complex_numbers.md` for engineering math
3. Complete the practice exercises above

---

## 📚 Quick Reference Card

```python
# Creation
x = 42                    # Decimal
x = 0b101010             # Binary
x = 0o52                 # Octal
x = 0x2A                 # Hex
x = int("42")            # From string

# Methods
x.bit_length()           # Bits needed
x.to_bytes(2, 'big')     # To bytes
int.from_bytes(b, 'big') # From bytes

# Bitwise ops
x & y   # AND
x | y   # OR
x ^ y   # XOR
~x      # NOT
x << n  # Left shift
x >> n  # Right shift

# Math ops
x + y   # Add
x - y   # Subtract
x * y   # Multiply
x / y   # Division (float)
x // y  # Floor division
x % y   # Modulus
x ** y  # Power
```

---

*Master integers, and you've mastered the foundation of Python numbers! 🐍✨*

---
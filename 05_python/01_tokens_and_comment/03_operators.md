# Operators in Python ➕

---

## What are Operators?

Operators are special symbols that perform operations on variables and values. They are the building blocks that allow you to manipulate data.

```python
# Operator example
result = 10 + 5  # '+' is the operator, '10' and '5' are operands
print(result)    # 15
```

---

## Types of Operators in Python

| Category | Operators |
|----------|-----------|
| Arithmetic | +, -, *, /, //, %, ** |
| Comparison | ==, !=, >, <, >=, <= |
| Logical | and, or, not |
| Assignment | =, +=, -=, *=, /=, //=, %=, **= |
| Bitwise | &, \|, ^, ~, <<, >> |
| Membership | in, not in |
| Identity | is, is not |

---

## 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | 10 + 5 | 15 |
| - | Subtraction | 10 - 5 | 5 |
| * | Multiplication | 10 * 5 | 50 |
| / | Division (float) | 10 / 3 | 3.333 |
| // | Floor Division (integer) | 10 // 3 | 3 |
| % | Modulus (remainder) | 10 % 3 | 1 |
| ** | Exponentiation (power) | 2 ** 3 | 8 |

### Code Examples:

```python
# Basic arithmetic
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335
print(a // b)  # 3 (floor division - rounds down)
print(a % b)   # 1 (remainder)
print(a ** b)  # 1000 (10 to the power 3)

# Practical examples
total = 100 + 50 + 30
print(total)  # 180

average = total / 3
print(average)  # 60.0

is_even = 8 % 2
print(is_even)  # 0 (remainder 0 means even)

square = 4 ** 2
print(square)  # 16
```

---

## 2. Comparison Operators

Used to compare values. Returns True or False.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| == | Equal to | 5 == 5 | True |
| != | Not equal to | 5 != 3 | True |
| > | Greater than | 5 > 3 | True |
| < | Less than | 5 < 3 | False |
| >= | Greater than or equal | 5 >= 5 | True |
| <= | Less than or equal | 5 <= 3 | False |

### Code Examples:

```python
x = 10
y = 20

print(x == y)   # False (10 equals 20? No)
print(x != y)   # True (10 not equal 20? Yes)
print(x > y)    # False (10 greater than 20? No)
print(x < y)    # True (10 less than 20? Yes)
print(x >= 10)  # True (10 greater than or equal 10? Yes)
print(x <= 5)   # False (10 less than or equal 5? No)

# Using comparisons in conditions
age = 18
if age >= 18:
    print("You can vote")  # This runs

score = 85
if score >= 60:
    print("Pass")  # This runs
else:
    print("Fail")
```

---

## 3. Logical Operators

Used to combine conditional statements.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| and | Logical AND | True and False | False |
| or | Logical OR | True or False | True |
| not | Logical NOT | not True | False |

### Truth Table:

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

### Code Examples:

```python
# and - BOTH conditions must be True
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")  # This runs (both True)

# or - AT LEAST ONE condition must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")  # This runs (weekend is True)

# not - REVERSES the boolean value
is_raining = False

if not is_raining:
    print("Go outside")  # This runs (not False = True)

# Complex conditions
temperature = 25
is_sunny = True

if temperature > 20 and temperature < 30 and is_sunny:
    print("Perfect weather")  # This runs

# Using parentheses for clarity
if (age >= 18) and (has_license == True):
    print("Valid driver")
```

---

## 4. Assignment Operators

Used to assign values to variables.

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| //= | x //= 3 | x = x // 3 |
| %= | x %= 3 | x = x % 3 |
| **= | x **= 3 | x = x ** 3 |

### Code Examples:

```python
# Basic assignment
x = 10
print(x)  # 10

# Addition assignment
x = 5
x += 3   # Same as: x = x + 3
print(x)  # 8

# Subtraction assignment
x = 10
x -= 4   # Same as: x = x - 4
print(x)  # 6

# Multiplication assignment
x = 4
x *= 3   # Same as: x = x * 3
print(x)  # 12

# Division assignment
x = 15
x /= 3   # Same as: x = x / 3
print(x)  # 5.0

# Floor division assignment
x = 17
x //= 5  # Same as: x = x // 5
print(x)  # 3

# Modulus assignment
x = 17
x %= 5   # Same as: x = x % 5
print(x)  # 2

# Exponent assignment
x = 2
x **= 3  # Same as: x = x ** 3
print(x)  # 8

# Practical use - counters
counter = 0
counter += 1  # counter = 1
counter += 1  # counter = 2
print(counter)  # 2

# String concatenation
message = "Hello"
message += " World"
print(message)  # Hello World
```

---

## 5. Bitwise Operators

Work on bits (binary representation).

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| & | AND | 5 & 3 | 1 |
| \| | OR | 5 \| 3 | 7 |
| ^ | XOR | 5 ^ 3 | 6 |
| ~ | NOT | ~5 | -6 |
| << | Left shift | 5 << 1 | 10 |
| >> | Right shift | 5 >> 1 | 2 |

### Code Examples:

```python
# Binary representation
# 5 in binary:  0101
# 3 in binary:  0011

# Bitwise AND (both bits 1 = 1)
print(5 & 3)   # 0001 = 1

# Bitwise OR (at least one bit 1 = 1)
print(5 | 3)   # 0111 = 7

# Bitwise XOR (bits different = 1)
print(5 ^ 3)   # 0110 = 6

# Bitwise NOT (flips all bits)
print(~5)      # -6

# Left shift (shifts bits left, adds zeros)
print(5 << 1)  # 1010 = 10
print(5 << 2)  # 10100 = 20

# Right shift (shifts bits right)
print(5 >> 1)  # 0010 = 2
print(5 >> 2)  # 0001 = 1
```

---

## 6. Membership Operators

Used to test if a value exists in a sequence.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| in | Returns True if value exists | "a" in "apple" | True |
| not in | Returns True if value does NOT exist | "b" in "apple" | False |

### Code Examples:

```python
# Strings
text = "Hello World"
print("H" in text)      # True
print("X" in text)      # False
print("World" in text)  # True
print("x" not in text)  # True

# Lists
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)    # True
print("grape" in fruits)     # False
print("grape" not in fruits) # True

# Tuples
numbers = (1, 2, 3, 4, 5)
print(3 in numbers)   # True
print(10 in numbers)  # False

# Dictionaries (checks keys)
person = {"name": "Alice", "age": 25}
print("name" in person)     # True (checks keys)
print("Alice" in person)    # False (doesn't check values)
print("Alice" in person.values())  # True (checks values)

# Ranges
print(5 in range(10))   # True
print(15 in range(10))  # False

# Practical use
user_input = "yes"
if user_input in ["yes", "y", "yeah"]:
    print("User agreed")
```

---

## 7. Identity Operators

Used to compare if two objects are the same (memory location).

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| is | True if same object | a is b | True/False |
| is not | True if different objects | a is not b | True/False |

### Difference between == and is:

- `==` compares values (content)
- `is` compares identity (memory location)

### Code Examples:

```python
# Same value, different objects
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (same values)
print(a is b)   # False (different objects in memory)

# Same object
c = a
print(a is c)   # True (same object)

# With integers (small integers are cached)
x = 10
y = 10
print(x is y)   # True (Python caches small integers)

# With strings (interning)
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True (Python interns strings)

# is not
print(a is not b)  # True (different objects)

# Practical use (checking for None)
result = None
if result is None:
    print("No result")  # This runs

# Better than == for None
if result == None:   # Works but not recommended
    print("Use 'is' instead")
```

---

## Operator Precedence

Determines which operator is evaluated first.

| Precedence | Operators | Description |
|------------|-----------|-------------|
| 1 (Highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, floor, modulus |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (Lowest) | `or` | Logical OR |

### Code Examples:

```python
# Without parentheses (follows precedence)
result = 10 + 5 * 2
print(result)  # 20 (5*2 first, then +10)

# With parentheses (overrides precedence)
result = (10 + 5) * 2
print(result)  # 30 (parentheses first)

# Complex example
x = 2 + 3 * 4 ** 2 - 8 / 2
# Steps:
# 4 ** 2 = 16
# 3 * 16 = 48
# 8 / 2 = 4
# 2 + 48 - 4 = 46
print(x)  # 46

# Using parentheses for clarity
y = 2 + (3 * (4 ** 2)) - (8 / 2)
print(y)  # 46 (same but clearer)
```

---

## Operator Overloading

Same operator can behave differently based on data type.

```python
# '+' operator works differently for different types
print(5 + 3)          # 8 (integer addition)
print(5.5 + 2.3)      # 7.8 (float addition)
print("Hello" + " World")  # Hello World (string concatenation)
print([1, 2] + [3, 4])     # [1, 2, 3, 4] (list concatenation)

# '*' operator
print(5 * 3)          # 15 (multiplication)
print("Ha" * 3)       # HaHaHa (string repetition)
print([1, 2] * 3)     # [1, 2, 1, 2, 1, 2] (list repetition)
```

---

## Practice Exercises

### Exercise 1: Arithmetic Operations
Write a program that takes two numbers and prints their sum, difference, product, and quotient.

```python
# Solution
a = 15
b = 4

print(f"Sum: {a + b}")          # 19
print(f"Difference: {a - b}")   # 11
print(f"Product: {a * b}")      # 60
print(f"Quotient: {a / b}")     # 3.75
print(f"Floor: {a // b}")       # 3
print(f"Remainder: {a % b}")    # 3
```

### Exercise 2: Comparison and Logical Operators
Check if a number is between 10 and 20 (inclusive).

```python
# Solution
num = 15

if num >= 10 and num <= 20:
    print(f"{num} is between 10 and 20")
else:
    print(f"{num} is not between 10 and 20")
```

### Exercise 3: Assignment Operators
Start with x = 10, then add 5, multiply by 2, subtract 3.

```python
# Solution
x = 10
x += 5   # 15
x *= 2   # 30
x -= 3   # 27
print(x)  # 27
```

### Exercise 4: Membership Operator
Check if a letter is a vowel.

```python
# Solution
letter = "a"
vowels = ["a", "e", "i", "o", "u"]

if letter in vowels:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
```

### Exercise 5: Identity Operator
Explain the output.

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)   # ?
print(x is y)   # ?
print(x is z)   # ?

# Solution:
# True (same values)
# False (different objects)
# True (same object)
```

---

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `TypeError` | Using operator with wrong types | `"5" + 3` → convert to same type |
| `NameError` | Variable not defined | Define variable before using |
| `SyntaxError` | Wrong operator syntax | Check spelling (`= =` should be `==`) |

---

## Key Takeaways

- Operators perform operations on variables and values
- Different operator types serve different purposes
- Operator precedence determines evaluation order
- Use parentheses to make expressions clear
- `==` compares values, `is` compares identity

---

## Next Steps

- Proceed to [04_punctuators.md](./04_punctuators.md) to learn about if-else and loops
- Practice writing expressions with different operators

---

*"Operators are the verbs of programming - they make things happen."*
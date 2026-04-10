# 🔄 TYPE CONVERSION – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Types of Conversion](#types-of-conversion)
3. [Implicit Conversion](#implicit-conversion)
4. [Explicit Conversion](#explicit-conversion)
5. [Common Conversion Functions](#common-conversion-functions)
6. [When to Use Each](#when-to-use-each)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Type conversion** is the process of converting a value from one data type to another. Python supports both implicit (automatic) and explicit (manual) conversion.

```python
# Implicit conversion (automatic)
result = 5 + 2.5    # int + float = float (7.5)

# Explicit conversion (manual)
num_str = "123"
num_int = int(num_str)  # "123" → 123
```

**Key Characteristics:**
- ✅ Python is strongly typed (no automatic mixing of incompatible types)
- ✅ Implicit conversion happens for compatible types (int → float)
- ✅ Explicit conversion required for incompatible types (str → int)
- ✅ Conversion functions return new objects (originals unchanged)

---

## 🔄 Types of Conversion

### Implicit Conversion (Automatic)

Python automatically converts types when safe and lossless.

```python
# int to float (widening)
x = 10          # int
y = 3.14        # float
z = x + y       # float (13.14)
print(type(z))  # <class 'float'>

# int to bool
x = 0
if x:           # 0 → False
    print("True")
else:
    print("False")

# bool to int
count = True + True + False  # 1 + 1 + 0 = 2
print(count)    # 2

# int to complex
c = 5 + 2j
result = 10 + c  # int → complex (15+2j)
print(result)    # (15+2j)
```

### Explicit Conversion (Manual)

You must explicitly convert between incompatible types.

```python
# String to number (required)
num_str = "123"
# result = num_str + 456  # TypeError!
num_int = int(num_str)
result = num_int + 456    # 579

# Number to string
num = 42
text = "The answer is " + str(num)  # "The answer is 42"

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)

# Tuple to list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)   # [1, 2, 3]
```

---

## 📊 Common Conversion Functions

### Numeric Conversions

| Function | Description | Example | Result |
|----------|-------------|---------|--------|
| `int(x)` | Convert to integer | `int(3.14)` | `3` |
| `float(x)` | Convert to float | `float(42)` | `42.0` |
| `complex(x)` | Convert to complex | `complex(5)` | `(5+0j)` |
| `bool(x)` | Convert to boolean | `bool(1)` | `True` |

```python
# int()
print(int(3.14))      # 3 (truncates)
print(int("42"))      # 42
print(int("FF", 16))  # 255 (hex conversion)
print(int(True))      # 1

# float()
print(float(42))      # 42.0
print(float("3.14"))  # 3.14
print(float("inf"))   # inf

# complex()
print(complex(5))     # (5+0j)
print(complex(2, 3))  # (2+3j)
print(complex("3+4j"))# (3+4j)

# bool()
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))       # False
print(bool("hello"))  # True
```

### Sequence Conversions

| Function | Description | Example | Result |
|----------|-------------|---------|--------|
| `str(x)` | Convert to string | `str(42)` | `"42"` |
| `list(x)` | Convert to list | `list("abc")` | `['a','b','c']` |
| `tuple(x)` | Convert to tuple | `tuple([1,2,3])` | `(1,2,3)` |
| `set(x)` | Convert to set | `set([1,2,2,3])` | `{1,2,3}` |

```python
# str()
print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str(True))      # "True"
print(str([1, 2, 3])) # "[1, 2, 3]"

# list()
print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']
print(list((1,2,3)))  # [1, 2, 3]
print(list(range(5))) # [0, 1, 2, 3, 4]

# tuple()
print(tuple([1,2,3])) # (1, 2, 3)
print(tuple("abc"))   # ('a', 'b', 'c')
print(tuple(range(3)))# (0, 1, 2)

# set()
print(set([1,2,2,3])) # {1, 2, 3}
print(set("hello"))   # {'h', 'e', 'l', 'o'}
```

### Specialized Conversions

| Function | Description | Example | Result |
|----------|-------------|---------|--------|
| `chr(x)` | Int to character | `chr(65)` | `'A'` |
| `ord(c)` | Character to int | `ord('A')` | `65` |
| `hex(x)` | Int to hex string | `hex(255)` | `'0xff'` |
| `bin(x)` | Int to binary string | `bin(42)` | `'0b101010'` |
| `oct(x)` | Int to octal string | `oct(42)` | `'0o52'` |

```python
# chr() and ord()
print(chr(65))        # 'A'
print(chr(97))        # 'a'
print(ord('A'))       # 65
print(ord('♥'))       # 9829

# hex(), bin(), oct()
print(hex(255))       # '0xff'
print(bin(42))        # '0b101010'
print(oct(42))        # '0o52'

# Remove prefix
print(hex(255)[2:])   # 'ff'
print(bin(42)[2:])    # '101010'
```

---

## ⚠️ When to Use Each

### Numeric Conversions

```python
# User input (always string)
age_str = input("Enter age: ")  # "25"
age = int(age_str)              # Convert to int

# Mathematical operations
result = 10 / 3                 # 3.333...
int_result = int(result)        # 3 (floor)

# Formatted output
pi = 3.14159
print("Pi is " + str(pi))       # "Pi is 3.14159"
```

### Sequence Conversions

```python
# Remove duplicates
my_list = [1, 2, 2, 3, 3, 3]
unique = list(set(my_list))     # [1, 2, 3]

# Convert string to list of characters
text = "hello"
chars = list(text)              # ['h','e','l','l','o']

# Convert list to tuple (immutable)
scores = [85, 90, 88]
immutable_scores = tuple(scores)  # (85, 90, 88)

# Convert range to list
numbers = list(range(10))       # [0,1,2,3,4,5,6,7,8,9]
```

### Type Checking Before Conversion

```python
def safe_int_convert(value):
    """Safely convert to int, return None if not possible"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(safe_int_convert("123"))    # 123
print(safe_int_convert("abc"))    # None
print(safe_int_convert(3.14))     # 3
```

---

## 💡 Quick Tips

```python
# Convert string to int (handle errors)
try:
    num = int(user_input)
except ValueError:
    print("Invalid number")

# Convert list to string
words = ["Hello", "World"]
text = " ".join(words)          # "Hello World"

# Convert string to list
text = "a,b,c"
items = text.split(",")          # ['a', 'b', 'c']

# Convert between number bases
num = 42
print(bin(num))     # '0b101010'
print(hex(num))     # '0x2a'
print(oct(num))     # '0o52'

# Convert back from base
print(int('101010', 2))   # 42
print(int('2a', 16))      # 42
print(int('52', 8))       # 42

# Type checking before conversion
if isinstance(value, (int, float)):
    result = int(value)
elif isinstance(value, str) and value.isdigit():
    result = int(value)
else:
    result = None
```

---

## Next Step

- Go to [explicit_conversion.md](explicit_conversion.md) for understanding Explicit Type Conversion.
---

## 🔗 Related Topics

- **Type Checking** – `isinstance()`, `type()`
- **Type Hints** – Optional static typing
- **Casting** – C-style type conversion
- **String Formatting** – Converting values to strings

---

*Master type conversion to handle different data types effectively! 🐍✨*
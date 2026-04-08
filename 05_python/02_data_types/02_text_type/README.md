# 📝 TEXT TYPE (str) – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Creating Strings](#creating-strings)
3. [String Characteristics](#string-characteristics)
4. [Basic Operations](#basic-operations)
5. [Common String Methods](#common-string-methods)
6. [String Formatting](#string-formatting)
7. [When to Use Strings](#when-to-use-strings)
8. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Strings** are sequences of Unicode characters used to represent text in Python.

```python
# Examples of strings
name = "Python"
message = 'Hello, World!'
multi_line = """This is
a multi-line
string"""
empty = ""
```

**Key Features:**
- ✅ Immutable (cannot be changed after creation)
- ✅ Ordered (characters have positions)
- ✅ Indexable and sliceable
- ✅ Unicode support (any language)
- ✅ Rich set of methods

---

## 🎯 Creating Strings

### Method 1: Quotes

```python
# Single quotes
single = 'Hello'

# Double quotes
double = "World"

# Triple quotes (multi-line)
multi = """Line 1
Line 2
Line 3"""

# Triple single quotes also work
multi2 = '''Line 1
Line 2'''
```

### Method 2: Using `str()` Constructor

```python
# From different types
str(42)        # "42"
str(3.14)      # "3.14"
str(True)      # "True"
str([1, 2, 3]) # "[1, 2, 3]"

# Empty string
empty = str()
```

### Method 3: Escape Sequences

```python
# Common escape sequences
print("Hello\nWorld")    # Newline
print("Hello\tWorld")    # Tab
print("Hello\\World")    # Backslash
print("Hello\"World")    # Double quote
print("Hello\'World")    # Single quote
print("Hello\rWorld")    # Carriage return

# Raw strings (ignore escape sequences)
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents
```

---

## 🔧 String Characteristics

### Immutability

```python
# Strings cannot be changed
s = "Hello"
# s[0] = "J"  # TypeError!

# Create new string instead
s = "J" + s[1:]  # "Jello"
```

### Indexing and Slicing

```python
s = "Python"

# Indexing (0-based)
print(s[0])    # 'P'
print(s[-1])   # 'n' (last character)

# Slicing [start:end:step]
print(s[0:3])   # "Pyt" (indices 0,1,2)
print(s[:3])    # "Pyt" (from start)
print(s[3:])    # "hon" (to end)
print(s[::2])   # "Pto" (every 2nd)
print(s[::-1])  # "nohtyP" (reverse)
```

### Length

```python
s = "Python"
print(len(s))  # 6

empty = ""
print(len(empty))  # 0
```

---

## ⚡ Basic Operations

### Concatenation and Repetition

```python
# Concatenation (+)
first = "Hello"
last = "World"
full = first + " " + last
print(full)  # "Hello World"

# Repetition (*)
print("Ha" * 3)  # "HaHaHa"
print("-" * 20)  # "--------------------"
```

### Membership Testing

```python
text = "Python Programming"

print("Python" in text)     # True
print("Java" in text)       # False
print("gram" in text)       # True
print("x" not in text)      # True
```

### Comparison

```python
# Lexicographic (dictionary) order
print("apple" < "banana")   # True
print("Apple" < "apple")    # True (ASCII order)
print("abc" == "abc")       # True
print("abc" != "def")       # True
```

### Iteration

```python
# Loop through characters
for char in "Python":
    print(char)
# Output: P y t h o n

# With index
for i, char in enumerate("Python"):
    print(f"{i}: {char}")
# Output: 0:P, 1:y, 2:t, 3:h, 4:o, 5:n
```

---

## 📚 Common String Methods

### Case Conversion

```python
s = "Hello World"

print(s.upper())      # "HELLO WORLD"
print(s.lower())      # "hello world"
print(s.capitalize()) # "Hello world"
print(s.title())      # "Hello World"
print(s.swapcase())   # "hELLO wORLD"
```

### Checking Content

```python
s = "Python123"

print(s.isalpha())    # False (has numbers)
print(s.isdigit())    # False (has letters)
print(s.isalnum())    # True (letters/numbers only)
print(s.islower())    # False
print(s.isupper())    # False
print(s.isspace())    # False
print(s.startswith("Py"))  # True
print(s.endswith("123"))   # True
```

### Finding and Replacing

```python
s = "Hello Hello Hello"

# Find
print(s.find("Hello"))    # 0 (first occurrence)
print(s.rfind("Hello"))   # 12 (last occurrence)
print(s.index("Hello"))   # 0 (like find, but raises error if not found)
print(s.count("Hello"))   # 3

# Replace
print(s.replace("Hello", "Hi"))  # "Hi Hi Hi"
print(s.replace("Hello", "Hi", 2))  # "Hi Hi Hello"
```

### Stripping Whitespace

```python
s = "  Hello World  "

print(s.strip())        # "Hello World"
print(s.lstrip())       # "Hello World  "
print(s.rstrip())       # "  Hello World"
print(s.strip(" H"))    # "ello World"
```

### Splitting and Joining

```python
# Split
s = "apple,banana,orange"
print(s.split(","))     # ['apple', 'banana', 'orange']
print(s.split(",", 1))  # ['apple', 'banana,orange']

# Join
words = ["Hello", "World"]
print(" ".join(words))  # "Hello World"
print("-".join(words))  # "Hello-World"
```

---

## 🎨 String Formatting

### Method 1: f-strings (Python 3.6+) – RECOMMENDED

```python
name = "Alice"
age = 30
price = 19.99

# Basic
print(f"Name: {name}, Age: {age}")  # "Name: Alice, Age: 30"

# Formatting numbers
print(f"Price: ${price:.2f}")      # "Price: $19.99"
print(f"Percentage: {age:.1%}")    # "Percentage: 3000.0%"

# Expressions
print(f"Sum: {5 + 3}")             # "Sum: 8"
print(f"Name upper: {name.upper()}") # "Name upper: ALICE"

# Alignment
print(f"{name:>10}")  # Right align: "     Alice"
print(f"{name:<10}")  # Left align: "Alice     "
print(f"{name:^10}")  # Center: "  Alice   "
```

### Method 2: `format()` Method

```python
name = "Alice"
age = 30

# Positional
print("{} is {} years old".format(name, age))

# Indexed
print("{0} is {1} years old".format(name, age))

# Named
print("{name} is {age} years old".format(name=name, age=age))
```

### Method 3: `%` Formatting (Old style)

```python
name = "Alice"
age = 30
pi = 3.14159

print("%s is %d years old" % (name, age))  # "Alice is 30 years old"
print("Pi = %.2f" % pi)  # "Pi = 3.14"
```

---

## 📁 When to Use Strings

| Use Case | Example | Why |
|----------|---------|-----|
| User input/output | `name = input("Enter name: ")` | Natural for text |
| File paths | `path = "/home/user/file.txt"` | File system paths |
| URLs | `url = "https://python.org"` | Web addresses |
| Messages | `error = "File not found"` | Human-readable text |
| Data serialization | `json.dumps(data)` | JSON, XML, CSV |
| Regular expressions | `pattern = r"\d+"` | Pattern matching |
| Database queries | `query = "SELECT * FROM users"` | SQL statements |

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `strings.md` | Complete str guide with all methods |
| `string_methods.md` | All 40+ string methods with examples |
| `string_formatting.md` | f-strings, format(), % formatting |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 🚀 Quick Start

```bash
# Open the detailed guide
cat strings.md

# Or run examples (if .py files)
python strings.py
```

---

## 📚 Next Steps

After understanding string basics:
1. Open `strings.md` for detailed examples
2. Study `string_methods.md` for all methods
3. Master `string_formatting.md` for output formatting
4. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Lists** – Mutable sequences
- **Tuples** – Immutable sequences
- **Regular expressions** – Pattern matching
- **File I/O** – Reading/writing strings to files

---

*Happy Coding! 🐍✨*
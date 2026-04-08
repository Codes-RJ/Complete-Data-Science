# 🔢 NUMERIC TYPES – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Three Numeric Types](#three-numeric-types)
3. [Quick Comparison](#quick-comparison)
4. [Basic Operations](#basic-operations)
5. [Type Conversion](#type-conversion)
6. [When to Use Each](#when-to-use-each)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

Python provides **three numeric types** for mathematical computations:

| Type | Description | Example |
|------|-------------|---------|
| **int** | Whole numbers (unlimited precision) | `42`, `-7`, `0` |
| **float** | Decimal numbers (IEEE 754) | `3.14`, `-0.5`, `2.0` |
| **complex** | Numbers with real & imaginary parts | `3+4j`, `-2j` |

Python is **dynamically typed** - you don't need to declare types:

```python
x = 5        # x is int
x = 3.14     # x is now float
x = 2 + 3j   # x is now complex
```

---

## 🎯 Three Numeric Types

### 1. **int (Integer)**
Whole numbers with unlimited precision.

```python
# Different bases
decimal = 42
binary = 0b101010   # 42 in binary
octal = 0o52        # 42 in octal
hexadecimal = 0x2A  # 42 in hex

# From strings
int("123")        # 123
int("FF", 16)     # 255
```

### 2. **float (Floating-Point)**
Decimal numbers with scientific notation support.

```python
# Standard notation
pi = 3.14159
negative = -0.5

# Scientific notation
small = 1.2e-4    # 0.00012
large = 5.6e6     # 5,600,000

# Special values
inf = float('inf')
nan = float('nan')
```

### 3. **complex (Complex Numbers)**
Numbers with real and imaginary parts (using `j`).

```python
# Creation methods
z1 = 3 + 4j
z2 = complex(3, 4)
z3 = complex("3+4j")

# Access parts
print(z1.real)    # 3.0
print(z1.imag)    # 4.0
print(z1.conjugate())  # (3-4j)
```

---

## 📊 Quick Comparison

| Feature | int | float | complex |
|---------|-----|-------|---------|
| **Example** | `42` | `3.14` | `3+4j` |
| **Mutable?** | No | No | No |
| **Precision** | Unlimited | ~15 digits | ~15 digits each |
| **Common Use** | Counting | Measurements | Engineering |

---

## 🔧 Basic Operations

### Arithmetic (works for all types)

```python
a, b = 10, 3

print(a + b)   # 13 (addition)
print(a - b)   # 7  (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division)
print(a ** b)  # 1000 (power)
```

### Integer-only operations

```python
x = 42

print(x // 3)   # 14 (floor division)
print(x % 3)    # 0  (modulus/remainder)
print(bin(x))   # '0b101010'
print(hex(x))   # '0x2a'
```

### Float operations

```python
y = 3.14159

print(round(y, 2))     # 3.14
print(abs(y))          # 3.14159
print(y.is_integer())  # False
```

### Complex operations

```python
z = 3 + 4j

print(abs(z))      # 5.0 (magnitude)
print(z.real)      # 3.0
print(z.imag)      # 4.0
```

---

## 🔄 Type Conversion

```python
# int to others
float(42)      # 42.0
complex(42)    # (42+0j)

# float to others
int(3.14)      # 3 (truncates)
complex(3.14)  # (3.14+0j)

# complex to others
int(3+4j)      # Error! Use .real
float(3+4j)    # Error! Use .real
int((3+4j).real)   # 3
float((3+4j).real) # 3.0
```

---

## 📁 When to Use Each

| Use Case | Best Type | Why |
|----------|-----------|-----|
| Counting, indexing, IDs | `int` | Exact, fast, unlimited |
| Money (simple) | `float` | Decimal support |
| Money (precise) | `Decimal` (see module) | No precision errors |
| Measurements, percentages | `float` | Natural for decimals |
| AC circuits, quantum physics | `complex` | Built-in complex math |
| Game positions | `float` | Smooth movement |

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `01_integers.py` | Complete int guide with all methods |
| `02_floats.py` | Complete float guide with all methods |
| `03_complex_numbers.py` | Complete complex guide with all methods |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 🚀 Quick Start

```bash
# Run the example files
python 01_integers.py
python 02_floats.py
python 03_complex_numbers.py
```

---

## 📚 Next Steps

After understanding these basics:
1. Open `01_integers.py` for detailed examples
2. Complete the exercises in `exercises.md`
3. Move to `02_text_type/` for strings

---

*Happy Coding! 🐍*
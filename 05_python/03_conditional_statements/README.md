# 🔀 CONDITIONAL STATEMENTS – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Conditionals?](#what-are-conditionals)
3. [Types of Conditionals](#types-of-conditionals)
4. [Quick Reference](#quick-reference)
5. [Comparison Operators](#comparison-operators)
6. [Logical Operators](#logical-operators)
7. [Truthy and Falsy Values](#truthy-and-falsy-values)
8. [When to Use Each](#when-to-use-each)
9. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Conditional statements** allow your program to make decisions and execute different code blocks based on whether conditions are `True` or `False`.

```python
# Basic conditional
age = 18
if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")
```

**Key Characteristics:**
- ✅ Conditions evaluate to `True` or `False`
- ✅ Code blocks are indented (4 spaces)
- ✅ `elif` = else if (multiple conditions)
- ✅ `else` catches all remaining cases
- ✅ Can be nested for complex logic

---

## 📖 What are Conditionals?

Conditionals are the decision-makers in Python. They control which code runs based on conditions.

```python
temperature = 30

if temperature > 25:
    print("It's hot outside")
elif temperature > 15:
    print("It's warm outside")
elif temperature > 5:
    print("It's cool outside")
else:
    print("It's cold outside")
```

**Why Conditionals Matter:**
- Make programs intelligent and responsive
- Handle different scenarios and edge cases
- Control program flow based on user input
- Validate data before processing
- Implement business logic and rules

---

## 📚 Types of Conditionals

| Type | Syntax | Use Case |
|------|--------|----------|
| `if` | `if condition:` | Single condition check |
| `if-else` | `if condition: else:` | Two-way decision |
| `if-elif-else` | `if: elif: else:` | Multiple conditions |
| Nested | `if: if: else:` | Complex logic |
| Ternary | `x if cond else y` | One-line conditional |
| Match-case | `match value: case:` | Pattern matching (3.10+) |

```python
# if
if x > 0:
    print("Positive")

# if-else
if x > 0:
    print("Positive")
else:
    print("Non-positive")

# if-elif-else
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Ternary
result = "Positive" if x > 0 else "Non-positive"
```

---

## 📊 Quick Reference

### Syntax

```python
# Basic if
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

# Ternary
value = true_value if condition else false_value
```

### Indentation Rules

```python
# ✅ Correct - 4 spaces
if x > 5:
    print("x is greater than 5")
    print("This is also inside if")

# ❌ Wrong - No indentation
if x > 5:
print("This will cause IndentationError")

# ❌ Wrong - Inconsistent indentation
if x > 5:
    print("4 spaces")
   print("3 spaces")  # Error!
```

---

## 📐 Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 3` | `False` |

```python
x = 10
y = 20

print(f"x == y: {x == y}")  # False
print(f"x != y: {x != y}")  # True
print(f"x > y: {x > y}")    # False
print(f"x < y: {x < y}")    # True
print(f"x >= 10: {x >= 10}") # True
print(f"x <= 5: {x <= 5}")   # False

# Chained comparisons
if 0 < x < 10:
    print("x is between 0 and 10")
```

---

## 🔗 Logical Operators

| Operator | Meaning | Truth Table |
|----------|---------|-------------|
| `and` | Both must be True | `True and True = True`, else `False` |
| `or` | At least one True | `False or False = False`, else `True` |
| `not` | Negation | `not True = False`, `not False = True` |

```python
age = 25
has_license = True

# and - both must be True
if age >= 18 and has_license:
    print("Can drive")

# or - at least one must be True
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("Stay home")

# not - negation
is_raining = False
if not is_raining:
    print("Go outside")

# Precedence: not > and > or
result = True or False and not False  # True
```

---

## 🔍 Truthy and Falsy Values

### Falsy Values (Evaluate to False)

```python
falsy_values = [
    None,      # None
    False,     # Boolean False
    0,         # Zero integer
    0.0,       # Zero float
    0j,        # Zero complex
    "",        # Empty string
    [],        # Empty list
    (),        # Empty tuple
    {},        # Empty dict
    set()      # Empty set
]

for val in falsy_values:
    print(f"{repr(val):10} -> {bool(val)}")
```

### Truthy Values (Evaluate to True)

```python
truthy_values = [
    True,
    1,
    -1,
    3.14,
    "hello",
    " ",
    "False",
    [1, 2],
    (1, 2),
    {"a": 1},
    {1, 2}
]

for val in truthy_values:
    print(f"{repr(val):10} -> {bool(val)}")
```

### Using Truthy/Falsy in Conditions

```python
# ✅ Pythonic - Direct truthy check
name = "Alice"
if name:
    print(f"Hello, {name}")

# ❌ Unnecessary comparison
if name != "":
    print(f"Hello, {name}")

# Check if list is empty
items = []
if not items:
    print("No items")

# Default value using or
name = user_input or "Guest"
```

---

## 📁 When to Use Each

| Use Case | Best Conditional | Why |
|----------|------------------|-----|
| Single condition | `if` | Simple check |
| Two possibilities | `if-else` | Clear branching |
| Multiple mutually exclusive | `if-elif-else` | Only one executes |
| Complex nested logic | Nested `if` | Dependent conditions |
| Simple assignment | Ternary | One-line readability |
| Pattern matching (3.10+) | `match-case` | Multiple value checks |

### Examples

```python
# Single condition
if is_ready:
    process()

# Two possibilities
if is_valid:
    save()
else:
    show_error()

# Multiple conditions
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Nested conditionals
if user.is_authenticated:
    if user.has_permission:
        grant_access()
    else:
        deny_access()
else:
    redirect_to_login()

# Ternary operator
status = "Active" if is_active else "Inactive"
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `01_if_statement.md` | Complete if, if-else, if-elif-else guide |
| `02_nested_conditionals.md` | Conditionals inside conditionals |
| `03_ternary_operator.md` | Conditional expressions (`x if cond else y`) |
| `04_match_case.md` | Pattern matching (Python 3.10+) |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 💡 Quick Tips

```python
# ✅ DO: Use direct boolean checks
if is_valid:
    process()

# ❌ DON'T: Compare to True/False unnecessarily
if is_valid == True:  # Redundant
    process()

# ✅ DO: Use parentheses for complex conditions
if (age >= 18 and has_license) or (age >= 21 and has_permit):
    can_drive = True

# ✅ DO: Use chained comparisons
if 0 < x < 10:
    print("x between 0 and 10")

# ❌ DON'T: Use = instead of ==
if x = 10:  # SyntaxError! Use == for comparison
    pass
```

---

## 📚 Next Steps

After understanding conditional basics:
1. Open `01_if_statement.md` for detailed if/elif/else guide
2. Open `02_nested_conditionals.md` for nested conditions
3. Open `03_ternary_operator.md` for one-liners
4. Open `04_match_case.md` for pattern matching (3.10+)
5. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Boolean Values** – True/False conditions
- **Comparison Operators** – `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators** – `and`, `or`, `not`
- **Truthy/Falsy** – All values have boolean equivalents
- **Loops** – While loops also use conditions

## Next Step

- Go to [01_if_statement.md](01_if_statement.md) for understanding more about if-elif-else statements.

---

*Master conditionals to make your programs smart and decision-making! 🐍✨*
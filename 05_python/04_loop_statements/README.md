# 🔄 LOOPS – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Loops?](#what-are-loops)
3. [Types of Loops](#types-of-loops)
4. [Quick Reference](#quick-reference)
5. [Loop Control Statements](#loop-control-statements)
6. [When to Use Each](#when-to-use-each)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Loops** allow you to execute a block of code repeatedly. They are essential for automating repetitive tasks and processing collections of data.

```python
# for loop - iterate over a sequence
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# while loop - iterate while condition is true
count = 0
while count < 5:
    print(count)
    count += 1
```

**Key Characteristics:**
- ✅ Automate repetitive tasks
- ✅ Process collections of data
- ✅ Reduce code duplication
- ✅ Two types: `for` and `while`
- ✅ Can be nested for complex iterations
- ✅ Control statements: `break`, `continue`, `else`

---

## 📖 What are Loops?

Loops are control flow statements that repeat a block of code multiple times.

```python
# Without loop (bad - repetitive)
print(1)
print(2)
print(3)
print(4)
print(5)

# With loop (good - efficient)
for i in range(1, 6):
    print(i)
```

**Why Loops Matter:**
- Process hundreds or thousands of items with few lines of code
- Handle user input until valid
- Implement algorithms that require repetition
- Traverse data structures (lists, dictionaries, etc.)
- Create patterns and shapes

---

## 📚 Types of Loops

| Type | Syntax | Use Case |
|------|--------|----------|
| `for` loop | `for item in iterable:` | Iterate over sequences (list, tuple, string, range) |
| `while` loop | `while condition:` | Loop until condition becomes False |
| Nested loops | Loops inside loops | Work with multi-dimensional data |

```python
# for loop - best for known number of iterations
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for loop with range
for i in range(5):
    print(i)

# while loop - best for unknown number of iterations
count = 0
while count < 5:
    print(count)
    count += 1

# while loop with user input
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
```

---

## 📊 Quick Reference

### For Loop Syntax

```python
# Iterate over range
for i in range(stop):
for i in range(start, stop):
for i in range(start, stop, step):

# Iterate over sequence
for item in list:
for item in tuple:
for char in string:
for key in dict:
for value in dict.values():
for key, value in dict.items():

# With index
for i, item in enumerate(list):

# Multiple sequences
for a, b in zip(list1, list2):
```

### While Loop Syntax

```python
while condition:
    # code block
    # update condition

# Infinite loop (use with break)
while True:
    # code
    if condition:
        break
```

### Loop Control Statements

| Statement | Purpose |
|-----------|---------|
| `break` | Exit loop completely |
| `continue` | Skip to next iteration |
| `else` | Execute if loop completes without break |

```python
# break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0,1,2,3,4

# continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0,1,3,4

# else - runs if no break
for i in range(5):
    print(i)
else:
    print("Loop completed")  # Runs
```

---

## 📁 When to Use Each

| Use Case | Best Loop | Why |
|----------|-----------|-----|
| Iterate over list/tuple | `for` | Direct iteration over items |
| Loop fixed number of times | `for` with `range()` | Simple and clear |
| Loop through dictionary | `for` | Iterate keys, values, or items |
| Unknown number of iterations | `while` | Condition-based looping |
| User input validation | `while` | Loop until valid input |
| Game loop | `while` | Runs until game over |
| Infinite loop with exit condition | `while True` with `break` | Flexible exit point |

### Examples

```python
# for loop - iterate over list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# for loop - fixed number of times
for i in range(5):
    print(f"Iteration {i}")

# while loop - user input validation
password = ""
while password != "secret":
    password = input("Enter password: ")

# while loop - game loop
game_running = True
while game_running:
    # game logic
    if game_over:
        game_running = False

# while True with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `01_for_loop.md` | Complete for loop guide |
| `02_while_loop.md` | Complete while loop guide |
| `03_loop_control.md` | break, continue, else statements |
| `04_nested_loops.md` | Loops inside loops |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 💡 Quick Tips

```python
# ✅ DO: Use for loop for sequences
for item in my_list:
    process(item)

# ❌ DON'T: Use while loop for sequences
i = 0
while i < len(my_list):  # More verbose, error-prone
    process(my_list[i])
    i += 1

# ✅ DO: Use enumerate() for index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# ❌ DON'T: Use range(len()) for index
for i in range(len(my_list)):
    print(f"{i}: {my_list[i]}")

# ✅ DO: Use break to exit early
for item in my_list:
    if item == target:
        print("Found!")
        break

# ✅ DO: Use continue to skip
for item in my_list:
    if not is_valid(item):
        continue
    process(item)
```

---

## 📚 Next Steps

After understanding loop basics:
1. Open `01_for_loop.md` for detailed for loop guide
2. Open `02_while_loop.md` for while loop guide
3. Open `03_loop_control.md` for break, continue, else
4. Open `04_nested_loops.md` for nested loops
5. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Conditionals** – if statements inside loops
- **Lists** – Iterating over collections
- **Range** – Generating number sequences
- **Break/Continue** – Loop control
- **List Comprehensions** – Concise loop syntax

---

*Master loops to automate repetitive tasks efficiently! 🐍✨*

---

## Next Step

- Move to [01_for_loop.md](01_for_loop.md) to understand the for loop in depth and learn how to iterate over sequences like lists, strings, and ranges.
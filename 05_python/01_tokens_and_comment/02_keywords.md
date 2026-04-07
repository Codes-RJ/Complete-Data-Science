# Keywords in Python 📦

## What are Keywords?

They are pre-defined words with special meaning to the language compiler or interpreter. Think of it as reserved words that serve a special purpose and must not be used as normal keywords

## Python Keywords (Reserved Words)

| | | Keywords | | |
|---|---|---|---|---|
| if | elif | else | for | while |
| pass | break | continue | def | return |
| try | except | finally | raise | assert |
| and | or | not | in | not in |
| is | is not | True | False | None |
| class | del | yield | global | nonlocal |
| import | from | as | lambda | with |
| async | await | | | |

## Use of different Keywords

| Keywords | Description |
|---|---|
| if | Conditional statement to test a condition |
| elif | Checks multiple conditions after *if* |
| else | Executes if all previous conditions are *False* |
| for | Loop used for iterating over a sequence |
| while | Loop that runs if a condition is *True* |
| break | Terminates the loop immediately |
| continue | Skips to next iteration of loop |
| pass | Does nothing |
| def | Define a function |
| return | Returns value from a function |
| yield | Returns a generator value |
| try | Starts exception handling block |
| except | Catches exceptions |
| finally | Executes no matter what in exception handling |
| raise | Raises an exception manually |
| assert | Tests a condition and return error if *False* |
| and | Logical *AND* operator |
| or | Logical *OR* operator |
| not | Logical *NOT* operator |
| in | Checks membership |
| not in | Checks non-membership |
| is | Checks identity (same object) |
| is not | Checks different identity |
| True | Boolean *True* value |
| False | Boolean *False* value |
| None | No value present |
| class | Define a class |
| del | Delete an object/reference |
| global | Declares global variable |
| nonlocal | Declares non-local variables |
| import | Import a *module* |
| from | Imports specific parts from module |
| as | Gives alias to module |
| lambda | Creates anonymous function |
| with | Resource management |
| async | Declare asynchronous function |
| await | Waits for async result |

---

## CODE for use of different Keywords

### Conditional Statements
```python
n = int(input("Enter a integer : "))
if n%2 == 0:
    print("Divisible by 2")
elif n%3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")
```

### Loops
```python
for i in range (3):
    print(f"Number {i}")
```
and
```python
while True:
    print("Hello")        \ infinite loop
```

---

## Next Steps

- Proceed to [03_operators](./03_operators.md.md) to explore operators and its operations in depth
- Practice applying operations to the variables

---
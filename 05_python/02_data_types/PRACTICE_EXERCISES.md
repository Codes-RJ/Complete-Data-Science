# Practice Exercises — Data Types 🧠

---

## A. Identify the Type (and the Output)

For each value, write:
1) the output of `type(value)`  
2) what `print(value)` shows

1. `42`
2. `3.14`
3. `2 + 5j`
4. `"hello"`
5. `["a", "b", "c"]`
6. `("x", 1, True)`
7. `range(5)`
8. `{"a", "b"}`
9. `{"name": "Ava", "age": 20}`
10. `None`
11. `b"ABC"`
12. `bytearray(b"ABC")`
13. `{"x": 1, "y": 2}.keys()`
14. `{"x": 1, "y": 2}.items()`

---

## B. Predict the Output

### 1) Strings vs numbers

```python
print("5" + "3")
print(5 + 3)
print("5" * 3)
```

### 2) Truthiness

```python
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool("0"))
print(bool([0]))
```

### 3) Identity vs equality

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a is c)
```

---

## C. Conversions (Safe vs Unsafe)

1. Convert `"123"` to `int`.
2. Convert `"123.45"` to `float`.
3. Convert `123.45` to `int` and observe (round vs truncate).
4. Convert `"True"` to `bool` and compare with `bool(True)`.
5. Convert `[1, 2, 2, 3]` to a `set`.
6. Convert `{"a": 1, "b": 2}` to:
   - `list(d)`
   - `list(d.items())`

---

## D. Mini Programs (Data Types in Action)

1. **Square calculator**
   - Input: a number (string from `input()`)
   - Output: square of the number
   - Handle invalid input using `try/except`

2. **Sentence stats**
   - Input: a sentence
   - Output:
     - number of characters
     - number of words
     - sentence in `title()` case

3. **Unique counter**
   - Start with a list of integers
   - Output:
     - unique values (as a set)
     - count of unique values

---

## E. Challenge (Mix Everything)

Create a program that stores student data in a `dict` where each student has:
- `name` (str)
- `age` (int)
- `marks` (list of floats)

Then:
- compute average marks for each student
- print the top student by average


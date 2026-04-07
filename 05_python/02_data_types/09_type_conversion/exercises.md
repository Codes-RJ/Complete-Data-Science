# Exercises — Type Conversion 📝

---

## A. Explicit conversion

1. Convert `"123"` to `int`.
2. Convert `"123.45"` to `float`.
3. Convert `123.45` to `int` and observe the result.
4. Convert `-123.45` to `int` and observe the result.
5. Convert `"hello"` to a list of characters.
6. Convert `[1, 2, 2, 3]` to a set.

---

## B. Implicit conversion

1. What is the type of `5 + 2.0`?
2. What is the output of:
   - `5 / 2`
   - `5 // 2`
3. What is the output of `True + True + False`?

---

## C. Error spotting

For each line, say if it works or gives an error. If error, fix it.

1. `"5" + 3`
2. `int("12.3")`
3. `float("abc")`
4. `list(123)`

---

## Challenge ⭐

Write a program that:
- reads two inputs (strings) from the user
- tries to convert both to `int`
- if that fails, tries to convert both to `float`
- if that fails, prints `"Invalid numbers"`
- otherwise prints sum and average


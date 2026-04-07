# Exercises — Sequence Types 📝

---

## A. Lists

1. Create a list of 5 numbers. Print:
   - first element
   - last element
   - slice of middle 3 elements
2. Start with `nums = [1, 2, 3]` then:
   - `append(4)`
   - `insert(0, 0)`
   - `extend([5, 6])`
   Print the list after each step.
3. Remove all occurrences of `2` from `[1, 2, 2, 3, 2, 4]` (try two ways).
4. Sort `["banana", "apple", "cherry"]` in:
   - ascending order
   - descending order

---

## B. Tuples

1. Create a tuple with one element (correct syntax).
2. Unpack `(10, 20)` into `x` and `y`.
3. Use `a, *rest = (1, 2, 3, 4, 5)` and print both.
4. Create a dictionary that uses tuples as keys:
   - key: `(row, col)`
   - value: a string name

---

## C. Ranges

1. Print `list(range(10))`.
2. Print the odd numbers from 1 to 19 using `range`.
3. For `r = range(0, 20, 2)`:
   - check if `10` is in `r`
   - check if `11` is in `r`
   - print `r[3]` and `r[-1]`

---

## Challenge ⭐

Write a program that:
- takes a list of integers
- creates a new list of only the even numbers
- prints both lists

Example:
```
input  = [1, 2, 3, 4, 5, 6]
output = [2, 4, 6]
```


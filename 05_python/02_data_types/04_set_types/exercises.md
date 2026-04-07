# Exercises — Set Types 📝

---

## A. Basics

1. Create a set from `[1, 2, 2, 3, 3, 3]` and print it.
2. What is the difference between `{}` and `set()`?
3. Given `s = {1, 2, 3}`, do:
   - add `4`
   - remove `2`
   - discard `100` (no error)

---

## B. Set Operations

Let:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

Compute:
1. `A | B`
2. `A & B`
3. `A - B`
4. `B - A`
5. `A ^ B`

---

## C. Subset / Superset

1. Check if `{1, 2}` is a subset of `{1, 2, 3, 4}`.
2. Check if `{1, 2, 3, 4}` is a superset of `{2, 4}`.
3. What is the difference between `<=` and `<` for sets?

---

## D. Frozenset

1. Create a `frozenset` from `{1, 2, 2, 3}`.
2. Try calling `add()` on a `frozenset`. What error do you get?
3. Use a `frozenset` as a dictionary key.

---

## Challenge ⭐

Write a program that:
- takes two lists of integers
- converts them to sets
- prints:
  - common elements (intersection)
  - all unique elements (union)
  - elements only in first list (difference)


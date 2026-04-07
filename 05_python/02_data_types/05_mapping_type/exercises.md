# Exercises — Mapping Type (`dict`) 📝

---

## A. Basics

1. Create a dictionary for a student:
   - name
   - age
   - marks (list of 3 numbers)
2. Print the student name using:
   - `student["name"]`
   - `student.get("name")`
3. Try accessing a missing key with `[]` and with `.get()` and observe the difference.

---

## B. Update and delete

Given:

```python
d = {"a": 1, "b": 2}
```

1. Add `"c": 3`
2. Update `"b"` to `200`
3. Remove `"a"` using `pop()`
4. Clear the dictionary

---

## C. Looping

Given:

```python
d = {"x": 10, "y": 20, "z": 30}
```

1. Print all keys
2. Print all values
3. Print all key-value pairs like: `x -> 10`

---

## D. Frequency counter

Write a program that counts character frequency in a string.

Example:
```
input  = "banana"
output = {'b': 1, 'a': 3, 'n': 2}
```

---

## Challenge ⭐

Create a dictionary of 5 students where:
- key = roll number (int)
- value = name (str)

Then:
- print all roll numbers
- search a roll number and print the name (handle if not found)


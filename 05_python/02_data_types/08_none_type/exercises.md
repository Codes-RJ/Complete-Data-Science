# Exercises — None Type (`None`) 📝

---

## A. Basics

1. Create a variable `x = None` and print `type(x)`.
2. Check:
   - `x is None`
   - `x == None`
   Which is recommended and why?

---

## B. Predict the Output

```python
x = None
print(bool(x))

if x:
    print("truthy")
else:
    print("falsy")
```

---

## C. Functions returning None

1. Write a function `print_name(name)` that prints the name but does not return anything.
2. Store its result in a variable and print that variable.

---

## Challenge ⭐

Write a function `safe_divide(a, b)` that:
- returns `a / b` if `b != 0`
- otherwise returns `None`

Then write code that calls it and prints:
- the result if it is not None
- otherwise prints `"Cannot divide by zero"`


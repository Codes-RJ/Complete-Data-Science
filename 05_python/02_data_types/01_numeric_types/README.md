# Numeric Types 🔢

---

## What You’ll Learn

Python provides 3 main numeric types:

- **`int`** → whole numbers (unlimited precision)
- **`float`** → decimal numbers (IEEE-754 double precision)
- **`complex`** → complex numbers \(a + bj\)

---

## Key Ideas

### 1) `int` has unlimited precision

```python
print(2**100)
```

### 2) Floats can have precision issues

```python
print(0.1 + 0.2)          # 0.30000000000000004
print((0.1 + 0.2) == 0.3) # False
```

### 3) Complex numbers are built-in

```python
z = 2 + 3j
print(z.real)  # 2.0
print(z.imag)  # 3.0
```

---

## Files in This Folder 📁

| File | Focus |
|------|-------|
| `01_integers.py` | int basics, bases, bitwise, helpers |
| `02_floats.py` | float precision, rounding, formatting, Decimal |
| `03_complex_numbers.py` | complex parts, operations, cmath |
| `exercises.md` | practice questions |

---

## How to Run

```bash
python 01_integers.py
python 02_floats.py
python 03_complex_numbers.py
```

---

## Learning Outcome 🎯

After this module, you can:
- choose the correct numeric type
- predict numeric operations’ results
- handle float precision safely (tolerance/Decimal)
- work with complex numbers and their properties

---


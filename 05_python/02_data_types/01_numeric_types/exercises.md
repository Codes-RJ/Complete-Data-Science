# Exercises — Numeric Types 📝

---

## A. Integers (`int`)

1. Compute and print:
   - `17 // 3`
   - `17 % 3`
   - `3 ** 5`
2. Ask the user for an integer and print whether it is even or odd.
3. Print the last digit of an integer (example: `1234 → 4`).
4. Convert `255` to:
   - binary using `bin(255)`
   - hex using `hex(255)`
5. Evaluate and explain:
   - `-7 // 3`
   - `-7 % 3`

---

## B. Floats (`float`)

1. Show that `0.1 + 0.2` is not exactly `0.3`.
2. Use `math.isclose()` to compare `0.1 + 0.2` and `0.3`.
3. Ask the user for a float and print it rounded to:
   - 2 decimal places
   - 4 decimal places
4. Convert a Celsius temperature to Fahrenheit:
   \[
   F = C \times \frac{9}{5} + 32
   \]
5. Format `12345.6789` as:
   - `12345.68`
   - `12,345.68`
   - scientific notation (3 digits)

---

## C. Complex Numbers (`complex`)

1. Create `z1 = 2 + 3j` and `z2 = 1 - 4j`, then print:
   - `z1 + z2`
   - `z1 * z2`
   - `z1 / z2`
2. Print:
   - `z1.real`
   - `z1.imag`
   - `z1.conjugate()`
3. Print the magnitude of `3 + 4j` (should be `5.0`).
4. Use `cmath` to compute:
   - `cmath.sqrt(-1)`
   - `cmath.exp(1j * cmath.pi)` (Euler’s identity)

---

## Challenge ⭐

Write a program that:
- asks the user for **two numbers**
- if both look like integers, treat them as `int`
- otherwise treat them as `float`
- print sum, difference, product

Hint: use `str.isdigit()` carefully (consider negative numbers too).



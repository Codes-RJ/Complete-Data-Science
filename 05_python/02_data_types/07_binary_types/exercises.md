# Exercises — Binary Types 📝

---

## A. Bytes

1. Create `b = b"ABC"` and print:
   - `b[0]`
   - `b[1:3]`
2. Convert `"hello"` to bytes using UTF-8:
   - `"hello".encode("utf-8")`
3. Convert back to string using `.decode("utf-8")`.
4. Try changing a byte inside a `bytes` object. What error occurs?

---

## B. Bytearray

1. Create `ba = bytearray(b"HELLO")` and change the first letter to lowercase.
2. Append the ASCII code of `'!'` and print the final bytearray.
3. Decode the bytearray to text (if it contains valid text).

---

## C. Memoryview

1. Create a `memoryview` from a `bytearray`.
2. Slice the first 3 bytes using the memoryview.
3. Modify the slice and show that the original `bytearray` changed.

---

## Challenge ⭐

Write a program that:
- takes a string input
- encodes it into bytes (UTF-8)
- prints the bytes and their length
- decodes back and prints the original string


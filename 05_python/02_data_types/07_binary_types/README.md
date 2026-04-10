# 📦 BINARY TYPES – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Three Binary Types](#three-binary-types)
3. [Quick Comparison](#quick-comparison)
4. [Common Operations](#common-operations)
5. [When to Use Each](#when-to-use-each)
6. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Binary types** are used for handling raw binary data, such as files, network communications, and low-level data manipulation.

| Type | Description | Example | Mutability |
|------|-------------|---------|------------|
| **bytes** | Immutable sequence of bytes | `b'hello'` | ❌ Immutable |
| **bytearray** | Mutable sequence of bytes | `bytearray(b'hello')` | ✅ Mutable |
| **memoryview** | View of bytes without copying | `memoryview(b'hello')` | Depends on source |

```python
# Examples of binary types
bytes_data = b'hello'                    # bytes literal
byte_array = bytearray([65, 66, 67])     # bytearray from list
mem_view = memoryview(b'world')          # memoryview of bytes

# Display
print(bytes_data)      # b'hello'
print(byte_array)      # bytearray(b'ABC')
print(mem_view[0])     # 119 (ASCII 'w')
```

**Key Characteristics:**
- ✅ Used for binary data (images, files, network packets)
- ✅ Each element is an integer (0-255)
- ✅ Support indexing and slicing
- ✅ Efficient for I/O operations
- ✅ Can be converted to/from strings via encoding

---

## 📦 Three Binary Types

### 1. **bytes** – Immutable Bytes

Bytes are **immutable** sequences of bytes (0-255). They are created using the `b` prefix or `bytes()` constructor.

```python
# Creating bytes
b1 = b'hello'                    # Bytes literal
b2 = b"world"                    # Double quotes work too
b3 = b'\x48\x65\x6c\x6c\x6f'    # Hex escape: b'Hello'
b4 = bytes([65, 66, 67])         # From list: b'ABC'
b5 = bytes(5)                    # Zero-filled: b'\x00\x00\x00\x00\x00'
b6 = b''                         # Empty bytes

# Can contain any byte value (0-255)
data = b'\x00\x01\x02\xff'       # Hex values
print(data)                      # b'\x00\x01\x02\xff'
```

### 2. **bytearray** – Mutable Bytes

Bytearray is a **mutable** version of bytes. You can modify individual bytes.

```python
# Creating bytearray
ba1 = bytearray(b'hello')        # From bytes
ba2 = bytearray([65, 66, 67])    # From list: bytearray(b'ABC')
ba3 = bytearray(5)               # Zero-filled: bytearray(b'\x00\x00\x00\x00\x00')
ba4 = bytearray()                # Empty bytearray

# Modifying (unlike bytes)
ba = bytearray(b'hello')
ba[0] = 72                       # Change 'h' (104) to 'H' (72)
print(ba)                        # bytearray(b'Hello')
ba.append(33)                    # Add exclamation mark
print(ba)                        # bytearray(b'Hello!')
```

### 3. **memoryview** – Zero-Copy View

Memoryview provides a **view** of bytes without copying the data.

```python
# Creating memoryview
data = bytearray(b'hello world')
view = memoryview(data)

# Access elements
print(view[0])       # 104 ('h')
print(view[6])       # 119 ('w')

# Modify through view (if source is mutable)
view[0] = 72         # Change to 'H'
print(data)          # bytearray(b'Hello world')

# Slicing creates new view (no copy)
slice_view = view[6:11]
print(bytes(slice_view))  # b'world'

# Different formats (for numerical data)
import array
arr = array.array('i', [1, 2, 3, 4])  # array of integers
mem = memoryview(arr)
print(mem[0])        # 1
```

---

## 📊 Quick Comparison

| Feature | bytes | bytearray | memoryview |
|---------|-------|-----------|------------|
| **Syntax** | `b'hello'` | `bytearray(b'hello')` | `memoryview(data)` |
| **Mutable?** | ❌ No | ✅ Yes | Depends on source |
| **Index type** | Integer (0-255) | Integer (0-255) | Integer |
| **Slicing** | Returns `bytes` | Returns `bytearray` | Returns `memoryview` |
| **Memory** | Fixed | Dynamic | Zero-copy view |
| **Hashable?** | ✅ Yes | ❌ No | ❌ No |
| **Use as dict key?** | ✅ Yes | ❌ No | ❌ No |
| **Literal syntax** | `b'...'` | No | No |

### Memory Comparison

```python
import sys

data = b'hello world' * 1000
bytes_obj = data
bytearray_obj = bytearray(data)
view = memoryview(data)

print(f"bytes:      {sys.getsizeof(bytes_obj)} bytes")
print(f"bytearray:  {sys.getsizeof(bytearray_obj)} bytes")
print(f"memoryview: {sys.getsizeof(view)} bytes (view only)")

# Typical output:
# bytes:      12043 bytes
# bytearray:  12043 bytes
# memoryview: 64 bytes (just the view, not the data!)
```

---

## 🔧 Common Operations

### Operations That Work on All Binary Types

```python
data = b'hello world'

# Length
print(len(data))           # 11

# Indexing (returns int 0-255)
print(data[0])             # 104 ('h')
print(data[-1])            # 100 ('d')

# Slicing
print(data[0:5])           # b'hello'
print(data[6:])            # b'world'
print(data[::-1])          # b'dlrow olleh'

# Membership
print(b'h' in data)        # True
print(b'x' in data)        # False

# Concatenation
print(b'hello' + b' world')    # b'hello world'

# Repetition
print(b'ha' * 3)           # b'hahaha'

# Iteration
for byte in b'ABC':
    print(byte)            # 65, 66, 67

# Comparison
print(b'hello' == b'hello')   # True
print(b'hello' < b'world')    # True (lexicographic)
```

### Bytes-Specific (Immutable)

```python
# Creating from strings (encoding)
text = "Hello"
utf8_bytes = text.encode('utf-8')
print(utf8_bytes)          # b'Hello \xe4\xb8\x96\xe7\x95\x8c'

# Back to string
decoded = utf8_bytes.decode('utf-8')
print(decoded)

# Hex representation
print(b'hello'.hex())      # '68656c6c6f'
print(bytes.fromhex('68656c6c6f'))  # b'hello'
```

### Bytearray-Specific (Mutable)

```python
ba = bytearray(b'hello')

# Adding elements
ba.append(33)              # Add '!'
print(ba)                  # bytearray(b'hello!')
ba.extend(b' world')       # Add multiple
print(ba)                  # bytearray(b'hello! world')

# Inserting
ba.insert(5, 32)           # Insert space at position 5
print(ba)                  # bytearray(b'hello world')

# Removing
ba.pop()                   # Remove last byte
ba.remove(32)              # Remove first space
ba.clear()                 # Remove all

# Modifying slices
ba = bytearray(b'hello world')
ba[6:11] = b'python'       # Replace 'world' with 'python'
print(ba)                  # bytearray(b'hello python')
```

### Memoryview-Specific (Zero-Copy)

```python
# Slicing doesn't copy data
data = bytearray(b'hello world')
view = memoryview(data)
slice_view = view[6:11]    # No copy!
slice_view[0] = 80         # Modifies original
print(data)                # bytearray(b'hello Porld')

# Cast to different formats (for numerical data)
import array
arr = array.array('i', [1, 2, 3, 4])
mem = memoryview(arr)
mem = mem.cast('B')        # Cast to bytes
print(mem.tolist())        # [1, 0, 0, 0, 2, 0, 0, 0, ...]

# Working with large data efficiently
large_data = bytearray(1000000)
view = memoryview(large_data)
# Modify without copying
for i in range(0, len(view), 1000):
    view[i:i+1000] = b'\xff' * 1000
```

---

## 📁 When to Use Each

| Use Case | Best Type | Why |
|----------|-----------|-----|
| **Reading files** | `bytes` | Immutable, hashable for caching |
| **Writing/modifying files** | `bytearray` | Mutable, can modify in-place |
| **Network buffers** | `memoryview` | Zero-copy, efficient |
| **String encoding** | `bytes` | encode()/decode() methods |
| **Binary protocols** | `bytearray` | Easy to build/modify |
| **Large data processing** | `memoryview` | No copying overhead |
| **Dictionary keys** | `bytes` | Hashable |
| **Image processing** | `memoryview` | Efficient slicing |
| **Cryptography** | `bytes` | Immutable, secure |

### Real-World Examples

```python
# Reading binary file
with open('image.jpg', 'rb') as f:
    data = f.read()          # Returns bytes
    print(f"File size: {len(data)} bytes")

# Modifying data in place
with open('file.bin', 'r+b') as f:
    data = bytearray(f.read())
    # Modify bytes
    data[0] = 0xFF
    f.seek(0)
    f.write(data)

# Network packet processing (zero-copy)
packet = bytearray(1024)
view = memoryview(packet)
# Parse header without copying
header = view[0:20]
if header[0] == 0x45:  # IP version check
    print("IPv4 packet detected")

# String to bytes (encoding)
text = "Hello"
utf8 = text.encode('utf-8')
print(utf8)  # b'Hello \xe4\xb8\x96\xe7\x95\x8c'

# Bytes to string (decoding)
decoded = utf8.decode('utf-8')
print(decoded)

# Working with hex
hex_string = "48656c6c6f"
bytes_data = bytes.fromhex(hex_string)
print(bytes_data)          # b'Hello'
print(bytes_data.hex())    # '48656c6c6f'
```

---

## 🔄 Conversion Between Types

```python
# bytes ↔ bytearray
b = b'hello'
ba = bytearray(b)          # bytes → bytearray
b2 = bytes(ba)             # bytearray → bytes

# bytes ↔ memoryview
b = b'hello'
view = memoryview(b)       # bytes → memoryview
b2 = bytes(view)           # memoryview → bytes

# bytearray ↔ memoryview
ba = bytearray(b'hello')
view = memoryview(ba)      # bytearray → memoryview
ba2 = bytearray(view)      # memoryview → bytearray

# String ↔ bytes (encoding/decoding)
text = "Hello"
bytes_data = text.encode('utf-8')     # str → bytes
text2 = bytes_data.decode('utf-8')    # bytes → str

# List ↔ bytes
byte_list = [65, 66, 67]
bytes_data = bytes(byte_list)         # list → bytes
list_back = list(bytes_data)          # bytes → list
```

---

## 💡 Quick Tips

```python
# Create bytes efficiently
b = b'hello'                         # Use literal when possible
b = bytes([65, 66, 67])             # From list of ints
b = bytes(range(256))               # All byte values

# Create bytearray efficiently
ba = bytearray(1000)                # Pre-allocate size
ba.extend(b'\x00' * 1000)           # Extend with zeros

# Use memoryview for large data
with open('large_file.bin', 'rb') as f:
    data = f.read()
    view = memoryview(data)
    # Process without copying
    header = view[0:100]

# Encode/decode with error handling
bytes_data = text.encode('ascii', errors='ignore')  # Skip non-ascii
bytes_data = text.encode('ascii', errors='replace') # Replace with '?'
text = bytes_data.decode('ascii', errors='ignore')

# Check if object is binary type
def is_binary(obj):
    return isinstance(obj, (bytes, bytearray, memoryview))

print(is_binary(b'hello'))      # True
print(is_binary('hello'))       # False
```

---

## 📚 Next Steps

- Go to [01_bytes.md](01_bytes.md) for detailed bytes guide

---

## 🔗 Related Topics

- **Strings** – Text data with encoding
- **File I/O** – Reading/writing binary files
- **Struct module** – Packing/unpacking binary data
- **Array module** – Homogeneous numeric arrays
- **Socket programming** – Network communication

---

*Master binary types for efficient data processing and I/O operations! 🐍✨*
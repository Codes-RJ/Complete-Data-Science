# 📘 BYTEARRAY – COMPLETE GUIDE

## 📌 Table of Contents
1. What is Bytearray?
2. Creating Bytearray
3. Bytearray Methods
4. Bytearray Operations
5. Modifying Bytearray
6. Real-World Examples
7. Common Pitfalls
8. Performance Tips
9. Practice Exercises

---

## What is Bytearray?

**Bytearray** is a mutable sequence of integers in the range 0-255. Unlike bytes (immutable), bytearray can be modified in-place.

```python
# Examples of bytearray
ba1 = bytearray(b'hello')           # From bytes
ba2 = bytearray([65, 66, 67])       # From list: bytearray(b'ABC')
ba3 = bytearray(10)                 # Zero-filled: bytearray(b'\x00' * 10)
ba4 = bytearray()                   # Empty bytearray

print(type(ba1))    # <class 'bytearray'>
print(ba1)          # bytearray(b'hello')
print(ba1[0])       # 104 (ASCII 'h')
```

**Key Features:**
- Mutable (can be changed after creation)
- Elements are integers (0-255)
- Supports indexing, slicing, iteration
- Not hashable (cannot be used as dict keys)
- Efficient for in-place modifications
- Can be converted to bytes

---

## Creating Bytearray

### Method 1: From String with Encoding

```python
# From string with encoding
ba1 = bytearray('hello', 'utf-8')
print(ba1)  # bytearray(b'hello')

# Different encodings
ba2 = bytearray('Hello', 'utf-8')
print(ba2)  # bytearray(b'Hello \xe4\xb8\x96\xe7\x95\x8c')

# With error handling
ba3 = bytearray('Hello', 'ascii', errors='ignore')
print(ba3)  # bytearray(b'Hello ')
```

### Method 2: From Bytes Literal

```python
# From bytes literal
ba1 = bytearray(b'hello')
print(ba1)  # bytearray(b'hello')

# With escape sequences
ba2 = bytearray(b'hello\nworld')
print(ba2)  # bytearray(b'hello\nworld')

# Hex escapes
ba3 = bytearray(b'\x48\x65\x6c\x6c\x6f')
print(ba3)  # bytearray(b'Hello')
```

### Method 3: From List of Integers

```python
# From list of integers (0-255)
ba1 = bytearray([65, 66, 67, 68, 69])
print(ba1)  # bytearray(b'ABCDE')

# From range
ba2 = bytearray(range(10))
print(ba2)  # bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')

# Invalid values (outside 0-255)
try:
    ba3 = bytearray([256, -1])
except ValueError as e:
    print(f"Error: {e}")  # byte must be in range(0, 256)
```

### Method 4: Pre-allocate Size

```python
# Pre-allocate with zeros
ba = bytearray(10)
print(ba)  # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Useful for buffers
buffer = bytearray(1024)  # 1KB buffer
print(f"Buffer size: {len(buffer)}")
```

### Method 5: From Hex String

```python
# From hex string
ba = bytearray.fromhex('48656c6c6f')
print(ba)  # bytearray(b'Hello')

# With spaces
ba = bytearray.fromhex('48 65 6c 6c 6f')
print(ba)  # bytearray(b'Hello')

# Real use: Parse hex dump
hex_dump = "50 4b 03 04 14 00 00 00"
data = bytearray.fromhex(hex_dump)
print(data[:8])  # bytearray(b'PK\x03\x04\x14\x00\x00\x00')
```

---

## Bytearray Methods

### Adding Elements

#### `append(x)`
Appends a single byte to the end.

```python
ba = bytearray(b'Hello')
ba.append(33)  # ASCII '!'
print(ba)  # bytearray(b'Hello!')

# Must be 0-255
try:
    ba.append(256)
except ValueError:
    print("Value must be 0-255")
```

#### `extend(iterable)`
Extends by appending all bytes from iterable.

```python
ba = bytearray(b'Hello')
ba.extend(b' World')
print(ba)  # bytearray(b'Hello World')

# From list
ba.extend([33, 34, 35])
print(ba)  # bytearray(b'Hello World!"#$')

# From range
ba = bytearray(b'ABC')
ba.extend(range(68, 71))  # D, E, F
print(ba)  # bytearray(b'ABCDEF')
```

#### `insert(i, x)`
Inserts a byte at the specified position.

```python
ba = bytearray(b'Hello')
ba.insert(5, 32)  # Insert space at position 5
print(ba)  # bytearray(b'Hello ')

ba.insert(0, 72)  # Insert 'H' at beginning
print(ba)  # bytearray(b'HHello ')

# Insert in middle
ba = bytearray(b'abc')
ba.insert(2, 90)  # Insert 'Z'
print(ba)  # bytearray(b'abZc')
```

### Removing Elements

#### `pop(i=-1)`
Removes and returns the byte at the specified position (default last).

```python
ba = bytearray(b'Hello')

# Pop last
last = ba.pop()
print(last)     # 111 ('o')
print(ba)       # bytearray(b'Hell')

# Pop at index
byte = ba.pop(0)
print(byte)     # 72 ('H')
print(ba)       # bytearray(b'ell')

# Pop from empty
empty = bytearray()
try:
    empty.pop()
except IndexError:
    print("Cannot pop from empty bytearray")
```

#### `remove(value)`
Removes the first occurrence of the specified value.

```python
ba = bytearray(b'Hello World')

# Remove space (ASCII 32)
ba.remove(32)
print(ba)  # bytearray(b'HelloWorld')

# Remove multiple (only first)
ba = bytearray(b'banana')
ba.remove(97)  # 'a'
print(ba)  # bytearray(b'bnana')

# Value not found
try:
    ba.remove(120)
except ValueError:
    print("Value not found")
```

#### `clear()`
Removes all elements from the bytearray.

```python
ba = bytearray(b'Hello World')
ba.clear()
print(ba)  # bytearray(b'')

# Reuse the same object
ba = bytearray(b'data')
ba.clear()
ba.extend(b'new data')
print(ba)  # bytearray(b'new data')
```

### Modifying Elements

#### Direct Assignment

```python
ba = bytearray(b'Hello')

# Modify single byte
ba[0] = 74  # 'J'
print(ba)  # bytearray(b'Jello')

# Modify slice
ba[1:3] = b'hi'
print(ba)  # bytearray(b'Jhilo')

# Assign with different length
ba[2:4] = b'XYZ'
print(ba)  # bytearray(b'JhXYZo')

# Delete slice
ba[2:5] = b''
print(ba)  # bytearray(b'Jho')
```

### Searching Methods

#### `find(sub[, start[, end]])`
Returns the lowest index where sub is found, or -1 if not found.

```python
ba = bytearray(b'Hello Hello Hello')

print(ba.find(b'Hello'))      # 0
print(ba.find(b'Hello', 1))   # 6
print(ba.find(b'World'))      # -1

# Find with range
print(ba.find(b'Hello', 1, 10))  # 6
```

#### `rfind(sub[, start[, end]])`
Returns the highest index where sub is found, or -1 if not found.

```python
ba = bytearray(b'Hello Hello Hello')

print(ba.rfind(b'Hello'))     # 12
print(ba.rfind(b'Hello', 0, 10))  # 6
```

#### `index(sub[, start[, end]])`
Like find() but raises ValueError if not found.

```python
ba = bytearray(b'Hello World')

print(ba.index(b'World'))     # 6

try:
    ba.index(b'Python')
except ValueError:
    print("Not found")
```

#### `count(sub[, start[, end]])`
Returns the number of non-overlapping occurrences.

```python
ba = bytearray(b'Hello Hello Hello')

print(ba.count(b'Hello'))     # 3
print(ba.count(b'Hello', 1, 10))  # 1
```

### Case Conversion Methods

```python
ba = bytearray(b'Hello World')

# upper() - convert to uppercase
ba.upper()
print(ba)  # bytearray(b'HELLO WORLD')

# lower() - convert to lowercase
ba.lower()
print(ba)  # bytearray(b'hello world')

# capitalize() - first letter uppercase
ba = bytearray(b'hello world')
ba.capitalize()
print(ba)  # bytearray(b'Hello world')

# title() - each word title case
ba = bytearray(b'hello world python')
ba.title()
print(ba)  # bytearray(b'Hello World Python')

# swapcase() - swap case
ba = bytearray(b'Hello World')
ba.swapcase()
print(ba)  # bytearray(b'hELLO wORLD')
```

### Checking Methods

```python
# isalpha() - all bytes are alphabetic
print(bytearray(b'Hello').isalpha())     # True
print(bytearray(b'Hello123').isalpha())  # False

# isdigit() - all bytes are digits
print(bytearray(b'123').isdigit())       # True
print(bytearray(b'123.45').isdigit())    # False

# isalnum() - alphanumeric
print(bytearray(b'Hello123').isalnum())  # True
print(bytearray(b'Hello 123').isalnum()) # False

# isspace() - all bytes are whitespace
print(bytearray(b'   ').isspace())       # True
print(bytearray(b'\t\n').isspace())      # True

# islower() - all cased bytes are lowercase
print(bytearray(b'hello').islower())     # True
print(bytearray(b'Hello').islower())     # False

# isupper() - all cased bytes are uppercase
print(bytearray(b'HELLO').isupper())     # True
print(bytearray(b'Hello').isupper())     # False

# isascii() - all bytes are ASCII
print(bytearray(b'Hello').isascii())     # True
print(bytearray(b'\xff').isascii())      # False
```

### Split and Join Methods

```python
# split() - split by delimiter
ba = bytearray(b'apple,banana,orange')
result = ba.split(b',')
print(result)  # [bytearray(b'apple'), bytearray(b'banana'), bytearray(b'orange')]

# rsplit() - split from right
result = ba.rsplit(b',', 1)
print(result)  # [bytearray(b'apple,banana'), bytearray(b'orange')]

# splitlines() - split by line breaks
ba = bytearray(b'line1\nline2\r\nline3')
print(ba.splitlines())  # [bytearray(b'line1'), bytearray(b'line2'), bytearray(b'line3')]

# join() - join bytearray objects
parts = [bytearray(b'Hello'), bytearray(b'World')]
result = bytearray(b' ').join(parts)
print(result)  # bytearray(b'Hello World')
```

### Strip Methods

```python
# strip() - remove whitespace
ba = bytearray(b'  Hello World  \n')
ba.strip()
print(ba)  # bytearray(b'Hello World')

# lstrip() - remove left whitespace
ba = bytearray(b'  Hello World  ')
ba.lstrip()
print(ba)  # bytearray(b'Hello World  ')

# rstrip() - remove right whitespace
ba = bytearray(b'  Hello World  ')
ba.rstrip()
print(ba)  # bytearray(b'  Hello World')

# strip with characters
ba = bytearray(b'xxHello Worldxx')
ba.strip(b'x')
print(ba)  # bytearray(b'Hello World')
```

### Replace and Translate

```python
# replace() - replace occurrences
ba = bytearray(b'Hello Hello Hello')
ba.replace(b'Hello', b'Hi')
print(ba)  # bytearray(b'Hi Hi Hi')

# replace with count limit
ba = bytearray(b'Hello Hello Hello')
ba.replace(b'Hello', b'Hi', 2)
print(ba)  # bytearray(b'Hi Hi Hello')

# translate() - character mapping
table = bytes.maketrans(b'aeiou', b'12345')
ba = bytearray(b'hello world')
ba.translate(table)
print(ba)  # bytearray(b'h2ll4 w4rld')

# Remove characters
table = bytes.maketrans(b'', b'', b'aeiou')
ba = bytearray(b'hello world')
ba.translate(table)
print(ba)  # bytearray(b'hll wrld')
```

### Padding and Alignment

```python
# center() - center align
ba = bytearray(b'Python')
ba.center(20, b'*')
print(ba)  # bytearray(b'*******Python*******')

# ljust() - left justify
ba = bytearray(b'Python')
ba.ljust(20, b'-')
print(ba)  # bytearray(b'Python--------------')

# rjust() - right justify
ba = bytearray(b'Python')
ba.rjust(20, b'-')
print(ba)  # bytearray(b'--------------Python')

# zfill() - zero pad
ba = bytearray(b'42')
ba.zfill(5)
print(ba)  # bytearray(b'00042')
```

### Hex and Conversion

```python
# hex() - convert to hex string
ba = bytearray(b'Hello')
print(ba.hex())           # '48656c6c6f'
print(ba.hex(' '))        # '48 65 6c 6c 6f'
print(ba.hex(':', 2))     # '48:65:6c:6c:6f'

# fromhex() - class method
ba = bytearray.fromhex('48656c6c6f')
print(ba)  # bytearray(b'Hello')
```

---

## Bytearray Operations

### Indexing and Slicing

```python
ba = bytearray(b'Python Programming')

# Indexing (returns int)
print(ba[0])      # 80 (ASCII 'P')
print(ba[-1])     # 103 (ASCII 'g')

# Slicing (returns bytearray)
print(ba[0:6])    # bytearray(b'Python')
print(ba[7:18])   # bytearray(b'Programming')
print(ba[::-1])   # bytearray(b'gnimmargorP nohtyP')

# Modify via slice
ba[0:6] = b'PYTHON'
print(ba)  # bytearray(b'PYTHON Programming')
```

### Concatenation and Repetition

```python
# Concatenation (+)
ba1 = bytearray(b'Hello')
ba2 = bytearray(b' World')
ba3 = ba1 + ba2
print(ba3)  # bytearray(b'Hello World')

# Repetition (*)
ba = bytearray(b'Ha') * 3
print(ba)  # bytearray(b'HaHaHa')

# In-place extension
ba = bytearray(b'Hello')
ba += b' World'
print(ba)  # bytearray(b'Hello World')
```

### Membership Testing

```python
ba = bytearray(b'Hello World')

print(b'Hello' in ba)     # True
print(b'World' in ba)     # True
print(b'Python' in ba)    # False
print(72 in ba)           # True (ASCII 'H')
```

### Comparison Operators

```python
ba1 = bytearray(b'apple')
ba2 = bytearray(b'banana')
ba3 = bytearray(b'apple')

print(ba1 == ba3)    # True
print(ba1 < ba2)     # True ('a' < 'b')
print(ba1 > ba2)     # False
```

### Length and Iteration

```python
ba = bytearray(b'Hello')

print(len(ba))  # 5

# Iteration (returns ints)
for byte in ba:
    print(byte)  # 72, 101, 108, 108, 111

# Convert to list
print(list(ba))  # [72, 101, 108, 108, 111]
```

---

## Real-World Examples

### Example 1: In-Place File Modification

```python
class FileEditor:
    @staticmethod
    def replace_in_file(filename, old, new):
        """Replace bytes in file without creating new file"""
        with open(filename, 'r+b') as f:
            data = bytearray(f.read())
            count = data.count(old)
            if count > 0:
                data = data.replace(old, new)
                f.seek(0)
                f.write(data)
                f.truncate()
            return count
    
    @staticmethod
    def patch_file(filename, offset, new_bytes):
        """Patch file at specific offset"""
        with open(filename, 'r+b') as f:
            f.seek(offset)
            f.write(new_bytes)
    
    @staticmethod
    def insert_at_position(filename, position, data):
        """Insert bytes at position"""
        with open(filename, 'r+b') as f:
            content = bytearray(f.read())
            content[position:position] = data
            f.seek(0)
            f.write(content)
            f.truncate()

# Create test file
with open('test.txt', 'wb') as f:
    f.write(b'Hello World! This is a test.')

editor = FileEditor()

# Replace text
count = editor.replace_in_file('test.txt', b'World', b'Python')
print(f"Replaced {count} occurrence(s)")

# Patch at offset
editor.patch_file('test.txt', 6, b'UNIVERSE')

# Insert at position
editor.insert_at_position('test.txt', 13, b' Amazing')

# Verify
with open('test.txt', 'rb') as f:
    print(f.read())  # b'Hello UNIVERSE! Amazing This is a test.'
```

### Example 2: Network Buffer Manager

```python
class NetworkBuffer:
    def __init__(self, capacity=1024):
        self.buffer = bytearray(capacity)
        self.size = 0
        self.position = 0
    
    def write(self, data):
        """Write data to buffer"""
        space_available = len(self.buffer) - self.position
        if len(data) > space_available:
            self._expand_buffer(len(data) - space_available)
        
        self.buffer[self.position:self.position + len(data)] = data
        self.position += len(data)
        self.size = max(self.size, self.position)
    
    def read(self, length=None):
        """Read data from buffer"""
        if length is None:
            length = self.size
        
        data = bytes(self.buffer[:length])
        # Shift remaining data
        self.buffer = self.buffer[length:] + bytearray(len(self.buffer) - length)
        self.position -= length
        self.size -= length
        if self.position < 0:
            self.position = 0
        
        return data
    
    def _expand_buffer(self, needed):
        """Expand buffer capacity"""
        new_capacity = len(self.buffer) + max(needed, 1024)
        new_buffer = bytearray(new_capacity)
        new_buffer[:self.size] = self.buffer[:self.size]
        self.buffer = new_buffer
    
    def peek(self, length=None):
        """Peek at data without consuming"""
        if length is None:
            length = self.size
        return bytes(self.buffer[:length])
    
    def clear(self):
        """Clear buffer"""
        self.buffer = bytearray(len(self.buffer))
        self.size = 0
        self.position = 0
    
    def available(self):
        """Get available bytes to read"""
        return self.size

# Usage
buffer = NetworkBuffer(64)

# Write data
buffer.write(b'Hello ')
buffer.write(b'World')
buffer.write(b'! ' * 10)

print(f"Available: {buffer.available()} bytes")
print(f"Peek: {buffer.peek(20)}")

# Read data
data = buffer.read(12)
print(f"Read: {data}")

print(f"Remaining: {buffer.available()} bytes")
```

### Example 3: Binary Protocol Parser

```python
import struct

class BinaryProtocol:
    def __init__(self):
        self.buffer = bytearray()
        self.packets = []
    
    def feed(self, data):
        """Feed raw data into parser"""
        self.buffer.extend(data)
        self._parse()
    
    def _parse(self):
        """Parse packets from buffer"""
        while len(self.buffer) >= 5:  # Minimum header size
            # Check packet length
            packet_len = struct.unpack('!I', self.buffer[1:5])[0]
            
            if len(self.buffer) >= 5 + packet_len:
                # Extract packet
                packet_type = self.buffer[0]
                payload = bytes(self.buffer[5:5 + packet_len])
                
                self.packets.append({
                    'type': packet_type,
                    'length': packet_len,
                    'payload': payload
                })
                
                # Remove processed data
                self.buffer = self.buffer[5 + packet_len:]
            else:
                break
    
    def create_packet(self, packet_type, payload):
        """Create a packet"""
        header = struct.pack('!BI', packet_type, len(payload))
        return header + payload
    
    def get_packets(self):
        """Get all parsed packets"""
        packets = self.packets
        self.packets = []
        return packets

# Usage
protocol = BinaryProtocol()

# Create packets
packet1 = protocol.create_packet(1, b'Hello Server')
packet2 = protocol.create_packet(2, b'Data packet')
packet3 = protocol.create_packet(3, b'Goodbye')

# Simulate network stream (might be fragmented)
protocol.feed(packet1[:5])  # Partial packet
protocol.feed(packet1[5:])  # Rest of packet
protocol.feed(packet2[:10]) # Partial
protocol.feed(packet2[10:]) # Rest
protocol.feed(packet3)      # Complete

# Get parsed packets
for packet in protocol.get_packets():
    print(f"Type: {packet['type']}, Length: {packet['length']}, Payload: {packet['payload']}")
```

### Example 4: Binary Search and Replace Tool

```python
class BinaryEditor:
    def __init__(self, data=None):
        self.data = bytearray(data) if data else bytearray()
    
    def load_file(self, filename):
        """Load binary file"""
        with open(filename, 'rb') as f:
            self.data = bytearray(f.read())
    
    def save_file(self, filename):
        """Save to binary file"""
        with open(filename, 'wb') as f:
            f.write(self.data)
    
    def find_all(self, pattern):
        """Find all occurrences of pattern"""
        positions = []
        start = 0
        while True:
            pos = self.data.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        return positions
    
    def replace_all(self, old, new):
        """Replace all occurrences"""
        count = self.data.count(old)
        self.data = self.data.replace(old, new)
        return count
    
    def replace_at(self, position, new_bytes):
        """Replace bytes at position"""
        if position + len(new_bytes) <= len(self.data):
            self.data[position:position + len(new_bytes)] = new_bytes
            return True
        return False
    
    def insert_at(self, position, data):
        """Insert bytes at position"""
        self.data[position:position] = data
    
    def delete_range(self, start, end):
        """Delete bytes in range"""
        self.data[start:end] = b''
    
    def extract_range(self, start, end):
        """Extract bytes in range"""
        return bytes(self.data[start:end])
    
    def search_hex(self, hex_pattern):
        """Search by hex pattern"""
        pattern = bytes.fromhex(hex_pattern)
        return self.find_all(pattern)
    
    def get_hex_dump(self, width=16):
        """Get hex dump of data"""
        result = []
        for i in range(0, len(self.data), width):
            chunk = self.data[i:i+width]
            hex_part = ' '.join(f'{b:02x}' for b in chunk)
            hex_part = hex_part.ljust(width * 3)
            ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
            result.append(f'{i:08x}: {hex_part} {ascii_part}')
        return '\n'.join(result)

# Usage
editor = BinaryEditor(b'Hello World Hello Python Hello World')

print("Original:")
print(editor.get_hex_dump(16))

# Find all
positions = editor.find_all(b'Hello')
print(f"\n'Hello' found at: {positions}")

# Replace all
count = editor.replace_all(b'Hello', b'Hi')
print(f"Replaced {count} occurrences")

# Replace at position
editor.replace_at(3, b'XXXX')

# Insert
editor.insert_at(0, b'START:')

# Delete
editor.delete_range(10, 20)

print("\nAfter modifications:")
print(editor.get_hex_dump(16))

# Extract range
extracted = editor.extract_range(5, 15)
print(f"\nExtracted (5-15): {extracted}")
```

### Example 5: Bytearray as Ring Buffer

```python
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = bytearray(capacity)
        self.head = 0  # Write position
        self.tail = 0  # Read position
        self.full = False
    
    def write(self, data):
        """Write data to buffer"""
        for byte in data:
            self.buffer[self.head] = byte
            self.head = (self.head + 1) % self.capacity
            
            if self.head == self.tail:
                self.full = True
                self.tail = (self.tail + 1) % self.capacity
    
    def read(self, size=None):
        """Read data from buffer"""
        if size is None:
            size = self.available()
        
        data = bytearray()
        for _ in range(min(size, self.available())):
            data.append(self.buffer[self.tail])
            self.tail = (self.tail + 1) % self.capacity
        
        self.full = False
        return bytes(data)
    
    def available(self):
        """Get available bytes to read"""
        if self.full:
            return self.capacity
        if self.head >= self.tail:
            return self.head - self.tail
        return self.capacity - self.tail + self.head
    
    def peek(self, size=None):
        """Peek at data without consuming"""
        if size is None:
            size = self.available()
        
        data = bytearray()
        pos = self.tail
        for _ in range(min(size, self.available())):
            data.append(self.buffer[pos])
            pos = (pos + 1) % self.capacity
        
        return bytes(data)
    
    def clear(self):
        """Clear buffer"""
        self.head = 0
        self.tail = 0
        self.full = False
        self.buffer = bytearray(self.capacity)
    
    def is_empty(self):
        """Check if buffer is empty"""
        return not self.full and self.head == self.tail
    
    def is_full(self):
        """Check if buffer is full"""
        return self.full

# Usage
buffer = RingBuffer(10)

print("Writing data...")
buffer.write(b'Hello')
print(f"Available: {buffer.available()}")
print(f"Peek: {buffer.peek()}")

buffer.write(b' World')
print(f"Available: {buffer.available()}")

print(f"\nReading data...")
data = buffer.read(5)
print(f"Read: {data}")
print(f"Available: {buffer.available()}")

data = buffer.read()
print(f"Read all: {data}")
print(f"Available: {buffer.available()}")
print(f"Is empty: {buffer.is_empty()}")

print("\nWriting more data...")
buffer.write(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f"Available: {buffer.available()}")
print(f"Is full: {buffer.is_full()}")

data = buffer.read(10)
print(f"Read: {data}")
print(f"Available: {buffer.available()}")
```

### Example 6: CRC and Checksum Calculator

```python
import zlib
import binascii

class ChecksumTool:
    @staticmethod
    def update_checksum(data, position, new_value):
        """Update data and recalculate checksum"""
        ba = bytearray(data)
        ba[position] = new_value
        return bytes(ba), zlib.crc32(ba) & 0xFFFFFFFF
    
    @staticmethod
    def find_checksum_collision(target_crc, data, start_pos, end_pos):
        """Find byte values that produce target CRC"""
        ba = bytearray(data)
        results = []
        
        for value in range(256):
            ba[start_pos:end_pos] = bytes([value]) * (end_pos - start_pos)
            crc = zlib.crc32(ba) & 0xFFFFFFFF
            if crc == target_crc:
                results.append(value)
        
        return results
    
    @staticmethod
    def verify_data_integrity(data, expected_crc):
        """Verify data integrity with CRC"""
        actual_crc = zlib.crc32(data) & 0xFFFFFFFF
        return actual_crc == expected_crc, actual_crc
    
    @staticmethod
    def create_checksummed_packet(packet_type, payload):
        """Create packet with checksum"""
        header = struct.pack('!B', packet_type)
        data = header + payload
        crc = zlib.crc32(data) & 0xFFFFFFFF
        crc_bytes = struct.pack('!I', crc)
        return data + crc_bytes
    
    @staticmethod
    def verify_packet(packet):
        """Verify packet checksum"""
        if len(packet) < 5:
            return False, "Packet too short"
        
        received_crc = struct.unpack('!I', packet[-4:])[0]
        calculated_crc = zlib.crc32(packet[:-4]) & 0xFFFFFFFF
        
        if received_crc != calculated_crc:
            return False, f"Checksum mismatch: expected {calculated_crc:08x}, got {received_crc:08x}"
        
        packet_type = packet[0]
        payload = packet[1:-4]
        return True, {'type': packet_type, 'payload': payload}

# Usage
print("CHECKSUM TOOL")
print("=" * 40)

# Create packet
packet = ChecksumTool.create_checksummed_packet(1, b'Hello World')
print(f"Packet with checksum: {packet.hex()}")

# Verify packet
valid, result = ChecksumTool.verify_packet(packet)
print(f"Packet valid: {valid}")
if valid:
    print(f"  Type: {result['type']}")
    print(f"  Payload: {result['payload']}")

# Test integrity
data = b'Important data'
crc = zlib.crc32(data) & 0xFFFFFFFF
print(f"\nData: {data}")
print(f"CRC32: {crc:08x}")

# Modify data
modified = bytearray(data)
modified[5] = 88
modified = bytes(modified)

valid, actual = ChecksumTool.verify_data_integrity(modified, crc)
print(f"Modified data valid: {valid}")
print(f"Actual CRC: {actual:08x}")

# Update checksum after modification
new_data, new_crc = ChecksumTool.update_checksum(data, 5, 88)
print(f"\nAfter updating byte at position 5:")
print(f"New CRC: {new_crc:08x}")
valid, _ = ChecksumTool.verify_data_integrity(new_data, new_crc)
print(f"New data valid: {valid}")
```

---

## Common Pitfalls

### Pitfall 1: Bytearray vs Bytes

```python
# Bytearray is mutable, bytes is immutable
ba = bytearray(b'Hello')
b = b'Hello'

ba[0] = 74  # Works
# b[0] = 74  # TypeError!

# Conversion
ba = bytearray(b'Hello')
b = bytes(ba)  # bytearray to bytes
ba2 = bytearray(b)  # bytes to bytearray
```

### Pitfall 2: Index Returns Integer

```python
ba = bytearray(b'Hello')

# Index returns int, not bytearray
value = ba[0]  # 72 (int), not b'H'

# Get single byte as bytearray
single = ba[0:1]  # bytearray(b'H')
```

### Pitfall 3: Methods Modify In-Place

```python
ba = bytearray(b'hello')

# Most methods modify in-place and return None
result = ba.upper()
print(result)  # None
print(ba)      # bytearray(b'HELLO')

# To keep original, copy first
ba = bytearray(b'hello')
ba_copy = ba.copy()
ba_copy.upper()
print(ba)      # bytearray(b'hello') (unchanged)
print(ba_copy) # bytearray(b'HELLO')
```

### Pitfall 4: Value Range

```python
ba = bytearray(5)

# Values must be 0-255
try:
    ba[0] = 256
except ValueError:
    print("Value must be in range(0, 256)")

# Valid values
ba[0] = 0      # OK
ba[1] = 128    # OK
ba[2] = 255    # OK
```

---

## Performance Tips

### Pre-allocate When Size Known

```python
# Slow: Growing dynamically
ba = bytearray()
for i in range(10000):
    ba.append(i % 256)

# Fast: Pre-allocate
ba = bytearray(10000)
for i in range(10000):
    ba[i] = i % 256
```

### Use Slice Assignment for Bulk Operations

```python
# Slow: Individual assignments
ba = bytearray(1000)
for i in range(1000):
    ba[i] = 65

# Fast: Slice assignment
ba = bytearray(1000)
ba[:] = b'A' * 1000
```

### Extend vs Append

```python
# Append one byte at a time (slower for many)
ba = bytearray()
for i in range(1000):
    ba.append(65)

# Extend with pre-created data (faster)
ba = bytearray()
ba.extend(b'A' * 1000)

# Pre-allocate and assign (fastest)
ba = bytearray(1000)
ba[:] = b'A' * 1000
```

---

## Practice Exercises

### Beginner Level

1. **Bytearray from String**
   ```python
   # Create bytearray from string and modify
   # Example: b'hello' -> b'HELLO'
   ```

2. **Find and Replace**
   ```python
   # Replace all spaces with underscores
   # Example: b'hello world' -> b'hello_world'
   ```

3. **Byte Counter**
   ```python
   # Count frequency of each byte value
   # Example: b'hello' -> {104:1, 101:1, 108:2, 111:1}
   ```

### Intermediate Level

4. **XOR Encryption**
   ```python
   # Implement XOR cipher on bytearray
   # Encrypt and decrypt in-place
   ```

5. **Binary Search Tool**
   ```python
   # Search for pattern in bytearray with wildcard support
   # Example: b'he??o' matches b'hello', b'heppo'
   ```

6. **Bytearray Compressor**
   ```python
   # Implement simple run-length encoding
   # Example: b'aaabbbcc' -> b'\x03a\x03b\x02c'
   ```

### Advanced Level

7. **Protocol Parser**
   ```python
   # Implement parser for custom binary protocol
   # Support variable-length fields
   ```

8. **Ring Buffer**
   ```python
   # Implement efficient ring buffer with bytearray
   # Support overwrite when full
   ```

9. **Binary Diff Tool**
   ```python
   # Find differences between two bytearrays
   # Output insertions, deletions, modifications
   ```

---

## Quick Reference Card

```python
# Creation
ba = bytearray(b'hello')           # From bytes
ba = bytearray([65, 66, 67])       # From list
ba = bytearray(10)                 # Pre-allocate
ba = bytearray.fromhex('48656c6c6f') # From hex

# Adding
ba.append(33)                      # Add byte
ba.extend(b' world')               # Add multiple
ba.insert(5, 32)                   # Insert at position

# Removing
ba.pop()                           # Remove last
ba.pop(0)                          # Remove at index
ba.remove(108)                     # Remove first 'l'
ba.clear()                         # Remove all

# Modifying
ba[0] = 74                         # Modify byte
ba[1:3] = b'XX'                    # Modify slice
ba[2:5] = b''                      # Delete slice

# Searching
ba.find(b'ell')                    # Find position
ba.rfind(b'ell')                   # Find from right
ba.index(b'ell')                   # Find (raises error)
ba.count(b'l')                     # Count occurrences

# Case
ba.upper()                         # To uppercase
ba.lower()                         # To lowercase
ba.capitalize()                    # First letter uppercase
ba.title()                         # Title case

# Checking
ba.isalpha()                       # Check alphabetic
ba.isdigit()                       # Check digits
ba.isalnum()                       # Check alphanumeric

# Split/Join
ba.split(b',')                     # Split
ba.splitlines()                    # Split by lines
b' '.join([ba1, ba2])              # Join

# Strip
ba.strip()                         # Strip whitespace
ba.lstrip()                        # Strip left
ba.rstrip()                        # Strip right

# Replace/Translate
ba.replace(b'old', b'new')         # Replace
ba.translate(table)                # Translate

# Hex
ba.hex()                           # To hex string
ba.hex(' ')                        # Hex with spaces
```

## Next Step

- Move to [03_memoryview.md](03_memoryview.md) for understanding Memoryiew Data Type.
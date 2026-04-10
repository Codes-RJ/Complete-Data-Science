# 📘 BYTES (bytes) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Bytes?](#what-are-bytes)
2. [Creating Bytes](#creating-bytes)
3. [Bytes Methods](#bytes-methods)
4. [Bytes Operations](#bytes-operations)
5. [Encoding and Decoding](#encoding-and-decoding)
6. [Bytes vs Strings](#bytes-vs-strings)
7. [Real-World Examples](#real-world-examples)
8. [Common Pitfalls](#common-pitfalls)
9. [Performance Tips](#performance-tips)
10. [Practice Exercises](#practice-exercises)

---

## 📖 What are Bytes?

**Bytes** are immutable sequences of integers in the range 0-255. They represent binary data and are used for handling files, network communication, and low-level data manipulation.

```python
# Examples of bytes
b1 = b'hello'                    # Bytes literal
b2 = b"world"                    # Double quotes
b3 = b'\x48\x65\x6c\x6c\x6f'    # Hex escape: b'Hello'
b4 = bytes([65, 66, 67])         # From list: b'ABC'
b5 = bytes(5)                    # Zero-filled: b'\x00\x00\x00\x00\x00'
b6 = b''                         # Empty bytes

print(type(b1))   # <class 'bytes'>
print(b1)         # b'hello'
print(b1[0])      # 104 (ASCII value of 'h')
```

**Key Features:**
- ✅ Immutable (cannot be changed after creation)
- ✅ Elements are integers (0-255)
- ✅ Supports indexing, slicing, iteration
- ✅ Hashable (can be used as dict keys)
- ✅ Efficient for binary data storage
- ✅ Can be created from strings via encoding

---

## 🎯 Creating Bytes

### Method 1: Bytes Literal (`b''`)

```python
# Basic literals
b1 = b'hello'
b2 = b"world"
b3 = b'''multi
line'''                    # Multi-line bytes
b4 = b''                   # Empty bytes

print(b1)  # b'hello'
print(b3)  # b'multi\nline'

# Escape sequences work
b5 = b'hello\nworld'       # Newline
b6 = b'hello\tworld'       # Tab
b7 = b'C:\\path\\file'     # Backslash
b8 = b'It\'s working'      # Single quote

# Hex escape sequences
b9 = b'\x48\x65\x6c\x6c\x6f'  # b'Hello'
b10 = b'\x00\x01\x02\xff'      # Any byte values

print(b9)  # b'Hello'
print(b10) # b'\x00\x01\x02\xff'
```

### Method 2: `bytes()` Constructor

```python
# From string with encoding
b1 = bytes('hello', 'utf-8')
print(b1)  # b'hello'

# From list of integers (0-255)
b2 = bytes([65, 66, 67, 68, 69])
print(b2)  # b'ABCDE'

# From range
b3 = bytes(range(10))
print(b3)  # b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'

# From integer (zero-filled)
b4 = bytes(10)
print(b4)  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# From another bytes object
b5 = bytes(b'hello')
print(b5)  # b'hello'

# Empty bytes
b6 = bytes()
print(b6)  # b''
```

### Method 3: `fromhex()` Class Method

```python
# From hex string
b1 = bytes.fromhex('48656c6c6f')
print(b1)  # b'Hello'

# With spaces (ignored)
b2 = bytes.fromhex('48 65 6c 6c 6f')
print(b2)  # b'Hello'

# Uppercase/lowercase both work
b3 = bytes.fromhex('FF ff Ff')
print(b3)  # b'\xff\xff\xff'

# Real use: Convert hex dump to bytes
hex_dump = "50 4b 03 04 14 00 00 00"
data = bytes.fromhex(hex_dump)
print(data[:8])  # b'PK\x03\x04\x14\x00\x00\x00'
```

### Method 4: From String Encoding

```python
# UTF-8 encoding (default)
text = "Hello"
b1 = text.encode('utf-8')
print(b1)  # b'Hello \xe4\xb8\x96\xe7\x95\x8c'

# ASCII encoding (raises error for non-ASCII)
try:
    b2 = text.encode('ascii')
except UnicodeEncodeError:
    print("Cannot encode non-ASCII to ASCII")

# ASCII with error handling
b3 = text.encode('ascii', errors='ignore')
print(b3)  # b'Hello '

b4 = text.encode('ascii', errors='replace')
print(b4)  # b'Hello ??'

b5 = text.encode('ascii', errors='xmlcharrefreplace')
print(b5)  # b'Hello &#19990;&#30028;'

# Other encodings
b6 = "Hello".encode('utf-16')
print(b6)  # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00'

b7 = "Hello".encode('utf-32')
print(b7)  # b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00...'
```

---

## 📚 Bytes Methods

Bytes methods are similar to string methods but work with byte values.

### Case Conversion Methods

```python
b = b'Hello World'

# upper() - convert to uppercase
print(b.upper())  # b'HELLO WORLD'

# lower() - convert to lowercase
print(b.lower())  # b'hello world'

# capitalize() - first letter uppercase
print(b.capitalize())  # b'Hello world'

# title() - each word title case
print(b.title())  # b'Hello World'

# swapcase() - swap case
print(b.swapcase())  # b'hELLO wORLD'

# Real use: Case-insensitive comparison
def case_insensitive_bytes_equal(b1, b2):
    return b1.lower() == b2.lower()

print(case_insensitive_bytes_equal(b'Hello', b'HELLO'))  # True
```

### Checking Methods

```python
# isalpha() - all bytes are alphabetic
print(b'Hello'.isalpha())     # True
print(b'Hello123'.isalpha())  # False

# isdigit() - all bytes are digits
print(b'123'.isdigit())       # True
print(b'123.45'.isdigit())    # False

# isalnum() - alphanumeric
print(b'Hello123'.isalnum())  # True
print(b'Hello 123'.isalnum()) # False (space)

# isspace() - all bytes are whitespace
print(b'   '.isspace())       # True
print(b'\t\n'.isspace())      # True

# islower() - all cased bytes are lowercase
print(b'hello'.islower())     # True
print(b'Hello'.islower())     # False

# isupper() - all cased bytes are uppercase
print(b'HELLO'.isupper())     # True
print(b'Hello'.isupper())     # False

# isascii() - all bytes are ASCII
print(b'Hello'.isascii())     # True
print(b'\xff'.isascii())      # False
```

### Search Methods

```python
b = b'Hello Hello Hello'

# find() - find first occurrence
print(b.find(b'Hello'))      # 0
print(b.find(b'Hello', 1))   # 6
print(b.find(b'World'))      # -1

# rfind() - find from right
print(b.rfind(b'Hello'))     # 12

# index() - like find but raises ValueError
print(b.index(b'Hello'))     # 0
try:
    b.index(b'World')
except ValueError:
    print("Not found")

# rindex() - from right
print(b.rindex(b'Hello'))    # 12

# count() - count occurrences
print(b.count(b'Hello'))     # 3
print(b.count(b'Hello', 1, 10))  # 1

# startswith() - check prefix
print(b.startswith(b'Hello'))    # True
print(b.startswith(b'World'))    # False

# endswith() - check suffix
print(b.endswith(b'Hello'))      # True
print(b.endswith(b'World'))      # False
```

### Split and Join Methods

```python
# split() - split by delimiter
b = b'apple,banana,orange'
print(b.split(b','))        # [b'apple', b'banana', b'orange']
print(b.split(b',', 1))     # [b'apple', b'banana,orange']

# rsplit() - split from right
print(b.rsplit(b',', 1))    # [b'apple,banana', b'orange']

# splitlines() - split by line breaks
b = b'line1\nline2\r\nline3'
print(b.splitlines())       # [b'line1', b'line2', b'line3']
print(b.splitlines(True))   # [b'line1\n', b'line2\r\n', b'line3']

# partition() - split into 3 parts
print(b.partition(b','))    # (b'apple', b',', b'banana,orange')

# rpartition() - from right
print(b.rpartition(b','))   # (b'apple,banana', b',', b'orange')

# join() - join bytes objects
parts = [b'Hello', b'World', b'Python']
print(b' '.join(parts))     # b'Hello World Python'
print(b'-'.join(parts))     # b'Hello-World-Python'

# Real use: CSV parsing
csv_data = b'name,age,city\nAlice,30,NYC\nBob,25,LA'
lines = csv_data.splitlines()
for line in lines:
    fields = line.split(b',')
    print(fields)
# Output:
# [b'name', b'age', b'city']
# [b'Alice', b'30', b'NYC']
# [b'Bob', b'25', b'LA']
```

### Strip Methods

```python
b = b'  Hello World  \n'

# strip() - remove whitespace
print(b.strip())         # b'Hello World'

# lstrip() - remove left whitespace
print(b.lstrip())        # b'Hello World  \n'

# rstrip() - remove right whitespace
print(b.rstrip())        # b'  Hello World'

# strip with characters
b2 = b'xxHello Worldxx'
print(b2.strip(b'x'))    # b'Hello World'

# Real use: Clean binary data
def clean_bytes(data):
    return data.strip()

binary_data = b'\x00\x00Hello World\x00\x00'
print(clean_bytes(binary_data))  # b'Hello World'
```

### Replace and Translate Methods

```python
# replace() - replace occurrences
b = b'Hello Hello Hello'
print(b.replace(b'Hello', b'Hi'))        # b'Hi Hi Hi'
print(b.replace(b'Hello', b'Hi', 2))     # b'Hi Hi Hello'

# translate() - character mapping
# Create translation table
table = bytes.maketrans(b'aeiou', b'12345')
b = b'hello world'
print(b.translate(table))  # b'h2ll4 w4rld'

# Remove characters
table = bytes.maketrans(b'', b'', b'aeiou')
print(b.translate(table))  # b'hll wrld'

# Real use: Censoring
def censor_bytes(data, bad_words):
    for word in bad_words:
        data = data.replace(word, b'*' * len(word))
    return data

message = b'This is a bad word'
censored = censor_bytes(message, [b'bad'])
print(censored)  # b'This is a *** word'
```

### Padding and Alignment

```python
# center() - center align
b = b'Python'
print(b.center(20))        # b'      Python       '
print(b.center(20, b'*'))  # b'*******Python*******'

# ljust() - left justify
print(b.ljust(20))         # b'Python              '
print(b.ljust(20, b'-'))   # b'Python--------------'

# rjust() - right justify
print(b.rjust(20))         # b'              Python'
print(b.rjust(20, b'-'))   # b'--------------Python'

# zfill() - zero pad
print(b'42'.zfill(5))      # b'00042'
print(b'-42'.zfill(5))     # b'-0042'

# Real use: Format binary output
def format_hex_dump(data, width=16):
    result = []
    for i in range(0, len(data), width):
        chunk = data[i:i+width]
        hex_part = ' '.join(f'{b:02x}' for b in chunk)
        hex_part = hex_part.ljust(width * 3)
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        result.append(f'{i:08x}: {hex_part} {ascii_part}')
    return '\n'.join(result)

sample = b'Hello World! This is a test.'
print(format_hex_dump(sample))
# Output:
# 00000000: 48 65 6c 6c 6f 20 57 6f 72 6c 64 21 20 54 68 69 Hello World! Thi
# 00000010: 73 20 69 73 20 61 20 74 65 73 74 2e             s is a test.
```

### Hex and Conversion Methods

```python
# hex() - convert to hex string
b = b'Hello'
print(b.hex())           # '48656c6c6f'
print(b.hex(' '))        # '48 65 6c 6c 6f'
print(b.hex(':', 2))     # '48:65:6c:6c:6f'

# fromhex() - class method (already covered)

# Real use: Convert binary to readable hex
def bytes_to_hex_string(data, separator=' '):
    return data.hex(separator)

binary_data = b'\x00\x01\x02\xff\xfe\xfd'
print(bytes_to_hex_string(binary_data))  # '00 01 02 ff fe fd'
```

---

## ⚡ Bytes Operations

### Indexing and Slicing

```python
b = b'Python Programming'

# Indexing (returns int, not bytes)
print(b[0])      # 80 (ASCII 'P')
print(b[-1])     # 103 (ASCII 'g')
print(type(b[0]))  # <class 'int'>

# Slicing (returns bytes)
print(b[0:6])    # b'Python'
print(b[7:18])   # b'Programming'
print(b[::-1])   # b'gnimmargorP nohtyP'

# Modify? No! Bytes are immutable
# b[0] = 74  # TypeError!
```

### Concatenation and Repetition

```python
# Concatenation (+)
b1 = b'Hello'
b2 = b' World'
b3 = b1 + b2
print(b3)  # b'Hello World'

# Repetition (*)
print(b'Ha' * 3)  # b'HaHaHa'
print(b'-' * 20)  # b'--------------------'

# In-place? No (immutable)
# b1 += b2  # Creates new object
```

### Membership Testing

```python
b = b'Hello World'

print(b'Hello' in b)     # True
print(b'World' in b)     # True
print(b'Python' in b)    # False
print(b'e' in b)         # True (single byte)

# Check for byte values
print(72 in b)   # True (ASCII 'H')
print(100 in b)  # True (ASCII 'd')
print(255 in b)  # False
```

### Comparison Operators

```python
# Lexicographic comparison
b1 = b'apple'
b2 = b'banana'
b3 = b'apple'

print(b1 == b3)    # True
print(b1 < b2)     # True ('a' < 'b')
print(b1 > b2)     # False

# With different lengths
b4 = b'abc'
b5 = b'abcd'
print(b4 < b5)     # True (shorter is smaller)

# With bytes vs bytes (not strings)
# print(b'5' < b'10')  # True (compares '5' vs '1', not numeric)
```

### Length and Iteration

```python
b = b'Hello'

# Length
print(len(b))  # 5

# Iteration (returns ints)
for byte in b:
    print(byte)  # 72, 101, 108, 108, 111

# Convert to list of ints
print(list(b))  # [72, 101, 108, 108, 111]

# Convert to list of bytes (slicing)
print([b[i:i+1] for i in range(len(b))])  # [b'H', b'e', b'l', b'l', b'o']
```

---

## 🔄 Encoding and Decoding

### String to Bytes (Encoding)

```python
text = "Hello"

# Different encodings
utf8 = text.encode('utf-8')
utf16 = text.encode('utf-16')
utf32 = text.encode('utf-32')
ascii_ignore = text.encode('ascii', errors='ignore')
ascii_replace = text.encode('ascii', errors='replace')

print(f"UTF-8:    {utf8}")
print(f"UTF-16:   {utf16}")
print(f"UTF-32:   {utf32}")
print(f"ASCII (ignore): {ascii_ignore}")
print(f"ASCII (replace): {ascii_replace}")

# Common encodings
encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252']
for enc in encodings:
    try:
        encoded = "Hello".encode(enc)
        print(f"{enc:8}: {encoded}")
    except:
        print(f"{enc:8}: Error")
```

### Bytes to String (Decoding)

```python
# Decode bytes to string
b = b'Hello \xe4\xb8\x96\xe7\x95\x8c'

# Correct decoding
text = b.decode('utf-8')
print(text)  # "Hello"

# Wrong decoding (produces garbage)
text_wrong = b.decode('latin-1')
print(text_wrong)  # "Hello ä¸ç"

# Error handling
try:
    b.decode('ascii')
except UnicodeDecodeError:
    print("Cannot decode as ASCII")

# With error handling
text_ignore = b.decode('ascii', errors='ignore')
text_replace = b.decode('ascii', errors='replace')

print(text_ignore)   # "Hello "
print(text_replace)  # "Hello ���"
```

### Detecting Encoding

```python
import chardet  # Third-party library

def detect_encoding(data):
    """Try to detect encoding of bytes"""
    # Common encodings to try
    encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252']
    
    for enc in encodings:
        try:
            data.decode(enc)
            return enc
        except UnicodeDecodeError:
            continue
    return None

# Test
b = b'Hello \xe4\xb8\x96\xe7\x95\x8c'
detected = detect_encoding(b)
print(f"Detected encoding: {detected}")  # utf-8
```

---

## 🔄 Bytes vs Strings

### Key Differences

```python
# Strings are Unicode, Bytes are raw data
s = 'Hello'
b = b'Hello'

print(type(s))  # <class 'str'>
print(type(b))  # <class 'bytes'>

# Strings have characters, Bytes have integers (0-255)
print(s[0])     # 'H'
print(b[0])     # 72

# Slicing returns same type
print(s[0:2])   # 'He'
print(b[0:2])   # b'He'

# Concatenation works similarly
print(s + ' World')   # 'Hello World'
print(b + b' World')  # b'Hello World'

# Cannot mix types
# print(s + b' World')  # TypeError!
```

### When to Use Which

```python
# ✅ Use str for:
# - Text processing
# - User input/output
# - JSON/XML data
# - Database text fields

# ✅ Use bytes for:
# - File I/O (binary mode)
# - Network communication
# - Cryptography
# - Image/audio/video data
# - Binary protocols
```

### Conversion Between Types

```python
# str → bytes (encode)
text = "Hello"
bytes_data = text.encode('utf-8')
bytes_data = bytes(text, 'utf-8')

# bytes → str (decode)
bytes_data = b'Hello'
text = bytes_data.decode('utf-8')
text = str(bytes_data, 'utf-8')

# With error handling
text = "Hello"
bytes_data = text.encode('ascii', errors='ignore')
text_back = bytes_data.decode('ascii', errors='ignore')
```

---

## 🌍 Real-World Examples

### Example 1: File Reader with Different Modes

```python
class BinaryFileHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def read_as_bytes(self):
        """Read file as bytes"""
        with open(self.filename, 'rb') as f:
            return f.read()
    
    def read_as_hex(self):
        """Read file as hex string"""
        data = self.read_as_bytes()
        return data.hex()
    
    def read_as_hex_dump(self, width=16):
        """Read file as formatted hex dump"""
        data = self.read_as_bytes()
        result = []
        
        for i in range(0, len(data), width):
            chunk = data[i:i+width]
            hex_part = ' '.join(f'{b:02x}' for b in chunk)
            hex_part = hex_part.ljust(width * 3)
            ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
            result.append(f'{i:08x}: {hex_part} {ascii_part}')
        
        return '\n'.join(result)
    
    def search_bytes(self, pattern):
        """Search for byte pattern in file"""
        data = self.read_as_bytes()
        positions = []
        start = 0
        
        while True:
            pos = data.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        
        return positions
    
    def replace_bytes(self, old, new, output_file):
        """Replace bytes and save to new file"""
        data = self.read_as_bytes()
        modified = data.replace(old, new)
        
        with open(output_file, 'wb') as f:
            f.write(modified)
        
        return len(modified) - len(data)

# Create sample file
with open('sample.txt', 'wb') as f:
    f.write(b'Hello World\nThis is a test file.\nHello again!')

# Use the handler
handler = BinaryFileHandler('sample.txt')

print("File as bytes:")
print(handler.read_as_bytes())
print("\nFile as hex:")
print(handler.read_as_hex())
print("\nHex dump:")
print(handler.read_as_hex_dump())

print("\nSearch for 'Hello':")
positions = handler.search_bytes(b'Hello')
print(f"Found at positions: {positions}")

# Replace bytes
handler.replace_bytes(b'Hello', b'Hi', 'modified.txt')
print("\nCreated modified.txt with 'Hello' replaced by 'Hi'")
```

### Example 2: Network Packet Simulator

```python
import struct
import socket

class PacketBuilder:
    @staticmethod
    def build_ip_packet(src_ip, dst_ip, data):
        """Build a simple IP packet"""
        # Convert IP strings to bytes
        src_bytes = socket.inet_aton(src_ip)
        dst_bytes = socket.inet_aton(dst_ip)
        
        # IP header fields
        version_ihl = 0x45  # IPv4, header length 20 bytes
        tos = 0
        total_length = 20 + len(data)  # header + data
        identification = 0x1234
        flags_offset = 0
        ttl = 64
        protocol = 6  # TCP
        checksum = 0  # Would calculate in real implementation
        
        # Pack header
        header = struct.pack('!BBHHHBBH',
            version_ihl, tos, total_length, identification,
            flags_offset, ttl, protocol, checksum)
        
        # Add source and destination IPs
        header += src_bytes + dst_bytes
        
        return header + data
    
    @staticmethod
    def parse_ip_packet(packet):
        """Parse IP packet"""
        # Unpack header
        header = packet[:20]
        version_ihl, tos, total_length, identification, flags_offset, ttl, protocol, checksum = struct.unpack('!BBHHHBBH', header[:12])
        
        src_ip = socket.inet_ntoa(packet[12:16])
        dst_ip = socket.inet_ntoa(packet[16:20])
        data = packet[20:total_length]
        
        return {
            'version': version_ihl >> 4,
            'header_length': (version_ihl & 0x0F) * 4,
            'total_length': total_length,
            'ttl': ttl,
            'protocol': protocol,
            'source_ip': src_ip,
            'destination_ip': dst_ip,
            'data': data
        }

# Build packets
builder = PacketBuilder()

# Create data payloads
data1 = b'Hello, Server!'
data2 = b'GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n'

# Build IP packets
packet1 = builder.build_ip_packet('192.168.1.100', '192.168.1.1', data1)
packet2 = builder.build_ip_packet('10.0.0.5', '8.8.8.8', data2)

print("PACKET 1:")
print(f"Raw packet (first 50 bytes): {packet1[:50]}")
parsed1 = builder.parse_ip_packet(packet1)
for key, value in parsed1.items():
    print(f"  {key}: {value}")

print("\nPACKET 2:")
parsed2 = builder.parse_ip_packet(packet2)
for key, value in parsed2.items():
    print(f"  {key}: {value}")
```

### Example 3: Image Header Parser

```python
class ImageAnalyzer:
    @staticmethod
    def detect_image_type(data):
        """Detect image type from magic bytes"""
        magic_bytes = data[:8]
        
        # Common image signatures
        signatures = {
            b'\x89PNG\r\n\x1a\n': 'PNG',
            b'\xff\xd8\xff': 'JPEG',
            b'GIF87a': 'GIF87',
            b'GIF89a': 'GIF89',
            b'BM': 'BMP',
            b'RIFF': 'WEBP'  # Check further for WEBP
        }
        
        for sig, img_type in signatures.items():
            if magic_bytes.startswith(sig):
                return img_type
        
        return 'Unknown'
    
    @staticmethod
    def parse_png(data):
        """Parse PNG header"""
        if not data.startswith(b'\x89PNG\r\n\x1a\n'):
            return None
        
        # PNG header is 8 bytes
        # IHDR chunk follows
        ihdr = data[8:8+25]  # Length(4) + Type(4) + Data(13) + CRC(4)
        
        width = struct.unpack('>I', ihdr[8:12])[0]
        height = struct.unpack('>I', ihdr[12:16])[0]
        bit_depth = ihdr[16]
        color_type = ihdr[17]
        
        color_types = {
            0: 'Grayscale',
            2: 'RGB',
            3: 'Palette',
            4: 'Grayscale with alpha',
            6: 'RGBA'
        }
        
        return {
            'width': width,
            'height': height,
            'bit_depth': bit_depth,
            'color_type': color_types.get(color_type, 'Unknown'),
            'file_size': len(data)
        }
    
    @staticmethod
    def parse_jpeg(data):
        """Parse JPEG header"""
        if not data.startswith(b'\xff\xd8\xff'):
            return None
        
        # Find SOF0 marker (Start of Frame)
        pos = 2
        while pos < len(data) - 1:
            if data[pos] == 0xFF and data[pos+1] == 0xC0:
                # SOF0 found
                height = struct.unpack('>H', data[pos+5:pos+7])[0]
                width = struct.unpack('>H', data[pos+7:pos+9])[0]
                return {
                    'width': width,
                    'height': height,
                    'file_size': len(data)
                }
            pos += 1
        
        return {'width': 0, 'height': 0, 'file_size': len(data)}

# Create sample image data (simulated)
png_data = (b'\x89PNG\r\n\x1a\n' +  # PNG signature
            b'\x00\x00\x00\x0DIHDR' +  # IHDR chunk
            b'\x00\x00\x01\x00' +  # width 256
            b'\x00\x00\x00\x80' +  # height 128
            b'\x08\x02\x00\x00\x00' +  # bit depth, color type
            b'\x00\x00\x00\x00')  # CRC (simplified)

jpeg_data = (b'\xff\xd8\xff' +  # JPEG SOI
             b'\x00\x00' +  # Some data
             b'\xff\xc0' +  # SOF0 marker
             b'\x00\x11' +  # Length
             b'\x08' +  # Precision
             b'\x00\x80' +  # Height 128
             b'\x01\x00' +  # Width 256
             b'\x03' +  # Components
             b'\x00' * 10)  # Rest of data

analyzer = ImageAnalyzer()

print("PNG ANALYSIS:")
png_type = analyzer.detect_image_type(png_data)
print(f"Type: {png_type}")
png_info = analyzer.parse_png(png_data)
if png_info:
    for key, value in png_info.items():
        print(f"  {key}: {value}")

print("\nJPEG ANALYSIS:")
jpeg_type = analyzer.detect_image_type(jpeg_data)
print(f"Type: {jpeg_type}")
jpeg_info = analyzer.parse_jpeg(jpeg_data)
if jpeg_info:
    for key, value in jpeg_info.items():
        print(f"  {key}: {value}")
```

### Example 4: CRC32 Checksum Calculator

```python
import zlib
import binascii

class ChecksumCalculator:
    @staticmethod
    def crc32(data):
        """Calculate CRC32 checksum"""
        return zlib.crc32(data) & 0xFFFFFFFF
    
    @staticmethod
    def crc32_hex(data):
        """CRC32 as hex string"""
        return f"{ChecksumCalculator.crc32(data):08x}"
    
    @staticmethod
    def adler32(data):
        """Calculate Adler-32 checksum"""
        return zlib.adler32(data) & 0xFFFFFFFF
    
    @staticmethod
    def verify_integrity(original, checksum_func=crc32):
        """Verify data integrity with checksum"""
        original_checksum = checksum_func(original)
        
        def verify(data):
            return checksum_func(data) == original_checksum
        
        return verify
    
    @staticmethod
    def find_corruption(data, verify_func, chunk_size=1024):
        """Find corrupted section in data"""
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            if not verify_func(chunk):
                return i
        return -1

# Create test data
original_data = b'Hello World! This is important data.' * 1000

# Calculate checksums
print("CHECKSUM CALCULATION")
print("=" * 40)
print(f"Original data size: {len(original_data)} bytes")
print(f"CRC32: {ChecksumCalculator.crc32_hex(original_data)}")
print(f"Adler-32: {ChecksumCalculator.adler32(original_data):08x}")

# Verify integrity
verify_crc = ChecksumCalculator.verify_integrity(original_data, ChecksumCalculator.crc32)

# Test with modified data
modified_data = bytearray(original_data)
modified_data[500] = 0xFF  # Corrupt one byte
modified_data = bytes(modified_data)

print(f"\nModified data CRC32: {ChecksumCalculator.crc32_hex(modified_data)}")
print(f"Integrity check passed: {verify_crc(modified_data)}")

# Find corruption
corrupt_pos = ChecksumCalculator.find_corruption(modified_data, verify_crc)
print(f"Corruption detected at position: {corrupt_pos}")

# Real use: File integrity check
def file_checksum(filename):
    """Calculate checksum of file"""
    crc = 0
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            crc = zlib.crc32(chunk, crc)
    return crc & 0xFFFFFFFF

# Create test file
with open('test.dat', 'wb') as f:
    f.write(original_data)

file_crc = file_checksum('test.dat')
print(f"\nFile CRC32: {file_crc:08x}")
print(f"Matches original: {file_crc == ChecksumCalculator.crc32(original_data)}")
```

### Example 5: Protocol Buffer Simulator

```python
import struct

class SimpleProtocol:
    """Simple binary protocol for data transmission"""
    
    # Message types
    MSG_HELLO = 0x01
    MSG_DATA = 0x02
    MSG_GOODBYE = 0x03
    MSG_ERROR = 0xFF
    
    @staticmethod
    def encode_message(msg_type, payload=b''):
        """Encode message to bytes"""
        # Format: [type(1)] [length(4)] [payload]
        length = len(payload)
        header = struct.pack('!BI', msg_type, length)
        return header + payload
    
    @staticmethod
    def decode_message(data):
        """Decode bytes to message"""
        if len(data) < 5:
            raise ValueError("Message too short")
        
        msg_type, length = struct.unpack('!BI', data[:5])
        
        if len(data) < 5 + length:
            raise ValueError("Incomplete message")
        
        payload = data[5:5+length]
        
        return {
            'type': msg_type,
            'type_name': SimpleProtocol.get_type_name(msg_type),
            'length': length,
            'payload': payload
        }
    
    @staticmethod
    def get_type_name(msg_type):
        """Get message type name"""
        names = {
            SimpleProtocol.MSG_HELLO: 'HELLO',
            SimpleProtocol.MSG_DATA: 'DATA',
            SimpleProtocol.MSG_GOODBYE: 'GOODBYE',
            SimpleProtocol.MSG_ERROR: 'ERROR'
        }
        return names.get(msg_type, 'UNKNOWN')
    
    @staticmethod
    def create_hello_message(client_name):
        """Create HELLO message"""
        payload = client_name.encode('utf-8')
        return SimpleProtocol.encode_message(SimpleProtocol.MSG_HELLO, payload)
    
    @staticmethod
    def create_data_message(data):
        """Create DATA message"""
        return SimpleProtocol.encode_message(SimpleProtocol.MSG_DATA, data)
    
    @staticmethod
    def create_goodbye_message():
        """Create GOODBYE message"""
        return SimpleProtocol.encode_message(SimpleProtocol.MSG_GOODBYE)
    
    @staticmethod
    def create_error_message(error_msg):
        """Create ERROR message"""
        payload = error_msg.encode('utf-8')
        return SimpleProtocol.encode_message(SimpleProtocol.MSG_ERROR, payload)

# Simulate communication
print("PROTOCOL SIMULATION")
print("=" * 40)

# Create messages
hello = SimpleProtocol.create_hello_message("Client_Python")
data = SimpleProtocol.create_data_message(b'Hello Server! This is my data.')
data2 = SimpleProtocol.create_data_message(b'Second packet of data.')
goodbye = SimpleProtocol.create_goodbye_message()
error = SimpleProtocol.create_error_message("Invalid operation")

# Simulate sending over network (just printing)
messages = [hello, data, data2, goodbye, error]

for i, msg in enumerate(messages, 1):
    print(f"\nMessage {i}:")
    print(f"  Raw ({len(msg)} bytes): {msg[:20]}...")
    
    decoded = SimpleProtocol.decode_message(msg)
    print(f"  Type: {decoded['type_name']} (0x{decoded['type']:02X})")
    print(f"  Length: {decoded['length']}")
    
    if decoded['payload']:
        try:
            text = decoded['payload'].decode('utf-8')
            print(f"  Payload: {text}")
        except:
            print(f"  Payload (hex): {decoded['payload'].hex()}")

# Simulate packet reassembly
print("\n" + "=" * 40)
print("PACKET REASSEMBLY")

def reassemble_packets(packets):
    """Reassemble fragmented packets"""
    complete = b''
    for packet in packets:
        decoded = SimpleProtocol.decode_message(packet)
        if decoded['type'] == SimpleProtocol.MSG_DATA:
            complete += decoded['payload']
    return complete

fragments = [
    SimpleProtocol.create_data_message(b'Hello '),
    SimpleProtocol.create_data_message(b'World'),
    SimpleProtocol.create_data_message(b'! This '),
    SimpleProtocol.create_data_message(b'is a test.')
]

reassembled = reassemble_packets(fragments)
print(f"Reassembled message: {reassembled.decode('utf-8')}")
```

### Example 6: Binary Search in Bytes

```python
class BinarySearch:
    @staticmethod
    def find_pattern(data, pattern):
        """Find all occurrences of pattern in bytes"""
        positions = []
        start = 0
        
        while True:
            pos = data.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        
        return positions
    
    @staticmethod
    def find_longest_repeated_substring(data):
        """Find longest repeating substring"""
        n = len(data)
        longest = b''
        
        for length in range(1, n // 2 + 1):
            seen = set()
            for i in range(n - length + 1):
                substring = data[i:i+length]
                if substring in seen:
                    if length > len(longest):
                        longest = substring
                else:
                    seen.add(substring)
        
        return longest
    
    @staticmethod
    def find_pattern_with_wildcard(data, pattern, wildcard=b'?'):
        """Find pattern with wildcard bytes"""
        positions = []
        
        # Convert pattern to list for easy comparison
        pattern_list = list(pattern)
        wildcard_positions = [i for i, b in enumerate(pattern_list) if b == wildcard]
        
        for start in range(len(data) - len(pattern) + 1):
            match = True
            for i, p in enumerate(pattern_list):
                if p != wildcard and data[start + i] != p:
                    match = False
                    break
            
            if match:
                positions.append(start)
        
        return positions
    
    @staticmethod
    def extract_byte_ranges(data, ranges):
        """Extract multiple byte ranges"""
        result = []
        for start, end in ranges:
            result.append(data[start:end])
        return result

# Test data
test_data = b'Hello Hello Hello World Hello Python Hello World'

print("BINARY SEARCH EXAMPLES")
print("=" * 40)

# Find pattern
pattern = b'Hello'
positions = BinarySearch.find_pattern(test_data, pattern)
print(f"Pattern '{pattern}' found at: {positions}")
print(f"Occurrences: {len(positions)}")

# Find longest repeating substring
longest = BinarySearch.find_longest_repeated_substring(test_data)
print(f"\nLongest repeating substring: '{longest}' ({len(longest)} bytes)")

# Wildcard search
data = b'abcXdefYabcZdef'
pattern = b'a?c'  # ? is wildcard
matches = BinarySearch.find_pattern_with_wildcard(data, pattern)
print(f"\nWildcard pattern '{pattern}' found at: {matches}")
for pos in matches:
    print(f"  Match: {data[pos:pos+3]}")

# Extract ranges
ranges = [(0, 5), (6, 11), (12, 17)]
extracted = BinarySearch.extract_byte_ranges(test_data, ranges)
print(f"\nExtracted ranges: {extracted}")

# Real use: DNA sequence search
dna = b'ATCGATCGATCGATCG'
pattern = b'ATCG'
positions = BinarySearch.find_pattern(dna, pattern)
print(f"\nDNA pattern '{pattern.decode()}' found at: {positions}")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Mixing Bytes and Strings

```python
# ❌ WRONG - Cannot mix bytes and strings
text = "Hello"
binary = b'World'
# result = text + binary  # TypeError!

# ✅ CORRECT - Convert to same type
result = text + binary.decode('utf-8')  # 'HelloWorld'
result = text.encode('utf-8') + binary  # b'HelloWorld'
```

### Pitfall 2: Index Returns Integer, Not Bytes

```python
b = b'Hello'

# ❌ WRONG - Index returns int
char = b[0]  # 72, not b'H'

# ✅ CORRECT - Slice to get single byte
char = b[0:1]  # b'H'

# ✅ CORRECT - Convert to string for character
char = chr(b[0])  # 'H'
```

### Pitfall 3: Modifying Bytes (Impossible)

```python
# ❌ WRONG - Bytes are immutable
b = b'Hello'
# b[0] = 74  # TypeError!

# ✅ CORRECT - Create new bytes
b = b'J' + b[1:]  # b'Jello'

# ✅ CORRECT - Use bytearray for mutable
ba = bytearray(b'Hello')
ba[0] = 74  # Works!
```

### Pitfall 4: Encoding Errors

```python
text = "Hello"

# ❌ WRONG - ASCII can't encode non-ASCII
# b = text.encode('ascii')  # UnicodeEncodeError!

# ✅ CORRECT - Use UTF-8 for Unicode
b = text.encode('utf-8')

# ✅ CORRECT - Handle errors
b = text.encode('ascii', errors='ignore')   # b'Hello '
b = text.encode('ascii', errors='replace')  # b'Hello ??'
```

---

## ⚡ Performance Tips

### Bytes Are More Efficient Than Strings for Binary Data

```python
import sys
import timeit

# Memory efficiency
text = "Hello World" * 1000
binary = b'Hello World' * 1000

print(f"String memory: {sys.getsizeof(text)} bytes")
print(f"Bytes memory: {sys.getsizeof(binary)} bytes")

# Processing speed
def process_string(s):
    return s.upper()

def process_bytes(b):
    return b.upper()

str_time = timeit.timeit('process_string(text)', globals=globals(), number=10000)
bytes_time = timeit.timeit('process_bytes(binary)', globals=globals(), number=10000)

print(f"String time: {str_time:.4f}s")
print(f"Bytes time: {bytes_time:.4f}s")
```

### Use Memoryview for Large Data

```python
# For large data, memoryview avoids copying
large_data = b'x' * 10000000

# Slicing creates copy
slice_copy = large_data[1000:2000]  # Copies 1000 bytes

# memoryview creates view (no copy)
view = memoryview(large_data)
slice_view = view[1000:2000]  # No copy!
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Bytes to Hex Converter**
   ```python
   # Convert bytes to hex string with spaces
   # Example: b'Hello' → '48 65 6c 6c 6f'
   ```

2. **ASCII Checker**
   ```python
   # Check if all bytes in data are printable ASCII (32-126)
   ```

3. **Byte Counter**
   ```python
   # Count occurrences of each byte value (0-255) in data
   ```

### Intermediate Level

4. **XOR Cipher**
   ```python
   # Implement XOR encryption/decryption for bytes
   # cipher = bytes([b ^ key for b in data])
   ```

5. **Base64 Encoder**
   ```python
   # Implement simple Base64 encoding without using base64 module
   ```

6. **Binary File Splitter**
   ```python
   # Split binary file into chunks of specified size
   ```

### Advanced Level

7. **PNG Chunk Parser**
   ```python
   # Parse PNG file and extract all chunks (IHDR, IDAT, IEND)
   ```

8. **Bit Manipulator**
   ```python
   # Extract specific bits from bytes (e.g., get bits 3-7)
   ```

9. **Protocol Parser**
   ```python
   # Implement parser for custom binary protocol with variable-length fields
   ```

---

## 📚 Quick Reference Card

```python
# Creation
b = b'hello'                    # Literal
b = bytes([72, 101, 108])       # From list
b = bytes(10)                   # Zero-filled
b = bytes.fromhex('48656c6c6f') # From hex

# Methods
b.upper()                       # Uppercase
b.lower()                       # Lowercase
b.find(sub)                     # Find position
b.count(sub)                    # Count occurrences
b.split(sep)                    # Split
b.join(iterable)                # Join
b.replace(old, new)             # Replace
b.strip()                       # Strip whitespace
b.hex()                         # To hex string
b.isalpha()                     # Check alphabetic
b.isdigit()                     # Check digits

# Operations
len(b)                          # Length
b[0]                            # Index (returns int)
b[0:5]                          # Slice (returns bytes)
b1 + b2                         # Concatenation
b * 3                           # Repetition
sub in b                        # Membership

# Encoding/Decoding
text.encode('utf-8')            # str → bytes
b.decode('utf-8')               # bytes → str

# Conversion
bytes.fromhex(hex_str)          # Hex → bytes
list(b)                         # Bytes → list of ints
```

## Next Step

- Move to [02_bytearray.md](02_bytearray.md) for understanding Bytearray Data Type.

---

*Master bytes for efficient binary data handling! 🐍✨*
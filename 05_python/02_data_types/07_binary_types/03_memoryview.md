# 📘 MEMORYVIEW – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Memoryview?](#what-is-memoryview)
2. [Creating Memoryview](#creating-memoryview)
3. [Memoryview Operations](#memoryview-operations)
4. [Casting Memoryview](#casting-memoryview)
5. [Real-World Examples](#real-world-examples)
6. [Common Pitfalls](#common-pitfalls)
7. [Performance Tips](#performance-tips)
8. [Practice Exercises](#practice-exercises)

---

## What is Memoryview?

**Memoryview** is a built-in type that provides a view of another object's memory without copying the data. It's useful for working with large binary data efficiently.

```python
# Examples of memoryview
data = bytearray(b'hello world')
view = memoryview(data)

print(type(view))     # <class 'memoryview'>
print(view[0])        # 104 (ASCII 'h')
print(view[0:5].tobytes())  # b'hello'

# Modify through view
view[0] = 72  # Change 'h' to 'H'
print(data)   # bytearray(b'Hello world')
```

**Key Features:**
- Zero-copy access to underlying data
- Supports indexing and slicing
- Can cast to different formats
- Memory efficient for large data
- Supports buffer protocol
- Can be used with numpy, PIL, etc.

---

## Creating Memoryview

### From Bytes and Bytearray

```python
# From bytes (read-only view)
b = b'hello world'
view = memoryview(b)
print(view.readonly)  # True (cannot modify)
# view[0] = 72  # TypeError!

# From bytearray (mutable view)
ba = bytearray(b'hello world')
view = memoryview(ba)
print(view.readonly)  # False (can modify)
view[0] = 72  # Works
print(ba)     # bytearray(b'Hello world')
```

### From Other Buffer Objects

```python
# From array module
import array
arr = array.array('i', [1, 2, 3, 4])
view = memoryview(arr)
print(view[0])    # 1
view[1] = 99
print(arr)        # array('i', [1, 99, 3, 4])

# From numpy array (if installed)
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# view = memoryview(arr)

# From PIL Image (if installed)
# from PIL import Image
# img = Image.open('photo.jpg')
# view = memoryview(img.tobytes())
```

---

## Memoryview Operations

### Indexing and Slicing

```python
data = bytearray(b'Python Programming')
view = memoryview(data)

# Indexing (returns int)
print(view[0])      # 80 (ASCII 'P')
print(view[-1])     # 103 (ASCII 'g')

# Slicing (returns new memoryview)
slice_view = view[0:6]
print(slice_view.tobytes())  # b'Python'

# Step slicing
print(view[::2].tobytes())   # b'Pto rgamn'
print(view[::-1].tobytes())  # b'gnimmargorP nohtyP'

# Modify through slice view
slice_view = view[7:18]
slice_view[:] = b'PROGRAMMING'
print(data)  # bytearray(b'Python PROGRAMMING')
```

### Properties

```python
data = bytearray(b'hello')
view = memoryview(data)

# Basic properties
print(len(view))           # 5
print(view.itemsize)       # 1 (bytes)
print(view.format)         # 'B' (unsigned char)
print(view.ndim)           # 1 (one-dimensional)
print(view.shape)          # (5,)
print(view.strides)        # (1,)
print(view.readonly)       # False
print(view.nbytes)         # 5 (total bytes)

# For multi-dimensional
arr = array.array('i', [1, 2, 3, 4])
view = memoryview(arr)
print(view.itemsize)       # 4 (integers are 4 bytes)
print(view.format)         # 'i' (signed integer)
```

### Methods

#### `tobytes()`
Returns the data as a bytes object.

```python
view = memoryview(b'hello')
b = view.tobytes()
print(b)          # b'hello'
print(type(b))    # <class 'bytes'>

# tobytes copies the data
view = memoryview(bytearray(b'hello'))
b = view.tobytes()
print(b)          # b'hello'
```

#### `tolist()`
Returns the data as a list of integers.

```python
view = memoryview(b'hello')
lst = view.tolist()
print(lst)  # [104, 101, 108, 108, 111]

# For multi-byte elements
arr = array.array('i', [1000, 2000, 3000])
view = memoryview(arr)
print(view.tolist())  # [1000, 2000, 3000]
```

#### `hex()`
Returns the data as a hex string.

```python
view = memoryview(b'hello')
print(view.hex())        # '68656c6c6f'
print(view.hex(' '))     # '68 65 6c 6c 6f'
print(view.hex(':', 2))  # '68:65:6c:6c:6f'
```

#### `cast()`
Casts the memoryview to a different format.

```python
# Cast bytes to integers
data = bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00')
view = memoryview(data)
int_view = view.cast('i')  # Cast to signed integers (4 bytes each)

print(len(int_view))       # 2
print(int_view[0])         # 1
print(int_view[1])         # 2

# Modify through cast view
int_view[0] = 100
print(data)  # bytearray(b'd\x00\x00\x00\x02\x00\x00\x00')
```

#### `release()`
Releases the underlying buffer.

```python
view = memoryview(b'hello')
view.release()

# After release, view is unusable
try:
    view[0]
except ValueError:
    print("View is released")
```

---

## Casting Memoryview

### Basic Casting

```python
# Create 8 bytes of data
data = bytearray([1, 0, 0, 0, 2, 0, 0, 0])
view = memoryview(data)

# Cast to different types
int_view = view.cast('i')      # Signed integer (4 bytes)
uint_view = view.cast('I')     # Unsigned integer (4 bytes)
short_view = view.cast('h')    # Signed short (2 bytes)
ushort_view = view.cast('H')   # Unsigned short (2 bytes)
char_view = view.cast('b')     # Signed char (1 byte)

print(f"Original: {view.tolist()}")
print(f"As int: {int_view.tolist()}")
print(f"As short: {short_view.tolist()}")
print(f"As char: {char_view.tolist()}")
```

### Format Codes

```python
# Format codes for cast()
format_codes = {
    'b': 'signed char (1 byte)',
    'B': 'unsigned char (1 byte)',
    'h': 'signed short (2 bytes)',
    'H': 'unsigned short (2 bytes)',
    'i': 'signed int (4 bytes)',
    'I': 'unsigned int (4 bytes)',
    'l': 'signed long (4/8 bytes)',
    'L': 'unsigned long (4/8 bytes)',
    'q': 'signed long long (8 bytes)',
    'Q': 'unsigned long long (8 bytes)',
    'f': 'float (4 bytes)',
    'd': 'double (8 bytes)'
}

for code, desc in format_codes.items():
    print(f"{code}: {desc}")
```

### Multi-dimensional Casting

```python
# Create 2x2 matrix of integers
data = bytearray([1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0])
view = memoryview(data)

# Cast to 2x2 integer matrix
matrix = view.cast('i', shape=(2, 2))
print(f"Shape: {matrix.shape}")
print(f"NDim: {matrix.ndim}")
print(f"Itemsize: {matrix.itemsize}")

# Access as 2D
print(f"matrix[0][0] = {matrix[0][0]}")  # 1
print(f"matrix[0][1] = {matrix[0][1]}")  # 2
print(f"matrix[1][0] = {matrix[1][0]}")  # 3
print(f"matrix[1][1] = {matrix[1][1]}")  # 4

# Modify through 2D view
matrix[0][0] = 99
print(data[:4])  # b'c\x00\x00\x00' (99)
```

### 3D Casting

```python
# Create 3D RGB image data (2x2 pixels, 3 channels)
# R,G,B for each pixel
data = bytearray([
    255, 0, 0,    # Pixel (0,0): Red
    0, 255, 0,    # Pixel (0,1): Green
    0, 0, 255,    # Pixel (1,0): Blue
    255, 255, 0   # Pixel (1,1): Yellow
])

# Cast to 2x2x3 array
view = memoryview(data)
rgb_image = view.cast('B', shape=(2, 2, 3))

print(f"Shape: {rgb_image.shape}")
print(f"Total pixels: {rgb_image.shape[0] * rgb_image.shape[1]}")

# Access pixel values
print(f"Pixel (0,0): R={rgb_image[0][0][0]}, G={rgb_image[0][0][1]}, B={rgb_image[0][0][2]}")
print(f"Pixel (0,1): R={rgb_image[0][1][0]}, G={rgb_image[0][1][1]}, B={rgb_image[0][1][2]}")
print(f"Pixel (1,0): R={rgb_image[1][0][0]}, G={rgb_image[1][0][1]}, B={rgb_image[1][0][2]}")
print(f"Pixel (1,1): R={rgb_image[1][1][0]}, G={rgb_image[1][1][1]}, B={rgb_image[1][1][2]}")

# Modify a pixel
rgb_image[0][0] = [0, 255, 0]  # Change to green
print(f"After modification: Pixel (0,0): R={rgb_image[0][0][0]}, G={rgb_image[0][0][1]}, B={rgb_image[0][0][2]}")
```

---

## Real-World Examples

### Example 1: Zero-Copy Image Processing

```python
class ImageProcessor:
    def __init__(self, width, height, channels=3):
        self.width = width
        self.height = height
        self.channels = channels
        self.data = bytearray(width * height * channels)
        self.view = memoryview(self.data).cast('B', shape=(height, width, channels))
    
    def set_pixel(self, x, y, r, g, b):
        """Set pixel color (RGB)"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.view[y][x][0] = r
            self.view[y][x][1] = g
            self.view[y][x][2] = b
    
    def get_pixel(self, x, y):
        """Get pixel color"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return tuple(self.view[y][x])
        return None
    
    def fill_rect(self, x, y, w, h, r, g, b):
        """Fill rectangle with color"""
        for i in range(max(0, y), min(self.height, y + h)):
            for j in range(max(0, x), min(self.width, x + w)):
                self.view[i][j][0] = r
                self.view[i][j][1] = g
                self.view[i][j][2] = b
    
    def invert(self):
        """Invert all colors"""
        for i in range(self.height):
            for j in range(self.width):
                self.view[i][j][0] = 255 - self.view[i][j][0]
                self.view[i][j][1] = 255 - self.view[i][j][1]
                self.view[i][j][2] = 255 - self.view[i][j][2]
    
    def grayscale(self):
        """Convert to grayscale"""
        for i in range(self.height):
            for j in range(self.width):
                r, g, b = self.view[i][j]
                gray = int(r * 0.299 + g * 0.587 + b * 0.114)
                self.view[i][j][0] = gray
                self.view[i][j][1] = gray
                self.view[i][j][2] = gray
    
    def to_bytes(self):
        """Get raw bytes"""
        return bytes(self.data)
    
    def display_ascii(self):
        """Display image as ASCII (using brightness)"""
        for i in range(self.height):
            line = ''
            for j in range(self.width):
                brightness = sum(self.view[i][j]) / 3
                if brightness > 200:
                    line += '@'
                elif brightness > 150:
                    line += '#'
                elif brightness > 100:
                    line += '*'
                elif brightness > 50:
                    line += '.'
                else:
                    line += ' '
            print(line)

# Usage
img = ImageProcessor(20, 10)

# Draw shapes
img.fill_rect(0, 0, 20, 10, 50, 50, 50)  # Gray background
img.fill_rect(5, 2, 10, 6, 255, 0, 0)    # Red rectangle
img.fill_rect(8, 4, 4, 2, 0, 255, 0)     # Green square

# Set individual pixels
img.set_pixel(10, 5, 0, 0, 255)  # Blue pixel

print("ASCII Representation:")
img.display_ascii()

print(f"\nImage size: {len(img.to_bytes())} bytes")
print(f"First 20 bytes: {img.to_bytes()[:20]}")
```

### Example 2: Audio Buffer Processing

```python
import array
import math

class AudioBuffer:
    def __init__(self, samples, sample_rate=44100):
        self.sample_rate = sample_rate
        self.data = array.array('h', samples)  # Signed short (16-bit audio)
        self.view = memoryview(self.data).cast('h')
    
    @classmethod
    def sine_wave(cls, frequency, duration, sample_rate=44100, amplitude=32767):
        """Generate sine wave"""
        num_samples = int(sample_rate * duration)
        samples = []
        for i in range(num_samples):
            t = i / sample_rate
            value = int(amplitude * math.sin(2 * math.pi * frequency * t))
            samples.append(value)
        return cls(samples, sample_rate)
    
    def apply_gain(self, factor):
        """Apply gain (volume change)"""
        for i in range(len(self.view)):
            self.view[i] = int(self.view[i] * factor)
    
    def apply_fade_in(self, duration_ms):
        """Apply fade-in effect"""
        fade_samples = int(self.sample_rate * duration_ms / 1000)
        for i in range(min(fade_samples, len(self.view))):
            factor = i / fade_samples
            self.view[i] = int(self.view[i] * factor)
    
    def apply_fade_out(self, duration_ms):
        """Apply fade-out effect"""
        fade_samples = int(self.sample_rate * duration_ms / 1000)
        start = max(0, len(self.view) - fade_samples)
        for i in range(start, len(self.view)):
            factor = (len(self.view) - i) / fade_samples
            self.view[i] = int(self.view[i] * factor)
    
    def mix(self, other, position=0):
        """Mix another audio buffer at position"""
        for i in range(min(len(other.view), len(self.view) - position)):
            self.view[position + i] = (self.view[position + i] + other.view[i]) // 2
    
    def normalize(self):
        """Normalize audio to maximum amplitude"""
        max_val = max(abs(s) for s in self.view)
        if max_val > 0:
            factor = 32767 / max_val
            self.apply_gain(factor)
    
    def get_peak(self):
        """Get peak amplitude"""
        return max(abs(s) for s in self.view)
    
    def get_rms(self):
        """Get RMS (Root Mean Square) amplitude"""
        if len(self.view) == 0:
            return 0
        sum_squares = sum(s * s for s in self.view)
        return math.sqrt(sum_squares / len(self.view))
    
    def to_bytes(self):
        """Convert to bytes"""
        return self.data.tobytes()

# Usage
print("AUDIO BUFFER PROCESSING")
print("=" * 40)

# Generate sine waves
tone_440 = AudioBuffer.sine_wave(440, 1.0)  # A4 note
tone_880 = AudioBuffer.sine_wave(880, 1.0)  # A5 note

print(f"Tone 440Hz - Peak: {tone_440.get_peak()}, RMS: {tone_440.get_rms():.0f}")
print(f"Tone 880Hz - Peak: {tone_880.get_peak()}, RMS: {tone_880.get_rms():.0f}")

# Mix tones
tone_440.mix(tone_880)
print(f"\nAfter mixing - Peak: {tone_440.get_peak()}, RMS: {tone_440.get_rms():.0f}")

# Apply effects
tone_440.apply_gain(0.5)
print(f"After gain (0.5) - Peak: {tone_440.get_peak()}, RMS: {tone_440.get_rms():.0f}")

tone_440.apply_fade_in(100)   # 100ms fade in
tone_440.apply_fade_out(100)  # 100ms fade out
print(f"After fades - Peak: {tone_440.get_peak()}, RMS: {tone_440.get_rms():.0f}")

tone_440.normalize()
print(f"After normalization - Peak: {tone_440.get_peak()}, RMS: {tone_440.get_rms():.0f}")

# Output size
print(f"\nAudio data size: {len(tone_440.to_bytes())} bytes")
```

### Example 3: Network Packet Inspector

```python
import struct
import socket
from datetime import datetime

class PacketInspector:
    def __init__(self, packet_data):
        self.data = bytearray(packet_data)
        self.view = memoryview(self.data)
    
    def parse_ethernet(self):
        """Parse Ethernet frame header"""
        if len(self.view) < 14:
            return None
        
        dest_mac = ':'.join(f'{b:02x}' for b in self.view[0:6])
        src_mac = ':'.join(f'{b:02x}' for b in self.view[6:12])
        eth_type = struct.unpack('!H', self.view[12:14])[0]
        
        return {
            'destination_mac': dest_mac,
            'source_mac': src_mac,
            'type': f'0x{eth_type:04x}',
            'type_name': 'IPv4' if eth_type == 0x0800 else 'IPv6' if eth_type == 0x86DD else 'Unknown'
        }
    
    def parse_ip(self, offset=14):
        """Parse IP header"""
        if len(self.view) < offset + 20:
            return None
        
        version_ihl = self.view[offset]
        version = version_ihl >> 4
        ihl = (version_ihl & 0x0F) * 4
        
        tos = self.view[offset + 1]
        total_length = struct.unpack('!H', self.view[offset + 2:offset + 4])[0]
        identification = struct.unpack('!H', self.view[offset + 4:offset + 6])[0]
        flags_offset = struct.unpack('!H', self.view[offset + 6:offset + 8])[0]
        ttl = self.view[offset + 8]
        protocol = self.view[offset + 9]
        checksum = struct.unpack('!H', self.view[offset + 10:offset + 12])[0]
        src_ip = socket.inet_ntoa(self.view[offset + 12:offset + 16])
        dst_ip = socket.inet_ntoa(self.view[offset + 16:offset + 20])
        
        protocols = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        
        return {
            'version': version,
            'header_length': ihl,
            'tos': tos,
            'total_length': total_length,
            'identification': identification,
            'ttl': ttl,
            'protocol': protocol,
            'protocol_name': protocols.get(protocol, 'Unknown'),
            'source_ip': src_ip,
            'destination_ip': dst_ip,
            'checksum': f'0x{checksum:04x}'
        }
    
    def parse_tcp(self, offset):
        """Parse TCP header"""
        if len(self.view) < offset + 20:
            return None
        
        src_port = struct.unpack('!H', self.view[offset:offset + 2])[0]
        dst_port = struct.unpack('!H', self.view[offset + 2:offset + 4])[0]
        seq_num = struct.unpack('!I', self.view[offset + 4:offset + 8])[0]
        ack_num = struct.unpack('!I', self.view[offset + 8:offset + 12])[0]
        offset_res = self.view[offset + 12]
        tcp_offset = (offset_res >> 4) * 4
        flags = self.view[offset + 13]
        
        flag_names = []
        if flags & 0x01: flag_names.append('FIN')
        if flags & 0x02: flag_names.append('SYN')
        if flags & 0x04: flag_names.append('RST')
        if flags & 0x08: flag_names.append('PSH')
        if flags & 0x10: flag_names.append('ACK')
        if flags & 0x20: flag_names.append('URG')
        
        window = struct.unpack('!H', self.view[offset + 14:offset + 16])[0]
        checksum = struct.unpack('!H', self.view[offset + 16:offset + 18])[0]
        
        return {
            'source_port': src_port,
            'destination_port': dst_port,
            'sequence_number': seq_num,
            'acknowledgment_number': ack_num,
            'header_length': tcp_offset,
            'flags': flag_names,
            'window_size': window,
            'checksum': f'0x{checksum:04x}'
        }
    
    def inspect(self):
        """Inspect full packet"""
        print("=" * 50)
        print("PACKET INSPECTION")
        print("=" * 50)
        print(f"Packet size: {len(self.view)} bytes")
        
        # Ethernet
        eth = self.parse_ethernet()
        if eth:
            print(f"\n[Ethernet]")
            print(f"  Dest MAC: {eth['destination_mac']}")
            print(f"  Src MAC: {eth['source_mac']}")
            print(f"  Type: {eth['type']} ({eth['type_name']})")
        
        # IP
        ip = self.parse_ip()
        if ip:
            print(f"\n[IP]")
            print(f"  Version: {ip['version']}")
            print(f"  Header Length: {ip['header_length']} bytes")
            print(f"  TTL: {ip['ttl']}")
            print(f"  Protocol: {ip['protocol_name']} ({ip['protocol']})")
            print(f"  Source: {ip['source_ip']}")
            print(f"  Destination: {ip['destination_ip']}")
        
        # TCP/UDP
        if ip and ip['protocol'] == 6:  # TCP
            tcp = self.parse_tcp(14 + ip['header_length'])
            if tcp:
                print(f"\n[TCP]")
                print(f"  Source Port: {tcp['source_port']}")
                print(f"  Dest Port: {tcp['destination_port']}")
                print(f"  Seq Num: {tcp['sequence_number']}")
                print(f"  Flags: {', '.join(tcp['flags'])}")
                print(f"  Window: {tcp['window_size']}")

# Create sample packet (simplified)
def create_sample_packet():
    # Ethernet header (14 bytes)
    ethernet = (
        b'\xff\xff\xff\xff\xff\xff' +  # Dest MAC (broadcast)
        b'\x00\x11\x22\x33\x44\x55' +  # Src MAC
        b'\x08\x00'                     # Type: IPv4
    )
    
    # IP header (20 bytes)
    ip_header = struct.pack('!BBHHHBBH4s4s',
        0x45,           # Version (4) + IHL (5)
        0,              # TOS
        60,             # Total length
        0x1234,         # Identification
        0,              # Flags + Offset
        64,             # TTL
        6,              # Protocol (TCP)
        0,              # Checksum (placeholder)
        socket.inet_aton('192.168.1.100'),  # Source IP
        socket.inet_aton('8.8.8.8')         # Dest IP
    )
    
    # TCP header (20 bytes)
    tcp_header = struct.pack('!HHIIBBHHH',
        12345,          # Source port
        80,             # Dest port (HTTP)
        0x12345678,     # Sequence number
        0,              # Acknowledgment number
        0x50,           # Data offset (5) + reserved
        0x02,           # Flags (SYN)
        8192,           # Window size
        0,              # Checksum
        0               # Urgent pointer
    )
    
    return ethernet + ip_header + tcp_header

# Inspect packet
packet = create_sample_packet()
inspector = PacketInspector(packet)
inspector.inspect()
```

### Example 4: Large File Viewer with Memoryview

```python
import mmap
import os

class LargeFileViewer:
    def __init__(self, filename):
        self.filename = filename
        self.file_size = os.path.getsize(filename)
    
    def view_chunk(self, offset, size):
        """View a chunk of file without loading entire file"""
        with open(self.filename, 'rb') as f:
            f.seek(offset)
            data = f.read(size)
            return memoryview(data)
    
    def search_pattern(self, pattern, chunk_size=1024*1024):
        """Search for pattern using memoryview"""
        positions = []
        pattern_bytes = pattern if isinstance(pattern, bytes) else pattern.encode()
        
        with open(self.filename, 'rb') as f:
            overlap = len(pattern_bytes)
            prev_chunk = b''
            
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                
                # Combine with previous chunk for overlap
                search_data = prev_chunk + chunk
                view = memoryview(search_data)
                
                # Search in this chunk
                start = 0
                while True:
                    pos = view.find(pattern_bytes, start)
                    if pos == -1:
                        break
                    
                    absolute_pos = f.tell() - len(chunk) + pos - len(prev_chunk)
                    positions.append(absolute_pos)
                    start = pos + 1
                
                prev_chunk = chunk[-overlap:] if len(chunk) >= overlap else chunk
        
        return positions
    
    def extract_region(self, start, end):
        """Extract region without copying entire file"""
        size = end - start
        with open(self.filename, 'rb') as f:
            f.seek(start)
            return memoryview(f.read(size))
    
    def hex_dump_region(self, start, length=256):
        """Generate hex dump of region"""
        data = self.extract_region(start, start + length)
        result = []
        
        for i in range(0, len(data), 16):
            chunk = data[i:i+16]
            hex_part = ' '.join(f'{b:02x}' for b in chunk)
            hex_part = hex_part.ljust(48)
            ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
            result.append(f'{start + i:08x}: {hex_part} {ascii_part}')
        
        return '\n'.join(result)

# Create a test file
with open('test_large.bin', 'wb') as f:
    f.write(b'Hello ' * 1000)
    f.write(b'WORLD ' * 1000)
    f.write(b'Python ' * 1000)

# Use the viewer
viewer = LargeFileViewer('test_large.bin')
print(f"File size: {viewer.file_size} bytes")

# Search for pattern
positions = viewer.search_pattern(b'WORLD')
print(f"Found 'WORLD' at positions: {positions[:5]}...")

# Extract region
region = viewer.extract_region(5000, 5100)
print(f"\nExtracted region size: {len(region)} bytes")
print(f"First 50 bytes: {region[:50].tobytes()}")

# Hex dump
print("\nHex dump of region 5000-5256:")
print(viewer.hex_dump_region(5000, 256))

# Clean up
os.remove('test_large.bin')
```

### Example 5: Matrix Operations with Memoryview

```python
class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = bytearray(rows * cols * 4)  # 4 bytes per float
        else:
            self.data = bytearray(data)
        self.view = memoryview(self.data).cast('f', shape=(rows, cols))
    
    @classmethod
    def zeros(cls, rows, cols):
        return cls(rows, cols)
    
    @classmethod
    def ones(cls, rows, cols):
        mat = cls(rows, cols)
        for i in range(rows):
            for j in range(cols):
                mat.view[i][j] = 1.0
        return mat
    
    @classmethod
    def identity(cls, size):
        mat = cls(size, size)
        for i in range(size):
            mat.view[i][i] = 1.0
        return mat
    
    def __getitem__(self, idx):
        return self.view[idx]
    
    def __setitem__(self, idx, value):
        self.view[idx] = value
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.view[i][j] = self.view[i][j] + other.view[i][j]
        return result
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Scalar multiplication
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.view[i][j] = self.view[i][j] * other
            return result
        elif isinstance(other, Matrix):
            # Matrix multiplication
            if self.cols != other.rows:
                raise ValueError("Matrix dimensions incompatible for multiplication")
            
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    total = 0.0
                    for k in range(self.cols):
                        total += self.view[i][k] * other.view[k][j]
                    result.view[i][j] = total
            return result
        
        raise TypeError("Unsupported operand type")
    
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.view[j][i] = self.view[i][j]
        return result
    
    def to_list(self):
        return [[self.view[i][j] for j in range(self.cols)] for i in range(self.rows)]
    
    def __str__(self):
        result = []
        for i in range(self.rows):
            row = ' '.join(f'{self.view[i][j]:6.2f}' for j in range(self.cols))
            result.append(row)
        return '\n'.join(result)

# Usage
print("MATRIX OPERATIONS WITH MEMORYVIEW")
print("=" * 50)

# Create matrices
A = Matrix.identity(3)
B = Matrix.ones(3, 3)
C = Matrix.zeros(2, 3)
C[0][0] = 1
C[0][1] = 2
C[0][2] = 3
C[1][0] = 4
C[1][1] = 5
C[1][2] = 6

print("Matrix A (Identity):")
print(A)
print("\nMatrix B (Ones):")
print(B)
print("\nMatrix C:")
print(C)

# Operations
print("\nA + B:")
print(A + B)

print("\nB * 2 (Scalar multiplication):")
print(B * 2)

print("\nC * C.T (Matrix multiplication):")
print(C * C.transpose())

print("\nC.T:")
print(C.transpose())
```

### Example 6: Binary Data Stream Processor

```python
class DataStreamProcessor:
    def __init__(self, data):
        self.data = bytearray(data)
        self.view = memoryview(self.data)
        self.position = 0
    
    def read_uint8(self):
        """Read unsigned 8-bit integer"""
        if self.position + 1 > len(self.view):
            raise EOFError("End of stream")
        value = self.view[self.position]
        self.position += 1
        return value
    
    def read_uint16(self, little_endian=True):
        """Read unsigned 16-bit integer"""
        if self.position + 2 > len(self.view):
            raise EOFError("End of stream")
        
        if little_endian:
            value = self.view[self.position] | (self.view[self.position + 1] << 8)
        else:
            value = (self.view[self.position] << 8) | self.view[self.position + 1]
        
        self.position += 2
        return value
    
    def read_uint32(self, little_endian=True):
        """Read unsigned 32-bit integer"""
        if self.position + 4 > len(self.view):
            raise EOFError("End of stream")
        
        value = 0
        for i in range(4):
            if little_endian:
                value |= self.view[self.position + i] << (i * 8)
            else:
                value |= self.view[self.position + i] << ((3 - i) * 8)
        
        self.position += 4
        return value
    
    def read_bytes(self, length):
        """Read bytes"""
        if self.position + length > len(self.view):
            raise EOFError("End of stream")
        
        result = bytes(self.view[self.position:self.position + length])
        self.position += length
        return result
    
    def read_string(self, length=None):
        """Read null-terminated or fixed-length string"""
        if length is None:
            # Read until null terminator
            end = self.position
            while end < len(self.view) and self.view[end] != 0:
                end += 1
            result = self.view[self.position:end].tobytes().decode('utf-8')
            self.position = end + 1  # Skip null terminator
            return result
        else:
            result = self.view[self.position:self.position + length].tobytes().decode('utf-8')
            self.position += length
            return result.rstrip('\x00')
    
    def peek(self, offset=0):
        """Peek at next byte without consuming"""
        if self.position + offset >= len(self.view):
            return None
        return self.view[self.position + offset]
    
    def skip(self, bytes_count):
        """Skip bytes"""
        self.position += bytes_count
    
    def remaining(self):
        """Get remaining bytes"""
        return len(self.view) - self.position
    
    def has_more(self):
        """Check if more data available"""
        return self.position < len(self.view)

# Create sample data
def create_sample_data():
    data = bytearray()
    
    # Write header
    data.extend(b'MAGIC')
    data.append(0)  # Null terminator
    
    # Write version (uint32)
    data.extend((1).to_bytes(4, 'little'))
    
    # Write count (uint16)
    data.extend((3).to_bytes(2, 'little'))
    
    # Write records
    records = [
        (b'Alice', 25, 5.5),
        (b'Bob', 30, 4.2),
        (b'Charlie', 35, 3.8)
    ]
    
    for name, age, score in records:
        # Name length (uint8)
        data.append(len(name))
        # Name bytes
        data.extend(name)
        # Age (uint8)
        data.append(age)
        # Score (float - 4 bytes)
        data.extend(struct.pack('f', score))
    
    return data

import struct

# Process the data
sample_data = create_sample_data()
print(f"Sample data size: {len(sample_data)} bytes")
print(f"Hex dump: {sample_data.hex()}\n")

processor = DataStreamProcessor(sample_data)

print("PARSING BINARY STREAM")
print("=" * 40)

# Read magic header
magic = processor.read_string()
print(f"Magic: {magic}")

# Read version
version = processor.read_uint32(little_endian=True)
print(f"Version: {version}")

# Read record count
count = processor.read_uint16(little_endian=True)
print(f"Record Count: {count}")

# Read records
print("\nRecords:")
for i in range(count):
    name_len = processor.read_uint8()
    name = processor.read_bytes(name_len).decode('utf-8')
    age = processor.read_uint8()
    
    # Read float (4 bytes)
    float_bytes = processor.read_bytes(4)
    score = struct.unpack('f', float_bytes)[0]
    
    print(f"  {i+1}. Name: {name}, Age: {age}, Score: {score:.1f}")

print(f"\nRemaining bytes: {processor.remaining()}")
```

---

## Common Pitfalls

### Pitfall 1: Read-Only Views

```python
# Memoryview from bytes is read-only
b = b'hello'
view = memoryview(b)
print(view.readonly)  # True

try:
    view[0] = 72
except TypeError as e:
    print(f"Error: {e}")  # cannot modify read-only memory

# Use bytearray for mutable view
ba = bytearray(b'hello')
view = memoryview(ba)
view[0] = 72  # Works
```

### Pitfall 2: Released Views

```python
view = memoryview(b'hello')
view.release()

try:
    view[0]
except ValueError as e:
    print(f"Error: {e}")  # operation forbidden on released memoryview object
```

### Pitfall 3: Casting Size Mismatch

```python
data = bytearray(5)  # 5 bytes
view = memoryview(data)

# Cannot cast to 4-byte integers (5 not divisible by 4)
try:
    int_view = view.cast('i')
except ValueError as e:
    print(f"Error: {e}")  # memoryview size is not a multiple of new itemsize
```

---

## Performance Tips

### Memoryview vs Copying

```python
import timeit

large_data = bytearray(10000000)  # 10 MB

def with_copy():
    data = large_data[:]  # Creates copy
    return data[5000000]

def with_view():
    view = memoryview(large_data)
    return view[5000000]

copy_time = timeit.timeit(with_copy, number=1000)
view_time = timeit.timeit(with_view, number=1000)

print(f"With copy: {copy_time:.4f}s")
print(f"With view: {view_time:.4f}s")
print(f"View is {copy_time/view_time:.1f}x faster")
```

### Slicing Memoryview

```python
# Slicing memoryview does not copy data
large_data = bytearray(10000000)
view = memoryview(large_data)

# This does NOT copy
slice_view = view[1000000:2000000]

# This DOES copy
copied = large_data[1000000:2000000]

print(f"Slice view size: {len(slice_view)} bytes (no copy)")
print(f"Copied size: {len(copied)} bytes (with copy)")
```

---

## Practice Exercises

### Beginner Level

1. **View and Modify**
   ```python
   # Create bytearray, create view, modify through view
   # Example: Change first 5 bytes to uppercase
   ```

2. **Cast to Integers**
   ```python
   # Cast bytearray of 8 bytes to two integers
   # Example: b'\x01\x00\x00\x00\x02\x00\x00\x00' -> [1, 2]
   ```

3. **Hex Dump**
   ```python
   # Create hex dump using memoryview
   # Format: offset: hex bytes ascii
   ```

### Intermediate Level

4. **Image Filter**
   ```python
   # Apply brightness filter using memoryview
   # Process image data without copying
   ```

5. **Protocol Parser**
   ```python
   # Parse custom binary protocol using memoryview
   # Support variable-length fields
   ```

6. **Audio Mixer**
   ```python
   # Mix two audio buffers using memoryview
   # Apply volume scaling
   ```

### Advanced Level

7. **Matrix Library**
   ```python
   # Implement matrix operations using memoryview
   # Support addition, multiplication, transpose
   ```

8. **File Mapper**
   ```python
   # Use mmap with memoryview for large files
   # Implement search and replace
   ```

9. **Stream Processor**
   ```python
   # Implement streaming parser using memoryview
   # Process data in chunks without copying
   ```

---

## Quick Reference Card

```python
# Creation
view = memoryview(data)          # From bytes/bytearray/array
view = memoryview(arr).cast('i') # Cast to different type

# Properties
len(view)                        # Length in bytes
view.itemsize                    # Size of each element
view.format                      # Format code
view.ndim                        # Number of dimensions
view.shape                       # Tuple of dimensions
view.strides                     # Tuple of strides
view.readonly                    # Whether view is read-only
view.nbytes                      # Total bytes

# Indexing/Slicing
view[0]                          # Get element (int)
view[0:5]                        # Slice (returns memoryview)
view[0][0]                       # Multi-dimensional access

# Methods
view.tobytes()                   # Convert to bytes
view.tolist()                    # Convert to list
view.hex()                       # Convert to hex string
view.cast('B')                   # Cast to new format
view.cast('i', shape=(2,2))      # Cast with shape
view.release()                   # Release view

# Format codes
'B' - unsigned char (1 byte)
'b' - signed char (1 byte)
'H' - unsigned short (2 bytes)
'h' - signed short (2 bytes)
'I' - unsigned int (4 bytes)
'i' - signed int (4 bytes)
'f' - float (4 bytes)
'd' - double (8 bytes)
```

## Next Step

- Move to [08_none_type](/05_python/02_data_types/08_none_type/README.md) for understanding None Data Type.
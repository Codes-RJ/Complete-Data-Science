# 📚 OTHER STANDARD LIBRARY MODULES – OVERVIEW

## 📌 Table of Contents
1. [Overview](#overview)
2. [Modules Covered](#modules-covered)
3. [Quick Reference](#quick-reference)
4. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

This folder covers additional standard library modules that are useful but not as commonly used as the core modules. They provide specialized functionality for specific tasks.

```python
# CSV handling
import csv
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Command-line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name')
args = parser.parse_args()

# Time functions
import time
print(time.time())        # Unix timestamp
time.sleep(2)             # Pause execution
```

---

## 📚 Modules Covered

| Module | Purpose | Common Use |
|--------|---------|-------------|
| `time` | Time access and conversion | Timing, delays, performance measurement |
| `platform` | Platform identification | Cross-platform code |
| `shlex` | Shell-like syntax parsing | Command parsing, configuration |
| `io` | Core I/O tools | String I/O, byte I/O |
| `stat` | File stat constants | File permissions, file types |
| `signal` | Signal handling | Process management, graceful shutdown |

---

## 📊 Quick Reference

### CSV Module

```python
import csv

# Read CSV
with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Write CSV
with open('file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])

# DictReader
with open('file.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'])
```

### Argparse Module

```python
import argparse

parser = argparse.ArgumentParser(description='My script')
parser.add_argument('--input', required=True, help='Input file')
parser.add_argument('--output', help='Output file')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()
```

### Time Module

```python
import time

# Timestamps
timestamp = time.time()
time.sleep(1)

# Struct time
struct_time = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

# Performance
start = time.perf_counter()
# ... code ...
end = time.perf_counter()
print(f"Took {end - start:.4f}s")
```

### Platform Module

```python
import platform

print(platform.system())     # 'Linux', 'Windows', 'Darwin'
print(platform.release())    # Kernel version
print(platform.python_version())  # '3.11.0'
print(platform.machine())    # 'x86_64'
```

### Shlex Module

```python
import shlex

# Split string like shell
tokens = shlex.split('echo "Hello World"')
print(tokens)  # ['echo', 'Hello World']

# Quote for shell safety
safe = shlex.quote("user input; rm -rf /")
print(safe)  # 'user input; rm -rf /'
```

### IO Module

```python
import io

# StringIO (file-like from string)
buffer = io.StringIO()
buffer.write("Hello World")
buffer.seek(0)
content = buffer.read()

# BytesIO (file-like from bytes)
byte_buffer = io.BytesIO()
byte_buffer.write(b"Binary data")
```

### Stat Module

```python
import os
import stat

file_stat = os.stat('file.txt')

# Check file type
print(stat.S_ISREG(file_stat.st_mode))  # Regular file
print(stat.S_ISDIR(file_stat.st_mode))  # Directory

# Check permissions
is_readable = bool(file_stat.st_mode & stat.S_IRUSR)
```

### Signal Module

```python
import signal
import sys

def handler(signum, frame):
    print("Interrupted!")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)
```

---

## 📁 Files in This Folder

| File | Module | Description |
|------|--------|-------------|
| `01_time.md` | `time` | Time access and conversion |
| `02_platform.md` | `platform` | Platform identification |
| `03_shlex.md` | `shlex` | Shell-like syntax parsing |
| `04_io.md` | `io` | Core I/O tools |
| `05_stat.md` | `stat` | File stat constants |
| `06_signal.md` | `signal` | Signal handling |

---

## 💡 Quick Tips

```python
# ✅ DO: Use csv for CSV files (not manual parsing)
import csv
reader = csv.reader(open('data.csv'))

# ❌ DON'T: Parse CSV manually
# line.split(',')  # Fails with quoted fields

# ✅ DO: Use argparse for CLI tools
import argparse

# ❌ DON'T: Use sys.argv manually for complex scripts
# if len(sys.argv) > 1: ...

# ✅ DO: Use platform for cross-platform code
if platform.system() == 'Windows':
    # Windows-specific code
else:
    # Unix-specific code

# ✅ DO: Use shlex.quote() for shell commands
import subprocess
import shlex
subprocess.run(['echo', shlex.quote(user_input)])
```

---

## 🔗 Related Topics

- **File Handling** – Reading/writing files
- **Regular Expressions** – Pattern matching
- **Subprocess** – Running shell commands
- **OS Module** – Operating system interface

---

*Master these additional modules to handle specific tasks efficiently! 🐍✨*

---

## Next Step

- Move to [01_time.md](01_time.md) to learn about time management.

---
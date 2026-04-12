# 📚 STANDARD LIBRARY – OVERVIEW

## 📌 Table of Contents
1. [What is the Standard Library?](#what-is-the-standard-library)
2. [Why Use Standard Library?](#why-use-standard-library)
3. [Module Categories](#module-categories)
4. [Commonly Used Modules](#commonly-used-modules)
5. [Quick Reference](#quick-reference)
6. [Files in This Folder](#files-in-this-folder)

---

## 📖 What is the Standard Library?

The **Python Standard Library** is a collection of modules included with every Python installation. It provides ready-to-use functionality for common programming tasks.

```python
# No installation needed - just import and use
import math
import random
import datetime
import json

print(math.sqrt(16))        # 4.0
print(random.randint(1, 10)) # Random number
print(datetime.datetime.now()) # Current time
print(json.dumps({"name": "Alice"})) # '{"name": "Alice"}'
```

**Key Characteristics:**
- ✅ Included with Python (no extra installation)
- ✅ Cross-platform (works on Windows, Mac, Linux)
- ✅ Well-tested and documented
- ✅ Covers most common programming needs
- ✅ Actively maintained with each Python release

---

## 🎯 Why Use Standard Library?

### Benefits

| Benefit | Description |
|---------|-------------|
| **No installation** | Available immediately after Python installation |
| **Reliability** | Extensively tested and used by millions |
| **Documentation** | Excellent official documentation |
| **Performance** | Many modules implemented in C for speed |
| **Portability** | Works the same across all platforms |
| **Security** | Regular security updates |

### Comparison

```python
# Without standard library (reinventing the wheel)
def calculate_square_root(x):
    # Complex implementation...
    pass

# With standard library (simple and reliable)
import math
result = math.sqrt(x)
```

---

## 📚 Module Categories

| Category | Modules | Purpose |
|----------|---------|---------|
| **Math & Numbers** | `math`, `cmath`, `random`, `statistics`, `decimal`, `fractions` | Mathematical operations, random numbers, statistics |
| **Data Types** | `collections`, `array`, `heapq`, `bisect`, `enum` | Specialized data structures |
| **File & Directory** | `os`, `os.path`, `shutil`, `glob`, `fnmatch`, `tempfile` | File system operations |
| **Data Persistence** | `json`, `pickle`, `sqlite3`, `csv`, `xml` | Data storage and serialization |
| **Date & Time** | `datetime`, `time`, `calendar` | Date and time manipulation |
| **Text Processing** | `re`, `string`, `textwrap`, `difflib` | Regular expressions, string manipulation |
| **System** | `sys`, `argparse`, `logging`, `subprocess` | System interfaces, command line, logging |
| **Internet** | `urllib`, `http`, `smtplib`, `socket`, `email` | Network and web protocols |
| **Concurrency** | `threading`, `multiprocessing`, `asyncio`, `concurrent` | Parallel execution |
| **Development** | `unittest`, `doctest`, `pdb`, `timeit`, `profile` | Testing, debugging, profiling |

---

## 📖 Commonly Used Modules

### Math & Numbers

```python
import math
import random
import statistics

# math
print(math.pi)              # 3.141592653589793
print(math.sqrt(25))        # 5.0
print(math.factorial(5))    # 120

# random
print(random.randint(1, 100))   # Random integer
print(random.choice(['a', 'b', 'c']))  # Random choice

# statistics
data = [10, 20, 30, 40, 50]
print(statistics.mean(data))    # 30
print(statistics.median(data))  # 30
```

### File & Directory

```python
import os
import glob
import shutil

# os
print(os.getcwd())              # Current directory
os.mkdir("new_folder")          # Create directory
os.listdir(".")                 # List files

# glob
py_files = glob.glob("*.py")    # Find all Python files

# shutil
shutil.copy("source.txt", "dest.txt")  # Copy file
shutil.move("old.txt", "new.txt")      # Move file
```

### Data Serialization

```python
import json
import csv

# JSON
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)          # To JSON string
parsed = json.loads(json_str)        # From JSON string

# CSV
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])
```

### Date & Time

```python
from datetime import datetime, date, time, timedelta

# Current time
now = datetime.now()
print(now.year, now.month, now.day)

# Date arithmetic
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
```

### System & OS

```python
import sys
import argparse

# sys
print(sys.argv)              # Command line arguments
print(sys.version)           # Python version
sys.exit(0)                  # Exit program

# argparse (command line parsing)
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str)
args = parser.parse_args()
```

### Text Processing

```python
import re

# Regular expressions
pattern = r'\d+'  # One or more digits
text = "I have 42 apples and 7 oranges"

matches = re.findall(pattern, text)  # ['42', '7']
replaced = re.sub(pattern, 'X', text)  # "I have X apples and X oranges"
```

---

## 📊 Quick Reference

### Most Common Standard Library Modules

| Module | Common Use | Example |
|--------|------------|---------|
| `math` | Math functions | `math.sqrt(16)` |
| `random` | Random numbers | `random.randint(1,10)` |
| `datetime` | Dates and times | `datetime.now()` |
| `json` | JSON handling | `json.dumps(data)` |
| `os` | Operating system | `os.getcwd()` |
| `sys` | System info | `sys.argv` |
| `re` | Regular expressions | `re.search(pattern, text)` |
| `collections` | Data structures | `Counter(items)` |
| `itertools` | Iteration tools | `itertools.cycle(colors)` |
| `functools` | Function tools | `partial(func, arg)` |
| `glob` | File matching | `glob.glob("*.py")` |
| `shutil` | File operations | `shutil.copy(src, dst)` |
| `subprocess` | Run commands | `subprocess.run(["ls"])` |
| `argparse` | CLI parsing | `parser.parse_args()` |
| `logging` | Logging | `logging.info("message")` |
| `unittest` | Testing | `unittest.TestCase` |
| `sqlite3` | Database | `sqlite3.connect("db.db")` |
| `csv` | CSV files | `csv.reader(file)` |
| `hashlib` | Hashing | `hashlib.md5(b"data")` |
| `tempfile` | Temp files | `tempfile.TemporaryFile()` |

---

## 📁 Files in This Folder

| File | Module | Description |
|------|--------|-------------|
| `01_math.md` | `math` | Mathematical functions (trig, log, constants) |
| `02_cmath.md` | `cmath` | Complex number mathematics |
| `03_random.md` | `random` | Random number generation |
| `04_datetime.md` | `datetime` | Date and time handling |
| `05_os.md` | `os` | Operating system interface |
| `06_sys.md` | `sys` | System-specific parameters |
| `07_json.md` | `json` | JSON encoding/decoding |
| `08_re.md` | `re` | Regular expressions |
| `09_collections.md` | `collections` | Specialized container types |
| `10_itertools.md` | `itertools` | Iterator building tools |
| `11_functools.md` | `functools` | Higher-order functions |
| `12_statistics.md` | `statistics` | Statistical functions |
| `13_hashlib.md` | `hashlib` | Cryptographic hashing |
| `14_glob.md` | `glob` | Unix style pathname pattern expansion |
| `15_shutil.md` | `shutil` | High-level file operations |
| `16_tempfile.md` | `tempfile` | Temporary file and directory creation |
| `17_subprocess.md` | `subprocess` | Subprocess management |

---

## 💡 Quick Tips

```python
# ✅ DO: Use standard library when possible
import json
data = json.loads(json_string)

# ❌ DON'T: Reinvent the wheel
# Writing your own JSON parser

# ✅ DO: Check if module exists before import
try:
    import numpy
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

# ✅ DO: Use from import for frequently used items
from math import sqrt, pi
print(sqrt(25))

# ✅ DO: Use aliases for long module names
import datetime as dt
now = dt.datetime.now()
```

---

## 📚 Next Steps

After understanding the standard library overview:
1. Open `01_math.md` for mathematical functions
2. Open `02_cmath.md` for complex numbers
3. Open `03_random.md` for random number generation
4. Explore other modules as needed

---

## 🔗 Related Topics

- **Third-party modules** – Packages you install with pip
- **Built-in functions** – `print()`, `len()`, `type()`, etc.
- **Python documentation** – Official standard library reference

---

*Master the standard library to write powerful Python programs without reinventing the wheel! 🐍✨*

---

## Next Step

- Move to [01_math.md](01_math.md) to learn about the math module.

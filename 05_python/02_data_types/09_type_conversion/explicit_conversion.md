# 📘 EXPLICIT TYPE CONVERSION – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Explicit Conversion?](#what-is-explicit-conversion)
2. [Numeric Conversions](#numeric-conversions)
3. [String Conversions](#string-conversions)
4. [Sequence Conversions](#sequence-conversions)
5. [Set and Dictionary Conversions](#set-and-dictionary-conversions)
6. [Boolean Conversions](#boolean-conversions)
7. [Base Conversions](#base-conversions)
8. [Character Conversions](#character-conversions)
9. [Real-World Examples](#real-world-examples)
10. [Common Pitfalls](#common-pitfalls)
11. [Practice Exercises](#practice-exercises)

---

## What is Explicit Conversion?

**Explicit conversion** (also called type casting) is when you manually convert a value from one data type to another using conversion functions.

```python
# Explicit conversion examples
num_str = "123"
num_int = int(num_str)      # String → Integer
num_float = float(num_str)  # String → Float
text = str(456)             # Integer → String

print(type(num_str))   # <class 'str'>
print(type(num_int))   # <class 'int'>
```

**Why Explicit Conversion?**
- Python doesn't automatically convert incompatible types
- User input is always string
- Need specific types for operations
- Data validation and sanitization

---

## Numeric Conversions

### `int()` – Convert to Integer

```python
# From float (truncates toward zero)
print(int(3.14))    # 3
print(int(3.99))    # 3
print(int(-3.14))   # -3
print(int(-3.99))   # -3

# From string
print(int("42"))      # 42
print(int("-42"))     # -42
print(int("   42   ")) # 42 (strips whitespace)

# From string with base
print(int("101010", 2))   # 42 (binary)
print(int("52", 8))       # 42 (octal)
print(int("2A", 16))      # 42 (hex)
print(int("FF", 16))      # 255

# From boolean
print(int(True))     # 1
print(int(False))    # 0

# From other types
print(int(3+4j))     # TypeError! Can't convert complex to int
```

### `float()` – Convert to Float

```python
# From integer
print(float(42))      # 42.0
print(float(-10))     # -10.0

# From string
print(float("3.14"))      # 3.14
print(float("-0.5"))      # -0.5
print(float("  2.5  "))   # 2.5
print(float("1e-4"))      # 0.0001
print(float("inf"))       # inf
print(float("-inf"))      # -inf
print(float("nan"))       # nan

# From boolean
print(float(True))    # 1.0
print(float(False))   # 0.0

# Invalid conversions
try:
    float("abc")
except ValueError:
    print("Cannot convert 'abc' to float")
```

### `complex()` – Convert to Complex

```python
# From numbers
print(complex(5))         # (5+0j)
print(complex(2.5))       # (2.5+0j)
print(complex(3, 4))      # (3+4j)

# From string
print(complex("3+4j"))    # (3+4j)
print(complex("5"))       # (5+0j)
print(complex("2j"))      # 2j

# Invalid formats
try:
    complex("3+4")
except ValueError:
    print("Invalid complex format (missing j)")

# From boolean
print(complex(True))      # (1+0j)
print(complex(False))     # 0j
```

---

## String Conversions

### `str()` – Convert to String

```python
# From numbers
print(str(42))          # "42"
print(str(3.14))        # "3.14"
print(str(3+4j))        # "(3+4j)"

# From boolean
print(str(True))        # "True"
print(str(False))       # "False"

# From None
print(str(None))        # "None"

# From collections
print(str([1, 2, 3]))   # "[1, 2, 3]"
print(str((1, 2, 3)))   # "(1, 2, 3)"
print(str({"a": 1}))    # "{'a': 1}"
print(str({1, 2, 3}))   # "{1, 2, 3}"

# From custom objects
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person(name={self.name})"

p = Person("Alice")
print(str(p))  # "Person(name=Alice)"
```

### String Formatting as Conversion

```python
# f-strings (Python 3.6+)
value = 42
text = f"The answer is {value}"  # "The answer is 42"

# format() method
text = "The answer is {}".format(42)

# % formatting (old style)
text = "The answer is %d" % 42

# Real use: Building messages
name = "Alice"
age = 30
message = f"{name} is {age} years old"
print(message)  # "Alice is 30 years old"
```

---

## Sequence Conversions

### `list()` – Convert to List

```python
# From string (characters)
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']

# From tuple
print(list((1, 2, 3)))      # [1, 2, 3]

# From range
print(list(range(5)))       # [0, 1, 2, 3, 4]

# From set
print(list({1, 2, 3}))      # [1, 2, 3] (order may vary)

# From dictionary (keys only)
print(list({"a": 1, "b": 2}))  # ['a', 'b']

# From dict items
print(list({"a": 1, "b": 2}.items()))  # [('a', 1), ('b', 2)]

# From dict values
print(list({"a": 1, "b": 2}.values()))  # [1, 2]

# Real use: Convert range to list for modification
numbers = list(range(10))
numbers[5] = 99
print(numbers)  # [0, 1, 2, 3, 4, 99, 6, 7, 8, 9]
```

### `tuple()` – Convert to Tuple

```python
# From list
print(tuple([1, 2, 3]))     # (1, 2, 3)

# From string
print(tuple("hello"))       # ('h', 'e', 'l', 'l', 'o')

# From range
print(tuple(range(5)))      # (0, 1, 2, 3, 4)

# From set
print(tuple({1, 2, 3}))     # (1, 2, 3)

# From dictionary (keys)
print(tuple({"a": 1, "b": 2}))  # ('a', 'b')

# Real use: Make list immutable
scores = [85, 90, 88]
scores_tuple = tuple(scores)  # (85, 90, 88)
# scores_tuple[0] = 100  # TypeError! Immutable
```

### `range()` – Convert to Range

```python
# Cannot directly convert other types to range
# But you can create range from numbers

# From list (create new range)
numbers = [1, 2, 3, 4, 5]
if len(numbers) >= 2:
    step = numbers[1] - numbers[0]
    r = range(numbers[0], numbers[-1] + 1, step)
    print(list(r))  # [1, 2, 3, 4, 5]

# From string of numbers
text = "12345"
r = range(int(text[0]), int(text[-1]) + 1)
print(list(r))  # [1, 2, 3, 4, 5]
```

---

## Set and Dictionary Conversions

### `set()` – Convert to Set

```python
# From list (removes duplicates)
print(set([1, 2, 2, 3, 3, 3]))  # {1, 2, 3}

# From string (unique characters)
print(set("hello"))              # {'h', 'e', 'l', 'o'}

# From tuple
print(set((1, 2, 2, 3)))         # {1, 2, 3}

# From range
print(set(range(5)))             # {0, 1, 2, 3, 4}

# From dictionary (keys)
print(set({"a": 1, "b": 2}))     # {'a', 'b'}

# Real use: Remove duplicates while preserving order
def unique_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

numbers = [1, 2, 2, 3, 3, 3, 4, 1, 5]
unique = unique_preserve_order(numbers)
print(unique)  # [1, 2, 3, 4, 5]
```

### `dict()` – Convert to Dictionary

```python
# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# From two lists (using zip)
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# From keyword arguments
d = dict(a=1, b=2, c=3)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# From dictionary (copy)
original = {"a": 1, "b": 2}
copy = dict(original)
print(copy)  # {'a': 1, 'b': 2}

# Real use: Convert API response to dict
api_response = [("user", "Alice"), ("age", 30), ("city", "NYC")]
user_data = dict(api_response)
print(user_data)  # {'user': 'Alice', 'age': 30, 'city': 'NYC'}
```

### `frozenset()` – Convert to Frozenset

```python
# From list
print(frozenset([1, 2, 2, 3]))   # frozenset({1, 2, 3})

# From set
my_set = {1, 2, 3}
fs = frozenset(my_set)
print(fs)  # frozenset({1, 2, 3})

# From string
print(frozenset("hello"))  # frozenset({'h', 'e', 'l', 'o'})

# Real use: Use as dictionary key
cache = {}
cache[frozenset([1, 2, 3])] = "value"
print(cache[frozenset([1, 2, 3])])  # "value"
```

---

## Boolean Conversions

### `bool()` – Convert to Boolean

```python
# Falsy values (convert to False)
falsy_values = [None, False, 0, 0.0, 0j, "", [], (), {}, set()]
for val in falsy_values:
    print(f"{repr(val):10} -> {bool(val)}")
# None       -> False
# False      -> False
# 0          -> False
# 0.0        -> False
# 0j         -> False
# ''         -> False
# []         -> False
# ()         -> False
# {}         -> False
# set()      -> False

# Truthy values (convert to True)
truthy_values = [True, 1, -1, 3.14, "hello", [1, 2], (1, 2), {"a": 1}, {1, 2}]
for val in truthy_values:
    print(f"{repr(val):10} -> {bool(val)}")
# True       -> True
# 1          -> True
# -1         -> True
# 3.14       -> True
# 'hello'    -> True
# [1, 2]     -> True
# (1, 2)     -> True
# {'a': 1}   -> True
# {1, 2}     -> True

# Real use: Conditional logic
user_input = ""
if bool(user_input):
    print("Has input")
else:
    print("No input")  # This prints

# Better: Direct truthy check
if user_input:
    print("Has input")
```

---

## Base Conversions

### Binary, Octal, Hexadecimal

```python
# To binary string
print(bin(42))      # '0b101010'
print(bin(255))     # '0b11111111'

# To octal string
print(oct(42))      # '0o52'
print(oct(255))     # '0o377'

# To hex string
print(hex(42))      # '0x2a'
print(hex(255))     # '0xff'

# Remove prefix
print(bin(42)[2:])  # '101010'
print(oct(42)[2:])  # '52'
print(hex(42)[2:])  # '2a'

# From binary string
print(int('101010', 2))   # 42
print(int('11111111', 2)) # 255

# From octal string
print(int('52', 8))       # 42
print(int('377', 8))      # 255

# From hex string
print(int('2a', 16))      # 42
print(int('ff', 16))      # 255

# Real use: Color conversion
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)

print(hex_to_rgb('#FF0000'))  # (255, 0, 0)
print(hex_to_rgb('#00FF00'))  # (0, 255, 0)
print(hex_to_rgb('#0000FF'))  # (0, 0, 255)
```

---

## Character Conversions

### `chr()` – Integer to Character

```python
# ASCII characters
print(chr(65))    # 'A'
print(chr(97))    # 'a'
print(chr(48))    # '0'

# Unicode characters
print(chr(8364))  # '€' (Euro)
print(chr(9829))  # '♥' (Heart)
print(chr(128512)) # '😀' (Grinning face)

# Generate alphabet
alphabet = [chr(i) for i in range(65, 91)]
print(alphabet)  # ['A', 'B', 'C', ... 'Z']

# Generate digits
digits = [chr(i) for i in range(48, 58)]
print(digits)  # ['0', '1', '2', ... '9']
```

### `ord()` – Character to Integer

```python
# ASCII characters
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('0'))   # 48

# Unicode characters
print(ord('€'))   # 8364
print(ord('♥'))   # 9829
print(ord('😀'))  # 128512

# Real use: Caesar cipher
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return ''.join(result)

print(caesar_cipher("HELLO", 3))   # "KHOOR"
print(caesar_cipher("KHOOR", -3))  # "HELLO"

# Real use: Character arithmetic
def next_char(c):
    return chr(ord(c) + 1)

print(next_char('A'))  # 'B'
print(next_char('z'))  # '{' (wraps to next ASCII)
```

---

## Real-World Examples

### Example 1: User Input Processor

```python
class InputProcessor:
    @staticmethod
    def get_int(prompt, default=None):
        """Get integer input from user"""
        while True:
            try:
                value = input(prompt)
                if not value and default is not None:
                    return default
                return int(value)
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    @staticmethod
    def get_float(prompt, default=None):
        """Get float input from user"""
        while True:
            try:
                value = input(prompt)
                if not value and default is not None:
                    return default
                return float(value)
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    @staticmethod
    def get_bool(prompt, default=None):
        """Get boolean input from user"""
        while True:
            value = input(prompt).lower()
            if not value and default is not None:
                return default
            if value in ('y', 'yes', 'true', 't', '1'):
                return True
            if value in ('n', 'no', 'false', 'f', '0'):
                return False
            print("Invalid input. Please enter yes/no.")

# Usage
print("USER INPUT PROCESSOR")
print("=" * 40)

age = InputProcessor.get_int("Enter your age: ")
height = InputProcessor.get_float("Enter your height (m): ")
is_student = InputProcessor.get_bool("Are you a student? (y/n): ")

print(f"\nProcessed data:")
print(f"  Age: {age} (type: {type(age).__name__})")
print(f"  Height: {height} (type: {type(height).__name__})")
print(f"  Student: {is_student} (type: {type(is_student).__name__})")
```

### Example 2: Data Cleaner and Normalizer

```python
class DataCleaner:
    @staticmethod
    def to_int(value, default=0):
        """Safely convert to int"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def to_float(value, default=0.0):
        """Safely convert to float"""
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def to_bool(value, default=False):
        """Safely convert to bool"""
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, str):
            return value.lower() in ('true', 'yes', 'y', 't', '1')
        return default
    
    @staticmethod
    def to_list(value, default=None):
        """Convert to list"""
        if default is None:
            default = []
        if isinstance(value, list):
            return value
        if isinstance(value, (tuple, set)):
            return list(value)
        if isinstance(value, str):
            return list(value)
        if value is None:
            return default
        return [value]
    
    @staticmethod
    def clean_csv_row(row, types):
        """Clean CSV row with type conversion"""
        cleaned = []
        for value, expected_type in zip(row, types):
            if expected_type == int:
                cleaned.append(DataCleaner.to_int(value))
            elif expected_type == float:
                cleaned.append(DataCleaner.to_float(value))
            elif expected_type == bool:
                cleaned.append(DataCleaner.to_bool(value))
            else:
                cleaned.append(value)
        return cleaned

# Usage
print("DATA CLEANER")
print("=" * 40)

# Raw data (could be from CSV, API, etc.)
raw_data = [
    ["123", "45.67", "true", "apple"],
    ["abc", "78.90", "false", "banana"],
    ["456", "invalid", "yes", "cherry"],
    ["", "0", "1", "date"]
]

# Define expected types
types = [int, float, bool, str]

print("Raw data:")
for row in raw_data:
    print(f"  {row}")

print("\nCleaned data:")
for row in raw_data:
    cleaned = DataCleaner.clean_csv_row(row, types)
    print(f"  {cleaned}")

# Individual conversions
print("\nIndividual conversions:")
print(f"to_int('123'): {DataCleaner.to_int('123')}")
print(f"to_int('abc'): {DataCleaner.to_int('abc')}")
print(f"to_float('45.67'): {DataCleaner.to_float('45.67')}")
print(f"to_float('invalid'): {DataCleaner.to_float('invalid')}")
print(f"to_bool('true'): {DataCleaner.to_bool('true')}")
print(f"to_bool('yes'): {DataCleaner.to_bool('yes')}")
print(f"to_bool('0'): {DataCleaner.to_bool('0')}")
```

### Example 3: CSV Parser with Type Conversion

```python
import csv
from io import StringIO

class CSVParser:
    def __init__(self, headers=None, types=None):
        self.headers = headers
        self.types = types or []
    
    def parse(self, csv_string):
        """Parse CSV string with type conversion"""
        result = []
        reader = csv.reader(StringIO(csv_string))
        
        rows = list(reader)
        if not rows:
            return result
        
        # Use headers if provided, otherwise first row
        headers = self.headers or rows[0]
        start_row = 0 if self.headers else 1
        
        for row in rows[start_row:]:
            # Ensure row has same length as headers
            while len(row) < len(headers):
                row.append('')
            
            # Convert types
            converted = {}
            for i, (header, value) in enumerate(zip(headers, row)):
                if i < len(self.types) and self.types[i]:
                    converted[header] = self._convert(value, self.types[i])
                else:
                    converted[header] = value
            
            result.append(converted)
        
        return result
    
    def _convert(self, value, target_type):
        """Convert single value to target type"""
        if not value or value.strip() == '':
            return None
        
        try:
            if target_type == int:
                return int(float(value))  # Handle decimal strings
            elif target_type == float:
                return float(value)
            elif target_type == bool:
                return value.lower() in ('true', 'yes', 'y', 't', '1')
            elif target_type == str:
                return str(value)
            else:
                return target_type(value)
        except (ValueError, TypeError):
            return None
    
    def to_csv(self, data, headers=None):
        """Convert data to CSV string"""
        output = StringIO()
        writer = csv.writer(output)
        
        headers = headers or self.headers or list(data[0].keys())
        writer.writerow(headers)
        
        for row in data:
            writer.writerow([row.get(h, '') for h in headers])
        
        return output.getvalue()

# Usage
print("CSV PARSER WITH TYPE CONVERSION")
print("=" * 50)

# Sample CSV data
csv_data = """name,age,score,active
Alice,25,85.5,true
Bob,30,92.3,false
Charlie,35,invalid,yes
Diana,28,88.7,1
Eve,,75.2,true"""

print("Original CSV:")
print(csv_data)
print()

# Parse with type conversion
parser = CSVParser(
    headers=["name", "age", "score", "active"],
    types=[str, int, float, bool]
)

parsed = parser.parse(csv_data)

print("Parsed data with types:")
for row in parsed:
    print(f"  {row}")
    for key, value in row.items():
        print(f"    {key}: {value} ({type(value).__name__})")

# Convert back to CSV
print("\nConverted back to CSV:")
csv_output = parser.to_csv(parsed)
print(csv_output)
```

### Example 4: Configuration Loader with Type Conversion

```python
import json
import os
from typing import Any, Optional

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config = {}
        self.types = {}
        self.config_file = config_file
        self.env_prefix = "APP_"
        
        if config_file and os.path.exists(config_file):
            self.load_from_file(config_file)
    
    def register_type(self, key, converter):
        """Register type converter for a key"""
        self.types[key] = converter
    
    def set(self, key, value, convert=True):
        """Set configuration value"""
        if convert and key in self.types:
            try:
                value = self.types[key](value)
            except (ValueError, TypeError):
                pass
        self.config[key] = value
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def load_from_file(self, filename):
        """Load configuration from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            for key, value in data.items():
                self.set(key, value)
    
    def load_from_env(self):
        """Load configuration from environment variables"""
        for key in self.types:
            env_var = f"{self.env_prefix}{key.upper()}"
            if env_var in os.environ:
                self.set(key, os.environ[env_var])
    
    def load_from_dict(self, data):
        """Load configuration from dictionary"""
        for key, value in data.items():
            self.set(key, value)
    
    def get_int(self, key, default=0):
        """Get integer value"""
        value = self.get(key, default)
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def get_float(self, key, default=0.0):
        """Get float value"""
        value = self.get(key, default)
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    def get_bool(self, key, default=False):
        """Get boolean value"""
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', 'yes', 'y', 't', '1')
        if isinstance(value, (int, float)):
            return value != 0
        return default
    
    def get_list(self, key, default=None):
        """Get list value"""
        if default is None:
            default = []
        value = self.get(key, default)
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            return [item.strip() for item in value.split(',')]
        if value is None:
            return default
        return [value]

# Usage
print("CONFIGURATION LOADER")
print("=" * 50)

# Create config loader
config = ConfigLoader()

# Register type converters
config.register_type("port", int)
config.register_type("debug", bool)
config.register_type("timeout", float)
config.register_type("allowed_hosts", lambda x: x.split(',') if isinstance(x, str) else x)

# Load from dictionary
config.load_from_dict({
    "host": "localhost",
    "port": "8080",  # Will be converted to int
    "debug": "true",  # Will be converted to bool
    "timeout": "30.5",  # Will be converted to float
    "allowed_hosts": "localhost,127.0.0.1,0.0.0.0",  # Will be split to list
    "max_connections": 100
})

# Get values with type conversion
print(f"Host: {config.get('host')} ({type(config.get('host')).__name__})")
print(f"Port: {config.get_int('port')} ({type(config.get_int('port')).__name__})")
print(f"Debug: {config.get_bool('debug')} ({type(config.get_bool('debug')).__name__})")
print(f"Timeout: {config.get_float('timeout')} ({type(config.get_float('timeout')).__name__})")
print(f"Allowed Hosts: {config.get_list('allowed_hosts')} ({type(config.get_list('allowed_hosts')).__name__})")
print(f"Max Connections: {config.get_int('max_connections')}")

# Get with default
missing = config.get_int("nonexistent", 999)
print(f"Missing key (default 999): {missing}")
```

### Example 5: API Response Normalizer

```python
from datetime import datetime
from typing import Any, Dict, List

class APINormalizer:
    """Normalize API responses with consistent types"""
    
    @staticmethod
    def normalize_int(value: Any, default: int = 0) -> int:
        """Convert to int"""
        if value is None:
            return default
        if isinstance(value, bool):
            return 1 if value else 0
        try:
            return int(float(str(value)))
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def normalize_float(value: Any, default: float = 0.0) -> float:
        """Convert to float"""
        if value is None:
            return default
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def normalize_bool(value: Any, default: bool = False) -> bool:
        """Convert to bool"""
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, str):
            return value.lower() in ('true', 'yes', 'y', 't', '1')
        return default
    
    @staticmethod
    def normalize_str(value: Any, default: str = "") -> str:
        """Convert to string"""
        if value is None:
            return default
        return str(value)
    
    @staticmethod
    def normalize_list(value: Any, default: List = None) -> List:
        """Convert to list"""
        if default is None:
            default = []
        if value is None:
            return default
        if isinstance(value, list):
            return value
        if isinstance(value, (tuple, set)):
            return list(value)
        if isinstance(value, str):
            return [value]
        return [value]
    
    @staticmethod
    def normalize_dict(value: Any, default: Dict = None) -> Dict:
        """Convert to dict"""
        if default is None:
            default = {}
        if value is None:
            return default
        if isinstance(value, dict):
            return value
        return default
    
    @staticmethod
    def normalize_datetime(value: Any, default=None) -> datetime:
        """Convert to datetime"""
        if value is None:
            return default
        if isinstance(value, datetime):
            return value
        if isinstance(value, (int, float)):
            try:
                return datetime.fromtimestamp(value)
            except (ValueError, OSError):
                return default
        if isinstance(value, str):
            formats = [
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%d",
                "%Y/%m/%d %H:%M:%S",
                "%Y/%m/%d"
            ]
            for fmt in formats:
                try:
                    return datetime.strptime(value, fmt)
                except ValueError:
                    continue
        return default

# Usage
print("API RESPONSE NORMALIZER")
print("=" * 50)

# Raw API response (inconsistent types)
api_response = {
    "user_id": "123",
    "name": "Alice",
    "age": "30",
    "score": "85.5",
    "is_active": "true",
    "tags": "python,developer",
    "created_at": "2024-01-15 10:30:00",
    "metadata": None
}

print("Raw API response:")
for key, value in api_response.items():
    print(f"  {key}: {value} ({type(value).__name__})")

# Normalize
normalizer = APINormalizer()
normalized = {
    "user_id": normalizer.normalize_int(api_response.get("user_id")),
    "name": normalizer.normalize_str(api_response.get("name")),
    "age": normalizer.normalize_int(api_response.get("age")),
    "score": normalizer.normalize_float(api_response.get("score")),
    "is_active": normalizer.normalize_bool(api_response.get("is_active")),
    "tags": normalizer.normalize_list(api_response.get("tags")),
    "created_at": normalizer.normalize_datetime(api_response.get("created_at")),
    "metadata": normalizer.normalize_dict(api_response.get("metadata"))
}

print("\nNormalized response:")
for key, value in normalized.items():
    print(f"  {key}: {value} ({type(value).__name__})")
```

### Example 6: Database Query Result Converter

```python
import sqlite3
from typing import List, Dict, Any, Optional

class DatabaseConverter:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()
    
    def fetch_as_dicts(self, query: str, params: tuple = ()) -> List[Dict]:
        """Fetch results as list of dictionaries"""
        self.cursor.execute(query, params)
        columns = [description[0] for description in self.cursor.description]
        rows = self.cursor.fetchall()
        
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
        
        return results
    
    def fetch_as_typed(self, query: str, types: List[type], params: tuple = ()) -> List[List]:
        """Fetch results with type conversion"""
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        
        results = []
        for row in rows:
            converted = []
            for value, expected_type in zip(row, types):
                converted.append(self._convert_type(value, expected_type))
            results.append(converted)
        
        return results
    
    def _convert_type(self, value: Any, target_type: type) -> Any:
        """Convert value to target type"""
        if value is None:
            return None
        
        if target_type == int:
            try:
                return int(value)
            except (ValueError, TypeError):
                return None
        elif target_type == float:
            try:
                return float(value)
            except (ValueError, TypeError):
                return None
        elif target_type == bool:
            if isinstance(value, int):
                return value != 0
            if isinstance(value, str):
                return value.lower() in ('true', 'yes', 'y', 't', '1')
            return bool(value)
        elif target_type == str:
            return str(value)
        else:
            return value
    
    def insert_from_list(self, table: str, data: List[Dict]) -> int:
        """Insert list of dictionaries into table"""
        if not data:
            return 0
        
        columns = list(data[0].keys())
        placeholders = ','.join(['?' for _ in columns])
        query = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({placeholders})"
        
        rows_affected = 0
        for row in data:
            values = [row.get(col) for col in columns]
            self.cursor.execute(query, values)
            rows_affected += 1
        
        self.conn.commit()
        return rows_affected

# Create test database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        score REAL,
        is_active INTEGER
    )
''')

# Insert sample data
cursor.executemany(
    "INSERT INTO users (name, age, score, is_active) VALUES (?, ?, ?, ?)",
    [
        ('Alice', 25, 85.5, 1),
        ('Bob', 30, 92.3, 0),
        ('Charlie', 35, 78.9, 1),
        ('Diana', 28, 88.7, 1),
    ]
)
conn.commit()

print("DATABASE CONVERTER")
print("=" * 50)

# Create converter
converter = DatabaseConverter(conn)

# Fetch as dictionaries
print("\n1. Fetch as dictionaries:")
users = converter.fetch_as_dicts("SELECT * FROM users")
for user in users:
    print(f"  {user}")

# Fetch with type conversion
print("\n2. Fetch with type conversion:")
types = [int, str, int, float, bool]
users_typed = converter.fetch_as_typed(
    "SELECT id, name, age, score, is_active FROM users",
    types
)
for user in users_typed:
    print(f"  {user}")

# Insert from list
print("\n3. Insert from list:")
new_users = [
    {"name": "Eve", "age": "32", "score": "91.2", "is_active": True},
    {"name": "Frank", "age": "27", "score": "87.5", "is_active": False},
]
count = converter.insert_from_list("users", new_users)
print(f"  Inserted {count} rows")

# Verify insertion
print("\n4. All users after insertion:")
users = converter.fetch_as_dicts("SELECT * FROM users")
for user in users:
    print(f"  {user}")

conn.close()
```

---

## Common Pitfalls

### Pitfall 1: Loss of Precision

```python
# Converting float to int truncates (not rounds)
print(int(3.14))   # 3 (not 3.14)
print(int(3.99))   # 3 (not 4)

# Use round() for proper rounding
print(round(3.14))  # 3
print(round(3.99))  # 4

# Converting large numbers
large_float = 1e100
try:
    large_int = int(large_float)  # OverflowError!
except OverflowError:
    print("Float too large for integer conversion")
```

### Pitfall 2: Invalid String Conversions

```python
# Non-numeric strings
try:
    int("abc")
except ValueError:
    print("Cannot convert 'abc' to int")

# Empty string
try:
    int("")
except ValueError:
    print("Cannot convert empty string to int")

# String with spaces
print(int("  42  "))  # 42 (works, strips whitespace)
print(int("42.5"))    # ValueError! (decimal point not allowed)

# Use float first for decimal strings
value = int(float("42.5"))  # 42
```

### Pitfall 3: Boolean Conversion Surprises

```python
# Non-empty strings are True
print(bool("False"))   # True (not False!)
print(bool("0"))       # True (not False!)
print(bool(" "))       # True

# Empty string is False
print(bool(""))        # False

# Zero is False, non-zero is True
print(bool(0))         # False
print(bool(-1))        # True

# Collections
print(bool([]))        # False
print(bool([1, 2]))    # True
```

### Pitfall 4: Type Conversion with None

```python
# Converting None raises TypeError
try:
    int(None)
except TypeError:
    print("Cannot convert None to int")

# Safe conversion with default
def safe_int(value, default=0):
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int(None))      # 0
print(safe_int("123"))     # 123
print(safe_int("abc"))     # 0
```

---

## Practice Exercises

### Beginner Level

1. **String to Number**
   ```python
   # Convert user input to int safely
   # Handle errors and provide default
   ```

2. **List to Set**
   ```python
   # Remove duplicates from list using set
   # Convert back to list preserving order
   ```

3. **Temperature Converter**
   ```python
   # Convert between Celsius and Fahrenheit
   # Use type conversion for input/output
   ```

### Intermediate Level

4. **CSV Parser**
   ```python
   # Parse CSV string to list of dictionaries
   # Convert numeric strings to appropriate types
   ```

5. **Config Parser**
   ```python
   # Parse config file with different types
   # Support int, float, bool, list, dict
   ```

6. **Data Normalizer**
   ```python
   # Normalize mixed-type data to consistent types
   # Handle None, empty strings, invalid values
   ```

### Advanced Level

7. **Type Inference**
   ```python
   # Automatically detect and convert string to appropriate type
   # Support int, float, bool, list, dict, datetime
   ```

8. **Schema Validator**
   ```python
   # Validate and convert data against schema
   # Support nested structures and custom converters
   ```

9. **API Response Normalizer**
   ```python
   # Normalize API responses to consistent types
   # Handle missing fields, null values, type mismatches
   ```

---

## Quick Reference Card

```python
# Numeric conversions
int(x)          # To integer
float(x)        # To float
complex(x)      # To complex
bool(x)         # To boolean

# String conversion
str(x)          # To string

# Sequence conversions
list(x)         # To list
tuple(x)        # To tuple
set(x)          # To set
frozenset(x)    # To frozenset
dict(x)         # To dictionary

# Base conversions
bin(x)          # To binary string
oct(x)          # To octal string
hex(x)          # To hex string
int(s, base)    # From base string

# Character conversions
chr(i)          # Integer to character
ord(c)          # Character to integer

# Safe conversion pattern
def safe_convert(value, converter, default):
    try:
        return converter(value)
    except (ValueError, TypeError):
        return default

# Type checking before conversion
if isinstance(value, (int, float)):
    result = int(value)
elif isinstance(value, str) and value.isdigit():
    result = int(value)
else:
    result = None
```

## Next Step

- Go to [implicit_conversion.md](implicit_conversion.md) for understanding Implicit Type Conversion.
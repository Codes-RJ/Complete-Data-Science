# 📘 JSON MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is JSON?](#what-is-json)
2. [JSON Module Overview](#json-module-overview)
3. [Serialization (Python to JSON)](#serialization-python-to-json)
4. [Deserialization (JSON to Python)](#deserialization-json-to-python)
5. [Working with Files](#working-with-files)
6. [Custom JSON Encoding](#custom-json-encoding)
7. [Custom JSON Decoding](#custom-json-decoding)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

```json
{
  "name": "Alice",
  "age": 30,
  "city": "New York",
  "hobbies": ["reading", "swimming"],
  "address": {
    "street": "123 Main St",
    "zip": "10001"
  }
}
```

**JSON Data Types:**
- Strings: `"hello"`
- Numbers: `42`, `3.14`
- Booleans: `true`, `false`
- Null: `null`
- Arrays: `[1, 2, 3]`
- Objects: `{"key": "value"}`

---

## JSON Module Overview

The `json` module provides functions for working with JSON data.

```python
import json

# Python to JSON (serialization)
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Alice", "age": 30}'

# JSON to Python (deserialization)
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
print(data)  # {'name': 'Bob', 'age': 25}
```

**Key Functions:**
| Function | Purpose |
|----------|---------|
| `json.dumps()` | Python object → JSON string |
| `json.loads()` | JSON string → Python object |
| `json.dump()` | Python object → JSON file |
| `json.load()` | JSON file → Python object |

---

## Serialization (Python to JSON)

### `json.dumps()` – Convert Python to JSON String

```python
import json

# Basic conversion
python_dict = {"name": "Alice", "age": 30, "active": True}
json_str = json.dumps(python_dict)
print(json_str)  # '{"name": "Alice", "age": 30, "active": true}'

# Python types and their JSON equivalents
python_data = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"key": "value"}
}

json_str = json.dumps(python_data)
print(json_str)
# {"string": "hello", "integer": 42, "float": 3.14, "boolean": true, 
#  "null": null, "list": [1, 2, 3], "tuple": [4, 5, 6], "dict": {"key": "value"}}
```

### Formatting Options

```python
import json

data = {"name": "Alice", "age": 30, "hobbies": ["reading", "swimming"]}

# Compact (default)
print(json.dumps(data))
# {"name": "Alice", "age": 30, "hobbies": ["reading", "swimming"]}

# Indented (pretty print)
print(json.dumps(data, indent=2))
# {
#   "name": "Alice",
#   "age": 30,
#   "hobbies": [
#     "reading",
#     "swimming"
#   ]
# }

# Custom indentation
print(json.dumps(data, indent=4))

# With separators
print(json.dumps(data, separators=(',', ':')))
# {"name":"Alice","age":30,"hobbies":["reading","swimming"]}

# Sorted keys
print(json.dumps(data, sort_keys=True, indent=2))
# {
#   "age": 30,
#   "hobbies": [
#     "reading",
#     "swimming"
#   ],
#   "name": "Alice"
# }
```

### Handling Non-Serializable Types

```python
import json
from datetime import datetime

data = {
    "name": "Alice",
    "created": datetime.now(),
    "price": 19.99
}

# This fails: TypeError: Object of type datetime is not JSON serializable
# json.dumps(data)

# Solution 1: Use default parameter
def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

json_str = json.dumps(data, default=json_serializer, indent=2)
print(json_str)

# Solution 2: Convert before serializing
data['created'] = data['created'].isoformat()
json_str = json.dumps(data, indent=2)
```

---

## Deserialization (JSON to Python)

### `json.loads()` – Convert JSON String to Python

```python
import json

# Basic conversion
json_str = '{"name": "Alice", "age": 30, "active": true}'
data = json.loads(json_str)
print(data)  # {'name': 'Alice', 'age': 30, 'active': True}
print(type(data))  # <class 'dict'>

# JSON types to Python types mapping
json_data = """
{
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {"key": "value"}
}
"""

python_data = json.loads(json_data)
print(python_data)
# {
#     'string': 'hello',
#     'number': 42,
#     'float': 3.14,
#     'boolean': True,
#     'null': None,
#     'array': [1, 2, 3],
#     'object': {'key': 'value'}
# }
```

### Type Mapping Table

| JSON | Python |
|------|--------|
| object | dict |
| array | list |
| string | str |
| number (int) | int |
| number (real) | float |
| true | True |
| false | False |
| null | None |

### Handling Invalid JSON

```python
import json

invalid_json = '{"name": "Alice", age: 30}'  # Missing quotes around age

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Position: {e.pos}")
    print(f"Line: {e.lineno}, Column: {e.colno}")
```

---

## Working with Files

### `json.dump()` – Write JSON to File

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "swimming"]
}

# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Write with custom options
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)
```

### `json.load()` – Read JSON from File

```python
import json

# Read from file
with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
```

### Complete File Example

```python
import json

class JSONFileHandler:
    @staticmethod
    def save(data, filename, indent=2):
        """Save data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=indent)
        print(f"Saved to {filename}")
    
    @staticmethod
    def load(filename):
        """Load data from JSON file"""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found")
            return None
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in {filename}: {e}")
            return None
    
    @staticmethod
    def append(data, filename):
        """Append data to JSON array in file"""
        existing = JSONFileHandler.load(filename)
        if existing is None:
            existing = []
        if isinstance(existing, list):
            existing.append(data)
            JSONFileHandler.save(existing, filename)
        else:
            print("Cannot append to non-array JSON")

# Usage
data = {"name": "Alice", "age": 30}
JSONFileHandler.save(data, 'user.json')

loaded = JSONFileHandler.load('user.json')
print(loaded)
```

---

## Custom JSON Encoding

### Using `default` Parameter

```python
import json
from datetime import datetime, date
from decimal import Decimal

class CustomEncoder(json.JSONEncoder):
    """Custom JSON encoder for non-standard types"""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, complex):
            return {"real": obj.real, "imag": obj.imag}
        
        return super().default(obj)

# Usage
data = {
    "name": "Alice",
    "created": datetime.now(),
    "birthday": date(1990, 5, 15),
    "price": Decimal('19.99'),
    "complex": 3 + 4j
}

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_str)
```

### Using `default` Function

```python
import json
from datetime import datetime

def json_serializer(obj):
    """Simple serializer function"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    raise TypeError(f"Type {type(obj)} not serializable")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

data = {
    "now": datetime.now(),
    "person": Person("Alice", 30)
}

json_str = json.dumps(data, default=json_serializer, indent=2)
print(json_str)
```

---

## Custom JSON Decoding

### Using `object_hook` Parameter

```python
import json
from datetime import datetime

def json_decoder(dct):
    """Custom decoder for specific patterns"""
    # Check for datetime fields
    if 'created' in dct:
        try:
            dct['created'] = datetime.fromisoformat(dct['created'])
        except (ValueError, TypeError):
            pass
    
    # Check for complex numbers
    if 'real' in dct and 'imag' in dct and len(dct) == 2:
        return complex(dct['real'], dct['imag'])
    
    return dct

json_str = '''
{
    "name": "Alice",
    "created": "2024-01-15T10:30:00",
    "complex": {"real": 3, "imag": 4}
}
'''

data = json.loads(json_str, object_hook=json_decoder)
print(data)
print(f"Created type: {type(data['created'])}")
print(f"Complex: {data['complex']}")
```

### Using `object_pairs_hook`

```python
import json
from collections import OrderedDict

# Preserve order (pre-Python 3.7)
json_str = '{"b": 1, "a": 2, "c": 3}'

# Regular load (order not guaranteed)
data = json.loads(json_str)
print(data)  # {'b': 1, 'a': 2, 'c': 3} (order depends on Python version)

# Use OrderedDict to preserve order
data = json.loads(json_str, object_pairs_hook=OrderedDict)
print(data)  # OrderedDict([('b', 1), ('a', 2), ('c', 3)])

# Custom hook for duplicate keys
def handle_duplicates(pairs):
    """Handle duplicate keys by keeping last value"""
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

json_with_dupes = '{"a": 1, "b": 2, "a": 3}'
data = json.loads(json_with_dupes, object_pairs_hook=handle_duplicates)
print(data)  # {'a': 3, 'b': 2}
```

---

## Real-World Examples

### Example 1: Configuration Manager

```python
import json
import os

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load()
    
    def load(self):
        """Load configuration from file"""
        if not os.path.exists(self.config_file):
            return self.get_defaults()
        
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Invalid JSON in {self.config_file}, using defaults")
            return self.get_defaults()
    
    def save(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"Config saved to {self.config_file}")
    
    def get_defaults(self):
        """Return default configuration"""
        return {
            "app": {
                "name": "MyApp",
                "version": "1.0.0",
                "debug": False
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp_db",
                "user": "admin",
                "password": "secret"
            },
            "logging": {
                "level": "INFO",
                "file": "app.log"
            }
        }
    
    def get(self, key, default=None):
        """Get value using dot notation"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        return value
    
    def set(self, key, value):
        """Set value using dot notation"""
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        self.save()
    
    def display(self):
        """Display configuration"""
        print(json.dumps(self.config, indent=2))

# Usage
config = ConfigManager('app_config.json')
print(f"App name: {config.get('app.name')}")
print(f"Debug mode: {config.get('app.debug')}")

config.set('app.debug', True)
config.set('database.port', 5433)

config.display()
```

### Example 2: API Response Handler

```python
import json
import requests
from datetime import datetime

class APIHandler:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint, params=None):
        """Make GET request and parse JSON response"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return self.parse_response(response.json())
        except requests.RequestException as e:
            return {"error": str(e)}
        except json.JSONDecodeError as e:
            return {"error": f"Invalid JSON response: {e}"}
    
    def parse_response(self, data):
        """Recursively parse JSON data"""
        if isinstance(data, dict):
            return {k: self.parse_response(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.parse_response(item) for item in data]
        elif isinstance(data, str):
            # Try to parse date strings
            try:
                return datetime.fromisoformat(data)
            except ValueError:
                return data
        else:
            return data
    
    def post(self, endpoint, data=None):
        """Make POST request with JSON data"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

# Usage (simulated)
api = APIHandler("https://api.example.com")

# Simulated response
response = {
    "user": {
        "id": 123,
        "name": "Alice",
        "created_at": "2024-01-15T10:30:00",
        "tags": ["premium", "verified"]
    },
    "status": "success"
}

print("Parsed response:")
print(json.dumps(response, indent=2))
```

### Example 3: JSON Schema Validator

```python
import json
from typing import Any, Dict, List

class JSONValidator:
    """Simple JSON schema validator"""
    
    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema
        self.errors: List[str] = []
    
    def validate(self, data: Any, path: str = "") -> bool:
        """Validate data against schema"""
        self.errors.clear()
        return self._validate(data, self.schema, path)
    
    def _validate(self, data: Any, schema: Dict[str, Any], path: str) -> bool:
        valid = True
        
        # Type validation
        if 'type' in schema:
            expected_type = schema['type']
            if not self._check_type(data, expected_type):
                self.errors.append(f"{path}: Expected {expected_type}, got {type(data).__name__}")
                return False
        
        # Required fields (for objects)
        if 'required' in schema and isinstance(data, dict):
            for field in schema['required']:
                if field not in data:
                    self.errors.append(f"{path}.{field}: Missing required field")
                    valid = False
        
        # Properties validation (for objects)
        if 'properties' in schema and isinstance(data, dict):
            for prop, prop_schema in schema['properties'].items():
                prop_path = f"{path}.{prop}" if path else prop
                if prop in data:
                    if not self._validate(data[prop], prop_schema, prop_path):
                        valid = False
        
        # Items validation (for arrays)
        if 'items' in schema and isinstance(data, list):
            items_schema = schema['items']
            for i, item in enumerate(data):
                item_path = f"{path}[{i}]"
                if not self._validate(item, items_schema, item_path):
                    valid = False
        
        return valid
    
    def _check_type(self, data: Any, expected_type: str) -> bool:
        """Check if data matches expected type"""
        type_map = {
            'string': str,
            'number': (int, float),
            'integer': int,
            'boolean': bool,
            'array': list,
            'object': dict,
            'null': type(None)
        }
        
        expected = type_map.get(expected_type)
        if expected is None:
            return True
        
        return isinstance(data, expected)
    
    def get_errors(self) -> List[str]:
        return self.errors

# Define schema
user_schema = {
    "type": "object",
    "required": ["name", "age", "email"],
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string"},
        "is_active": {"type": "boolean"},
        "tags": {"type": "array", "items": {"type": "string"}},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "zip": {"type": "string"}
            }
        }
    }
}

# Test data
valid_user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "is_active": True,
    "tags": ["premium", "verified"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

invalid_user = {
    "name": "Bob",
    "age": "25",  # Wrong type
    # Missing email
    "is_active": "true",  # Wrong type
    "tags": "premium"  # Wrong type (should be array)
}

validator = JSONValidator(user_schema)

print("Valid user:")
valid = validator.validate(valid_user)
print(f"Valid: {valid}")
if not valid:
    for error in validator.get_errors():
        print(f"  Error: {error}")

print("\nInvalid user:")
valid = validator.validate(invalid_user)
print(f"Valid: {valid}")
if not valid:
    for error in validator.get_errors():
        print(f"  Error: {error}")
```

### Example 4: Data Export/Import Tool

```python
import json
import csv
from datetime import datetime

class DataConverter:
    @staticmethod
    def json_to_csv(json_file, csv_file):
        """Convert JSON file to CSV"""
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        if not data:
            print("No data to convert")
            return
        
        # Handle both single object and array
        if isinstance(data, dict):
            data = [data]
        
        # Get all unique keys
        keys = set()
        for item in data:
            keys.update(item.keys())
        keys = sorted(keys)
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Converted {json_file} to {csv_file}")
    
    @staticmethod
    def csv_to_json(csv_file, json_file):
        """Convert CSV file to JSON"""
        data = []
        
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Try to convert numeric values
                converted = {}
                for key, value in row.items():
                    if value.isdigit():
                        converted[key] = int(value)
                    elif value.replace('.', '').isdigit():
                        converted[key] = float(value)
                    elif value.lower() == 'true':
                        converted[key] = True
                    elif value.lower() == 'false':
                        converted[key] = False
                    else:
                        converted[key] = value
                data.append(converted)
        
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Converted {csv_file} to {json_file}")
    
    @staticmethod
    def json_to_jsonl(json_file, jsonl_file):
        """Convert JSON array to JSONL (JSON Lines) format"""
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            data = [data]
        
        with open(jsonl_file, 'w') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')
        
        print(f"Converted {json_file} to {jsonl_file}")
    
    @staticmethod
    def jsonl_to_json(jsonl_file, json_file):
        """Convert JSONL to JSON array"""
        data = []
        
        with open(jsonl_file, 'r') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
        
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Converted {jsonl_file} to {json_file}")

# Usage
sample_data = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Save sample JSON
with open('data.json', 'w') as f:
    json.dump(sample_data, f, indent=2)

# Convert formats
DataConverter.json_to_csv('data.json', 'data.csv')
DataConverter.csv_to_json('data.csv', 'data_from_csv.json')
DataConverter.json_to_jsonl('data.json', 'data.jsonl')
```

### Example 5: JSON Pretty Printer

```python
import json
import sys
import argparse

class JSONPrettyPrinter:
    @staticmethod
    def print_json(data, indent=2, sort_keys=False, colors=True):
        """Print JSON with syntax highlighting"""
        json_str = json.dumps(data, indent=indent, sort_keys=sort_keys)
        
        if colors and sys.stdout.isatty():
            # Add ANSI color codes
            colors = {
                '"': '\033[92m',   # Green for strings
                ':': '\033[93m',   # Yellow for keys
                '{': '\033[96m',   # Cyan for braces
                '}': '\033[96m',
                '[': '\033[96m',
                ']': '\033[96m',
                'true': '\033[95m',  # Magenta for booleans
                'false': '\033[95m',
                'null': '\033[91m'   # Red for null
            }
            reset = '\033[0m'
            
            # Simple highlighting
            for token, color in colors.items():
                json_str = json_str.replace(token, f"{color}{token}{reset}")
        
        print(json_str)
    
    @staticmethod
    def print_from_file(filename, indent=2, sort_keys=False):
        """Print JSON file content"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            JSONPrettyPrinter.print_json(data, indent, sort_keys)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
    
    @staticmethod
    def minify(json_str):
        """Remove whitespace from JSON"""
        data = json.loads(json_str)
        return json.dumps(data, separators=(',', ':'))

# Usage
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "swimming"],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}

print("Pretty printed JSON:")
JSONPrettyPrinter.print_json(data, indent=2, colors=False)

print("\nMinified JSON:")
minified = JSONPrettyPrinter.minify(json.dumps(data))
print(minified)
```

---

## Practice Exercises

### Beginner Level

1. **Dict to JSON**
   ```python
   # Convert Python dictionary to JSON string
   ```

2. **JSON to Dict**
   ```python
   # Parse JSON string to Python dictionary
   ```

3. **Save to File**
   ```python
   # Save Python object to JSON file
   ```

### Intermediate Level

4. **Pretty Print**
   ```python
   # Format JSON with indentation
   ```

5. **JSON Validator**
   ```python
   # Check if string is valid JSON
   ```

6. **Merge JSON Files**
   ```python
   # Merge multiple JSON files into one
   ```

### Advanced Level

7. **JSON Schema Validator**
   ```python
   # Validate JSON against schema
   ```

8. **Custom Encoder**
   ```python
   # Handle datetime and Decimal types
   ```

9. **JSON Diff Tool**
   ```python
   # Compare two JSON objects and show differences
   ```

---

## Quick Reference Card

```python
import json

# Serialization (Python → JSON)
json.dumps(obj)                     # To string
json.dumps(obj, indent=2)           # Pretty print
json.dumps(obj, sort_keys=True)     # Sorted keys
json.dumps(obj, default=func)       # Custom serializer
json.dump(obj, file)                # To file

# Deserialization (JSON → Python)
json.loads(string)                  # From string
json.load(file)                     # From file
json.loads(string, object_hook=func) # Custom decoder

# Type mapping
# JSON          → Python
# object        → dict
# array         → list
# string        → str
# number        → int/float
# true          → True
# false         → False
# null          → None

# Common patterns
with open('file.json', 'r') as f:
    data = json.load(f)

with open('file.json', 'w') as f:
    json.dump(data, f, indent=2)

# Custom encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Custom decoder
def custom_decoder(dct):
    if 'date' in dct:
        dct['date'] = datetime.fromisoformat(dct['date'])
    return dct
```

---

## Next Step

- Move to [08_re.md](08_re.md) to learn about regular expressions.

---

*Master the JSON module for data interchange and configuration management! 🐍✨*
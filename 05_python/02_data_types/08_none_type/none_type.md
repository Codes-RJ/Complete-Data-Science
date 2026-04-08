# 📘 NONE TYPE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is None?](#what-is-none)
2. [None Characteristics](#none-characteristics)
3. [Common Use Cases](#common-use-cases)
4. [None in Functions](#none-in-functions)
5. [None in Data Structures](#none-in-data-structures)
6. [None vs Other Falsy Values](#none-vs-other-falsy-values)
7. [Real-World Examples](#real-world-examples)
8. [Common Pitfalls](#common-pitfalls)
9. [Performance Tips](#performance-tips)
10. [Practice Exercises](#practice-exercises)

---

## What is None?

**None** is a singleton object in Python that represents the absence of a value. It is the sole instance of the `NoneType` class.

```python
# None is a singleton
a = None
b = None
print(a is b)      # True (same object)
print(id(a))       # Same memory address
print(id(b))       # Same memory address

# None type
print(type(None))  # <class 'NoneType'>
print(isinstance(None, type(None)))  # True

# Cannot create new None instances
try:
    n = NoneType()
except NameError:
    print("NoneType is not directly accessible")

# None is falsy
print(bool(None))  # False
```

**Key Characteristics:**
- Singleton (only one instance exists)
- Immutable (cannot be modified)
- Falsy in boolean contexts
- Represents "no value" or "null"
- Used as default for optional parameters
- Used as sentinel for missing data

---

## None Characteristics

### Singleton Property

```python
# All None references point to same object
x = None
y = None
z = None

print(x is y)      # True
print(y is z)      # True
print(x is z)      # True

# Memory address is same
print(id(x))       # 140735217596752
print(id(y))       # 140735217596752

# None is a built-in constant
import builtins
print(builtins.None is None)  # True
```

### Immutability

```python
# None cannot be modified
try:
    None.value = 42
except AttributeError:
    print("Cannot add attributes to None")

# None is immutable
# You cannot change it (but you can reassign variables)
x = None
x = 42  # This reassigns x, doesn't modify None
```

### Type Information

```python
# NoneType is not directly available in builtins
try:
    print(NoneType)
except NameError:
    print("NoneType is not a built-in name")

# But you can get it
none_type = type(None)
print(none_type)  # <class 'NoneType'>

# Check if something is None
def is_none(value):
    return type(value) is type(None)

print(is_none(None))   # True
print(is_none(42))     # False
```

---

## Common Use Cases

### 1. Default Arguments for Mutable Types

```python
# ❌ WRONG - Mutable default argument
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(add_item_bad(1))  # [1]
print(add_item_bad(2))  # [1, 2] (unexpected!)

# ✅ CORRECT - Use None as default
def add_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_good(1))  # [1]
print(add_item_good(2))  # [2] (correct!)

# For dictionaries
def update_config(key, value, config=None):
    if config is None:
        config = {}
    config[key] = value
    return config

print(update_config("debug", True))     # {'debug': True}
print(update_config("port", 8080))      # {'port': 8080}
```

### 2. Optional Parameters

```python
# Function with optional parameters
def greet(name, greeting=None, punctuation="!"):
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice"))                    # "Hello, Alice!"
print(greet("Bob", "Hi"))                # "Hi, Bob!"
print(greet("Charlie", "Hey", "?"))      # "Hey, Charlie?"
print(greet("David", punctuation="!!"))  # "Hello, David!!"

# Multiple optional parameters
def create_user(name, email=None, phone=None, address=None):
    user = {"name": name}
    if email is not None:
        user["email"] = email
    if phone is not None:
        user["phone"] = phone
    if address is not None:
        user["address"] = address
    return user

print(create_user("Alice", email="alice@example.com"))
print(create_user("Bob", phone="555-1234"))
```

### 3. Sentinel for Missing Values

```python
# Search function returning None for not found
def find_user(users, name):
    for user in users:
        if user['name'] == name:
            return user
    return None

users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

user = find_user(users, 'Bob')
if user is None:
    print("User not found")
else:
    print(f"Found: {user}")

user = find_user(users, 'Unknown')
if user is None:
    print("User not found")  # This prints
```

### 4. Lazy Initialization

```python
class DatabaseConnection:
    def __init__(self):
        self._connection = None
    
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._create_connection()
        return self._connection
    
    def _create_connection(self):
        print("Creating database connection...")
        return "DB Connection Object"
    
    def close(self):
        if self._connection is not None:
            print("Closing connection...")
            self._connection = None

# Usage
db = DatabaseConnection()
print(db.connection)  # Creates connection
print(db.connection)  # Uses existing
db.close()
print(db.connection)  # Re-creates connection
```

### 5. Cache Implementation

```python
class SimpleCache:
    def __init__(self):
        self._cache = {}
    
    def get(self, key):
        """Get value from cache, returns None if not found"""
        return self._cache.get(key)
    
    def set(self, key, value):
        """Set value in cache"""
        self._cache[key] = value
    
    def get_or_compute(self, key, compute_func):
        """Get from cache or compute and store"""
        value = self.get(key)
        if value is None:
            value = compute_func()
            self.set(key, value)
        return value

# Usage
cache = SimpleCache()

def expensive_computation():
    print("Computing...")
    return 42

result = cache.get_or_compute("key", expensive_computation)  # Computes
print(result)  # 42

result2 = cache.get_or_compute("key", expensive_computation)  # From cache
print(result2)  # 42 (no computation)
```

### 6. Removing Dictionary Keys Safely

```python
# Safe removal with pop()
config = {"host": "localhost", "port": 8080, "debug": True}

# Remove existing key
port = config.pop("port", None)
print(port)      # 8080
print(config)    # {'host': 'localhost', 'debug': True}

# Remove non-existing key (no error)
ssl = config.pop("ssl", None)
print(ssl)       # None
print(config)    # unchanged

# Using None as default for get()
host = config.get("host")
print(host)      # "localhost"

missing = config.get("missing")
print(missing)   # None
```

---

## None in Functions

### Functions Returning None

```python
# Functions without return statement return None
def print_message(msg):
    print(msg)
    # Implicitly returns None

result = print_message("Hello")
print(result)  # None

# Explicitly returning None
def do_nothing():
    return None

print(do_nothing())  # None

# Functions that modify in-place often return None
my_list = [1, 2, 3]
result = my_list.append(4)
print(result)  # None

result = my_list.sort()
print(result)  # None
```

### Type Hints with None (Optional)

```python
from typing import Optional

# Function that may return None
def find_user(user_id: int) -> Optional[dict]:
    """Returns user dict or None if not found"""
    if user_id in database:
        return database[user_id]
    return None

# Function with optional parameter
def process_data(data: Optional[list] = None) -> list:
    if data is None:
        data = []
    return data

# Python 3.10+ alternative (Union)
def find_user(user_id: int) -> dict | None:
    """Returns user dict or None if not found"""
    return database.get(user_id)
```

### Default Value Pattern

```python
# Simple default
def connect(host, port=None):
    if port is None:
        port = 5432
    return f"{host}:{port}"

print(connect("localhost"))      # localhost:5432
print(connect("localhost", 8080)) # localhost:8080

# One-line default (be careful with mutable types)
def connect(host, port=None):
    port = port or 5432  # Only works if 0 is not valid
    return f"{host}:{port}"

# When 0 is a valid value
def set_timeout(timeout=None):
    if timeout is None:
        timeout = 30  # Default
    # timeout can be 0 (no timeout)
    return timeout

print(set_timeout())     # 30
print(set_timeout(0))    # 0 (not replaced by default)
```

---

## None in Data Structures

### Lists with None

```python
# None can be stored in lists
data = [1, None, 3, None, 5]
print(data)  # [1, None, 3, None, 5]

# Filter out None values
filtered = [x for x in data if x is not None]
print(filtered)  # [1, 3, 5]

# Replace None with default
clean = [x if x is not None else 0 for x in data]
print(clean)  # [1, 0, 3, 0, 5]

# Using None as placeholder
size = 5
array = [None] * size
print(array)  # [None, None, None, None, None]
array[2] = 42
print(array)  # [None, None, 42, None, None]
```

### Dictionaries with None

```python
# None as value (valid)
config = {
    "host": "localhost",
    "port": None,  # Not set yet
    "debug": True
}

print(config["port"])  # None

# Check if key exists with None value
if "port" in config:
    print("Port key exists")  # This prints
    if config["port"] is not None:
        print(f"Port: {config['port']}")
    else:
        print("Port not configured yet")

# Using None as default with get()
value = config.get("missing", None)
print(value)  # None

# Removing keys with None values
clean_config = {k: v for k, v in config.items() if v is not None}
print(clean_config)  # {'host': 'localhost', 'debug': True}
```

### Sets with None

```python
# None can be in sets
my_set = {1, 2, None, 3}
print(my_set)  # {1, 2, 3, None}

# Check for None
if None in my_set:
    print("None is in the set")

# Remove None
my_set.discard(None)
print(my_set)  # {1, 2, 3}
```

### Tuples with None

```python
# Tuples can contain None
result = (42, None, "success")
print(result)  # (42, None, 'success')

# Unpacking with None
value, error, status = result
if error is None:
    print("No error")
```

---

## None vs Other Falsy Values

### Comparison Table

```python
values = [None, False, 0, 0.0, "", [], (), {}]

print("Value    | bool() | == None | is None")
print("-" * 45)
for val in values:
    print(f"{repr(val):8} | {bool(val):5} | {val == None:7} | {val is None:7}")

# Output:
# None     | False | True    | True
# False    | False | False   | False
# 0        | False | False   | False
# 0.0      | False | False   | False
# ''       | False | False   | False
# []       | False | False   | False
# ()       | False | False   | False
# {}       | False | False   | False
```

### Why Distinction Matters

```python
def process_data(data):
    # This is WRONG - treats 0, "", [] as missing
    if not data:
        return "No data"
    return f"Processing: {data}"

print(process_data(None))    # "No data"
print(process_data(0))       # "No data" (but 0 is valid!)
print(process_data(""))      # "No data" (but empty string might be valid)
print(process_data([]))      # "No data" (but empty list might be valid)

# ✅ CORRECT - Explicit None check
def process_data_correct(data):
    if data is None:
        return "No data"
    return f"Processing: {data}"

print(process_data_correct(None))    # "No data"
print(process_data_correct(0))       # "Processing: 0"
print(process_data_correct(""))      # "Processing: "
print(process_data_correct([]))      # "Processing: []"
```

### When to Use Which

```python
# Use None for: Missing/optional values
def get_user(id):
    if id not in database:
        return None  # User doesn't exist

# Use False for: Boolean false state
is_active = False

# Use 0 for: Numeric zero
count = 0
temperature = 0.0

# Use "" for: Empty string
name = ""
message = ""

# Use [] for: Empty list
items = []
queue = []

# Use {} for: Empty dict
config = {}
cache = {}

# Use () for: Empty tuple
coordinates = ()
```

---

## Real-World Examples

### Example 1: Configuration Loader with Fallback

```python
import json
from typing import Optional, Any

class ConfigLoader:
    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file
        self._config = None
        self._defaults = {
            "host": "localhost",
            "port": 8080,
            "debug": False,
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "app_db"
            }
        }
    
    def load(self) -> dict:
        """Load configuration, returns dict"""
        if self._config is not None:
            return self._config
        
        if self.config_file is None:
            self._config = self._defaults.copy()
            return self._config
        
        try:
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self._config = self._merge_config(self._defaults, user_config)
        except FileNotFoundError:
            print(f"Config file {self.config_file} not found, using defaults")
            self._config = self._defaults.copy()
        except json.JSONDecodeError:
            print(f"Invalid JSON in {self.config_file}, using defaults")
            self._config = self._defaults.copy()
        
        return self._config
    
    def _merge_config(self, defaults: dict, overrides: dict) -> dict:
        """Deep merge two dictionaries"""
        result = defaults.copy()
        for key, value in overrides.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by dot notation"""
        if self._config is None:
            self.load()
        
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value if value is not None else default
    
    def reload(self) -> None:
        """Reload configuration"""
        self._config = None
        return self.load()

# Usage
config = ConfigLoader()

# Load config
settings = config.load()
print(f"Loaded config: {settings.keys()}")

# Get values with defaults
host = config.get("host", "127.0.0.1")
port = config.get("port", 3000)
debug = config.get("debug", True)
db_host = config.get("database.host", "127.0.0.1")

print(f"Host: {host}")
print(f"Port: {port}")
print(f"Debug: {debug}")
print(f"DB Host: {db_host}")

# Missing key returns None
missing = config.get("nonexistent.key")
print(f"Missing: {missing}")

# With default
missing_with_default = config.get("nonexistent.key", "default_value")
print(f"Missing with default: {missing_with_default}")
```

### Example 2: Binary Tree Implementation

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        """Insert value into BST"""
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        # Equal values not inserted (BST property)
    
    def search(self, value):
        """Search for value, return node or None"""
        if value == self.value:
            return self
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        return None
    
    def find_min(self):
        """Find minimum value node"""
        if self.left is None:
            return self
        return self.left.find_min()
    
    def find_max(self):
        """Find maximum value node"""
        if self.right is None:
            return self
        return self.right.find_max()
    
    def delete(self, value):
        """Delete value from BST"""
        if self is None:
            return None
        
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            # Found the node to delete
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Node with two children
            successor = self.right.find_min()
            self.value = successor.value
            self.right = self.right.delete(successor.value)
        
        return self
    
    def inorder(self, result=None):
        """Inorder traversal"""
        if result is None:
            result = []
        
        if self.left is not None:
            self.left.inorder(result)
        result.append(self.value)
        if self.right is not None:
            self.right.inorder(result)
        
        return result
    
    def __str__(self):
        return f"TreeNode({self.value})"

# Usage
print("BINARY SEARCH TREE")
print("=" * 40)

# Create tree
root = TreeNode(50)
values = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]

for val in values:
    root.insert(val)

print("Inorder traversal (sorted):", root.inorder())

# Search
search_val = 40
result = root.search(search_val)
if result is None:
    print(f"{search_val} not found")
else:
    print(f"Found: {result}")

search_val = 100
result = root.search(search_val)
if result is None:
    print(f"{search_val} not found")

# Min and max
min_node = root.find_min()
max_node = root.find_max()
print(f"Minimum: {min_node.value}")
print(f"Maximum: {max_node.value}")

# Delete
delete_val = 30
print(f"\nDeleting {delete_val}...")
root = root.delete(delete_val)
print(f"Inorder after deletion: {root.inorder()}")
```

### Example 3: Cache with Expiration

```python
import time
from datetime import datetime
from typing import Optional, Any, Tuple

class TimedCache:
    def __init__(self, default_ttl: Optional[int] = 300):
        """
        Initialize cache with default TTL in seconds
        If default_ttl is None, entries never expire
        """
        self._cache = {}
        self.default_ttl = default_ttl
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Set value in cache with optional TTL"""
        if ttl is None:
            ttl = self.default_ttl
        
        expires_at = None if ttl is None else time.time() + ttl
        self._cache[key] = (value, expires_at)
    
    def get(self, key: str) -> Optional[Any]:
        """Get value from cache, returns None if expired or not found"""
        entry = self._cache.get(key)
        
        if entry is None:
            return None
        
        value, expires_at = entry
        
        if expires_at is not None and time.time() > expires_at:
            # Entry expired
            del self._cache[key]
            return None
        
        return value
    
    def get_or_set(self, key: str, compute_func, ttl: Optional[int] = None) -> Any:
        """Get from cache or compute and store"""
        value = self.get(key)
        
        if value is None:
            value = compute_func()
            self.set(key, value, ttl)
        
        return value
    
    def delete(self, key: str) -> bool:
        """Delete key from cache, returns True if existed"""
        if key in self._cache:
            del self._cache[key]
            return True
        return False
    
    def clear(self) -> None:
        """Clear all cache entries"""
        self._cache.clear()
    
    def cleanup(self) -> int:
        """Remove all expired entries, returns count removed"""
        current_time = time.time()
        expired_keys = [
            key for key, (_, expires_at) in self._cache.items()
            if expires_at is not None and current_time > expires_at
        ]
        
        for key in expired_keys:
            del self._cache[key]
        
        return len(expired_keys)
    
    def stats(self) -> dict:
        """Get cache statistics"""
        current_time = time.time()
        total = len(self._cache)
        expired = sum(
            1 for _, expires_at in self._cache.values()
            if expires_at is not None and current_time > expires_at
        )
        
        return {
            "total_entries": total,
            "expired_entries": expired,
            "valid_entries": total - expired
        }

# Usage
cache = TimedCache(default_ttl=2)  # 2 second TTL

print("CACHE WITH EXPIRATION")
print("=" * 40)

# Set values
cache.set("key1", "value1")
cache.set("key2", "value2", ttl=1)  # 1 second TTL
cache.set("key3", "value3", ttl=None)  # Never expires

print("Initial stats:", cache.stats())

# Get values
print(f"key1: {cache.get('key1')}")
print(f"key2: {cache.get('key2')}")
print(f"key3: {cache.get('key3')}")
print(f"missing: {cache.get('missing')}")

# Wait for expiration
print("\nWaiting for expiration...")
time.sleep(3)

# Get after expiration
print(f"key1 (expired): {cache.get('key1')}")
print(f"key2 (expired): {cache.get('key2')}")
print(f"key3 (still valid): {cache.get('key3')}")

print("Stats after expiration:", cache.stats())

# Cleanup
removed = cache.cleanup()
print(f"Removed {removed} expired entries")
print("Final stats:", cache.stats())

# get_or_set
def expensive_computation():
    print("Computing expensive value...")
    return 42

value = cache.get_or_set("computed", expensive_computation)
print(f"Computed value: {value}")

value2 = cache.get_or_set("computed", expensive_computation)
print(f"Cached value: {value2}")  # No computation
```

### Example 4: Lazy Property Decorator

```python
class lazy_property:
    """Decorator that creates a lazy property"""
    
    def __init__(self, function):
        self.function = function
        self.name = function.__name__
    
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        value = self.function(obj)
        setattr(obj, self.name, value)
        return value

class DatabaseQuery:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self._connection = None
        self._schema = None
        self._tables = None
    
    @property
    def connection(self):
        """Lazy connection property"""
        if self._connection is None:
            print("Creating database connection...")
            self._connection = f"Connected to {self.connection_string}"
        return self._connection
    
    @lazy_property
    def schema(self):
        """Lazy schema property using decorator"""
        print("Loading database schema...")
        # Simulate expensive operation
        return {"tables": ["users", "products", "orders"]}
    
    @lazy_property
    def tables(self):
        """Lazy tables property"""
        print("Loading table list...")
        # Simulate expensive operation
        return ["users", "products", "orders"]
    
    def reset(self):
        """Reset all lazy properties"""
        self._connection = None
        self._schema = None
        self._tables = None

# Usage
print("LAZY PROPERTIES")
print("=" * 40)

db = DatabaseQuery("postgresql://localhost/mydb")

# First access creates connection
print(db.connection)
print(db.connection)  # Second access uses cached

# Lazy properties
print("\nFirst access to schema:")
print(db.schema)  # Computes
print(db.schema)  # Uses cached

print("\nFirst access to tables:")
print(db.tables)  # Computes
print(db.tables)  # Uses cached

# Reset
print("\nResetting...")
db.reset()
print(db.connection)  # Creates new connection
```

### Example 5: Optional Chain Implementation

```python
class Optional:
    """Simple Optional type implementation"""
    
    def __init__(self, value):
        self._value = value
    
    def map(self, func):
        """Apply function if value is not None"""
        if self._value is None:
            return self
        return Optional(func(self._value))
    
    def flat_map(self, func):
        """Apply function that returns Optional"""
        if self._value is None:
            return self
        return func(self._value)
    
    def get_or_else(self, default):
        """Get value or default"""
        return self._value if self._value is not None else default
    
    def or_else(self, func):
        """Return value or compute alternative"""
        if self._value is not None:
            return self
        return Optional(func())
    
    def is_present(self):
        """Check if value exists"""
        return self._value is not None
    
    def __str__(self):
        return f"Optional({self._value})"

# Safe access utilities
def safe_get(obj, *keys):
    """Safely get nested dictionary values"""
    current = obj
    for key in keys:
        if current is None:
            return None
        current = current.get(key)
    return current

def safe_attr(obj, *attrs):
    """Safely get nested attributes"""
    current = obj
    for attr in attrs:
        if current is None:
            return None
        current = getattr(current, attr, None)
    return current

# Usage
print("OPTIONAL CHAINING")
print("=" * 40)

# Nested dictionary
data = {
    "user": {
        "profile": {
            "address": {
                "city": "New York",
                "zip": "10001"
            },
            "phone": None
        }
    }
}

# Safe nested access
city = safe_get(data, "user", "profile", "address", "city")
phone = safe_get(data, "user", "profile", "phone")
missing = safe_get(data, "user", "profile", "nonexistent")

print(f"City: {city}")
print(f"Phone: {phone}")
print(f"Missing: {missing}")

# Using Optional class
result = Optional(data)\
    .map(lambda d: d.get("user"))\
    .map(lambda u: u.get("profile"))\
    .map(lambda p: p.get("address"))\
    .map(lambda a: a.get("city"))

print(f"Optional result: {result}")
print(f"Value or default: {result.get_or_else('Unknown')}")

# Chain with fallback
def get_city(data):
    city = safe_get(data, "user", "profile", "address", "city")
    if city is None:
        return "Unknown"
    return city

print(f"Function result: {get_city(data)}")
```

### Example 6: Retry Mechanism with None

```python
import random
import time
from typing import Optional, Callable, Any

class RetryConfig:
    def __init__(
        self,
        max_attempts: int = 3,
        delay: float = 1.0,
        backoff: float = 2.0,
        exceptions: tuple = (Exception,)
    ):
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff = backoff
        self.exceptions = exceptions

def retry(
    config: Optional[RetryConfig] = None,
    on_retry: Optional[Callable[[int, Exception], None]] = None
):
    """Retry decorator with optional configuration"""
    if config is None:
        config = RetryConfig()
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = config.delay
            
            for attempt in range(1, config.max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    if result is not None:
                        return result
                    # If function returns None, treat as failure
                    if attempt == config.max_attempts:
                        return None
                except config.exceptions as e:
                    last_exception = e
                    if on_retry is not None:
                        on_retry(attempt, e)
                    
                    if attempt == config.max_attempts:
                        raise
                    
                    time.sleep(current_delay)
                    current_delay *= config.backoff
                else:
                    # No exception but returned None
                    if attempt < config.max_attempts:
                        if on_retry is not None:
                            on_retry(attempt, Exception("Function returned None"))
                        time.sleep(current_delay)
                        current_delay *= config.backoff
            
            return None
        
        return wrapper
    return decorator

# Example functions
@retry()
def unstable_network_call():
    """Simulate unstable network call"""
    if random.random() < 0.7:
        print("Network call failed!")
        raise ConnectionError("Network error")
    return "Success!"

@retry(config=RetryConfig(max_attempts=5, delay=0.5))
def database_query():
    """Simulate database query that sometimes returns None"""
    if random.random() < 0.5:
        print("Query returned no results")
        return None
    return {"data": "result"}

@retry(
    config=RetryConfig(max_attempts=3, delay=0.2),
    on_retry=lambda attempt, e: print(f"Retry {attempt}: {e}")
)
def flaky_service():
    """Flaky service with retry logging"""
    if random.random() < 0.6:
        raise ValueError("Service temporarily unavailable")
    return "Service response"

# Usage
print("RETRY MECHANISM")
print("=" * 40)

print("\n1. Unstable network call:")
result = unstable_network_call()
print(f"Final result: {result}")

print("\n2. Database query (may return None):")
result = database_query()
print(f"Final result: {result}")

print("\n3. Flaky service with logging:")
result = flaky_service()
print(f"Final result: {result}")
```

---

## Common Pitfalls

### Pitfall 1: Using `==` Instead of `is`

```python
# ❌ WRONG - Using == to check for None
def process(value):
    if value == None:  # Works but not recommended
        return "No value"
    return value

# ✅ CORRECT - Using is
def process(value):
    if value is None:
        return "No value"
    return value

# Why? Some objects can be equal to None
class AlwaysEqual:
    def __eq__(self, other):
        return True

weird = AlwaysEqual()
print(weird == None)   # True
print(weird is None)   # False (correct)
```

### Pitfall 2: Using `not value` to Check for None

```python
# ❌ WRONG - Treats 0, "", [] as missing
def get_length(data):
    if not data:  # Wrong! None, 0, "", [] all trigger this
        return 0
    return len(data)

print(get_length(None))   # 0 (correct)
print(get_length(0))      # 0 (but 0 has no length)
print(get_length(""))     # 0 (correct)
print(get_length([]))     # 0 (correct)

# ✅ CORRECT - Explicit None check
def get_length(data):
    if data is None:
        return 0
    return len(data)

print(get_length(None))   # 0
print(get_length(0))      # TypeError (as expected)
```

### Pitfall 3: Mutable Default Arguments

```python
# ❌ WRONG - Mutable default
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] (unexpected!)

# ✅ CORRECT - None default
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [2] (correct!)
```

### Pitfall 4: Returning None vs Raising Exception

```python
# ❌ BAD - Returning None for errors
def divide(a, b):
    if b == 0:
        return None
    return a / b

result = divide(10, 0)
if result is None:
    print("Error")  # Error message lost

# ✅ GOOD - Raise exception for errors
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

---

## Performance Tips

### None Comparison Speed

```python
import timeit

x = None

# 'is' is faster than '=='
time_is = timeit.timeit('x is None', globals=globals(), number=10000000)
time_eq = timeit.timeit('x == None', globals=globals(), number=10000000)

print(f"'is None': {time_is:.4f}s")
print(f"'== None': {time_eq:.4f}s")
print(f"'is' is {time_eq/time_is:.1f}x faster")
```

### None in Collections

```python
# None in list - fast membership
lst = [1, 2, 3, None, 4, 5]
print(None in lst)  # O(n) but fast

# None as dict key - O(1) lookup
d = {None: "value"}
print(d[None])  # Very fast
```

---

## Practice Exercises

### Beginner Level

1. **Safe Division**
   ```python
   # Write function that returns None for division by zero
   # Example: safe_divide(10, 2) → 5, safe_divide(10, 0) → None
   ```

2. **Find First Match**
   ```python
   # Find first element matching condition, return None if not found
   # Example: find_first([1,2,3,4], lambda x: x > 3) → 4
   ```

3. **Default Value**
   ```python
   # Function that returns default if value is None
   # Example: with_default(None, "default") → "default"
   ```

### Intermediate Level

4. **Optional Chain**
   ```python
   # Implement safe nested attribute access
   # Example: safe_attr(obj, "user", "profile", "name")
   ```

5. **Lazy Property**
   ```python
   # Implement lazy property decorator
   # Compute value only once on first access
   ```

6. **Cache with None Values**
   ```python
   # Cache that distinguishes between None and missing
   # get() returns None for cached None, raises for missing
   ```

### Advanced Level

7. **Optional Type**
   ```python
   # Implement full Optional type with map, flat_map, filter
   # Similar to Java/Scala Optional
   ```

8. **Retry with None**
   ```python
   # Implement retry that treats None as failure
   # Configurable max attempts and backoff
   ```

9. **Null Object Pattern**
   ```python
   # Implement Null Object Pattern using None
   # Create NullLogger, NullDatabase, etc.
   ```

---

## Quick Reference Card

```python
# None basics
None                        # Singleton null value
type(None)                  # <class 'NoneType'>
x is None                   # Check for None (preferred)
x is not None               # Check for not None

# Common patterns
def func(optional=None):    # Optional parameter
    if optional is None:    # Check for None
        optional = default   # Set default

# Return None
def find(items, target):
    for item in items:
        if item == target:
            return item
    return None              # Not found

# Safe dict access
value = d.get(key)          # Returns None if missing
value = d.pop(key, None)    # Safe removal

# Lazy initialization
self._cache = None
if self._cache is None:
    self._cache = compute()

# Type hints (Python 3.10+)
def func(x: int | None) -> str | None:
    pass

# Type hints (older)
from typing import Optional
def func(x: Optional[int]) -> Optional[str]:
    pass

# Falsy values (all False)
None, False, 0, 0.0, "", [], (), {}

# Check for None vs falsy
if value is None:           # Check for None only
if not value:               # Check for any falsy value
```
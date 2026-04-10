# 📘 TYPE CHECKING – isinstance() AND type() COMPLETE GUIDE

## 📌 Table of Contents
1. [Introduction to Type Checking](#introduction-to-type-checking)
2. [The type() Function](#the-type-function)
3. [The isinstance() Function](#the-isinstance-function)
4. [The issubclass() Function](#the-issubclass-function)
5. [Comparison: type() vs isinstance()](#comparison-type-vs-isinstance)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

---

## Introduction to Type Checking

Type checking allows you to determine and validate the data type of objects at runtime. Python provides three main functions for this purpose.

```python
# Three type checking functions
x = 42

# 1. type() - returns exact type
print(type(x))        # <class 'int'>

# 2. isinstance() - checks type including inheritance
print(isinstance(x, int))      # True
print(isinstance(x, object))   # True

# 3. issubclass() - checks class inheritance
print(issubclass(int, object))  # True
```

**When to Use Each:**
- `type()` - When exact type matching is required
- `isinstance()` - For most type checking (handles inheritance)
- `issubclass()` - For class hierarchy validation

---

## The type() Function

### Basic Usage

```python
# Get type of built-in types
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>
print(type([1, 2, 3]))    # <class 'list'>
print(type((1, 2, 3)))    # <class 'tuple'>
print(type({1, 2, 3}))    # <class 'set'>
print(type({"a": 1}))     # <class 'dict'>

# Get type of custom objects
class Person:
    pass

p = Person()
print(type(p))            # <class '__main__.Person'>
print(type(Person))       # <class 'type'>
```

### Type Comparison

```python
# Direct type comparison
def process_value(value):
    if type(value) == int:
        print("Processing integer")
    elif type(value) == str:
        print("Processing string")
    elif type(value) == list:
        print("Processing list")
    else:
        print("Unknown type")

process_value(42)     # Processing integer
process_value("hello") # Processing string
process_value([1,2,3]) # Processing list

# Comparing with multiple types
def check_type(value):
    if type(value) in (int, float, complex):
        print("Numeric type")
    elif type(value) in (str, bytes):
        print("String/bytes type")
    else:
        print("Other")

check_type(42)      # Numeric type
check_type(3.14)    # Numeric type
check_type("hello") # String/bytes type
```

### type() with Inheritance (Limitation)

```python
# type() does not consider inheritance
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(type(dog) == Dog)      # True
print(type(dog) == Animal)   # False (Dog is not Animal type)
print(type(cat) == Animal)   # False

# This is often NOT what you want
def process_animal(animal):
    if type(animal) == Animal:
        print("Processing animal")
    else:
        print("Not an animal")

process_animal(dog)  # Not an animal (unexpected!)
```

### Creating Types with type()

```python
# type() can also create new classes dynamically
# Syntax: type(name, bases, dict)

# Traditional class definition
class Person:
    def greet(self):
        return "Hello"

# Dynamic class creation
Person = type('Person', (), {'greet': lambda self: "Hello"})

p = Person()
print(p.greet())  # Hello

# With inheritance
class Animal:
    def speak(self):
        return "Sound"

Dog = type('Dog', (Animal,), {'breed': 'Unknown'})

d = Dog()
print(d.speak())  # Sound
print(d.breed)    # Unknown
```

---

## The isinstance() Function

### Basic Usage

```python
# Check single type
print(isinstance(42, int))      # True
print(isinstance(42, float))    # False
print(isinstance("hello", str)) # True
print(isinstance([1,2], list))  # True

# Check multiple types (tuple of types)
print(isinstance(42, (int, float)))      # True
print(isinstance(3.14, (int, float)))    # True
print(isinstance("hello", (int, str)))   # True
print(isinstance([1,2], (int, float)))   # False

# Works with inheritance
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog is subclass of Animal)
print(isinstance(dog, object))  # True (everything is object)
```

### isinstance() with Built-in Types

```python
# Numeric types
print(isinstance(42, int))          # True
print(isinstance(42, bool))         # False (bool is subclass of int)
print(isinstance(True, int))        # True (bool is subclass of int)
print(isinstance(True, bool))       # True
print(isinstance(3.14, float))      # True
print(isinstance(3+4j, complex))    # True

# Sequence types
print(isinstance("hello", str))     # True
print(isinstance([1,2], list))      # True
print(isinstance((1,2), tuple))     # True
print(isinstance(range(5), range))  # True

# Mapping and set types
print(isinstance({"a":1}, dict))    # True
print(isinstance({1,2}, set))       # True
print(isinstance(frozenset([1,2]), frozenset))  # True

# Other types
print(isinstance(None, type(None))) # True
print(isinstance(print, callable))  # True
```

### isinstance() with Abstract Base Classes

```python
from collections.abc import Iterable, Sequence, MutableSequence

# Check if object is iterable
print(isinstance([1,2,3], Iterable))    # True
print(isinstance("hello", Iterable))    # True
print(isinstance(42, Iterable))         # False

# Check if object is sequence
print(isinstance([1,2,3], Sequence))    # True
print(isinstance("hello", Sequence))    # True
print(isinstance({1,2,3}, Sequence))    # False (set is not sequence)

# Check if object is mutable sequence
print(isinstance([1,2,3], MutableSequence))  # True
print(isinstance((1,2,3), MutableSequence))  # False (tuple is immutable)

# Real use: Generic container handling
def process_container(container):
    if isinstance(container, MutableSequence):
        container.append("new item")
        print(f"Added item to {type(container).__name__}")
    elif isinstance(container, Sequence):
        print(f"Read-only sequence of length {len(container)}")
    elif isinstance(container, Iterable):
        print(f"Iterable with {len(list(container))} items")
    else:
        print("Not a container")
```

### isinstance() with Custom Classes

```python
class BaseClass:
    def base_method(self):
        return "base"

class Intermediate(BaseClass):
    def intermediate_method(self):
        return "intermediate"

class Child(Intermediate):
    def child_method(self):
        return "child"

obj = Child()

# isinstance works through entire inheritance chain
print(isinstance(obj, Child))         # True
print(isinstance(obj, Intermediate))  # True
print(isinstance(obj, BaseClass))     # True
print(isinstance(obj, object))        # True

# Practical use: Polymorphic handling
def process_object(obj):
    if isinstance(obj, Child):
        print("Processing as Child")
        return obj.child_method()
    elif isinstance(obj, Intermediate):
        print("Processing as Intermediate")
        return obj.intermediate_method()
    elif isinstance(obj, BaseClass):
        print("Processing as BaseClass")
        return obj.base_method()
    else:
        print("Unknown type")
        return None

print(process_object(obj))  # Processing as Child -> child
```

### isinstance() with Type Hints (Runtime)

```python
from typing import List, Dict, Optional

def validate_type(value, expected_type):
    """Runtime type validation with type hints"""
    if hasattr(expected_type, '__origin__'):
        # Handle generic types like List[int]
        origin = expected_type.__origin__
        if not isinstance(value, origin):
            return False
        
        # Check inner types if specified
        if expected_type.__args__:
            inner_type = expected_type.__args__[0]
            return all(isinstance(item, inner_type) for item in value)
    
    return isinstance(value, expected_type)

# Usage
print(validate_type([1, 2, 3], List[int]))    # True
print(validate_type([1, "2", 3], List[int]))  # False
print(validate_type([1, 2, 3], list))         # True
```

---

## The issubclass() Function

### Basic Usage

```python
# Check class inheritance
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Beagle(Dog):
    pass

print(issubclass(Dog, Animal))      # True
print(issubclass(Cat, Animal))      # True
print(issubclass(Beagle, Dog))      # True
print(issubclass(Beagle, Animal))   # True (indirect inheritance)
print(issubclass(Animal, Dog))      # False
print(issubclass(Dog, Dog))         # True (class is subclass of itself)

# Check multiple classes
print(issubclass(Dog, (Animal, object)))  # True
print(issubclass(Dog, (Cat, object)))     # True (object works)
print(issubclass(Dog, (Cat, list)))       # False
```

### issubclass() with Built-in Types

```python
# Numeric type hierarchy
print(issubclass(bool, int))        # True
print(issubclass(bool, float))      # False
print(issubclass(int, object))      # True
print(issubclass(float, object))    # True

# Sequence types
print(issubclass(list, object))     # True
print(issubclass(tuple, object))    # True
print(issubclass(str, object))      # True

# Custom class relationships
class MyInt(int):
    pass

print(issubclass(MyInt, int))       # True
print(issubclass(MyInt, object))    # True
print(issubclass(int, MyInt))       # False
```

### Practical Use: Class Validation

```python
class Validator:
    def validate(self, value):
        raise NotImplementedError

class EmailValidator(Validator):
    def validate(self, value):
        return '@' in value and '.' in value

class PhoneValidator(Validator):
    def validate(self, value):
        return value.isdigit() and len(value) == 10

class AgeValidator(Validator):
    def validate(self, value):
        return isinstance(value, int) and 0 <= value <= 150

class ValidationSystem:
    def __init__(self):
        self.validators = []
    
    def register_validator(self, validator_class):
        """Register a validator class"""
        if not issubclass(validator_class, Validator):
            raise TypeError(f"{validator_class.__name__} must inherit from Validator")
        self.validators.append(validator_class())
    
    def validate_all(self, value):
        """Run all validators"""
        results = {}
        for validator in self.validators:
            results[type(validator).__name__] = validator.validate(value)
        return results

# Usage
system = ValidationSystem()

# Register validators
system.register_validator(EmailValidator)
system.register_validator(PhoneValidator)
system.register_validator(AgeValidator)

# Test values
test_values = ["alice@example.com", "1234567890", 25, "invalid"]

for value in test_values:
    print(f"\nTesting: {value}")
    results = system.validate_all(value)
    for validator_name, result in results.items():
        print(f"  {validator_name}: {result}")
```

---

## Comparison: type() vs isinstance()

### Key Differences

```python
class Parent:
    pass

class Child(Parent):
    pass

obj = Child()

# type() - exact type
print(type(obj) == Child)    # True
print(type(obj) == Parent)   # False

# isinstance() - type or subclass
print(isinstance(obj, Child))   # True
print(isinstance(obj, Parent))  # True (Child is subclass of Parent)

# Practical example
def process_with_type(value):
    if type(value) == int:
        return "Integer (exact)"
    elif type(value) == bool:
        return "Boolean (exact)"
    else:
        return "Other"

def process_with_isinstance(value):
    if isinstance(value, int):
        return "Integer or bool"
    elif isinstance(value, str):
        return "String"
    else:
        return "Other"

print(process_with_type(True))     # Boolean (exact)
print(process_with_isinstance(True))  # Integer or bool (unexpected!)
```

### When to Use type()

```python
# Use type() when exact type matters (rare)

# Example 1: Distinguish between int and bool
def process_number(n):
    if type(n) is bool:
        return f"Boolean: {n}"
    elif type(n) is int:
        return f"Integer: {n}"
    else:
        return f"Other: {type(n)}"

print(process_number(True))   # Boolean: True
print(process_number(42))     # Integer: 42

# Example 2: Prevent subclass behavior
class MyInt(int):
    pass

def add_one(n):
    if type(n) is int:  # Only accepts exact int, not MyInt
        return n + 1
    else:
        raise TypeError("Only int allowed")

print(add_one(42))        # 43
try:
    print(add_one(MyInt(42)))  # TypeError!
except TypeError as e:
    print(f"Error: {e}")

# Example 3: Type checking in serialization
def to_json(obj):
    if type(obj) is dict:
        return "{...}"
    elif type(obj) is list:
        return "[...]"
    elif type(obj) is str:
        return f'"{obj}"'
    else:
        return str(obj)
```

### When to Use isinstance()

```python
# Use isinstance() for most cases (recommended)

# Example 1: Polymorphic handling
def describe(animal):
    if isinstance(animal, Dog):
        return "Woof!"
    elif isinstance(animal, Cat):
        return "Meow!"
    elif isinstance(animal, Animal):
        return "Some animal sound"
    else:
        return "Not an animal"

class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass
class Beagle(Dog): pass

print(describe(Dog()))      # Woof!
print(describe(Beagle()))   # Woof! (works with subclass)
print(describe(Cat()))      # Meow!
print(describe(Animal()))   # Some animal sound

# Example 2: Numeric operations
def square(x):
    if isinstance(x, (int, float)):
        return x * x
    else:
        raise TypeError("Numeric value required")

print(square(5))      # 25
print(square(5.5))    # 30.25
print(square(True))   # 1 (True is int, but may not be desired)

# Example 3: Container handling
def process_container(container):
    if isinstance(container, (list, tuple)):
        return f"Sequence with {len(container)} items"
    elif isinstance(container, dict):
        return f"Dict with {len(container)} keys"
    elif isinstance(container, set):
        return f"Set with {len(container)} elements"
    else:
        return "Unknown container"

print(process_container([1,2,3]))     # Sequence with 3 items
print(process_container((1,2,3)))     # Sequence with 3 items
print(process_container({1,2,3}))     # Set with 3 elements
print(process_container({"a":1}))     # Dict with 1 keys
```

### Performance Comparison

```python
import timeit

# Performance test
obj = 42

type_time = timeit.timeit('type(obj) == int', globals=globals(), number=10000000)
isinstance_time = timeit.timeit('isinstance(obj, int)', globals=globals(), number=10000000)

print(f"type() comparison: {type_time:.4f}s")
print(f"isinstance(): {isinstance_time:.4f}s")
print(f"isinstance() is {type_time/isinstance_time:.1f}x faster")
```

---

## Real-World Examples

### Example 1: Data Validation Framework

```python
from datetime import datetime
from typing import Any, Dict, List, Optional

class TypeValidator:
    @staticmethod
    def validate_int(value: Any, min_val: Optional[int] = None, max_val: Optional[int] = None) -> bool:
        """Validate integer value"""
        if not isinstance(value, int):
            return False
        if min_val is not None and value < min_val:
            return False
        if max_val is not None and value > max_val:
            return False
        return True
    
    @staticmethod
    def validate_float(value: Any, min_val: Optional[float] = None, max_val: Optional[float] = None) -> bool:
        """Validate float value"""
        if not isinstance(value, (int, float)):
            return False
        if min_val is not None and value < min_val:
            return False
        if max_val is not None and value > max_val:
            return False
        return True
    
    @staticmethod
    def validate_str(value: Any, min_len: Optional[int] = None, max_len: Optional[int] = None) -> bool:
        """Validate string value"""
        if not isinstance(value, str):
            return False
        if min_len is not None and len(value) < min_len:
            return False
        if max_len is not None and len(value) > max_len:
            return False
        return True
    
    @staticmethod
    def validate_list(value: Any, item_type: Optional[type] = None) -> bool:
        """Validate list value"""
        if not isinstance(value, list):
            return False
        if item_type is not None:
            return all(isinstance(item, item_type) for item in value)
        return True
    
    @staticmethod
    def validate_dict(value: Any, key_type: Optional[type] = None, value_type: Optional[type] = None) -> bool:
        """Validate dictionary value"""
        if not isinstance(value, dict):
            return False
        if key_type is not None and not all(isinstance(k, key_type) for k in value.keys()):
            return False
        if value_type is not None and not all(isinstance(v, value_type) for v in value.values()):
            return False
        return True
    
    @staticmethod
    def validate_email(value: Any) -> bool:
        """Validate email string"""
        if not isinstance(value, str):
            return False
        return '@' in value and '.' in value and len(value) > 5
    
    @staticmethod
    def validate_phone(value: Any) -> bool:
        """Validate phone number"""
        if not isinstance(value, str):
            return False
        digits = ''.join(filter(str.isdigit, value))
        return len(digits) == 10

class DataValidator:
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema
        self.errors: List[str] = []
    
    def validate(self, data: Dict[str, Any]) -> bool:
        """Validate data against schema"""
        self.errors.clear()
        
        # Check required fields
        for field, expected_type in self.schema.items():
            if field not in data:
                self.errors.append(f"Missing required field: {field}")
                continue
            
            value = data[field]
            if not isinstance(value, expected_type):
                self.errors.append(f"Field '{field}' expected {expected_type.__name__}, got {type(value).__name__}")
        
        return len(self.errors) == 0
    
    def get_errors(self) -> List[str]:
        return self.errors

# Usage
print("DATA VALIDATION FRAMEWORK")
print("=" * 50)

# Define schema
user_schema = {
    "name": str,
    "age": int,
    "email": str,
    "scores": list,
    "metadata": dict
}

# Create validator
validator = DataValidator(user_schema)

# Test data
test_data = {
    "name": "Alice",
    "age": "30",  # Wrong type (should be int)
    "email": "alice@example.com",
    "scores": [85, 90, 88],
    "metadata": {"city": "NYC"}
}

print(f"Test data: {test_data}")
print(f"Valid: {validator.validate(test_data)}")
print(f"Errors: {validator.get_errors()}")

# Correct data
correct_data = {
    "name": "Bob",
    "age": 25,
    "email": "bob@example.com",
    "scores": [92, 88, 95],
    "metadata": {"city": "LA"}
}

print(f"\nCorrect data valid: {validator.validate(correct_data)}")
```

### Example 2: Plugin System with Type Checking

```python
from abc import ABC, abstractmethod
from typing import Dict, List, Type

class Plugin(ABC):
    """Base plugin class"""
    
    @abstractmethod
    def execute(self, data: str) -> str:
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass

class UppercasePlugin(Plugin):
    @property
    def name(self) -> str:
        return "uppercase"
    
    def execute(self, data: str) -> str:
        return data.upper()

class LowercasePlugin(Plugin):
    @property
    def name(self) -> str:
        return "lowercase"
    
    def execute(self, data: str) -> str:
        return data.lower()

class ReversePlugin(Plugin):
    @property
    def name(self) -> str:
        return "reverse"
    
    def execute(self, data: str) -> str:
        return data[::-1]

class CapitalizePlugin(Plugin):
    @property
    def name(self) -> str:
        return "capitalize"
    
    def execute(self, data: str) -> str:
        return data.capitalize()

class PluginManager:
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
    
    def register_plugin(self, plugin_class: Type[Plugin]) -> bool:
        """Register a plugin class"""
        # Validate plugin class
        if not issubclass(plugin_class, Plugin):
            raise TypeError(f"{plugin_class.__name__} must inherit from Plugin")
        
        # Create instance
        plugin = plugin_class()
        
        # Validate instance
        if not isinstance(plugin, Plugin):
            raise TypeError(f"Instance of {plugin_class.__name__} is not a Plugin")
        
        # Check for duplicate names
        if plugin.name in self.plugins:
            print(f"Warning: Overwriting plugin '{plugin.name}'")
        
        self.plugins[plugin.name] = plugin
        return True
    
    def execute_plugin(self, name: str, data: str) -> str:
        """Execute plugin by name"""
        if name not in self.plugins:
            raise ValueError(f"Plugin '{name}' not found")
        
        plugin = self.plugins[name]
        return plugin.execute(data)
    
    def list_plugins(self) -> List[str]:
        """List all registered plugins"""
        return list(self.plugins.keys())
    
    def execute_all(self, data: str) -> Dict[str, str]:
        """Execute all plugins"""
        results = {}
        for name, plugin in self.plugins.items():
            results[name] = plugin.execute(data)
        return results

# Usage
print("PLUGIN SYSTEM WITH TYPE CHECKING")
print("=" * 50)

# Create plugin manager
manager = PluginManager()

# Register plugins
plugins_to_register = [UppercasePlugin, LowercasePlugin, ReversePlugin, CapitalizePlugin]

for plugin_class in plugins_to_register:
    try:
        manager.register_plugin(plugin_class)
        print(f"Registered: {plugin_class.__name__}")
    except TypeError as e:
        print(f"Failed to register {plugin_class.__name__}: {e}")

print(f"\nRegistered plugins: {manager.list_plugins()}")

# Execute plugins
test_data = "hello world"
print(f"\nTest data: '{test_data}'")
print("Results:")

results = manager.execute_all(test_data)
for name, result in results.items():
    print(f"  {name}: '{result}'")
```

### Example 3: JSON Type Validator

```python
import json
from typing import Any, Dict, List, Union

class JSONTypeValidator:
    """Validate JSON data against a schema with type checking"""
    
    def __init__(self):
        self.errors: List[str] = []
    
    def validate(self, data: Any, schema: Dict[str, Any], path: str = "") -> bool:
        """Validate data against schema"""
        self.errors.clear()
        return self._validate(data, schema, path)
    
    def _validate(self, data: Any, schema: Dict[str, Any], path: str) -> bool:
        """Internal validation logic"""
        if 'type' in schema:
            if not self._check_type(data, schema['type'], path):
                return False
        
        if 'properties' in schema and isinstance(data, dict):
            for prop, prop_schema in schema['properties'].items():
                prop_path = f"{path}.{prop}" if path else prop
                if prop in data:
                    self._validate(data[prop], prop_schema, prop_path)
                elif 'required' in schema and prop in schema.get('required', []):
                    self.errors.append(f"Missing required field: {prop_path}")
        
        if 'items' in schema and isinstance(data, list):
            for i, item in enumerate(data):
                item_path = f"{path}[{i}]"
                self._validate(item, schema['items'], item_path)
        
        return len(self.errors) == 0
    
    def _check_type(self, data: Any, expected_type: Union[str, List[str]], path: str) -> bool:
        """Check type of data"""
        types = expected_type if isinstance(expected_type, list) else [expected_type]
        
        for t in types:
            if t == 'string' and isinstance(data, str):
                return True
            elif t == 'number' and isinstance(data, (int, float)):
                return True
            elif t == 'integer' and isinstance(data, int) and not isinstance(data, bool):
                return True
            elif t == 'boolean' and isinstance(data, bool):
                return True
            elif t == 'array' and isinstance(data, list):
                return True
            elif t == 'object' and isinstance(data, dict):
                return True
            elif t == 'null' and data is None:
                return True
        
        self.errors.append(f"Field '{path}' expected {expected_type}, got {type(data).__name__}")
        return False
    
    def get_errors(self) -> List[str]:
        return self.errors

# Usage
print("JSON TYPE VALIDATOR")
print("=" * 50)

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

# Create validator
validator = JSONTypeValidator()

# Test data
test_data = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "is_active": True,
    "tags": ["python", "developer"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

print("Valid data:")
valid = validator.validate(test_data, user_schema)
print(f"  Valid: {valid}")
if not valid:
    for error in validator.get_errors():
        print(f"  Error: {error}")

# Invalid data
invalid_data = {
    "name": "Bob",
    "age": "25",  # Wrong type (should be integer)
    "email": "bob@example.com",
    # Missing is_active (optional, so ok)
    "tags": "python",  # Wrong type (should be array)
    "address": {
        "street": "456 Oak Ave",
        "city": "Los Angeles"
        # Missing zip (optional, so ok)
    }
}

print("\nInvalid data:")
valid = validator.validate(invalid_data, user_schema)
print(f"  Valid: {valid}")
if not valid:
    for error in validator.get_errors():
        print(f"  Error: {error}")
```

### Example 4: Generic Repository Pattern

```python
from typing import Dict, List, Optional, Type, TypeVar, Generic
from abc import ABC, abstractmethod
import json

T = TypeVar('T')

class Entity(ABC):
    """Base entity class"""
    @abstractmethod
    def get_id(self) -> str:
        pass
    
    def to_dict(self) -> Dict:
        """Convert entity to dictionary"""
        return self.__dict__
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict) -> 'Entity':
        """Create entity from dictionary"""
        pass

class User(Entity):
    def __init__(self, user_id: str, name: str, age: int):
        self._id = user_id
        self.name = name
        self.age = age
    
    def get_id(self) -> str:
        return self._id
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        return cls(data['_id'], data['name'], data['age'])
    
    def __repr__(self):
        return f"User(id={self._id}, name={self.name}, age={self.age})"

class Product(Entity):
    def __init__(self, product_id: str, name: str, price: float):
        self._id = product_id
        self.name = name
        self.price = price
    
    def get_id(self) -> str:
        return self._id
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        return cls(data['_id'], data['name'], data['price'])
    
    def __repr__(self):
        return f"Product(id={self._id}, name={self.name}, price={self.price})"

class Repository(Generic[T]):
    """Generic repository with type checking"""
    
    def __init__(self, entity_class: Type[T]):
        if not issubclass(entity_class, Entity):
            raise TypeError(f"{entity_class.__name__} must inherit from Entity")
        
        self.entity_class = entity_class
        self._storage: Dict[str, T] = {}
    
    def save(self, entity: T) -> None:
        """Save entity"""
        if not isinstance(entity, self.entity_class):
            raise TypeError(f"Expected {self.entity_class.__name__}, got {type(entity).__name__}")
        
        self._storage[entity.get_id()] = entity
    
    def find_by_id(self, entity_id: str) -> Optional[T]:
        """Find entity by ID"""
        return self._storage.get(entity_id)
    
    def find_all(self) -> List[T]:
        """Get all entities"""
        return list(self._storage.values())
    
    def delete(self, entity_id: str) -> bool:
        """Delete entity by ID"""
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False
    
    def save_all(self, entities: List[T]) -> None:
        """Save multiple entities"""
        if not all(isinstance(e, self.entity_class) for e in entities):
            raise TypeError(f"All entities must be {self.entity_class.__name__}")
        
        for entity in entities:
            self.save(entity)
    
    def to_json(self) -> str:
        """Export to JSON"""
        data = {entity_id: entity.to_dict() for entity_id, entity in self._storage.items()}
        return json.dumps(data, indent=2)
    
    def from_json(self, json_str: str) -> None:
        """Import from JSON"""
        data = json.loads(json_str)
        for entity_id, entity_data in data.items():
            entity = self.entity_class.from_dict(entity_data)
            self.save(entity)

# Usage
print("GENERIC REPOSITORY WITH TYPE CHECKING")
print("=" * 50)

# Create repositories
user_repo = Repository(User)
product_repo = Repository(Product)

# Create entities
user1 = User("1", "Alice", 30)
user2 = User("2", "Bob", 25)
product1 = Product("P1", "Laptop", 999.99)
product2 = Product("P2", "Mouse", 29.99)

# Save entities
user_repo.save(user1)
user_repo.save(user2)
product_repo.save(product1)
product_repo.save(product2)

print("Users:")
for user in user_repo.find_all():
    print(f"  {user}")

print("\nProducts:")
for product in product_repo.find_all():
    print(f"  {product}")

# Type checking prevents mixing
try:
    user_repo.save(product1)  # This will raise TypeError
except TypeError as e:
    print(f"\nType checking prevented error: {e}")

# Find by ID
found = user_repo.find_by_id("1")
print(f"\nFound user with ID '1': {found}")

# Delete
user_repo.delete("2")
print(f"\nAfter deletion, users: {user_repo.find_all()}")

# Export to JSON
print("\nUser repository JSON:")
print(user_repo.to_json())
```

---

## Common Pitfalls

### Pitfall 1: bool is Subclass of int

```python
# bool is subclass of int
print(issubclass(bool, int))  # True
print(isinstance(True, int))  # True

# This can cause unexpected behavior
def process_number(n):
    if isinstance(n, int):
        return n * 2
    return None

print(process_number(5))    # 10
print(process_number(True)) # 2 (unexpected!)

# Solution: Check exact type when needed
def process_number_exact(n):
    if type(n) is int and not isinstance(n, bool):
        return n * 2
    return None

print(process_number_exact(True))  # None
```

### Pitfall 2: type() vs isinstance() with None

```python
value = None

# Both work, but isinstance is more readable
print(type(value) is type(None))  # True
print(isinstance(value, type(None)))  # True
print(value is None)  # Best way

# Recommended
if value is None:
    print("Value is None")
```

### Pitfall 3: Checking for Multiple Types

```python
# ❌ Wrong - OR doesn't work like this
def process_bad(value):
    if type(value) == int or float:  # Always True! (float is truthy)
        return "Number"
    return "Other"

print(process_bad(42))     # Number
print(process_bad("hello")) # Number (unexpected!)

# ✅ Correct - Check against tuple
def process_good(value):
    if isinstance(value, (int, float)):
        return "Number"
    return "Other"

print(process_good(42))     # Number
print(process_good("hello")) # Other
```

### Pitfall 4: Class vs Instance

```python
class MyClass:
    pass

obj = MyClass()

# Checking class vs instance
print(isinstance(MyClass, type))      # True (class is type)
print(isinstance(obj, MyClass))       # True (instance of class)
print(isinstance(MyClass, MyClass))   # False (class is not instance of itself)

# Use issubclass for class relationships
print(issubclass(MyClass, object))    # True
```

---

## Practice Exercises

### Beginner Level

1. **Type Identifier**
   ```python
   # Write function that returns type name as string
   # Example: get_type_name(42) → "int"
   ```

2. **Type Validator**
   ```python
   # Check if value is one of allowed types
   # Example: is_type(42, (int, float)) → True
   ```

3. **Safe Division**
   ```python
   # Divide only if both are numbers
   # Raise TypeError otherwise
   ```

### Intermediate Level

4. **Polymorphic Printer**
   ```python
   # Print different messages based on type
   # Handle int, float, str, list, dict
   ```

5. **Type Registry**
   ```python
   # Create registry that maps types to handlers
   # Register and execute handlers by type
   ```

6. **Schema Validator**
   ```python
   # Validate dict against schema with types
   # Support nested structures
   ```

### Advanced Level

7. **Generic Container**
   ```python
   # Create type-checked container
   # Only allow specific types to be added
   ```

8. **Polymorphic Serializer**
   ```python
   # Serialize objects based on their type
   # Support custom serialization per class
   ```

9. **Dependency Injector**
   ```python
   # Type-checked dependency injection
   # Validate dependencies by type
   ```

---

## Quick Reference Card

```python
# type() - Exact type
type(obj)                    # Get type
type(obj) == int            # Compare exact type
type(obj) in (int, float)   # Check multiple

# isinstance() - Type or subclass
isinstance(obj, int)        # Check single type
isinstance(obj, (int, float))  # Check multiple
isinstance(obj, type(None)) # Check for None

# issubclass() - Class hierarchy
issubclass(Child, Parent)   # Check inheritance
issubclass(Dog, (Animal, object))  # Multiple
issubclass(cls, ABC)        # Check abstract base class

# Common patterns
if isinstance(value, (int, float)):
    # Numeric processing

if type(value) is int and not isinstance(value, bool):
    # Exact int (excluding bool)

if value is None:
    # Check for None (preferred)

if callable(func):
    # Check if callable

if hasattr(obj, 'method'):
    # Duck typing
```

## Next Step

- Go to [type_hints.md](02_type_hints.md) now.
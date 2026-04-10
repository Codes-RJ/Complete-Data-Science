# 🔍 TYPE CHECKING – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [Why Type Checking Matters](#why-type-checking-matters)
3. [Type Checking Methods](#type-checking-methods)
4. [Quick Comparison](#quick-comparison)
5. [Type Hints](#type-hints)
6. [When to Use Each](#when-to-use-each)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Type checking** is the process of determining and validating the data type of variables, function parameters, and return values in Python.

```python
# Type checking examples
x = 42
print(type(x))        # <class 'int'>
print(isinstance(x, int))  # True
print(isinstance(x, (int, float)))  # True
```

**Key Characteristics:**
- ✅ Python is dynamically typed (types determined at runtime)
- ✅ Type checking helps catch bugs early
- ✅ Can be done at runtime or with static analysis
- ✅ Type hints provide documentation (Python 3.5+)
- ✅ Runtime checking prevents type errors

---

## 🎯 Why Type Checking Matters

### 1. Prevent Runtime Errors

```python
def add_numbers(a, b):
    return a + b

# This works
print(add_numbers(5, 3))     # 8

# This crashes
try:
    print(add_numbers("5", 3))
except TypeError as e:
    print(f"Error: {e}")  # can only concatenate str to str

# With type checking
def add_numbers_safe(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
```

### 2. Self-Documenting Code

```python
# Without type hints (unclear)
def process(data, options):
    pass

# With type hints (clear)
def process(data: List[Dict[str, Any]], options: Optional[Dict] = None) -> bool:
    """Process data with optional configuration"""
    pass
```

### 3. IDE Support and Autocomplete

```python
# Type hints enable better IDE features
def calculate_total(prices: List[float], tax_rate: float = 0.08) -> float:
    return sum(prices) * (1 + tax_rate)

# IDE knows prices is list of floats
# IDE knows return type is float
```

---

## 🔧 Type Checking Methods

### 1. `type()` – Get Exact Type

```python
# Returns the exact type of an object
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("hello"))      # <class 'str'>
print(type([1, 2, 3]))    # <class 'list'>
print(type({"a": 1}))     # <class 'dict'>

# Type comparison
if type(x) == int:
    print("x is an integer")

# Does NOT work with inheritance
class Parent:
    pass

class Child(Parent):
    pass

obj = Child()
print(type(obj) == Child)   # True
print(type(obj) == Parent)  # False (Child is not Parent type)
```

### 2. `isinstance()` – Check Inheritance

```python
# Checks if object is instance of class or tuple of classes
print(isinstance(42, int))           # True
print(isinstance(42, (int, float)))  # True
print(isinstance(42, object))        # True (everything is object)

# Works with inheritance
class Parent:
    pass

class Child(Parent):
    pass

obj = Child()
print(isinstance(obj, Child))   # True
print(isinstance(obj, Parent))  # True (Child inherits from Parent)
print(isinstance(obj, object))  # True

# Recommended over type() for most cases
def process_value(value):
    if isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, str):
        return value + value
    else:
        return None
```

### 3. `issubclass()` – Check Class Hierarchy

```python
# Checks if class is subclass of another class
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(issubclass(Dog, Animal))   # True
print(issubclass(Cat, Animal))   # True
print(issubclass(Dog, object))   # True
print(issubclass(int, object))   # True

# Check multiple classes
print(issubclass(Dog, (Animal, object)))  # True

# Real use: Validate class hierarchies
def validate_class(cls):
    if not issubclass(cls, BaseValidator):
        raise TypeError(f"{cls.__name__} must inherit from BaseValidator")
```

### 4. `callable()` – Check if Callable

```python
# Checks if object can be called as function
def my_function():
    pass

class MyClass:
    def __call__(self):
        pass
    
    def method(self):
        pass

print(callable(my_function))    # True
print(callable(MyClass))        # True (class is callable)
print(callable(MyClass()))      # True (instance with __call__)
print(callable(MyClass.method)) # True
print(callable(42))             # False
print(callable("hello"))        # False

# Real use: Execute callbacks
def execute_callback(callback, *args, **kwargs):
    if not callable(callback):
        raise TypeError("Callback must be callable")
    return callback(*args, **kwargs)
```

### 5. `hasattr()` – Check Attributes

```python
# Checks if object has specific attribute
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}"

p = Person("Alice")

print(hasattr(p, "name"))     # True
print(hasattr(p, "greet"))    # True
print(hasattr(p, "age"))      # False
print(hasattr(p, "__init__")) # True

# Real use: Duck typing
def process_object(obj):
    if hasattr(obj, "process"):
        return obj.process()
    elif hasattr(obj, "save"):
        return obj.save()
    else:
        raise AttributeError("Object has no process or save method")
```

---

## 📊 Quick Comparison

| Function | Checks | Inheritance | Use Case |
|----------|--------|-------------|----------|
| `type()` | Exact type | ❌ No | When exact type matters |
| `isinstance()` | Type or subclass | ✅ Yes | Most common use |
| `issubclass()` | Class hierarchy | ✅ Yes | Class validation |
| `callable()` | Callable objects | N/A | Callback validation |
| `hasattr()` | Attribute existence | N/A | Duck typing |

### When to Use Each

```python
# Use type() for exact type matching (rare)
if type(value) is int:
    # Must be exactly int, not bool or float
    pass

# Use isinstance() for most cases (recommended)
if isinstance(value, (int, float)):
    # Works with int, float, bool, and subclasses
    pass

# Use issubclass() for class validation
if issubclass(cls, BaseClass):
    # Ensure class inherits from BaseClass
    pass

# Use callable() for callbacks
if callable(callback):
    callback()

# Use hasattr() for duck typing
if hasattr(obj, "save"):
    obj.save()
```

---

## 📝 Type Hints (Python 3.5+)

### Basic Type Hints

```python
# Variable annotations
name: str = "Alice"
age: int = 30
prices: list[float] = [19.99, 29.99, 39.99]
config: dict[str, any] = {"debug": True, "port": 8080}

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate_total(prices: list[float], tax: float = 0.08) -> float:
    return sum(prices) * (1 + tax)

def process_data(data: dict[str, int]) -> list[str]:
    return [str(k) for k, v in data.items() if v > 0]
```

### Optional and Union Types

```python
from typing import Optional, Union

# Optional (can be None)
def find_user(user_id: int) -> Optional[dict]:
    # Returns dict or None
    pass

# Union (multiple possible types)
def process(value: Union[int, float, str]) -> str:
    return str(value)

# Python 3.10+ alternative
def process(value: int | float | str) -> str:
    return str(value)
```

### Collection Types

```python
from typing import List, Dict, Tuple, Set

# Lists
def process_items(items: List[str]) -> List[int]:
    return [len(item) for item in items]

# Dictionaries
def update_config(config: Dict[str, any]) -> Dict[str, any]:
    config["updated"] = True
    return config

# Tuples
def get_user() -> Tuple[str, int, str]:
    return ("Alice", 30, "alice@example.com")

# Sets
def unique_chars(text: str) -> Set[str]:
    return set(text)
```

---

## 📁 When to Use Each Method

| Use Case | Best Method | Why |
|----------|-------------|-----|
| General type checking | `isinstance()` | Handles inheritance |
| Exact type matching | `type()` | Strict comparison |
| Class validation | `issubclass()` | Checks hierarchy |
| Callback validation | `callable()` | Functions/classes/methods |
| Duck typing | `hasattr()` | Check capabilities |
| Documentation | Type hints | Self-documenting |
| Runtime validation | `isinstance()` + Type hints | Best of both |

### Real-World Examples

```python
# 1. API Input Validation
def validate_user_data(data: dict) -> bool:
    required_types = {
        "name": str,
        "age": int,
        "email": str,
        "is_active": bool
    }
    
    for field, expected_type in required_types.items():
        if field not in data:
            return False
        if not isinstance(data[field], expected_type):
            return False
    return True

# 2. Polymorphic Processing
def process_animal(animal):
    if isinstance(animal, Dog):
        return animal.bark()
    elif isinstance(animal, Cat):
        return animal.meow()
    else:
        raise TypeError(f"Unknown animal type: {type(animal)}")

# 3. Safe Operation
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `isinstance_type.md` | Detailed guide to type() and isinstance() |
| `type_hints.md` | Complete type hints guide |
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 💡 Quick Tips

```python
# ✅ DO: Use isinstance() for most cases
if isinstance(value, int):
    process_int(value)

# ❌ DON'T: Use type() unless exact match needed
if type(value) == int:  # Fails for bool (bool is subclass of int)
    process_int(value)

# ✅ DO: Use type() for exact type matching
if type(value) is int and not isinstance(value, bool):
    process_int_only(value)

# ✅ DO: Use type hints for documentation
def process(data: list[int]) -> list[str]:
    return [str(x) for x in data]

# ✅ DO: Validate at function boundaries
def set_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, got {type(age)}")
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}")
```

---

## 📚 Next Steps

After understanding type checking basics:
1. Open `isinstance_type.md` for detailed examples
2. Open `type_hints.md` for static typing
3. Complete exercises in `exercises.md`

---

## 🔗 Related Topics

- **Type Conversion** – Converting between types
- **Duck Typing** – "If it walks like a duck"
- **ABC (Abstract Base Classes)** – Advanced type checking
- **Pydantic** – Runtime data validation
- **MyPy** – Static type checker

## Next Step

- Move to [01_isinstance_type.md](01_isinstance_type.md) for understanding the applications of what we learnt so far.

---

*Master type checking for safer, more reliable Python code! 🐍✨*
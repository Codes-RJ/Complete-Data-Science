# 📘 CIRCULAR IMPORTS – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Circular Imports?](#what-are-circular-imports)
2. [Why Circular Imports Fail](#why-circular-imports-fail)
3. [Common Circular Import Scenarios](#common-circular-import-scenarios)
4. [How to Fix Circular Imports](#how-to-fix-circular-imports)
5. [Best Practices to Avoid Circular Imports](#best-practices-to-avoid-circular-imports)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

---

## What are Circular Imports?

A **circular import** occurs when two or more modules import each other, either directly or indirectly.

### Direct Circular Import

```python
# module_a.py
import module_b

def func_a():
    return module_b.func_b()

# module_b.py
import module_a

def func_b():
    return module_a.func_a()

# This creates a circular dependency!
```

### Indirect Circular Import

```python
# module_a.py
import module_b

# module_b.py
import module_c

# module_c.py
import module_a

# Indirect circle: A → B → C → A
```

### Visual Representation

```
Direct:              Indirect:
    A                    A
    ↑                    ↑
    │                    │
    B                    B
                         │
                         ↓
                         C
```

---

## Why Circular Imports Fail

### How Python Imports Work

```python
# Python's import process:
# 1. Check if module already in sys.modules
# 2. If not, create new module object
# 3. Execute module code
# 4. Add module to sys.modules
# 5. Return module to importer

# Problem: During circular import, module is partially initialized
```

### Example of Failure

```python
# module_a.py
print("A: Starting import")
import module_b

def func_a():
    return "A"

print("A: Finished import")
```

```python
# module_b.py
print("B: Starting import")
import module_a

def func_b():
    return module_a.func_a()  # Error! module_a not fully initialized

print("B: Finished import")
```

```python
# main.py
import module_a

# Output:
# A: Starting import
# B: Starting import
# A: Starting import (again? module_a already importing)
# AttributeError: partially initialized module 'module_a'
```

### The Error Message

```python
# Typical circular import error
# AttributeError: partially initialized module 'module_a' 
# (most likely due to a circular import)
```

---

## Common Circular Import Scenarios

### Scenario 1: Two Modules Need Each Other

```python
# models/user.py
from models.order import Order  # User needs Order

class User:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def add_order(self, order):
        if isinstance(order, Order):
            self.orders.append(order)

# models/order.py
from models.user import User  # Order needs User

class Order:
    def __init__(self, user):
        if isinstance(user, User):
            self.user = user
```

### Scenario 2: Type Hints Causing Circular Imports

```python
# user.py
from typing import List
from order import Order  # Circular!

class User:
    def __init__(self, name: str):
        self.name = name
        self.orders: List[Order] = []

# order.py
from user import User  # Circular!

class Order:
    def __init__(self, user: User):
        self.user = user
```

### Scenario 3: Inheritance Across Modules

```python
# animal.py
from dog import Dog  # Circular!

class Animal:
    pass

# dog.py
from animal import Animal  # Circular!

class Dog(Animal):
    pass
```

### Scenario 4: Module-Level Code Execution

```python
# config.py
from constants import DEFAULT_PORT  # Circular!

port = DEFAULT_PORT

# constants.py
from config import port  # Circular!

DEFAULT_PORT = 8080
```

---

## How to Fix Circular Imports

### Solution 1: Import Inside Function (Lazy Import)

Move the import inside the function where it's needed.

```python
# module_a.py
def func_a():
    from module_b import func_b  # Import inside function
    return func_b()

# module_b.py
def func_b():
    from module_a import func_a  # Import inside function
    return func_a()
```

```python
# models/user.py
class User:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def add_order(self, order):
        from models.order import Order  # Lazy import
        if isinstance(order, Order):
            self.orders.append(order)

# models/order.py
class Order:
    def __init__(self, user):
        from models.user import User  # Lazy import
        if isinstance(user, User):
            self.user = user
```

### Solution 2: Import at End of Module

Place imports after the definitions that are needed.

```python
# module_a.py
def func_a():
    return "A"

# Import at the end
from module_b import func_b

# module_b.py
def func_b():
    return "B"

# Import at the end
from module_a import func_a
```

```python
# models/user.py
class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

# Import at the end
from models.order import Order

# models/order.py
class Order:
    def __init__(self, user):
        self.user = user

# Import at the end
from models.user import User
```

### Solution 3: Use `import module` Instead of `from module import`

Module-level imports are less likely to cause circular issues.

```python
# module_a.py
import module_b

def func_a():
    return module_b.func_b()

# module_b.py
import module_a

def func_b():
    return module_a.func_a()  # Works! module_a is in namespace
```

### Solution 4: Restructure Code into Third Module

Move shared dependencies to a separate module.

```python
# common.py (new module)
# Contains shared types and base classes
class Base:
    pass

# user.py
from common import Base

class User(Base):
    def __init__(self, name):
        self.name = name

# order.py
from common import Base

class Order(Base):
    def __init__(self, user):
        self.user = user
```

### Solution 5: Use Type Hints with Strings (Forward References)

For type hints, use string literals to avoid imports.

```python
# user.py
from typing import List

class User:
    def __init__(self, name: str):
        self.name = name
        self.orders: List['Order'] = []  # String reference

# order.py
class Order:
    def __init__(self, user: 'User'):  # String reference
        self.user = user
```

### Solution 6: Use `TYPE_CHECKING` for Conditional Imports

```python
# user.py
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from order import Order  # Only for type checking

class User:
    def __init__(self, name: str):
        self.name = name
        self.orders: List['Order'] = []
```

### Solution 7: Merge Modules

If two modules are tightly coupled, consider merging them.

```python
# models.py (merged)
class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

class Order:
    def __init__(self, user):
        self.user = user
```

---

## Best Practices to Avoid Circular Imports

### 1. Plan Your Module Structure

```python
# Good structure - dependencies flow one way
# app/
# ├── models.py      (data models)
# ├── services.py    (business logic, imports models)
# ├── views.py       (presentation, imports services)
# └── utils.py       (helpers, imported by everyone)
```

### 2. Keep Modules Focused

```python
# ❌ Bad - module does too many things
# everything.py

# ✅ Good - single responsibility
# user_models.py
# order_models.py
# payment_models.py
```

### 3. Use Dependency Injection

```python
# Instead of importing, pass dependencies as parameters
class Order:
    def __init__(self, user):  # user passed in, not imported
        self.user = user
```

### 4. Create a Separate Types Module

```python
# types.py - contains only type definitions
from typing import Protocol

class UserProtocol(Protocol):
    name: str

class OrderProtocol(Protocol):
    user: UserProtocol
```

### 5. Follow Import Conventions

```python
# Import order (helps avoid circular issues)
# 1. Standard library
import sys
import os

# 2. Third-party
import requests

# 3. Local modules (from least to most dependent)
from .base import BaseClass
from .utils import helper
from .models import User  # Depends on base and utils
```

---

## Real-World Examples

### Example 1: Flask Application Blueprints

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import blueprints inside function to avoid circular imports
    from app.routes.auth import auth_bp
    from app.routes.users import users_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    
    return app
```

```python
# app/routes/auth.py
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    # Import models inside function
    from app.models import User
    return "Login page"
```

### Example 2: Django Models with Foreign Keys

```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    # Use string reference instead of direct import
    user = models.ForeignKey('User', on_delete=models.CASCADE)
```

### Example 3: API Client with Circular Models

```python
# api/models.py
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from api.client import APIClient  # Only for type checking

class User:
    def __init__(self, data: dict, client: Optional['APIClient'] = None):
        self.id = data['id']
        self.name = data['name']
        self._client = client
    
    def get_orders(self) -> List['Order']:
        if self._client:
            return self._client.get_orders(self.id)
        return []
```

```python
# api/client.py
from typing import List
from api.models import User, Order  # OK, no circular

class APIClient:
    def get_user(self, user_id: int) -> User:
        data = self._request(f"/users/{user_id}")
        return User(data, client=self)  # Pass self
    
    def get_orders(self, user_id: int) -> List[Order]:
        data = self._request(f"/users/{user_id}/orders")
        return [Order(item) for item in data]
```

### Example 4: Plugin System with Circular Avoidance

```python
# core/plugin_manager.py
class PluginManager:
    def __init__(self):
        self.plugins = {}
    
    def register_plugin(self, name, plugin_class):
        # Store class, don't import yet
        self.plugins[name] = plugin_class
    
    def load_plugin(self, name):
        # Import inside method when needed
        if name in self.plugins:
            plugin_class = self.plugins[name]
            return plugin_class()
        return None
```

```python
# plugins/my_plugin.py
def register(manager):
    # Register without importing core classes
    manager.register_plugin('my_plugin', MyPlugin)

class MyPlugin:
    def run(self):
        return "Running"
```

```python
# main.py
from core.plugin_manager import PluginManager
from plugins import my_plugin

manager = PluginManager()
my_plugin.register(manager)  # No circular import
```

### Example 5: Circular Import Detection Tool

```python
# detect_circular.py
import sys
import traceback

class CircularImportDetector:
    def __init__(self):
        self.import_stack = []
        self.original_import = __import__
        
        # Replace built-in import
        import builtins
        builtins.__import__ = self._import_hook
    
    def _import_hook(self, name, globals=None, locals=None, fromlist=(), level=0):
        # Check for circular import
        if name in self.import_stack:
            print(f"⚠️ Circular import detected: {name}")
            print(f"  Import chain: {' → '.join(self.import_stack)} → {name}")
            traceback.print_stack()
        
        self.import_stack.append(name)
        try:
            return self.original_import(name, globals, locals, fromlist, level)
        finally:
            self.import_stack.pop()
    
    def restore(self):
        import builtins
        builtins.__import__ = self.original_import

# Usage
detector = CircularImportDetector()

# Now run your code
import mymodule  # Will detect circular imports

detector.restore()
```

---

## Common Pitfalls

### Pitfall 1: Importing Inside Function Repeatedly

```python
# ❌ Bad - imports every time function is called
def my_function():
    from module import helper
    return helper()

# ✅ Good - import once at module level (if no circular issue)
from module import helper

def my_function():
    return helper()

# ✅ Or cache the import
_helper = None

def my_function():
    global _helper
    if _helper is None:
        from module import helper as _helper
    return _helper()
```

### Pitfall 2: Using `from module import *` in Circular Scenarios

```python
# ❌ Worse with circular imports
from module_a import *  # Imports everything, harder to trace

# ✅ Better
import module_a  # Clearer dependency
```

### Pitfall 3: Ignoring Import Order

```python
# ❌ Can cause issues
from .submodule import Something  # Early import

class MyClass:
    pass

# ✅ Import after definitions
class MyClass:
    pass

from .submodule import Something
```

---

## Practice Exercises

### Beginner Level

1. **Identify Circular Import**
   ```python
   # Given two modules, identify if they have circular import
   # Fix the circular import
   ```

2. **Lazy Import**
   ```python
   # Convert direct import to lazy import inside function
   # Test that it works
   ```

3. **Import at End**
   ```python
   # Restructure module to import at the end
   # Move imports after function definitions
   ```

### Intermediate Level

4. **Type Hint Fix**
   ```python
   # Fix circular imports caused by type hints
   # Use string literals or TYPE_CHECKING
   ```

5. **Third Module Refactor**
   ```python
   # Extract common dependencies to third module
   # Remove circular dependency
   ```

6. **Dependency Injection**
   ```python
   # Refactor code to use dependency injection
   # Pass dependencies instead of importing
   ```

### Advanced Level

7. **Circular Import Detector**
   ```python
   # Write tool that detects circular imports
   # Analyze module dependencies
   ```

8. **Lazy Loader**
   ```python
   # Implement lazy module loader
   # Load modules only when accessed
   ```

9. **Module Dependency Graph**
   ```python
   # Build dependency graph of modules
   # Detect and report circular dependencies
   ```

---

## Quick Reference Card

```python
# Circular import symptoms
# AttributeError: partially initialized module
# ImportError: cannot import name 'X' from partially initialized module

# Fixes:
# 1. Import inside function
def func():
    from module import something
    return something

# 2. Import at end of module
class MyClass:
    pass

from module import something

# 3. Use module import instead of from import
import module
module.func()

# 4. String literals for type hints
def func(arg: 'MyClass'):
    pass

# 5. TYPE_CHECKING for type hints only
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from module import MyClass

# 6. Third module for shared code
# common.py - shared types

# 7. Merge tightly coupled modules
# one_module.py

# Prevention:
# - Plan module structure
# - Single responsibility
# - Dependency injection
# - Import conventions
```

---

## Next Step

- Move to [standard_library](standard_library/README.md) to explore Python's standard library modules.

---

*Master circular imports to avoid common Python pitfalls! 🐍✨*
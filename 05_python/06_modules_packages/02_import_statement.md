# 📘 IMPORT STATEMENT – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Import Statement?](#what-is-the-import-statement)
2. [Basic Import Syntax](#basic-import-syntax)
3. [Importing Entire Modules](#importing-entire-modules)
4. [Importing Specific Items](#importing-specific-items)
5. [Aliasing (as keyword)](#aliasing-as-keyword)
6. [Wildcard Imports](#wildcard-imports)
7. [Relative Imports](#relative-imports)
8. [Dynamic Imports](#dynamic-imports)
9. [Real-World Examples](#real-world-examples)
10. [Common Pitfalls](#common-pitfalls)
11. [Practice Exercises](#practice-exercises)

---

## What is the Import Statement?

The `import` statement brings modules, functions, classes, or variables from other files into your current namespace.

```python
# Basic import
import math
print(math.sqrt(16))  # 4.0

# Import specific item
from math import sqrt
print(sqrt(16))       # 4.0

# Import with alias
import numpy as np
```

**Why Different Import Styles:**
- ✅ Control namespace pollution
- ✅ Improve code readability
- ✅ Avoid naming conflicts
- ✅ Optimize memory usage
- ✅ Make code more maintainable

---

## Basic Import Syntax

### Syntax Variations

| Syntax | Example | When to Use |
|--------|---------|-------------|
| `import module` | `import math` | Use many functions from module |
| `import module as alias` | `import numpy as np` | Module has long name |
| `from module import name` | `from math import sqrt` | Use few specific functions |
| `from module import name as alias` | `from math import sqrt as sq` | Avoid naming conflicts |
| `from module import *` | `from math import *` | **AVOID** (pollutes namespace) |
| `from package import module` | `from os import path` | Import from package |
| `from package.subpackage import module` | `from datetime import datetime` | Deep package import |

---

## Importing Entire Modules

### Basic Module Import

```python
# Import the entire module
import math

# Access functions and constants using dot notation
print(math.sqrt(25))      # 5.0
print(math.pi)            # 3.141592653589793
print(math.factorial(5))  # 120

# Module maintains its own namespace
# No conflict with your own variables
pi = 3.14
print(pi)                 # 3.14 (your variable)
print(math.pi)            # 3.14159 (math module's pi)
```

### Multiple Module Imports

```python
# Import multiple modules on one line
import math, random, datetime

# Better - one per line (PEP 8 recommendation)
import math
import random
import datetime

# Group imports
import sys
import os
import json

# Use the modules
print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.datetime.now())
```

### Import Order Convention

```python
# Standard import order:
# 1. Standard library imports
import sys
import os
import json
import math
from datetime import datetime

# 2. Third-party imports
import numpy as np
import pandas as pd
import requests

# 3. Local application imports
import mymodule
from mypackage import myfunction
```

---

## Importing Specific Items

### Importing Single Items

```python
# Import only what you need
from math import sqrt
from math import pi
from random import randint

# Use directly without module prefix
print(sqrt(25))     # 5.0
print(pi)           # 3.14159
print(randint(1, 10))

# Namespace is cleaner (no unnecessary names)
# dir() shows fewer items
```

### Importing Multiple Items

```python
# Import multiple items from same module
from math import sqrt, pi, factorial, sin, cos

print(sqrt(25))      # 5.0
print(pi)            # 3.14159
print(factorial(5))  # 120
print(sin(pi/2))     # 1.0

# Line continuation for many imports
from math import (
    sqrt,
    pi,
    factorial,
    sin,
    cos,
    tan,
    log,
    exp
)
```

### Selective Imports

```python
# Only import what you actually use
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from os import path, getcwd, listdir

# Use them
d = defaultdict(int)
c = Counter([1, 2, 2, 3])
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(getcwd())
```

---

## Aliasing (as keyword)

### Module Aliasing

```python
# Give a module a shorter or different name
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Use the alias
arr = np.array([1, 2, 3])
df = pd.DataFrame({'A': [1, 2, 3]})
plt.plot([1, 2, 3])

# Common aliases in the Python ecosystem
import tensorflow as tf
import torch as th
import seaborn as sns
import requests as req
```

### Function Aliasing

```python
# Give a function a different name
from math import sqrt as square_root
from random import randint as random_int
from time import sleep as wait

print(square_root(25))     # 5.0
print(random_int(1, 10))   # Random number
wait(1)                    # Sleep for 1 second

# Avoid naming conflicts
from math import sqrt
from cmath import sqrt as csqrt

print(sqrt(25))    # 5.0 (real)
print(csqrt(-1))   # 1j (complex)
```

### Variable and Class Aliasing

```python
# Alias constants
from math import pi as PI
from datetime import datetime as dt

print(PI)          # 3.14159
print(dt.now())    # Current datetime

# Alias classes
from collections import defaultdict as dd
from json import JSONDecoder as decoder

d = dd(int)
dec = decoder()
```

---

## Wildcard Imports

### What Wildcard Imports Do

```python
# Imports everything from the module
from math import *

# Now you can use all functions without prefix
print(sqrt(25))      # 5.0
print(sin(pi/2))     # 1.0
print(factorial(5))  # 120
print(floor(3.14))   # 3

# Problem: pollutes namespace
# dir() shows many names
print(dir())
# ['__builtins__', '__doc__', '__name__', ..., 'acos', 'acosh', 'asin', ...]
```

### Why to Avoid Wildcard Imports

```python
# Problem 1: Namespace pollution
from math import *
from random import *

# Which module does 'sqrt' come from?
# Both math and random have a 'sqrt'? (random doesn't, but imagine)
sqrt(25)  # Unclear where it came from

# Problem 2: Accidental overwriting
from math import *
pi = 3.14  # Now pi is overwritten!

# Problem 3: Readability
# Someone reading your code doesn't know where functions come from

# Problem 4: Memory usage
# Imports everything even if you don't use it
```

### When Wildcard Might Be Acceptable

```python
# Rare acceptable cases:

# 1. Interactive interpreter (quick testing)
>>> from math import *
>>> sqrt(25)
5.0

# 2. Some specific modules designed for it
from tkinter import *  # Tkinter (GUI) often uses this

# 3. When explicitly defined with __all__
# module.py
__all__ = ['public_func1', 'public_func2']

from module import *  # Only imports public_func1 and public_func2
```

---

## Relative Imports

### Package Structure

```
mypackage/
├── __init__.py
├── module_a.py
├── module_b.py
└── subpackage/
    ├── __init__.py
    └── module_c.py
```

### Relative Import Syntax

| Syntax | Meaning |
|--------|---------|
| `from . import module` | Import from current directory |
| `from .module import func` | Import from module in current directory |
| `from .. import module` | Import from parent directory |
| `from ... import module` | Import from grandparent directory |
| `from .subpackage import module` | Import from subpackage |

### Examples

```python
# module_b.py (same level as module_a)
# Import from module_a in same directory
from . import module_a
from .module_a import some_function

# Import from parent directory
from .. import module_c

# Import from sibling subpackage
from .subpackage import module_c

# Import from subpackage with alias
from .subpackage import module_c as mc
```

### Important Notes on Relative Imports

```python
# Relative imports only work within packages
# They don't work in scripts run directly

# ❌ This will fail if run directly:
# python mypackage/module_a.py
from . import module_b  # ImportError

# ✅ Works when imported as package:
# python -m mypackage.module_a

# Absolute imports are often clearer
from mypackage import module_b
```

---

## Dynamic Imports

### Using `importlib`

```python
# Dynamic import - import module by string name
import importlib

# Import module whose name is stored in a variable
module_name = "math"
math = importlib.import_module(module_name)
print(math.sqrt(25))  # 5.0

# Import from package dynamically
module = importlib.import_module("os.path")
print(module.exists("test.txt"))

# Conditional imports
if user_input == "json":
    import json as data_module
elif user_input == "pickle":
    import pickle as data_module
```

### Using `__import__()` (Built-in)

```python
# Built-in __import__ function (less common)
math = __import__("math")
print(math.sqrt(25))  # 5.0

# With fromlist parameter
os = __import__("os", fromlist=["path"])
print(os.getcwd())

# Not recommended - use importlib instead
```

### Plugin System Example

```python
# plugin_system.py
import importlib
import os

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}
    
    def load_plugins(self):
        """Load all plugins from directory"""
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{self.plugin_dir}.{module_name}")
                self.plugins[module_name] = module
                print(f"Loaded plugin: {module_name}")
    
    def run_plugin(self, name, *args, **kwargs):
        """Run a plugin function"""
        if name in self.plugins:
            if hasattr(self.plugins[name], "run"):
                return self.plugins[name].run(*args, **kwargs)
        return None

# Usage
manager = PluginManager("plugins")
manager.load_plugins()
manager.run_plugin("my_plugin", data)
```

---

## Real-World Examples

### Example 1: Module Import Patterns

```python
# config.py - Configuration module
"""
Application configuration settings.
"""

import os
import json
from pathlib import Path

# Import with alias
from datetime import datetime as dt

# Selective import
from dotenv import load_dotenv

# Constants
DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

def load_config():
    """Load configuration from environment and files."""
    load_dotenv()  # Load .env file
    
    config = DEFAULT_CONFIG.copy()
    config["host"] = os.getenv("APP_HOST", config["host"])
    config["port"] = int(os.getenv("APP_PORT", config["port"]))
    config["debug"] = os.getenv("APP_DEBUG", "false").lower() == "true"
    
    return config

if __name__ == "__main__":
    config = load_config()
    print(f"Config loaded at {dt.now()}")
    print(json.dumps(config, indent=2))
```

```python
# main.py
# Different import styles in practice

# Standard library imports
import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Third-party imports
import requests
from dotenv import load_dotenv

# Local imports
import config
from config import load_config
from utils.helpers import format_date, validate_email

# Import with alias
from utils.database import connect as db_connect

# Conditional import
if sys.platform == "win32":
    import msvcrt
else:
    import termios

def main():
    # Use imported items
    load_dotenv()
    config = load_config()
    
    print(f"Starting app at {datetime.now()}")
    print(f"Config: {json.dumps(config, indent=2)}")
    
    response = requests.get("https://api.github.com")
    print(f"GitHub API status: {response.status_code}")
    
    db_connect(config["database"])

if __name__ == "__main__":
    main()
```

### Example 2: Package Structure with Imports

```
myapp/
├── __init__.py
├── main.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── constants.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── formatters.py
└── models/
    ├── __init__.py
    ├── user.py
    └── product.py
```

```python
# config/__init__.py
from .settings import load_settings
from .constants import API_KEY, API_SECRET

__all__ = ['load_settings', 'API_KEY', 'API_SECRET']
```

```python
# utils/validators.py
def validate_email(email):
    return '@' in email and '.' in email

def validate_phone(phone):
    digits = ''.join(filter(str.isdigit, phone))
    return len(digits) == 10
```

```python
# utils/formatters.py
def format_date(date):
    return date.strftime("%Y-%m-%d")

def format_currency(amount):
    return f"${amount:,.2f}"
```

```python
# models/user.py
from ..utils.validators import validate_email

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        if not validate_email(email):
            raise ValueError("Invalid email")
```

```python
# main.py
# Absolute imports (recommended for clarity)
from myapp.config import load_settings, API_KEY
from myapp.utils.validators import validate_email, validate_phone
from myapp.utils.formatters import format_date, format_currency
from myapp.models.user import User

# Or import the whole package
import myapp.config as config
import myapp.utils.validators as validators

def main():
    settings = load_settings()
    user = User("Alice", "alice@example.com")
    print(f"User created: {user.name}")

if __name__ == "__main__":
    main()
```

### Example 3: Conditional Imports for Compatibility

```python
# compatibility.py
"""
Handle Python version differences with conditional imports.
"""

import sys

# Python version specific imports
if sys.version_info >= (3, 10):
    # Python 3.10+ features
    from typing import TypeAlias
else:
    # Fallback for older versions
    from typing import Any as TypeAlias

# Platform specific imports
if sys.platform == "win32":
    import msvcrt
    import ctypes
    
    def get_input():
        """Windows-specific input handling."""
        return msvcrt.getch()
    
elif sys.platform == "linux":
    import termios
    import tty
    
    def get_input():
        """Linux-specific input handling."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
else:
    def get_input():
        """Default input handling."""
        return input()

# Optional dependencies
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    np = None

def process_data(data):
    """Process data with or without numpy."""
    if HAS_NUMPY:
        return np.array(data) * 2
    else:
        return [x * 2 for x in data]

# Usage
if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"NumPy available: {HAS_NUMPY}")
    print(f"Processed: {process_data([1, 2, 3])}")
```

---

## Common Pitfalls

### Pitfall 1: Circular Imports

```python
# module_a.py
from module_b import func_b

def func_a():
    return func_b()

# module_b.py
from module_a import func_a

def func_b():
    return func_a()

# This creates a circular import!
# Solution: Import inside function or restructure
```

### Pitfall 2: Importing Inside Function Repeatedly

```python
# ❌ Bad - imports every time function is called
def process_data(data):
    import json
    return json.dumps(data)

# ✅ Good - import once at top
import json

def process_data(data):
    return json.dumps(data)
```

### Pitfall 3: Shadowing Built-in Names

```python
# ❌ Bad - shadows built-in open()
from os import open

# ❌ Bad - shadows built-in list
list = [1, 2, 3]

# ✅ Good - use different name or alias
from os import open as os_open
my_list = [1, 2, 3]
```

### Pitfall 4: Using `from module import *` in Production

```python
# ❌ Bad - namespace pollution
from math import *

# ✅ Good - explicit imports
import math
# or
from math import sqrt, pi
```

---

## Practice Exercises

### Beginner Level

1. **Basic Imports**
   ```python
   # Import math module and use:
   # - sqrt()
   # - factorial()
   # - pi constant
   ```

2. **Alias Practice**
   ```python
   # Import datetime module as dt
   # Print current date and time
   ```

3. **Selective Import**
   ```python
   # Import only randint and choice from random
   # Generate random number and random choice from list
   ```

### Intermediate Level

4. **Package Import**
   ```python
   # Create a package with two modules
   # Import using relative and absolute imports
   ```

5. **Conditional Import**
   ```python
   # Import different modules based on platform
   # Windows: use msvcrt, Linux: use termios
   ```

6. **Alias Practice**
   ```python
   # Import numpy as np
   # Import pandas as pd
   # Import matplotlib.pyplot as plt
   ```

### Advanced Level

7. **Dynamic Import**
   ```python
   # Write function that dynamically imports module
   # Module name passed as string
   ```

8. **Plugin System**
   ```python
   # Create plugin system using dynamic imports
   # Load all modules from plugins directory
   ```

9. **Lazy Imports**
   ```python
   # Implement lazy import that imports only when used
   # Use class with __getattr__
   ```

---

## Quick Reference Card

```python
# Basic imports
import module
import module as alias
from module import name
from module import name as alias
from module import name1, name2, name3

# Wildcard (avoid)
from module import *

# Package imports
from package import module
from package.subpackage import module
from . import module          # relative
from .. import module         # parent directory

# Dynamic imports
import importlib
module = importlib.import_module("name")

# Conditional imports
if condition:
    import module1
else:
    import module2

# Try-except import (optional dependency)
try:
    import module
    HAS_MODULE = True
except ImportError:
    HAS_MODULE = False

# Import order convention
# 1. Standard library
import sys
import os

# 2. Third-party
import numpy as np

# 3. Local
import mymodule
```

---

## Next Step

- Move to [03_packages.md](03_packages.md) to learn about creating and using packages.

---

*Master import statements to organize your code effectively! 🐍✨*
# 📘 PACKAGES – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is a Package?](#what-is-a-package)
2. [Creating a Package](#creating-a-package)
3. [`__init__.py` File](#__init__py-file)
4. [Importing from Packages](#importing-from-packages)
5. [Subpackages](#subpackages)
6. [`__all__` Variable](#__all__-variable)
7. [Package Structure Best Practices](#package-structure-best-practices)
8. [Real-World Examples](#real-world-examples)
9. [Common Pitfalls](#common-pitfalls)
10. [Practice Exercises](#practice-exercises)

---

## What is a Package?

A **package** is a way of organizing related modules into a directory hierarchy. A package contains a special `__init__.py` file (which can be empty) and one or more modules.

```
mypackage/                 # Package directory
├── __init__.py           # Required (can be empty)
├── module1.py
├── module2.py
└── subpackage/           # Subpackage
    ├── __init__.py
    └── module3.py
```

```python
# Import from package
import mypackage.module1
from mypackage import module2
from mypackage.subpackage import module3
```

**Why Use Packages:**
- ✅ Organize large codebases
- ✅ Avoid naming conflicts
- ✅ Provide hierarchical structure
- ✅ Control what gets exported
- ✅ Enable namespace management

---

## Creating a Package

### Basic Package Structure

```
mycalculator/              # Package name
├── __init__.py           # Makes Python treat directory as package
├── basic.py              # Basic operations module
├── advanced.py           # Advanced operations module
└── constants.py          # Constants module
```

### Step 1: Create Directory

```bash
mkdir mycalculator
cd mycalculator
```

### Step 2: Create `__init__.py`

```python
# mycalculator/__init__.py
"""
MyCalculator - A simple calculator package.
"""

# This file can be empty, or can contain initialization code
# It marks the directory as a Python package

__version__ = "1.0.0"
__author__ = "Python Developer"

# Import key functions to package level
from .basic import add, subtract, multiply, divide
from .advanced import power, sqrt, factorial
from .constants import PI, E

# Define what gets imported with "from mycalculator import *"
__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt', 'factorial', 'PI', 'E']
```

### Step 3: Create Modules

```python
# mycalculator/basic.py
"""
Basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# mycalculator/advanced.py
"""
Advanced mathematical operations.
"""

import math

def power(a, b):
    """Raise a to power b."""
    return a ** b

def sqrt(a):
    """Calculate square root."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def factorial(n):
    """Calculate factorial."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)
```

```python
# mycalculator/constants.py
"""
Mathematical constants.
"""

PI = 3.141592653589793
E = 2.718281828459045
TAU = 6.283185307179586
```

### Step 4: Use the Package

```python
# main.py
import mycalculator as calc

# Use package functions
print(calc.add(5, 3))           # 8
print(calc.multiply(4, 5))      # 20
print(calc.power(2, 10))        # 1024
print(calc.sqrt(16))            # 4.0
print(calc.PI)                  # 3.141592653589793

# Alternative import styles
from mycalculator import add, subtract, PI
print(add(10, 5))      # 15
print(PI)              # 3.14159

from mycalculator.basic import multiply
print(multiply(6, 7))  # 42
```

---

## `__init__.py` File

The `__init__.py` file is required for Python to treat a directory as a package.

### Empty `__init__.py`

```python
# __init__.py (empty)
# This is enough to make the directory a package
```

### Package Initialization

```python
# __init__.py with initialization code
"""
MyPackage - Awesome package description.
"""

__version__ = "1.0.0"
__author__ = "Python Developer"
__all__ = ['func1', 'func2', 'MyClass']

# Package-level imports
from .module1 import func1
from .module2 import func2, MyClass

# Package initialization code
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Configuration
DEFAULT_CONFIG = {
    "debug": False,
    "timeout": 30
}

def setup(config=None):
    """Initialize package with configuration."""
    if config:
        DEFAULT_CONFIG.update(config)
    print(f"Package initialized with config: {DEFAULT_CONFIG}")
```

### Controlling Exports with `__all__`

```python
# __init__.py
# __all__ controls what gets imported with "from package import *"

__all__ = ['public_function', 'PublicClass', 'PUBLIC_CONSTANT']

from .internal import public_function, PrivateHelper
from .models import PublicClass, _InternalClass
from .config import PUBLIC_CONSTANT, _PRIVATE_CONFIG

# Without __all__, only names without underscore would be imported
# With __all__, only specified names are imported
```

---

## Importing from Packages

### Different Import Styles

```python
# Style 1: Import entire package (need __init__.py)
import mycalculator
print(mycalculator.add(5, 3))

# Style 2: Import specific module
import mycalculator.basic
print(mycalculator.basic.add(5, 3))

# Style 3: Import from module
from mycalculator.basic import add
print(add(5, 3))

# Style 4: Import module with alias
import mycalculator.basic as basic
print(basic.add(5, 3))

# Style 5: Import package with alias
import mycalculator as calc
print(calc.add(5, 3))

# Style 6: Import all (controlled by __all__)
from mycalculator import *
print(add(5, 3))
print(PI)
```

### Absolute vs Relative Imports

```python
# Within a package, you have two options:

# Absolute import (recommended)
from mycalculator.basic import add
from mycalculator.constants import PI

# Relative import (within same package)
from .basic import add
from .constants import PI
from ..otherpackage import helper
```

### Importing Subpackages

```
myapp/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── database.py
│   └── auth.py
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
# Import from subpackages
import myapp.core.database
from myapp.core.auth import login, logout
from myapp.utils.validators import validate_email
import myapp.models.user as user_model

# With __init__.py exposing functions
# myapp/core/__init__.py
from .database import connect, disconnect
from .auth import login, logout

# Then you can do:
from myapp.core import connect, login
```

---

## Subpackages

### Creating Subpackages

```
mywebapp/
├── __init__.py
├── api/
│   ├── __init__.py
│   ├── v1/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── products.py
│   └── v2/
│       ├── __init__.py
│       ├── users.py
│       └── products.py
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── queries.py
└── utils/
    ├── __init__.py
    ├── helpers.py
    └── validators.py
```

### Subpackage `__init__.py` Examples

```python
# mywebapp/api/__init__.py
"""
API subpackage.
"""

from . import v1, v2

def get_api_version(version="v1"):
    """Get API module by version."""
    if version == "v1":
        return v1
    elif version == "v2":
        return v2
    else:
        raise ValueError(f"Unknown API version: {version}")
```

```python
# mywebapp/api/v1/__init__.py
"""
API version 1.
"""

from .users import UserAPI
from .products import ProductAPI

__all__ = ['UserAPI', 'ProductAPI']
```

### Importing from Subpackages

```python
# Import from subpackages
from mywebapp.api.v1 import UserAPI
from mywebapp.database.models import User, Product
from mywebapp.utils.helpers import format_date

# Import with alias
from mywebapp.api.v2 import users as users_v2

# Import entire subpackage
import mywebapp.database.queries as queries
```

---

## `__all__` Variable

The `__all__` variable controls what gets imported when using `from package import *`.

### Basic `__all__` Usage

```python
# mypackage/__init__.py
__all__ = ['public_func', 'PublicClass', 'CONSTANT']

from .module1 import public_func, _private_func
from .module2 import PublicClass, _InternalClass
from .config import CONSTANT, _PRIVATE

# Now, `from mypackage import *` only imports:
# - public_func
# - PublicClass
# - CONSTANT
```

### `__all__` in Modules

```python
# mymodule.py
__all__ = ['add', 'subtract', 'PI']

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):  # Not in __all__
    return a * b

PI = 3.14159
_SECRET = 42  # Underscore convention (not exported)
```

```python
# main.py
from mymodule import *  # Only imports add, subtract, PI

print(add(5, 3))      # Works
print(subtract(10, 4)) # Works
print(PI)              # Works
# print(multiply(2, 3))  # NameError! (not imported)
```

### Package-Level `__all__`

```python
# mypackage/__init__.py
__all__ = ['basic', 'advanced', 'utils']

from . import basic
from . import advanced
from . import utils
```

```python
# This imports the subpackages
from mypackage import *
# Now basic, advanced, utils are available
```

---

## Package Structure Best Practices

### Recommended Structure

```
myproject/
├── README.md
├── setup.py                 # Package installation script
├── requirements.txt         # Dependencies
├── LICENSE
├── .gitignore
│
├── src/                     # Source directory
│   └── mypackage/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   └── logic.py
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── helpers.py
│       │   └── validators.py
│       └── config/
│           ├── __init__.py
│           └── settings.py
│
├── tests/                   # Test directory
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
│
└── examples/                # Example usage
    └── demo.py
```

### `__init__.py` Best Practices

```python
# __init__.py - Good practices

# 1. Add version and author info
__version__ = "1.0.0"
__author__ = "Your Name"

# 2. Import commonly used items for easier access
from .core import main_function
from .utils import helper_function

# 3. Define __all__ to control wildcard imports
__all__ = ['main_function', 'helper_function']

# 4. Package initialization (optional)
def setup():
    """Initialize package."""
    pass

# 5. Lazy imports for heavy modules (optional)
def get_heavy_module():
    from .heavy import HeavyClass
    return HeavyClass
```

### Avoiding Common Structure Mistakes

```python
# ❌ Bad: Too much in __init__.py
# __init__.py
import numpy as np
import pandas as pd
from .core import func1, func2, func3, func4, func5
import logging
import sys
import os
# ... many lines of code

# ✅ Good: Keep __init__.py minimal
# __init__.py
from .core import func1, func2, func3  # Only commonly used

__version__ = "1.0.0"
```

---

## Real-World Examples

### Example 1: Data Processing Package

```
dataproc/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── loader.py
│   ├── cleaner.py
│   └── transformer.py
├── analysis/
│   ├── __init__.py
│   ├── statistics.py
│   └── ml.py
└── visualization/
    ├── __init__.py
    ├── plots.py
    └── charts.py
```

```python
# dataproc/__init__.py
"""
Data Processing Package - Handle data loading, cleaning, and analysis.
"""

__version__ = "1.0.0"
__author__ = "Data Team"

from .core.loader import load_csv, load_json
from .core.cleaner import remove_nulls, normalize
from .core.transformer import scale, encode_categorical
from .analysis.statistics import mean, median, std_dev
from .visualization.plots import line_plot, bar_chart

__all__ = [
    'load_csv', 'load_json',
    'remove_nulls', 'normalize',
    'scale', 'encode_categorical',
    'mean', 'median', 'std_dev',
    'line_plot', 'bar_chart'
]
```

```python
# dataproc/core/loader.py
import csv
import json

def load_csv(filepath):
    """Load data from CSV file."""
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_json(filepath):
    """Load data from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)
```

```python
# dataproc/analysis/statistics.py
def mean(data):
    """Calculate mean of data."""
    if not data:
        return 0
    return sum(data) / len(data)

def median(data):
    """Calculate median of data."""
    if not data:
        return 0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def std_dev(data):
    """Calculate standard deviation."""
    if len(data) < 2:
        return 0
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / (len(data) - 1)
    return variance ** 0.5
```

```python
# main.py
import dataproc as dp

# Load data
data = dp.load_csv("data.csv")
print(f"Loaded {len(data)} rows")

# Clean data
cleaned = dp.remove_nulls(data)
normalized = dp.normalize(cleaned)

# Analyze
values = [row['value'] for row in normalized]
print(f"Mean: {dp.mean(values)}")
print(f"Median: {dp.median(values)}")
print(f"Std Dev: {dp.std_dev(values)}")

# Visualize
dp.line_plot(values)
```

### Example 2: Web Application Package

```
webapp/
├── __init__.py
├── app.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── users.py
│   └── api.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   └── order.py
├── services/
│   ├── __init__.py
│   ├── email.py
│   ├── payment.py
│   └── storage.py
└── templates/
    └── (HTML templates)
```

```python
# webapp/__init__.py
"""
Web Application Package - Full-featured web framework.
"""

from flask import Flask

def create_app(config=None):
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Load configuration
    if config:
        app.config.update(config)
    
    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.users import users_bp
    from .routes.api import api_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Initialize services
    from .services.email import init_email
    init_email(app)
    
    return app
```

```python
# webapp/routes/__init__.py
"""
Routes subpackage.
"""

from .auth import auth_bp
from .users import users_bp
from .api import api_bp

__all__ = ['auth_bp', 'users_bp', 'api_bp']
```

```python
# webapp/models/__init__.py
"""
Database models.
"""

from .user import User
from .product import Product
from .order import Order

__all__ = ['User', 'Product', 'Order']
```

```python
# run.py
from webapp import create_app

app = create_app({
    'DEBUG': True,
    'SECRET_KEY': 'your-secret-key',
    'DATABASE_URL': 'sqlite:///app.db'
})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

### Example 3: Machine Learning Package

```
mlpackage/
├── __init__.py
├── data/
│   ├── __init__.py
│   ├── dataset.py
│   └── preprocessing.py
├── models/
│   ├── __init__.py
│   ├── linear.py
│   ├── tree.py
│   └── neural.py
├── metrics/
│   ├── __init__.py
│   ├── classification.py
│   └── regression.py
└── utils/
    ├── __init__.py
    ├── validation.py
    └── visualization.py
```

```python
# mlpackage/__init__.py
"""
Machine Learning Package - Train and evaluate models.
"""

__version__ = "2.0.0"

from .data.dataset import Dataset
from .data.preprocessing import StandardScaler, MinMaxScaler
from .models.linear import LinearRegression, LogisticRegression
from .models.tree import DecisionTree
from .metrics.classification import accuracy, precision, recall
from .metrics.regression import mae, mse, r2_score

__all__ = [
    'Dataset',
    'StandardScaler', 'MinMaxScaler',
    'LinearRegression', 'LogisticRegression', 'DecisionTree',
    'accuracy', 'precision', 'recall',
    'mae', 'mse', 'r2_score'
]
```

```python
# mlpackage/data/dataset.py
class Dataset:
    def __init__(self, data, target=None):
        self.data = data
        self.target = target
        self.n_samples = len(data)
    
    def split(self, test_size=0.2, random_state=None):
        """Split dataset into train and test."""
        import random
        if random_state:
            random.seed(random_state)
        
        indices = list(range(self.n_samples))
        random.shuffle(indices)
        
        split_idx = int(self.n_samples * (1 - test_size))
        train_idx = indices[:split_idx]
        test_idx = indices[split_idx:]
        
        train_data = [self.data[i] for i in train_idx]
        test_data = [self.data[i] for i in test_idx]
        
        if self.target:
            train_target = [self.target[i] for i in train_idx]
            test_target = [self.target[i] for i in test_idx]
            return Dataset(train_data, train_target), Dataset(test_data, test_target)
        
        return Dataset(train_data), Dataset(test_data)
```

```python
# main.py
from mlpackage import Dataset, StandardScaler, LinearRegression, accuracy

# Load data
data = Dataset(
    data=[[1, 2], [2, 3], [3, 4], [4, 5]],
    target=[2, 4, 6, 8]
)

# Split and scale
train, test = data.split(test_size=0.25)
scaler = StandardScaler()
train.data = scaler.fit_transform(train.data)
test.data = scaler.transform(test.data)

# Train model
model = LinearRegression()
model.fit(train.data, train.target)

# Predict
predictions = model.predict(test.data)
print(f"Predictions: {predictions}")
```

---

## Common Pitfalls

### Pitfall 1: Missing `__init__.py`

```python
# Without __init__.py, Python doesn't recognize directory as package
mypackage/
├── module.py  # No __init__.py

# This will fail
import mypackage  # Not recognized as a package
```

### Pitfall 2: Circular Imports Between Subpackages

```python
# mypackage/module_a.py
from mypackage.module_b import func_b

def func_a():
    return func_b()

# mypackage/module_b.py
from mypackage.module_a import func_a

def func_b():
    return func_a()

# Circular import! Restructure or use local imports
```

### Pitfall 3: `__all__` Not Respecting Underscore Convention

```python
# __init__.py
__all__ = []  # Empty list - nothing exported

# Users can't import anything
from mypackage import *  # Nothing imported
```

### Pitfall 4: Relative Imports in Scripts

```python
# When running a script directly, relative imports fail
# mypackage/script.py
from .module import func  # ImportError when run directly

# Use absolute imports or run as module
# python -m mypackage.script
```

---

## Practice Exercises

### Beginner Level

1. **Simple Package**
   ```python
   # Create package 'shapes' with modules:
   # circle.py (area, circumference)
   # rectangle.py (area, perimeter)
   # triangle.py (area)
   ```

2. **Package Import**
   ```python
   # Import from shapes package
   # Calculate area of circle and rectangle
   ```

3. **`__init__.py` Export**
   ```python
   # Use __all__ to control exports
   # Test wildcard import
   ```

### Intermediate Level

4. **Subpackage Structure**
   ```python
   # Create package with subpackages:
   # math/basic.py
   # math/advanced.py
   # stats/descriptive.py
   ```

5. **Package Initialization**
   ```python
   # Add initialization code in __init__.py
   # Set up logging or configuration
   ```

6. **Lazy Loading**
   ```python
   # Implement lazy loading for heavy modules
   # Load only when accessed
   ```

### Advanced Level

7. **Plugin Architecture**
   ```python
   # Create package that discovers plugins
   # Dynamically load subpackages
   ```

8. **Application Factory**
   ```python
   # Implement app factory pattern
   # Configure package on creation
   ```

9. **Namespace Packages**
   ```python
   # Create namespace package split across directories
   # Use PEP 420 implicit namespace packages
   ```

---

## Quick Reference Card

```python
# Package structure
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

# __init__.py
__version__ = "1.0.0"
__all__ = ['func1', 'func2']
from .module1 import func1, func2

# Import styles
import mypackage
import mypackage.module1
from mypackage import module1
from mypackage.module1 import func1
from mypackage.subpackage import module3

# Aliases
import mypackage as mp
from mypackage.module1 import func1 as f1

# Wildcard (controlled by __all__)
from mypackage import *

# Relative imports
from . import module1
from .module1 import func1
from .. import module2
```

---

## Next Step

- Move to [04_module_search_path.md](04_module_search_path.md) to understand how Python finds modules.

---

*Master packages to organize large Python projects effectively! 🐍✨*
# 📦 MODULES AND PACKAGES – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Modules?](#what-are-modules)
3. [What are Packages?](#what-are-packages)
4. [Importing Modules](#importing-modules)
5. [Standard Library](#standard-library)
6. [Third-Party Modules](#third-party-modules)
7. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Modules** and **packages** allow you to organize Python code into reusable files and directories. They help you structure large projects and avoid code duplication.

```python
# Import a module
import math

# Use functions from the module
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.14159...

# Import from a package
from datetime import datetime
print(datetime.now())
```

**Key Characteristics:**
- ✅ Modules are `.py` files containing Python code
- ✅ Packages are directories containing modules
- ✅ `import` statement brings modules into your code
- ✅ Standard library comes with Python installation
- ✅ Third-party modules can be installed with `pip`

---

## 📖 What are Modules?

A **module** is a single `.py` file that contains functions, classes, and variables. You can create your own modules or use built-in ones.

```python
# Create a file called mymodule.py
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# Use it in another file
import mymodule

print(mymodule.greet("Alice"))  # Hello, Alice!
print(mymodule.PI)              # 3.14159
```

**Benefits of Modules:**
- Organize related code together
- Reuse code across multiple programs
- Avoid naming conflicts
- Make code easier to maintain

---

## 📖 What are Packages?

A **package** is a directory that contains multiple modules and a special `__init__.py` file.

```
mypackage/
├── __init__.py      # Required (can be empty)
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# Import from package
import mypackage.module1
from mypackage import module2
from mypackage.subpackage import module3
```

---

## 📥 Importing Modules

### Import Syntax

| Syntax | Example | Use Case |
|--------|---------|----------|
| `import module` | `import math` | Import entire module |
| `import module as alias` | `import numpy as np` | Shorter alias |
| `from module import name` | `from math import sqrt` | Import specific item |
| `from module import *` | `from math import *` | Import all (avoid) |

```python
# Different import styles
import math
print(math.sqrt(25))  # 5.0

import math as m
print(m.sqrt(25))     # 5.0

from math import sqrt
print(sqrt(25))       # 5.0

from math import sqrt, pi
print(sqrt(25), pi)   # 5.0 3.14159
```

---

## 📚 Standard Library

Python comes with a rich **standard library** of modules.

### Common Standard Library Modules

| Module | Purpose | Example |
|--------|---------|---------|
| `math` | Mathematical functions | `math.sqrt(16)` |
| `cmath` | Complex number math | `cmath.sqrt(-1)` |
| `random` | Random number generation | `random.randint(1,10)` |
| `datetime` | Date and time | `datetime.now()` |
| `os` | Operating system interface | `os.getcwd()` |
| `sys` | System-specific parameters | `sys.argv` |
| `json` | JSON encoding/decoding | `json.dumps(data)` |
| `re` | Regular expressions | `re.search(pattern, text)` |
| `collections` | Specialized containers | `Counter(items)` |
| `itertools` | Efficient looping | `itertools.cycle(iterable)` |
| `functools` | Higher-order functions | `functools.partial(func, arg)` |
| `statistics` | Statistical functions | `statistics.mean(numbers)` |
| `hashlib` | Cryptographic hashing | `hashlib.md5(b'data')` |
| `glob` | File pattern matching | `glob.glob("*.py")` |
| `shutil` | High-level file operations | `shutil.copy(src, dst)` |
| `tempfile` | Temporary files | `tempfile.TemporaryFile()` |
| `subprocess` | Run system commands | `subprocess.run(["ls"])` |

```python
# Standard library examples
import math
import random
import datetime
import json

print(math.factorial(5))           # 120
print(random.randint(1, 100))      # Random number
print(datetime.datetime.now())     # Current time

data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)  # '{"name": "Alice", "age": 30}'
```

---

## 📦 Third-Party Modules

Modules not included with Python that you install using `pip`.

### Installing Modules

```bash
# Install a module
pip install requests

# Install specific version
pip install requests==2.28.0

# Install from requirements file
pip install -r requirements.txt

# Uninstall a module
pip uninstall requests

# List installed modules
pip list
```

### Popular Third-Party Modules

| Module | Purpose | Installation | Example |
|--------|---------|--------------|---------|
| `requests` | HTTP requests | `pip install requests` | `requests.get(url)` |
| `numpy` | Numerical computing | `pip install numpy` | `np.array([1,2,3])` |
| `pandas` | Data analysis | `pip install pandas` | `pd.DataFrame(data)` |
| `matplotlib` | Plotting | `pip install matplotlib` | `plt.plot(x, y)` |
| `flask` | Web framework | `pip install flask` | `@app.route('/')` |
| `django` | Web framework | `pip install django` | `python manage.py runserver` |
| `pytest` | Testing | `pip install pytest` | `pytest test_file.py` |

```python
# Third-party module example (requires installation)
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())
```

---

## 📁 Files in This Folder

### Core Module Files

| File | Description |
|------|-------------|
| `01_creating_modules.md` | Creating and using custom modules |
| `02_import_statement.md` | Import syntax in detail |
| `03_packages.md` | Creating and using packages |
| `04_module_search_path.md` | How Python finds modules |
| `05_circular_imports.md` | Problems and solutions |

### Standard Library Modules (`standard_library/`)

| File | Module | Description |
|------|--------|-------------|
| `01_math.md` | `math` | Mathematical functions |
| `02_cmath.md` | `cmath` | Complex number math |
| `03_random.md` | `random` | Random number generation |
| `04_datetime.md` | `datetime` | Date and time handling |
| `05_os.md` | `os` | Operating system interface |
| `06_sys.md` | `sys` | System parameters |
| `07_json.md` | `json` | JSON encoding/decoding |
| `08_re.md` | `re` | Regular expressions |
| `09_collections.md` | `collections` | Specialized containers |
| `10_itertools.md` | `itertools` | Efficient looping |
| `11_functools.md` | `functools` | Higher-order functions |
| `12_statistics.md` | `statistics` | Statistical functions |
| `13_hashlib.md` | `hashlib` | Cryptographic hashing |
| `14_glob.md` | `glob` | File pattern matching |
| `15_shutil.md` | `shutil` | File operations |
| `16_tempfile.md` | `tempfile` | Temporary files |
| `17_subprocess.md` | `subprocess` | System commands |

### Third-Party Modules (`third_party/`)

| File | Description |
|------|-------------|
| `01_pip.md` | pip package manager |
| `02_requests.md` | HTTP requests library |
| `03_numpy.md` | Numerical computing |
| `04_pandas.md` | Data analysis |
| `05_virtual_env.md` | Virtual environments |

### Practice Files

| File | Description |
|------|-------------|
| `exercises.md` | Practice problems |
| `solutions.md` | Answer key |

---

## 💡 Quick Tips

```python
# ✅ DO: Use specific imports
from math import sqrt, pi

# ❌ DON'T: Use import * (pollutes namespace)
from math import *

# ✅ DO: Use aliases for long module names
import numpy as np

# ✅ DO: Place all imports at the top of the file
import sys
import os
import json

# ✅ DO: Use if __name__ == "__main__" guard
if __name__ == "__main__":
    main()

# ✅ DO: Create __init__.py for packages
# (can be empty file)
```

---

## 📚 Next Steps

After understanding modules and packages basics:
1. Open `01_creating_modules.md` for custom modules
2. Open `02_import_statement.md` for import syntax
3. Explore `standard_library/` for built-in modules
4. Explore `third_party/` for external packages

---

## 🔗 Related Topics

- **Functions** – Code organization within a file
- **Classes** – Object-oriented organization
- **Namespaces** – Name resolution rules
- **Virtual Environments** – Isolated environments

---

*Master modules and packages to organize large Python projects! 🐍✨*

---

## Next Step

- Move to [01_creating_modules.md](01_creating_modules.md) to learn how to create your own modules.
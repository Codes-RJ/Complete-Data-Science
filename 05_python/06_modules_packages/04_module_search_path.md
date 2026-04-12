# 📘 MODULE SEARCH PATH – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Module Search Path?](#what-is-the-module-search-path)
2. [`sys.path` – The Search Path List](#syspath--the-search-path-list)
3. [Default Search Path Order](#default-search-path-order)
4. [Modifying the Search Path](#modifying-the-search-path)
5. [`PYTHONPATH` Environment Variable](#pythonpath-environment-variable)
6. [Site-packages Directory](#site-packages-directory)
7. [`.pth` Files](#pth-files)
8. [Real-World Examples](#real-world-examples)
9. [Common Pitfalls](#common-pitfalls)
10. [Practice Exercises](#practice-exercises)

---

## What is the Module Search Path?

The **module search path** is the list of directories where Python looks for modules and packages when you use an `import` statement.

```python
import sys
print(sys.path)
# ['', '/usr/lib/python39.zip', '/usr/lib/python3.9', ...]
```

**How It Works:**
1. When you write `import mymodule`, Python searches directories in `sys.path`
2. It looks for `mymodule.py` or `mymodule/__init__.py`
3. The first match is used
4. If no match found, `ModuleNotFoundError` is raised

```python
# Python searches for module in this order:
import mymodule

# 1. Current directory
# 2. Directories in PYTHONPATH
# 3. Standard library directories
# 4. Site-packages directories
```

---

## `sys.path` – The Search Path List

`s

[2026-04-13T06:28:22.913Z] sys.path` is a Python list containing the module search paths.

### Viewing `sys.path`

```python
import sys
import pprint

# Print all search paths
print(sys.path)

# Pretty print
pprint.pprint(sys.path)

# Each path is a string
for path in sys.path:
    print(path)

# Output example:
# /home/user/myproject          # Current directory
# /usr/lib/python39.zip
# /usr/lib/python3.9
# /usr/lib/python3.9/lib-dynload
# /home/user/.local/lib/python3.9/site-packages
# /usr/local/lib/python3.9/dist-packages
```

### `sys.path` is a List

```python
import sys

# sys.path is a regular Python list
print(type(sys.path))  # <class 'list'>

# You can modify it like any list
print(len(sys.path))
print(sys.path[0])     # First path (usually current directory)

# Check if a path is in sys.path
if '/my/custom/path' in sys.path:
    print("Path exists")
```

---

## Default Search Path Order

### Order of Directories

```python
import sys

for i, path in enumerate(sys.path):
    print(f"{i}: {path}")

# Typical order:
# 0: '' or '.'           # Current directory (empty string means current dir)
# 1: script directory    # Directory of the script being executed
# 2: PYTHONPATH          # Environment variable directories
# 3: standard library    # Python's built-in modules
# 4: site-packages       # Third-party packages
```

### How Python Resolves Imports

```python
# Python uses first match found
# Example: If you have both math.py in current dir and built-in math

# 1. Checks current directory for math.py
# 2. If found, uses it (shadowing built-in)
# 3. If not, checks standard library

# This can cause problems if you name your module same as built-in
# mymath.py is fine, but math.py is dangerous
```

### Script Directory vs Current Directory

```python
# When running a script, sys.path[0] is the script's directory
# Example: python /home/user/project/main.py
# sys.path[0] = '/home/user/project'

# When running interactively (REPL), sys.path[0] is '' (current directory)
```

---

## Modifying the Search Path

### Method 1: `sys.path.append()`

```python
import sys

# Add a directory to the end (lowest priority)
sys.path.append('/home/user/my_modules')

# Now Python will look here if module not found elsewhere
import mymodule
```

### Method 2: `sys.path.insert()`

```python
import sys

# Add at the beginning (highest priority)
sys.path.insert(0, '/home/user/my_modules')

# This module will be found before others
import mymodule

# Add at specific position
sys.path.insert(1, '/home/user/second_choice')
```

### Method 3: `sys.path.remove()`

```python
import sys

# Remove a path (if you want to prevent certain imports)
if '/bad/path' in sys.path:
    sys.path.remove('/bad/path')
```

### Temporary vs Permanent

```python
# Modifications to sys.path are temporary (only for current session)
import sys
sys.path.append('/my/temp/path')

# This change lasts only while the program is running
# Next run, sys.path will be back to default

# For permanent changes, use PYTHONPATH environment variable
```

---

## `PYTHONPATH` Environment Variable

`PYTHONPATH` is an environment variable that adds directories to `sys.path`.

### Setting PYTHONPATH (Unix/Linux/Mac)

```bash
# Temporary (current shell session)
export PYTHONPATH="/path/to/my/modules:$PYTHONPATH"

# Check current value
echo $PYTHONPATH

# Run Python script
python my_script.py

# Multiple directories (colon-separated)
export PYTHONPATH="/path1:/path2:/path3:$PYTHONPATH"
```

### Setting PYTHONPATH (Windows)

```cmd
# Command Prompt
set PYTHONPATH=C:\path\to\modules;%PYTHONPATH%

# PowerShell
$env:PYTHONPATH = "C:\path\to\modules;$env:PYTHONPATH"

# Check
echo %PYTHONPATH%
```

### Permanent PYTHONPATH

```bash
# Add to ~/.bashrc (Linux/Mac)
echo 'export PYTHONPATH="/my/permanent/path:$PYTHONPATH"' >> ~/.bashrc

# Or ~/.profile
echo 'export PYTHONPATH="/my/permanent/path:$PYTHONPATH"' >> ~/.profile

# Reload
source ~/.bashrc
```

### PYTHONPATH in Python

```python
import os
import sys

# Check if PYTHONPATH is set
pythonpath = os.environ.get('PYTHONPATH', '')
print(f"PYTHONPATH: {pythonpath}")

# PYTHONPATH directories appear in sys.path
# They are inserted after the script directory but before standard library
```

---

## Site-packages Directory

`s

[2026-04-13T06:28:22.913Z] ite-packages` is where third-party packages are installed.

### Finding site-packages

```python
import site
import sys

# Get site-packages directories
print(site.getsitepackages())
# ['/usr/local/lib/python3.9/dist-packages', '/usr/lib/python3.9/dist-packages']

# Get user-specific site-packages
print(site.getusersitepackages())
# '/home/user/.local/lib/python3.9/site-packages'

# Check if a package is in site-packages
import numpy
print(numpy.__file__)  # Shows location
```

### Site-packages Structure

```
site-packages/
├── numpy/                 # Package directory
│   ├── __init__.py
│   ├── core/
│   └── ...
├── requests/              # Another package
│   ├── __init__.py
│   └── ...
├── pandas/                # Yet another
├── mypackage.egg-link     # Development mode link
└── easy-install.pth       # .pth file
```

### User vs System Site-packages

```python
# System-wide site-packages (requires sudo/admin)
# /usr/lib/python3.9/site-packages/
# /usr/local/lib/python3.9/dist-packages/

# User-specific site-packages (no admin required)
# ~/.local/lib/python3.9/site-packages/

# pip install --user package_name  # Installs to user site-packages
# pip install package_name         # Installs to system (may need sudo)
```

---

## `.pth` Files

`.pth` (path) files are text files that add directories to `sys.path`.

### Creating `.pth` Files

```python
# Create a .pth file in site-packages directory
# /usr/lib/python3.9/site-packages/my_paths.pth

# Each line is a directory path to add
/home/user/my_modules
/home/user/another_module
/opt/shared_libs

# Comments start with #
# This is a comment
```

### How `.pth` Files Work

```python
# When Python starts, it reads all .pth files in site-packages
# Each directory in the .pth file is added to sys.path

# This is permanent and affects all Python sessions
# No need to modify sys.path in code
```

### Using `.pth` Files for Development

```python
# While developing a package, you can add its parent directory
# /usr/lib/python3.9/site-packages/mydev.pth
/home/user/projects/myproject/src

# Now you can import modules directly
import mypackage  # Finds it from src directory
```

---

## Real-World Examples

### Example 1: Custom Module Directory

```python
# project/
# ├── main.py
# ├── lib/
# │   └── mymodule.py
# └── utils/
#     └── helper.py

# main.py
import sys
import os

# Method 1: Add relative path
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
import mymodule  # Works!

# Method 2: Add absolute path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib'))
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

import mymodule

# Method 3: Use PYTHONPATH (set before running)
# export PYTHONPATH="/path/to/project/lib:$PYTHONPATH"
# python main.py
```

### Example 2: Dynamic Path Addition Based on Environment

```python
# config_paths.py
import os
import sys
from pathlib import Path

def setup_module_paths(environment='development'):
    """Configure module paths based on environment."""
    
    # Get project root
    project_root = Path(__file__).parent.parent
    
    # Common paths
    common_paths = [
        project_root / 'lib',
        project_root / 'shared',
    ]
    
    # Environment-specific paths
    if environment == 'development':
        extra_paths = [
            project_root / 'dev_modules',
            project_root / 'testing',
        ]
    elif environment == 'production':
        extra_paths = [
            project_root / 'prod_modules',
            '/opt/shared_libs',
        ]
    else:
        extra_paths = []
    
    # Add all paths to sys.path (at the beginning for priority)
    for path in common_paths + extra_paths:
        path_str = str(path.resolve())
        if path_str not in sys.path:
            sys.path.insert(0, path_str)
            print(f"Added to path: {path_str}")
    
    # Also support PYTHONPATH environment variable
    pythonpath = os.environ.get('PYTHONPATH', '')
    if pythonpath:
        for path in pythonpath.split(os.pathsep):
            if path and path not in sys.path:
                sys.path.append(path)
                print(f"Added from PYTHONPATH: {path}")

# Usage
if __name__ == "__main__":
    env = os.environ.get('APP_ENV', 'development')
    setup_module_paths(env)
    
    # Now import modules from added paths
    import mycustommodule
```

### Example 3: Module Finder and Loader

```python
# module_finder.py
import sys
import os
import importlib

class CustomModuleFinder:
    """Custom module finder for specific directories."""
    
    def __init__(self, search_dirs):
        self.search_dirs = search_dirs
    
    def find_module(self, fullname, path=None):
        """Find module in custom directories."""
        for search_dir in self.search_dirs:
            # Check for module.py
            module_path = os.path.join(search_dir, f"{fullname}.py")
            if os.path.exists(module_path):
                return CustomModuleLoader(module_path)
            
            # Check for package directory
            package_path = os.path.join(search_dir, fullname)
            if os.path.isdir(package_path) and os.path.exists(os.path.join(package_path, "__init__.py")):
                return CustomModuleLoader(package_path)
        
        return None

class CustomModuleLoader:
    """Custom module loader."""
    
    def __init__(self, path):
        self.path = path
    
    def load_module(self, fullname):
        """Load the module."""
        if fullname in sys.modules:
            return sys.modules[fullname]
        
        # Create module
        spec = importlib.util.spec_from_file_location(fullname, self.path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[fullname] = module
        spec.loader.exec_module(module)
        
        return module

# Install custom finder
custom_dirs = ['/my/custom/modules', '/opt/shared']
sys.meta_path.insert(0, CustomModuleFinder(custom_dirs))

# Now Python will look in custom directories
import my_custom_module  # Found in /my/custom/modules/
```

### Example 4: Virtual Environment Path Management

```python
# virtual_env_paths.py
import sys
import os
from pathlib import Path

def get_virtual_env_paths():
    """Get all paths from current virtual environment."""
    
    # Detect virtual environment
    venv_path = os.environ.get('VIRTUAL_ENV')
    if not venv_path:
        print("Not in a virtual environment")
        return []
    
    venv = Path(venv_path)
    
    # Common virtual environment paths
    paths = []
    
    # Site-packages (where pip installs packages)
    site_packages = venv / 'lib' / f'python{sys.version_info.major}.{sys.version_info.minor}' / 'site-packages'
    if site_packages.exists():
        paths.append(str(site_packages))
    
    # For Windows
    if sys.platform == 'win32':
        site_packages_win = venv / 'Lib' / 'site-packages'
        if site_packages_win.exists():
            paths.append(str(site_packages_win))
    
    # Scripts directory (for executables)
    scripts = venv / 'bin' if sys.platform != 'win32' else venv / 'Scripts'
    if scripts.exists():
        paths.append(str(scripts))
    
    return paths

def ensure_virtual_env_paths():
    """Ensure virtual environment paths are in sys.path."""
    for path in get_virtual_env_paths():
        if path not in sys.path:
            sys.path.insert(0, path)
            print(f"Added virtual env path: {path}")

# Usage
ensure_virtual_env_paths()
print(sys.path[:5])  # First 5 paths
```

### Example 5: Project-Specific Path Configuration

```python
# path_config.py
import os
import sys
from pathlib import Path

class ProjectPathManager:
    """Manage project-specific module paths."""
    
    def __init__(self, project_root=None):
        if project_root is None:
            # Auto-detect project root (looking for specific markers)
            project_root = self.find_project_root()
        
        self.project_root = Path(project_root).resolve()
        self.added_paths = []
    
    def find_project_root(self):
        """Find project root by looking for markers."""
        current = Path.cwd()
        
        # Markers that indicate project root
        markers = ['.git', 'setup.py', 'pyproject.toml', 'requirements.txt']
        
        while current != current.parent:
            for marker in markers:
                if (current / marker).exists():
                    return current
            current = current.parent
        
        return Path.cwd()
    
    def add_module_paths(self):
        """Add common module paths to sys.path."""
        
        # Standard project directories
        directories = [
            self.project_root / 'src',
            self.project_root / 'lib',
            self.project_root / 'modules',
            self.project_root / 'shared',
        ]
        
        # Add each directory if it exists
        for directory in directories:
            if directory.exists() and directory.is_dir():
                path_str = str(directory)
                if path_str not in sys.path:
                    sys.path.insert(0, path_str)
                    self.added_paths.append(path_str)
                    print(f"Added: {path_str}")
        
        return self.added_paths
    
    def add_custom_path(self, path):
        """Add a custom path to sys.path."""
        path_str = str(Path(path).resolve())
        if path_str not in sys.path:
            sys.path.append(path_str)
            self.added_paths.append(path_str)
    
    def get_import_paths(self):
        """Get all import paths (sys.path)."""
        return sys.path.copy()
    
    def show_paths(self):
        """Display current import paths."""
        print("\nCurrent Module Search Paths:")
        print("-" * 50)
        for i, path in enumerate(sys.path):
            marker = "→ " if path in self.added_paths else "  "
            print(f"{marker}{i}: {path}")
        print("-" * 50)

# Usage
manager = ProjectPathManager()
manager.add_module_paths()

# Add custom path
manager.add_custom_path('/opt/my_special_libs')

manager.show_paths()

# Now import modules from added paths
# import my_module
```

---

## Common Pitfalls

### Pitfall 1: Module Name Shadowing

```python
# ❌ Creating a module with same name as built-in
# math.py (your custom module)
def add(a, b):
    return a + b

# main.py
import math  # This imports YOUR math.py, not built-in!
print(math.sqrt(25))  # AttributeError! Your math has no sqrt

# ✅ Use different name
# mymath.py
# import mymath
```

### Pitfall 2: Forgetting `__init__.py`

```python
# Without __init__.py, Python doesn't recognize directory as package
mypackage/
├── module.py  # No __init__.py

# ❌ This fails
import mypackage  # Not a package

# ✅ Add empty __init__.py
mypackage/
├── __init__.py
└── module.py

import mypackage  # Works
```

### Pitfall 3: Relative Imports in Scripts

```python
# mypackage/script.py
from .module import func  # ❌ Relative import when run directly

# This works when run as module:
# python -m mypackage.script

# For direct execution, use absolute import:
from mypackage.module import func  # ✅ Works both ways
```

### Pitfall 4: Modifying `sys.path` Too Late

```python
# ❌ Modifying after import
import mymodule  # Already tried to find it

sys.path.append('/my/path')
import mymodule  # Still won't find it (already cached)

# ✅ Modify before import
sys.path.append('/my/path')
import mymodule  # Works
```

---

## Practice Exercises

### Beginner Level

1. **View Search Path**
   ```python
   # Write code to print all directories in sys.path
   # Format each path on a new line
   ```

2. **Add Custom Directory**
   ```python
   # Add a custom directory to sys.path
   # Import a module from that directory
   ```

3. **Check PYTHONPATH**
   ```python
   # Read PYTHONPATH environment variable
   # Print each directory on a new line
   ```

### Intermediate Level

4. **Conditional Path Addition**
   ```python
   # Add directory to path only if it exists
   # Handle both relative and absolute paths
   ```

5. **Find Module Location**
   ```python
   # Write function that finds where a module is located
   # Return file path or None if not found
   ```

6. **Safe Path Addition**
   ```python
   # Add directory to sys.path without duplicates
   # Ensure path exists before adding
   ```

### Advanced Level

7. **Custom Import Hook**
   ```python
   # Implement custom module finder
   # Load modules from database or network
   ```

8. **Virtual Environment Detector**
   ```python
   # Detect if running in virtual environment
   # Add appropriate paths automatically
   ```

9. **Project Root Finder**
   ```python
   # Auto-detect project root by finding markers
   # Add all relevant subdirectories to path
   ```

---

## Quick Reference Card

```python
# View search path
import sys
print(sys.path)

# Add to path (temporary)
sys.path.append('/my/path')
sys.path.insert(0, '/my/path')  # Higher priority

# Remove from path
sys.path.remove('/bad/path')

# Check if path exists
if '/my/path' in sys.path:
    print("Path exists")

# Environment variable
import os
pythonpath = os.environ.get('PYTHONPATH', '')

# Site-packages
import site
print(site.getsitepackages())
print(site.getusersitepackages())

# Find module location
import mymodule
print(mymodule.__file__)

# Module search order
# 1. Current directory / script directory
# 2. PYTHONPATH directories
# 3. Standard library
# 4. Site-packages

# .pth file (in site-packages)
# /path/to/site-packages/my_paths.pth
# Each line is a directory to add
```

---

## Next Step

- Move to [05_circular_imports.md](05_circular_imports.md) to learn about circular import problems and solutions.

---

*Master module search path to organize and import modules effectively! 🐍✨*
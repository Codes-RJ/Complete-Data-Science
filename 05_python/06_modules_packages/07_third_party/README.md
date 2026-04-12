# 📦 THIRD-PARTY MODULES – OVERVIEW & BASICS

## 📌 Table of Contents
1. [Overview](#overview)
2. [What are Third-Party Modules?](#what-are-third-party-modules)
3. [pip Package Manager](#pip-package-manager)
4. [Installing Packages](#installing-packages)
5. [Requirements Files](#requirements-files)
6. [Virtual Environments](#virtual-environments)
7. [Popular Third-Party Packages](#popular-third-party-packages)
8. [Files in This Folder](#files-in-this-folder)

---

## 📖 Overview

**Third-party modules** are packages developed by the Python community that are not included in the standard library. They extend Python's capabilities for specialized tasks like web requests, data analysis, machine learning, and more.

```python
# Third-party modules need to be installed first
# pip install requests

import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())
```

**Key Characteristics:**
- ✅ Extend Python's functionality
- ✅ Need to be installed with `pip`
- ✅ Hosted on PyPI (Python Package Index)
- ✅ Versioned and regularly updated
- ✅ Can have dependencies on other packages

---

## 📖 What are Third-Party Modules?

Third-party modules are packages created by the Python community to solve specific problems.

```python
# Standard library (no installation needed)
import json
import csv

# Third-party (requires pip install)
import requests
import numpy as np
import pandas as pd
```

**Why Use Third-Party Modules:**
- Don't reinvent the wheel
- Leverage community expertise
- Save development time
- Access specialized functionality
- Benefit from ongoing maintenance

---

## 📦 pip Package Manager

`pip` is the standard package manager for Python. It comes with modern Python installations.

### Checking pip

```bash
# Check pip version
pip --version

# List installed packages
pip list

# Show package info
pip show requests

# Search for packages
pip search "web framework"
```

### Common pip Commands

| Command | Purpose |
|---------|---------|
| `pip install package` | Install a package |
| `pip install package==1.2.3` | Install specific version |
| `pip install package>=1.0` | Install minimum version |
| `pip uninstall package` | Remove a package |
| `pip list` | List installed packages |
| `pip freeze` | List packages (requirements format) |
| `pip show package` | Show package details |
| `pip install --upgrade package` | Upgrade a package |

---

## 📥 Installing Packages

### Basic Installation

```bash
# Install latest version
pip install requests

# Install specific version
pip install requests==2.28.0

# Install minimum version
pip install "requests>=2.25.0"

# Install with extras
pip install "requests[security]"

# Install from a URL
pip install https://example.com/package.zip

# Install from local file
pip install ./package-1.0.0.tar.gz
```

### Installing Multiple Packages

```bash
# Install multiple packages
pip install requests numpy pandas matplotlib

# Install from requirements file
pip install -r requirements.txt
```

### Installation Options

```bash
# Install for user only (not system-wide)
pip install --user requests

# Install in editable/development mode
pip install -e /path/to/package

# Install without dependencies
pip install --no-deps requests

# Force reinstall
pip install --force-reinstall requests

# Upgrade pip itself
pip install --upgrade pip
```

---

## 📄 Requirements Files

`requirements.txt` files list all packages needed for a project.

### Creating requirements.txt

```bash
# Save all installed packages
pip freeze > requirements.txt

# Save only specific packages
pip freeze | grep requests > requirements.txt

# Manual requirements.txt
echo "requests>=2.28.0" >> requirements.txt
echo "numpy==1.24.0" >> requirements.txt
```

### Example requirements.txt

```txt
# requirements.txt
requests>=2.28.0
numpy==1.24.0
pandas>=1.5.0,<2.0.0
matplotlib~=3.6.0
flask
```

### Installing from requirements.txt

```bash
# Install all packages
pip install -r requirements.txt

# Install in specific environment
pip install -r requirements.txt --target ./libs
```

---

## 🎪 Virtual Environments

Virtual environments isolate project dependencies to avoid conflicts.

### Creating Virtual Environments

```bash
# Create virtual environment (Python 3.3+)
python -m venv myproject_env

# Create with specific Python version
python3.10 -m venv myproject_env

# Create in current directory
python -m venv .venv
```

### Activating Virtual Environments

```bash
# Windows
myproject_env\Scripts\activate

# macOS/Linux
source myproject_env/bin/activate

# After activation, terminal shows environment name
(myproject_env) $
```

### Deactivating Virtual Environments

```bash
# Deactivate current environment
deactivate
```

### Managing Environments

```bash
# List all virtual environments (no built-in command)
# They are just directories

# Remove environment
rm -rf myproject_env  # Linux/macOS
rmdir /s myproject_env  # Windows

# Export environment packages
pip freeze > requirements.txt

# Create environment from requirements
python -m venv new_env
source new_env/bin/activate
pip install -r requirements.txt
```

---

## 📚 Popular Third-Party Packages

### Web & Networking

| Package | Purpose | Installation |
|---------|---------|--------------|
| `requests` | HTTP requests | `pip install requests` |
| `beautifulsoup4` | Web scraping | `pip install beautifulsoup4` |
| `flask` | Web framework | `pip install flask` |
| `django` | Web framework | `pip install django` |
| `fastapi` | Modern web framework | `pip install fastapi` |

### Data Science & Analysis

| Package | Purpose | Installation |
|---------|---------|--------------|
| `numpy` | Numerical computing | `pip install numpy` |
| `pandas` | Data analysis | `pip install pandas` |
| `matplotlib` | Plotting | `pip install matplotlib` |
| `seaborn` | Statistical visualization | `pip install seaborn` |
| `scikit-learn` | Machine learning | `pip install scikit-learn` |

### Development Tools

| Package | Purpose | Installation |
|---------|---------|--------------|
| `pytest` | Testing framework | `pip install pytest` |
| `black` | Code formatter | `pip install black` |
| `flake8` | Linter | `pip install flake8` |
| `mypy` | Type checker | `pip install mypy` |
| `ipython` | Enhanced REPL | `pip install ipython` |

### Database

| Package | Purpose | Installation |
|---------|---------|--------------|
| `psycopg2` | PostgreSQL adapter | `pip install psycopg2` |
| `pymongo` | MongoDB driver | `pip install pymongo` |
| `redis` | Redis client | `pip install redis` |
| `sqlalchemy` | ORM | `pip install sqlalchemy` |

### Other Popular Packages

| Package | Purpose | Installation |
|---------|---------|--------------|
| `pillow` | Image processing | `pip install pillow` |
| `python-dotenv` | Environment variables | `pip install python-dotenv` |
| `click` | CLI creation | `pip install click` |
| `tqdm` | Progress bars | `pip install tqdm` |
| `pydantic` | Data validation | `pip install pydantic` |

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `01_pip.md` | Complete pip package manager guide |
| `02_requests.md` | HTTP requests library |
| `03_numpy.md` | Numerical computing with NumPy |
| `04_pandas.md` | Data analysis with pandas |
| `05_virtual_env.md` | Virtual environments guide |

---

## 💡 Quick Tips

```bash
# ✅ DO: Use virtual environments for projects
python -m venv project_env
source project_env/bin/activate

# ✅ DO: Keep requirements.txt updated
pip freeze > requirements.txt

# ✅ DO: Use specific versions for reproducibility
pip install requests==2.28.0

# ❌ DON'T: Install packages globally (use --user or venv)
pip install package  # Without venv, installs globally

# ✅ DO: Upgrade pip regularly
pip install --upgrade pip

# ✅ DO: Use pip cache to speed up installs
pip install --cache-dir /custom/cache package
```

---

## 📚 Next Steps

After understanding third-party modules basics:
1. Open `01_pip.md` for detailed pip guide
2. Open `02_requests.md` for HTTP requests
3. Open `03_numpy.md` for numerical computing
4. Open `04_pandas.md` for data analysis
5. Open `05_virtual_env.md` for virtual environments

---

## 🔗 Related Topics

- **Standard Library** – Built-in modules
- **PyPI** – Python Package Index (pypi.org)
- **setuptools** – Creating distributable packages
- **poetry** – Modern dependency management
- **conda** – Alternative package manager

---

*Master third-party modules to leverage the power of the Python ecosystem! 🐍✨*

---

## Next Step

- Move to [01_pip.md](01_pip.md) to learn about the pip package manager in detail.

---
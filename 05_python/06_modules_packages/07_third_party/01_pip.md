# 📘 PIP – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is pip?](#what-is-pip)
2. [Installing pip](#installing-pip)
3. [Basic pip Commands](#basic-pip-commands)
4. [Installing Packages](#installing-packages)
5. [Managing Package Versions](#managing-package-versions)
6. [Uninstalling Packages](#uninstalling-packages)
7. [Listing Packages](#listing-packages)
8. [Requirements Files](#requirements-files)
9. [Upgrading pip and Packages](#upgrading-pip-and-packages)
10. [Working with Different Package Sources](#working-with-different-package-sources)
11. [Real-World Examples](#real-world-examples)
12. [Practice Exercises](#practice-exercises)

---

## What is pip?

**pip** (pip installs packages) is the standard package manager for Python. It allows you to install, upgrade, and manage third-party packages from the Python Package Index (PyPI) and other repositories.

```bash
# Basic pip commands
pip install requests          # Install a package
pip uninstall requests        # Remove a package
pip list                      # List installed packages
pip freeze                    # List packages in requirements format
```

**Key Characteristics:**
- ✅ Included with Python 3.4+
- ✅ Installs packages from PyPI
- ✅ Manages dependencies automatically
- ✅ Supports version constraints
- ✅ Creates requirements files

---

## Installing pip

### pip is Included in Modern Python

```bash
# Check if pip is installed
pip --version
# pip 23.0.1 from /usr/lib/python3.11/site-packages (python 3.11)

# Python 3.4+ includes pip by default
python -m pip --version
```

### Installing pip (If Missing)

```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Run the script
python get-pip.py

# Verify installation
pip --version
```

### Upgrading pip

```bash
# Upgrade pip itself
pip install --upgrade pip

# Or using python -m
python -m pip install --upgrade pip
```

---

## Basic pip Commands

### Command Overview

| Command | Purpose |
|---------|---------|
| `pip install <package>` | Install a package |
| `pip uninstall <package>` | Remove a package |
| `pip list` | List installed packages |
| `pip freeze` | List packages (requirements format) |
| `pip show <package>` | Show package details |
| `pip search <query>` | Search PyPI |
| `pip download <package>` | Download package without installing |
| `pip wheel <package>` | Build wheel for package |
| `pip check` | Verify installed packages have compatible dependencies |
| `pip help` | Show help |

### Getting Help

```bash
# General help
pip help

# Help for specific command
pip help install
pip install --help
```

---

## Installing Packages

### Basic Installation

```bash
# Install latest version
pip install requests

# Install specific version
pip install requests==2.28.0

# Install minimum version
pip install "requests>=2.25.0"

# Install maximum version
pip install "requests<=2.30.0"

# Install within version range
pip install "requests>=2.25.0,<2.30.0"
```

### Installing Multiple Packages

```bash
# Install multiple packages
pip install requests numpy pandas

# Install from requirements file
pip install -r requirements.txt

# Install with constraints
pip install -c constraints.txt
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

# Install to custom directory
pip install --target ./libs requests

# Install without cache
pip install --no-cache-dir requests
```

### Installing from Different Sources

```bash
# From GitHub
pip install git+https://github.com/requests/requests.git

# From GitHub (specific branch)
pip install git+https://github.com/requests/requests.git@main

# From local directory
pip install ./package-directory

# From local archive
pip install ./package-1.0.0.tar.gz
pip install ./package-1.0.0.whl

# From URL
pip install https://example.com/package-1.0.0.tar.gz
```

---

## Managing Package Versions

### Version Specifiers

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `==` | Exact version | `requests==2.28.0` |
| `>=` | Minimum version | `requests>=2.25.0` |
| `<=` | Maximum version | `requests<=2.30.0` |
| `>` | Greater than | `requests>2.20.0` |
| `<` | Less than | `requests<3.0.0` |
| `~=` | Compatible release | `requests~=2.28.0` (>=2.28.0, <2.29.0) |
| `!=` | Not equal | `requests!=2.25.0` |

### Version Constraints

```bash
# Exact version
pip install requests==2.28.0

# Compatible version (2.28.x)
pip install "requests~=2.28.0"

# Minimum version
pip install "requests>=2.25.0"

# Range
pip install "requests>=2.25.0,<2.30.0"

# Multiple constraints
pip install "requests>=2.20.0,!=2.25.0"
```

### Pre-release Versions

```bash
# Include pre-release versions
pip install --pre requests

# Install specific pre-release
pip install requests==3.0.0b1

# Allow pre-release for all packages
pip install --pre -r requirements.txt
```

---

## Uninstalling Packages

### Basic Uninstall

```bash
# Uninstall a package
pip uninstall requests

# Uninstall multiple packages
pip uninstall requests numpy pandas

# Uninstall without confirmation
pip uninstall -y requests

# Uninstall with dependencies (if no other packages depend on them)
pip uninstall --auto-confirm requests  # Not standard, use -y
```

### Checking Dependencies Before Uninstall

```bash
# Show package dependencies
pip show requests

# Show reverse dependencies (packages that depend on this)
pip show requests | grep Requires

# Check for broken dependencies after uninstall
pip check
```

---

## Listing Packages

### Basic Listing

```bash
# List all installed packages
pip list

# List with outdated packages highlighted
pip list --outdated

# List with details
pip list --verbose

# List without showing pip/setuptools
pip list --not-required
```

### Different Output Formats

```bash
# JSON format
pip list --format=json

# Freeze format (requirements.txt format)
pip freeze

# Columns format (default)
pip list --format=columns

# Legacy format
pip list --format=legacy
```

### Package Information

```bash
# Show detailed package info
pip show requests

# Show with additional fields
pip show --verbose requests

# Show all packages with details
pip list --verbose
```

---

## Requirements Files

`requirements.txt` is a text file listing all packages needed for a project.

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
# Core dependencies
requests>=2.28.0
numpy==1.24.0
pandas>=1.5.0,<2.0.0

# Development dependencies
pytest~=7.2.0
black==23.1.0

# Optional dependencies
# matplotlib
```

### Installing from requirements.txt

```bash
# Install all packages
pip install -r requirements.txt

# Install without dependencies
pip install -r requirements.txt --no-deps

# Install for user only
pip install -r requirements.txt --user

# Install to custom directory
pip install -r requirements.txt --target ./libs
```

### Constraints Files

```txt
# constraints.txt
# These set upper/lower bounds but don't install
requests>=2.20.0,<3.0.0
numpy>=1.20.0
```

```bash
# Install with constraints
pip install -c constraints.txt -r requirements.txt
```

---

## Upgrading pip and Packages

### Upgrading pip

```bash
# Upgrade pip itself
pip install --upgrade pip

# Or using python -m
python -m pip install --upgrade pip

# Upgrade to specific version
pip install pip==23.0.0
```

### Upgrading Packages

```bash
# Upgrade single package
pip install --upgrade requests

# Upgrade multiple packages
pip install --upgrade requests numpy pandas

# Upgrade all outdated packages
pip list --outdated | awk '{print $1}' | xargs pip install --upgrade

# Upgrade with constraints
pip install --upgrade "requests<3.0.0"
```

### Checking for Updates

```bash
# List outdated packages
pip list --outdated

# Show which packages have updates
pip list --outdated --format=json

# Check if specific package has update
pip list --outdated | grep requests
```

---

## Working with Different Package Sources

### Private Repositories

```bash
# Install from private Git repository
pip install git+https://github.com/company/private-repo.git

# Install with authentication
pip install git+https://username:token@github.com/company/private-repo.git

# Install from private PyPI server
pip install --index-url https://private-pypi.com/simple mypackage
```

### Alternative Indexes

```bash
# Use alternative index
pip install --index-url https://pypi.org/simple/ requests

# Use extra index (fallback)
pip install --extra-index-url https://private-pypi.com/simple mypackage

# No index (offline)
pip install --no-index --find-links /path/to/packages mypackage
```

### Caching

```bash
# pip cache directory
pip cache info

# List cached packages
pip cache list

# Remove cached packages
pip cache purge

# Disable cache
pip install --no-cache-dir requests
```

---

## Real-World Examples

### Example 1: Setting Up a Project Environment

```bash
# Create project directory
mkdir myproject
cd myproject

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Upgrade pip
pip install --upgrade pip

# Install packages
pip install requests numpy pandas matplotlib jupyter

# Save requirements
pip freeze > requirements.txt
```

### Example 2: Requirements.txt for Web App

```txt
# requirements.txt for Flask web app
flask==2.3.0
flask-sqlalchemy==3.0.0
flask-migrate==4.0.0
flask-login==0.6.2
python-dotenv==1.0.0
psycopg2-binary==2.9.5
gunicorn==20.1.0
```

```bash
# Install all dependencies
pip install -r requirements.txt
```

### Example 3: Development vs Production

```txt
# requirements-base.txt (common)
requests==2.28.0
numpy==1.24.0

# requirements-dev.txt (development extras)
-r requirements-base.txt
pytest==7.2.0
black==23.1.0
flake8==6.0.0
ipython==8.10.0

# requirements-prod.txt (production only)
-r requirements-base.txt
gunicorn==20.1.0
```

```bash
# Install for development
pip install -r requirements-dev.txt

# Install for production
pip install -r requirements-prod.txt
```

### Example 4: Freeze with Comments

```bash
# Generate requirements with comments
pip freeze | sed 's/^/# /' > requirements.txt
# Then manually edit to organize

# Or use pip-tools
pip install pip-tools
pip-compile requirements.in
```

### Example 5: Offline Installation

```bash
# Download packages on internet-connected machine
pip download -r requirements.txt -d ./offline_packages

# Copy offline_packages to target machine
# Install from offline directory
pip install --no-index --find-links ./offline_packages -r requirements.txt
```

---

## Practice Exercises

### Beginner Level

1. **Install a Package**
   ```bash
   # Install the 'requests' package
   ```

2. **List Packages**
   ```bash
   # List all installed packages
   ```

3. **Uninstall a Package**
   ```bash
   # Uninstall the 'requests' package
   ```

### Intermediate Level

4. **Requirements File**
   ```bash
   # Create requirements.txt with specific versions
   ```

5. **Upgrade Package**
   ```bash
   # Upgrade pip and a package
   ```

6. **Package Info**
   ```bash
   # Show detailed information about numpy
   ```

### Advanced Level

7. **Virtual Environment**
   ```bash
   # Create virtual environment and install packages
   ```

8. **Offline Installation**
   ```bash
   # Download packages for offline use
   ```

9. **Constraints File**
   ```bash
   # Create and use constraints file
   ```

---

## Quick Reference Card

```bash
# Basic commands
pip install package              # Install package
pip uninstall package            # Remove package
pip list                         # List installed
pip freeze                       # List (requirements format)
pip show package                 # Package details
pip search query                 # Search PyPI

# Version specifiers
package==1.2.3                   # Exact version
package>=1.2.0                   # Minimum version
package<=2.0.0                   # Maximum version
package~=1.2.0                   # Compatible release
package!=1.2.3                   # Exclude version

# Installation options
--user                           # User installation
--upgrade                        # Upgrade package
--no-deps                        # Skip dependencies
--force-reinstall                # Reinstall
--target ./libs                  # Custom directory
--no-cache-dir                   # Disable cache

# Requirements files
-r requirements.txt              # Install from file
-c constraints.txt               # Use constraints
-f ./packages                    # Find packages in directory

# Virtual environments
python -m venv venv              # Create venv
source venv/bin/activate         # Activate (Linux/macOS)
venv\Scripts\activate            # Activate (Windows)
deactivate                       # Deactivate

# pip configuration
pip config list                  # Show config
pip config set global.index-url  # Set config
```

---

## Next Step

- Move to [02_requests.md](02_requests.md) to learn about the requests library for HTTP requests.

---

*Master pip to manage Python packages effectively! 🐍✨*
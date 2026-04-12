# 📘 VIRTUAL ENVIRONMENTS – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Virtual Environments?](#what-are-virtual-environments)
2. [Why Use Virtual Environments?](#why-use-virtual-environments)
3. [Creating Virtual Environments](#creating-virtual-environments)
4. [Activating and Deactivating](#activating-and-deactivating)
5. [Managing Packages in Virtual Environments](#managing-packages-in-virtual-environments)
6. [Requirements Files](#requirements-files)
7. [Virtual Environment Tools](#virtual-environment-tools)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What are Virtual Environments?

A **virtual environment** is an isolated Python environment that allows you to manage dependencies for different projects separately. Each virtual environment has its own Python interpreter and package directory.

```bash
# Create a virtual environment
python -m venv myproject_env

# Activate it
source myproject_env/bin/activate  # Linux/macOS
# myproject_env\Scripts\activate   # Windows

# Install packages in isolation
pip install requests

# Deactivate when done
deactivate
```

**Key Characteristics:**
- ✅ Isolated Python environments
- ✅ Project-specific dependencies
- ✅ No conflicts between projects
- ✅ No need for admin privileges
- ✅ Reproducible environments

---

## Why Use Virtual Environments?

### The Problem

```bash
# Without virtual environments, all packages install globally
pip install requests==2.28.0
pip install django==4.0

# Project A needs requests==2.20.0
# Project B needs requests==2.30.0
# Conflict! Can't have both versions globally
```

### The Solution

```bash
# Project A
cd project_a
python -m venv venv
source venv/bin/activate
pip install requests==2.20.0

# Project B
cd project_b
python -m venv venv
source venv/bin/activate
pip install requests==2.30.0

# No conflict! Each project has its own version
```

### Benefits

| Benefit | Description |
|---------|-------------|
| **Isolation** | Dependencies don't interfere across projects |
| **Version Control** | Different projects can use different versions |
| **Reproducibility** | `requirements.txt` captures exact versions |
| **No sudo** | Install packages without admin rights |
| **Clean uninstall** | Just delete the environment folder |
| **Testing** | Test with different Python versions |

---

## Creating Virtual Environments

### Using `venv` (Python 3.3+)

```bash
# Create virtual environment in current directory
python -m venv myenv

# Create with specific Python version
python3.10 -m venv myenv

# Create in specific location
python -m venv /path/to/myenv

# Create without pip (not recommended)
python -m venv --without-pip myenv

# Create with symlinks (Unix)
python -m venv --symlinks myenv

# Create with copies (Windows)
python -m venv --copies myenv
```

### Using `virtualenv` (Third-party, more features)

```bash
# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv myenv

# Create with specific Python version
virtualenv -p python3.10 myenv

# Create without site packages
virtualenv --no-site-packages myenv

# Create with system site packages
virtualenv --system-site-packages myenv
```

### Directory Structure

```
myenv/
├── bin/                    # Scripts (Unix)
│   ├── activate
│   ├── python
│   └── pip
├── Scripts/                # Scripts (Windows)
│   ├── activate.bat
│   ├── python.exe
│   └── pip.exe
├── lib/                    # Packages (Unix)
│   └── python3.x/
│       └── site-packages/
├── Lib/                    # Packages (Windows)
│   └── site-packages/
└── pyvenv.cfg              # Environment configuration
```

---

## Activating and Deactivating

### Linux/macOS Activation

```bash
# Activate virtual environment
source myenv/bin/activate

# After activation, prompt shows environment name
(myenv) $ 

# Check which python is being used
(myenv) $ which python
# /path/to/myenv/bin/python

# Check which pip is being used
(myenv) $ which pip
# /path/to/myenv/bin/pip
```

### Windows Activation (Command Prompt)

```cmd
# Activate
myenv\Scripts\activate.bat

# After activation
(myenv) C:\>

# Check python location
(myenv) C:\> where python
# C:\path\to\myenv\Scripts\python.exe
```

### Windows Activation (PowerShell)

```powershell
# Activate
myenv\Scripts\Activate.ps1

# If execution policy blocks, run:
Set-ExecutionPolicy Unrestricted -Scope Process

# After activation
(myenv) PS C:\>
```

### Deactivating

```bash
# Deactivate current environment (any OS)
deactivate

# Prompt returns to normal
$
```

---

## Managing Packages in Virtual Environments

### Installing Packages

```bash
# Activate environment first
source myenv/bin/activate

# Install packages (goes to virtual environment)
pip install requests
pip install numpy pandas

# Install specific version
pip install django==4.0

# Install from requirements file
pip install -r requirements.txt
```

### Listing Packages

```bash
# List installed packages in current environment
pip list

# List with details
pip list --verbose

# List outdated packages
pip list --outdated

# Generate requirements file
pip freeze > requirements.txt
```

### Uninstalling Packages

```bash
# Uninstall package
pip uninstall requests

# Uninstall multiple
pip uninstall numpy pandas

# Uninstall without confirmation
pip uninstall -y requests
```

### Checking Environment

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check installed packages
pip list

# Check environment path
echo $VIRTUAL_ENV  # Unix
echo %VIRTUAL_ENV%  # Windows
```

---

## Requirements Files

### Creating requirements.txt

```bash
# After installing packages
pip freeze > requirements.txt

# With comments
pip freeze | sed 's/^/# /' > requirements.txt

# Manual requirements.txt
cat > requirements.txt << EOF
requests>=2.28.0
numpy==1.24.0
pandas>=1.5.0,<2.0.0
EOF
```

### Example requirements.txt

```txt
# requirements.txt for web project
flask==2.3.0
flask-sqlalchemy==3.0.0
psycopg2-binary==2.9.5
python-dotenv==1.0.0
gunicorn==20.1.0
```

### Installing from requirements.txt

```bash
# Activate environment
source myenv/bin/activate

# Install all packages
pip install -r requirements.txt

# Install without dependencies
pip install -r requirements.txt --no-deps

# Install for specific Python version
pip install -r requirements.txt --python-version 3.10
```

### Development vs Production Requirements

```txt
# requirements-base.txt (common)
requests==2.28.0
numpy==1.24.0

# requirements-dev.txt (development only)
-r requirements-base.txt
pytest==7.2.0
black==23.1.0
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

---

## Virtual Environment Tools

### `venv` (Built-in, Python 3.3+)

```bash
# Simple, built-in, no extra install
python -m venv myenv
```

### `virtualenv` (Third-party)

```bash
# More features, works with Python 2
pip install virtualenv
virtualenv myenv

# Features: faster, relocatable, more options
virtualenv --relocatable myenv
```

### `pipenv` (Pip + Virtualenv)

```bash
# Higher-level tool
pip install pipenv

# Create environment and install
pipenv install requests

# Install from Pipfile
pipenv install

# Activate
pipenv shell
```

### `poetry` (Modern dependency management)

```bash
# All-in-one tool
pip install poetry

# Create project
poetry new myproject

# Add dependencies
poetry add requests

# Activate shell
poetry shell
```

### `conda` (Anaconda distribution)

```bash
# Create environment
conda create -n myenv python=3.10

# Activate
conda activate myenv

# Install packages
conda install numpy pandas
```

---

## Real-World Examples

### Example 1: Project Setup Script

```bash
#!/bin/bash
# setup_project.sh - Setup new Python project with virtual environment

PROJECT_NAME=$1
if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: ./setup_project.sh <project_name>"
    exit 1
fi

# Create project directory
mkdir $PROJECT_NAME
cd $PROJECT_NAME

# Create virtual environment
python -m venv venv

# Activate and install basic packages
source venv/bin/activate
pip install --upgrade pip

# Create requirements files
touch requirements.txt
touch requirements-dev.txt

# Create initial Python file
cat > main.py << EOF
def main():
    print("Hello from $PROJECT_NAME!")

if __name__ == "__main__":
    main()
EOF

# Create README
cat > README.md << EOF
# $PROJECT_NAME

## Setup
\`\`\`bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Run
\`\`\`bash
python main.py
\`\`\`
EOF

echo "Project $PROJECT_NAME created successfully!"
echo "Activate with: source venv/bin/activate"
```

### Example 2: Multi-Environment Setup

```bash
# Create environments for different purposes
python -m venv dev_env
python -m venv test_env
python -m venv prod_env

# Development environment
source dev_env/bin/activate
pip install ipython pytest black flake8
pip freeze > dev_requirements.txt
deactivate

# Test environment
source test_env/bin/activate
pip install pytest pytest-cov
pip freeze > test_requirements.txt
deactivate

# Production environment (minimal)
source prod_env/bin/activate
pip install gunicorn
pip freeze > prod_requirements.txt
deactivate
```

### Example 3: CI/CD Pipeline with Virtual Environments

```yaml
# .github/workflows/test.yml
name: Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10, 3.11]
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Create virtual environment
      run: python -m venv venv
    
    - name: Activate and install dependencies
      run: |
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements-dev.txt
    
    - name: Run tests
      run: |
        source venv/bin/activate
        pytest tests/
```

### Example 4: Environment Comparison Script

```python
# check_env.py
import sys
import os
import site

def check_environment():
    """Check current Python environment details"""
    print("=" * 50)
    print("PYTHON ENVIRONMENT INFO")
    print("=" * 50)
    
    # Python version
    print(f"\nPython version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    # Virtual environment detection
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    print(f"\nIn virtual environment: {in_venv}")
    
    if in_venv:
        print(f"Virtual environment: {sys.prefix}")
    
    # Site packages
    print(f"\nSite packages directories:")
    for path in site.getsitepackages():
        print(f"  {path}")
    
    # PATH
    print(f"\nPATH:")
    for path in sys.path[:5]:
        print(f"  {path}")
    
    # Installed packages
    import subprocess
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    print(f"\nInstalled packages:\n{result.stdout[:500]}...")

if __name__ == "__main__":
    check_environment()
```

### Example 5: Virtual Environment Wrapper Script

```bash
#!/bin/bash
# ve.sh - Virtual environment helper script

VE_DIR=".venv"

function ve_create() {
    if [ -d "$VE_DIR" ]; then
        echo "Virtual environment already exists"
        return 1
    fi
    python -m venv "$VE_DIR"
    echo "Created virtual environment in $VE_DIR"
}

function ve_activate() {
    if [ ! -d "$VE_DIR" ]; then
        echo "No virtual environment found. Run: ve_create"
        return 1
    fi
    source "$VE_DIR/bin/activate"
    echo "Activated virtual environment"
}

function ve_install() {
    ve_activate
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        echo "No requirements.txt found"
    fi
}

function ve_freeze() {
    ve_activate
    pip freeze > requirements.txt
    echo "Updated requirements.txt"
}

function ve_list() {
    ve_activate
    pip list
}

function ve_remove() {
    deactivate 2>/dev/null
    rm -rf "$VE_DIR"
    echo "Removed virtual environment"
}

function ve_help() {
    echo "Usage: ve.sh [command]"
    echo ""
    echo "Commands:"
    echo "  create    - Create virtual environment"
    echo "  activate  - Activate virtual environment"
    echo "  install   - Install from requirements.txt"
    echo "  freeze    - Update requirements.txt"
    echo "  list      - List installed packages"
    echo "  remove    - Remove virtual environment"
    echo "  help      - Show this help"
}

# Main
case "${1:-help}" in
    create) ve_create ;;
    activate) ve_activate ;;
    install) ve_install ;;
    freeze) ve_freeze ;;
    list) ve_list ;;
    remove) ve_remove ;;
    *) ve_help ;;
esac
```

---

## Practice Exercises

### Beginner Level

1. **Create Environment**
   ```bash
   # Create virtual environment named 'test_env'
   ```

2. **Install Package**
   ```bash
   # Activate environment and install requests
   ```

3. **Generate Requirements**
   ```bash
   # Generate requirements.txt from installed packages
   ```

### Intermediate Level

4. **Multiple Environments**
   ```bash
   # Create dev and prod environments with different packages
   ```

5. **Requirements Management**
   ```bash
   # Create base, dev, and prod requirements files
   ```

6. **Environment Check**
   ```bash
   # Write script to check if running in virtual environment
   ```

### Advanced Level

7. **Project Setup Script**
   ```bash
   # Automate project setup with virtual environment
   ```

8. **CI/CD Integration**
   ```bash
   # Configure GitHub Actions with virtual environments
   ```

9. **Custom Wrapper**
   ```bash
   # Create shell script to manage virtual environments
   ```

---

## Quick Reference Card

```bash
# Create
python -m venv myenv              # Create virtual environment
virtualenv myenv                  # Using virtualenv (third-party)

# Activate (Linux/macOS)
source myenv/bin/activate

# Activate (Windows CMD)
myenv\Scripts\activate.bat

# Activate (Windows PowerShell)
myenv\Scripts\Activate.ps1

# Deactivate
deactivate

# Package management (after activation)
pip install package               # Install package
pip install -r requirements.txt   # Install from file
pip freeze > requirements.txt     # Save packages
pip list                          # List packages
pip uninstall package             # Remove package

# Check environment
which python                      # Python location (Unix)
where python                      # Python location (Windows)
echo $VIRTUAL_ENV                 # Environment path (Unix)
echo %VIRTUAL_ENV%                # Environment path (Windows)

# Delete environment
rm -rf myenv                      # Linux/macOS
rmdir /s myenv                    # Windows

# Tools
venv                              # Built-in (Python 3.3+)
virtualenv                        # Third-party, more features
pipenv                            # Pip + Virtualenv
poetry                            # Modern dependency management
conda                             # Anaconda distribution
```

---

## Next Step

- Move to [07_file_handling/README.md](../07_file_handling/README.md) to learn about file operations.

---

*Master virtual environments to manage project dependencies like a pro! 🐍✨*
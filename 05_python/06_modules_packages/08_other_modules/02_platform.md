# 📘 PLATFORM MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Platform Module?](#what-is-the-platform-module)
2. [Operating System Information](#operating-system-information)
3. [Hardware Information](#hardware-information)
4. [Python Implementation Information](#python-implementation-information)
5. [Cross-Platform Code Examples](#cross-platform-code-examples)
6. [Real-World Examples](#real-world-examples)
7. [Practice Exercises](#practice-exercises)

---

## What is the Platform Module?

The `platform` module provides functions to access information about the underlying platform (operating system, hardware, Python implementation).

```python
import platform

# Operating system
print(platform.system())      # 'Windows', 'Linux', 'Darwin'
print(platform.release())     # Kernel version
print(platform.version())     # OS version

# Hardware
print(platform.machine())     # 'AMD64', 'x86_64', 'arm64'
print(platform.processor())   # CPU info

# Python
print(platform.python_version())  # '3.11.0'
print(platform.python_implementation())  # 'CPython'
```

**Key Characteristics:**
- ✅ Cross-platform compatibility
- ✅ Detect OS, hardware, Python version
- ✅ Write platform-specific code
- ✅ No external dependencies

---

## Operating System Information

### `platform.system()` – OS Name

```python
import platform

system = platform.system()
print(f"OS: {system}")

# Common return values:
# 'Windows' - Microsoft Windows
# 'Linux' - Linux
# 'Darwin' - macOS
# 'Java' - Java Virtual Machine
```

### `platform.release()` – OS Release Version

```python
import platform

release = platform.release()
print(f"Release: {release}")

# Examples:
# Windows: '10', '11'
# Linux: '5.15.0-91-generic'
# macOS: '21.6.0'
```

### `platform.version()` – OS Version String

```python
import platform

version = platform.version()
print(f"Version: {version}")

# Examples:
# Windows: '10.0.19045'
# Linux: '#1 SMP Fri Nov 18 15:30:00 UTC 2024'
# macOS: 'Darwin Kernel Version 21.6.0'
```

### `platform.platform()` – Complete Platform String

```python
import platform

info = platform.platform()
print(f"Platform: {info}")

# Examples:
# Windows: 'Windows-10-10.0.19045-SP0'
# Linux: 'Linux-5.15.0-91-generic-x86_64-with-glibc2.35'
# macOS: 'macOS-12.6.3-arm64-arm-64bit'
```

### `platform.uname()` – Detailed System Information

```python
import platform

uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Access as tuple
system, node, release, version, machine, processor = platform.uname()
```

---

## Hardware Information

### `platform.machine()` – Hardware Architecture

```python
import platform

machine = platform.machine()
print(f"Machine: {machine}")

# Common values:
# 'AMD64', 'x86_64' - 64-bit Intel/AMD
# 'arm64', 'aarch64' - 64-bit ARM
# 'i386', 'i686' - 32-bit Intel
```

### `platform.processor()` – CPU Information

```python
import platform

processor = platform.processor()
print(f"Processor: {processor}")

# May return empty string on some systems
if processor:
    print(f"CPU: {processor}")
else:
    print("Processor info not available")
```

---

## Python Implementation Information

### `platform.python_version()` – Python Version

```python
import platform

version = platform.python_version()
print(f"Python version: {version}")  # '3.11.0'

# Get as tuple
version_tuple = platform.python_version_tuple()
print(f"Major: {version_tuple[0]}")
print(f"Minor: {version_tuple[1]}")
print(f"Patch: {version_tuple[2]}")
```

### `platform.python_implementation()` – Python Implementation

```python
import platform

impl = platform.python_implementation()
print(f"Implementation: {impl}")

# Common values:
# 'CPython' - Standard Python
# 'PyPy' - PyPy implementation
# 'Jython' - Java implementation
# 'IronPython' - .NET implementation
```

### `platform.python_compiler()` – Compiler Information

```python
import platform

compiler = platform.python_compiler()
print(f"Compiler: {compiler}")
# Example: 'GCC 11.4.0'
```

### `platform.python_build()` – Build Information

```python
import platform

build_no, build_date = platform.python_build()
print(f"Build: {build_no}")
print(f"Build date: {build_date}")
```

---

## Cross-Platform Code Examples

### Platform Detection Pattern

```python
import platform
import os
import sys

def get_platform_info():
    """Get detailed platform information"""
    info = {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'python_version': platform.python_version(),
        'python_impl': platform.python_implementation()
    }
    return info

# Platform-specific code
def get_temp_dir():
    """Get temporary directory path"""
    if platform.system() == 'Windows':
        return os.environ.get('TEMP', 'C:\\Windows\\Temp')
    else:
        return '/tmp'

def get_user_home():
    """Get user home directory"""
    if platform.system() == 'Windows':
        return os.environ.get('USERPROFILE', 'C:\\Users')
    else:
        return os.environ.get('HOME', '/home')

def clear_screen():
    """Clear terminal screen"""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
```

### Platform-Specific Functionality

```python
import platform
import subprocess

def get_installed_packages():
    """Get list of installed packages (platform-specific)"""
    if platform.system() == 'Windows':
        # Windows: use pip list
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        return result.stdout
    else:
        # Unix: use pip list
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        return result.stdout

def open_file(filepath):
    """Open file with default application"""
    system = platform.system()
    
    if system == 'Windows':
        os.startfile(filepath)
    elif system == 'Darwin':  # macOS
        subprocess.run(['open', filepath])
    else:  # Linux
        subprocess.run(['xdg-open', filepath])
```

---

## Real-World Examples

### Example 1: Cross-Platform Path Manager

```python
import platform
import os
from pathlib import Path

class CrossPlatformPath:
    @staticmethod
    def get_app_data_dir(app_name):
        """Get application data directory"""
        system = platform.system()
        
        if system == 'Windows':
            base = os.environ.get('APPDATA', '')
            return Path(base) / app_name
        elif system == 'Darwin':  # macOS
            base = Path.home() / 'Library' / 'Application Support'
            return base / app_name
        else:  # Linux
            base = Path.home() / '.local' / 'share'
            return base / app_name
    
    @staticmethod
    def get_config_dir(app_name):
        """Get configuration directory"""
        system = platform.system()
        
        if system == 'Windows':
            base = os.environ.get('APPDATA', '')
            return Path(base) / app_name / 'config'
        elif system == 'Darwin':
            base = Path.home() / 'Library' / 'Preferences'
            return base / app_name
        else:
            base = Path.home() / '.config'
            return base / app_name
    
    @staticmethod
    def get_cache_dir(app_name):
        """Get cache directory"""
        system = platform.system()
        
        if system == 'Windows':
            base = os.environ.get('LOCALAPPDATA', '')
            return Path(base) / app_name / 'cache'
        elif system == 'Darwin':
            base = Path.home() / 'Library' / 'Caches'
            return base / app_name
        else:
            base = Path.home() / '.cache'
            return base / app_name

# Usage
app_name = "MyApp"
data_dir = CrossPlatformPath.get_app_data_dir(app_name)
config_dir = CrossPlatformPath.get_config_dir(app_name)
cache_dir = CrossPlatformPath.get_cache_dir(app_name)

print(f"Data dir: {data_dir}")
print(f"Config dir: {config_dir}")
print(f"Cache dir: {cache_dir}")
```

### Example 2: System Information Reporter

```python
import platform
import os
import psutil  # Third-party, for additional info

class SystemReporter:
    @staticmethod
    def get_all_info():
        """Get comprehensive system information"""
        info = {}
        
        # OS Information
        info['os'] = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'platform': platform.platform(),
        }
        
        # Hardware Information
        info['hardware'] = {
            'machine': platform.machine(),
            'processor': platform.processor(),
            'cpu_count': os.cpu_count(),
        }
        
        # Python Information
        info['python'] = {
            'version': platform.python_version(),
            'implementation': platform.python_implementation(),
            'compiler': platform.python_compiler(),
            'build': platform.python_build(),
        }
        
        # Additional info using psutil (if available)
        try:
            import psutil
            info['memory'] = {
                'total': psutil.virtual_memory().total,
                'available': psutil.virtual_memory().available,
            }
            info['disk'] = {
                'total': psutil.disk_usage('/').total,
                'free': psutil.disk_usage('/').free,
            }
        except ImportError:
            pass
        
        return info
    
    @staticmethod
    def print_report():
        """Print formatted system report"""
        info = SystemReporter.get_all_info()
        
        print("=" * 50)
        print("SYSTEM INFORMATION REPORT")
        print("=" * 50)
        
        print("\n[OPERATING SYSTEM]")
        for key, value in info['os'].items():
            print(f"  {key}: {value}")
        
        print("\n[HARDWARE]")
        for key, value in info['hardware'].items():
            print(f"  {key}: {value}")
        
        print("\n[PYTHON]")
        for key, value in info['python'].items():
            print(f"  {key}: {value}")
        
        if 'memory' in info:
            print("\n[MEMORY]")
            print(f"  total: {info['memory']['total'] / (1024**3):.2f} GB")
            print(f"  available: {info['memory']['available'] / (1024**3):.2f} GB")
        
        print("=" * 50)

# Usage
SystemReporter.print_report()
```

### Example 3: Platform-Aware File Operations

```python
import platform
import os
import shutil

class FileOperations:
    @staticmethod
    def get_desktop_path():
        """Get desktop path"""
        system = platform.system()
        
        if system == 'Windows':
            return os.path.join(os.environ['USERPROFILE'], 'Desktop')
        elif system == 'Darwin':
            return os.path.join(os.path.expanduser('~'), 'Desktop')
        else:
            return os.path.join(os.path.expanduser('~'), 'Desktop')
    
    @staticmethod
    def get_documents_path():
        """Get documents path"""
        system = platform.system()
        
        if system == 'Windows':
            return os.path.join(os.environ['USERPROFILE'], 'Documents')
        elif system == 'Darwin':
            return os.path.join(os.path.expanduser('~'), 'Documents')
        else:
            return os.path.join(os.path.expanduser('~'), 'Documents')
    
    @staticmethod
    def get_downloads_path():
        """Get downloads path"""
        system = platform.system()
        
        if system == 'Windows':
            return os.path.join(os.environ['USERPROFILE'], 'Downloads')
        elif system == 'Darwin':
            return os.path.join(os.path.expanduser('~'), 'Downloads')
        else:
            return os.path.join(os.path.expanduser('~'), 'Downloads')
    
    @staticmethod
    def open_in_explorer(path):
        """Open folder in file explorer"""
        system = platform.system()
        
        if not os.path.exists(path):
            print(f"Path does not exist: {path}")
            return
        
        if system == 'Windows':
            os.startfile(path)
        elif system == 'Darwin':
            subprocess.run(['open', path])
        else:
            subprocess.run(['xdg-open', path])
    
    @staticmethod
    def get_trash_path():
        """Get trash/recycle bin path"""
        system = platform.system()
        
        if system == 'Windows':
            return os.path.join(os.environ['SYSTEMDRIVE'], '$Recycle.Bin')
        elif system == 'Darwin':
            return os.path.join(os.path.expanduser('~'), '.Trash')
        else:
            return os.path.join(os.path.expanduser('~'), '.local/share/Trash')

# Usage
print(f"Desktop: {FileOperations.get_desktop_path()}")
print(f"Documents: {FileOperations.get_documents_path()}")
print(f"Downloads: {FileOperations.get_downloads_path()}")
print(f"Trash: {FileOperations.get_trash_path()}")
```

### Example 4: Cross-Platform Process Manager

```python
import platform
import subprocess
import os

class ProcessManager:
    @staticmethod
    def kill_process(pid):
        """Kill process by PID"""
        system = platform.system()
        
        if system == 'Windows':
            subprocess.run(['taskkill', '/F', '/PID', str(pid)])
        else:
            os.kill(pid, 9)  # SIGKILL
    
    @staticmethod
    def list_processes():
        """List running processes"""
        system = platform.system()
        
        if system == 'Windows':
            result = subprocess.run(['tasklist'], capture_output=True, text=True)
            return result.stdout
        else:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            return result.stdout
    
    @staticmethod
    def get_process_info(pid):
        """Get process information"""
        system = platform.system()
        
        if system == 'Windows':
            result = subprocess.run(['tasklist', '/FI', f'PID eq {pid}'], 
                                   capture_output=True, text=True)
            return result.stdout
        else:
            result = subprocess.run(['ps', '-p', str(pid), '-o', 'pid,ppid,user,%cpu,%mem,etime,cmd'],
                                   capture_output=True, text=True)
            return result.stdout
    
    @staticmethod
    def is_process_running(pid):
        """Check if process is running"""
        system = platform.system()
        
        if system == 'Windows':
            result = subprocess.run(['tasklist', '/FI', f'PID eq {pid}'], 
                                   capture_output=True, text=True)
            return str(pid) in result.stdout
        else:
            try:
                os.kill(pid, 0)  # Signal 0 doesn't kill, just checks
                return True
            except OSError:
                return False

# Usage
import time

# Start a long-running process (for demo)
# process = subprocess.Popen(['sleep', '30'])
# pid = process.pid
# print(f"Process started with PID: {pid}")
# 
# time.sleep(2)
# print(f"Is running: {ProcessManager.is_process_running(pid)}")
# ProcessManager.kill_process(pid)
# print(f"Is running after kill: {ProcessManager.is_process_running(pid)}")
```

### Example 5: Dependency Checker

```python
import platform
import sys
import subprocess

class DependencyChecker:
    @staticmethod
    def check_python_version(min_version=(3, 8)):
        """Check Python version"""
        current = sys.version_info[:2]
        if current >= min_version:
            print(f"✓ Python {'.'.join(map(str, current))} meets minimum {'.'.join(map(str, min_version))}")
            return True
        else:
            print(f"✗ Python {'.'.join(map(str, current))} is below {'.'.join(map(str, min_version))}")
            return False
    
    @staticmethod
    def check_command_exists(command):
        """Check if command exists in PATH"""
        system = platform.system()
        
        if system == 'Windows':
            cmd = ['where', command]
        else:
            cmd = ['which', command]
        
        result = subprocess.run(cmd, capture_output=True)
        exists = result.returncode == 0
        
        if exists:
            print(f"✓ Command '{command}' found")
        else:
            print(f"✗ Command '{command}' not found")
        
        return exists
    
    @staticmethod
    def check_package(package_name):
        """Check if Python package is installed"""
        try:
            __import__(package_name)
            print(f"✓ Package '{package_name}' is installed")
            return True
        except ImportError:
            print(f"✗ Package '{package_name}' is not installed")
            return False
    
    @staticmethod
    def get_system_info():
        """Get system information summary"""
        info = {
            'os': platform.system(),
            'os_version': platform.release(),
            'architecture': platform.machine(),
            'python_version': platform.python_version(),
            'python_impl': platform.python_implementation(),
            'cpu_count': os.cpu_count()
        }
        return info
    
    @staticmethod
    def print_dependency_report(requirements):
        """Print dependency report"""
        print("=" * 50)
        print("DEPENDENCY CHECK REPORT")
        print("=" * 50)
        
        print("\n[SYSTEM INFORMATION]")
        for key, value in DependencyChecker.get_system_info().items():
            print(f"  {key}: {value}")
        
        print("\n[REQUIREMENTS CHECK]")
        for req in requirements:
            if req['type'] == 'python_version':
                DependencyChecker.check_python_version(req['version'])
            elif req['type'] == 'command':
                DependencyChecker.check_command_exists(req['name'])
            elif req['type'] == 'package':
                DependencyChecker.check_package(req['name'])
        
        print("=" * 50)

# Usage
requirements = [
    {'type': 'python_version', 'version': (3, 9)},
    {'type': 'command', 'name': 'git'},
    {'type': 'command', 'name': 'python'},
    {'type': 'package', 'name': 'requests'},
    {'type': 'package', 'name': 'numpy'},
]

# DependencyChecker.print_dependency_report(requirements)
```

---

## Practice Exercises

### Beginner Level

1. **Detect OS**
   ```python
   # Print the operating system name
   ```

2. **Python Version**
   ```python
   # Print Python version and implementation
   ```

3. **Machine Architecture**
   ```python
   # Print machine architecture (32-bit or 64-bit)
   ```

### Intermediate Level

4. **Cross-Platform Path**
   ```python
   # Get platform-specific temp directory path
   ```

5. **System Reporter**
   ```python
   # Create function that returns system information dictionary
   ```

6. **Platform-Specific Code**
   ```python
   # Write function that behaves differently on Windows vs Unix
   ```

### Advanced Level

7. **Dependency Checker**
   ```python
   # Create tool to check system requirements
   ```

8. **Cross-Platform Process Manager**
   ```python
   # Implement process listing for all platforms
   ```

9. **Environment Setup Script**
   ```python
   # Create script that sets up environment based on OS
   ```

---

## Quick Reference Card

```python
import platform

# OS Information
platform.system()               # 'Windows', 'Linux', 'Darwin'
platform.release()              # OS release version
platform.version()              # OS version string
platform.platform()             # Complete platform string
platform.uname()                # Named tuple of system info

# Hardware Information
platform.machine()              # Hardware architecture
platform.processor()            # CPU information

# Python Information
platform.python_version()       # '3.11.0'
platform.python_version_tuple() # ('3', '11', '0')
platform.python_implementation() # 'CPython', 'PyPy', etc.
platform.python_compiler()      # Compiler information
platform.python_build()         # Build number and date

# Cross-platform patterns
if platform.system() == 'Windows':
    # Windows-specific code
elif platform.system() == 'Darwin':
    # macOS-specific code
else:
    # Linux/Unix code

# Common cross-platform paths
# Windows: os.environ['APPDATA']
# macOS: ~/Library/Application Support
# Linux: ~/.local/share
```

---

## Next Step

- Move to [03_shlex.md](03_shlex.md) to learn about shell lexing and quoting.

---

*Master the platform module to write truly cross-platform Python code! 🐍✨*
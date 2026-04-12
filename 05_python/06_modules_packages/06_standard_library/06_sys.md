# 📘 SYS MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Sys Module?](#what-is-the-sys-module)
2. [Command Line Arguments](#command-line-arguments)
3. [System Path](#system-path)
4. [Standard Streams](#standard-streams)
5. [Exit and Status Codes](#exit-and-status-codes)
6. [Python Version Information](#python-version-information)
7. [System Information](#system-information)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What is the Sys Module?

The `sys` module provides access to system-specific parameters and functions. It allows you to interact with the Python runtime environment.

```python
import sys

# Command line arguments
print(sys.argv)  # ['script.py', 'arg1', 'arg2']

# Python version
print(sys.version)  # 3.12.0 (main, ...)

# Exit program
sys.exit(0)  # Successful exit
```

**Key Characteristics:**
- ✅ Access to command-line arguments
- ✅ Control Python's runtime environment
- ✅ Standard input/output/error streams
- ✅ System exit functionality
- ✅ Version and platform information

---

## Command Line Arguments

### `sys.argv` – Command Line Arguments

```python
import sys

# Print all arguments
print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")

# Example: python script.py arg1 arg2 arg3
# Script name: script.py
# Arguments: ['arg1', 'arg2', 'arg3']
```

### Parsing Command Line Arguments

```python
import sys

def parse_args():
    """Simple command line argument parser"""
    args = sys.argv[1:]
    options = {}
    positional = []
    
    i = 0
    while i < len(args):
        if args[i].startswith('--'):
            # Long option
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                options[key] = args[i + 1]
                i += 2
            else:
                options[key] = True
                i += 1
        elif args[i].startswith('-'):
            # Short option
            key = args[i][1:]
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                options[key] = args[i + 1]
                i += 2
            else:
                options[key] = True
                i += 1
        else:
            # Positional argument
            positional.append(args[i])
            i += 1
    
    return options, positional

# Usage
# python script.py --name Alice --age 30 file.txt
options, positional = parse_args()
print(f"Options: {options}")
print(f"Positional: {positional}")
```

---

## System Path

### `sys.path` – Module Search Path

```python
import sys

# View module search path
for i, path in enumerate(sys.path):
    print(f"{i}: {path}")

# Add custom path
sys.path.append('/my/custom/path')

# Insert at beginning (higher priority)
sys.path.insert(0, '/my/priority/path')

# Remove path
if '/bad/path' in sys.path:
    sys.path.remove('/bad/path')
```

### `sys.prefix` – Python Installation Prefix

```python
import sys

print(f"Python prefix: {sys.prefix}")
print(f"Executable prefix: {sys.exec_prefix}")
print(f"Base prefix: {sys.base_prefix}")
```

---

## Standard Streams

### `sys.stdin` – Standard Input

```python
import sys

# Read single line
line = sys.stdin.readline()
print(f"Read: {line}")

# Read all lines
for line in sys.stdin:
    print(f"Line: {line.strip()}")

# Read entire input
data = sys.stdin.read()
print(f"Data length: {len(data)}")
```

### `sys.stdout` – Standard Output

```python
import sys

# Write to stdout
sys.stdout.write("Hello World\n")

# Print redirection
original_stdout = sys.stdout
sys.stdout = open('output.txt', 'w')
print("This goes to file")
sys.stdout = original_stdout
print("Back to console")
```

### `sys.stderr` – Standard Error

```python
import sys

# Write to stderr
sys.stderr.write("Error message\n")

# Redirect stderr
original_stderr = sys.stderr
sys.stderr = open('error.log', 'w')
print("Error logged", file=sys.stderr)
sys.stderr = original_stderr
```

### Redirecting Output Example

```python
import sys
from io import StringIO

class OutputCapture:
    """Capture stdout/stderr for testing"""
    
    def __init__(self):
        self.stdout = StringIO()
        self.stderr = StringIO()
    
    def __enter__(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        return self
    
    def __exit__(self, *args):
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
    
    def get_output(self):
        return self.stdout.getvalue()
    
    def get_error(self):
        return self.stderr.getvalue()

# Usage
with OutputCapture() as capture:
    print("Hello World")
    sys.stderr.write("Error occurred\n")

print(f"Captured output: {capture.get_output()}")
print(f"Captured error: {capture.get_error()}")
```

---

## Exit and Status Codes

### `sys.exit()` – Exit Program

```python
import sys

# Successful exit
sys.exit(0)

# Exit with error
sys.exit(1)

# Exit with message
sys.exit("Error: Something went wrong")

# Custom exit code
sys.exit(42)
```

### Exit Code Conventions

| Code | Meaning |
|------|---------|
| 0 | Successful execution |
| 1 | General error |
| 2 | Command line usage error |
| 126 | Command invoked cannot execute |
| 127 | Command not found |
| 128 | Invalid exit argument |
| 130 | Script terminated by Ctrl-C |

```python
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>", file=sys.stderr)
        sys.exit(2)  # Command line usage error
    
    try:
        # Do something
        pass
    except FileNotFoundError:
        print("File not found", file=sys.stderr)
        sys.exit(1)  # General error
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
    
    sys.exit(0)  # Success

if __name__ == "__main__":
    main()
```

---

## Python Version Information

### `sys.version` – Version String

```python
import sys

print(sys.version)
# 3.12.0 (main, Oct 2 2023, 10:00:00) [GCC 9.4.0]

# Parse version
version = sys.version.split()[0]
print(f"Python {version}")
```

### `sys.version_info` – Version Tuple

```python
import sys

# Version info as tuple
print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=0, releaselevel='final', serial=0)

# Check Python version
if sys.version_info < (3, 10):
    print("This script requires Python 3.10 or higher")
    sys.exit(1)

# Access components
print(f"Major: {sys.version_info.major}")
print(f"Minor: {sys.version_info.minor}")
print(f"Micro: {sys.version_info.micro}")
print(f"Release level: {sys.version_info.releaselevel}")
```

### `sys.hexversion` – Version as Integer

```python
import sys

print(hex(sys.hexversion))  # 0x30a00f0

# Compare versions
if sys.hexversion >= 0x30a0000:
    print("Python 3.10 or higher")
```

---

## System Information

### `sys.platform` – Platform Identifier

```python
import sys

print(sys.platform)
# 'linux', 'win32', 'darwin' (macOS)

# Platform-specific code
if sys.platform == 'win32':
    print("Windows detected")
elif sys.platform == 'darwin':
    print("macOS detected")
elif sys.platform.startswith('linux'):
    print("Linux detected")
```

### `sys.maxsize` – Maximum Integer Size

```python
import sys

print(f"Max size: {sys.maxsize}")
print(f"Max size (hex): {hex(sys.maxsize)}")
```

### `sys.byteorder` – Byte Order

```python
import sys

print(f"Byte order: {sys.byteorder}")
# 'little' or 'big'
```

### `sys.getrecursionlimit()` – Recursion Limit

```python
import sys

print(f"Recursion limit: {sys.getrecursionlimit()}")

# Set new limit (use with caution)
sys.setrecursionlimit(10000)
print(f"New limit: {sys.getrecursionlimit()}")
```

### `sys.getsizeof()` – Object Size

```python
import sys

print(f"Empty list: {sys.getsizeof([])} bytes")
print(f"Empty dict: {sys.getsizeof({})} bytes")
print(f"Integer 0: {sys.getsizeof(0)} bytes")
print(f"String 'a': {sys.getsizeof('a')} bytes")
```

---

## Real-World Examples

### Example 1: Command Line Tool

```python
import sys
import argparse

def main():
    """Command line tool with argument parsing"""
    parser = argparse.ArgumentParser(
        description='File Processing Tool',
        epilog='Example: python tool.py --input data.txt --output result.txt'
    )
    
    parser.add_argument('-i', '--input', required=True, help='Input file')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Processing {args.input}")
    
    # Process file
    try:
        with open(args.input, 'r') as f:
            data = f.read()
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(data.upper())
            if args.verbose:
                print(f"Output written to {args.output}")
        else:
            print(data.upper())
    
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Example 2: Progress Bar

```python
import sys
import time

class ProgressBar:
    @staticmethod
    def show(percent, width=50, prefix='Progress', suffix='Complete'):
        """Display progress bar"""
        filled = int(width * percent / 100)
        bar = '█' * filled + '░' * (width - filled)
        
        # Format with color based on progress
        if percent < 30:
            color = '\033[91m'  # Red
        elif percent < 70:
            color = '\033[93m'  # Yellow
        else:
            color = '\033[92m'  # Green
        
        reset = '\033[0m'
        
        sys.stdout.write(f"\r{prefix}: |{color}{bar}{reset}| {percent:5.1f}% {suffix}")
        sys.stdout.flush()
    
    @staticmethod
    def animate(duration=5, steps=100):
        """Animate progress bar"""
        for i in range(steps + 1):
            percent = i / steps * 100
            ProgressBar.show(percent, prefix='Processing')
            time.sleep(duration / steps)
        print()  # New line after completion

# Usage
ProgressBar.show(45, width=30, prefix='Loading')
print()  # New line

# Animated example
# ProgressBar.animate(3)
```

### Example 3: Error Logger

```python
import sys
import traceback
from datetime import datetime

class ErrorLogger:
    def __init__(self, log_file='error.log'):
        self.log_file = log_file
    
    def log_exception(self):
        """Log current exception to file and stderr"""
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Format timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get traceback as string
        tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        tb_str = ''.join(tb_lines)
        
        # Log to file
        with open(self.log_file, 'a') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"[{timestamp}] ERROR\n")
            f.write(tb_str)
        
        # Print to stderr
        sys.stderr.write(f"\n{'='*60}\n")
        sys.stderr.write(f"[{timestamp}] ERROR: {exc_value}\n")
        sys.stderr.write(f"Details logged to {self.log_file}\n")
    
    def log_message(self, message, level='INFO'):
        """Log custom message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {level}: {message}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_line)
        
        if level in ['ERROR', 'CRITICAL']:
            sys.stderr.write(log_line)
        elif level == 'WARNING':
            sys.stdout.write(log_line)

# Usage
logger = ErrorLogger()

try:
    x = 1 / 0
except Exception:
    logger.log_exception()

logger.log_message("Application started", "INFO")
logger.log_message("Disk space low", "WARNING")
```

### Example 4: Interactive Shell

```python
import sys
import readline  # Optional, for better input handling

class InteractiveShell:
    def __init__(self, prompt='>>> '):
        self.prompt = prompt
        self.commands = {}
        self.running = True
    
    def register(self, name, func, help_text=''):
        """Register a command"""
        self.commands[name] = {'func': func, 'help': help_text}
    
    def run(self):
        """Run interactive shell"""
        print("Interactive Shell (type 'help' for commands, 'exit' to quit)")
        
        while self.running:
            try:
                # Get user input
                user_input = input(self.prompt).strip()
                
                if not user_input:
                    continue
                
                # Parse command and arguments
                parts = user_input.split()
                cmd = parts[0].lower()
                args = parts[1:]
                
                # Handle built-in commands
                if cmd == 'exit' or cmd == 'quit':
                    print("Goodbye!")
                    self.running = False
                
                elif cmd == 'help':
                    self.show_help()
                
                elif cmd in self.commands:
                    try:
                        self.commands[cmd]['func'](*args)
                    except Exception as e:
                        print(f"Error: {e}", file=sys.stderr)
                
                else:
                    print(f"Unknown command: {cmd}. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit")
            except EOFError:
                print("\nGoodbye!")
                self.running = False
    
    def show_help(self):
        """Show available commands"""
        print("\nAvailable commands:")
        print("  help          - Show this help")
        print("  exit/quit     - Exit the shell")
        
        for name, info in self.commands.items():
            help_text = f" - {info['help']}" if info['help'] else ''
            print(f"  {name}{help_text}")
        print()

# Example commands
def echo(*args):
    print(' '.join(args))

def add(*args):
    total = sum(int(arg) for arg in args)
    print(f"Sum: {total}")

# Usage
shell = InteractiveShell(prompt='cmd> ')
shell.register('echo', echo, 'Echo arguments')
shell.register('add', add, 'Add numbers (e.g., add 1 2 3)')
# shell.run()
```

### Example 5: Resource Monitor

```python
import sys
import time
import gc

class ResourceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.start_memory = self.get_memory_usage()
    
    def get_memory_usage(self):
        """Get current memory usage in MB"""
        import psutil  # Third-party, or use resource module on Unix
        try:
            process = psutil.Process()
            return process.memory_info().rss / 1024 / 1024
        except ImportError:
            # Fallback for Unix
            if sys.platform.startswith('linux'):
                import resource
                return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
            return 0
    
    def get_cpu_usage(self):
        """Get CPU usage percentage"""
        import psutil
        try:
            return psutil.cpu_percent(interval=0.1)
        except ImportError:
            return 0
    
    def report(self):
        """Generate resource usage report"""
        elapsed = time.time() - self.start_time
        current_memory = self.get_memory_usage()
        
        print("\nRESOURCE USAGE REPORT")
        print("=" * 40)
        print(f"Elapsed time: {elapsed:.2f} seconds")
        print(f"Initial memory: {self.start_memory:.2f} MB")
        print(f"Current memory: {current_memory:.2f} MB")
        print(f"Memory delta: {current_memory - self.start_memory:.2f} MB")
        
        # Garbage collector info
        gc.collect()
        print(f"Garbage collector objects: {len(gc.get_objects())}")
    
    def track(self, func, *args, **kwargs):
        """Track resource usage of a function"""
        monitor = ResourceMonitor()
        result = func(*args, **kwargs)
        monitor.report()
        return result

# Example
def memory_intensive_task():
    """Create many objects to test memory"""
    data = []
    for i in range(100000):
        data.append([i] * 10)
    return len(data)

# Usage
monitor = ResourceMonitor()
# result = monitor.track(memory_intensive_task)
```

### Example 6: Script Runner with Error Handling

```python
import sys
import traceback
import importlib

class ScriptRunner:
    @staticmethod
    def run_module(module_name, *args):
        """Run a Python module with arguments"""
        original_argv = sys.argv
        sys.argv = [module_name] + list(args)
        
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, 'main'):
                module.main()
            sys.exit(0)
        except Exception as e:
            print(f"Error running {module_name}: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)
        finally:
            sys.argv = original_argv
    
    @staticmethod
    def run_function(func, *args, **kwargs):
        """Run a function with error handling"""
        try:
            result = func(*args, **kwargs)
            return result
        except KeyboardInterrupt:
            print("\nInterrupted by user", file=sys.stderr)
            sys.exit(130)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)
    
    @staticmethod
    def run_with_timeout(func, timeout, *args, **kwargs):
        """Run function with timeout"""
        import signal
        
        def timeout_handler(signum, frame):
            raise TimeoutError(f"Function timed out after {timeout} seconds")
        
        # Set timeout handler (Unix only)
        if sys.platform.startswith('linux'):
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)
        
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            if sys.platform.startswith('linux'):
                signal.alarm(0)

# Example
def slow_function():
    import time
    time.sleep(5)
    return "Done"

# Usage
runner = ScriptRunner()
# result = runner.run_with_timeout(slow_function, 3)  # Will timeout
```

---

## Common Pitfalls

### Pitfall 1: Modifying `sys.path` After Imports

```python
# ❌ Bad - modifying after imports
import mymodule  # Already imported
sys.path.append('/new/path')
import mymodule  # Won't reload

# ✅ Good - modify before imports
sys.path.append('/new/path')
import mymodule
```

### Pitfall 2: Not Flushing stdout

```python
# ❌ May not show immediately
for i in range(10):
    sys.stdout.write(f"{i} ")
    time.sleep(0.1)
# Output may appear all at once

# ✅ Force flush
for i in range(10):
    sys.stdout.write(f"{i} ")
    sys.stdout.flush()
    time.sleep(0.1)
```

### Pitfall 3: Assuming `sys.argv` Always Has Arguments

```python
# ❌ IndexError if no arguments
filename = sys.argv[1]

# ✅ Check length
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: script.py <filename>")
    sys.exit(1)
```

---

## Practice Exercises

### Beginner Level

1. **Print Arguments**
   ```python
   # Print all command line arguments
   ```

2. **Check Python Version**
   ```python
   # Print Python version and exit if < 3.8
   ```

3. **Redirect Output**
   ```python
   # Redirect print statements to a file
   ```

### Intermediate Level

4. **Argument Parser**
   ```python
   # Simple argument parser for --help, --version
   ```

5. **Progress Bar**
   ```python
   # Display progress bar using sys.stdout
   ```

6. **Error Logger**
   ```python
   # Log errors to file and console
   ```

### Advanced Level

7. **Interactive Shell**
   ```python
   # Create custom REPL with commands
   ```

8. **Resource Monitor**
   ```python
   # Monitor memory and CPU usage
   ```

9. **Script Runner**
   ```python
   # Run scripts with timeout and error handling
   ```

---

## Quick Reference Card

```python
import sys

# Command line
sys.argv                    # Arguments list
sys.argv[0]                 # Script name
sys.argv[1:]                # Arguments

# Path
sys.path                    # Module search path
sys.prefix                  # Python installation prefix

# Streams
sys.stdin                   # Standard input
sys.stdout                  # Standard output
sys.stderr                  # Standard error

# Exit
sys.exit(code)              # Exit with code
sys.exit(message)           # Exit with message

# Version
sys.version                 # Version string
sys.version_info            # Version tuple
sys.hexversion              # Version as integer

# Platform
sys.platform                # Platform name
sys.byteorder               # Byte order
sys.maxsize                 # Max integer size

# Runtime
sys.getrecursionlimit()     # Recursion limit
sys.setrecursionlimit(n)    # Set recursion limit
sys.getsizeof(obj)          # Object size in bytes

# Hooks
sys.excepthook              # Exception hook
sys.displayhook             # Display hook
```

---

## Next Step

- Move to [07_json.md](07_json.md) to learn about JSON handling.

---

*Master the sys module for system-level programming and runtime control! 🐍✨*
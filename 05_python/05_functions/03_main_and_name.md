# 📘 MAIN AND NAME – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is `__name__`?](#what-is-__name__)
2. [What is `__main__`?](#what-is-__main__)
3. [The `if __name__ == "__main__"` Guard](#the-if-__name__-__main__-guard)
4. [Module vs Script](#module-vs-script)
5. [Practical Examples](#practical-examples)
6. [Common Patterns](#common-patterns)
7. [Real-World Examples](#real-world-examples)
8. [Common Pitfalls](#common-pitfalls)
9. [Practice Exercises](#practice-exercises)

---

## What is `__name__`?

Every Python module has a built-in variable called `__name__` that tells you how the module is being used.

```python
# my_module.py
print(f"__name__ = {__name__}")

# When run directly: __name__ = __main__
# When imported: __name__ = my_module
```

### `__name__` in Different Contexts

```python
# Create a file called test.py with this content:
print(f"This module's name is: {__name__}")

# Run directly:
# $ python test.py
# This module's name is: __main__

# Import as module:
# >>> import test
# This module's name is: test
```

### `__name__` for Built-in Modules

```python
import math
import json
import sys

print(f"math.__name__: {math.__name__}")    # math
print(f"json.__name__: {json.__name__}")    # json
print(f"sys.__name__: {sys.__name__}")      # sys
```

---

## What is `__main__`?

`__main__` is the name of the scope where top-level code executes.

### Top-Level Code Environment

```python
# script.py
print("This is top-level code")

def my_function():
    print("This is inside a function")

if __name__ == "__main__":
    print("This runs when script is executed directly")
    my_function()

# When run: python script.py
# This is top-level code
# This runs when script is executed directly
# This is inside a function

# When imported: import script
# This is top-level code
# (the if block does NOT run)
```

### The `__main__` Scope

```python
# When you run a script directly, Python sets __name__ = "__main__"
# This creates a special scope called __main__

import sys
print(f"Running in: {__name__}")
print(f"Main module: {sys.modules['__main__']}")
```

---

## The `if __name__ == "__main__"` Guard

This is the most common pattern for making Python files both importable and runnable.

### Basic Pattern

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# This only runs when the script is executed directly
if __name__ == "__main__":
    # Test code
    print("Testing calculator functions:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
```

### Without Guard (Problem)

```python
# bad_module.py
def helper():
    print("Helper function")

print("This runs on import!")  # Runs when imported
helper()                       # Runs when imported

# When you import this module, you get unexpected output
```

### With Guard (Solution)

```python
# good_module.py
def helper():
    print("Helper function")

if __name__ == "__main__":
    # This only runs when executed directly
    print("This runs only when script is run directly")
    helper()

# When imported: nothing runs automatically
# When run directly: prints and calls helper
```

---

## Module vs Script

### Differences Between Module and Script

| Aspect | Module (Imported) | Script (Run Directly) |
|--------|-------------------|----------------------|
| `__name__` | Module name (e.g., "mymodule") | `"__main__"` |
| Purpose | Provide functions/classes | Execute actions |
| Side effects | Should be minimal | Can have side effects |
| Test code | Inside `if __name__ == "__main__"` | Can be at top level |
| Reusability | High | Low |

### Example: Module Design

```python
# data_processor.py
"""
Module for processing data.
Can be imported or run as script.
"""

def load_data(filename):
    """Load data from file"""
    with open(filename, 'r') as f:
        return f.read()

def process_data(data):
    """Process the data"""
    return data.upper()

def save_data(filename, data):
    """Save data to file"""
    with open(filename, 'w') as f:
        f.write(data)

def main():
    """Main function when run as script"""
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python data_processor.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    data = load_data(input_file)
    processed = process_data(data)
    save_data(output_file, processed)
    print(f"Processed {input_file} -> {output_file}")

if __name__ == "__main__":
    main()
```

### Using as Module

```python
# other_script.py
import data_processor

# Use functions without running main()
data = data_processor.load_data("input.txt")
processed = data_processor.process_data(data)
print(processed)
```

---

## Practical Examples

### Example 1: Testing Module

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Run tests when script is executed directly
    print("Running tests...")
    
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(4, 3) == 12
    assert divide(10, 2) == 5
    
    print("All tests passed!")
    
    # Example usage
    print("\nExamples:")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
```

### Example 2: CLI Tool

```python
# file_tool.py
import sys
import os

def read_file(filename):
    """Read file contents"""
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    """Write content to file"""
    with open(filename, 'w') as f:
        f.write(content)

def count_lines(content):
    """Count lines in content"""
    return len(content.splitlines())

def count_words(content):
    """Count words in content"""
    return len(content.split())

def count_chars(content):
    """Count characters in content"""
    return len(content)

def show_help():
    """Display help message"""
    print("""
File Tool - Command Line Interface

Usage:
    python file_tool.py <filename> [options]

Options:
    --lines     Count number of lines
    --words     Count number of words
    --chars     Count number of characters
    --copy <dest>  Copy to destination file
    --help      Show this help message

Examples:
    python file_tool.py input.txt --lines
    python file_tool.py input.txt --copy output.txt
    """)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    
    content = read_file(filename)
    
    if len(sys.argv) == 2:
        # No options, just display file
        print(content)
    
    elif sys.argv[2] == "--lines":
        print(f"Lines: {count_lines(content)}")
    
    elif sys.argv[2] == "--words":
        print(f"Words: {count_words(content)}")
    
    elif sys.argv[2] == "--chars":
        print(f"Characters: {count_chars(content)}")
    
    elif sys.argv[2] == "--copy":
        if len(sys.argv) < 4:
            print("Error: Missing destination file")
            sys.exit(1)
        dest = sys.argv[3]
        write_file(dest, content)
        print(f"Copied to {dest}")
    
    elif sys.argv[2] == "--help":
        show_help()
    
    else:
        print(f"Unknown option: {sys.argv[2]}")
        show_help()

if __name__ == "__main__":
    main()
```

### Example 3: Module with Demo Mode

```python
# sorting_algorithms.py
"""
Sorting algorithms module.
Can be imported or run to demonstrate algorithms.
"""

def bubble_sort(arr):
    """Bubble sort algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Selection sort algorithm"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion sort algorithm"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    """Quick sort algorithm"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """Merge sort algorithm"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def demo_sorting():
    """Demonstrate all sorting algorithms"""
    import random
    import time
    
    original = [random.randint(1, 100) for _ in range(10)]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort)
    ]
    
    print(f"Original: {original}\n")
    
    for name, algorithm in algorithms:
        arr = original.copy()
        start = time.time()
        sorted_arr = algorithm(arr)
        elapsed = time.time() - start
        print(f"{name:15} {sorted_arr} ({elapsed:.6f}s)")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_sorting()
    else:
        print("Sorting Algorithms Module")
        print("Available functions:")
        print("  bubble_sort(arr) - Bubble sort")
        print("  selection_sort(arr) - Selection sort")
        print("  insertion_sort(arr) - Insertion sort")
        print("  quick_sort(arr) - Quick sort")
        print("  merge_sort(arr) - Merge sort")
        print("\nRun with --demo to see demonstration")
```

---

## Common Patterns

### Pattern 1: Simple Guard

```python
# simplest.py
def main():
    print("Program starts here")

if __name__ == "__main__":
    main()
```

### Pattern 2: Argument Parsing

```python
# with_args.py
import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("No arguments provided")
    else:
        print(f"Arguments: {args}")

if __name__ == "__main__":
    main()
```

### Pattern 3: Multiple Entry Points

```python
# multiple_entry.py
def run_server():
    print("Starting server...")

def run_client():
    print("Starting client...")

def run_tests():
    print("Running tests...")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script.py [server|client|test]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "server":
        run_server()
    elif command == "client":
        run_client()
    elif command == "test":
        run_tests()
    else:
        print(f"Unknown command: {command}")
```

### Pattern 4: Module with Configuration

```python
# configurable.py
DEBUG = False

def log(message):
    if DEBUG:
        print(f"[DEBUG] {message}")

def process(data):
    log(f"Processing {data}")
    return data.upper()

if __name__ == "__main__":
    import sys
    
    if "--debug" in sys.argv:
        DEBUG = True
    
    result = process("hello")
    print(result)
```

### Pattern 5: Self-Testing Module

```python
# self_testing.py
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

def run_tests():
    calc = Calculator()
    
    tests = [
        (calc.add, (2, 3), 5),
        (calc.add, (-1, 1), 0),
        (calc.subtract, (5, 3), 2),
        (calc.subtract, (10, 20), -10),
    ]
    
    passed = 0
    for func, args, expected in tests:
        result = func(*args)
        if result == expected:
            passed += 1
            print(f"✓ {func.__name__}{args} = {result}")
        else:
            print(f"✗ {func.__name__}{args} = {result} (expected {expected})")
    
    print(f"\nPassed {passed}/{len(tests)} tests")
    return passed == len(tests)

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
```

---

## Real-World Examples

### Example 1: Data Analysis Script

```python
# data_analyzer.py
"""
Data Analysis Tool - Analyze CSV files
Usage: python data_analyzer.py data.csv --column age --operation mean
"""

import sys
import csv
from typing import List, Dict, Any

def load_csv(filename: str) -> List[Dict]:
    """Load CSV file into list of dictionaries"""
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def get_column(data: List[Dict], column: str) -> List[Any]:
    """Extract column from data"""
    return [row[column] for row in data if column in row]

def calculate_mean(values: List[float]) -> float:
    """Calculate mean of values"""
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_median(values: List[float]) -> float:
    """Calculate median of values"""
    if not values:
        return 0.0
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]

def calculate_sum(values: List[float]) -> float:
    """Calculate sum of values"""
    return sum(values)

def calculate_min(values: List[float]) -> float:
    """Calculate minimum of values"""
    return min(values) if values else 0.0

def calculate_max(values: List[float]) -> float:
    """Calculate maximum of values"""
    return max(values) if values else 0.0

OPERATIONS = {
    'mean': calculate_mean,
    'median': calculate_median,
    'sum': calculate_sum,
    'min': calculate_min,
    'max': calculate_max,
}

def show_help():
    """Display help message"""
    print("""
Data Analyzer Tool

Usage:
    python data_analyzer.py <filename> --column <col> --operation <op>

Operations:
    mean    - Calculate average
    median  - Calculate median
    sum     - Calculate sum
    min     - Find minimum
    max     - Find maximum

Example:
    python data_analyzer.py sales.csv --column revenue --operation mean
    """)

def main():
    """Main entry point"""
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        show_help()
        sys.exit(0)
    
    filename = sys.argv[1]
    
    # Parse arguments
    column = None
    operation = None
    
    for i, arg in enumerate(sys.argv):
        if arg == "--column" and i + 1 < len(sys.argv):
            column = sys.argv[i + 1]
        elif arg == "--operation" and i + 1 < len(sys.argv):
            operation = sys.argv[i + 1]
    
    if not column or not operation:
        print("Error: Missing --column or --operation")
        show_help()
        sys.exit(1)
    
    if operation not in OPERATIONS:
        print(f"Error: Unknown operation '{operation}'")
        print(f"Available: {', '.join(OPERATIONS.keys())}")
        sys.exit(1)
    
    try:
        # Load data
        data = load_csv(filename)
        
        # Extract column
        values = get_column(data, column)
        
        # Convert to numbers
        numeric_values = []
        for v in values:
            try:
                numeric_values.append(float(v))
            except ValueError:
                pass
        
        if not numeric_values:
            print(f"Error: No numeric values in column '{column}'")
            sys.exit(1)
        
        # Calculate result
        result = OPERATIONS[operation](numeric_values)
        
        print(f"\nFile: {filename}")
        print(f"Column: {column}")
        print(f"Operation: {operation}")
        print(f"Result: {result}")
        print(f"Values processed: {len(numeric_values)}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Example 2: Web Server Stub

```python
# simple_server.py
"""
Simple HTTP Server - Can be run directly or imported
"""

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello, World!</h1>")
    
    def log_message(self, format, *args):
        if DEBUG:
            super().log_message(format, *args)

DEBUG = False

def run_server(port=8080, debug=False):
    """Run the HTTP server"""
    global DEBUG
    DEBUG = debug
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    
    print(f"Server running on port {port}")
    print(f"Debug mode: {DEBUG}")
    print("Press Ctrl+C to stop")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.server_close()

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Simple HTTP Server')
    parser.add_argument('-p', '--port', type=int, default=8080,
                        help='Port to run server on (default: 8080)')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Enable debug mode')
    
    args = parser.parse_args()
    run_server(port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()
```

### Example 3: Package Initialization

```python
# mypackage/__init__.py
"""
MyPackage - A collection of utilities
"""

__version__ = "1.0.0"
__author__ = "Python Developer"

from .module1 import func1
from .module2 import func2

def main():
    """Run package as main"""
    print(f"MyPackage v{__version__}")
    print("Available functions:")
    print("  func1() - Does something")
    print("  func2() - Does something else")

if __name__ == "__main__":
    main()
```

---

## Common Pitfalls

### Pitfall 1: Forgetting the Guard

```python
# bad.py
def helper():
    print("Helper")

print("Module loaded")  # Runs on import!

# When imported, this prints unexpectedly
```

### Pitfall 2: Putting Import Code in Guard

```python
# bad.py
if __name__ == "__main__":
    import sys  # Imports only when run directly
    # If imported, sys is not available!

def main():
    print(sys.argv)  # NameError if imported!

if __name__ == "__main__":
    main()

# Fix: Put imports at top
import sys  # Always available

def main():
    print(sys.argv)

if __name__ == "__main__":
    main()
```

### Pitfall 3: Testing Inside Guard

```python
# bad.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # Tests only run when script is executed
    assert add(2, 3) == 5

# When imported, tests don't run
# But you might want to run tests separately

# Better: Separate test file or use pytest
```

---

## Practice Exercises

### Beginner Level

1. **Simple Guard**
   ```python
   # Create module that prints "Hello" when run directly
   # But nothing when imported
   ```

2. **Module Info**
   ```python
   # Create module that prints its __name__
   # Try running directly and importing
   ```

3. **Math Module**
   ```python
   # Create math_utils module with add, subtract
   # Add test code under guard
   ```

### Intermediate Level

4. **CLI Calculator**
   ```python
   # Create calculator that takes command line arguments
   # Example: python calc.py 5 + 3
   ```

5. **File Processor**
   ```python
   # Create module that can be imported or run
   # When run, process command line arguments
   ```

6. **Self-Testing Module**
   ```python
   # Create module with unit tests under guard
   # Run tests when script executed
   ```

### Advanced Level

7. **Multi-Command Tool**
   ```python
   # Create CLI tool with multiple subcommands
   # Example: python tool.py encrypt file.txt
   ```

8. **Plugin System**
   ```python
   # Create module that discovers plugins
   # Use __name__ for module identification
   ```

9. **Configuration Loader**
   ```python
   # Create config module that works as both
   # Can be imported or run to generate config
   ```

---

## Quick Reference Card

```python
# Check if running directly
if __name__ == "__main__":
    # Code here runs only when script is executed
    pass

# Standard pattern
def main():
    """Main function"""
    pass

if __name__ == "__main__":
    main()

# With arguments
import sys

def main():
    args = sys.argv[1:]
    # process args

if __name__ == "__main__":
    main()

# Module metadata
print(__name__)      # Current module name
print(__file__)      # Current file path

# Get main module
import sys
main_module = sys.modules['__main__']
```

## Next Step

- Go to [04_functional_tools.md](04_functional_tools.md) for understanding the Toolkits that can be used in functions to make our work better.

---

*Master `__main__` and `__name__` to create modules that are both importable and executable! 🐍✨*

---
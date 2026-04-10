# 🎨 STRING FORMATTING – COMPLETE GUIDE

## 📌 Table of Contents
1. [Introduction to String Formatting](#introduction-to-string-formatting)
2. [f-strings (Python 3.6+)](#f-strings-python-36)
3. [format() Method](#format-method)
4. [% Formatting (Old Style)](#-formatting-old-style)
5. [Template Strings](#template-strings)
6. [Format Specification Mini-Language](#format-specification-mini-language)
7. [Real-World Examples](#real-world-examples)
8. [Performance Comparison](#performance-comparison)
9. [Best Practices](#best-practices)

---

## 📖 Introduction to String Formatting

Python offers **four ways** to format strings:

| Method | Syntax | Version | When to Use |
|--------|--------|---------|-------------|
| **f-strings** | `f"Hello {name}"` | 3.6+ | **RECOMMENDED** for most cases |
| **format()** | `"Hello {}".format(name)` | 2.6+ | When f-strings not available |
| **% formatting** | `"Hello %s" % name` | 1.x+ | Legacy code only |
| **Template** | `Template("Hello $name")` | 2.4+ | User-supplied format strings |

---

## ⚡ f-strings (Python 3.6+)

### Basic Usage

```python
name = "Alice"
age = 30
city = "New York"

# Simple variable insertion
print(f"Name: {name}")           # "Name: Alice"
print(f"Age: {age}")             # "Age: 30"
print(f"{name} is {age} years old")  # "Alice is 30 years old"

# Multiple variables
print(f"Name: {name}, Age: {age}, City: {city}")
# "Name: Alice, Age: 30, City: New York"
```

### Expressions Inside f-strings

```python
# Arithmetic operations
print(f"5 + 3 = {5 + 3}")                    # "5 + 3 = 8"
print(f"10 * 2 = {10 * 2}")                  # "10 * 2 = 20"
print(f"Square of 5: {5 ** 2}")              # "Square of 5: 25"

# Method calls
text = "hello"
print(f"Uppercase: {text.upper()}")          # "Uppercase: HELLO"
print(f"Length: {len(text)}")                # "Length: 5"

# Function calls
def double(x):
    return x * 2

print(f"Double of 5: {double(5)}")           # "Double of 5: 10"

# Conditional expressions
age = 18
print(f"{'Adult' if age >= 18 else 'Minor'}")  # "Adult"

# List comprehensions
numbers = [1, 2, 3, 4, 5]
print(f"Squares: {[x**2 for x in numbers]}")  # "Squares: [1, 4, 9, 16, 25]"

# Dictionary access
person = {'name': 'Alice', 'age': 30}
print(f"Name: {person['name']}, Age: {person['age']}")  # "Name: Alice, Age: 30"

# Attribute access
class Person:
    name = "Alice"
    age = 30

print(f"Name: {Person.name}")  # "Name: Alice"
```

### Format Specifiers with f-strings

```python
# Numbers
pi = 3.14159265359

# Decimal places
print(f"Pi: {pi:.2f}")      # "Pi: 3.14"
print(f"Pi: {pi:.4f}")      # "Pi: 3.1416"
print(f"Pi: {pi:.0f}")      # "Pi: 3"

# Percentage
score = 0.856
print(f"Score: {score:.1%}")   # "Score: 85.6%"
print(f"Score: {score:.2%}")   # "Score: 85.60%"

# Thousands separator
large_num = 1000000
print(f"Large: {large_num:,}")      # "Large: 1,000,000"
print(f"Large: {large_num:_}")      # "Large: 1_000_000"

# Width and alignment
name = "Alice"
print(f"{name:>10}")   # "     Alice" (right align, width 10)
print(f"{name:<10}")   # "Alice     " (left align)
print(f"{name:^10}")   # "  Alice   " (center)

# Fill characters
print(f"{name:*^10}")  # "**Alice***"
print(f"{name:-<10}")  # "Alice-----"
print(f"{name:_>10}")  # "_____Alice"

# Combining formats
price = 19.99
print(f"Price: ${price:>8.2f}")  # "Price: $   19.99"
print(f"Price: ${price:0>8.2f}") # "Price: $0019.99"

# Binary, octal, hexadecimal
num = 42
print(f"Binary: {num:b}")     # "Binary: 101010"
print(f"Octal: {num:o}")      # "Octal: 52"
print(f"Hex: {num:x}")        # "Hex: 2a"
print(f"Hex upper: {num:X}")  # "Hex upper: 2A"

# Number systems with prefix
print(f"Binary: {num:#b}")    # "Binary: 0b101010"
print(f"Octal: {num:#o}")     # "Octal: 0o52"
print(f"Hex: {num:#x}")       # "Hex: 0x2a"

# Scientific notation
sci_num = 1234567.89
print(f"Scientific: {sci_num:e}")   # "Scientific: 1.234568e+06"
print(f"Scientific: {sci_num:.2e}") # "Scientific: 1.23e+06"
```

### Debugging with f-strings (Python 3.8+)

```python
# Self-documenting expressions
x = 42
y = 10

print(f"{x=}")        # "x=42"
print(f"{x=:.2f}")    # "x=42.00"
print(f"{x+y=}")      # "x+y=52"

# Multiple variables
print(f"{x=}, {y=}")  # "x=42, y=10"

# With expressions
print(f"{x**2=}")     # "x**2=1764"
```

### Multiline f-strings

```python
name = "Alice"
age = 30
city = "New York"

# Using triple quotes
message = f"""
Name: {name}
Age: {age}
City: {city}
"""
print(message)
# Output:
# Name: Alice
# Age: 30
# City: New York

# Using parentheses for implicit concatenation
message = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"City: {city}"
)
print(message)
```

### Nested f-strings

```python
# Nesting is possible but rarely needed
width = 10
value = 42

# Outer f-string for width, inner for value
print(f"{value:>{width}}")  # "        42"

# Dynamic width
precision = 3
pi = 3.14159
print(f"{pi:.{precision}f}")  # "3.142"
```

### Raw f-strings

```python
# Combine raw string with f-string
path = r"C:\Users\{name}\Documents"
name = "Alice"
print(f"{path}")  # "C:\Users\{name}\Documents" (not interpolated)

# Need to use regular f-string for interpolation
print(f"C:\\Users\\{name}\\Documents")  # "C:\Users\Alice\Documents"
```

---

## 🔧 format() Method

### Basic Usage

```python
# Positional arguments
print("{} is {} years old".format("Alice", 30))
# "Alice is 30 years old"

# Indexed arguments (reusable)
print("{0} is {1} years old. {0} lives in NYC".format("Alice", 30))
# "Alice is 30 years old. Alice lives in NYC"

# Named arguments
print("{name} is {age} years old".format(name="Alice", age=30))
# "Alice is 30 years old"

# Mixed positional and named
print("{0} is {age} years old".format("Alice", age=30))
# "Alice is 30 years old"
```

### Format Specifiers with format()

```python
# Numbers
pi = 3.14159
print("{:.2f}".format(pi))     # "3.14"
print("{:.4f}".format(pi))     # "3.1416"

# Percentage
score = 0.856
print("{:.1%}".format(score))  # "85.6%"

# Thousands separator
print("{:,}".format(1000000))   # "1,000,000"
print("{:_}".format(1000000))   # "1_000_000"

# Alignment
name = "Alice"
print("{:>10}".format(name))    # "     Alice"
print("{:<10}".format(name))    # "Alice     "
print("{:^10}".format(name))    # "  Alice   "

# Fill characters
print("{:*^10}".format(name))   # "**Alice***"
print("{:-<10}".format(name))   # "Alice-----"

# Different bases
num = 42
print("{:b}".format(num))   # "101010" (binary)
print("{:o}".format(num))   # "52" (octal)
print("{:x}".format(num))   # "2a" (hex)
print("{:#b}".format(num))  # "0b101010" (with prefix)
```

### Advanced format() Features

```python
# Using dictionary
data = {'name': 'Alice', 'age': 30}
print("{name} is {age} years old".format(**data))

# Using list
data = ['Alice', 30]
print("{0[0]} is {0[1]} years old".format(data))

# Dynamic format specifiers
width = 10
value = 42
print("{0:>{1}}".format(value, width))  # "        42"

# Formatting datetime
from datetime import datetime
now = datetime.now()
print("{:%Y-%m-%d %H:%M:%S}".format(now))  # "2024-01-15 10:30:00"

# Formatting with conditions
value = 42
print("{:b} ({:#x})".format(value, value))  # "101010 (0x2a)"
```

---

## 📟 % Formatting (Old Style)

### Basic Usage

```python
# %s - string
print("%s is %d years old" % ("Alice", 30))
# "Alice is 30 years old"

# %d - integer
print("Integer: %d" % 42)        # "Integer: 42"
print("Integer: %5d" % 42)       # "Integer:    42" (width 5)

# %f - float
print("Float: %f" % 3.14159)     # "Float: 3.141590"
print("Float: %.2f" % 3.14159)   # "Float: 3.14"
print("Float: %8.2f" % 3.14)     # "Float:     3.14"

# %x - hexadecimal
print("Hex: %x" % 255)            # "Hex: ff"
print("Hex: %X" % 255)            # "Hex: FF"

# %o - octal
print("Octal: %o" % 42)           # "Octal: 52"

# %e - scientific
print("Scientific: %e" % 12345)   # "Scientific: 1.234500e+04"

# %% - literal percent sign
print("Discount: 50%%")            # "Discount: 50%"
```

### Multiple Values

```python
# Using tuple
print("Name: %s, Age: %d" % ("Alice", 30))

# Using dictionary
data = {'name': 'Alice', 'age': 30}
print("Name: %(name)s, Age: %(age)d" % data)

# Width and alignment
name = "Alice"
print("%10s" % name)   # "     Alice"
print("%-10s" % name)  # "Alice     "
```

### Format Specifiers for %

```python
# Flags
print("%+d" % 42)      # "+42"
print("%+d" % -42)     # "-42"
print("% d" % 42)      # " 42" (space for positive)
print("%0d" % 42)      # "42" (zero padding)
print("%05d" % 42)     # "00042"

# Combining flags
print("%+05d" % 42)    # "+0042"

# Width and precision
print("%10.2f" % 3.14159)  # "      3.14"
print("%-10.2f" % 3.14159) # "3.14      "
```

---

## 📋 Template Strings

### Basic Usage

```python
from string import Template

# Simple substitution
t = Template("Hello $name")
print(t.substitute(name="Alice"))  # "Hello Alice"

# Multiple substitutions
t = Template("$name is $age years old")
print(t.substitute(name="Alice", age=30))
# "Alice is 30 years old"

# Using dictionary
data = {'name': 'Alice', 'age': 30}
print(t.substitute(data))
# "Alice is 30 years old"

# Braces for adjacent characters
t = Template("${name}s age is $age")
print(t.substitute(name="Alice", age=30))
# "Alices age is 30" (note: no space after name)
```

### safe_substitute() vs substitute()

```python
from string import Template

t = Template("Hello $name")

# substitute() raises KeyError for missing keys
try:
    print(t.substitute())  # KeyError!
except KeyError:
    print("Missing key!")

# safe_substitute() leaves placeholders unchanged
print(t.safe_substitute())  # "Hello $name"

# Works with missing keys
print(t.safe_substitute(age=30))  # "Hello $name"
```

### Custom Delimiters

```python
from string import Template

class MyTemplate(Template):
    delimiter = '{{'
    pattern = r'\{\{(?P<named>[a-zA-Z0-9_]+)\}\}'

t = MyTemplate("Hello {{name}}")
print(t.substitute(name="Alice"))  # "Hello Alice"

# Or simply use different syntax
t = Template("Hello $name")
print(t.substitute(name="Alice"))  # "Hello Alice"
```

---

## 📐 Format Specification Mini-Language

### Syntax

```
format_spec ::= [[fill]align][sign][#][0][width][grouping_option][.precision][type]
```

### Alignment

| Option | Meaning |
|--------|---------|
| `<` | Left align (default for strings) |
| `>` | Right align (default for numbers) |
| `^` | Center align |
| `=` | Padding after sign (for numbers) |

```python
# Left align
print(f"{'left':<10}")     # "left      "

# Right align
print(f"{'right':>10}")    # "     right"

# Center
print(f"{'center':^10}")   # "  center   "

# With fill character
print(f"{'center':*^10}")  # "**center***"
```

### Sign Options

| Option | Meaning |
|--------|---------|
| `+` | Show sign for both positive and negative |
| `-` | Show sign only for negative (default) |
| ` ` | Space for positive, minus for negative |

```python
print(f"{42:+}")   # "+42"
print(f"{-42:+}")  # "-42"
print(f"{42: }")   # " 42"
print(f"{-42: }")  # "-42"
```

### Number Formatting

```python
# Thousands separator
print(f"{1000000:,}")   # "1,000,000"
print(f"{1000000:_}")   # "1_000_000"

# Percentage
print(f"{0.856:.1%}")   # "85.6%"

# Scientific notation
print(f"{12345.67:e}")  # "1.234567e+04"
print(f"{12345.67:.2e}") # "1.23e+04"
```

### Type Codes

| Type | Meaning |
|------|---------|
| `s` | String |
| `d` | Decimal integer |
| `b` | Binary |
| `o` | Octal |
| `x` / `X` | Hexadecimal |
| `f` / `F` | Fixed-point |
| `e` / `E` | Scientific notation |
| `g` / `G` | General (f or e) |
| `%` | Percentage |

```python
# Different types
num = 42
print(f"{num:d}")   # "42" (decimal)
print(f"{num:b}")   # "101010" (binary)
print(f"{num:o}")   # "52" (octal)
print(f"{num:x}")   # "2a" (hex)
print(f"{num:X}")   # "2A" (hex uppercase)

# Float types
pi = 3.14159
print(f"{pi:f}")    # "3.141590"
print(f"{pi:e}")    # "3.141590e+00"
print(f"{pi:g}")    # "3.14159" (chooses f or e)

# String
text = "Hello"
print(f"{text:s}")  # "Hello"
```

---

## 🌍 Real-World Examples

### Example 1: Invoice Generator

```python
class Invoice:
    def __init__(self, invoice_number, customer_name, date):
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.date = date
        self.items = []
    
    def add_item(self, description, quantity, unit_price):
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'total': quantity * unit_price
        })
    
    def generate(self):
        # Header
        invoice = f"""
{'=' * 60}
INVOICE #{self.invoice_number:06d}
{'=' * 60}
Customer: {self.customer_name}
Date: {self.date}
{'-' * 60}

{'Description':<30} {'Qty':>5} {'Unit Price':>10} {'Total':>10}
{'-' * 60}"""

        # Items
        subtotal = 0
        for item in self.items:
            invoice += f"\n{item['description']:<30} {item['quantity']:>5} ${item['unit_price']:>9.2f} ${item['total']:>9.2f}"
            subtotal += item['total']
        
        # Tax and total
        tax_rate = 0.08
        tax = subtotal * tax_rate
        total = subtotal + tax
        
        invoice += f"""
{'-' * 60}
{'Subtotal:':>45} ${subtotal:>9.2f}
{'Tax (8%):':>45} ${tax:>9.2f}
{'=' * 60}
{'TOTAL:':>45} ${total:>9.2f}
{'=' * 60}

Thank you for your business!
"""
        return invoice

# Create invoice
inv = Invoice(1234, "Alice Johnson", "2024-01-15")
inv.add_item("Laptop", 1, 999.99)
inv.add_item("Mouse", 2, 25.50)
inv.add_item("Keyboard", 1, 75.00)

print(inv.generate())
```

**Output:**
```
============================================================
INVOICE #001234
============================================================
Customer: Alice Johnson
Date: 2024-01-15
------------------------------------------------------------

Description                      Qty  Unit Price      Total
------------------------------------------------------------
Laptop                             1     $999.99    $999.99
Mouse                              2      $25.50     $51.00
Keyboard                           1      $75.00     $75.00
------------------------------------------------------------
                                      Subtotal: $1125.99
                                       Tax (8%):   $90.08
============================================================
                                         TOTAL: $1216.07
============================================================

Thank you for your business!
```

### Example 2: Log Formatter

```python
from datetime import datetime

class LogFormatter:
    LEVELS = {
        'DEBUG': '🔍',
        'INFO': 'ℹ️',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '💀'
    }
    
    @staticmethod
    def format(level, message, module=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        icon = LogFormatter.LEVELS.get(level, '📝')
        
        # Different formats based on level
        if level == 'ERROR' or level == 'CRITICAL':
            # Highlighted format for errors
            log = f"""
{icon} [{timestamp}] {level}
{'=' * 60}
Module: {module or 'N/A'}
Message: {message}
{'=' * 60}
"""
        elif level == 'WARNING':
            # Warning format
            log = f"{icon} [{timestamp}] {level:8} | {module:15} | {message}"
        else:
            # Standard format
            log = f"{icon} [{timestamp}] {level:8} | {message}"
        
        return log.strip()
    
    @staticmethod
    def create_table(data, headers):
        """Create formatted table from data"""
        # Calculate column widths
        col_widths = []
        for i, header in enumerate(headers):
            max_width = len(header)
            for row in data:
                max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)  # Add padding
        
        # Create header
        table = ""
        header_row = "|"
        separator = "+"
        for i, header in enumerate(headers):
            header_row += f" {header:<{col_widths[i]-1}}|"
            separator += "-" * col_widths[i] + "+"
        
        table += separator + "\n"
        table += header_row + "\n"
        table += separator + "\n"
        
        # Add data rows
        for row in data:
            data_row = "|"
            for i, cell in enumerate(row):
                data_row += f" {str(cell):<{col_widths[i]-1}}|"
            table += data_row + "\n"
        
        table += separator
        
        return table

# Usage
logger = LogFormatter()

print(logger.format("INFO", "Application started"))
print("\n")
print(logger.format("WARNING", "Low disk space", "storage.py"))
print("\n")
print(logger.format("ERROR", "Database connection failed", "db.py"))

# Create table
print("\n" + "=" * 60)
print("USER TABLE")
print("=" * 60)

data = [
    ["Alice", 30, "alice@example.com"],
    ["Bob", 25, "bob@example.com"],
    ["Charlie", 35, "charlie@example.com"]
]
headers = ["Name", "Age", "Email"]

print(logger.create_table(data, headers))
```

### Example 3: Progress Bar

```python
import time

class ProgressBar:
    @staticmethod
    def show(percent, width=50, prefix='Progress', suffix='Complete'):
        """Display a progress bar"""
        filled = int(width * percent / 100)
        bar = '█' * filled + '░' * (width - filled)
        
        # Format with colors (ANSI codes)
        GREEN = '\033[92m'
        RESET = '\033[0m'
        
        # Choose color based on progress
        if percent < 30:
            color = '\033[91m'  # Red
        elif percent < 70:
            color = '\033[93m'  # Yellow
        else:
            color = GREEN
        
        # Create progress bar string
        progress_str = f"\r{prefix}: |{bar}| {percent:5.1f}% {suffix}"
        
        # Add color for first part
        colored = f"{color}{progress_str}{RESET}"
        print(colored, end='', flush=True)
    
    @staticmethod
    def animate(duration=5):
        """Animate progress bar"""
        for i in range(101):
            ProgressBar.show(i, width=40, prefix='Downloading')
            time.sleep(duration / 100)
        print()  # New line after completion

# Simple progress
ProgressBar.show(45, width=30, prefix='Loading', suffix='Please wait')
print()

# Animated progress
# ProgressBar.animate(3)  # Uncomment to see animation

# Dynamic progress with different styles
tasks = [
    ("Downloading file", 30),
    ("Processing data", 50),
    ("Saving results", 70),
    ("Cleaning up", 90)
]

for task, start_percent in tasks:
    for i in range(start_percent, min(start_percent + 30, 101)):
        ProgressBar.show(i, width=40, prefix=task, suffix=f'{i}%')
        time.sleep(0.05)
    print()
```

### Example 4: Report Generator

```python
class ReportGenerator:
    @staticmethod
    def generate_sales_report(sales_data):
        """Generate formatted sales report"""
        # Calculate totals
        total_revenue = sum(item['revenue'] for item in sales_data)
        total_units = sum(item['units'] for item in sales_data)
        avg_price = total_revenue / total_units if total_units > 0 else 0
        
        # Header with dynamic width
        title = "SALES REPORT"
        width = 80
        print("=" * width)
        print(f"{title:^{width}}")
        print("=" * width)
        
        # Summary section
        print(f"\n{'SUMMARY':^{width}}")
        print("-" * width)
        print(f"Total Revenue:    ${total_revenue:>15,.2f}")
        print(f"Total Units:      {total_units:>15,}")
        print(f"Average Price:    ${avg_price:>15,.2f}")
        
        # Detailed table
        print(f"\n{'DETAILED BREAKDOWN':^{width}}")
        print("-" * width)
        
        # Table headers with dynamic alignment
        headers = ["Product", "Units Sold", "Unit Price", "Revenue"]
        col_widths = [25, 12, 12, 15]
        
        # Print header
        header_line = ""
        for i, header in enumerate(headers):
            header_line += f"{header:<{col_widths[i]}}"
        print(header_line)
        print("-" * width)
        
        # Print data rows
        for item in sales_data:
            row = (
                f"{item['product']:<{col_widths[0]}}"
                f"{item['units']:>{col_widths[1]},}"
                f"${item['price']:>{col_widths[2]-1},.2f}"
                f"${item['revenue']:>{col_widths[3]-1},.2f}"
            )
            print(row)
        
        print("=" * width)
        
        # Performance indicators
        print(f"\n{'PERFORMANCE INDICATORS':^{width}}")
        print("-" * width)
        
        best_product = max(sales_data, key=lambda x: x['revenue'])
        worst_product = min(sales_data, key=lambda x: x['revenue'])
        
        print(f"Best Performing:  {best_product['product']:<20} ${best_product['revenue']:>10,.2f}")
        print(f"Worst Performing: {worst_product['product']:<20} ${worst_product['revenue']:>10,.2f}")
        
        # Top products by units
        top_products = sorted(sales_data, key=lambda x: x['units'], reverse=True)[:3]
        print(f"\n{'TOP 3 PRODUCTS BY UNITS':^{width}}")
        print("-" * width)
        for i, product in enumerate(top_products, 1):
            print(f"{i}. {product['product']:<25} {product['units']:>8,} units")
        
        print("=" * width)

# Sample data
sales_data = [
    {'product': 'Laptop Pro', 'units': 45, 'price': 1299.99, 'revenue': 58499.55},
    {'product': 'Wireless Mouse', 'units': 234, 'price': 29.99, 'revenue': 7017.66},
    {'product': 'Mechanical Keyboard', 'units': 89, 'price': 89.99, 'revenue': 8009.11},
    {'product': 'USB-C Hub', 'units': 156, 'price': 49.99, 'revenue': 7798.44},
    {'product': 'Monitor 27"', 'units': 34, 'price': 349.99, 'revenue': 11899.66}
]

ReportGenerator.generate_sales_report(sales_data)
```

### Example 5: Data Table Formatter

```python
class TableFormatter:
    @staticmethod
    def format_table(data, headers=None, alignment='left', border_style='simple'):
        """
        Format data as a table
        
        alignment: 'left', 'right', 'center'
        border_style: 'simple', 'grid', 'markdown', 'none'
        """
        if not data:
            return ""
        
        # Use headers from first row if not provided
        if headers is None:
            headers = [f"Col{i+1}" for i in range(len(data[0]))]
        
        # Calculate column widths
        col_widths = []
        for i in range(len(headers)):
            max_width = len(str(headers[i]))
            for row in data:
                max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)  # Add padding
        
        # Create border characters based on style
        if border_style == 'simple':
            h_line = '─'
            v_line = ' '
            t_l = ' '
            t_r = ' '
            b_l = ' '
            b_r = ' '
            cross = ' '
        elif border_style == 'grid':
            h_line = '─'
            v_line = '│'
            t_l = '┌'
            t_r = '┐'
            b_l = '└'
            b_r = '┘'
            cross = '┼'
        elif border_style == 'markdown':
            h_line = '-'
            v_line = '|'
            t_l = '|'
            t_r = '|'
            b_l = '|'
            b_r = '|'
            cross = '|'
        else:  # none
            h_line = ' '
            v_line = ' '
            t_l = ' '
            t_r = ' '
            b_l = ' '
            b_r = ' '
            cross = ' '
        
        # Helper function to align text
        def align_text(text, width, align):
            text = str(text)
            if align == 'left':
                return text.ljust(width)
            elif align == 'right':
                return text.rjust(width)
            else:  # center
                return text.center(width)
        
        # Build table
        table = []
        
        # Top border
        if border_style == 'grid':
            top = t_l + h_line.join([h_line * w for w in col_widths]) + t_r
            table.append(top)
        
        # Header row
        header_row = v_line
        for i, header in enumerate(headers):
            header_row += align_text(header, col_widths[i], 'center') + v_line
        table.append(header_row)
        
        # Separator after header
        if border_style in ['grid', 'markdown']:
            sep = cross if border_style == 'grid' else v_line
            separator = sep + h_line.join([h_line * w for w in col_widths]) + sep
            table.append(separator)
        elif border_style == 'simple':
            table.append('')
        
        # Data rows
        for row in data:
            data_row = v_line
            for i, cell in enumerate(row):
                data_row += align_text(cell, col_widths[i], alignment) + v_line
            table.append(data_row)
        
        # Bottom border
        if border_style == 'grid':
            bottom = b_l + h_line.join([h_line * w for w in col_widths]) + b_r
            table.append(bottom)
        
        return '\n'.join(table)

# Test data
data = [
    ["Alice Johnson", 30, "Engineer", "New York"],
    ["Bob Smith", 25, "Designer", "Los Angeles"],
    ["Charlie Brown", 35, "Manager", "Chicago"],
    ["Diana Prince", 28, "Developer", "San Francisco"]
]

headers = ["Name", "Age", "Position", "Location"]

print("SIMPLE STYLE:")
print(TableFormatter.format_table(data, headers, alignment='left', border_style='simple'))
print("\n" + "="*60 + "\n")

print("GRID STYLE:")
print(TableFormatter.format_table(data, headers, alignment='center', border_style='grid'))
print("\n" + "="*60 + "\n")

print("MARKDOWN STYLE:")
print(TableFormatter.format_table(data, headers, alignment='right', border_style='markdown'))
```

---

## ⚡ Performance Comparison

```python
import timeit

name = "Alice"
age = 30
city = "New York"

# Test different formatting methods
def test_fstring():
    return f"Name: {name}, Age: {age}, City: {city}"

def test_format():
    return "Name: {}, Age: {}, City: {}".format(name, age, city)

def test_percent():
    return "Name: %s, Age: %d, City: %s" % (name, age, city)

def test_template():
    from string import Template
    t = Template("Name: $name, Age: $age, City: $city")
    return t.substitute(name=name, age=age, city=city)

# Measure performance
iterations = 1_000_000

fstring_time = timeit.timeit(test_fstring, number=iterations)
format_time = timeit.timeit(test_format, number=iterations)
percent_time = timeit.timeit(test_percent, number=iterations)
template_time = timeit.timeit(test_template, number=iterations)

print("=" * 50)
print("PERFORMANCE COMPARISON")
print("=" * 50)
print(f"f-strings:    {fstring_time:.4f} seconds (fastest)")
print(f"format():     {format_time:.4f} seconds")
print(f"% formatting: {percent_time:.4f} seconds")
print(f"Template:     {template_time:.4f} seconds (slowest)")
```

---

## 💡 Best Practices

### 1. **Use f-strings for Most Cases**
```python
# ✅ RECOMMENDED
name = "Alice"
print(f"Hello, {name}!")

# ❌ AVOID (unless supporting older Python)
print("Hello, {}!".format(name))
print("Hello, %s!" % name)
```

### 2. **Use Template Strings for User Input**
```python
from string import Template

# ✅ GOOD - Safe for user-supplied templates
user_template = "Hello $name"
t = Template(user_template)
print(t.substitute(name="Alice"))

# ❌ BAD - f-strings with user input (security risk)
# user_input = "Hello {name}"  # Could inject code
```

### 3. **Keep f-strings Readable**
```python
# ✅ GOOD - Simple expressions
print(f"Total: {price * quantity:.2f}")

# ❌ BAD - Complex logic in f-string
print(f"Result: {[x for x in data if x > 0 and x < 100][0] if data else 'empty'}")

# ✅ BETTER - Move complex logic out
filtered = [x for x in data if 0 < x < 100]
result = filtered[0] if filtered else 'empty'
print(f"Result: {result}")
```

### 4. **Use Appropriate Format Specifiers**
```python
# Money
price = 19.99
print(f"${price:.2f}")  # "$19.99"

# Large numbers
population = 8000000
print(f"{population:,}")  # "8,000,000"

# Percentages
score = 0.856
print(f"{score:.1%}")  # "85.6%"

# Padding for alignment
print(f"{name:>20}")  # Right align in 20 chars
```

### 5. **Multiline Strings**
```python
# ✅ GOOD - Clear multiline f-string
message = f"""
Name: {name}
Age: {age}
City: {city}
"""

# ✅ GOOD - Using parentheses
message = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"City: {city}"
)
```

---

## 📚 Quick Reference Card

```python
# f-strings (Python 3.6+)
f"{value}"                    # Basic
f"{value:.2f}"                # 2 decimal places
f"{value:>10}"                # Right align width 10
f"{value:*^20}"               # Center with * fill
f"{value:,}"                  # Thousands separator
f"{value:.1%}"                # Percentage
f"{value:b}"                  # Binary
f"{value:x}"                  # Hexadecimal
f"{value=}"                   # Self-documenting (3.8+)

# format() method
"{}".format(value)            # Basic
"{:.2f}".format(value)        # 2 decimal places
"{:>10}".format(value)        # Right align
"{name}".format(name="Alice") # Named arguments

# % formatting (old)
"%s" % value                  # String
"%d" % value                  # Integer
"%.2f" % value                # Float with 2 decimals
"%5d" % value                 # Width 5

# Template strings
from string import Template
Template("$name").substitute(name="Alice")
```

## Next Steps

- Go to [03_sequence_types](/05_python/02_data_types/03_sequence_types/README.md) for starting with Sequential Data Types.

---

*Master string formatting to create beautiful, professional output! 🐍✨*
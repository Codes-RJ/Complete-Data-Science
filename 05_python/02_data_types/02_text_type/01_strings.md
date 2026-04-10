# 📘 STRINGS (str) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Strings?](#what-are-strings)
2. [Creating Strings](#creating-strings)
3. [String Indexing and Slicing](#string-indexing-and-slicing)
4. [All String Methods](#all-string-methods)
5. [String Formatting](#string-formatting)
6. [Escape Sequences](#escape-sequences)
7. [Real-World Examples](#real-world-examples)
8. [Common Pitfalls](#common-pitfalls)
9. [Practice Exercises](#practice-exercises)

---

## 📖 What are Strings?

**Strings** are sequences of Unicode characters used to represent text in Python. They are immutable (cannot be changed after creation).

```python
# Examples of strings
single = 'Hello'
double = "World"
multi_line = """This is
a multi-line
string"""
empty = ""
unicode_str = ".__ .. _"  # Morse Code
emoji_str = "Python 🐍"
```

**Key Features:**
- ✅ Immutable (cannot be modified in-place)
- ✅ Ordered (characters have positions)
- ✅ Indexable and sliceable
- ✅ Iterable (can loop through characters)
- ✅ Unicode support (any language/emoji)

---

## 🎯 Creating Strings

### Method 1: Using Quotes

```python
# Single quotes
s1 = 'Hello'

# Double quotes
s2 = "World"

# Triple quotes (multi-line)
s3 = """Line 1
Line 2
Line 3"""

# Triple single quotes
s4 = '''Also multi-line'''

# Empty string
empty = ''
```

### Method 2: Using `str()` Constructor

```python
# From numbers
print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str(1+2j))      # "(1+2j)"

# From booleans
print(str(True))      # "True"
print(str(False))     # "False"

# From collections
print(str([1, 2, 3])) # "[1, 2, 3]"
print(str({'a': 1}))  # "{'a': 1}"

# From None
print(str(None))      # "None"
```

### Method 3: Using String Literals

```python
# Raw strings (ignore escape sequences)
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents

# Formatted strings (f-strings)
name = "Alice"
age = 30
print(f"{name} is {age} years old")

# Bytes to string
bytes_data = b'Hello'
s = bytes_data.decode('utf-8')
print(s)  # "Hello"
```

---

## 🔍 String Indexing and Slicing

### Indexing (Accessing Characters)

```python
s = "Python"

# Positive indexing (0 to len-1)
print(s[0])   # 'P'
print(s[1])   # 'y'
print(s[2])   # 't'
print(s[3])   # 'h'
print(s[4])   # 'o'
print(s[5])   # 'n'

# Negative indexing (-1 to -len)
print(s[-1])  # 'n' (last character)
print(s[-2])  # 'o'
print(s[-3])  # 'h'
print(s[-4])  # 't'
print(s[-5])  # 'y'
print(s[-6])  # 'P'

# IndexError if out of range
# print(s[6])  # IndexError!
```

### Slicing (Extracting Substrings)

```python
s = "Python Programming"

# Syntax: s[start:end:step]
# start - inclusive, end - exclusive

# Basic slicing
print(s[0:6])    # "Python" (indices 0-5)
print(s[7:18])   # "Programming" (indices 7-17)
print(s[:6])     # "Python" (from start)
print(s[7:])     # "Programming" (to end)
print(s[:])      # "Python Programming" (full copy)

# Negative indices in slicing
print(s[-11:-1]) # "Programmin" (excludes last)
print(s[-11:])   # "Programming" (to end)

# Step parameter
print(s[::2])    # "Pto rgamn" (every 2nd character)
print(s[1::2])   # "yhnPormig" (every 2nd from index 1)
print(s[::-1])   # "gnimmargorP nohtyP" (reverse)

# Slicing with out-of-range indices
print(s[0:100])  # "Python Programming" (truncates)
print(s[100:])   # "" (empty string)
```

### Practical Slicing Examples

```python
# Extract file extension
filename = "document.pdf"
extension = filename.split('.')[-1]
print(extension)  # "pdf"

# Get first and last characters
text = "Hello World"
first_char = text[0]
last_char = text[-1]
print(f"First: {first_char}, Last: {last_char}")  # First: H, Last: d

# Remove first character
print(text[1:])   # "ello World"

# Remove last character
print(text[:-1])  # "Hello Worl"

# Get middle characters
print(text[2:-2]) # "llo Wor"

# Check if palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

---

## 📚 All String Methods

### Case Conversion Methods

```python
s = "hello WORLD"

# capitalize() - First letter uppercase, rest lowercase
print(s.capitalize())  # "Hello world"

# title() - First letter of each word uppercase
print(s.title())       # "Hello World"

# upper() - All uppercase
print(s.upper())       # "HELLO WORLD"

# lower() - All lowercase
print(s.lower())       # "hello world"

# swapcase() - Swap case of each letter
print(s.swapcase())    # "HELLO world"

# casefold() - Aggressive lowercase (for caseless matching)
print("Straße".casefold())  # "strasse"

# Real use: Case-insensitive user input
user_input = "YES"
if user_input.lower() == "yes":
    print("User agreed")  # Works with "YES", "Yes", "yes"
```

### Checking Content Methods

```python
# isalpha() - All characters are letters
print("Hello".isalpha())     # True
print("Hello123".isalpha())  # False
print("".isalpha())          # False

# isdigit() - All characters are digits
print("123".isdigit())       # True
print("123.45".isdigit())    # False
print("123abc".isdigit())    # False

# isalnum() - All characters are letters or digits
print("Hello123".isalnum())  # True
print("Hello 123".isalnum()) # False (space)

# isspace() - All characters are whitespace
print("   ".isspace())       # True
print("\\t".isspace())       # True
print(" a ".isspace())       # False

# islower() - All cased characters are lowercase
print("hello".islower())     # True
print("Hello".islower())     # False
print("123".islower())       # False (no cased chars)

# isupper() - All cased characters are uppercase
print("HELLO".isupper())     # True
print("Hello".isupper())     # False

# istitle() - String is in title case
print("Hello World".istitle())  # True
print("Hello world".istitle())  # False

# isdecimal() / isnumeric() - For numeric strings
print("123".isdecimal())     # True
print("一二三".isdecimal())  # False
print("一二三".isnumeric())  # True

# Real use: Input validation
def validate_username(username):
    if not username.isalnum():
        return False, "Username must contain only letters and numbers"
    if len(username) < 3:
        return False, "Username too short"
    return True, "Valid username"

print(validate_username("john123"))   # (True, "Valid username")
print(validate_username("john@123"))  # (False, "Username must contain only letters and numbers")
```

### Search and Find Methods

```python
s = "Hello Hello Hello"

# find() - Returns lowest index, -1 if not found
print(s.find("Hello"))     # 0
print(s.find("Hello", 1))  # 6 (search from index 1)
print(s.find("World"))     # -1

# rfind() - Returns highest index
print(s.rfind("Hello"))    # 12

# index() - Like find but raises ValueError if not found
print(s.index("Hello"))    # 0
# print(s.index("World"))  # ValueError!

# rindex() - Like rfind but raises ValueError
print(s.rindex("Hello"))   # 12

# count() - Count occurrences
print(s.count("Hello"))    # 3
print(s.count("Hello", 1, 10))  # 1 (between indices 1-10)

# startswith() - Check prefix
print(s.startswith("Hello"))    # True
print(s.startswith("World"))    # False
print(s.startswith("He", 0, 5)) # True (check specific range)

# endswith() - Check suffix
print(s.endswith("Hello"))      # True
print(s.endswith("World"))      # False

# Real use: Find and extract
log_line = "ERROR: Disk full at 2024-01-15 10:30:00"
if log_line.startswith("ERROR"):
    error_msg = log_line[6:]  # Remove "ERROR: "
    print(f"Critical: {error_msg}")

# Find all positions
def find_all(text, substring):
    positions = []
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

print(find_all("abababab", "ab"))  # [0, 2, 4, 6]
```

### Stripping Whitespace Methods

```python
s = "  Hello World  \n"

# strip() - Remove leading/trailing whitespace
print(repr(s.strip()))     # 'Hello World'

# lstrip() - Remove leading whitespace
print(repr(s.lstrip()))    # 'Hello World  \n'

# rstrip() - Remove trailing whitespace
print(repr(s.rstrip()))    # '  Hello World'

# strip() with characters
s2 = "xxHello Worldxx"
print(s2.strip("x"))       # "Hello World"

s3 = "www.example.com"
print(s3.strip("w.com"))   # "example"

# Real use: Cleaning user input
user_input = "   john@example.com   \n"
clean_email = user_input.strip()
print(f"Cleaned: '{clean_email}'")  # 'john@example.com'

# Remove specific characters
phone = "+1-555-123-4567"
clean_phone = phone.strip("+-")
print(clean_phone)  # "1-555-123-4567"
```

### Split and Join Methods

```python
# split() - Split string into list
s = "apple,banana,orange,grape"

# Default split (whitespace)
print("Hello World Python".split())  # ['Hello', 'World', 'Python']

# Split by delimiter
print(s.split(","))                  # ['apple', 'banana', 'orange', 'grape']

# Split with max splits
print(s.split(",", 2))               # ['apple', 'banana', 'orange,grape']

# rsplit() - Split from right
print(s.rsplit(",", 2))              # ['apple,banana', 'orange', 'grape']

# splitlines() - Split at line breaks
multi = "Line1\nLine2\r\nLine3"
print(multi.splitlines())            # ['Line1', 'Line2', 'Line3']
print(multi.splitlines(True))        # ['Line1\n', 'Line2\r\n', 'Line3']

# partition() - Split into 3 parts
s = "name: John"
print(s.partition(":"))  # ('name', ':', ' John')

# rpartition() - Split from right
print(s.rpartition(":")) # ('name', ':', ' John')

# join() - Join list into string
words = ['Hello', 'World', 'Python']
print(" ".join(words))   # "Hello World Python"
print("-".join(words))   # "Hello-World-Python"
print("".join(words))    # "HelloWorldPython"

# Real use: CSV parsing
csv_line = "John,Doe,30,New York"
fields = csv_line.split(",")
print(fields)  # ['John', 'Doe', '30', 'New York']

# Real use: Building paths
path_parts = ['home', 'user', 'documents', 'file.txt']
path = '/'.join(path_parts)
print(path)  # "home/user/documents/file.txt"

# Real use: Slug creation
title = "My Blog Post Title"
slug = "-".join(title.lower().split())
print(slug)  # "my-blog-post-title"
```

### Replace and Translate Methods

```python
# replace() - Replace substrings
s = "Hello World, Hello Python"

print(s.replace("Hello", "Hi"))           # "Hi World, Hi Python"
print(s.replace("Hello", "Hi", 1))        # "Hi World, Hello Python"

# translate() - Replace characters using translation table
# Create translation table
table = str.maketrans("aeiou", "12345")
s = "hello world"
print(s.translate(table))  # "h2ll4 w4rld"

# Remove characters using translate
remove_table = str.maketrans("", "", "aeiou")
print(s.translate(remove_table))  # "hll wrld"

# maketrans() with dictionary
table = str.maketrans({'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'})
print("hello".translate(table))  # "h2ll4"

# Real use: Censoring bad words
def censor(text, bad_words):
    for word in bad_words:
        text = text.replace(word, "*" * len(word))
    return text

message = "This is a bad word and another bad word"
censored = censor(message, ["bad", "another"])
print(censored)  # "This is a *** word and ****** *** word"

# Real use: Normalizing quotes
def normalize_quotes(text):
    table = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"'})
    return text.translate(table)

print(normalize_quotes("‘Hello’ “World”"))  # "'Hello' \"World\""
```

### Alignment and Padding Methods

```python
# center() - Center align
s = "Python"
print(s.center(20))       # "      Python       "
print(s.center(20, '*'))  # "*******Python*******"

# ljust() - Left justify
print(s.ljust(20))        # "Python              "
print(s.ljust(20, '-'))   # "Python--------------"

# rjust() - Right justify
print(s.rjust(20))        # "              Python"
print(s.rjust(20, '-'))   # "--------------Python"

# zfill() - Pad with zeros
print("42".zfill(5))      # "00042"
print("-42".zfill(5))     # "-0042"
print("12345".zfill(3))   # "12345" (no padding needed)

# Real use: Formatting tables
def print_table(data):
    # Find maximum width
    max_width = max(len(str(item)) for row in data for item in row)
    
    for row in data:
        formatted = " | ".join(str(item).ljust(max_width) for item in row)
        print(formatted)

data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"]
]
print_table(data)
# Output:
# Name    | Age | City
# Alice   | 30  | New York
# Bob     | 25  | Los Angeles

# Real use: Creating invoices
def format_invoice(item, price, quantity):
    item_line = item.ljust(20)
    price_line = f"${price:.2f}".rjust(10)
    qty_line = str(quantity).rjust(5)
    total_line = f"${price * quantity:.2f}".rjust(10)
    
    return f"{item_line}{price_line}{qty_line}{total_line}"

print(format_invoice("Laptop", 999.99, 2))
# "Laptop               $999.99    2   $1999.98"
```

### Prefix and Suffix Methods

```python
# removeprefix() - Python 3.9+
url = "https://example.com"
print(url.removeprefix("https://"))  # "example.com"
print(url.removeprefix("http://"))   # "https://example.com" (unchanged)

# removesuffix() - Python 3.9+
filename = "document.pdf"
print(filename.removesuffix(".pdf"))  # "document"
print(filename.removesuffix(".txt"))  # "document.pdf" (unchanged)

# Real use: Cleaning URLs
def clean_url(url):
    url = url.removeprefix("https://")
    url = url.removeprefix("http://")
    url = url.removesuffix("/")
    return url

print(clean_url("https://example.com/"))  # "example.com"

# Real use: File processing
def process_file(filename):
    if filename.endswith(".txt"):
        base = filename.removesuffix(".txt")
        return f"{base}_processed.txt"
    return filename

print(process_file("data.txt"))  # "data_processed.txt"
```

### Encoding and Decoding

```python
# encode() - Convert string to bytes
s = "Hello"
utf8_bytes = s.encode('utf-8')
utf16_bytes = s.encode('utf-16')
ascii_bytes = s.encode('ascii', errors='ignore')  # Ignore non-ascii

print(utf8_bytes)   # b'Hello \xe4\xb8\x96\xe7\x95\x8c'
print(utf16_bytes)  # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00\x16N\x8c\x75'

# decode() - Convert bytes to string
bytes_data = b'Hello \xe4\xb8\x96\xe7\x95\x8c'
decoded = bytes_data.decode('utf-8')
print(decoded)

# Real use: Reading binary files
with open('file.txt', 'rb') as f:
    binary_data = f.read()
    text = binary_data.decode('utf-8')
    print(text)

# Real use: Handling different encodings
def safe_encode(text, encoding='utf-8'):
    try:
        return text.encode(encoding)
    except UnicodeEncodeError:
        return text.encode(encoding, errors='replace')

print(safe_encode("Hello", 'ascii'))
```

---

## 🎨 String Formatting

### Method 1: f-strings (Python 3.6+) – BEST

```python
name = "Alice"
age = 30
pi = 3.14159
score = 0.856

# Basic
print(f"Name: {name}, Age: {age}")  # "Name: Alice, Age: 30"

# Format numbers
print(f"Pi: {pi:.2f}")              # "Pi: 3.14"
print(f"Score: {score:.1%}")        # "Score: 85.6%"
print(f"Age: {age:5d}")             # "Age:    30" (width 5)

# Alignment
print(f"{name:>10}")   # "     Alice" (right align)
print(f"{name:<10}")   # "Alice     " (left align)
print(f"{name:^10}")   # "  Alice   " (center)

# Expressions
print(f"Sum: {5 + 3}")              # "Sum: 8"
print(f"Upper: {name.upper()}")     # "Upper: ALICE"

# Debugging (Python 3.8+)
x = 42
print(f"{x=}")        # "x=42"
print(f"{x=:.2f}")   # "x=42.00"

# Dates
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")  # "2024-01-15 10:30:00"

# Nested formatting
width = 10
print(f"{name:>{width}}")  # "     Alice"
```

### Method 2: `format()` Method

```python
name = "Alice"
age = 30
pi = 3.14159

# Positional arguments
print("{} is {} years old".format(name, age))  # "Alice is 30 years old"

# Indexed arguments
print("{0} is {1} years old".format(name, age))  # "Alice is 30 years old"
print("{1} is {0} years old".format(name, age))  # "30 is Alice years old"

# Named arguments
print("{name} is {age} years old".format(name=name, age=age))

# Format specifiers
print("{:.2f}".format(pi))           # "3.14"
print("{:>10}".format(name))         # "     Alice"
print("{:<10}".format(name))         # "Alice     "
print("{:^10}".format(name))         # "  Alice   "

# Multiple formats
print("{:10} {:5d} {:.2f}".format(name, age, pi))

# Using dictionary
data = {'name': 'Alice', 'age': 30}
print("{name} is {age} years old".format(**data))

# Using list
data = ['Alice', 30]
print("{0[0]} is {0[1]} years old".format(data))
```

### Method 3: `%` Formatting (Old Style)

```python
name = "Alice"
age = 30
pi = 3.14159

# %s - string
print("%s is %d years old" % (name, age))  # "Alice is 30 years old"

# %d - integer
print("Age: %d" % age)          # "Age: 30"

# %f - float
print("Pi: %f" % pi)            # "Pi: 3.141590"
print("Pi: %.2f" % pi)          # "Pi: 3.14"

# %x - hexadecimal
print("Hex: %x" % 255)          # "Hex: ff"

# Multiple values
print("Name: %s, Age: %d" % (name, age))

# Dictionary
data = {'name': 'Alice', 'age': 30}
print("%(name)s is %(age)d years old" % data)
```

---

## 🔧 Escape Sequences

```python
# Common escape sequences
print("Newline\nHere")      # Newline
print("Tab\tHere")          # Tab
print("Backslash\\Here")    # Backslash
print("Single quote\'")     # Single quote
print("Double quote\"")     # Double quote
print("Carriage\rReturn")   # Carriage return
print("Backspace\bHere")    # Backspace
print("Form feed\fHere")    # Form feed
print("Vertical\vTab")      # Vertical tab

# Unicode escapes
print("\u03A9")             # Ω (Omega)
print("\U0001F600")         # 😀 (Grinning face)
print("\N{GREEK CAPITAL LETTER OMEGA}")  # Ω

# Octal and hex
print("\x48\x65\x6c\x6c\x6f")  # "Hello" (hex)
print("\110\145\154\154\157")  # "Hello" (octal)

# Raw strings (ignore escapes)
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents

# Real use: Multi-line with escapes
poem = "Roses are red,\nViolets are blue,\nPython is awesome,\nAnd so are you!"
print(poem)
```

---

## 🌍 Real-World Examples

### Example 1: Email Validator

```python
import re

class EmailValidator:
    @staticmethod
    def is_valid_email(email):
        """Basic email validation without regex"""
        # Check for @
        if '@' not in email:
            return False, "Missing @ symbol"
        
        # Split into local and domain parts
        parts = email.split('@')
        if len(parts) != 2:
            return False, "Multiple @ symbols"
        
        local_part, domain = parts
        
        # Check local part
        if not local_part:
            return False, "Empty local part"
        if len(local_part) > 64:
            return False, "Local part too long"
        
        # Check domain
        if not domain:
            return False, "Empty domain"
        if '.' not in domain:
            return False, "Domain must contain dot"
        if domain.startswith('.') or domain.endswith('.'):
            return False, "Domain cannot start or end with dot"
        
        # Check for consecutive dots
        if '..' in local_part or '..' in domain:
            return False, "Consecutive dots not allowed"
        
        # Allowed characters check
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
        for char in local_part:
            if char not in allowed:
                return False, f"Invalid character '{char}' in local part"
        
        return True, "Valid email"
    
    @staticmethod
    def extract_domain(email):
        """Extract domain from email"""
        if '@' not in email:
            return None
        return email.split('@')[1]
    
    @staticmethod
    def anonymize(email):
        """Anonymize email for privacy"""
        if '@' not in email:
            return email
        local, domain = email.split('@')
        if len(local) <= 2:
            anonymized_local = local[0] + '*' * (len(local) - 1)
        else:
            anonymized_local = local[0] + '*' * (len(local) - 2) + local[-1]
        return f"{anonymized_local}@{domain}"

# Test emails
test_emails = [
    "user@example.com",
    "john.doe@gmail.com",
    "invalid.email",
    "missing@dot",
    "@missing.com",
    "user@.com",
    "user..name@example.com",
    "a" * 65 + "@example.com"
]

print("=" * 60)
print("EMAIL VALIDATOR")
print("=" * 60)

for email in test_emails:
    valid, message = EmailValidator.is_valid_email(email)
    status = "✓" if valid else "✗"
    print(f"{status} {email:<35} → {message}")
    if valid:
        print(f"   Domain: {EmailValidator.extract_domain(email)}")
        print(f"   Anonymized: {EmailValidator.anonymize(email)}")
    print()
```

### Example 2: Password Strength Checker

```python
class PasswordChecker:
    @staticmethod
    def check_strength(password):
        """Check password strength and return score"""
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
            feedback.append("✓ Good length (12+ characters)")
        elif len(password) >= 8:
            score += 1
            feedback.append("⚠️ Acceptable length (8-11 characters)")
        else:
            feedback.append("✗ Too short (<8 characters)")
        
        # Uppercase letters
        if any(c.isupper() for c in password):
            score += 1
            feedback.append("✓ Has uppercase letters")
        else:
            feedback.append("✗ Missing uppercase letters")
        
        # Lowercase letters
        if any(c.islower() for c in password):
            score += 1
            feedback.append("✓ Has lowercase letters")
        else:
            feedback.append("✗ Missing lowercase letters")
        
        # Digits
        if any(c.isdigit() for c in password):
            score += 1
            feedback.append("✓ Has numbers")
        else:
            feedback.append("✗ Missing numbers")
        
        # Special characters
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if any(c in special_chars for c in password):
            score += 1
            feedback.append("✓ Has special characters")
        else:
            feedback.append("✗ Missing special characters")
        
        # No common patterns
        common_patterns = ["password", "123456", "qwerty", "abc123", "admin"]
        if any(pattern in password.lower() for pattern in common_patterns):
            score -= 1
            feedback.append("✗ Contains common password pattern")
        
        # Determine strength
        if score >= 6:
            strength = "VERY STRONG"
            color = "🟢"
        elif score >= 4:
            strength = "STRONG"
            color = "🔵"
        elif score >= 2:
            strength = "WEAK"
            color = "🟡"
        else:
            strength = "VERY WEAK"
            color = "🔴"
        
        return {
            'score': score,
            'max_score': 7,
            'strength': strength,
            'color': color,
            'feedback': feedback
        }
    
    @staticmethod
    def suggest_improvements(password):
        """Suggest improvements for weak passwords"""
        suggestions = []
        
        if len(password) < 8:
            suggestions.append(f"Add {8 - len(password)} more characters")
        
        if not any(c.isupper() for c in password):
            suggestions.append("Add an uppercase letter")
        
        if not any(c.islower() for c in password):
            suggestions.append("Add a lowercase letter")
        
        if not any(c.isdigit() for c in password):
            suggestions.append("Add a number")
        
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            suggestions.append(f"Add a special character ({special_chars[:10]}...)")
        
        return suggestions

# Test passwords
test_passwords = [
    "weak",
    "Password123",
    "Str0ngP@ssw0rd!",
    "123456",
    "MySecureP@ssw0rd2024!",
    "password123"
]

print("=" * 70)
print("PASSWORD STRENGTH CHECKER")
print("=" * 70)

for pwd in test_passwords:
    result = PasswordChecker.check_strength(pwd)
    
    print(f"\nPassword: {pwd}")
    print(f"Strength: {result['color']} {result['strength']} (Score: {result['score']}/{result['max_score']})")
    print("Feedback:")
    for fb in result['feedback']:
        print(f"  {fb}")
    
    if result['score'] < 4:
        suggestions = PasswordChecker.suggest_improvements(pwd)
        print("Suggestions:")
        for sug in suggestions:
            print(f"  💡 {sug}")
```

### Example 3: Text Analyzer

```python
class TextAnalyzer:
    @staticmethod
    def analyze(text):
        """Complete text analysis"""
        if not text:
            return None
        
        # Basic statistics
        chars = len(text)
        words = text.split()
        word_count = len(words)
        sentences = text.count('.') + text.count('!') + text.count('?')
        
        # Character analysis
        uppercase = sum(1 for c in text if c.isupper())
        lowercase = sum(1 for c in text if c.islower())
        digits = sum(1 for c in text if c.isdigit())
        spaces = sum(1 for c in text if c.isspace())
        punctuation = chars - uppercase - lowercase - digits - spaces
        
        # Word analysis
        unique_words = set(word.lower().strip('.,!?;:') for word in words)
        word_frequencies = {}
        for word in words:
            clean_word = word.lower().strip('.,!?;:')
            word_frequencies[clean_word] = word_frequencies.get(clean_word, 0) + 1
        
        # Most common words
        most_common = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Average word length
        avg_word_length = sum(len(word.strip('.,!?;:')) for word in words) / word_count if word_count > 0 else 0
        
        # Reading time (assuming 200 words per minute)
        reading_time = word_count / 200
        
        return {
            'characters': chars,
            'words': word_count,
            'sentences': sentences,
            'uppercase': uppercase,
            'lowercase': lowercase,
            'digits': digits,
            'spaces': spaces,
            'punctuation': punctuation,
            'unique_words': len(unique_words),
            'most_common_words': most_common,
            'avg_word_length': round(avg_word_length, 2),
            'reading_time_minutes': round(reading_time, 1)
        }
    
    @staticmethod
    def generate_report(text):
        """Generate formatted report"""
        stats = TextAnalyzer.analyze(text)
        if not stats:
            return "No text to analyze"
        
        print("=" * 60)
        print("TEXT ANALYSIS REPORT")
        print("=" * 60)
        
        print("\n📊 BASIC STATISTICS")
        print("-" * 40)
        print(f"Characters: {stats['characters']:,}")
        print(f"Words: {stats['words']:,}")
        print(f"Sentences: {stats['sentences']}")
        print(f"Unique Words: {stats['unique_words']:,}")
        print(f"Average Word Length: {stats['avg_word_length']} characters")
        print(f"Estimated Reading Time: {stats['reading_time_minutes']} minutes")
        
        print("\n🔤 CHARACTER BREAKDOWN")
        print("-" * 40)
        print(f"Uppercase: {stats['uppercase']} ({stats['uppercase']/stats['characters']*100:.1f}%)")
        print(f"Lowercase: {stats['lowercase']} ({stats['lowercase']/stats['characters']*100:.1f}%)")
        print(f"Digits: {stats['digits']} ({stats['digits']/stats['characters']*100:.1f}%)")
        print(f"Spaces: {stats['spaces']} ({stats['spaces']/stats['characters']*100:.1f}%)")
        print(f"Punctuation: {stats['punctuation']} ({stats['punctuation']/stats['characters']*100:.1f}%)")
        
        print("\n📝 MOST COMMON WORDS")
        print("-" * 40)
        for word, count in stats['most_common_words']:
            print(f"  '{word}': {count} times")
        
        return stats

# Sample text for analysis
sample_text = """Python is a powerful programming language. It is widely used in data science, 
web development, and artificial intelligence. Python's simplicity makes it perfect for beginners. 
Many companies use Python for their backend systems. Python has a large and active community. 
The language continues to evolve with new features every year."""

TextAnalyzer.generate_report(sample_text)
```

### Example 4: URL Parser and Builder

```python
class URLParser:
    @staticmethod
    def parse(url):
        """Parse URL into components"""
        result = {
            'scheme': '',
            'host': '',
            'port': '',
            'path': '',
            'query': {},
            'fragment': ''
        }
        
        # Extract scheme
        if '://' in url:
            scheme_part, rest = url.split('://', 1)
            result['scheme'] = scheme_part
        else:
            rest = url
        
        # Extract fragment
        if '#' in rest:
            rest, fragment = rest.split('#', 1)
            result['fragment'] = fragment
        
        # Extract query string
        if '?' in rest:
            rest, query_string = rest.split('?', 1)
            # Parse query parameters
            if query_string:
                for param in query_string.split('&'):
                    if '=' in param:
                        key, value = param.split('=', 1)
                        result['query'][key] = value
                    else:
                        result['query'][param] = ''
        
        # Extract host and path
        if '/' in rest:
            host_part, path = rest.split('/', 1)
            result['path'] = '/' + path
        else:
            host_part = rest
            result['path'] = ''
        
        # Extract host and port
        if ':' in host_part:
            host, port = host_part.split(':', 1)
            result['host'] = host
            result['port'] = port
        else:
            result['host'] = host_part
        
        return result
    
    @staticmethod
    def build(components):
        """Build URL from components"""
        url = ""
        
        # Add scheme
        if components.get('scheme'):
            url += f"{components['scheme']}://"
        
        # Add host
        url += components.get('host', '')
        
        # Add port
        if components.get('port'):
            url += f":{components['port']}"
        
        # Add path
        if components.get('path'):
            path = components['path']
            if not path.startswith('/'):
                path = '/' + path
            url += path
        
        # Add query string
        if components.get('query'):
            query_parts = []
            for key, value in components['query'].items():
                if value:
                    query_parts.append(f"{key}={value}")
                else:
                    query_parts.append(key)
            url += "?" + "&".join(query_parts)
        
        # Add fragment
        if components.get('fragment'):
            url += f"#{components['fragment']}"
        
        return url
    
    @staticmethod
    def normalize(url):
        """Normalize URL (lowercase host, remove default ports)"""
        parsed = URLParser.parse(url)
        
        # Lowercase host
        parsed['host'] = parsed['host'].lower()
        
        # Remove default ports
        if parsed['scheme'] == 'http' and parsed['port'] == '80':
            parsed['port'] = ''
        elif parsed['scheme'] == 'https' and parsed['port'] == '443':
            parsed['port'] = ''
        
        return URLParser.build(parsed)
    
    @staticmethod
    def is_valid(url):
        """Basic URL validation"""
        if not url:
            return False
        
        # Must have scheme
        if '://' not in url:
            return False
        
        scheme = url.split('://')[0]
        if scheme not in ['http', 'https', 'ftp', 'file']:
            return False
        
        # Must have host
        rest = url.split('://')[1]
        if not rest or rest.startswith('/'):
            return False
        
        return True

# Test URLs
urls = [
    "https://www.example.com/path/to/page?name=John&age=30#section",
    "http://localhost:8080/api/users?id=123",
    "https://github.com/python/cpython/blob/main/README.md",
    "ftp://files.example.com/downloads/file.zip",
    "invalid-url",
    "https://Example.com:443/page"
]

print("=" * 70)
print("URL PARSER AND BUILDER")
print("=" * 70)

for url in urls:
    print(f"\nOriginal URL: {url}")
    
    if URLParser.is_valid(url):
        parsed = URLParser.parse(url)
        print("Parsed components:")
        print(f"  Scheme: {parsed['scheme']}")
        print(f"  Host: {parsed['host']}")
        print(f"  Port: {parsed['port'] or '(default)'}")
        print(f"  Path: {parsed['path'] or '/'}")
        print(f"  Query: {parsed['query']}")
        print(f"  Fragment: {parsed['fragment'] or '(none)'}")
        
        # Rebuild URL
        rebuilt = URLParser.build(parsed)
        print(f"Rebuilt: {rebuilt}")
        
        # Normalize URL
        normalized = URLParser.normalize(url)
        if normalized != url:
            print(f"Normalized: {normalized}")
    else:
        print("  Invalid URL")
```

### Example 5: CSV Processor

```python
import csv
from io import StringIO

class CSVProcessor:
    @staticmethod
    def parse_line(line, delimiter=','):
        """Parse a single CSV line considering quotes"""
        result = []
        current = []
        in_quotes = False
        
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
            elif char == delimiter and not in_quotes:
                result.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        
        result.append(''.join(current).strip())
        return result
    
    @staticmethod
    def to_csv(data, delimiter=','):
        """Convert list of lists to CSV string"""
        output = StringIO()
        writer = csv.writer(output, delimiter=delimiter)
        writer.writerows(data)
        return output.getvalue()
    
    @staticmethod
    def from_csv(csv_string, delimiter=','):
        """Parse CSV string to list of lists"""
        output = StringIO(csv_string)
        reader = csv.reader(output, delimiter=delimiter)
        return list(reader)
    
    @staticmethod
    def filter_rows(data, column, value):
        """Filter rows where column matches value"""
        if not data:
            return []
        
        header = data[0]
        if column not in header:
            return []
        
        col_index = header.index(column)
        filtered = [header]
        
        for row in data[1:]:
            if row[col_index] == value:
                filtered.append(row)
        
        return filtered
    
    @staticmethod
    def sort_rows(data, column, reverse=False):
        """Sort rows by column"""
        if not data or len(data) < 2:
            return data
        
        header = data[0]
        if column not in header:
            return data
        
        col_index = header.index(column)
        sorted_data = [header]
        sorted_data.extend(sorted(data[1:], key=lambda x: x[col_index], reverse=reverse))
        
        return sorted_data
    
    @staticmethod
    def add_column(data, column_name, default_value=''):
        """Add a new column to CSV data"""
        if not data:
            return []
        
        for row in data:
            row.append(default_value if row == data[0] else default_value)
        
        # Update header
        if data:
            data[0][-1] = column_name
        
        return data

# Sample CSV data
csv_data = """Name,Age,City,Salary
John,30,New York,50000
Alice,25,Los Angeles,60000
Bob,35,Chicago,55000
Carol,28,New York,65000
David,32,Chicago,52000"""

print("=" * 70)
print("CSV PROCESSOR")
print("=" * 70)

# Parse CSV
print("\n📄 ORIGINAL CSV DATA")
print("-" * 40)
print(csv_data)

# Convert to list of lists
data = CSVProcessor.from_csv(csv_data)
print("\n📊 PARSED DATA")
for row in data:
    print(f"  {row}")

# Filter rows
print("\n🔍 FILTER: City = 'New York'")
filtered = CSVProcessor.filter_rows(data, 'City', 'New York')
for row in filtered:
    print(f"  {row}")

# Sort rows
print("\n📈 SORT BY: Salary (descending)")
sorted_data = CSVProcessor.sort_rows(data, 'Salary', reverse=True)
for row in sorted_data:
    print(f"  {row}")

# Add column
print("\n➕ ADD COLUMN: 'Bonus' (10% of salary)")
data_with_bonus = CSVProcessor.add_column(data, 'Bonus')
for i, row in enumerate(data_with_bonus):
    if i > 0:  # Calculate bonus for data rows
        salary = float(row[3])
        bonus = salary * 0.1
        row[4] = f"${bonus:.2f}"
    print(f"  {row}")

# Convert back to CSV
csv_output = CSVProcessor.to_csv(data_with_bonus)
print("\n📄 OUTPUT CSV")
print("-" * 40)
print(csv_output)
```

### Example 6: String Encryption (Simple Caesar Cipher)

```python
class CaesarCipher:
    @staticmethod
    def encrypt(text, shift):
        """Encrypt text using Caesar cipher"""
        result = []
        
        for char in text:
            if char.isupper():
                # Uppercase letters
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result.append(shifted)
            elif char.islower():
                # Lowercase letters
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                result.append(shifted)
            else:
                # Non-letters remain unchanged
                result.append(char)
        
        return ''.join(result)
    
    @staticmethod
    def decrypt(text, shift):
        """Decrypt text using Caesar cipher"""
        return CaesarCipher.encrypt(text, -shift)
    
    @staticmethod
    def brute_force(ciphertext):
        """Try all possible shifts to decrypt"""
        results = []
        for shift in range(26):
            decrypted = CaesarCipher.decrypt(ciphertext, shift)
            results.append((shift, decrypted))
        return results
    
    @staticmethod
    def frequency_analysis(text):
        """Analyze letter frequency in text"""
        # Only count letters
        letters = [c.lower() for c in text if c.isalpha()]
        
        if not letters:
            return {}
        
        # Count frequencies
        freq = {}
        for letter in letters:
            freq[letter] = freq.get(letter, 0) + 1
        
        # Convert to percentages
        total = len(letters)
        for letter in freq:
            freq[letter] = (freq[letter] / total) * 100
        
        # Sort by frequency
        return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

# Test the cipher
print("=" * 70)
print("CAESAR CIPHER")
print("=" * 70)

# Original message
original = "Hello, World! Python is awesome."
shift = 3

print(f"\nOriginal: {original}")
print(f"Shift: {shift}")

# Encrypt
encrypted = CaesarCipher.encrypt(original, shift)
print(f"Encrypted: {encrypted}")

# Decrypt
decrypted = CaesarCipher.decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")

# Brute force
print("\n🔓 BRUTE FORCE ATTACK")
print("-" * 40)
ciphertext = CaesarCipher.encrypt("Secret message", 5)
print(f"Ciphertext: {ciphertext}\n")

print("Trying all shifts:")
attempts = CaesarCipher.brute_force(ciphertext)
for shift, text in attempts[:5]:  # Show first 5 attempts
    print(f"  Shift {shift:2d}: {text}")
print("  ...")

# Find the correct one (with most English-like words)
print("\n✅ Most likely decryption (shift 5):")
print(f"  {CaesarCipher.decrypt(ciphertext, 5)}")

# Frequency analysis
print("\n📊 FREQUENCY ANALYSIS")
print("-" * 40)

sample = "The quick brown fox jumps over the lazy dog"
print(f"Sample text: {sample}")

freq = CaesarCipher.frequency_analysis(sample)
print("\nLetter frequencies:")
for letter, percentage in list(freq.items())[:5]:
    print(f"  '{letter}': {percentage:.1f}%")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Strings are Immutable

```python
# ❌ WRONG - Trying to modify in-place
s = "Hello"
# s[0] = "J"  # TypeError!

# ✅ CORRECT - Create new string
s = "J" + s[1:]  # "Jello"
```

### Pitfall 2: Comparing Strings with `is`

```python
# ❌ WRONG - Using 'is' for value comparison
a = "hello"
b = "hello"
print(a is b)  # May be True or False (implementation dependent)

# ✅ CORRECT - Use '==' for value comparison
print(a == b)  # True
```

### Pitfall 3: Default Split Behavior

```python
# split() without argument splits on ANY whitespace
s = "hello   world\tpython\ncode"
print(s.split())     # ['hello', 'world', 'python', 'code']

# split(' ') splits only on space
print(s.split(' '))  # ['hello', '', '', 'world\tpython\ncode']
```

### Pitfall 4: Encoding Issues

```python
# ❌ WRONG - Assuming ASCII
# text = "café".encode('ascii')  # UnicodeEncodeError!

# ✅ CORRECT - Use appropriate encoding
text = "café".encode('utf-8')  # b'caf\xc3\xa9'

# ✅ CORRECT - Handle errors
text = "café".encode('ascii', errors='ignore')  # b'caf'
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Reverse a String**
   ```python
   # Write a function that reverses a string
   # Example: "hello" → "olleh"
   ```

2. **Count Vowels**
   ```python
   # Count vowels (a, e, i, o, u) in a string
   # Example: "hello" → 2
   ```

3. **Palindrome Checker**
   ```python
   # Check if a string reads the same forward and backward
   # Example: "racecar" → True, "hello" → False
   ```

### Intermediate Level

4. **Anagram Checker**
   ```python
   # Check if two strings are anagrams
   # Example: "listen" and "silent" → True
   ```

5. **String Compression**
   ```python
   # Compress string using run-length encoding
   # Example: "aaabbc" → "a3b2c1"
   ```

6. **Remove Duplicates**
   ```python
   # Remove duplicate characters while preserving order
   # Example: "hello" → "helo"
   ```

### Advanced Level

7. **Regular Expression Engine (Simplified)**
   ```python
   # Implement basic regex matching for '.' and '*'
   ```

8. **Markdown Parser**
   ```python
   # Convert basic markdown to HTML
   # Headers, bold, italic, links
   ```

9. **Template Engine**
   ```python
   # Create simple template engine with variables and loops
   # Example: "Hello {{name}}" with {"name": "John"} → "Hello John"
   ```

---

## 🔗 Next Steps

After mastering strings:
1. Move to `03_sequence_types/` for lists and tuples
2. Learn `string_methods.md` for all 40+ methods
3. Study `string_formatting.md` for advanced formatting

---

## 📚 Quick Reference Card

```python
# Creation
s = "text"              # Quotes
s = str(42)            # From other types
s = """multi-line"""   # Triple quotes

# Indexing & Slicing
s[0]                   # First character
s[-1]                  # Last character
s[1:4]                 # Substring
s[::-1]                # Reverse

# Common Methods
s.upper()              # Uppercase
s.lower()              # Lowercase
s.strip()              # Remove whitespace
s.split()              # Split into list
s.join(list)           # Join list
s.replace(a, b)        # Replace
s.find(sub)            # Find position
s.count(sub)           # Count occurrences
s.startswith(prefix)   # Check prefix
s.endswith(suffix)     # Check suffix
s.isalpha()            # Check letters
s.isdigit()            # Check digits

# Formatting
f"{name}"              # f-string
"{}".format(value)     # format()
"%s" % value           # % formatting

# Escape Sequences
\n                     # Newline
\t                     # Tab
\\                     # Backslash
\'                     # Single quote
\"                     # Double quote
r"raw"                 # Raw string
```

## Next Steps

- Move to [02_string_methods.md](02_string_methods.md) for starting with functions of Strings.

---

*Master strings, and you'll handle all text processing needs with confidence! 🐍✨*

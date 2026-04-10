# 📚 STRING METHODS – COMPLETE REFERENCE

## 📌 Table of Contents
1. [Case Conversion Methods](#case-conversion-methods)
2. [Character Classification Methods](#character-classification-methods)
3. [Search and Find Methods](#search-and-find-methods)
4. [Strip Methods](#strip-methods)
5. [Split and Join Methods](#split-and-join-methods)
6. [Replace and Translate Methods](#replace-and-translate-methods)
7. [Alignment and Padding Methods](#alignment-and-padding-methods)
8. [Prefix and Suffix Methods](#prefix-and-suffix-methods)
9. [Encoding Methods](#encoding-methods)
10. [Quick Reference Table](#quick-reference-table)

---

## 🔤 Case Conversion Methods

### `capitalize()`
Returns a copy of the string with first character uppercase and the rest lowercase.

```python
s = "hello WORLD"
print(s.capitalize())  # "Hello world"

# Edge cases
print("python".capitalize())     # "Python"
print("PYTHON".capitalize())     # "Python"
print("123abc".capitalize())     # "123abc"
print("".capitalize())           # ""
```

### `title()`
Returns a string where the first character of each word is uppercase.

```python
s = "hello world python"
print(s.title())  # "Hello World Python"

# Handles apostrophes (not always ideal)
print("don't stop".title())  # "Don'T Stop" (note the capital T)

# Better approach for apostrophes
import string
print(string.capwords("don't stop"))  # "Don't Stop"
```

### `upper()`
Returns a copy of the string converted to uppercase.

```python
s = "Hello World"
print(s.upper())  # "HELLO WORLD"

# Real use: Case-insensitive comparison
user_input = "Yes"
if user_input.upper() == "YES":
    print("User agreed")
```

### `lower()`
Returns a copy of the string converted to lowercase.

```python
s = "Hello World"
print(s.lower())  # "hello world"

# Real use: Normalizing email addresses
email = "User@Example.COM"
normalized = email.lower()
print(normalized)  # "user@example.com"
```

### `swapcase()`
Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

```python
s = "Hello World"
print(s.swapcase())  # "hELLO wORLD"

# Mixed case
print("PyThOn".swapcase())  # "pYtHoN"
print("123".swapcase())     # "123"
```

### `casefold()`
Returns a casefolded string (more aggressive than lower() for caseless matching).

```python
# German sharp s
s = "straße"
print(s.lower())    # "straße"
print(s.casefold()) # "strasse" (ss replaces ß)

# Real use: Case-insensitive search
def contains_casefold(text, search):
    return search.casefold() in text.casefold()

text = "HELLO WORLD"
print(contains_casefold(text, "hello"))  # True
print(contains_casefold(text, "world"))  # True
```

---

## 🔍 Character Classification Methods

### `isalpha()`
Returns True if all characters in the string are alphabetic (a-z, A-Z).

```python
print("Hello".isalpha())     # True
print("Hello123".isalpha())  # False (has numbers)
print("Hello World".isalpha()) # False (has space)
print("".isalpha())          # False (empty)
print("café".isalpha())      # True (Unicode letters)
```

### `isdigit()`
Returns True if all characters in the string are digits.

```python
print("123".isdigit())       # True
print("123.45".isdigit())    # False (decimal point)
print("-123".isdigit())      # False (minus sign)
print("一二三".isdigit())    # False (Chinese numerals)
print("".isdigit())          # False

# For other numeral systems
print("一二三".isnumeric())  # True
```

### `isalnum()`
Returns True if all characters are alphanumeric (letters or digits).

```python
print("Hello123".isalnum())  # True
print("Hello 123".isalnum()) # False (space)
print("Hello!".isalnum())    # False (punctuation)
print("".isalnum())          # False
```

### `isspace()`
Returns True if all characters are whitespace.

```python
print("   ".isspace())       # True
print("\t\n".isspace())      # True (tab, newline)
print(" a ".isspace())       # False (has 'a')
print("".isspace())          # False
```

### `islower()`
Returns True if all cased characters are lowercase.

```python
print("hello".islower())     # True
print("Hello".islower())     # False
print("hello123".islower())  # True (numbers ignored)
print("".islower())          # False (no cased chars)
```

### `isupper()`
Returns True if all cased characters are uppercase.

```python
print("HELLO".isupper())     # True
print("Hello".isupper())     # False
print("HELLO123".isupper())  # True
print("".isupper())          # False
```

### `istitle()`
Returns True if string is in title case (each word starts with uppercase).

```python
print("Hello World".istitle())   # True
print("Hello world".istitle())   # False ('w' should be uppercase)
print("HELLO WORLD".istitle())   # False
print("The Quick Brown Fox".istitle())  # True
```

### `isdecimal()`
Returns True if all characters are decimal characters.

```python
print("123".isdecimal())     # True
print("123.45".isdecimal())  # False
print("一二三".isdecimal())  # False
print("⅓".isdecimal())       # False (fraction)
```

### `isnumeric()`
Returns True if all characters are numeric (broader than isdigit).

```python
print("123".isnumeric())     # True
print("一二三".isnumeric())  # True (Chinese numerals)
print("⅓".isnumeric())       # True (fraction)
print("1/3".isnumeric())     # False
```

### `isprintable()`
Returns True if all characters are printable.

```python
print("Hello".isprintable())     # True
print("Hello\n".isprintable())   # False (newline not printable)
print("\t".isprintable())        # False
```

### `isascii()` (Python 3.7+)
Returns True if all characters are ASCII.

```python
print("Hello".isascii())     # True
print("café".isascii())      # False (é not ASCII)
print("123".isascii())       # True
```

---

## 🔎 Search and Find Methods

### `find(sub[, start[, end]])`
Returns the lowest index where substring is found, or -1 if not found.

```python
s = "Hello Hello Hello"

print(s.find("Hello"))      # 0
print(s.find("Hello", 1))   # 6 (start searching from index 1)
print(s.find("Hello", 1, 5)) # -1 (not in range)
print(s.find("World"))      # -1

# Real use: Find all positions
def find_all(text, sub):
    positions = []
    start = 0
    while True:
        pos = text.find(sub, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

print(find_all("ababab", "ab"))  # [0, 2, 4]
```

### `rfind(sub[, start[, end]])`
Returns the highest index where substring is found, or -1 if not found.

```python
s = "Hello Hello Hello"

print(s.rfind("Hello"))     # 12 (last occurrence)
print(s.rfind("Hello", 0, 10)) # 6 (within range)
print(s.rfind("World"))     # -1
```

### `index(sub[, start[, end]])`
Like find(), but raises ValueError if substring is not found.

```python
s = "Hello World"

print(s.index("World"))     # 6

# Raises error
try:
    s.index("Python")
except ValueError as e:
    print("Not found!")     # "Not found!"
```

### `rindex(sub[, start[, end]])`
Like rfind(), but raises ValueError if substring is not found.

```python
s = "Hello Hello"

print(s.rindex("Hello"))    # 6

try:
    s.rindex("Python")
except ValueError:
    print("Not found!")
```

### `count(sub[, start[, end]])`
Returns the number of non-overlapping occurrences of substring.

```python
s = "ababab"

print(s.count("ab"))        # 3
print(s.count("aba"))       # 1 (non-overlapping)
print(s.count("ab", 1))     # 2 (from index 1)
print(s.count("ab", 1, 4))  # 1 (between indices 1-4)

# Real use: Word frequency
text = "the cat and the dog and the bird"
print(text.count("the"))    # 3
```

### `startswith(prefix[, start[, end]])`
Returns True if string starts with the specified prefix.

```python
s = "Hello World"

print(s.startswith("Hello"))    # True
print(s.startswith("World"))    # False
print(s.startswith("He", 0, 5)) # True (check range)
print(s.startswith(("Hello", "Hi")))  # True (tuple of prefixes)

# Real use: File type checking
filename = "document.pdf"
if filename.startswith(("image", "photo")):
    print("Image file")
elif filename.startswith("document"):
    print("Document file")
```

### `endswith(suffix[, start[, end]])`
Returns True if string ends with the specified suffix.

```python
s = "Hello World"

print(s.endswith("World"))      # True
print(s.endswith("Hello"))      # False
print(s.endswith("ld", 8))      # True (from index 8)
print(s.endswith((".py", ".txt", ".md")))  # Check multiple

# Real use: File extension validation
filename = "script.py"
if filename.endswith((".py", ".pyw")):
    print("Python file")
elif filename.endswith((".txt", ".md")):
    print("Text file")
```

---

## ✂️ Strip Methods

### `strip([chars])`
Returns a copy with leading and trailing whitespace (or specified characters) removed.

```python
s = "  Hello World  \n"

print(repr(s.strip()))      # 'Hello World'
print(repr(s.strip(" Hd"))) # 'ello Worl'

# Remove specific characters
s2 = "xxHello Worldxx"
print(s2.strip("x"))        # "Hello World"

# Real use: Cleaning user input
user_input = "  john@example.com  "
clean = user_input.strip()
print(clean)  # "john@example.com"
```

### `lstrip([chars])`
Returns a copy with leading whitespace (or specified characters) removed.

```python
s = "  Hello World  "

print(repr(s.lstrip()))     # 'Hello World  '
print(repr(s.lstrip(" H"))) # 'ello World  '
```

### `rstrip([chars])`
Returns a copy with trailing whitespace (or specified characters) removed.

```python
s = "  Hello World  "

print(repr(s.rstrip()))     # '  Hello World'
print(repr(s.rstrip("ld"))) # '  Hello Wor'
```

### `removeprefix(prefix)` (Python 3.9+)
Returns a copy with the specified prefix removed if present.

```python
url = "https://example.com"

print(url.removeprefix("https://"))  # "example.com"
print(url.removeprefix("http://"))   # "https://example.com" (unchanged)

# Real use: Clean URLs
def clean_url(url):
    return url.removeprefix("https://").removeprefix("http://").removesuffix("/")

print(clean_url("https://example.com/"))  # "example.com"
```

### `removesuffix(suffix)` (Python 3.9+)
Returns a copy with the specified suffix removed if present.

```python
filename = "document.pdf"

print(filename.removesuffix(".pdf"))  # "document"
print(filename.removesuffix(".txt"))  # "document.pdf" (unchanged)

# Real use: File processing
def get_base_name(filename):
    extensions = [".pdf", ".txt", ".py", ".jpg"]
    for ext in extensions:
        filename = filename.removesuffix(ext)
    return filename

print(get_base_name("image.jpg"))   # "image"
print(get_base_name("script.py"))   # "script"
```

---

## ✂️ Split and Join Methods

### `split(sep=None, maxsplit=-1)`
Returns a list of substrings split by delimiter.

```python
# Default: split on whitespace
s = "Hello World Python"
print(s.split())        # ['Hello', 'World', 'Python']

# Split on specific delimiter
csv = "apple,banana,orange"
print(csv.split(","))   # ['apple', 'banana', 'orange']

# Limit number of splits
print(csv.split(",", 1))  # ['apple', 'banana,orange']

# Real use: Parsing log files
log = "ERROR 2024-01-15 Disk full"
parts = log.split(maxsplit=2)
print(parts)  # ['ERROR', '2024-01-15', 'Disk full']
```

### `rsplit(sep=None, maxsplit=-1)`
Returns a list of substrings split from the right.

```python
s = "a,b,c,d,e"
print(s.rsplit(",", 2))  # ['a,b,c', 'd', 'e']

# Real use: Extract file extension
filename = "archive.tar.gz"
parts = filename.rsplit(".", 1)
print(parts)  # ['archive.tar', 'gz']
```

### `splitlines(keepends=False)`
Returns a list of lines in the string, breaking at line boundaries.

```python
text = "Line1\nLine2\r\nLine3"

print(text.splitlines())           # ['Line1', 'Line2', 'Line3']
print(text.splitlines(True))       # ['Line1\n', 'Line2\r\n', 'Line3']

# Different line endings
print("Line1\nLine2\nLine3".splitlines())  # ['Line1', 'Line2', 'Line3']
print("Line1\rLine2\rLine3".splitlines())  # ['Line1', 'Line2', 'Line3']
```

### `partition(sep)`
Splits the string at the first occurrence of sep and returns a 3-tuple.

```python
s = "name: John Doe"

print(s.partition(":"))  # ('name', ':', ' John Doe')

# Real use: Parsing key-value pairs
config = "username=admin"
key, sep, value = config.partition("=")
print(f"Key: {key}, Value: {value}")  # Key: username, Value: admin
```

### `rpartition(sep)`
Splits the string at the last occurrence of sep and returns a 3-tuple.

```python
s = "a:b:c:d"

print(s.rpartition(":"))  # ('a:b:c', ':', 'd')

# Real use: Extract last part of path
path = "/home/user/documents/file.txt"
directory, sep, filename = path.rpartition("/")
print(f"Directory: {directory}, File: {filename}")
```

### `join(iterable)`
Returns a string concatenating elements of an iterable with the string as separator.

```python
# Join list
words = ["Hello", "World", "Python"]
print(" ".join(words))      # "Hello World Python"
print("-".join(words))      # "Hello-World-Python"
print("".join(words))       # "HelloWorldPython"

# Join tuple
colors = ("red", "green", "blue")
print(", ".join(colors))    # "red, green, blue"

# Join with different types (must be strings)
numbers = [1, 2, 3]
print(", ".join(str(n) for n in numbers))  # "1, 2, 3"

# Real use: Building paths
path_parts = ["home", "user", "docs"]
path = "/".join(path_parts)
print(path)  # "home/user/docs"

# Real use: Creating CSV
data = [["John", 30], ["Jane", 25]]
for row in data:
    print(",".join(str(cell) for cell in row))
# Output:
# John,30
# Jane,25
```

---

## 🔄 Replace and Translate Methods

### `replace(old, new, count=-1)`
Returns a copy with all occurrences of old replaced by new.

```python
s = "Hello Hello Hello"

print(s.replace("Hello", "Hi"))        # "Hi Hi Hi"
print(s.replace("Hello", "Hi", 2))     # "Hi Hi Hello"

# Real use: Censoring
message = "This is a bad word"
censored = message.replace("bad", "***")
print(censored)  # "This is a *** word"

# Real use: Template replacement
template = "Hello {{name}}, you are {{age}} years old"
result = template.replace("{{name}}", "Alice").replace("{{age}}", "30")
print(result)  # "Hello Alice, you are 30 years old"
```

### `translate(table)`
Returns a copy where each character is mapped through the translation table.

```python
# Create translation table with maketrans()
# Method 1: Two strings of equal length
table = str.maketrans("aeiou", "12345")
s = "hello world"
print(s.translate(table))  # "h2ll4 w4rld"

# Method 2: Dictionary mapping
table = str.maketrans({'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'})
print("hello".translate(table))  # "h2ll4"

# Method 3: With deletion
table = str.maketrans("", "", "aeiou")
print("hello world".translate(table))  # "hll wrld"

# Real use: Remove punctuation
import string
def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

print(remove_punctuation("Hello, World!"))  # "Hello World"

# Real use: Simple encryption
def rot13(text):
    table = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklm",
        "NOPQRSTUVWXYZnopqrstuvwxyz"
    )
    return text.translate(table)

print(rot13("Hello"))  # "Uryyb"
```

### `maketrans(x, y=None, z=None)`
Static method that creates a translation table for translate().

```python
# Two arguments (must be same length)
table = str.maketrans("abc", "123")
print("abc".translate(table))  # "123"

# Three arguments (third is characters to delete)
table = str.maketrans("abc", "123", "xyz")
print("abcxyz".translate(table))  # "123"

# Dictionary argument
table = str.maketrans({"a": "1", "b": "2", "c": "3"})
print("abc".translate(table))  # "123"
```

---

## 📏 Alignment and Padding Methods

### `center(width[, fillchar])`
Returns centered string in a field of given width.

```python
s = "Python"

print(s.center(20))        # "      Python       "
print(s.center(20, '*'))   # "*******Python*******"
print(s.center(5))         # "Python" (width smaller than string)

# Real use: Creating headers
def print_header(text, width=50):
    print(text.center(width, '='))
    print()

print_header("Welcome to Python")
# Output: ==========Welcome to Python==========
```

### `ljust(width[, fillchar])`
Returns left-justified string in a field of given width.

```python
s = "Python"

print(s.ljust(20))        # "Python              "
print(s.ljust(20, '-'))   # "Python--------------"

# Real use: Creating table columns
def print_table_row(col1, col2, col3, widths):
    print(col1.ljust(widths[0]), col2.ljust(widths[1]), col3.ljust(widths[2]))

print_table_row("Name", "Age", "City", [15, 5, 20])
print_table_row("Alice", "30", "New York", [15, 5, 20])
# Output:
# Name            Age  City
# Alice           30   New York
```

### `rjust(width[, fillchar])`
Returns right-justified string in a field of given width.

```python
s = "Python"

print(s.rjust(20))        # "              Python"
print(s.rjust(20, '-'))   # "--------------Python"

# Real use: Aligning numbers
prices = [19.99, 5.50, 125.00]
for price in prices:
    print(f"${price:.2f}".rjust(10))
# Output:
#     $19.99
#      $5.50
#    $125.00
```

### `zfill(width)`
Pads string on the left with zeros to fill width.

```python
print("42".zfill(5))       # "00042"
print("-42".zfill(5))      # "-0042"
print("12345".zfill(3))    # "12345" (no padding needed)
print("".zfill(5))         # "00000"

# Real use: Formatting numbers
def format_id(id_num, width=8):
    return str(id_num).zfill(width)

print(format_id(123))       # "00000123"
print(format_id(42, 5))     # "00042"

# Real use: Time formatting
hours = [1, 2, 3, 10, 11, 12]
for h in hours:
    print(f"{str(h).zfill(2)}:00")
# Output: 01:00, 02:00, 03:00, 10:00, 11:00, 12:00
```

### `expandtabs(tabsize=8)`
Returns a copy with tab characters expanded to spaces.

```python
s = "Hello\tWorld"

print(s.expandtabs())      # "Hello   World" (default 8 spaces)
print(s.expandtabs(4))     # "Hello   World" (4 spaces)
print(s.expandtabs(2))     # "Hello World" (2 spaces)

# Real use: Formatting tab-separated data
data = "Name\tAge\tCity\nJohn\t30\tNYC"
print(data.expandtabs(15))
# Output:
# Name           Age            City
# John           30             NYC
```

---

## 📌 Prefix and Suffix Methods

### `removeprefix(prefix)` (Python 3.9+)
Already covered in Strip Methods section.

### `removesuffix(suffix)` (Python 3.9+)
Already covered in Strip Methods section.

---

## 🔐 Encoding Methods

### `encode(encoding='utf-8', errors='strict')`
Returns encoded version of the string as bytes object.

```python
s = "Hello"

# UTF-8 encoding
utf8_bytes = s.encode('utf-8')
print(utf8_bytes)  # b'Hello \xe4\xb8\x96\xe7\x95\x8c'

# ASCII with error handling
try:
    ascii_bytes = s.encode('ascii')
except UnicodeEncodeError:
    print("Cannot encode to ASCII")

# Different error handling
print(s.encode('ascii', errors='ignore'))   # b'Hello '
print(s.encode('ascii', errors='replace'))  # b'Hello ??'
print(s.encode('ascii', errors='xmlcharrefreplace'))  # b'Hello &#19990;&#30028;'

# Real use: Saving to file
text = "Python is awesome"
with open('file.txt', 'wb') as f:
    f.write(text.encode('utf-8'))
```

---

## 📊 Quick Reference Table

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `capitalize()` | First letter uppercase | `"hello".capitalize()` | `"Hello"` |
| `title()` | Each word title case | `"hello world".title()` | `"Hello World"` |
| `upper()` | All uppercase | `"Hello".upper()` | `"HELLO"` |
| `lower()` | All lowercase | `"Hello".lower()` | `"hello"` |
| `swapcase()` | Swap case | `"Hello".swapcase()` | `"hELLO"` |
| `casefold()` | Aggressive lowercase | `"straße".casefold()` | `"strasse"` |
| `isalpha()` | Check letters | `"Hello".isalpha()` | `True` |
| `isdigit()` | Check digits | `"123".isdigit()` | `True` |
| `isalnum()` | Check alphanumeric | `"Hello123".isalnum()` | `True` |
| `isspace()` | Check whitespace | `"   ".isspace()` | `True` |
| `islower()` | Check lowercase | `"hello".islower()` | `True` |
| `isupper()` | Check uppercase | `"HELLO".isupper()` | `True` |
| `istitle()` | Check title case | `"Hello World".istitle()` | `True` |
| `find()` | Find substring | `"Hello".find("e")` | `1` |
| `rfind()` | Find from right | `"Hello".rfind("l")` | `3` |
| `index()` | Find or error | `"Hello".index("e")` | `1` |
| `rindex()` | Find from right or error | `"Hello".rindex("l")` | `3` |
| `count()` | Count occurrences | `"Hello".count("l")` | `2` |
| `startswith()` | Check prefix | `"Hello".startswith("He")` | `True` |
| `endswith()` | Check suffix | `"Hello".endswith("lo")` | `True` |
| `strip()` | Remove whitespace | `"  Hi  ".strip()` | `"Hi"` |
| `lstrip()` | Remove left whitespace | `"  Hi".lstrip()` | `"Hi"` |
| `rstrip()` | Remove right whitespace | `"Hi  ".rstrip()` | `"Hi"` |
| `removeprefix()` | Remove prefix (3.9+) | `"prefixHi".removeprefix("prefix")` | `"Hi"` |
| `removesuffix()` | Remove suffix (3.9+) | `"Hi suffix".removesuffix(" suffix")` | `"Hi"` |
| `split()` | Split into list | `"a,b,c".split(",")` | `['a','b','c']` |
| `rsplit()` | Split from right | `"a,b,c".rsplit(",",1)` | `['a,b','c']` |
| `splitlines()` | Split at line breaks | `"a\nb".splitlines()` | `['a','b']` |
| `partition()` | Split into 3 parts | `"a=b".partition("=")` | `('a','=','b')` |
| `rpartition()` | Split from right | `"a=b=c".rpartition("=")` | `('a=b','=','c')` |
| `join()` | Join iterable | `",".join(['a','b'])` | `"a,b"` |
| `replace()` | Replace substring | `"Hi".replace("i","ello")` | `"Hello"` |
| `translate()` | Character mapping | `"abc".translate(table)` | `"123"` |
| `maketrans()` | Create translation table | `str.maketrans("abc","123")` | Table |
| `center()` | Center align | `"Hi".center(5,'*')` | `"**Hi**"` |
| `ljust()` | Left justify | `"Hi".ljust(4,'-')` | `"Hi--"` |
| `rjust()` | Right justify | `"Hi".rjust(4,'-')` | `"--Hi"` |
| `zfill()` | Pad with zeros | `"42".zfill(5)` | `"00042"` |
| `expandtabs()` | Expand tabs | `"a\tb".expandtabs(4)` | `"a   b"` |
| `encode()` | Encode to bytes | `"Hi".encode()` | `b'Hi'` |

---

## 🎯 Quick Selection Guide

### What do you want to do?

| Task | Best Method |
|------|-------------|
| Change case | `upper()`, `lower()`, `capitalize()` |
| Validate input | `isalpha()`, `isdigit()`, `isalnum()` |
| Find text | `find()`, `index()` |
| Count occurrences | `count()` |
| Remove whitespace | `strip()`, `lstrip()`, `rstrip()` |
| Split text | `split()`, `rsplit()` |
| Join text | `join()` |
| Replace text | `replace()`, `translate()` |
| Format text | `center()`, `ljust()`, `rjust()`, `zfill()` |
| Check start/end | `startswith()`, `endswith()` |
| Remove prefix/suffix | `removeprefix()`, `removesuffix()` |

## Next Steps

- Move to [03_string_formatting.md](03_string_formatting.md) for starting with formatting of Strings.

---

*This completes the string methods reference! 🐍✨*
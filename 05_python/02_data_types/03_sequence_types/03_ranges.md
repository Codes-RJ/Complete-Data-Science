# 📘 RANGES (range) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Ranges?](#what-are-ranges)
2. [Creating Ranges](#creating-ranges)
3. [Range Properties](#range-properties)
4. [Range Operations](#range-operations)
5. [Iterating with Ranges](#iterating-with-ranges)
6. [Real-World Examples](#real-world-examples)
7. [Performance Benefits](#performance-benefits)
8. [Common Pitfalls](#common-pitfalls)
9. [Practice Exercises](#practice-exercises)

---

## 📖 What are Ranges?

**Ranges** are immutable sequences of numbers that are commonly used for looping a specific number of times. They are memory-efficient because they don't store all values; they calculate them on demand.

```python
# Examples of ranges
r1 = range(5)        # 0, 1, 2, 3, 4
r2 = range(2, 8)     # 2, 3, 4, 5, 6, 7
r3 = range(1, 10, 2) # 1, 3, 5, 7, 9
r4 = range(10, 0, -2) # 10, 8, 6, 4, 2
```

**Key Features:**
- ✅ Immutable (cannot be changed)
- ✅ Memory efficient (doesn't store all values)
- ✅ Fast for membership testing
- ✅ Supports slicing
- ✅ Works with negative steps
- ✅ Can be converted to list/tuple

---

## 🎯 Creating Ranges

### Method 1: `range(stop)`
Creates a range from 0 to stop-1.

```python
# Single argument (stop)
r = range(5)
print(list(r))  # [0, 1, 2, 3, 4]

r = range(1)
print(list(r))  # [0]

r = range(0)
print(list(r))  # [] (empty)

# With negative stop (empty range)
r = range(-5)
print(list(r))  # [] (empty)
```

### Method 2: `range(start, stop)`
Creates a range from start to stop-1.

```python
# Two arguments (start, stop)
r = range(2, 8)
print(list(r))  # [2, 3, 4, 5, 6, 7]

r = range(-5, 5)
print(list(r))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

r = range(10, 5)
print(list(r))  # [] (empty, start > stop with positive step)
```

### Method 3: `range(start, stop, step)`
Creates a range with specified step.

```python
# Three arguments (start, stop, step)
r = range(1, 10, 2)
print(list(r))  # [1, 3, 5, 7, 9]

r = range(10, 1, -2)
print(list(r))  # [10, 8, 6, 4, 2]

r = range(0, 10, 3)
print(list(r))  # [0, 3, 6, 9]

# Step can be negative
r = range(5, 0, -1)
print(list(r))  # [5, 4, 3, 2, 1]

# Step = 0 (invalid)
# r = range(0, 10, 0)  # ValueError!
```

### Converting Ranges to Other Types

```python
r = range(1, 11)

# To list
print(list(r))     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# To tuple
print(tuple(r))    # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# To set
print(set(r))      # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# To string (using join)
print(''.join(str(i) for i in r))  # "12345678910"
```

---

## 🔧 Range Properties

Ranges have three read-only properties.

### `start` – Starting Value

```python
r = range(5, 20, 3)
print(r.start)  # 5

r = range(10)
print(r.start)  # 0

r = range(-5, 5)
print(r.start)  # -5
```

### `stop` – Stopping Value (exclusive)

```python
r = range(5, 20, 3)
print(r.stop)   # 20

r = range(10)
print(r.stop)   # 10

r = range(-5, 5)
print(r.stop)   # 5
```

### `step` – Step Value

```python
r = range(5, 20, 3)
print(r.step)   # 3

r = range(10)
print(r.step)   # 1 (default)

r = range(10, 0, -2)
print(r.step)   # -2
```

### Length and Indexing

```python
r = range(1, 10, 2)

# Length
print(len(r))   # 5 (1,3,5,7,9)

# Indexing
print(r[0])     # 1
print(r[2])     # 5
print(r[-1])    # 9 (last element)
print(r[-2])    # 7

# Slicing ranges (returns new range)
r2 = r[1:4]
print(list(r2))  # [3, 5, 7]
print(type(r2))  # <class 'range'>

# IndexError if out of range
try:
    print(r[10])
except IndexError:
    print("Index out of range")
```

---

## ⚡ Range Operations

### Membership Testing (`in`)

```python
r = range(1, 1000000)

# Fast - doesn't generate all numbers
print(500000 in r)    # True (fast!)
print(1000000 in r)   # False (fast!)
print(0 in r)         # False (fast!)

# Check if number is in range without generating list
def is_in_range(n, start, stop, step=1):
    return n in range(start, stop, step)

print(is_in_range(5, 1, 10))     # True
print(is_in_range(15, 1, 10))    # False
```

### Comparison

```python
# Ranges compare lexicographically
r1 = range(1, 5)
r2 = range(1, 5)
r3 = range(1, 6)

print(r1 == r2)   # True (same values)
print(r1 == r3)   # False
print(r1 != r3)   # True

# Ranges can be compared even if not same object
r4 = range(1, 5)
r5 = range(1, 5)
print(r4 is r5)   # False (different objects)
print(r4 == r5)   # True (same values)
```

### Iteration

```python
# Basic iteration
for i in range(5):
    print(i, end=" ")
print()  # 0 1 2 3 4

# With start and step
for i in range(2, 10, 2):
    print(i, end=" ")
print()  # 2 4 6 8

# Reverse iteration
for i in range(10, 0, -1):
    print(i, end=" ")
print()  # 10 9 8 7 6 5 4 3 2 1

# Using enumerate
for index, value in enumerate(range(5, 10)):
    print(f"{index}: {value}")
# Output:
# 0: 5
# 1: 6
# 2: 7
# 3: 8
# 4: 9
```

---

## 🔄 Iterating with Ranges

### Basic Loops

```python
# Loop n times
n = 5
for i in range(n):
    print(f"Iteration {i+1}")

# Loop with specific range
for i in range(10, 21):
    print(f"Number: {i}")

# Loop with step
for i in range(0, 100, 10):
    print(f"Multiple of 10: {i}")
```

### Nested Loops

```python
# Multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
# Output: 10x10 multiplication table

# Triangle pattern
n = 5
for i in range(1, n+1):
    print('*' * i)
# Output:
# *
# **
# ***
# ****
# *****

# Reverse triangle
for i in range(n, 0, -1):
    print('*' * i)
# Output:
# *****
# ****
# ***
# **
# *
```

### Using Range with List Comprehensions

```python
# Squares of numbers 1-10
squares = [i**2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Even numbers
evens = [i for i in range(20) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Odd numbers
odds = [i for i in range(1, 20, 2)]
print(odds)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# List of tuples
pairs = [(i, i**2) for i in range(1, 6)]
print(pairs)  # [(1,1), (2,4), (3,9), (4,16), (5,25)]
```

---

## 🌍 Real-World Examples

### Example 1: Number Guessing Game

```python
import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.max_attempts = 7
    
    def guess(self, number):
        """Make a guess"""
        self.attempts += 1
        
        if number < self.min_num or number > self.max_num:
            return f"Number must be between {self.min_num} and {self.max_num}"
        
        if number == self.secret_number:
            return f"Correct! You guessed it in {self.attempts} attempts!"
        elif number < self.secret_number:
            return "Too low!"
        else:
            return "Too high!"
    
    def play(self):
        """Play the game"""
        print("=" * 50)
        print("NUMBER GUESSING GAME")
        print("=" * 50)
        print(f"Guess a number between {self.min_num} and {self.max_num}")
        print(f"You have {self.max_attempts} attempts")
        print("-" * 50)
        
        for attempt in range(1, self.max_attempts + 1):
            try:
                guess_num = int(input(f"Attempt {attempt}: "))
                result = self.guess(guess_num)
                print(result)
                
                if "Correct" in result:
                    break
                
                remaining = self.max_attempts - attempt
                if remaining > 0:
                    print(f"Remaining attempts: {remaining}")
                
            except ValueError:
                print("Please enter a valid number")
        
        if self.attempts >= self.max_attempts and self.secret_number not in [self.guess]:
            print(f"\nGame over! The number was {self.secret_number}")

# Play game
game = NumberGuessingGame(1, 50)
# game.play()  # Uncomment to play
```

### Example 2: Multiplication Table Generator

```python
class MultiplicationTable:
    @staticmethod
    def generate_table(size=10):
        """Generate multiplication table"""
        print("=" * (size * 5 + 1))
        print("MULTIPLICATION TABLE".center(size * 5 + 1))
        print("=" * (size * 5 + 1))
        
        # Header row
        print("    |", end="")
        for i in range(1, size + 1):
            print(f"{i:4}", end="")
        print("\n" + "-" * (size * 5 + 1))
        
        # Table rows
        for i in range(1, size + 1):
            print(f"{i:3} |", end="")
            for j in range(1, size + 1):
                print(f"{i*j:4}", end="")
            print()
        
        print("=" * (size * 5 + 1))
    
    @staticmethod
    def times_table(number, up_to=12):
        """Generate times table for a specific number"""
        print(f"\nTimes Table for {number}")
        print("-" * 30)
        
        for i in range(1, up_to + 1):
            result = number * i
            print(f"{number:2} × {i:2} = {result:3}")
        
        print("-" * 30)
    
    @staticmethod
    def find_patterns(size=10):
        """Find patterns in multiplication table"""
        print(f"\nPATTERNS IN {size}x{size} TABLE")
        print("=" * 40)
        
        # Diagonal (squares)
        squares = [i*i for i in range(1, size+1)]
        print(f"Squares: {squares}")
        
        # Even numbers count in each row
        for i in range(1, size+1):
            evens = sum(1 for j in range(1, size+1) if (i*j) % 2 == 0)
            print(f"Row {i:2}: {evens} even numbers")
        
        # Numbers ending with 5
        ends_with_5 = []
        for i in range(1, size+1):
            for j in range(1, size+1):
                if (i*j) % 10 == 5:
                    ends_with_5.append((i, j, i*j))
        
        print(f"\nProducts ending with 5: {ends_with_5[:10]}...")

# Generate tables
MultiplicationTable.generate_table(12)

MultiplicationTable.times_table(7)
MultiplicationTable.times_table(12, 15)

MultiplicationTable.find_patterns(10)
```

### Example 3: Password Generator

```python
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        """Generate random password"""
        # Build character pool
        pool = self.lowercase
        if use_upper:
            pool += self.uppercase
        if use_digits:
            pool += self.digits
        if use_symbols:
            pool += self.symbols
        
        if not pool:
            return "Error: No character types selected"
        
        # Generate password
        password_chars = []
        for _ in range(length):
            password_chars.append(random.choice(pool))
        
        # Ensure at least one of each selected type
        if use_upper and not any(c in self.uppercase for c in password_chars):
            password_chars[0] = random.choice(self.uppercase)
        
        if use_digits and not any(c in self.digits for c in password_chars):
            password_chars[1] = random.choice(self.digits)
        
        if use_symbols and not any(c in self.symbols for c in password_chars):
            password_chars[2] = random.choice(self.symbols)
        
        # Shuffle
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_multiple(self, count=5, **kwargs):
        """Generate multiple passwords"""
        passwords = []
        for i in range(count):
            passwords.append(self.generate(**kwargs))
        return passwords
    
    def check_strength(self, password):
        """Check password strength"""
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
        
        # Character variety
        if any(c in self.uppercase for c in password):
            score += 1
            feedback.append("✓ Has uppercase letters")
        else:
            feedback.append("✗ Missing uppercase letters")
        
        if any(c in self.digits for c in password):
            score += 1
            feedback.append("✓ Has numbers")
        else:
            feedback.append("✗ Missing numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
            feedback.append("✓ Has special characters")
        else:
            feedback.append("✗ Missing special characters")
        
        # Determine strength
        if score >= 5:
            strength = "VERY STRONG"
        elif score >= 3:
            strength = "STRONG"
        elif score >= 2:
            strength = "WEAK"
        else:
            strength = "VERY WEAK"
        
        return {'score': score, 'strength': strength, 'feedback': feedback}

# Create generator
pwd_gen = PasswordGenerator()

print("PASSWORD GENERATOR")
print("=" * 50)

# Generate single password
password = pwd_gen.generate(length=16)
print(f"\nSingle Password: {password}")

# Generate multiple passwords
print("\nMultiple Passwords:")
passwords = pwd_gen.generate_multiple(5, length=12)
for i, pwd in enumerate(passwords, 1):
    print(f"  {i}. {pwd}")

# Check password strength
print("\nPASSWORD STRENGTH CHECK")
print("-" * 40)
test_passwords = [
    "weak",
    "Medium123",
    "StrongP@ssw0rd",
    "VeryStr0ng!P@ssw0rd2024"
]

for pwd in test_passwords:
    result = pwd_gen.check_strength(pwd)
    print(f"\nPassword: {pwd}")
    print(f"Strength: {result['strength']} (Score: {result['score']}/5)")
    for fb in result['feedback']:
        print(f"  {fb}")

# Generate passwords with different settings
print("\nCUSTOM PASSWORD GENERATION")
print("-" * 40)

configs = [
    {"length": 8, "use_upper": True, "use_digits": True, "use_symbols": False},
    {"length": 12, "use_upper": True, "use_digits": True, "use_symbols": True},
    {"length": 16, "use_upper": True, "use_digits": True, "use_symbols": True}
]

for config in configs:
    pwd = pwd_gen.generate(**config)
    print(f"Length {config['length']:2}: {pwd}")
```

### Example 4: Data Range Analyzer

```python
class DataRangeAnalyzer:
    @staticmethod
    def analyze_range(data):
        """Analyze numeric data range"""
        if not data:
            return None
        
        min_val = min(data)
        max_val = max(data)
        range_size = max_val - min_val
        
        # Create range buckets
        num_buckets = min(10, len(set(data)))
        bucket_size = range_size / num_buckets if num_buckets > 0 else 1
        
        buckets = [[] for _ in range(num_buckets)]
        for value in data:
            if value == max_val:
                bucket_index = num_buckets - 1
            else:
                bucket_index = int((value - min_val) / bucket_size)
            buckets[bucket_index].append(value)
        
        return {
            'min': min_val,
            'max': max_val,
            'range': range_size,
            'count': len(data),
            'unique': len(set(data)),
            'buckets': buckets,
            'bucket_size': bucket_size
        }
    
    @staticmethod
    def generate_sequence(start, stop, step=1):
        """Generate sequence within range"""
        if step > 0 and start >= stop:
            return []
        if step < 0 and start <= stop:
            return []
        
        return list(range(start, stop, step))
    
    @staticmethod
    def find_missing_numbers(sequence):
        """Find missing numbers in sequence"""
        if not sequence:
            return []
        
        min_val = min(sequence)
        max_val = max(sequence)
        full_set = set(range(min_val, max_val + 1))
        missing = full_set - set(sequence)
        return sorted(missing)
    
    @staticmethod
    def chunk_range(start, stop, chunk_size):
        """Split range into chunks"""
        chunks = []
        for i in range(start, stop, chunk_size):
            chunk_end = min(i + chunk_size, stop)
            chunks.append(range(i, chunk_end))
        return chunks
    
    @staticmethod
    def report(stats):
        """Generate analysis report"""
        if not stats:
            return "No data"
        
        print("=" * 50)
        print("DATA RANGE ANALYSIS")
        print("=" * 50)
        print(f"Total Values: {stats['count']}")
        print(f"Unique Values: {stats['unique']}")
        print(f"Minimum: {stats['min']}")
        print(f"Maximum: {stats['max']}")
        print(f"Range: {stats['range']}")
        print(f"Bucket Size: {stats['bucket_size']:.2f}")
        
        print("\nBUCKET DISTRIBUTION:")
        print("-" * 40)
        for i, bucket in enumerate(stats['buckets']):
            percentage = (len(bucket) / stats['count']) * 100
            bar = '█' * int(percentage / 2)
            print(f"Bucket {i+1:2}: {len(bucket):5} values ({percentage:5.1f}%) {bar}")
        
        print("=" * 50)

# Example usage
print("DATA RANGE ANALYZER")
print("=" * 50)

# Generate sample data
data = list(range(1, 101)) + [50, 75, 25] * 10
random.shuffle(data)

# Analyze
analyzer = DataRangeAnalyzer()
stats = analyzer.analyze_range(data)
analyzer.report(stats)

# Generate sequences
print("\nSEQUENCE GENERATION")
print("-" * 40)
print(f"Range(10): {analyzer.generate_sequence(10)}")
print(f"Range(2, 10, 2): {analyzer.generate_sequence(2, 10, 2)}")
print(f"Range(10, 2, -2): {analyzer.generate_sequence(10, 2, -2)}")

# Find missing numbers
print("\nFIND MISSING NUMBERS")
print("-" * 40)
sequence = [1, 2, 3, 5, 6, 8, 9, 10]
missing = analyzer.find_missing_numbers(sequence)
print(f"Sequence: {sequence}")
print(f"Missing: {missing}")

# Chunk ranges
print("\nCHUNKING RANGES")
print("-" * 40)
chunks = analyzer.chunk_range(1, 20, 5)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {list(chunk)}")
```

### Example 5: Calendar Generator

```python
class CalendarGenerator:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.days_in_month = self._get_days_in_month()
        self.first_weekday = self._get_first_weekday()
    
    def _get_days_in_month(self):
        """Get number of days in month"""
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            # Check for leap year
            if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
                return 29
            return 28
        return 0
    
    def _get_first_weekday(self):
        """Get first weekday of month (0=Monday, 6=Sunday)"""
        # Zeller's congruence algorithm
        if self.month < 3:
            month = self.month + 12
            year = self.year - 1
        else:
            month = self.month
            year = self.year
        
        k = year % 100
        j = year // 100
        
        h = (1 + (13*(month+1))//5 + k + k//4 + j//4 + 5*j) % 7
        
        # Convert to Monday-based (0=Monday, 6=Sunday)
        return (h + 5) % 7
    
    def generate(self):
        """Generate calendar for month"""
        month_names = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        print("=" * 29)
        print(f"{month_names[self.month-1]} {self.year}".center(29))
        print("=" * 29)
        
        # Print weekdays
        for day in weekday_names:
            print(f"{day:>3}", end="")
        print()
        
        # Print calendar
        print("    " * self.first_weekday, end="")
        
        for day in range(1, self.days_in_month + 1):
            print(f"{day:3}", end="")
            if (self.first_weekday + day) % 7 == 0:
                print()
        
        print("\n" + "=" * 29)
    
    def generate_year_calendar(year):
        """Generate full year calendar"""
        print("=" * 29)
        print(f"{year}".center(29))
        print("=" * 29)
        
        for month in range(1, 13):
            cal = CalendarGenerator(year, month)
            cal.generate()
            print()

# Generate single month calendar
print("CALENDAR GENERATOR")
print("=" * 50)

cal = CalendarGenerator(2024, 12)
cal.generate()

# Generate full year
print("\nFULL YEAR CALENDAR")
CalendarGenerator.generate_year_calendar(2024)
```

### Example 6: Batch Processor

```python
class BatchProcessor:
    def __init__(self, items, batch_size=100):
        self.items = items
        self.batch_size = batch_size
        self.total_items = len(items)
        self.num_batches = (self.total_items + batch_size - 1) // batch_size
    
    def process_batch(self, start_idx, end_idx):
        """Process a single batch"""
        batch = self.items[start_idx:end_idx]
        # Simulate processing
        return {
            'batch_id': start_idx // self.batch_size + 1,
            'start': start_idx,
            'end': end_idx,
            'size': len(batch),
            'data': batch
        }
    
    def process_all(self, show_progress=True):
        """Process all batches"""
        results = []
        
        for batch_num in range(self.num_batches):
            start = batch_num * self.batch_size
            end = min(start + self.batch_size, self.total_items)
            
            result = self.process_batch(start, end)
            results.append(result)
            
            if show_progress:
                progress = (batch_num + 1) / self.num_batches * 100
                print(f"Batch {result['batch_id']:3}: {result['size']:3} items - Progress: {progress:5.1f}%")
        
        return results
    
    def get_summary(self, results):
        """Get processing summary"""
        print("=" * 50)
        print("BATCH PROCESSING SUMMARY")
        print("=" * 50)
        print(f"Total Items: {self.total_items}")
        print(f"Batch Size: {self.batch_size}")
        print(f"Number of Batches: {self.num_batches}")
        print(f"Last Batch Size: {results[-1]['size']}")
        print("=" * 50)

# Example usage
print("BATCH PROCESSOR")
print("=" * 50)

# Create sample data
data = list(range(1, 1001))  # 1000 items

# Process in different batch sizes
batch_sizes = [50, 100, 250, 500]

for batch_size in batch_sizes:
    print(f"\nProcessing with batch size: {batch_size}")
    print("-" * 40)
    
    processor = BatchProcessor(data, batch_size)
    results = processor.process_all(show_progress=True)
    processor.get_summary(results)

# Real-world example: Processing large file
print("\n" + "=" * 50)
print("LARGE FILE SIMULATION")
print("=" * 50)

class FileProcessor:
    def __init__(self, filename, batch_size=1000):
        self.filename = filename
        self.batch_size = batch_size
    
    def process_file(self):
        """Simulate processing large file in batches"""
        # Simulate reading file
        total_lines = 10000
        print(f"Processing file: {self.filename}")
        print(f"Total lines: {total_lines}")
        print(f"Batch size: {self.batch_size}")
        print("-" * 40)
        
        processed = 0
        for batch_num in range(0, total_lines, self.batch_size):
            batch_start = batch_num
            batch_end = min(batch_num + self.batch_size, total_lines)
            batch_size = batch_end - batch_start
            
            # Simulate processing
            processed += batch_size
            progress = (processed / total_lines) * 100
            
            print(f"Batch {batch_num//self.batch_size + 1:3}: "
                  f"Lines {batch_start:5}-{batch_end:5} "
                  f"({batch_size:4} lines) - {progress:5.1f}%")
        
        print("=" * 40)
        print(f"Processing complete! Total lines: {processed}")
        print("=" * 40)

# Process file
file_processor = FileProcessor("large_data.txt", batch_size=1500)
file_processor.process_file()
```

### Example 7: Pagination System

```python
class Paginator:
    def __init__(self, items, items_per_page=10):
        self.items = items
        self.items_per_page = items_per_page
        self.total_items = len(items)
        self.total_pages = (self.total_items + items_per_page - 1) // items_per_page
    
    def get_page(self, page_num):
        """Get specific page (1-indexed)"""
        if page_num < 1 or page_num > self.total_pages:
            return None
        
        start = (page_num - 1) * self.items_per_page
        end = min(start + self.items_per_page, self.total_items)
        
        return {
            'page': page_num,
            'items': self.items[start:end],
            'start': start + 1,
            'end': end,
            'total': self.total_items,
            'has_prev': page_num > 1,
            'has_next': page_num < self.total_pages
        }
    
    def get_page_range(self, current_page, window=3):
        """Get range of page numbers to display"""
        start = max(1, current_page - window)
        end = min(self.total_pages, current_page + window)
        
        pages = list(range(start, end + 1))
        
        # Add ellipsis
        if start > 2:
            pages = [1, '...'] + pages
        elif start > 1:
            pages = [1] + pages
        
        if end < self.total_pages - 1:
            pages = pages + ['...', self.total_pages]
        elif end < self.total_pages:
            pages = pages + [self.total_pages]
        
        return pages
    
    def display_page(self, page_num):
        """Display formatted page"""
        page_data = self.get_page(page_num)
        if not page_data:
            print("Page not found")
            return
        
        print("=" * 60)
        print(f"PAGE {page_data['page']} OF {self.total_pages}")
        print(f"Showing items {page_data['start']}-{page_data['end']} of {page_data['total']}")
        print("-" * 60)
        
        for i, item in enumerate(page_data['items'], page_data['start']):
            print(f"{i:4}. {item}")
        
        print("-" * 60)
        
        # Show pagination controls
        page_range = self.get_page_range(page_num)
        display = []
        for p in page_range:
            if p == page_num:
                display.append(f"[{p}]")
            elif p == '...':
                display.append('...')
            else:
                display.append(str(p))
        
        print(" ".join(display))
        print("=" * 60)
        
        # Navigation hints
        if page_data['has_prev']:
            print("← Previous (p)")
        if page_data['has_next']:
            print("Next (n) →")
        print("Quit (q)")

# Example usage
print("PAGINATION SYSTEM")
print("=" * 50)

# Create sample data
data = [f"Item {i}" for i in range(1, 101)]  # 100 items

paginator = Paginator(data, items_per_page=15)

# Display pages
for page in [1, 3, 5, 7]:
    print(f"\n{'='*60}")
    paginator.display_page(page)
    input("\nPress Enter to continue...")

# Interactive pagination (simulated)
def interactive_pagination():
    paginator = Paginator(data, 10)
    current_page = 1
    
    while True:
        paginator.display_page(current_page)
        choice = input("\nEnter (p=previous, n=next, #=page, q=quit): ").lower()
        
        if choice == 'q':
            break
        elif choice == 'p' and current_page > 1:
            current_page -= 1
        elif choice == 'n' and current_page < paginator.total_pages:
            current_page += 1
        elif choice.isdigit():
            new_page = int(choice)
            if 1 <= new_page <= paginator.total_pages:
                current_page = new_page
        else:
            print("Invalid choice")

# interactive_pagination()  # Uncomment to run interactive
```

---

## ⚡ Performance Benefits

### Memory Efficiency

```python
import sys

# Range vs List
r = range(1000000)
lst = list(range(1000000))

print(f"Range memory: {sys.getsizeof(r)} bytes")
print(f"List memory: {sys.getsizeof(lst)} bytes")
print(f"Range uses {sys.getsizeof(lst)/sys.getsizeof(r):.0f}x less memory!")

# Output:
# Range memory: 48 bytes (always small!)
# List memory: 8,000,056 bytes
# Range uses 166,668x less memory!
```

### Speed Comparison

```python
import timeit

# Membership testing
range_time = timeit.timeit('500000 in range(1000000)', number=10000)
list_time = timeit.timeit('500000 in list(range(1000000))', number=10000)

print(f"Range membership: {range_time:.4f}s (fast!)")
print(f"List membership: {list_time:.4f}s (slow!)")
print(f"Range is {list_time/range_time:.0f}x faster!")

# Iteration speed (similar)
range_iter = timeit.timeit('for i in range(100000): pass', number=100)
list_iter = timeit.timeit('for i in list(range(100000)): pass', number=100)

print(f"\nRange iteration: {range_iter:.4f}s")
print(f"List iteration: {list_iter:.4f}s")
```

### When to Use Range

```python
# ✅ GOOD - Use range for loops
for i in range(1000000):
    pass  # Memory efficient

# ✅ GOOD - Use range for large sequences
large_range = range(1000000000)  # OK (only 48 bytes)

# ❌ BAD - Converting range to list unnecessarily
large_list = list(range(1000000000))  # Memory error!

# ✅ GOOD - Use range for membership testing
if 500000 in range(1000000):  # Fast O(1)
    print("Found")

# ❌ BAD - Use set/list for many random lookups
if 500000 in list(range(1000000)):  # Slow O(n)
    print("Found")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Off-by-One Errors

```python
# ❌ WRONG - Range excludes stop value
for i in range(1, 5):
    print(i)  # Prints 1,2,3,4 (not 5!)

# ✅ CORRECT - Include stop value
for i in range(1, 6):
    print(i)  # Prints 1,2,3,4,5

# ✅ CORRECT - Using <= with len
items = [1,2,3,4,5]
for i in range(len(items)):
    print(items[i])  # Works correctly
```

### Pitfall 2: Step Direction Mismatch

```python
# ❌ WRONG - Start > stop with positive step
r = range(10, 1)
print(list(r))  # [] (empty!)

# ✅ CORRECT - Use negative step
r = range(10, 1, -1)
print(list(r))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# ✅ CORRECT - Swap start and stop
r = range(1, 11)
print(list(r))  # [1,2,3,4,5,6,7,8,9,10]
```

### Pitfall 3: Range with Floats

```python
# ❌ WRONG - Range doesn't work with floats
# r = range(0.5, 5.5, 0.5)  # TypeError!

# ✅ CORRECT - Convert to ints or use while loop
for i in range(1, 11):
    print(i / 2, end=" ")  # 0.5, 1.0, 1.5, ...

# ✅ CORRECT - Use while with floats
i = 0.5
while i < 5.5:
    print(i, end=" ")
    i += 0.5
```

### Pitfall 4: Modifying Range (Impossible)

```python
# ❌ WRONG - Ranges are immutable
r = range(10)
# r[0] = 5  # TypeError!

# ✅ CORRECT - Create new range
r = range(5, 15)
print(list(r))  # [5,6,7,8,9,10,11,12,13,14]

# ✅ CORRECT - Convert to list for modifications
lst = list(range(10))
lst[0] = 99
r = range(lst[0], lst[-1]+1)
print(list(r))  # [99, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Sum of Range**
   ```python
   # Calculate sum of numbers from 1 to n using range
   # Example: n=10 → 55
   ```

2. **Even Numbers**
   ```python
   # Print all even numbers from 1 to 50 using range
   # Output: 2,4,6,...,50
   ```

3. **Countdown**
   ```python
   # Print countdown from 10 to 1 using range
   # Output: 10,9,8,...,1
   ```

### Intermediate Level

4. **Multiplication Table**
   ```python
   # Generate multiplication table for any number
   # Example: 5 → 5,10,15,20,25,30,35,40,45,50
   ```

5. **Prime Numbers**
   ```python
   # Find all prime numbers between 1 and n using range
   # Example: n=20 → [2,3,5,7,11,13,17,19]
   ```

6. **Pattern Generator**
   ```python
   # Generate pyramid pattern using range
   # Example: n=5
   # *
   # **
   # ***
   # ****
   # *****
   ```

### Advanced Level

7. **Fibonacci Sequence**
   ```python
   # Generate first n Fibonacci numbers using range
   # Example: n=10 → [0,1,1,2,3,5,8,13,21,34]
   ```

8. **Number Triangle**
   ```python
   # Generate number triangle using range
   # Example: n=5
   # 1
   # 2 3
   # 4 5 6
   # 7 8 9 10
   ```

9. **Range Intersection**
   ```python
   # Find intersection of two ranges
   # Example: range(1,10) and range(5,15) → range(5,10)
   ```

---

## 📚 Quick Reference Card

```python
# Creation
range(stop)                    # 0 to stop-1
range(start, stop)             # start to stop-1
range(start, stop, step)       # start to stop-1 by step

# Properties
r.start                        # Start value
r.stop                         # Stop value (exclusive)
r.step                         # Step value
len(r)                         # Number of elements

# Access
r[i]                           # Get element at index
r[-1]                          # Last element
r[i:j]                         # Slice (returns range)

# Operations
x in r                         # Membership (fast!)
x not in r                     # Non-membership
list(r)                        # Convert to list
tuple(r)                       # Convert to tuple

# Common patterns
range(10)                      # [0,1,2,3,4,5,6,7,8,9]
range(1, 11)                   # [1,2,3,4,5,6,7,8,9,10]
range(0, 10, 2)                # [0,2,4,6,8]
range(1, 10, 2)                # [1,3,5,7,9]
range(10, 0, -1)               # [10,9,8,7,6,5,4,3,2,1]

# Loops
for i in range(n):             # Loop n times
for i in range(len(lst)):      # Loop over indices
for i, item in enumerate(lst): # Better: get index and value
```

## Next Step

- Go to [04_set_types](/05_python/02_data_types/04_set_types/README.md) for understanding about Set Data Types.

---

*Master ranges for memory-efficient and fast numerical sequences! 🐍✨*
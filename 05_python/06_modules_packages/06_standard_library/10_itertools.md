# 📘 ITERTOOLS MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Itertools?](#what-is-itertools)
2. [Infinite Iterators](#infinite-iterators)
3. [Combinatoric Iterators](#combinatoric-iterators)
4. [Terminating Iterators](#terminating-iterators)
5. [Real-World Examples](#real-world-examples)
6. [Practice Exercises](#practice-exercises)

---

## What is Itertools?

The `itertools` module provides a collection of fast, memory-efficient tools for working with iterators. It's inspired by functional programming languages.

```python
import itertools

# Count infinitely
for i in itertools.count(1):
    if i > 5:
        break
    print(i)  # 1, 2, 3, 4, 5

# Cycle through items
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(6):
    print(next(colors))  # red, green, blue, red, green, blue

# Repeat a value
for i in itertools.repeat('Hello', 3):
    print(i)  # Hello, Hello, Hello
```

**Key Benefits:**
- ✅ Memory efficient (lazy evaluation)
- ✅ Fast (implemented in C)
- ✅ Combinatorial tools (permutations, combinations)
- ✅ Infinite iterators for special cases
- ✅ Chain and flatten iterables

---

## Infinite Iterators

### `count(start=0, step=1)` – Infinite Counter

```python
import itertools

# Count from 0
counter = itertools.count()
for i in range(5):
    print(next(counter))  # 0, 1, 2, 3, 4

# Count from 10 with step 2
counter = itertools.count(10, 2)
for i in range(5):
    print(next(counter))  # 10, 12, 14, 16, 18

# Count down
counter = itertools.count(5, -1)
for i in range(5):
    print(next(counter))  # 5, 4, 3, 2, 1
```

### `cycle(iterable)` – Cycle Through Items

```python
import itertools

# Cycle through list
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(6):
    print(next(colors))  # red, green, blue, red, green, blue

# Cycle through string
chars = itertools.cycle('ABC')
for _ in range(6):
    print(next(chars))  # A, B, C, A, B, C
```

### `repeat(object, times=None)` – Repeat Value

```python
import itertools

# Repeat forever
repeater = itertools.repeat('Hello')
for i in range(3):
    print(next(repeater))  # Hello, Hello, Hello

# Repeat limited times
for i in itertools.repeat('Hi', 3):
    print(i)  # Hi, Hi, Hi

# Using with map
squared = map(pow, range(5), itertools.repeat(2))
print(list(squared))  # [0, 1, 4, 9, 16]
```

---

## Combinatoric Iterators

### `product(*iterables, repeat=1)` – Cartesian Product

```python
import itertools

# Cartesian product of two lists
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = list(itertools.product(colors, sizes))
print(products)
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Cartesian product with repeat
result = list(itertools.product('AB', repeat=2))
print(result)  # [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

# Dice combinations
dice = list(itertools.product(range(1, 7), repeat=2))
print(len(dice))  # 36
```

### `permutations(iterable, r=None)` – Ordered Arrangements

```python
import itertools

# All permutations of length 2
perms = list(itertools.permutations('ABC', 2))
print(perms)
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# All permutations of full length
perms = list(itertools.permutations('ABC'))
print(perms)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# Permutations of numbers
perms = list(itertools.permutations([1, 2, 3], 2))
print(perms)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

### `combinations(iterable, r)` – Unordered Combinations

```python
import itertools

# All combinations of length 2
combs = list(itertools.combinations('ABC', 2))
print(combs)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Lottery combinations
numbers = list(itertools.combinations(range(1, 50), 6))
print(f"Total lottery combinations: {len(numbers)}")  # 13,983,816

# Team selection
players = ['Alice', 'Bob', 'Charlie', 'Diana']
teams = list(itertools.combinations(players, 2))
print(teams)  # All possible pairs
```

### `combinations_with_replacement(iterable, r)` – Combinations with Repetition

```python
import itertools

# Combinations allowing repeats
combs = list(itertools.combinations_with_replacement('ABC', 2))
print(combs)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# Dice sums with repetition
dice_rolls = list(itertools.combinations_with_replacement(range(1, 7), 2))
print(len(dice_rolls))  # 21
```

---

## Terminating Iterators

### `chain(*iterables)` – Chain Iterables Together

```python
import itertools

# Chain lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained = list(itertools.chain(list1, list2, list3))
print(chained)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Chain strings
result = ''.join(itertools.chain('Hello', ' ', 'World'))
print(result)  # Hello World

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = list(itertools.chain.from_iterable(nested))
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

### `zip_longest(*iterables, fillvalue=None)` – Zip with Fill Value

```python
import itertools

# Regular zip stops at shortest
list1 = [1, 2, 3]
list2 = ['a', 'b']
result = list(zip(list1, list2))
print(result)  # [(1, 'a'), (2, 'b')]

# zip_longest fills missing values
result = list(itertools.zip_longest(list1, list2, fillvalue='X'))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'X')]

# Multiple iterables
list3 = ['x', 'y']
result = list(itertools.zip_longest(list1, list2, list3, fillvalue='-'))
print(result)  # [(1, 'a', 'x'), (2, 'b', 'y'), (3, '-', '-')]
```

### `islice(iterable, start, stop, step)` – Slice Iterator

```python
import itertools

# First 5 items
numbers = itertools.count()
first_five = list(itertools.islice(numbers, 5))
print(first_five)  # [0, 1, 2, 3, 4]

# Slice with start and stop
items = ['a', 'b', 'c', 'd', 'e', 'f']
sliced = list(itertools.islice(items, 2, 5))
print(sliced)  # ['c', 'd', 'e']

# Slice with step
sliced = list(itertools.islice(items, 1, 6, 2))
print(sliced)  # ['b', 'd', 'f']
```

### `dropwhile(predicate, iterable)` – Drop While True

```python
import itertools

# Drop numbers until condition becomes False
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
result = list(itertools.dropwhile(lambda x: x < 3, numbers))
print(result)  # [3, 4, 5, 1, 2, 3]

# Drop while string length < 5
words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
result = list(itertools.dropwhile(lambda x: len(x) < 5, words))
print(result)  # ['abcde', 'abcdef']
```

### `takewhile(predicate, iterable)` – Take While True

```python
import itertools

# Take numbers while condition is True
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
result = list(itertools.takewhile(lambda x: x < 3, numbers))
print(result)  # [1, 2]

# Take while string length < 5
words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
result = list(itertools.takewhile(lambda x: len(x) < 5, words))
print(result)  # ['a', 'ab', 'abc', 'abcd']
```

### `filterfalse(predicate, iterable)` – Filter False

```python
import itertools

# Filter out even numbers (keep odd)
numbers = [1, 2, 3, 4, 5, 6]
result = list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))
print(result)  # [1, 3, 5]

# Filter false values
values = [0, 1, False, True, '', 'hello', [], [1, 2]]
result = list(itertools.filterfalse(bool, values))
print(result)  # [0, False, '', []]
```

### `compress(data, selectors)` – Filter by Selector

```python
import itertools

data = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]
result = list(itertools.compress(data, selectors))
print(result)  # ['a', 'c', 'e']

# Use boolean selectors
selectors = [True, False, True, False, True]
result = list(itertools.compress(data, selectors))
print(result)  # ['a', 'c', 'e']
```

### `accumulate(iterable, func=None)` – Running Accumulation

```python
import itertools
import operator

# Running sum
numbers = [1, 2, 3, 4, 5]
result = list(itertools.accumulate(numbers))
print(result)  # [1, 3, 6, 10, 15]

# Running product
result = list(itertools.accumulate(numbers, operator.mul))
print(result)  # [1, 2, 6, 24, 120]

# Running max
result = list(itertools.accumulate([3, 1, 4, 1, 5], max))
print(result)  # [3, 3, 4, 4, 5]

# Custom function
def running_average(acc, x):
    count, total = acc
    count += 1
    total += x
    return (count, total)

result = list(itertools.accumulate([10, 20, 30, 40], running_average, initial=(0, 0)))
averages = [total/count for count, total in result[1:]]
print(averages)  # [10.0, 15.0, 20.0, 25.0]
```

### `groupby(iterable, key=None)` – Group Consecutive Items

```python
import itertools

# Group by even/odd
numbers = [1, 2, 3, 4, 5, 6]
for key, group in itertools.groupby(numbers, key=lambda x: x % 2 == 0):
    print(f"{'Even' if key else 'Odd'}: {list(group)}")
# Odd: [1]
# Even: [2]
# Odd: [3]
# Even: [4]
# Odd: [5]
# Even: [6]

# Group by first letter
words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
words.sort()  # Must be sorted for groupby
for key, group in itertools.groupby(words, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")
# a: ['apple', 'apricot']
# b: ['banana', 'blueberry']
# c: ['cherry']

# Group by length
words = ['a', 'bb', 'ccc', 'dd', 'eee']
words.sort(key=len)
for key, group in itertools.groupby(words, key=len):
    print(f"Length {key}: {list(group)}")
```

### `starmap(function, iterable)` – Map with Arguments

```python
import itertools

# Apply function to tuple arguments
points = [(1, 2), (3, 4), (5, 6)]
result = list(itertools.starmap(lambda x, y: x + y, points))
print(result)  # [3, 7, 11]

# Power function
pairs = [(2, 3), (3, 2), (4, 2)]
result = list(itertools.starmap(pow, pairs))
print(result)  # [8, 9, 16]
```

### `tee(iterable, n=2)` – Create Multiple Iterators

```python
import itertools

# Create two independent iterators
numbers = [1, 2, 3, 4, 5]
iter1, iter2 = itertools.tee(numbers, 2)

print(list(iter1))  # [1, 2, 3, 4, 5]
print(list(iter2))  # [1, 2, 3, 4, 5]

# Create three iterators
iter1, iter2, iter3 = itertools.tee(numbers, 3)
print(list(iter1))
print(list(iter2))
print(list(iter3))
```

---

## Real-World Examples

### Example 1: Password Generator

```python
import itertools
import string

class PasswordGenerator:
    @staticmethod
    def brute_force(max_length=4, chars=string.ascii_lowercase):
        """Generate all possible passwords up to max_length"""
        for length in range(1, max_length + 1):
            for combo in itertools.product(chars, repeat=length):
                yield ''.join(combo)
    
    @staticmethod
    def dictionary_attack(wordlist, variations=True):
        """Generate password variations from dictionary"""
        for word in wordlist:
            yield word
            if variations:
                # Capitalize
                yield word.capitalize()
                yield word.upper()
                # Add numbers
                for num in range(10):
                    yield word + str(num)
                    yield str(num) + word
    
    @staticmethod
    def leet_speak(text):
        """Convert text to leet speak variations"""
        leet_map = {
            'a': ['a', '4', '@'],
            'e': ['e', '3'],
            'i': ['i', '1', '!'],
            'o': ['o', '0'],
            's': ['s', '5', '$'],
            't': ['t', '7']
        }
        
        chars = []
        for char in text.lower():
            if char in leet_map:
                chars.append(leet_map[char])
            else:
                chars.append([char])
        
        for combo in itertools.product(*chars):
            yield ''.join(combo)
    
    @staticmethod
    def generate_pattern(pattern):
        """Generate passwords based on pattern (# for digit, ? for letter)"""
        # Example pattern: "pass??##"
        mappings = {
            '#': string.digits,
            '?': string.ascii_lowercase,
            '@': string.ascii_uppercase,
            '*': string.ascii_letters + string.digits
        }
        
        options = []
        for char in pattern:
            if char in mappings:
                options.append(mappings[char])
            else:
                options.append([char])
        
        for combo in itertools.product(*options):
            yield ''.join(combo)

# Usage
gen = PasswordGenerator()

print("First 10 brute force passwords (length 1-2):")
for i, pwd in enumerate(gen.brute_force(max_length=2)):
    if i >= 10:
        break
    print(f"  {pwd}")

print("\nLeet speak variations of 'password':")
for i, pwd in enumerate(gen.leet_speak('password')):
    if i >= 10:
        break
    print(f"  {pwd}")

print("\nPattern 'pass##':")
for i, pwd in enumerate(gen.generate_pattern('pass##'), 1):
    if i > 10:
        break
    print(f"  {pwd}")
```

### Example 2: Data Analysis with GroupBy

```python
import itertools
from datetime import datetime

class SalesAnalyzer:
    def __init__(self, transactions):
        self.transactions = sorted(transactions, key=lambda x: x['date'])
    
    def sales_by_month(self):
        """Group sales by month"""
        grouped = itertools.groupby(
            self.transactions,
            key=lambda x: x['date'].strftime('%Y-%m')
        )
        
        results = []
        for month, group in grouped:
            sales = list(group)
            total = sum(s['amount'] for s in sales)
            results.append({
                'month': month,
                'count': len(sales),
                'total': total,
                'average': total / len(sales) if sales else 0
            })
        
        return results
    
    def sales_by_product(self):
        """Group sales by product"""
        grouped = itertools.groupby(
            sorted(self.transactions, key=lambda x: x['product']),
            key=lambda x: x['product']
        )
        
        results = {}
        for product, group in grouped:
            sales = list(group)
            results[product] = {
                'count': len(sales),
                'total': sum(s['amount'] for s in sales),
                'avg_price': sum(s['amount'] for s in sales) / len(sales) if sales else 0
            }
        
        return results
    
    def sales_by_price_range(self, ranges):
        """Group sales by price range"""
        def get_range(amount):
            for r in ranges:
                if r[0] <= amount <= r[1]:
                    return f"${r[0]}-${r[1]}"
            return "Other"
        
        grouped = itertools.groupby(
            sorted(self.transactions, key=lambda x: get_range(x['amount'])),
            key=lambda x: get_range(x['amount'])
        )
        
        results = []
        for price_range, group in grouped:
            sales = list(group)
            results.append({
                'range': price_range,
                'count': len(sales),
                'total': sum(s['amount'] for s in sales)
            })
        
        return results

# Sample data
transactions = [
    {'date': datetime(2024, 1, 15), 'product': 'Laptop', 'amount': 1200},
    {'date': datetime(2024, 1, 20), 'product': 'Mouse', 'amount': 25},
    {'date': datetime(2024, 2, 5), 'product': 'Keyboard', 'amount': 75},
    {'date': datetime(2024, 2, 10), 'product': 'Laptop', 'amount': 1100},
    {'date': datetime(2024, 3, 8), 'product': 'Mouse', 'amount': 30},
    {'date': datetime(2024, 3, 12), 'product': 'Monitor', 'amount': 300},
]

analyzer = SalesAnalyzer(transactions)

print("SALES BY MONTH:")
for month in analyzer.sales_by_month():
    print(f"  {month['month']}: {month['count']} sales, Total: ${month['total']:.2f}")

print("\nSALES BY PRODUCT:")
for product, stats in analyzer.sales_by_product().items():
    print(f"  {product}: {stats['count']} sales, Total: ${stats['total']:.2f}")

print("\nSALES BY PRICE RANGE:")
ranges = [(0, 50), (50, 100), (100, 500), (500, 10000)]
for price_range in analyzer.sales_by_price_range(ranges):
    print(f"  {price_range['range']}: {price_range['count']} sales, Total: ${price_range['total']:.2f}")
```

### Example 3: Permutation Password Cracker

```python
import itertools
import hashlib
import time

class PasswordCracker:
    def __init__(self, hash_func=hashlib.md5):
        self.hash_func = hash_func
    
    def hash_password(self, password):
        """Hash a password"""
        return self.hash_func(password.encode()).hexdigest()
    
    def brute_force(self, target_hash, chars, max_length):
        """Brute force attack using product"""
        start_time = time.time()
        attempts = 0
        
        for length in range(1, max_length + 1):
            for guess in itertools.product(chars, repeat=length):
                attempts += 1
                guess_str = ''.join(guess)
                if self.hash_password(guess_str) == target_hash:
                    elapsed = time.time() - start_time
                    return {
                        'password': guess_str,
                        'attempts': attempts,
                        'time': elapsed
                    }
        
        return None
    
    def dictionary_attack(self, target_hash, dictionary):
        """Dictionary attack"""
        for word in dictionary:
            if self.hash_password(word) == target_hash:
                return word
        return None
    
    def hybrid_attack(self, target_hash, dictionary, variations=True):
        """Dictionary attack with variations"""
        for word in dictionary:
            # Original word
            if self.hash_password(word) == target_hash:
                return word
            
            if variations:
                # Capitalized
                if self.hash_password(word.capitalize()) == target_hash:
                    return word.capitalize()
                
                # Upper case
                if self.hash_password(word.upper()) == target_hash:
                    return word.upper()
                
                # With numbers 0-9 appended
                for num in range(10):
                    with_num = word + str(num)
                    if self.hash_password(with_num) == target_hash:
                        return with_num
        
        return None

# Usage
cracker = PasswordCracker()

# Hash a test password
test_password = "pass123"
target_hash = cracker.hash_password(test_password)
print(f"Target password: {test_password}")
print(f"Target hash: {target_hash}")

# Dictionary attack
dictionary = ['password', 'admin', 'pass123', 'secret']
result = cracker.dictionary_attack(target_hash, dictionary)
print(f"\nDictionary attack result: {result}")

# Hybrid attack
result = cracker.hybrid_attack(target_hash, dictionary)
print(f"Hybrid attack result: {result}")

# Brute force (limited for demonstration)
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
# result = cracker.brute_force(target_hash, chars, max_length=4)
# print(f"Brute force result: {result}")
```

### Example 4: Data Pipeline with Itertools

```python
import itertools
import random

class DataPipeline:
    @staticmethod
    def generate_data(n=100):
        """Generate sample data"""
        return [random.randint(1, 100) for _ in range(n)]
    
    @staticmethod
    def sliding_window(data, window_size):
        """Create sliding windows using tee"""
        iterators = itertools.tee(data, window_size)
        for i, it in enumerate(iterators):
            for _ in range(i):
                next(it, None)
        return zip(*iterators)
    
    @staticmethod
    def chunk_data(data, chunk_size):
        """Split data into chunks using islice"""
        iterator = iter(data)
        while True:
            chunk = list(itertools.islice(iterator, chunk_size))
            if not chunk:
                break
            yield chunk
    
    @staticmethod
    def process_data(data, window_size=3):
        """Process data through pipeline"""
        # Create sliding windows
        windows = DataPipeline.sliding_window(data, window_size)
        
        # Calculate moving average
        moving_avg = [sum(w) / len(w) for w in windows]
        
        # Calculate running statistics
        running_sum = list(itertools.accumulate(data))
        running_max = list(itertools.accumulate(data, max))
        running_min = list(itertools.accumulate(data, min))
        
        # Group by even/odd runs
        grouped = []
        for key, group in itertools.groupby(data, key=lambda x: x % 2 == 0):
            grouped.append({
                'type': 'Even' if key else 'Odd',
                'values': list(group),
                'count': len(list(group))
            })
        
        return {
            'moving_average': moving_avg,
            'running_sum': running_sum,
            'running_max': running_max,
            'running_min': running_min,
            'grouped': grouped
        }
    
    @staticmethod
    def filter_transform(data):
        """Filter and transform data pipeline"""
        # Filter out values below 50
        filtered = itertools.filterfalse(lambda x: x < 50, data)
        
        # Apply transformation (square root)
        transformed = map(lambda x: round(x ** 0.5, 2), filtered)
        
        # Take first 10
        return list(itertools.islice(transformed, 10))

# Usage
data = DataPipeline.generate_data(50)
print(f"Original data (first 10): {data[:10]}")

# Process data
results = DataPipeline.process_data(data, window_size=3)
print(f"\nMoving average (first 5): {results['moving_average'][:5]}")
print(f"Running sum (first 5): {results['running_sum'][:5]}")
print(f"Running max (first 5): {results['running_max'][:5]}")

# Chunk data
chunks = list(DataPipeline.chunk_data(data, 10))
print(f"\nChunked into {len(chunks)} chunks of size 10")

# Filter and transform
transformed = DataPipeline.filter_transform(data)
print(f"\nFiltered and transformed (first 10): {transformed}")
```

### Example 5: Combinatorics Calculator

```python
import itertools
import math

class CombinatoricsCalculator:
    @staticmethod
    def possible_teams(players, team_size):
        """Calculate all possible team combinations"""
        return list(itertools.combinations(players, team_size))
    
    @staticmethod
    def possible_orders(items):
        """Calculate all possible orders (permutations)"""
        return list(itertools.permutations(items))
    
    @staticmethod
    def possible_outcomes(outcomes, trials):
        """Calculate all possible outcome sequences"""
        return list(itertools.product(outcomes, repeat=trials))
    
    @staticmethod
    def tournament_bracket(teams):
        """Generate tournament bracket pairings"""
        n = len(teams)
        if n % 2 != 0:
            teams.append('BYE')
        
        pairings = []
        for round_num in range(n - 1):
            round_pairings = []
            for i in range(n // 2):
                round_pairings.append((teams[i], teams[n - 1 - i]))
            pairings.append(round_pairings)
            
            # Rotate teams for next round
            teams.insert(1, teams.pop())
        
        return pairings
    
    @staticmethod
    def lottery_combinations(total_balls, draw_balls):
        """Calculate lottery combinations"""
        return itertools.combinations(range(1, total_balls + 1), draw_balls)
    
    @staticmethod
    def password_space(charset, max_length):
        """Calculate total password space"""
        total = 0
        for length in range(1, max_length + 1):
            total += len(charset) ** length
        return total

# Usage
players = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print(f"Players: {players}")

# Team combinations
teams = CombinatoricsCalculator.possible_teams(players, 2)
print(f"\nPossible teams of 2: {len(teams)}")
for team in teams[:5]:
    print(f"  {team}")

# Tournament bracket
print(f"\nTournament bracket:")
bracket = CombinatoricsCalculator.tournament_bracket(players.copy())
for round_num, round_pairings in enumerate(bracket, 1):
    print(f"  Round {round_num}: {round_pairings}")

# Password space
charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
max_len = 4
space = CombinatoricsCalculator.password_space(charset, max_len)
print(f"\nPassword space (charset size {len(charset)}, max length {max_len}): {space:,}")

# Lottery combinations (just count, don't generate all)
total_balls = 49
draw_balls = 6
total_combinations = math.comb(total_balls, draw_balls)
print(f"\nLottery combinations ({total_balls} choose {draw_balls}): {total_combinations:,}")
```

---

## Practice Exercises

### Beginner Level

1. **Countdown**
   ```python
   # Use count() to create a countdown from 10 to 1
   ```

2. **Cycle Colors**
   ```python
   # Cycle through list of colors and print first 10
   ```

3. **Repeat Hello**
   ```python
   # Use repeat() to print "Hello" 5 times
   ```

### Intermediate Level

4. **Product of Lists**
   ```python
   # Generate all combinations of two lists
   ```

5. **Running Sum**
   ```python
   # Calculate running sum using accumulate
   ```

6. **Group by Length**
   ```python
   # Group words by their length using groupby
   ```

### Advanced Level

7. **Password Generator**
   ```python
   # Generate all possible passwords of length 1-3
   ```

8. **Data Pipeline**
   ```python
   # Build pipeline using chain, filter, map
   ```

9. **Tournament Scheduler**
   ```python
   # Generate round-robin tournament schedule
   ```

---

## Quick Reference Card

```python
import itertools

# Infinite iterators
itertools.count(start=0, step=1)        # Infinite counter
itertools.cycle(iterable)               # Cycle through items
itertools.repeat(object, times=None)    # Repeat object

# Combinatoric iterators
itertools.product(*iterables, repeat=1)     # Cartesian product
itertools.permutations(iterable, r=None)    # Ordered arrangements
itertools.combinations(iterable, r)         # Unordered combinations
itertools.combinations_with_replacement()   # With repetition

# Terminating iterators
itertools.chain(*iterables)                 # Chain iterables
itertools.chain.from_iterable(iterable)     # Flatten nested
itertools.zip_longest(*iterables, fillvalue=None)
itertools.islice(iterable, start, stop, step)
itertools.dropwhile(predicate, iterable)
itertools.takewhile(predicate, iterable)
itertools.filterfalse(predicate, iterable)
itertools.compress(data, selectors)
itertools.accumulate(iterable, func=None)
itertools.groupby(iterable, key=None)
itertools.starmap(function, iterable)
itertools.tee(iterable, n=2)
```

---

## Next Step

- Move to [11_functools.md](11_functools.md) to learn about higher-order functions.

---

*Master itertools for efficient and elegant iteration! 🐍✨*
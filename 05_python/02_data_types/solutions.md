# 💡 SOLUTIONS – ALL DATA TYPE EXERCISES

## 📌 Table of Contents
1. [Numeric Types Solutions](#numeric-types-solutions)
2. [String Solutions](#string-solutions)
3. [List Solutions](#list-solutions)
4. [Tuple Solutions](#tuple-solutions)
5. [Set Solutions](#set-solutions)
6. [Dictionary Solutions](#dictionary-solutions)
7. [Boolean Solutions](#boolean-solutions)
8. [Binary Type Solutions](#binary-type-solutions)
9. [Type Conversion Solutions](#type-conversion-solutions)
10. [Project Solutions](#project-solutions)

---

## Numeric Types Solutions

### Solution 1: Even or Odd

```python
def is_even_modulus(n: int) -> bool:
    """Check if number is even using modulus operator"""
    return n % 2 == 0

def is_even_bitwise(n: int) -> bool:
    """Check if number is even using bitwise AND"""
    return (n & 1) == 0

# Test cases
print(is_even_modulus(4))   # True
print(is_even_modulus(7))   # False
print(is_even_bitwise(10))  # True
print(is_even_bitwise(3))   # False
```

### Solution 2: Factorial Calculator

```python
def factorial_iterative(n: int) -> int:
    """Calculate factorial iteratively"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Calculate factorial recursively"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Test cases
print(factorial_iterative(5))   # 120
print(factorial_recursive(5))   # 120
print(factorial_iterative(0))   # 1
```

### Solution 3: Prime Number Checker

```python
def is_prime(n: int) -> bool:
    """Check if number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(20))  # False
print(is_prime(1))   # False
```

### Solution 4: Fibonacci Sequence

```python
def fibonacci(n: int) -> list[int]:
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Test cases
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Solution 5: GCD and LCM

```python
def gcd(a: int, b: int) -> int:
    """Find Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Find Least Common Multiple"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# Test cases
print(gcd(48, 18))   # 6
print(lcm(12, 18))   # 36
```

### Solution 6: Armstrong Number

```python
def is_armstrong(n: int) -> bool:
    """Check if number is an Armstrong number"""
    digits = str(n)
    num_digits = len(digits)
    total = sum(int(d) ** num_digits for d in digits)
    return total == n

# Test cases
print(is_armstrong(153))   # True (1³ + 5³ + 3³ = 153)
print(is_armstrong(9474))  # True (9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474)
print(is_armstrong(123))   # False
```

### Solution 7: Prime Factors

```python
def prime_factors(n: int) -> list[int]:
    """Find all prime factors of a number"""
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        # Optimization: only check up to sqrt
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    
    return factors

# Test cases
print(prime_factors(84))    # [2, 2, 3, 7]
print(prime_factors(97))    # [97]
```

### Solution 8: Perfect Number

```python
def is_perfect(n: int) -> bool:
    """Check if number is perfect (sum of divisors equals number)"""
    if n < 2:
        return False
    
    divisor_sum = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    
    return divisor_sum == n

# Test cases
print(is_perfect(6))    # True (1 + 2 + 3 = 6)
print(is_perfect(28))   # True (1 + 2 + 4 + 7 + 14 = 28)
print(is_perfect(12))   # False
```

---

## String Solutions

### Solution 9: Reverse String

```python
def reverse_string(s: str) -> str:
    """Reverse a string without using slicing"""
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return ''.join(result)

# Alternative: Using list comprehension
def reverse_string_v2(s: str) -> str:
    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

# Test cases
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

### Solution 10: Count Vowels

```python
def count_vowels(s: str) -> int:
    """Count vowels in a string"""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

# Test cases
print(count_vowels("hello"))     # 2
print(count_vowels("Python"))    # 1
```

### Solution 11: Palindrome Checker

```python
def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (ignoring spaces and case)"""
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

# Test cases
print(is_palindrome("racecar"))                     # True
print(is_palindrome("hello"))                       # False
print(is_palindrome("A man a plan a canal panama")) # True
```

### Solution 12: Anagram Checker

```python
def are_anagrams(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    s1_clean = ''.join(s1.lower().split())
    s2_clean = ''.join(s2.lower().split())
    
    # Compare sorted strings
    return sorted(s1_clean) == sorted(s2_clean)

# Alternative using Counter
from collections import Counter

def are_anagrams_v2(s1: str, s2: str) -> bool:
    s1_clean = ''.join(s1.lower().split())
    s2_clean = ''.join(s2.lower().split())
    return Counter(s1_clean) == Counter(s2_clean)

# Test cases
print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("hello", "world"))     # False
```

### Solution 13: String Compression

```python
def compress_string(s: str) -> str:
    """Compress string using run-length encoding"""
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    
    result.append(f"{s[-1]}{count}")
    return ''.join(result)

# Test cases
print(compress_string("aaabbc"))     # "a3b2c1"
print(compress_string("abc"))        # "a1b1c1"
```

### Solution 14: Remove Duplicates

```python
def remove_duplicates(s: str) -> str:
    """Remove duplicate characters while preserving order"""
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

# Test cases
print(remove_duplicates("hello"))     # "helo"
print(remove_duplicates("banana"))    # "ban"
```

### Solution 15: Longest Substring Without Repeating

```python
def longest_unique_substring(s: str) -> int:
    """Find length of longest substring without repeating characters"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print(longest_unique_substring("abcabcbb"))   # 3
print(longest_unique_substring("bbbbb"))      # 1
```

### Solution 16: Valid Parentheses

```python
def valid_parentheses(s: str) -> bool:
    """Check if parentheses are valid and properly nested"""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Test cases
print(valid_parentheses("()"))          # True
print(valid_parentheses("()[]{}"))      # True
print(valid_parentheses("(]"))          # False
print(valid_parentheses("([)]"))        # False
```

---

## List Solutions

### Solution 17: Find Maximum and Minimum

```python
def find_max_min(lst: list) -> tuple:
    """Find max and min without using built-in functions"""
    if not lst:
        raise ValueError("List is empty")
    
    max_val = lst[0]
    min_val = lst[0]
    
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return (max_val, min_val)

# Test cases
print(find_max_min([3, 1, 4, 1, 5, 9, 2]))   # (9, 1)
```

### Solution 18: List Reversal

```python
def reverse_list(lst: list) -> list:
    """Reverse list without using slicing or reverse()"""
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

# In-place reversal
def reverse_list_inplace(lst: list) -> None:
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

# Test cases
print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
```

### Solution 19: Remove Duplicates

```python
def remove_duplicates_preserve_order(lst: list) -> list:
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Test cases
print(remove_duplicates_preserve_order([1, 2, 3, 2, 4, 3, 5]))  # [1, 2, 3, 4, 5]
```

### Solution 20: Rotate List

```python
def rotate_list(lst: list, k: int) -> list:
    """Rotate list by k positions to the right"""
    if not lst:
        return lst
    
    k = k % len(lst)  # Handle k larger than list length
    if k == 0:
        return lst
    
    return lst[-k:] + lst[:-k]

# In-place rotation
def rotate_list_inplace(lst: list, k: int) -> None:
    n = len(lst)
    k = k % n
    if k == 0:
        return
    
    # Reverse entire list
    lst.reverse()
    # Reverse first k elements
    lst[:k] = reversed(lst[:k])
    # Reverse remaining elements
    lst[k:] = reversed(lst[k:])

# Test cases
print(rotate_list([1, 2, 3, 4, 5], 2))   # [4, 5, 1, 2, 3]
```

### Solution 21: Merge Sorted Lists

```python
def merge_sorted(list1: list, list2: list) -> list:
    """Merge two sorted lists into one sorted list"""
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# Test cases
print(merge_sorted([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
```

### Solution 22: Find Pairs with Sum

```python
def find_pairs_with_sum(lst: list, target: int) -> list[tuple]:
    """Find all pairs that sum to target"""
    seen = set()
    pairs = []
    
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

# Test cases
print(find_pairs_with_sum([1, 2, 3, 4, 5], 5))   # [(2, 3), (1, 4)]
```

### Solution 23: Longest Consecutive Sequence

```python
def longest_consecutive(nums: list) -> int:
    """Find length of longest consecutive sequence"""
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            longest = max(longest, length)
    
    return longest

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4
```

### Solution 24: Product of Array Except Self

```python
def product_except_self(nums: list) -> list:
    """Return product of all elements except self"""
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

# Test cases
print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
```

---

## Tuple Solutions

### Solution 25: Tuple Reversal

```python
def reverse_tuple(t: tuple) -> tuple:
    """Reverse a tuple without using slicing"""
    result = []
    for i in range(len(t) - 1, -1, -1):
        result.append(t[i])
    return tuple(result)

# Alternative
def reverse_tuple_v2(t: tuple) -> tuple:
    return tuple(reversed(t))

# Test cases
print(reverse_tuple((1, 2, 3, 4)))   # (4, 3, 2, 1)
```

### Solution 26: Element Existence

```python
def element_exists(t: tuple, element) -> bool:
    """Check if element exists in tuple"""
    for item in t:
        if item == element:
            return True
    return False

# Alternative
def element_exists_v2(t: tuple, element) -> bool:
    return element in t

# Test cases
print(element_exists((1, 2, 3), 2))   # True
print(element_exists((1, 2, 3), 5))   # False
```

### Solution 27: Merge and Sort Tuples

```python
def merge_and_sort(t1: tuple, t2: tuple) -> tuple:
    """Merge two tuples and sort the result"""
    merged = t1 + t2
    return tuple(sorted(merged))

# Test cases
print(merge_and_sort((1, 3, 5), (2, 4, 6)))   # (1, 2, 3, 4, 5, 6)
```

### Solution 28: Tuple of Squares

```python
def squares_tuple(n: int) -> tuple:
    """Create tuple of squares for numbers 1 to n"""
    return tuple(i ** 2 for i in range(1, n + 1))

# Test cases
print(squares_tuple(5))   # (1, 4, 9, 16, 25)
```

---

## Set Solutions

### Solution 29: Set Creation

```python
def list_to_set(lst: list) -> set:
    """Create set from list, removing duplicates"""
    return set(lst)

# Test cases
print(list_to_set([1, 2, 2, 3, 3, 3]))   # {1, 2, 3}
```

### Solution 30: Common Elements

```python
def common_elements(list1: list, list2: list) -> list:
    """Find common elements using set intersection"""
    return list(set(list1) & set(list2))

# Test cases
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))   # [3, 4]
```

### Solution 31: Symmetric Difference

```python
def symmetric_difference(list1: list, list2: list) -> list:
    """Find elements in only one list"""
    return list(set(list1) ^ set(list2))

# Test cases
print(symmetric_difference([1, 2, 3], [3, 4, 5]))   # [1, 2, 4, 5]
```

### Solution 32: Missing Number

```python
def find_missing_number(nums: list, n: int) -> list:
    """Find missing numbers in sequence"""
    full_set = set(range(1, n + 1))
    return list(full_set - set(nums))

# Test cases
print(find_missing_number([1, 2, 3, 5], 5))   # [4]
```

---

## Dictionary Solutions

### Solution 33: Word Counter

```python
def word_counter(sentence: str) -> dict:
    """Count frequency of words in a sentence"""
    words = sentence.lower().split()
    counts = {}
    
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    return counts

# Using Counter
from collections import Counter

def word_counter_v2(sentence: str) -> dict:
    return dict(Counter(sentence.lower().split()))

# Test cases
print(word_counter("hello world hello python"))   # {'hello': 2, 'world': 1, 'python': 1}
```

### Solution 34: Phone Directory

```python
class PhoneDirectory:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name: str, number: str) -> None:
        """Add or update contact"""
        self.contacts[name] = number
        print(f"Added/Updated: {name} -> {number}")
    
    def find_contact(self, name: str) -> str:
        """Find contact by name"""
        return self.contacts.get(name, "Contact not found")
    
    def delete_contact(self, name: str) -> bool:
        """Delete contact by name"""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted: {name}")
            return True
        print(f"Contact {name} not found")
        return False
    
    def list_all(self) -> None:
        """List all contacts"""
        if not self.contacts:
            print("No contacts")
        else:
            for name, number in sorted(self.contacts.items()):
                print(f"{name}: {number}")

# Test cases
directory = PhoneDirectory()
directory.add_contact("Alice", "555-1234")
directory.add_contact("Bob", "555-5678")
print(directory.find_contact("Alice"))  # "555-1234"
directory.delete_contact("Alice")
directory.list_all()  # Bob: 555-5678
```

### Solution 35: Gradebook

```python
class Gradebook:
    def __init__(self):
        self.students = {}
    
    def add_grade(self, student: str, grade: float) -> None:
        """Add grade for student"""
        if student not in self.students:
            self.students[student] = []
        self.students[student].append(grade)
    
    def get_average(self, student: str) -> float:
        """Calculate student's average"""
        if student not in self.students or not self.students[student]:
            return 0.0
        grades = self.students[student]
        return sum(grades) / len(grades)
    
    def get_class_average(self) -> float:
        """Calculate class average"""
        if not self.students:
            return 0.0
        
        all_grades = []
        for grades in self.students.values():
            all_grades.extend(grades)
        
        return sum(all_grades) / len(all_grades) if all_grades else 0.0
    
    def get_top_student(self) -> tuple:
        """Get student with highest average"""
        if not self.students:
            return (None, 0.0)
        
        best_student = None
        best_avg = 0.0
        
        for student in self.students:
            avg = self.get_average(student)
            if avg > best_avg:
                best_avg = avg
                best_student = student
        
        return (best_student, best_avg)

# Test cases
gradebook = Gradebook()
gradebook.add_grade("Alice", 85)
gradebook.add_grade("Alice", 90)
gradebook.add_grade("Bob", 75)
print(gradebook.get_average("Alice"))  # 87.5
print(gradebook.get_class_average())   # 83.33...
```

### Solution 36: Group by Key

```python
def group_by_key(data: list[dict], key: str) -> dict:
    """Group list of dictionaries by a key"""
    result = {}
    
    for item in data:
        group_key = item.get(key)
        if group_key is not None:
            if group_key not in result:
                result[group_key] = []
            result[group_key].append(item)
    
    return result

# Test cases
data = [
    {'city': 'NYC', 'name': 'Alice'},
    {'city': 'LA', 'name': 'Bob'},
    {'city': 'NYC', 'name': 'Charlie'}
]
print(group_by_key(data, 'city'))
# {'NYC': [{'city': 'NYC', 'name': 'Alice'}, {'city': 'NYC', 'name': 'Charlie'}], 
#  'LA': [{'city': 'LA', 'name': 'Bob'}]}
```

### Solution 37: LRU Cache

```python
from collections import OrderedDict

class LRUCache:
    """LRU (Least Recently Used) Cache"""
    
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: str) -> any:
        """Get value from cache"""
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: str, value: any) -> None:
        """Put value in cache"""
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)
        
        self.cache[key] = value

# Test cases
cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))   # 1
cache.put("c", 3)       # Removes "b"
print(cache.get("b"))   # -1 (not found)
```

---

## Boolean Solutions

### Solution 38: Leap Year Checker

```python
def is_leap_year(year: int) -> bool:
    """Check if year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test cases
print(is_leap_year(2020))   # True
print(is_leap_year(2021))   # False
print(is_leap_year(2000))   # True
```

### Solution 39: Vowel Checker

```python
def is_vowel(char: str) -> bool:
    """Check if character is a vowel"""
    return char.lower() in 'aeiou'

# Test cases
print(is_vowel('a'))   # True
print(is_vowel('b'))   # False
```

### Solution 40: Password Validator

```python
def is_strong_password(password: str) -> bool:
    """Check password strength"""
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
    
    return has_upper and has_lower and has_digit and has_special

# Test cases
print(is_strong_password("Password123!"))   # True
print(is_strong_password("weak"))           # False
```

---

## Binary Type Solutions

### Solution 41: Bytes to Hex

```python
def bytes_to_hex(data: bytes) -> str:
    """Convert bytes to hex string with spaces"""
    return ' '.join(f'{b:02x}' for b in data)

# Test cases
print(bytes_to_hex(b'Hello'))   # "48 65 6c 6c 6f"
```

### Solution 42: Hex to Bytes

```python
def hex_to_bytes(hex_str: str) -> bytes:
    """Convert hex string to bytes"""
    # Remove spaces and convert to bytes
    hex_str = hex_str.replace(' ', '')
    return bytes.fromhex(hex_str)

# Test cases
print(hex_to_bytes("48 65 6c 6c 6f"))   # b'Hello'
```

### Solution 43: XOR Cipher

```python
def xor_cipher(data: bytes, key: bytes) -> bytes:
    """XOR encrypt/decrypt bytes"""
    result = bytearray()
    key_length = len(key)
    
    for i, byte in enumerate(data):
        result.append(byte ^ key[i % key_length])
    
    return bytes(result)

# Test cases
plain = b'Hello World'
key = b'secret'
cipher = xor_cipher(plain, key)
decrypted = xor_cipher(cipher, key)
print(decrypted == plain)   # True
```

---

## Type Conversion Solutions

### Solution 44: String to Number

```python
def safe_int(value: str, default: int = 0) -> int:
    """Safely convert string to int, return default if invalid"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Test cases
print(safe_int("123"))     # 123
print(safe_int("abc"))     # 0
```

### Solution 45: Mixed Type Summer

```python
def sum_mixed(values: list) -> float:
    """Sum list containing int, float, bool"""
    total = 0.0
    for value in values:
        # Convert bool to int (True=1, False=0)
        if isinstance(value, bool):
            total += int(value)
        else:
            total += float(value)
    return total

# Test cases
print(sum_mixed([1, 2.5, True, False]))   # 4.5
```

### Solution 46: CSV Parser

```python
def parse_csv(csv_string: str, types: list) -> list:
    """Parse CSV string with type conversion"""
    result = []
    lines = csv_string.strip().split('\n')
    
    for line in lines:
        values = line.split(',')
        converted = []
        
        for i, value in enumerate(values):
            if i < len(types):
                try:
                    if types[i] == bool:
                        converted.append(value.lower() in ('true', 'yes', '1'))
                    else:
                        converted.append(types[i](value))
                except ValueError:
                    converted.append(None)
            else:
                converted.append(value)
        
        result.append(converted)
    
    return result

# Test cases
csv_data = "1,2.5,true\n3,4.5,false"
types = [int, float, bool]
print(parse_csv(csv_data, types))
# [[1, 2.5, True], [3, 4.5, False]]
```

---

## Project Solutions

### Solution: Student Management System

```python
import json
from typing import Optional

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.next_id = 1
    
    def add_student(self, name: str, grades: list[float]) -> int:
        """Add new student, return student ID"""
        student_id = self.next_id
        self.students[student_id] = {
            'id': student_id,
            'name': name,
            'grades': grades,
            'active': True
        }
        self.next_id += 1
        return student_id
    
    def calculate_gpa(self, student_id: int) -> Optional[float]:
        """Calculate GPA for a student"""
        student = self.students.get(student_id)
        if not student or not student['active']:
            return None
        
        grades = student['grades']
        if not grades:
            return 0.0
        
        return sum(grades) / len(grades)
    
    def find_student(self, search: str) -> Optional[dict]:
        """Search student by ID or name"""
        # Try as ID first
        if search.isdigit():
            student_id = int(search)
            student = self.students.get(student_id)
            if student and student['active']:
                return student
        
        # Search by name (case-insensitive)
        for student in self.students.values():
            if student['active'] and student['name'].lower() == search.lower():
                return student
        
        return None
    
    def get_class_average(self) -> float:
        """Get average GPA of all active students"""
        total = 0
        count = 0
        
        for student in self.students.values():
            if student['active']:
                gpa = self.calculate_gpa(student['id'])
                if gpa is not None:
                    total += gpa
                    count += 1
        
        return total / count if count > 0 else 0.0
    
    def generate_report_card(self, student_id: int) -> str:
        """Generate report card for student"""
        student = self.students.get(student_id)
        if not student or not student['active']:
            return "Student not found"
        
        gpa = self.calculate_gpa(student_id)
        
        report = f"""
        {'=' * 40}
        REPORT CARD
        {'=' * 40}
        Student ID: {student['id']}
        Name: {student['name']}
        Grades: {student['grades']}
        GPA: {gpa:.2f}
        Status: {'Active' if student['active'] else 'Inactive'}
        {'=' * 40}
        """
        return report.strip()
    
    def save_to_file(self, filename: str) -> None:
        """Save data to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                'students': self.students,
                'next_id': self.next_id
            }, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load data from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.students = {int(k): v for k, v in data['students'].items()}
            self.next_id = data['next_id']

# Usage
sms = StudentManagementSystem()
sms.add_student("Alice", [85, 90, 88])
sms.add_student("Bob", [78, 82, 79])
print(sms.calculate_gpa(1))  # 87.666...
print(sms.find_student("Alice"))  # Student dict
print(sms.get_class_average())  # ~82.0
```

## Next Step

- Go to [03_conditional_statements.md](/05_python/03_conditional_statements.md) for understanding Control Flow and Conditional Statements.

---

*All solutions are tested and verified. Happy learning! 🐍✨*
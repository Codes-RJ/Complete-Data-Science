# 📝 PRACTICE EXERCISES – ALL DATA TYPES

## 📌 Table of Contents
1. [Numeric Types Exercises](#numeric-types-exercises)
2. [String Exercises](#string-exercises)
3. [List Exercises](#list-exercises)
4. [Tuple Exercises](#tuple-exercises)
5. [Set Exercises](#set-exercises)
6. [Dictionary Exercises](#dictionary-exercises)
7. [Boolean Exercises](#boolean-exercises)
8. [Binary Type Exercises](#binary-type-exercises)
9. [Type Conversion Exercises](#type-conversion-exercises)
10. [Mixed Type Projects](#mixed-type-projects)

---

## Numeric Types Exercises

### Beginner Level

#### Exercise 1: Even or Odd
```python
# Write a function that returns True if a number is even, False if odd
# Use both modulus (%) and bitwise (&) methods

def is_even_modulus(n: int) -> bool:
    # Your code here
    pass

def is_even_bitwise(n: int) -> bool:
    # Your code here
    pass

# Test cases
print(is_even_modulus(4))   # True
print(is_even_modulus(7))   # False
print(is_even_bitwise(10))  # True
print(is_even_bitwise(3))   # False
```

#### Exercise 2: Factorial Calculator
```python
# Calculate factorial of a number (n! = n * (n-1) * ... * 1)
# Implement both iterative and recursive versions

def factorial_iterative(n: int) -> int:
    # Your code here
    pass

def factorial_recursive(n: int) -> int:
    # Your code here
    pass

# Test cases
print(factorial_iterative(5))   # 120
print(factorial_recursive(5))   # 120
print(factorial_iterative(0))   # 1
```

#### Exercise 3: Prime Number Checker
```python
# Check if a number is prime
# A prime number is only divisible by 1 and itself

def is_prime(n: int) -> bool:
    # Your code here
    pass

# Test cases
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(20))  # False
print(is_prime(1))   # False
```

### Intermediate Level

#### Exercise 4: Fibonacci Sequence
```python
# Generate first n Fibonacci numbers
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n: int) -> list[int]:
    # Your code here
    pass

# Test cases
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### Exercise 5: GCD and LCM
```python
# Find Greatest Common Divisor and Least Common Multiple
# Use Euclidean algorithm for GCD
# LCM = (a * b) // GCD(a, b)

def gcd(a: int, b: int) -> int:
    # Your code here
    pass

def lcm(a: int, b: int) -> int:
    # Your code here
    pass

# Test cases
print(gcd(48, 18))   # 6
print(lcm(12, 18))   # 36
```

#### Exercise 6: Armstrong Number
```python
# Check if number is Armstrong (narcissistic) number
# 153 = 1³ + 5³ + 3³ = 153

def is_armstrong(n: int) -> bool:
    # Your code here
    pass

# Test cases
print(is_armstrong(153))   # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))   # False
```

### Advanced Level

#### Exercise 7: Prime Factors
```python
# Find all prime factors of a number
# Example: 84 → [2, 2, 3, 7]

def prime_factors(n: int) -> list[int]:
    # Your code here
    pass

# Test cases
print(prime_factors(84))    # [2, 2, 3, 7]
print(prime_factors(97))    # [97]
```

#### Exercise 8: Perfect Number
```python
# Check if number is perfect (sum of divisors equals number)
# Example: 6 = 1 + 2 + 3

def is_perfect(n: int) -> bool:
    # Your code here
    pass

# Test cases
print(is_perfect(6))    # True
print(is_perfect(28))   # True
print(is_perfect(12))   # False
```

---

## String Exercises

### Beginner Level

#### Exercise 9: Reverse String
```python
# Reverse a string without using [::-1]
def reverse_string(s: str) -> str:
    # Your code here
    pass

# Test cases
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

#### Exercise 10: Count Vowels
```python
# Count vowels (a, e, i, o, u) in a string
def count_vowels(s: str) -> int:
    # Your code here
    pass

# Test cases
print(count_vowels("hello"))     # 2
print(count_vowels("Python"))    # 1
```

#### Exercise 11: Palindrome Checker
```python
# Check if string reads same forwards and backwards
def is_palindrome(s: str) -> bool:
    # Your code here
    pass

# Test cases
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("A man a plan a canal panama"))  # True (ignore spaces)
```

### Intermediate Level

#### Exercise 12: Anagram Checker
```python
# Check if two strings are anagrams (same letters, different order)
def are_anagrams(s1: str, s2: str) -> bool:
    # Your code here
    pass

# Test cases
print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("hello", "world"))     # False
```

#### Exercise 13: String Compression
```python
# Compress string using run-length encoding
# Example: "aaabbc" → "a3b2c1"
def compress_string(s: str) -> str:
    # Your code here
    pass

# Test cases
print(compress_string("aaabbc"))     # "a3b2c1"
print(compress_string("abc"))        # "a1b1c1"
```

#### Exercise 14: Remove Duplicates
```python
# Remove duplicate characters while preserving order
def remove_duplicates(s: str) -> str:
    # Your code here
    pass

# Test cases
print(remove_duplicates("hello"))     # "helo"
print(remove_duplicates("banana"))    # "ban"
```

### Advanced Level

#### Exercise 15: Longest Substring Without Repeating
```python
# Find length of longest substring without repeating characters
def longest_unique_substring(s: str) -> int:
    # Your code here
    pass

# Test cases
print(longest_unique_substring("abcabcbb"))   # 3 ("abc")
print(longest_unique_substring("bbbbb"))      # 1 ("b")
```

#### Exercise 16: Valid Parentheses
```python
# Check if parentheses are valid and properly nested
def valid_parentheses(s: str) -> bool:
    # Your code here
    pass

# Test cases
print(valid_parentheses("()"))          # True
print(valid_parentheses("()[]{}"))      # True
print(valid_parentheses("(]"))          # False
print(valid_parentheses("([)]"))        # False
```

---

## List Exercises

### Beginner Level

#### Exercise 17: Find Maximum and Minimum
```python
# Find max and min without using built-in functions
def find_max_min(lst: list) -> tuple:
    # Your code here
    pass

# Test cases
print(find_max_min([3, 1, 4, 1, 5, 9, 2]))   # (9, 1)
```

#### Exercise 18: List Reversal
```python
# Reverse list without using [::-1] or reverse()
def reverse_list(lst: list) -> list:
    # Your code here
    pass

# Test cases
print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
```

#### Exercise 19: Remove Duplicates
```python
# Remove duplicates while preserving order
def remove_duplicates_preserve_order(lst: list) -> list:
    # Your code here
    pass

# Test cases
print(remove_duplicates_preserve_order([1, 2, 3, 2, 4, 3, 5]))  # [1, 2, 3, 4, 5]
```

### Intermediate Level

#### Exercise 20: Rotate List
```python
# Rotate list by k positions to the right
def rotate_list(lst: list, k: int) -> list:
    # Your code here
    pass

# Test cases
print(rotate_list([1, 2, 3, 4, 5], 2))   # [4, 5, 1, 2, 3]
```

#### Exercise 21: Merge Sorted Lists
```python
# Merge two sorted lists into one sorted list
def merge_sorted(list1: list, list2: list) -> list:
    # Your code here
    pass

# Test cases
print(merge_sorted([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
```

#### Exercise 22: Find Pairs with Sum
```python
# Find all pairs that sum to target
def find_pairs_with_sum(lst: list, target: int) -> list[tuple]:
    # Your code here
    pass

# Test cases
print(find_pairs_with_sum([1, 2, 3, 4, 5], 5))   # [(1, 4), (2, 3)]
```

### Advanced Level

#### Exercise 23: Longest Consecutive Sequence
```python
# Find length of longest consecutive sequence in unsorted list
def longest_consecutive(nums: list) -> int:
    # Your code here
    pass

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4 (1,2,3,4)
```

#### Exercise 24: Product of Array Except Self
```python
# Return list where each element is product of all other elements
def product_except_self(nums: list) -> list:
    # Your code here
    pass

# Test cases
print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
```

---

## Tuple Exercises

### Beginner Level

#### Exercise 25: Tuple Reversal
```python
# Reverse a tuple without using [::-1]
def reverse_tuple(t: tuple) -> tuple:
    # Your code here
    pass

# Test cases
print(reverse_tuple((1, 2, 3, 4)))   # (4, 3, 2, 1)
```

#### Exercise 26: Element Existence
```python
# Check if element exists in tuple
def element_exists(t: tuple, element) -> bool:
    # Your code here
    pass

# Test cases
print(element_exists((1, 2, 3), 2))   # True
print(element_exists((1, 2, 3), 5))   # False
```

### Intermediate Level

#### Exercise 27: Merge and Sort Tuples
```python
# Merge two tuples and sort the result
def merge_and_sort(t1: tuple, t2: tuple) -> tuple:
    # Your code here
    pass

# Test cases
print(merge_and_sort((1, 3, 5), (2, 4, 6)))   # (1, 2, 3, 4, 5, 6)
```

#### Exercise 28: Tuple of Squares
```python
# Create tuple of squares for numbers 1 to n
def squares_tuple(n: int) -> tuple:
    # Your code here
    pass

# Test cases
print(squares_tuple(5))   # (1, 4, 9, 16, 25)
```

---

## Set Exercises

### Beginner Level

#### Exercise 29: Set Creation
```python
# Create set from list, removing duplicates
def list_to_set(lst: list) -> set:
    # Your code here
    pass

# Test cases
print(list_to_set([1, 2, 2, 3, 3, 3]))   # {1, 2, 3}
```

#### Exercise 30: Common Elements
```python
# Find common elements between two lists using set intersection
def common_elements(list1: list, list2: list) -> list:
    # Your code here
    pass

# Test cases
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))   # [3, 4]
```

### Intermediate Level

#### Exercise 31: Symmetric Difference
```python
# Find elements that appear in only one of two lists
def symmetric_difference(list1: list, list2: list) -> list:
    # Your code here
    pass

# Test cases
print(symmetric_difference([1, 2, 3], [3, 4, 5]))   # [1, 2, 4, 5]
```

#### Exercise 32: Missing Number
```python
# Find missing number in sequence using set difference
def find_missing_number(nums: list, n: int) -> list:
    # Your code here
    pass

# Test cases
print(find_missing_number([1, 2, 3, 5], 5))   # [4]
```

---

## Dictionary Exercises

### Beginner Level

#### Exercise 33: Word Counter
```python
# Count frequency of words in a sentence
def word_counter(sentence: str) -> dict:
    # Your code here
    pass

# Test cases
print(word_counter("hello world hello python"))   # {'hello': 2, 'world': 1, 'python': 1}
```

#### Exercise 34: Phone Directory
```python
# Create phone directory (name -> number)
# Add, find, and delete contacts
class PhoneDirectory:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name: str, number: str) -> None:
        # Your code here
        pass
    
    def find_contact(self, name: str) -> str:
        # Your code here
        pass
    
    def delete_contact(self, name: str) -> bool:
        # Your code here
        pass
```

### Intermediate Level

#### Exercise 35: Gradebook
```python
# Store student grades and calculate averages
class Gradebook:
    def __init__(self):
        self.students = {}
    
    def add_grade(self, student: str, grade: float) -> None:
        # Your code here
        pass
    
    def get_average(self, student: str) -> float:
        # Your code here
        pass
    
    def get_class_average(self) -> float:
        # Your code here
        pass
```

#### Exercise 36: Group by Key
```python
# Group list of dictionaries by a key
def group_by_key(data: list[dict], key: str) -> dict:
    # Your code here
    pass

# Test cases
data = [
    {'city': 'NYC', 'name': 'Alice'},
    {'city': 'LA', 'name': 'Bob'},
    {'city': 'NYC', 'name': 'Charlie'}
]
print(group_by_key(data, 'city'))
# {'NYC': [{'city': 'NYC', 'name': 'Alice'}, {'city': 'NYC', 'name': 'Charlie'}], 'LA': [{'city': 'LA', 'name': 'Bob'}]}
```

### Advanced Level

#### Exercise 37: Cache Implementation
```python
# Implement LRU (Least Recently Used) cache
class LRUCache:
    def __init__(self, capacity: int):
        # Your code here
        pass
    
    def get(self, key: str) -> any:
        # Your code here
        pass
    
    def put(self, key: str, value: any) -> None:
        # Your code here
        pass
```

---

## Boolean Exercises

### Beginner Level

#### Exercise 38: Leap Year Checker
```python
# Check if year is leap year
# Leap year: divisible by 4, not by 100 unless also by 400
def is_leap_year(year: int) -> bool:
    # Your code here
    pass

# Test cases
print(is_leap_year(2020))   # True
print(is_leap_year(2021))   # False
print(is_leap_year(2000))   # True
```

#### Exercise 39: Vowel Checker
```python
# Check if character is a vowel (a, e, i, o, u)
def is_vowel(char: str) -> bool:
    # Your code here
    pass

# Test cases
print(is_vowel('a'))   # True
print(is_vowel('b'))   # False
```

### Intermediate Level

#### Exercise 40: Password Validator
```python
# Check password strength
# Requirements:
# - At least 8 characters
# - Contains uppercase and lowercase
# - Contains at least one digit
# - Contains at least one special character
def is_strong_password(password: str) -> bool:
    # Your code here
    pass

# Test cases
print(is_strong_password("Password123!"))   # True
print(is_strong_password("weak"))           # False
```

---

## Binary Type Exercises

### Beginner Level

#### Exercise 41: Bytes to Hex
```python
# Convert bytes to hex string with spaces
def bytes_to_hex(data: bytes) -> str:
    # Your code here
    pass

# Test cases
print(bytes_to_hex(b'Hello'))   # "48 65 6c 6c 6f"
```

#### Exercise 42: Hex to Bytes
```python
# Convert hex string to bytes
def hex_to_bytes(hex_str: str) -> bytes:
    # Your code here
    pass

# Test cases
print(hex_to_bytes("48 65 6c 6c 6f"))   # b'Hello'
```

### Intermediate Level

#### Exercise 43: XOR Cipher
```python
# Implement XOR encryption/decryption for bytes
def xor_cipher(data: bytes, key: bytes) -> bytes:
    # Your code here
    pass

# Test cases
plain = b'Hello World'
key = b'secret'
cipher = xor_cipher(plain, key)
decrypted = xor_cipher(cipher, key)
print(decrypted == plain)   # True
```

---

## Type Conversion Exercises

### Beginner Level

#### Exercise 44: String to Number
```python
# Safely convert string to int, return default if invalid
def safe_int(value: str, default: int = 0) -> int:
    # Your code here
    pass

# Test cases
print(safe_int("123"))     # 123
print(safe_int("abc"))     # 0
```

#### Exercise 45: Mixed Type Summer
```python
# Sum list containing int, float, bool
def sum_mixed(values: list) -> float:
    # Your code here
    pass

# Test cases
print(sum_mixed([1, 2.5, True, False]))   # 4.5 (1 + 2.5 + 1 + 0)
```

### Intermediate Level

#### Exercise 46: CSV Parser
```python
# Parse CSV string with type conversion
def parse_csv(csv_string: str, types: list) -> list:
    # Your code here
    pass

# Test cases
csv_data = "1,2.5,true\n3,4.5,false"
types = [int, float, bool]
print(parse_csv(csv_data, types))
# [[1, 2.5, True], [3, 4.5, False]]
```

---

## Mixed Type Projects

### Project 1: Student Management System

```python
"""
Create a student management system with the following features:

1. Add student (ID, name, grades list)
2. Calculate GPA for each student
3. Find student by ID or name
4. Get class average
5. Generate report card
6. Save/Load data to file

Use appropriate data types:
- dict for student records
- list for grades
- tuple for return values
- set for course offerings
- bool for active status
- None for missing data
"""

class StudentManagementSystem:
    def __init__(self):
        # Your code here
        pass
    
    def add_student(self, student_id: int, name: str, grades: list[float]) -> None:
        # Your code here
        pass
    
    def calculate_gpa(self, student_id: int) -> float:
        # Your code here
        pass
    
    def find_student(self, search: str) -> dict | None:
        # Search by ID or name
        pass
    
    def get_class_average(self) -> float:
        # Your code here
        pass
    
    def generate_report_card(self, student_id: int) -> str:
        # Your code here
        pass
    
    def save_to_file(self, filename: str) -> None:
        # Your code here
        pass
    
    def load_from_file(self, filename: str) -> None:
        # Your code here
        pass
```

### Project 2: Shopping Cart System

```python
"""
Create a shopping cart system with:

1. Product catalog (name, price, stock)
2. Add/remove items from cart
3. Apply discounts (percentage or fixed)
4. Calculate tax
5. Generate invoice
6. Track inventory

Use:
- dict for products and cart
- list for cart items
- tuple for order history
- set for product categories
- float for prices
- int for quantities
- bool for active status
"""

class ShoppingCartSystem:
    def __init__(self):
        # Your code here
        pass
    
    def add_product(self, name: str, price: float, stock: int, category: str) -> None:
        # Your code here
        pass
    
    def add_to_cart(self, product_name: str, quantity: int) -> bool:
        # Your code here
        pass
    
    def remove_from_cart(self, product_name: str) -> bool:
        # Your code here
        pass
    
    def apply_discount(self, discount_type: str, value: float) -> None:
        # Your code here
        pass
    
    def calculate_total(self) -> float:
        # Your code here
        pass
    
    def generate_invoice(self) -> str:
        # Your code here
        pass
    
    def checkout(self) -> tuple[bool, str]:
        # Your code here
        pass
```

### Project 3: Contact Book Application

```python
"""
Create a contact book application with:

1. Add/edit/delete contacts
2. Search by name, phone, or email
3. Group contacts by category
4. Import/export to CSV
5. Find duplicates
6. Backup and restore

Use:
- dict for contacts
- list for search results
- set for categories
- tuple for contact data
- str for names/emails
- int for phone numbers
- bool for favorite status
- None for optional fields
"""

class ContactBook:
    def __init__(self):
        # Your code here
        pass
    
    def add_contact(self, name: str, phone: str, email: str = None, category: str = "General") -> None:
        # Your code here
        pass
    
    def edit_contact(self, name: str, **kwargs) -> bool:
        # Your code here
        pass
    
    def delete_contact(self, name: str) -> bool:
        # Your code here
        pass
    
    def search_by_name(self, name: str) -> list[dict]:
        # Your code here
        pass
    
    def search_by_phone(self, phone: str) -> dict | None:
        # Your code here
        pass
    
    def get_contacts_by_category(self, category: str) -> list[dict]:
        # Your code here
        pass
    
    def find_duplicates(self) -> list[tuple]:
        # Your code here
        pass
    
    def export_to_csv(self, filename: str) -> None:
        # Your code here
        pass
    
    def import_from_csv(self, filename: str) -> int:
        # Your code here
        pass
```

---

## Answer Key

Solutions for all exercises are available in `solutions.md`. Each solution includes:
- Complete code with proper formatting
- Explanation of the approach
- Test cases and expected outputs
- Alternative implementations
- Common mistakes to avoid

---

## Submission Guidelines

1. Write your code in the provided function stubs
2. Test your code with the given test cases
3. Add additional test cases for edge cases
4. Use meaningful variable names
5. Add docstrings and comments
6. Follow PEP 8 style guide

---

## Evaluation Criteria

| Criteria | Weight |
|----------|--------|
| Correctness | 40% |
| Code quality | 20% |
| Efficiency | 20% |
| Edge case handling | 10% |
| Documentation | 10% |

## Next Step

- Go to [solutions.md](solutions.md) for seeing its solutions.

---

*Happy Coding! Complete these exercises to master Python data types! 🐍✨*
# 💡 LOOPS – SOLUTIONS

## 📌 Table of Contents
1. [For Loop Solutions](#for-loop-solutions)
2. [While Loop Solutions](#while-loop-solutions)
3. [Nested Loop Solutions](#nested-loop-solutions)
4. [Loop Control Solutions](#loop-control-solutions)
5. [Mixed Practice Solutions](#mixed-practice-solutions)
6. [Challenge Solutions](#challenge-solutions)

---

## For Loop Solutions

### Solution 1: Print Numbers

```python
# Print numbers from 1 to 20
for i in range(1, 21):
    print(i, end=" ")
print()

# Alternative with list
numbers = list(range(1, 21))
print(numbers)
```

### Solution 2: Sum of Numbers

```python
# Sum of numbers 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")  # 5050

# Using sum() function
total = sum(range(1, 101))
print(f"Sum: {total}")  # 5050
```

### Solution 3: Even Numbers

```python
# Print even numbers 1 to 50
for i in range(2, 51, 2):
    print(i, end=" ")
print()

# Alternative with condition
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()
```

### Solution 4: Multiplication Table

```python
# Multiplication table for 7
number = 7
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
```

### Solution 5: List Iteration

```python
# Print fruits with lengths
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(f"{fruit}: {len(fruit)}")
```

### Solution 6: Factorial

```python
def factorial(n):
    """Calculate factorial using for loop"""
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120
print(factorial(7))   # 5040
print(factorial(0))   # 1
```

### Solution 7: Prime Number Checker

```python
def is_prime(n):
    """Check if number is prime using for loop"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(17))   # True
print(is_prime(20))   # False
print(is_prime(2))    # True
print(is_prime(1))    # False
```

### Solution 8: Reverse String

```python
def reverse_string(s):
    """Reverse a string using for loop"""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Alternative using range
def reverse_string_v2(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

print(reverse_string("hello"))     # "olleh"
print(reverse_string("Python"))    # "nohtyP"
```

### Solution 9: Count Vowels

```python
def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))        # 3
print(count_vowels("Python Programming")) # 4
```

### Solution 10: Find Maximum

```python
def find_max(numbers):
    """Find maximum number without using max()"""
    if not numbers:
        return None
    
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([3, 1, 4, 1, 5, 9, 2]))   # 9
print(find_max([-5, -2, -8, -1]))        # -1
```

### Solution 11: List Comprehension

```python
# List comprehension examples
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
words = ["apple", "banana", "cherry", "date"]
lengths = [len(word) for word in words]

print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(evens)     # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(lengths)   # [5, 6, 6, 4]
```

### Solution 12: Dictionary from Lists

```python
# Create dictionary using zip()
keys = ["name", "age", "city", "job"]
values = ["Alice", 30, "New York", "Engineer"]

person = dict(zip(keys, values))
print(person)
# {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Using loop
person = {}
for i in range(len(keys)):
    person[keys[i]] = values[i]
print(person)
```

### Solution 13: Enumerate Practice

```python
# Use enumerate to print index and value
fruits = ["apple", "banana", "cherry", "date"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start from 1
for index, fruit in enumerate(fruits, 1):
    print(f"{index}: {fruit}")
```

---

## While Loop Solutions

### Solution 14: Countdown

```python
# Countdown from 10 to 1
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
```

### Solution 15: Sum Until Zero

```python
# Sum numbers until zero
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Sum: {total}")
```

### Solution 16: Password Check

```python
# Password checker
correct_password = "secret"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")
```

### Solution 17: Digit Counter

```python
def count_digits(n):
    """Count number of digits in a number"""
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(12345))     # 5
print(count_digits(1000000))   # 7
print(count_digits(0))         # 1
```

### Solution 18: Reverse Number

```python
def reverse_number(n):
    """Reverse a number using while loop"""
    reversed_num = 0
    is_negative = n < 0
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return -reversed_num if is_negative else reversed_num

print(reverse_number(12345))   # 54321
print(reverse_number(1000))    # 1
print(reverse_number(-123))    # -321
```

### Solution 19: Sum of Digits

```python
def sum_of_digits(n):
    """Calculate sum of digits"""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(12345))   # 15
print(sum_of_digits(9876))    # 30
print(sum_of_digits(0))       # 0
```

### Solution 20: Palindrome Number

```python
def is_palindrome_number(n):
    """Check if number is palindrome"""
    if n < 0:
        return False
    
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return original == reversed_num

print(is_palindrome_number(12321))   # True
print(is_palindrome_number(12345))   # False
print(is_palindrome_number(0))       # True
```

### Solution 21: Guess the Number Game

```python
import random

def guess_number_game():
    """Number guessing game"""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("Guess the number between 1 and 100!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number")

# Uncomment to play
# guess_number_game()
```

### Solution 22: ATM PIN Validation

```python
def atm_pin_validation():
    """ATM PIN validation with 3 attempts"""
    correct_pin = "1234"
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        pin = input("Enter your PIN: ")
        attempts += 1
        
        if pin == correct_pin:
            print("Access granted!")
            return True
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Wrong PIN. {remaining} attempts remaining")
            else:
                print("Card blocked. Too many failed attempts.")
    
    return False

# Uncomment to test
# atm_pin_validation()
```

---

## Nested Loop Solutions

### Solution 23: Rectangle of Stars

```python
# Rectangle of stars (5×10)
rows = 5
cols = 10

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
```

### Solution 24: Right Triangle

```python
# Right triangle of stars (height 5)
height = 5

for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()
```

### Solution 25: Multiplication Table

```python
# Multiplication table 10×10
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n    " + "-" * 40)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
```

### Solution 26: Reverse Triangle

```python
# Reverse right triangle (height 5)
height = 5

for i in range(height, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

### Solution 27: Square of Numbers

```python
# 3x3 grid with coordinates
size = 3

for i in range(size):
    for j in range(size):
        print(f"({i},{j})", end=" ")
    print()
```

### Solution 28: Matrix Addition

```python
# Add two 3x3 matrices
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
C = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Result:")
for row in C:
    print(row)
# [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
```

### Solution 29: Floyd's Triangle

```python
# Floyd's Triangle for 5 rows
rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

### Solution 30: Pascal's Triangle

```python
# Pascal's Triangle for 5 rows
rows = 5
triangle = []

for i in range(rows):
    row = [1]
    if triangle:
        last_row = triangle[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
    triangle.append(row)

# Print with spacing
for row in triangle:
    print(" " * (rows - len(row)), " ".join(map(str, row)))
```

### Solution 31: Matrix Transpose

```python
# Transpose 3x4 matrix to 4x3
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transpose = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose:")
for row in transpose:
    print(row)
# [1, 5, 9]
# [2, 6, 10]
# [3, 7, 11]
# [4, 8, 12]
```

### Solution 32: Diagonal Sum

```python
# Sum of main and anti-diagonals
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

n = len(matrix)
main_sum = 0
anti_sum = 0

for i in range(n):
    main_sum += matrix[i][i]
    anti_sum += matrix[i][n - 1 - i]

print(f"Main diagonal sum: {main_sum}")    # 65
print(f"Anti-diagonal sum: {anti_sum}")    # 65
```

### Solution 33: Matrix Multiplication

```python
# Multiply two matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Cannot multiply: incompatible dimensions")
else:
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    print("Result:")
    for row in result:
        print(row)
# [[58, 64], [139, 154]]
```

### Solution 34: Spiral Matrix

```python
def spiral_matrix(n):
    """Create a spiral matrix of size n x n"""
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Fill top row
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        
        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Fill bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        
        # Fill left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    return matrix

print(spiral_matrix(3))
# [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
```

### Solution 35: Magic Square

```python
def is_magic_square(matrix):
    """Check if matrix is a magic square"""
    n = len(matrix)
    
    # Calculate target sum (first row sum)
    target = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != target:
            return False
    
    # Check columns
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != target:
            return False
    
    # Check main diagonal
    diag_sum = 0
    for i in range(n):
        diag_sum += matrix[i][i]
    if diag_sum != target:
        return False
    
    # Check anti-diagonal
    anti_sum = 0
    for i in range(n):
        anti_sum += matrix[i][n - 1 - i]
    if anti_sum != target:
        return False
    
    return True

matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(is_magic_square(matrix))  # True
```

---

## Loop Control Solutions

### Solution 36: Break on Condition

```python
# Print numbers until divisible by 7
for i in range(1, 21):
    if i % 7 == 0:
        break
    print(i, end=" ")
print()
```

### Solution 37: Skip Even Numbers

```python
# Print odd numbers using continue
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
```

### Solution 38: Search with else

```python
def search_list(items, target):
    """Search for target using for-else"""
    for item in items:
        if item == target:
            print("Found")
            break
    else:
        print("Not found")

search_list([1, 2, 3, 4, 5], 3)   # Found
search_list([1, 2, 3, 4, 5], 7)   # Not found
```

### Solution 39: First Positive Even

```python
# Find first positive even number
numbers = [-5, -2, 3, 7, 8, 10, -1]

for num in numbers:
    if num > 0 and num % 2 == 0:
        print(f"First positive even: {num}")
        break
```

### Solution 40: Skip and Stop

```python
# Process numbers: skip negatives, stop at zero
numbers = [5, -2, 8, -1, 0, 7, 3]

for num in numbers:
    if num < 0:
        print(f"Skipping negative: {num}")
        continue
    if num == 0:
        print("Found zero, stopping")
        break
    print(f"Processing: {num}")
```

---

## Mixed Practice Solutions

### Solution 41: FizzBuzz

```python
# FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Solution 42: Fibonacci Sequence

```python
def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Solution 43: Perfect Number

```python
def is_perfect(n):
    """Check if number is perfect"""
    if n < 2:
        return False
    
    divisors_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    
    return divisors_sum == n

print(is_perfect(6))    # True
print(is_perfect(28))   # True
print(is_perfect(12))   # False
```

### Solution 44: Armstrong Number

```python
def is_armstrong(n):
    """Check if number is Armstrong"""
    if n < 0:
        return False
    
    num_str = str(n)
    num_digits = len(num_str)
    total = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    
    return total == n

print(is_armstrong(153))    # True
print(is_armstrong(9474))   # True
print(is_armstrong(123))    # False
```

### Solution 45: Common Elements

```python
def common_elements(list1, list2):
    """Find common elements between two lists"""
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Using set (more efficient)
def common_elements_set(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
```

---

## Challenge Solutions

### Solution 46: Word Frequency Counter

```python
def word_frequency(sentence):
    """Count frequency of each word"""
    words = sentence.lower().split()
    freq = {}
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq

sentence = "the cat and the dog and the bird"
print(word_frequency(sentence))
# {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}

# Using collections.Counter
from collections import Counter
def word_frequency_counter(sentence):
    return dict(Counter(sentence.lower().split()))
```

### Solution 47: Group Anagrams

```python
def group_anagrams(words):
    """Group anagrams together"""
    from collections import defaultdict
    
    anagrams = defaultdict(list)
    
    for word in words:
        # Sort the word to use as key
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### Solution 48: Longest Substring Without Repeating

```python
def longest_unique_substring(s):
    """Find length of longest substring without repeating characters"""
    if not s:
        return 0
    
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

print(longest_unique_substring("abcabcbb"))  # 3
print(longest_unique_substring("bbbbb"))     # 1
print(longest_unique_substring("pwwkew"))    # 3
```

### Solution 49: Merge Sorted Lists

```python
def merge_sorted(list1, list2):
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

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

### Solution 50: Rotate Matrix

```python
def rotate_matrix(matrix):
    """Rotate matrix 90 degrees clockwise"""
    n = len(matrix)
    
    # Create result matrix filled with zeros
    result = [[0] * n for _ in range(n)]
    
    # Rotate
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    
    return result

# In-place rotation
def rotate_matrix_inplace(matrix):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix(matrix))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

---

## Scoring Guide

| Score Range | Rating | Recommendation |
|-------------|--------|----------------|
| 45-50/50 | Excellent | Ready for next topic |
| 35-44/50 | Good | Review missed concepts |
| 25-34/50 | Satisfactory | Practice more |
| 15-24/50 | Needs Improvement | Re-study material |
| Below 15 | Review | Start from basics |

---

## Next Step

- Move to [Functions](/05_python/05_functions/README.md) to learn about reusable blocks of code.

---

*Solutions verified and tested. Keep practicing! 🐍✨*
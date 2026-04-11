# 📝 LOOPS – PRACTICE EXERCISES

## 📌 Table of Contents
1. [For Loop Exercises](#for-loop-exercises)
2. [While Loop Exercises](#while-loop-exercises)
3. [Nested Loop Exercises](#nested-loop-exercises)
4. [Loop Control Exercises](#loop-control-exercises)
5. [Mixed Practice Exercises](#mixed-practice-exercises)
6. [Challenge Exercises](#challenge-exercises)

---

## For Loop Exercises

### Beginner Level

#### Exercise 1: Print Numbers
```python
# Print numbers from 1 to 20 using for loop
# Your code here
```

#### Exercise 2: Sum of Numbers
```python
# Calculate sum of all numbers from 1 to 100
# Your code here
# Expected output: 5050
```

#### Exercise 3: Even Numbers
```python
# Print all even numbers between 1 and 50
# Your code here
```

#### Exercise 4: Multiplication Table
```python
# Print multiplication table for number 7 (1 to 10)
# Your code here
# Expected output:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
```

#### Exercise 5: List Iteration
```python
# Given list: fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Print each fruit with its length
# Expected output:
# apple: 5
# banana: 6
# cherry: 6
# date: 4
# elderberry: 10
```

### Intermediate Level

#### Exercise 6: Factorial
```python
# Calculate factorial of a given number using for loop
# Example: factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
def factorial(n):
    # Your code here
    pass

print(factorial(5))  # 120
print(factorial(7))  # 5040
```

#### Exercise 7: Prime Number Checker
```python
# Check if a number is prime using for loop
def is_prime(n):
    # Your code here
    pass

print(is_prime(17))  # True
print(is_prime(20))  # False
print(is_prime(2))   # True
```

#### Exercise 8: Reverse String
```python
# Reverse a string using for loop (without [::-1])
def reverse_string(s):
    # Your code here
    pass

print(reverse_string("hello"))     # "olleh"
print(reverse_string("Python"))    # "nohtyP"
```

#### Exercise 9: Count Vowels
```python
# Count vowels in a string using for loop
def count_vowels(s):
    # Your code here
    pass

print(count_vowels("Hello World"))     # 3
print(count_vowels("Python Programming")) # 4
```

#### Exercise 10: Find Maximum
```python
# Find maximum number in a list without using max()
def find_max(numbers):
    # Your code here
    pass

print(find_max([3, 1, 4, 1, 5, 9, 2]))  # 9
print(find_max([-5, -2, -8, -1]))       # -1
```

### Advanced Level

#### Exercise 11: List Comprehension
```python
# Use list comprehension to create:
# 1. Squares of numbers 1-10
# 2. Even numbers from 1-20
# 3. Lengths of words in a list

squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
words = ["apple", "banana", "cherry", "date"]
lengths = [len(word) for word in words]

print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(evens)     # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(lengths)   # [5, 6, 6, 4]
```

#### Exercise 12: Dictionary from Lists
```python
# Create dictionary from two lists using zip()
keys = ["name", "age", "city", "job"]
values = ["Alice", 30, "New York", "Engineer"]

# Your code here
# Expected output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
```

#### Exercise 13: Enumerate Practice
```python
# Use enumerate to print index and value
fruits = ["apple", "banana", "cherry", "date"]

# Your code here
# Expected output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date
```

---

## While Loop Exercises

### Beginner Level

#### Exercise 14: Countdown
```python
# Print countdown from 10 to 1 using while loop
# Your code here
```

#### Exercise 15: Sum Until Zero
```python
# Keep asking user for numbers until they enter 0, then print sum
# Your code here
```

#### Exercise 16: Password Check
```python
# Keep asking for password until correct password "secret" is entered
# Your code here
```

#### Exercise 17: Digit Counter
```python
# Count number of digits in a number using while loop
def count_digits(n):
    # Your code here
    pass

print(count_digits(12345))     # 5
print(count_digits(1000000))   # 7
```

#### Exercise 18: Reverse Number
```python
# Reverse a number using while loop
def reverse_number(n):
    # Your code here
    pass

print(reverse_number(12345))   # 54321
print(reverse_number(1000))    # 1
```

### Intermediate Level

#### Exercise 19: Sum of Digits
```python
# Calculate sum of digits using while loop
def sum_of_digits(n):
    # Your code here
    pass

print(sum_of_digits(12345))   # 15
print(sum_of_digits(9876))    # 30
```

#### Exercise 20: Palindrome Number
```python
# Check if number is palindrome (reads same forward and backward)
def is_palindrome_number(n):
    # Your code here
    pass

print(is_palindrome_number(12321))   # True
print(is_palindrome_number(12345))   # False
```

#### Exercise 21: Guess the Number Game
```python
# Create number guessing game
# Generate random number between 1-100
# Keep asking until user guesses correctly
# Give hints "Too high" or "Too low"

import random
secret = random.randint(1, 100)

# Your code here
```

#### Exercise 22: ATM PIN Validation
```python
# ATM PIN validation with 3 attempts
# Correct PIN is "1234"
# If correct, print "Access granted"
# If wrong after 3 attempts, print "Card blocked"

# Your code here
```

---

## Nested Loop Exercises

### Beginner Level

#### Exercise 23: Rectangle of Stars
```python
# Print rectangle of stars (5 rows × 10 columns)
# Your code here
# Expected output:
# **********
# **********
# **********
# **********
# **********
```

#### Exercise 24: Right Triangle
```python
# Print right triangle of stars (height 5)
# Your code here
# Expected output:
# *
# **
# ***
# ****
# *****
```

#### Exercise 25: Multiplication Table
```python
# Print multiplication table from 1 to 10 (10x10 grid)
# Your code here
# Expected output format:
#    1   2   3   4   5   6   7   8   9  10
#    2   4   6   8  10  12  14  16  18  20
#    ... etc
```

#### Exercise 26: Reverse Triangle
```python
# Print reverse right triangle (height 5)
# Your code here
# Expected output:
# *****
# ****
# ***
# **
# *
```

#### Exercise 27: Square of Numbers
```python
# Print a square where each cell shows row,col
# For 3x3 grid, output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

# Your code here
```

### Intermediate Level

#### Exercise 28: Matrix Addition
```python
# Add two 3x3 matrices
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Calculate C = A + B
# Your code here
# Expected output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
```

#### Exercise 29: Floyd's Triangle
```python
# Print Floyd's Triangle for 5 rows
# Expected output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# Your code here
```

#### Exercise 30: Pascal's Triangle
```python
# Print Pascal's Triangle for 5 rows
# Expected output:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Your code here
```

#### Exercise 31: Matrix Transpose
```python
# Transpose a 3x4 matrix to 4x3
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Your code here
# Expected output:
# [1, 5, 9]
# [2, 6, 10]
# [3, 7, 11]
# [4, 8, 12]
```

#### Exercise 32: Diagonal Sum
```python
# Calculate sum of main diagonal and anti-diagonal of 5x5 matrix
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Your code here
# Expected: Main diagonal sum = 65, Anti-diagonal sum = 65
```

### Advanced Level

#### Exercise 33: Matrix Multiplication
```python
# Multiply two matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

# Calculate C = A × B
# Your code here
# Expected output: [[58, 64], [139, 154]]
```

#### Exercise 34: Spiral Matrix
```python
# Create a spiral matrix of size n x n
# Example for n=3:
# [[1, 2, 3],
#  [8, 9, 4],
#  [7, 6, 5]]

def spiral_matrix(n):
    # Your code here
    pass

print(spiral_matrix(3))
```

#### Exercise 35: Magic Square
```python
# Check if a matrix is a magic square (all rows, columns, diagonals sum to same value)
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

def is_magic_square(matrix):
    # Your code here
    pass

print(is_magic_square(matrix))  # True
```

---

## Loop Control Exercises

#### Exercise 36: Break on Condition
```python
# Print numbers from 1 to 20, stop when number is divisible by 7
# Your code here
# Expected output: 1,2,3,4,5,6
```

#### Exercise 37: Skip Even Numbers
```python
# Print numbers from 1 to 20, skip even numbers using continue
# Your code here
# Expected output: 1,3,5,7,9,11,13,15,17,19
```

#### Exercise 38: Search with else
```python
# Search for target in list, print "Found" or "Not found" using for-else
def search_list(items, target):
    # Your code here
    pass

search_list([1, 2, 3, 4, 5], 3)   # Found
search_list([1, 2, 3, 4, 5], 7)   # Not found
```

#### Exercise 39: First Positive Even
```python
# Find first positive even number in list, stop when found
numbers = [-5, -2, 3, 7, 8, 10, -1]
# Your code here
# Expected output: First positive even: 8
```

#### Exercise 40: Skip and Stop
```python
# Process numbers: skip negatives, stop at zero
numbers = [5, -2, 8, -1, 0, 7, 3]
# Your code here
# Expected output: Processing: 5, Skipping negative: -2, Processing: 8, Skipping negative: -1, Found zero, stopping
```

---

## Mixed Practice Exercises

#### Exercise 41: FizzBuzz
```python
# Print numbers 1 to 100
# For multiples of 3 print "Fizz"
# For multiples of 5 print "Buzz"
# For multiples of both print "FizzBuzz"

# Your code here
```

#### Exercise 42: Fibonacci Sequence
```python
# Generate first n Fibonacci numbers
def fibonacci(n):
    # Your code here
    pass

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### Exercise 43: Perfect Number
```python
# Check if number is perfect (sum of divisors equals number)
def is_perfect(n):
    # Your code here
    pass

print(is_perfect(6))   # True (1+2+3=6)
print(is_perfect(28))  # True (1+2+4+7+14=28)
print(is_perfect(12))  # False
```

#### Exercise 44: Armstrong Number
```python
# Check if number is Armstrong (sum of cubes of digits equals number)
def is_armstrong(n):
    # Your code here
    pass

print(is_armstrong(153))   # True (1³+5³+3³=153)
print(is_armstrong(9474))  # True (9⁴+4⁴+7⁴+4⁴=9474)
```

#### Exercise 45: Common Elements
```python
# Find common elements between two lists
def common_elements(list1, list2):
    # Your code here
    pass

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
```

---

## Challenge Exercises

#### Exercise 46: Word Frequency Counter
```python
# Count frequency of each word in a sentence
def word_frequency(sentence):
    # Your code here
    pass

sentence = "the cat and the dog and the bird"
print(word_frequency(sentence))
# Expected: {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
```

#### Exercise 47: Group Anagrams
```python
# Group anagrams together from a list of words
def group_anagrams(words):
    # Your code here
    pass

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

#### Exercise 48: Longest Substring Without Repeating
```python
# Find length of longest substring without repeating characters
def longest_unique_substring(s):
    # Your code here
    pass

print(longest_unique_substring("abcabcbb"))  # 3 ("abc")
print(longest_unique_substring("bbbbb"))     # 1 ("b")
print(longest_unique_substring("pwwkew"))    # 3 ("wke")
```

#### Exercise 49: Merge Sorted Lists
```python
# Merge two sorted lists into one sorted list
def merge_sorted(list1, list2):
    # Your code here
    pass

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

#### Exercise 50: Rotate Matrix
```python
# Rotate matrix 90 degrees clockwise
def rotate_matrix(matrix):
    # Your code here
    pass

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(matrix))
# Expected:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
```

---

## Submission Guidelines

1. Write your code in the provided function stubs
2. Test your code with the given examples
3. Add additional test cases for edge cases
4. Use meaningful variable names
5. Add comments for complex logic
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

---

## Next Step

- Move to [solutions.md](solutions.md) to check your answers and learn from detailed explanations.

---

*Practice makes perfect! Complete all exercises to master loops in Python! 🐍✨*
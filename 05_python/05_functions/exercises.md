# 📝 FUNCTIONS – PRACTICE EXERCISES

## 📌 Table of Contents
1. [Basic Function Exercises](#basic-function-exercises)
2. [Parameter Exercises](#parameter-exercises)
3. [Return Value Exercises](#return-value-exercises)
4. [Scope Exercises](#scope-exercises)
5. [Lambda Exercises](#lambda-exercises)
6. [Recursion Exercises](#recursion-exercises)
7. [Decorator Exercises](#decorator-exercises)
8. [Generator Exercises](#generator-exercises)
9. [Mixed Practice Exercises](#mixed-practice-exercises)
10. [Challenge Exercises](#challenge-exercises)

---

## Basic Function Exercises

### Exercise 1: Greeting Function
```python
# Write a function that takes a name and returns "Hello, {name}!"
def greet(name):
    # Your code here
    pass

print(greet("Alice"))  # "Hello, Alice!"
print(greet("Bob"))    # "Hello, Bob!"
```

### Exercise 2: Area of Circle
```python
# Write a function that calculates area of circle given radius
# Formula: π × r²
def circle_area(radius):
    # Your code here
    pass

print(circle_area(5))    # 78.53981633974483
print(circle_area(2.5))  # 19.634954084936208
```

### Exercise 3: Even or Odd
```python
# Write a function that returns True if number is even, False if odd
def is_even(n):
    # Your code here
    pass

print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True
```

### Exercise 4: Maximum of Two
```python
# Write a function that returns the larger of two numbers
def max_of_two(a, b):
    # Your code here
    pass

print(max_of_two(10, 20))  # 20
print(max_of_two(25, 15))  # 25
print(max_of_two(5, 5))    # 5
```

### Exercise 5: String Reverser
```python
# Write a function that reverses a string
def reverse_string(s):
    # Your code here
    pass

print(reverse_string("hello"))     # "olleh"
print(reverse_string("Python"))    # "nohtyP"
```

---

## Parameter Exercises

### Exercise 6: Default Parameter
```python
# Write a function with default greeting "Hello"
def greet_person(name, greeting="Hello"):
    # Your code here
    pass

print(greet_person("Alice"))           # "Hello, Alice!"
print(greet_person("Bob", "Hi"))       # "Hi, Bob!"
print(greet_person("Charlie", "Hey"))  # "Hey, Charlie!"
```

### Exercise 7: Variable Arguments (*args)
```python
# Write a function that sums any number of arguments
def sum_all(*args):
    # Your code here
    pass

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
print(sum_all())               # 0
```

### Exercise 8: Variable Keyword Arguments (**kwargs)
```python
# Write a function that prints all keyword arguments
def print_info(**kwargs):
    # Your code here
    pass

print_info(name="Alice", age=30, city="NYC")
# Expected output:
# name: Alice
# age: 30
# city: NYC
```

### Exercise 9: Mixed Parameters
```python
# Write a function that takes required, default, *args, and **kwargs
def process_data(required, default="default", *args, **kwargs):
    # Your code here
    pass

process_data("req", 1, 2, 3, name="Alice", age=30)
# Expected output:
# Required: req
# Default: 1
# Args: (2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
```

### Exercise 10: Keyword-Only Arguments
```python
# Write a function with keyword-only arguments
def configure(*, host, port, debug=False):
    # Your code here
    pass

configure(host="localhost", port=8080)        # OK
configure(host="localhost", port=8080, debug=True)  # OK
# configure("localhost", 8080)  # Should raise TypeError
```

---

## Return Value Exercises

### Exercise 11: Multiple Returns
```python
# Write a function that returns both min and max of a list
def min_max(numbers):
    # Your code here
    pass

result = min_max([3, 1, 4, 1, 5, 9, 2])
print(result)  # (1, 9)
```

### Exercise 12: Early Return
```python
# Write a function that returns early if condition met
def check_positive(numbers):
    # Return first positive number, or None if none found
    # Your code here
    pass

print(check_positive([-5, -2, 3, -1]))   # 3
print(check_positive([-5, -2, -1]))      # None
```

### Exercise 13: Multiple Return Types
```python
# Write a function that returns different types based on input
def process(value):
    # If list: return average
    # If dict: return sum of values
    # If number: return square
    # Otherwise: return None
    # Your code here
    pass

print(process([1, 2, 3, 4, 5]))     # 3.0
print(process({"a": 10, "b": 20}))  # 30
print(process(5))                   # 25
print(process("hello"))             # None
```

### Exercise 14: Guard Clauses
```python
# Write a function using guard clauses (early returns)
def calculate_discount(price, is_member, coupon=None):
    # Return 0 if price <= 0
    # Return 0 if not member and no coupon
    # Member: 10% off, +5% if price >= 100
    # Coupon: SAVE20 = 20% off, SAVE10 = 10% off
    # Return discount percentage (0-0.5)
    # Your code here
    pass

print(calculate_discount(50, True))        # 0.1
print(calculate_discount(150, True))       # 0.15
print(calculate_discount(50, False))       # 0
print(calculate_discount(50, True, "SAVE20"))  # 0.2
```

---

## Scope Exercises

### Exercise 15: Local vs Global
```python
# Predict and fix the scope issue
x = 10

def modify_global():
    # Modify the global variable x to 20
    # Your code here
    pass

modify_global()
print(x)  # Should print 20
```

### Exercise 16: Enclosing Scope
```python
# Write a function that returns a nested function
def make_multiplier(factor):
    # Return a function that multiplies by factor
    # Your code here
    pass

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

### Exercise 17: Nonlocal
```python
# Write a counter function using nonlocal
def counter():
    # Return a function that increments and returns count
    # Your code here
    pass

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

---

## Lambda Exercises

### Exercise 18: Basic Lambda
```python
# Convert this function to a lambda
def square(x):
    return x ** 2

square_lambda = # Your code here

print(square_lambda(5))  # 25
```

### Exercise 19: Lambda with map()
```python
# Use lambda with map() to square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map( # Your code here , numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### Exercise 20: Lambda with filter()
```python
# Use lambda with filter() to keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter( # Your code here , numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

### Exercise 21: Lambda with sorted()
```python
# Use lambda to sort by the second element
pairs = [(1, 5), (2, 3), (3, 1), (4, 2)]
sorted_pairs = sorted(pairs, key= # Your code here )
print(sorted_pairs)  # [(3, 1), (4, 2), (2, 3), (1, 5)]
```

### Exercise 22: Lambda in List Comprehension
```python
# Use lambda inside list comprehension to apply discount
prices = [100, 200, 300, 400, 500]
discount = 0.1
discounted = [(lambda x: x * (1 - discount))(price) for price in prices]
print(discounted)  # [90.0, 180.0, 270.0, 360.0, 450.0]
```

---

## Recursion Exercises

### Exercise 23: Factorial (Recursive)
```python
# Write recursive factorial function
def factorial(n):
    # Base case: n <= 1 returns 1
    # Recursive case: n * factorial(n-1)
    # Your code here
    pass

print(factorial(5))   # 120
print(factorial(10))  # 3628800
```

### Exercise 24: Fibonacci (Recursive)
```python
# Write recursive fibonacci function
def fibonacci(n):
    # Base case: n <= 1 returns n
    # Recursive case: fibonacci(n-1) + fibonacci(n-2)
    # Your code here
    pass

print(fibonacci(10))  # 55
```

### Exercise 25: Sum of List (Recursive)
```python
# Write recursive function to sum list elements
def sum_list(numbers):
    # Base case: empty list returns 0
    # Recursive case: first + sum of rest
    # Your code here
    pass

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

### Exercise 26: Palindrome Check (Recursive)
```python
# Write recursive function to check palindrome
def is_palindrome(s):
    # Clean string (lowercase, remove spaces)
    # Base case: length <= 1 returns True
    # Check first and last characters
    # Your code here
    pass

print(is_palindrome("racecar"))                      # True
print(is_palindrome("A man a plan a canal panama"))  # True
print(is_palindrome("hello"))                        # False
```

### Exercise 27: Power Function (Recursive)
```python
# Write recursive power function
def power(base, exponent):
    # Base case: exponent == 0 returns 1
    # Recursive case: base * power(base, exponent-1)
    # Your code here
    pass

print(power(2, 3))   # 8
print(power(5, 0))   # 1
print(power(3, 4))   # 81
```

---

## Decorator Exercises

### Exercise 28: Timer Decorator
```python
# Create decorator that prints execution time
import time

def timer(func):
    # Your code here
    pass

@timer
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())  # Should print: slow_function took 1.00 seconds
```

### Exercise 29: Uppercase Decorator
```python
# Create decorator that converts return value to uppercase
def uppercase(func):
    # Your code here
    pass

@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # "HELLO, ALICE"
```

### Exercise 30: Repeat Decorator
```python
# Create decorator that repeats function n times
def repeat(times):
    # Your code here
    pass

@repeat(3)
def say_hello():
    return "Hello"

print(say_hello())  # ['Hello', 'Hello', 'Hello']
```

### Exercise 31: Cache Decorator
```python
# Create decorator that caches results
def cache(func):
    # Your code here
    pass

@cache
def expensive_computation(n):
    print(f"Computing {n}...")
    return n ** 2

print(expensive_computation(5))  # Computing 5... 25
print(expensive_computation(5))  # 25 (from cache, no print)
```

### Exercise 32: Retry Decorator
```python
# Create decorator that retries on exception
def retry(max_attempts=3):
    # Your code here
    pass

@retry(max_attempts=3)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Failed!")
    return "Success"

print(unstable_function())
```

---

## Generator Exercises

### Exercise 33: Simple Generator
```python
# Write generator that yields numbers from 0 to n
def count_up_to(n):
    # Your code here
    pass

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4
```

### Exercise 34: Even Numbers Generator
```python
# Write generator that yields even numbers up to n
def even_numbers(n):
    # Your code here
    pass

for num in even_numbers(10):
    print(num, end=" ")  # 0, 2, 4, 6, 8, 10
print()
```

### Exercise 35: Fibonacci Generator
```python
# Write generator that yields Fibonacci numbers infinitely
def fibonacci():
    # Your code here
    pass

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print()
```

### Exercise 36: Generator Expression
```python
# Use generator expression (not list comprehension) to sum squares
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum( # Your code here )
print(sum_of_squares)  # 55
```

### Exercise 37: Generator with send()
```python
# Write generator that can receive values via send()
def accumulator():
    # Your code here
    pass

acc = accumulator()
next(acc)  # Initialize
print(acc.send(5))   # 5
print(acc.send(3))   # 8
print(acc.send(2))   # 10
```

---

## Mixed Practice Exercises

### Exercise 38: Validate Email
```python
# Write function to validate email format
def is_valid_email(email):
    # Check: contains @, contains dot after @, not empty
    # Your code here
    pass

print(is_valid_email("user@example.com"))   # True
print(is_valid_email("invalid"))            # False
print(is_valid_email("user@example"))       # False
```

### Exercise 39: Password Strength
```python
# Write function to check password strength
# Return "Weak", "Medium", or "Strong"
# Strong: length >= 8, has uppercase, lowercase, digit, special char
def password_strength(password):
    # Your code here
    pass

print(password_strength("weak"))                 # Weak
print(password_strength("WeakPass"))             # Medium
print(password_strength("Str0ngP@ss"))           # Strong
```

### Exercise 40: List Chunker
```python
# Write function that splits list into chunks of size n
def chunk_list(lst, size):
    # Your code here
    pass

print(chunk_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Challenge Exercises

### Exercise 41: Function Pipeline
```python
# Create a pipeline that chains multiple functions
def pipeline(functions):
    # Return a function that applies all functions in sequence
    # Your code here
    pass

def double(x): return x * 2
def square(x): return x ** 2
def half(x): return x / 2

process = pipeline([double, square, half])
print(process(5))  # ((5*2)^2)/2 = 50
```

### Exercise 42: Memoization Decorator
```python
# Create memoization decorator for recursive functions
def memoize(func):
    # Your code here
    pass

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))  # Should be fast
```

### Exercise 43: Rate Limiter Decorator
```python
# Create decorator that limits calls per second
def rate_limit(calls_per_second=1):
    # Your code here
    pass

@rate_limit(calls_per_second=2)
def fast_function():
    print("Called")

# Calling multiple times should be rate limited
```

### Exercise 44: Validate Decorator
```python
# Create decorator that validates arguments
def validate(validator):
    # Your code here
    pass

@validate(lambda x: x > 0)
def sqrt(x):
    return x ** 0.5

print(sqrt(25))  # 5.0
# sqrt(-5)  # Should raise ValueError
```

### Exercise 45: Lazy Property Decorator
```python
# Create decorator for lazy properties (computes once)
class lazy_property:
    # Your code here
    pass

class Data:
    def __init__(self):
        self._data = None
    
    @lazy_property
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]

d = Data()
print(d.data)  # Loading data... [1, 2, 3, 4, 5]
print(d.data)  # [1, 2, 3, 4, 5] (no "Loading" message)
```

---

## Submission Guidelines

1. Write your code in the provided function stubs
2. Test your code with the given examples
3. Add additional test cases for edge cases
4. Use meaningful variable names
5. Add docstrings for complex functions
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

*Practice makes perfect! Complete all exercises to master functions in Python! 🐍✨*
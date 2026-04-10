# 📘 IMPLICIT TYPE CONVERSION – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Implicit Conversion?](#what-is-implicit-conversion)
2. [Numeric Type Promotion](#numeric-type-promotion)
3. [Boolean in Numeric Operations](#boolean-in-numeric-operations)
4. [Comparison Type Coercion](#comparison-type-coercion)
5. [Container Type Conversion](#container-type-conversion)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

---

## What is Implicit Conversion?

**Implicit conversion** (also called type coercion) happens automatically when Python converts one data type to another without explicit instruction. This occurs only when the conversion is safe and lossless.

```python
# Implicit conversion examples
x = 10          # int
y = 3.14        # float
z = x + y       # int automatically converted to float
print(z)        # 13.14
print(type(z))  # <class 'float'>

# No implicit conversion between incompatible types
# result = "10" + 5  # TypeError! Can't convert implicitly
```

**Key Characteristics:**
- ✅ Automatic and transparent
- ✅ Only for compatible types
- ✅ Widening conversions (int → float)
- ✅ No data loss (usually)
- ✅ Cannot be disabled

---

## Numeric Type Promotion

### Integer to Float Promotion

```python
# int + float = float
result = 5 + 2.5
print(result)      # 7.5
print(type(result))  # <class 'float'>

# int - float = float
result = 10 - 3.14
print(result)      # 6.86
print(type(result))  # <class 'float'>

# int * float = float
result = 4 * 1.5
print(result)      # 6.0
print(type(result))  # <class 'float'>

# int / int = float (always)
result = 5 / 2
print(result)      # 2.5
print(type(result))  # <class 'float'>

# int // int = int (floor division)
result = 5 // 2
print(result)      # 2
print(type(result))  # <class 'int'>

# Mixed operations in expressions
a = 10        # int
b = 2.5       # float
c = 3         # int
result = a + b * c
print(result)      # 17.5
print(type(result))  # <class 'float'>
```

### Integer to Complex Promotion

```python
# int + complex = complex
result = 5 + (2+3j)
print(result)      # (7+3j)
print(type(result))  # <class 'complex'>

# float + complex = complex
result = 3.14 + (2+3j)
print(result)      # (5.14+3j)
print(type(result))  # <class 'complex'>

# Mixed numeric types
a = 10        # int
b = 2.5       # float
c = (1+2j)    # complex
result = a + b + c
print(result)      # (13.5+2j)
print(type(result))  # <class 'complex'>
```

### Type Promotion Hierarchy

```python
# Promotion order: int → float → complex
def show_promotion(a, b):
    result = a + b
    print(f"{type(a).__name__} + {type(b).__name__} = {type(result).__name__}")

# Same types
show_promotion(5, 3)        # int + int = int
show_promotion(5.0, 3.0)    # float + float = float
show_promotion(5j, 3j)      # complex + complex = complex

# Mixed types
show_promotion(5, 3.0)      # int + float = float
show_promotion(5, 3j)       # int + complex = complex
show_promotion(5.0, 3j)     # float + complex = complex

# Hierarchy visualization
print("\nType Promotion Hierarchy:")
print("  int → float → complex")
print("  int + float = float")
print("  int + complex = complex")
print("  float + complex = complex")
```

---

## Boolean in Numeric Operations

### Boolean as Integer Subclass

```python
# bool is subclass of int
print(issubclass(bool, int))  # True
print(issubclass(int, bool))  # False

# Boolean values have numeric equivalents
print(int(True))   # 1
print(int(False))  # 0

# Boolean in arithmetic
print(True + True)      # 2
print(True + False)     # 1
print(True * 10)        # 10
print(False * 100)      # 0

# Boolean in expressions
count = 0
is_active = True
count += is_active  # Adds 1
print(count)        # 1

# Boolean with float
print(True + 2.5)   # 3.5
print(False * 3.14) # 0.0

# Boolean with complex
print(True + (2+3j))    # (3+3j)
print(False * (2+3j))   # 0j
```

### Boolean in Comparisons

```python
# Boolean comparison with numbers
print(True == 1)    # True
print(False == 0)   # True
print(True == 2)    # False

# Boolean in chained comparisons
x = 1
print(True == x == 1)  # True
print(False == x == 0) # False

# Boolean in conditional expressions
value = 42
result = value if True else 0
print(result)  # 42

# Boolean in list operations
count = sum([True, False, True, True])  # 3
print(count)
```

---

## Comparison Type Coercion

### Numeric Comparisons

```python
# Different numeric types can be compared
print(5 == 5.0)       # True
print(5 == 5.0000001) # False
print(5 > 4.999)      # True
print(5 < 5.1)        # True

# Complex numbers cannot be ordered
try:
    result = (3+4j) > (1+2j)
except TypeError:
    print("Complex numbers cannot be ordered")

# But equality works
print((3+4j) == (3+4j))   # True
print((3+4j) == (3+5j))   # False
```

### String and Number Comparisons

```python
# Python doesn't convert strings to numbers for comparison
try:
    result = "5" > 3
except TypeError:
    print("Cannot compare string with number")

# Explicit conversion required
result = int("5") > 3    # True
result = "5" > str(3)    # True (lexicographic)

# Type checking before comparison
def safe_compare(a, b):
    if type(a) != type(b):
        return None
    return a > b

print(safe_compare(5, "3"))  # None
```

### Sequence Comparisons

```python
# Lists with different element types
list1 = [1, 2, 3]
list2 = [1, 2, 3.0]
print(list1 == list2)   # True (3 vs 3.0)

list3 = [1, 2, "3"]
print(list1 == list3)   # False (3 vs "3")

# Tuple comparisons
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3.0)
print(tuple1 == tuple2)  # True

# Mixed sequences
print([1, 2] == (1, 2))  # False (different types)
```

---

## Container Type Conversion

### Dictionary Key Coercion

```python
# Dictionary keys must be hashable
# int and float can be keys interchangeably
d = {}
d[5] = "int key"
d[5.0] = "float key"  # Overwrites the int key!

print(d)      # {5: 'float key'}
print(d[5])   # 'float key'
print(d[5.0]) # 'float key'

# Different numeric types as keys
d = {1: "one", 1.0: "one float", 1+0j: "one complex"}
print(d)      # Only one key remains
print(len(d)) # 1 (all treated as same key)

# Boolean as dictionary key
d = {True: "true", 1: "one"}
print(d)      # {True: 'one'} (overwrites)
```

### Set Element Coercion

```python
# Sets treat equal values as duplicates
s = {1, 1.0, 1+0j}
print(s)      # {1} (only one element)
print(len(s)) # 1

s = {True, 1}
print(s)      # {True} (True == 1)

s = {False, 0}
print(s)      # {False} (False == 0)

# Different values
s = {1, 2, 2.0, 3+0j}
print(s)      # {1, 2, 3}
```

---

## Real-World Examples

### Example 1: Counter with Mixed Types

```python
class FlexibleCounter:
    def __init__(self):
        self.count = 0
    
    def add(self, value):
        """Add value to counter (handles bool, int, float)"""
        self.count += value
        return self.count
    
    def subtract(self, value):
        """Subtract value from counter"""
        self.count -= value
        return self.count
    
    def reset(self):
        """Reset counter to zero"""
        self.count = 0
    
    def get_count(self):
        return self.count

# Usage
counter = FlexibleCounter()

print("FLEXIBLE COUNTER")
print("=" * 40)

# Adding different types
print(f"Add True: {counter.add(True)}")    # 1 (True → 1)
print(f"Add 5: {counter.add(5)}")          # 6
print(f"Add 2.5: {counter.add(2.5)}")      # 8.5
print(f"Add False: {counter.add(False)}")  # 8.5 (False → 0)

print(f"\nFinal count: {counter.get_count()} (type: {type(counter.get_count()).__name__})")
```

### Example 2: Temperature Converter with Auto Type

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit"""
        # Implicit conversion handles int/float
        return celsius * 9/5 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def process_temperatures(temps, convert_to='celsius'):
        """Process list of temperatures"""
        results = []
        for temp in temps:
            if convert_to == 'celsius':
                converted = TemperatureConverter.fahrenheit_to_celsius(temp)
            else:
                converted = TemperatureConverter.celsius_to_fahrenheit(temp)
            results.append(converted)
        return results

# Usage
print("TEMPERATURE CONVERTER")
print("=" * 40)

# Mixed types in list
temperatures = [32, 68.5, 100, 212.0, True]  # True becomes 1

print(f"Original temps: {temperatures}")
print(f"Types: {[type(t).__name__ for t in temperatures]}")

celsius = TemperatureConverter.process_temperatures(temperatures, 'celsius')
print(f"\nCelsius: {celsius}")
print(f"Types: {[type(t).__name__ for t in celsius]}")

fahrenheit = TemperatureConverter.process_temperatures(celsius, 'fahrenheit')
print(f"\nBack to Fahrenheit: {fahrenheit}")
```

### Example 3: Shopping Cart with Type Flexibility

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0.0
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart (handles int/float/boolean)"""
        # quantity can be int, float, or bool
        item_total = price * quantity
        self.items.append({
            'name': name,
            'price': float(price),  # Ensure float
            'quantity': quantity,
            'item_total': item_total
        })
        self.total += item_total
        return self.total
    
    def apply_discount(self, percentage):
        """Apply discount percentage"""
        # percentage can be int, float, or bool
        discount = self.total * (percentage / 100)
        self.total -= discount
        return discount
    
    def get_total(self):
        return self.total
    
    def summary(self):
        print("\n" + "=" * 50)
        print("SHOPPING CART")
        print("=" * 50)
        for item in self.items:
            print(f"{item['name']}: {item['quantity']} x ${item['price']:.2f} = ${item['item_total']:.2f}")
        print("-" * 50)
        print(f"Total: ${self.total:.2f}")
        print("=" * 50)

# Usage
cart = ShoppingCart()

print("SHOPPING CART WITH TYPE FLEXIBILITY")
print("=" * 40)

# Adding items with mixed types
cart.add_item("Laptop", 999.99, 1)      # int quantity
cart.add_item("Mouse", 29.99, True)     # bool quantity (True=1)
cart.add_item("Keyboard", 79.99, 2)     # int quantity
cart.add_item("USB Cable", 9.99, False) # bool quantity (False=0)

cart.summary()

# Apply discount with int
cart.apply_discount(10)  # 10% off
print(f"\nAfter 10% discount: ${cart.get_total():.2f}")

# Apply discount with float
cart.apply_discount(5.5)  # Additional 5.5% off
print(f"After additional 5.5%: ${cart.get_total():.2f}")
```

### Example 4: Statistical Calculator with Mixed Types

```python
class StatsCalculator:
    @staticmethod
    def mean(data):
        """Calculate mean of mixed numeric data"""
        if not data:
            return 0
        # Implicit conversion handles int/float/bool
        return sum(data) / len(data)
    
    @staticmethod
    def median(data):
        """Calculate median of mixed numeric data"""
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid-1] + sorted_data[mid]) / 2
        return sorted_data[mid]
    
    @staticmethod
    def mode(data):
        """Find mode (most frequent value)"""
        if not data:
            return None
        freq = {}
        for item in data:
            # Convert to consistent type for counting
            key = float(item) if isinstance(item, (int, float, bool)) else item
            freq[key] = freq.get(key, 0) + 1
        return max(freq.items(), key=lambda x: x[1])[0]
    
    @staticmethod
    def variance(data):
        """Calculate variance"""
        if len(data) < 2:
            return 0
        mean_val = StatsCalculator.mean(data)
        squared_diffs = [(x - mean_val) ** 2 for x in data]
        return sum(squared_diffs) / (len(data) - 1)
    
    @staticmethod
    def std_dev(data):
        """Calculate standard deviation"""
        return StatsCalculator.variance(data) ** 0.5

# Usage
print("STATISTICS CALCULATOR")
print("=" * 40)

# Mixed data types
data = [10, 20.5, 30, 40.5, True, False, 25, 35.5]
print(f"Original data: {data}")
print(f"Types: {[type(d).__name__ for d in data]}")

print(f"\nMean: {StatsCalculator.mean(data)}")
print(f"Median: {StatsCalculator.median(data)}")
print(f"Mode: {StatsCalculator.mode(data)}")
print(f"Variance: {StatsCalculator.variance(data):.2f}")
print(f"Std Dev: {StatsCalculator.std_dev(data):.2f}")

# Clean data (explicit conversion where needed)
clean_data = [float(x) for x in data if x is not None]
print(f"\nClean data: {clean_data}")
```

### Example 5: Matrix Operations with Type Promotion

```python
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __add__(self, other):
        """Matrix addition with type promotion"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                # Implicit conversion handles mixed types
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)
    
    def __mul__(self, scalar):
        """Scalar multiplication with type promotion"""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                # scalar can be int, float, bool
                row.append(self.data[i][j] * scalar)
            result.append(row)
        return Matrix(result)
    
    def __str__(self):
        return '\n'.join([' '.join(f'{val:6}' for val in row) for row in self.data])

# Usage
print("MATRIX WITH TYPE PROMOTION")
print("=" * 40)

# Matrix with mixed types
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix([
    [1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5],
    [7.5, 8.5, 9.5]
])

print("Matrix A (int):")
print(A)
print("\nMatrix B (float):")
print(B)

# Addition promotes int to float
print("\nA + B (int + float = float):")
print(A + B)

# Scalar multiplication
print("\nA * 2.5 (int * float = float):")
print(A * 2.5)

print("\nA * True (int * bool = int):")
print(A * True)

print("\nA * False (int * bool = int):")
print(A * False)
```

### Example 6: Flexible Function Parameters

```python
class FlexibleMath:
    @staticmethod
    def add(*args):
        """Add any number of numeric values"""
        result = 0
        for arg in args:
            result += arg  # Implicit conversion handles types
        return result
    
    @staticmethod
    def multiply(*args):
        """Multiply any number of numeric values"""
        if not args:
            return 0
        result = 1
        for arg in args:
            result *= arg
        return result
    
    @staticmethod
    def average(*args):
        """Calculate average of mixed types"""
        if not args:
            return 0
        return FlexibleMath.add(*args) / len(args)
    
    @staticmethod
    def weighted_average(values, weights):
        """Calculate weighted average"""
        if not values or not weights or len(values) != len(weights):
            return 0
        
        total_weight = 0
        weighted_sum = 0
        
        for v, w in zip(values, weights):
            weighted_sum += v * w
            total_weight += w
        
        return weighted_sum / total_weight if total_weight else 0

# Usage
print("FLEXIBLE MATH FUNCTIONS")
print("=" * 40)

# Mixed type addition
print(f"add(1, 2.5, True, False) = {FlexibleMath.add(1, 2.5, True, False)}")
print(f"add(10, 20.5, 30) = {FlexibleMath.add(10, 20.5, 30)}")

# Mixed type multiplication
print(f"multiply(2, 3.5, True) = {FlexibleMath.multiply(2, 3.5, True)}")
print(f"multiply(1.5, 2, False) = {FlexibleMath.multiply(1.5, 2, False)}")

# Average with mixed types
print(f"average(10, 20.5, 30, True) = {FlexibleMath.average(10, 20.5, 30, True)}")

# Weighted average
values = [85, 90, 78, 92]
weights = [True, 2, 1.5, 2.5]  # True becomes 1
print(f"Weighted average: {FlexibleMath.weighted_average(values, weights):.2f}")
```

---

## Common Pitfalls

### Pitfall 1: Unexpected Type Promotion

```python
# Division always returns float
result = 5 / 2
print(result)      # 2.5 (not 2)
print(type(result))  # float

# Floor division returns int
result = 5 // 2
print(result)      # 2
print(type(result))  # int

# Mixed division
result = 5 / 2.0
print(result)      # 2.5
print(type(result))  # float
```

### Pitfall 2: Boolean in Arithmetic

```python
# True and False have numeric values
count = 0
count += True   # Adds 1
count += False  # Adds 0
print(count)    # 1

# Unexpected in conditions
if 1:
    print("True")  # Prints
if True:
    print("True")  # Prints

# But they are not identical
print(True == 1)   # True
print(True is 1)   # False
```

### Pitfall 3: Dictionary Key Collisions

```python
# Different numeric types become same key
d = {}
d[1] = "integer"
d[1.0] = "float"
d[True] = "boolean"

print(d)        # {1: 'boolean'}
print(len(d))   # 1

# Be careful when using mixed numeric keys
def safe_dict_key(key):
    """Use consistent key type"""
    if isinstance(key, bool):
        return str(key)
    return key

d = {}
d[safe_dict_key(1)] = "value"
d[safe_dict_key(1.0)] = "different"  # Won't collide
```

### Pitfall 4: Precision Loss in Promotion

```python
# Large integers converted to float lose precision
large_int = 10**17
large_float = float(large_int)
print(large_int)          # 100000000000000000
print(large_float)        # 1e+17 (approximate)

# Comparison may fail
print(large_int == large_float)  # May be False

# Complex numbers lose real part precision
z = complex(10**17, 0)
print(z)  # (1e+17+0j)
```

---

## Practice Exercises

### Beginner Level

1. **Type Tracker**
   ```python
   # Write a function that tracks types after operations
   # Example: 5 + 2.5 → (7.5, float)
   ```

2. **Mixed List Summer**
   ```python
   # Sum a list containing int, float, bool
   # Example: [1, 2.5, True, False] → 4.5
   ```

3. **Type Promoter**
   ```python
   # Predict and verify type promotion
   # Test: int + float, int + complex, float + complex
   ```

### Intermediate Level

4. **Flexible Calculator**
   ```python
   # Create calculator that handles mixed types
   # Support +, -, *, / with type promotion
   ```

5. **Data Normalizer**
   ```python
   # Normalize mixed list to consistent type
   # Convert all to float or all to int
   ```

6. **Key Collision Detector**
   ```python
   # Detect potential key collisions in dict
   # Warn when different types map to same key
   ```

### Advanced Level

7. **Type-Aware Container**
   ```python
   # Create container that preserves original types
   # Prevent unwanted type coercion
   ```

8. **Expression Evaluator**
   ```python
   # Evaluate expressions with type promotion
   # Track type through operations
   ```

9. **Type Inference Engine**
   ```python
   # Infer result type of expression
   # Based on operand types and operator
   ```

---

## Quick Reference Card

```python
# Numeric promotion hierarchy
# int → float → complex

# int + int = int
5 + 3 = 8

# int + float = float
5 + 2.5 = 7.5

# int + complex = complex
5 + (2+3j) = (7+3j)

# float + complex = complex
2.5 + (2+3j) = (4.5+3j)

# Division always returns float
5 / 2 = 2.5

# Floor division returns int
5 // 2 = 2

# Boolean in arithmetic
True = 1, False = 0

# Comparison coercion
5 == 5.0        # True
5 == "5"        # False (TypeError in Python 3)

# Dictionary keys
{1: "one", 1.0: "float"}  # Only one key

# Set elements
{1, 1.0, True}  # Only one element

# Type checking
isinstance(x, (int, float))  # Check multiple types

# Safe mixed operations
def safe_add(a, b):
    try:
        return a + b
    except TypeError:
        return None
```

## Next Step

- Move to [10_type_checking](/05_python/02_data_types/10_type_checking/README.md) for understanding the Type Checking.
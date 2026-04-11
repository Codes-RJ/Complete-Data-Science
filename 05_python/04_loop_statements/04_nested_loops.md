# 📘 NESTED LOOPS – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Nested Loops?](#what-are-nested-loops)
2. [Nested For Loops](#nested-for-loops)
3. [Nested While Loops](#nested-while-loops)
4. [Mixed Nested Loops](#mixed-nested-loops)
5. [Common Patterns](#common-patterns)
6. [Real-World Examples](#real-world-examples)
7. [Performance Considerations](#performance-considerations)
8. [Common Pitfalls](#common-pitfalls)
9. [Practice Exercises](#practice-exercises)

---

## What are Nested Loops?

**Nested loops** are loops inside other loops. The inner loop completes all its iterations for each single iteration of the outer loop.

```python
# Basic nested loop
for i in range(3):      # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

**Key Characteristics:**
- ✅ Inner loop runs completely for each outer loop iteration
- ✅ Total iterations = outer iterations × inner iterations
- ✅ Used for multi-dimensional data (matrices, grids)
- ✅ Can nest multiple levels deep
- ⚠️ Can become slow with large data sets

---

## Nested For Loops

### Basic Nested For Loops

```python
# 2D pattern
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()  # New line after each row

# Output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

# Triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****

# Reverse triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *****
# ****
# ***
# **
# *
```

### Number Patterns

```python
# Number triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Floyd's triangle
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
```

### Matrix Operations

```python
# Create a matrix
rows, cols = 3, 4
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * j)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)
# Output:
# [0, 0, 0, 0]
# [0, 1, 2, 3]
# [0, 2, 4, 6]

# Sum of all elements
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum: {total}")  # 18

# Find maximum element
max_val = matrix[0][0]
for row in matrix:
    for element in row:
        if element > max_val:
            max_val = element
print(f"Max: {max_val}")  # 6

# Transpose matrix
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[0 for _ in range(len(original))] for _ in range(len(original[0]))]

for i in range(len(original)):
    for j in range(len(original[0])):
        transpose[j][i] = original[i][j]

print("Transpose:")
for row in transpose:
    print(row)
# Output:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
```

---

## Nested While Loops

### Basic Nested While Loops

```python
# Nested while loops
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1

# Output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

# Pattern with while
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

# Output:
# *
# **
# ***
# ****
# *****
```

### While Loop Patterns

```python
# Hollow square
size = 5
i = 0
while i < size:
    j = 0
    while j < size:
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1

# Output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# Diamond pattern
n = 5
i = 1
while i <= n:
    spaces = n - i
    stars = 2 * i - 1
    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1
    k = 0
    while k < stars:
        print("*", end="")
        k += 1
    print()
    i += 1

i = n - 1
while i >= 1:
    spaces = n - i
    stars = 2 * i - 1
    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1
    k = 0
    while k < stars:
        print("*", end="")
        k += 1
    print()
    i -= 1
```

---

## Mixed Nested Loops

### For inside While

```python
# For loop inside while
i = 1
while i <= 5:
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    i += 1

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# While inside for
for i in range(1, 6):
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

---

## Common Patterns

### Pattern 1: Square Patterns

```python
# Solid square
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Number square
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()

# Output:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
```

### Pattern 2: Triangle Patterns

```python
# Right triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Left triangle (with spaces)
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Output:
#     *
#    **
#   ***
#  ****
# *****

# Pascal's triangle
def print_pascal(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)
    
    for row in triangle:
        print(" " * (n - len(row)), " ".join(map(str, row)))

print_pascal(5)
# Output:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
```

### Pattern 3: Matrix Operations

```python
# Matrix addition
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

# Matrix multiplication
def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Cannot multiply: incompatible dimensions")
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Test matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

print("Matrix A x B:")
product = multiply_matrices(A, B)
for row in product:
    print(row)
# Output:
# [58, 64]
# [139, 154]
```

---

## Real-World Examples

### Example 1: Image Processing (Brightness Filter)

```python
class ImageProcessor:
    @staticmethod
    def apply_brightness(image, factor):
        """Apply brightness adjustment to image"""
        result = []
        for row in image:
            new_row = []
            for pixel in row:
                # Clamp values between 0 and 255
                new_value = min(255, max(0, int(pixel * factor)))
                new_row.append(new_value)
            result.append(new_row)
        return result
    
    @staticmethod
    def apply_grayscale(image):
        """Convert RGB image to grayscale"""
        result = []
        for row in image:
            new_row = []
            for pixel in row:
                # Assuming RGB tuple
                gray = int((pixel[0] + pixel[1] + pixel[2]) / 3)
                new_row.append((gray, gray, gray))
            result.append(new_row)
        return result
    
    @staticmethod
    def display_ascii(image, threshold=128):
        """Display image as ASCII art"""
        chars = " .:-=+*#%@"
        for row in image:
            line = ""
            for pixel in row:
                intensity = pixel if isinstance(pixel, int) else sum(pixel) // 3
                idx = int(intensity / 256 * len(chars))
                line += chars[min(idx, len(chars) - 1)]
            print(line)

# Create a simple gradient image
image = []
for i in range(20):
    row = []
    for j in range(40):
        row.append(int((i + j) / 60 * 255))
    image.append(row)

print("Original image (ASCII):")
ImageProcessor.display_ascii(image)

print("\nBrighter image:")
brighter = ImageProcessor.apply_brightness(image, 1.5)
ImageProcessor.display_ascii(brighter)

print("\nDarker image:")
darker = ImageProcessor.apply_brightness(image, 0.5)
ImageProcessor.display_ascii(darker)
```

### Example 2: Sudoku Validator

```python
class SudokuValidator:
    @staticmethod
    def is_valid_row(board, row):
        """Check if row is valid"""
        seen = set()
        for col in range(9):
            val = board[row][col]
            if val != 0:
                if val in seen:
                    return False
                seen.add(val)
        return True
    
    @staticmethod
    def is_valid_col(board, col):
        """Check if column is valid"""
        seen = set()
        for row in range(9):
            val = board[row][col]
            if val != 0:
                if val in seen:
                    return False
                seen.add(val)
        return True
    
    @staticmethod
    def is_valid_box(board, box_row, box_col):
        """Check if 3x3 box is valid"""
        seen = set()
        for i in range(3):
            for j in range(3):
                val = board[box_row + i][box_col + j]
                if val != 0:
                    if val in seen:
                        return False
                    seen.add(val)
        return True
    
    @staticmethod
    def is_valid_sudoku(board):
        """Validate entire Sudoku board"""
        # Check rows and columns
        for i in range(9):
            if not SudokuValidator.is_valid_row(board, i):
                return False
            if not SudokuValidator.is_valid_col(board, i):
                return False
        
        # Check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not SudokuValidator.is_valid_box(board, i, j):
                    return False
        
        return True
    
    @staticmethod
    def print_board(board):
        """Print Sudoku board"""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(board[i][j], end=" ")
            print()

# Test board
valid_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Board:")
SudokuValidator.print_board(valid_board)
print(f"\nIs valid: {SudokuValidator.is_valid_sudoku(valid_board)}")
```

### Example 3: Shopping Cart with Nested Items

```python
class ShoppingCart:
    def __init__(self):
        self.cart = []
    
    def add_order(self, customer, items):
        """Add an order with multiple items"""
        self.cart.append({
            "customer": customer,
            "items": items,
            "total": sum(item["price"] * item["quantity"] for item in items)
        })
    
    def generate_invoice(self):
        """Generate invoice for all orders"""
        grand_total = 0
        
        print("=" * 60)
        print("INVOICE")
        print("=" * 60)
        
        for order in self.cart:
            print(f"\nCustomer: {order['customer']}")
            print("-" * 40)
            print(f"{'Item':<20} {'Qty':<5} {'Price':<10} {'Total':<10}")
            print("-" * 40)
            
            for item in order['items']:
                item_total = item['price'] * item['quantity']
                print(f"{item['name']:<20} {item['quantity']:<5} ${item['price']:<9.2f} ${item_total:<9.2f}")
            
            print("-" * 40)
            print(f"Order Total: ${order['total']:.2f}")
            grand_total += order['total']
        
        print("=" * 60)
        print(f"GRAND TOTAL: ${grand_total:.2f}")
        print("=" * 60)
    
    def find_expensive_items(self, threshold):
        """Find items above price threshold across all orders"""
        expensive = []
        for order in self.cart:
            for item in order['items']:
                if item['price'] > threshold:
                    expensive.append({
                        "customer": order['customer'],
                        "item": item['name'],
                        "price": item['price']
                    })
        return expensive
    
    def get_customer_summary(self):
        """Get summary per customer"""
        summary = {}
        for order in self.cart:
            customer = order['customer']
            if customer not in summary:
                summary[customer] = {
                    'order_count': 0,
                    'total_spent': 0,
                    'items': []
                }
            summary[customer]['order_count'] += 1
            summary[customer]['total_spent'] += order['total']
            for item in order['items']:
                summary[customer]['items'].append(item['name'])
        
        return summary

# Usage
cart = ShoppingCart()

# Add orders
cart.add_order("Alice", [
    {"name": "Laptop", "price": 999.99, "quantity": 1},
    {"name": "Mouse", "price": 29.99, "quantity": 2}
])

cart.add_order("Bob", [
    {"name": "Keyboard", "price": 79.99, "quantity": 1},
    {"name": "Monitor", "price": 299.99, "quantity": 1},
    {"name": "USB Cable", "price": 9.99, "quantity": 3}
])

cart.add_order("Charlie", [
    {"name": "Headphones", "price": 149.99, "quantity": 1},
    {"name": "Mouse Pad", "price": 19.99, "quantity": 2}
])

# Generate invoice
cart.generate_invoice()

# Find expensive items
print("\n" + "=" * 60)
print("EXPENSIVE ITEMS (> $100)")
print("=" * 60)
expensive = cart.find_expensive_items(100)
for item in expensive:
    print(f"  {item['customer']}: {item['item']} - ${item['price']:.2f}")

# Customer summary
print("\n" + "=" * 60)
print("CUSTOMER SUMMARY")
print("=" * 60)
summary = cart.get_customer_summary()
for customer, data in summary.items():
    print(f"\n{customer}:")
    print(f"  Orders: {data['order_count']}")
    print(f"  Total spent: ${data['total_spent']:.2f}")
    print(f"  Items: {', '.join(data['items'])}")
```

### Example 4: Weather Data Analysis

```python
class WeatherAnalyzer:
    def __init__(self):
        self.data = []
    
    def add_weather_data(self, city, temperatures):
        """Add weather data for a city (temperatures by day)"""
        self.data.append({
            "city": city,
            "temperatures": temperatures
        })
    
    def find_hottest_day(self):
        """Find hottest day across all cities"""
        hottest = {"city": "", "day": 0, "temp": -float('inf')}
        
        for city_data in self.data:
            city = city_data["city"]
            for day, temp in enumerate(city_data["temperatures"], 1):
                if temp > hottest["temp"]:
                    hottest = {"city": city, "day": day, "temp": temp}
        
        return hottest
    
    def find_coldest_day(self):
        """Find coldest day across all cities"""
        coldest = {"city": "", "day": 0, "temp": float('inf')}
        
        for city_data in self.data:
            city = city_data["city"]
            for day, temp in enumerate(city_data["temperatures"], 1):
                if temp < coldest["temp"]:
                    coldest = {"city": city, "day": day, "temp": temp}
        
        return coldest
    
    def get_city_average(self, city):
        """Get average temperature for a city"""
        for city_data in self.data:
            if city_data["city"] == city:
                temps = city_data["temperatures"]
                return sum(temps) / len(temps)
        return None
    
    def get_weekly_summary(self):
        """Get weekly summary for all cities"""
        print("=" * 60)
        print("WEEKLY WEATHER SUMMARY")
        print("=" * 60)
        
        for city_data in self.data:
            city = city_data["city"]
            temps = city_data["temperatures"]
            avg = sum(temps) / len(temps)
            max_temp = max(temps)
            min_temp = min(temps)
            
            print(f"\n{city}:")
            print(f"  Temperatures: {temps}")
            print(f"  Average: {avg:.1f}°C")
            print(f"  Max: {max_temp}°C")
            print(f"  Min: {min_temp}°C")
            
            # Find days above average
            above_avg = [day + 1 for day, temp in enumerate(temps) if temp > avg]
            if above_avg:
                print(f"  Days above average: {above_avg}")
        
        print("=" * 60)
    
    def find_heatwave(self, threshold=30, consecutive=3):
        """Find heatwaves (consecutive days above threshold)"""
        heatwaves = []
        
        for city_data in self.data:
            city = city_data["city"]
            temps = city_data["temperatures"]
            
            consecutive_count = 0
            start_day = None
            
            for day, temp in enumerate(temps, 1):
                if temp > threshold:
                    if consecutive_count == 0:
                        start_day = day
                    consecutive_count += 1
                else:
                    if consecutive_count >= consecutive:
                        heatwaves.append({
                            "city": city,
                            "start": start_day,
                            "end": day - 1,
                            "days": consecutive_count
                        })
                    consecutive_count = 0
            
            # Check at the end
            if consecutive_count >= consecutive:
                heatwaves.append({
                    "city": city,
                    "start": start_day,
                    "end": len(temps),
                    "days": consecutive_count
                })
        
        return heatwaves

# Usage
analyzer = WeatherAnalyzer()

# Add weather data (7 days of temperatures)
analyzer.add_weather_data("New York", [22, 24, 28, 31, 33, 30, 26])
analyzer.add_weather_data("Los Angeles", [25, 26, 28, 29, 31, 32, 30])
analyzer.add_weather_data("Chicago", [18, 20, 22, 25, 27, 26, 23])
analyzer.add_weather_data("Miami", [28, 29, 31, 32, 34, 33, 31])

# Generate weekly summary
analyzer.get_weekly_summary()

# Find hottest and coldest days
hottest = analyzer.find_hottest_day()
coldest = analyzer.find_coldest_day()

print(f"\n🌡️ Hottest day: {hottest['city']} Day {hottest['day']} ({hottest['temp']}°C)")
print(f"❄️ Coldest day: {coldest['city']} Day {coldest['day']} ({coldest['temp']}°C)")

# Find heatwaves
heatwaves = analyzer.find_heatwave(threshold=30, consecutive=2)
if heatwaves:
    print("\n🔥 HEATWAVES DETECTED:")
    for hw in heatwaves:
        print(f"  {hw['city']}: Days {hw['start']}-{hw['end']} ({hw['days']} days)")
else:
    print("\nNo heatwaves detected")

# City averages
print("\n📊 CITY AVERAGES:")
for city_data in analyzer.data:
    avg = analyzer.get_city_average(city_data["city"])
    print(f"  {city_data['city']}: {avg:.1f}°C")
```

---

## Performance Considerations

### Time Complexity

```python
# O(n²) - Quadratic time
def nested_loop_2d(n):
    for i in range(n):
        for j in range(n):
            # Operation
            pass
    # Total operations: n × n = n²

# O(n³) - Cubic time
def nested_loop_3d(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # Operation
                pass
    # Total operations: n × n × n = n³

# O(n × m) - Different sizes
def nested_loop_diff(n, m):
    for i in range(n):
        for j in range(m):
            # Operation
            pass
    # Total operations: n × m
```

### Optimization Tips

```python
# ❌ Inefficient - repeated calculations
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 100:  # Condition checked each time
            matrix[i][j] = matrix[i][j] * 2

# ✅ Efficient - move invariant calculations outside
threshold = 100
multiplier = 2
for i in range(len(matrix)):
    row = matrix[i]
    for j in range(len(row)):
        if row[j] > threshold:
            row[j] = row[j] * multiplier

# ❌ Inefficient - nested loop for simple task
def find_max_slow(matrix):
    max_val = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
    return max_val

# ✅ Efficient - use built-in functions
def find_max_fast(matrix):
    return max(max(row) for row in matrix)
```

---

## Common Pitfalls

### Pitfall 1: Wrong Loop Variable

```python
# ❌ WRONG - Using same variable name
for i in range(3):
    for i in range(2):  # Shadows outer i
        print(i)  # Prints inner i only
    print(f"Outer i: {i}")  # i is now 1 (last inner value)

# ✅ CORRECT - Use different names
for outer in range(3):
    for inner in range(2):
        print(f"outer={outer}, inner={inner}")
```

### Pitfall 2: Forgetting to Reset Inner Variable

```python
# ❌ WRONG - Inner variable not reset
j = 0
for i in range(3):
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
# Output: i=0,j=0 i=0,j=1 (inner loop runs only once)

# ✅ CORRECT - Reset inner variable
for i in range(3):
    j = 0
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
```

### Pitfall 3: Deep Nesting (Hard to Read)

```python
# ❌ Too many levels (hard to read)
for a in list1:
    for b in list2:
        for c in list3:
            for d in list4:
                for e in list5:
                    process(a, b, c, d, e)

# ✅ Better - Use itertools.product
from itertools import product
for a, b, c, d, e in product(list1, list2, list3, list4, list5):
    process(a, b, c, d, e)
```

---

## Practice Exercises

### Beginner Level

1. **Multiplication Table**
   ```python
   # Print 10x10 multiplication table using nested loops
   ```

2. **Right Triangle**
   ```python
   # Print right triangle of stars (height 5)
   ```

3. **Matrix Sum**
   ```python
   # Calculate sum of all elements in 3x3 matrix
   ```

### Intermediate Level

4. **Matrix Multiplication**
   ```python
   # Multiply two 3x3 matrices
   ```

5. **Pattern Printing**
   ```python
   # Print diamond pattern of stars (height 5)
   ```

6. **Transpose Matrix**
   ```python
   # Transpose a 4x3 matrix to 3x4
   ```

### Advanced Level

7. **Sudoku Validator**
   ```python
   # Validate if a 9x9 Sudoku board is valid
   ```

8. **Image Filter**
   ```python
   # Apply blur filter to image using nested loops
   ```

9. **Conway's Game of Life**
   ```python
   # Implement one generation of Game of Life
   ```

---

## Quick Reference Card

```python
# Nested for loops
for i in range(outer):
    for j in range(inner):
        # inner loop runs fully for each i

# Nested while loops
i = 0
while i < outer:
    j = 0
    while j < inner:
        # inner loop runs fully for each i
        j += 1
    i += 1

# Mixed loops
for i in range(outer):
    j = 0
    while j < inner:
        j += 1

# Breaking out of nested loops
found = False
for i in range(n):
    if found:
        break
    for j in range(n):
        if condition:
            found = True
            break

# Common patterns
# Sum of matrix elements
total = 0
for row in matrix:
    for val in row:
        total += val

# Find maximum
max_val = matrix[0][0]
for row in matrix:
    for val in row:
        if val > max_val:
            max_val = val

# Create identity matrix
n = 5
identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
```

---

## Next Step

- Move to [exercises.md](exercises.md) to practice all loop concepts with hands-on problems.

---

*Master nested loops to work with multi-dimensional data and create complex patterns! 🐍✨*
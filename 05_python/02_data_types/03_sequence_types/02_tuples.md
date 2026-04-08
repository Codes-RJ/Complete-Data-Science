# 📘 TUPLES (tuple) – COMPLETE GUIDE

## 📌 Table of Contents
1.  [What are Tuples?](#what-are-tuples)
2.  [Creating Tuples](#creating-tuples)
3.  [Accessing Elements](#accessing-elements)
4.  [Tuple Methods](#tuple-methods)
5.  [Tuple Operations](#tuple-operations)
6.  [Tuple Packing and Unpacking](#tuple-packing-and-unpacking)
7.  [Named Tuples](#named-tuples)
8.  [Real-World Examples](#real-world-examples)
9.  [Common Pitfalls](#common-pitfalls)
10. [Performance Tips](#performance-tips)
11. [Practice Exercises](#practice-exercises)

---

## 📖 What are Tuples?

**Tuples** are ordered, immutable collections that can hold items of any type. Once created, tuples cannot be modified (no adding, removing, or changing elements).

```python
# Examples of tuples
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
single = (5,)  # Note: comma required
empty = ()
nested = ((1, 2), (3, 4), (5, 6))
```

**Key Features:**
- ✅ Ordered (items maintain position)
- ✅ Immutable (cannot be changed after creation)
- ✅ Heterogeneous (different types can mix)
- ✅ Hashable (can be used as dictionary keys)
- ✅ Indexable (access by position)
- ✅ Iterable (can loop through)
- ✅ Supports slicing
- ✅ Memory efficient (smaller than lists)

---

## 🎯 Creating Tuples

### Method 1: Parentheses (Optional)

```python
# Using parentheses
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.14, True)

# Parentheses are optional
t4 = 1, 2, 3  # Also a tuple!
print(t4)  # (1, 2, 3)

# Empty tuple
empty = ()
print(empty)  # ()
```

### Method 2: `tuple()` Constructor

```python
# From list
print(tuple([1, 2, 3]))     # (1, 2, 3)

# From string
print(tuple("hello"))       # ('h', 'e', 'l', 'l', 'o')

# From range
print(tuple(range(5)))      # (0, 1, 2, 3, 4)

# From set
print(tuple({1, 2, 3}))     # (1, 2, 3) (order not guaranteed)

# From dictionary (keys only)
print(tuple({'a': 1, 'b': 2}))  # ('a', 'b')

# Empty tuple
empty = tuple()
print(empty)  # ()
```

### Method 3: Single Element Tuple (Important!)

```python
# ❌ WRONG - This is an int, not a tuple!
single = (5)
print(type(single))  # <class 'int'>

# ✅ CORRECT - Comma makes it a tuple
single = (5,)
print(type(single))  # <class 'tuple'>
print(single)        # (5,)

# Without parentheses
single = 5,
print(type(single))  # <class 'tuple'>
```

---

## 🔍 Accessing Elements

### Indexing (Positive and Negative)

```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Positive indexing (0 to len-1)
print(fruits[0])   # "apple"
print(fruits[2])   # "cherry"
print(fruits[4])   # "elderberry"

# Negative indexing (-1 to -len)
print(fruits[-1])  # "elderberry" (last)
print(fruits[-2])  # "date"
print(fruits[-5])  # "apple" (first)

# IndexError if out of range
# print(fruits[10])  # IndexError!
```

### Slicing `[start:end:step]`

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
print(numbers[2:5])    # (2, 3, 4)
print(numbers[:5])     # (0, 1, 2, 3, 4)
print(numbers[5:])     # (5, 6, 7, 8, 9)
print(numbers[:])      # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# With step
print(numbers[::2])    # (0, 2, 4, 6, 8)
print(numbers[1::2])   # (1, 3, 5, 7, 9)
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# Negative indices in slicing
print(numbers[-5:-2])  # (5, 6, 7)
print(numbers[-3:])    # (7, 8, 9)
```

### Iterating Through Tuples

```python
fruits = ("apple", "banana", "cherry")

# Simple iteration
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# With index using enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Output: 0: apple, 1: banana, 2: cherry

# With index starting from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
# Output: 1: apple, 2: banana, 3: cherry

# Reverse iteration
for fruit in reversed(fruits):
    print(fruit)
# Output: cherry, banana, apple
```

---

## 📚 Tuple Methods

Tuples have only two methods (because they're immutable).

### `count(x)`
Returns the number of occurrences of the specified value.

```python
t = (1, 2, 3, 2, 4, 2, 5)

print(t.count(2))   # 3
print(t.count(10))  # 0

# Real use: Check frequency
numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
for num in set(numbers):
    print(f"{num} appears {numbers.count(num)} times")

# Output:
# 1 appears 1 times
# 2 appears 2 times
# 3 appears 3 times
# 4 appears 4 times
```

### `index(x[, start[, end]])`
Returns the index of the first occurrence of the specified value.

```python
fruits = ("apple", "banana", "cherry", "banana", "date")

print(fruits.index("banana"))     # 1
print(fruits.index("banana", 2))  # 3 (search from index 2)

# ValueError if not found
try:
    fruits.index("grape")
except ValueError:
    print("Not found")

# Real use: Find position of element
def find_all(tup, value):
    positions = []
    start = 0
    while True:
        try:
            pos = tup.index(value, start)
            positions.append(pos)
            start = pos + 1
        except ValueError:
            break
    return positions

numbers = (1, 2, 3, 2, 4, 2, 5)
print(find_all(numbers, 2))  # [1, 3, 5]
```

---

## ⚡ Tuple Operations

### Concatenation (`+`)

```python
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)  # (1, 2, 3, 4, 5, 6)

# Creates new tuple (doesn't modify original)
print(a)  # (1, 2, 3) (unchanged)
print(b)  # (4, 5, 6) (unchanged)
```

### Repetition (`*`)

```python
a = (1, 2)
b = a * 3
print(b)  # (1, 2, 1, 2, 1, 2)

# Creates new tuple
print(a)  # (1, 2) (unchanged)
```

### Membership (`in`, `not in`)

```python
fruits = ("apple", "banana", "cherry")

print("banana" in fruits)     # True
print("grape" in fruits)      # False
print("apple" not in fruits)  # False
```

### Comparison Operators

```python
# Lexicographic comparison
a = (1, 2, 3)
b = (1, 2, 3)
c = (1, 2, 4)

print(a == b)  # True
print(a == c)  # False
print(a < c)   # True (compares element by element)

# Works with strings
words1 = ("apple", "banana")
words2 = ("apple", "cherry")
print(words1 < words2)  # True ("banana" < "cherry")
```

### Built-in Functions with Tuples

```python
numbers = (3, 1, 4, 1, 5, 9, 2)

print(len(numbers))      # 7 (number of elements)
print(max(numbers))      # 9 (maximum value)
print(min(numbers))      # 1 (minimum value)
print(sum(numbers))      # 25 (sum of all elements)
print(sorted(numbers))   # [1, 1, 2, 3, 4, 5, 9] (list)
print(tuple(sorted(numbers)))  # (1, 1, 2, 3, 4, 5, 9)

# any() and all()
bool_tuple = (True, False, True)
print(any(bool_tuple))  # True (at least one True)
print(all(bool_tuple))  # False (not all True)

# zip() - combine tuples
names = ("Alice", "Bob", "Charlie")
ages = (30, 25, 35)
pairs = tuple(zip(names, ages))
print(pairs)  # (('Alice', 30), ('Bob', 25), ('Charlie', 35))
```

---

## 📦 Tuple Packing and Unpacking

### Packing
Creating a tuple by grouping values.

```python
# Packing values into tuple
point = 10, 20  # Automatically packed into tuple
print(point)    # (10, 20)
print(type(point))  # <class 'tuple'>

# Multiple values
person = "Alice", 30, "New York"
print(person)  # ('Alice', 30, 'New York')
```

### Unpacking
Extracting tuple values into variables.

```python
# Basic unpacking
point = (10, 20)
x, y = point
print(x)  # 10
print(y)  # 20

# Unpacking must match number of variables
person = ("Alice", 30, "New York")
name, age, city = person
print(name)  # Alice
print(age)   # 30
print(city)  # New York

# Too many variables causes error
# a, b = (1, 2, 3)  # ValueError!

# Using * to capture remaining values
a, *rest = (1, 2, 3, 4, 5)
print(a)     # 1
print(rest)  # [2, 3, 4, 5]

*first, last = (1, 2, 3, 4, 5)
print(first)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Swapping Variables

```python
# Traditional way (needs temporary variable)
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)  # 20 10

# Pythonic way (using tuple unpacking)
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10

# Swap multiple variables
a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)  # 3, 1, 2
```

### Unpacking in Functions

```python
# Returning multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([1, 2, 3, 4, 5])
print(result)  # (1, 5)

# Unpack return value
min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(min_val)  # 1
print(max_val)  # 5

# Using * for variable arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15

# Passing tuple as arguments
numbers = (1, 2, 3, 4, 5)
print(sum_all(*numbers))  # 15 (unpacks tuple)
```

---

## 🏷️ Named Tuples

Named tuples are subclass of tuples with named fields for better code readability.

### Creating Named Tuples

```python
from collections import namedtuple

# Define named tuple
Point = namedtuple('Point', ['x', 'y'])
# Or using string
Point = namedtuple('Point', 'x y')
# Or using comma-separated string
Point = namedtuple('Point', 'x, y')

# Create instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

print(p1)      # Point(x=10, y=20)
print(p1.x)    # 10
print(p1.y)    # 20
print(p1[0])   # 10 (still works as tuple)
```

### Named Tuple Methods

```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instance
alice = Person('Alice', 30, 'New York')

# Access by name
print(alice.name)  # Alice
print(alice.age)   # 30
print(alice.city)  # New York

# Access by index (still works)
print(alice[0])    # Alice
print(alice[1])    # 30

# Convert to dictionary
print(alice._asdict())  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Create new instance with replaced fields
bob = alice._replace(name='Bob', age=25)
print(bob)  # Person(name='Bob', age=25, city='New York')

# Get field names
print(Person._fields)  # ('name', 'age', 'city')

# Make from iterable
data = ['Charlie', 35, 'Boston']
charlie = Person._make(data)
print(charlie)  # Person(name='Charlie', age=35, city='Boston')
```

### Real-World Named Tuple Examples

```python
from collections import namedtuple

# RGB Color
Color = namedtuple('Color', ['red', 'green', 'blue'])
white = Color(255, 255, 255)
black = Color(0, 0, 0)
red = Color(255, 0, 0)

print(f"White: R={white.red}, G={white.green}, B={white.blue}")

# Stock Quote
Stock = namedtuple('Stock', ['symbol', 'price', 'volume', 'change'])
aapl = Stock('AAPL', 175.50, 50000000, 2.5)
print(f"{aapl.symbol}: ${aapl.price} (Change: {aapl.change}%)")

# HTTP Response
Response = namedtuple('Response', ['status_code', 'body', 'headers'])
resp = Response(200, '{"data": "success"}', {'Content-Type': 'application/json'})
if resp.status_code == 200:
    print("Request successful!")
```

---

## 🌍 Real-World Examples

### Example 1: Point and Distance Calculator

```python
from math import sqrt
from collections import namedtuple

# Using regular tuple
point1 = (3, 4)
point2 = (6, 8)

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print(f"Distance: {distance(point1, point2):.2f}")

# Using named tuple (more readable)
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
p2 = Point(6, 8)

def distance_named(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print(f"Distance: {distance_named(p1, p2):.2f}")

# 3D Point
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
p3d = Point3D(1, 2, 3)
print(f"3D Point: ({p3d.x}, {p3d.y}, {p3d.z})")
```

### Example 2: Student Record System

```python
from collections import namedtuple

# Define Student record
Student = namedtuple('Student', ['id', 'name', 'grades', 'major'])

class StudentRecords:
    def __init__(self):
        self.students = []
    
    def add_student(self, id, name, major, *grades):
        student = Student(id, name, grades, major)
        self.students.append(student)
        print(f"Added: {student}")
    
    def get_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None
    
    def calculate_gpa(self, student):
        if not student.grades:
            return 0.0
        return sum(student.grades) / len(student.grades)
    
    def get_honors_students(self, min_gpa=3.5):
        honors = []
        for student in self.students:
            gpa = self.calculate_gpa(student)
            if gpa >= min_gpa:
                honors.append((student, gpa))
        return sorted(honors, key=lambda x: x[1], reverse=True)
    
    def get_students_by_major(self, major):
        return [s for s in self.students if s.major == major]
    
    def generate_report(self):
        print("=" * 60)
        print("STUDENT RECORDS")
        print("=" * 60)
        
        for student in self.students:
            gpa = self.calculate_gpa(student)
            letter = self._get_letter_grade(gpa)
            
            print(f"\n📚 ID: {student.id}")
            print(f"   Name: {student.name}")
            print(f"   Major: {student.major}")
            print(f"   Grades: {student.grades}")
            print(f"   GPA: {gpa:.2f} ({letter})")
        
        print("\n" + "-" * 60)
        
        # Honors students
        honors = self.get_honors_students()
        if honors:
            print("\n🏆 HONORS STUDENTS (GPA ≥ 3.5):")
            for student, gpa in honors:
                print(f"   {student.name} - {gpa:.2f}")
        
        print("=" * 60)
    
    def _get_letter_grade(self, gpa):
        if gpa >= 3.7:
            return 'A'
        elif gpa >= 3.0:
            return 'B'
        elif gpa >= 2.0:
            return 'C'
        else:
            return 'F'

# Usage
records = StudentRecords()

# Add students
records.add_student(1001, "Alice Johnson", "Computer Science", 85, 90, 88, 92)
records.add_student(1002, "Bob Smith", "Mathematics", 75, 80, 78, 82)
records.add_student(1003, "Charlie Brown", "Physics", 95, 98, 92, 96)
records.add_student(1004, "Diana Prince", "Computer Science", 88, 85, 90, 87)

# Generate report
records.generate_report()

# Find student
student = records.get_student(1001)
if student:
    print(f"\nFound: {student.name} - GPA: {records.calculate_gpa(student):.2f}")

# Students by major
cs_students = records.get_students_by_major("Computer Science")
print(f"\nComputer Science Students: {len(cs_students)}")
for s in cs_students:
    print(f"  {s.name}")
```

### Example 3: RGB Color Processor

```python
from collections import namedtuple

# Define RGB color
Color = namedtuple('Color', ['red', 'green', 'blue'])

class ColorProcessor:
    @staticmethod
    def to_hex(color):
        """Convert RGB tuple to hex color code"""
        return f"#{color.red:02x}{color.green:02x}{color.blue:02x}"
    
    @staticmethod
    def from_hex(hex_code):
        """Convert hex color code to RGB tuple"""
        hex_code = hex_code.lstrip('#')
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return Color(r, g, b)
    
    @staticmethod
    def mix(color1, color2, ratio=0.5):
        """Mix two colors with given ratio"""
        r = int(color1.red * ratio + color2.red * (1 - ratio))
        g = int(color1.green * ratio + color2.green * (1 - ratio))
        b = int(color1.blue * ratio + color2.blue * (1 - ratio))
        return Color(r, g, b)
    
    @staticmethod
    def grayscale(color):
        """Convert color to grayscale"""
        gray = int(color.red * 0.299 + color.green * 0.587 + color.blue * 0.114)
        return Color(gray, gray, gray)
    
    @staticmethod
    def invert(color):
        """Invert color"""
        return Color(255 - color.red, 255 - color.green, 255 - color.blue)
    
    @staticmethod
    def brightness(color):
        """Calculate perceived brightness"""
        return (color.red * 0.299 + color.green * 0.587 + color.blue * 0.114) / 255
    
    @staticmethod
    def get_complementary(color):
        """Get complementary color"""
        return Color(255 - color.red, 255 - color.green, 255 - color.blue)

# Define common colors
colors = {
    'red': Color(255, 0, 0),
    'green': Color(0, 255, 0),
    'blue': Color(0, 0, 255),
    'white': Color(255, 255, 255),
    'black': Color(0, 0, 0),
    'yellow': Color(255, 255, 0),
    'cyan': Color(0, 255, 255),
    'magenta': Color(255, 0, 255)
}

print("COLOR PROCESSOR")
print("=" * 40)

# Display colors
for name, color in colors.items():
    hex_code = ColorProcessor.to_hex(color)
    brightness = ColorProcessor.brightness(color)
    print(f"{name:8} RGB{color} -> {hex_code} (brightness: {brightness:.2f})")

# Mix colors
print("\n🎨 COLOR MIXING")
print("-" * 40)

red = colors['red']
blue = colors['blue']
purple = ColorProcessor.mix(red, blue, 0.5)
print(f"Red + Blue = {ColorProcessor.to_hex(purple)}")

yellow = colors['yellow']
blue = colors['blue']
green = ColorProcessor.mix(yellow, blue, 0.5)
print(f"Yellow + Blue = {ColorProcessor.to_hex(green)}")

# Grayscale
print("\n⚫ GRAYSCALE")
print("-" * 40)
for name, color in colors.items():
    gray = ColorProcessor.grayscale(color)
    print(f"{name:8} -> {ColorProcessor.to_hex(gray)}")

# Complementary colors
print("\n🔄 COMPLEMENTARY COLORS")
print("-" * 40)
for name, color in colors.items():
    comp = ColorProcessor.get_complementary(color)
    print(f"{name:8} complement: {ColorProcessor.to_hex(comp)}")

# Color palette generation
print("\n🎨 COLOR PALETTE")
print("-" * 40)

def generate_palette(base_color, steps=5):
    """Generate color palette by varying brightness"""
    palette = []
    for i in range(steps):
        factor = i / (steps - 1)
        r = int(base_color.red * factor)
        g = int(base_color.green * factor)
        b = int(base_color.blue * factor)
        palette.append(Color(r, g, b))
    return palette

blue_palette = generate_palette(colors['blue'])
print("Blue palette:")
for i, color in enumerate(blue_palette):
    print(f"  {i}: {ColorProcessor.to_hex(color)}")
```

### Example 4: Geographic Coordinates

```python
from collections import namedtuple
import math

# Define coordinate types
GeoPoint = namedtuple('GeoPoint', ['latitude', 'longitude', 'name'])
Bounds = namedtuple('Bounds', ['min_lat', 'max_lat', 'min_lon', 'max_lon'])

class Geography:
    @staticmethod
    def haversine_distance(p1, p2):
        """Calculate distance between two points using Haversine formula"""
        R = 6371  # Earth's radius in kilometers
        
        lat1 = math.radians(p1.latitude)
        lon1 = math.radians(p1.longitude)
        lat2 = math.radians(p2.latitude)
        lon2 = math.radians(p2.longitude)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c
    
    @staticmethod
    def find_within_bounds(points, bounds):
        """Find points within given bounds"""
        return [
            p for p in points
            if bounds.min_lat <= p.latitude <= bounds.max_lat
            and bounds.min_lon <= p.longitude <= bounds.max_lon
        ]
    
    @staticmethod
    def find_nearest(points, target):
        """Find nearest point to target"""
        if not points:
            return None
        
        nearest = min(points, key=lambda p: Geography.haversine_distance(p, target))
        distance = Geography.haversine_distance(nearest, target)
        return nearest, distance
    
    @staticmethod
    def get_bounding_box(points):
        """Get bounding box containing all points"""
        if not points:
            return None
        
        min_lat = min(p.latitude for p in points)
        max_lat = max(p.latitude for p in points)
        min_lon = min(p.longitude for p in points)
        max_lon = max(p.longitude for p in points)
        
        return Bounds(min_lat, max_lat, min_lon, max_lon)

# Define cities
cities = [
    GeoPoint(40.7128, -74.0060, "New York"),
    GeoPoint(34.0522, -118.2437, "Los Angeles"),
    GeoPoint(41.8781, -87.6298, "Chicago"),
    GeoPoint(29.7604, -95.3698, "Houston"),
    GeoPoint(39.9526, -75.1652, "Philadelphia"),
    GeoPoint(37.7749, -122.4194, "San Francisco"),
    GeoPoint(42.3601, -71.0589, "Boston"),
    GeoPoint(38.9072, -77.0369, "Washington DC")
]

print("GEOGRAPHIC COORDINATES")
print("=" * 60)

# Display cities
for city in cities:
    print(f"{city.name:15} Lat: {city.latitude:8.4f}, Lon: {city.longitude:8.4f}")

# Calculate distances from New York
print("\n📏 DISTANCES FROM NEW YORK")
print("-" * 40)

nyc = cities[0]
for city in cities[1:]:
    distance = Geography.haversine_distance(nyc, city)
    print(f"{city.name:15} -> {distance:.1f} km")

# Find cities within bounding box
print("\n🗺️ CITIES IN NORTHEAST US")
print("-" * 40)

northeast = Bounds(38.0, 45.0, -80.0, -65.0)
nearby = Geography.find_within_bounds(cities, northeast)
for city in nearby:
    print(f"  {city.name}")

# Find nearest city to a point
print("\n📍 NEAREST CITY TO POINT")
print("-" * 40)

target = GeoPoint(39.5, -90.0, "Target")
nearest, distance = Geography.find_nearest(cities, target)
print(f"Target: {target.latitude}, {target.longitude}")
print(f"Nearest: {nearest.name} ({distance:.1f} km)")

# Get bounding box
print("\n📦 BOUNDING BOX")
print("-" * 40)

bbox = Geography.get_bounding_box(cities)
print(f"Min Latitude: {bbox.min_lat:.4f}")
print(f"Max Latitude: {bbox.max_lat:.4f}")
print(f"Min Longitude: {bbox.min_lon:.4f}")
print(f"Max Longitude: {bbox.max_lon:.4f}")
```

### Example 5: Database Record Handler

```python
from collections import namedtuple
from datetime import datetime

# Define record types
User = namedtuple('User', ['id', 'username', 'email', 'created_at'])
Product = namedtuple('Product', ['id', 'name', 'price', 'stock'])
Order = namedtuple('Order', ['id', 'user_id', 'product_id', 'quantity', 'order_date'])

class Database:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []
        self.next_id = 1
    
    def add_user(self, username, email):
        user = User(self.next_id, username, email, datetime.now())
        self.users.append(user)
        self.next_id += 1
        return user
    
    def add_product(self, name, price, stock):
        product = Product(self.next_id, name, price, stock)
        self.products.append(product)
        self.next_id += 1
        return product
    
    def place_order(self, user_id, product_id, quantity):
        # Check if user exists
        user = self.get_user(user_id)
        if not user:
            print(f"User {user_id} not found")
            return None
        
        # Check if product exists and has stock
        product = self.get_product(product_id)
        if not product:
            print(f"Product {product_id} not found")
            return None
        
        if product.stock < quantity:
            print(f"Insufficient stock for {product.name}")
            return None
        
        # Create order
        order = Order(self.next_id, user_id, product_id, quantity, datetime.now())
        self.orders.append(order)
        self.next_id += 1
        
        # Update stock
        updated_product = product._replace(stock=product.stock - quantity)
        self.update_product(product_id, updated_product)
        
        print(f"Order placed: {quantity}x {product.name} for {user.username}")
        return order
    
    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def get_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def update_product(self, product_id, new_product):
        for i, product in enumerate(self.products):
            if product.id == product_id:
                self.products[i] = new_product
                return True
        return False
    
    def get_user_orders(self, user_id):
        return [order for order in self.orders if order.user_id == user_id]
    
    def get_order_details(self, order):
        user = self.get_user(order.user_id)
        product = self.get_product(order.product_id)
        total = product.price * order.quantity
        return {
            'order_id': order.id,
            'user': user.username,
            'product': product.name,
            'quantity': order.quantity,
            'price': product.price,
            'total': total,
            'date': order.order_date
        }
    
    def generate_report(self):
        print("=" * 70)
        print("DATABASE REPORT")
        print("=" * 70)
        
        print(f"\n👥 USERS ({len(self.users)})")
        print("-" * 40)
        for user in self.users:
            print(f"  {user.id}. {user.username} ({user.email})")
        
        print(f"\n📦 PRODUCTS ({len(self.products)})")
        print("-" * 40)
        for product in self.products:
            print(f"  {product.id}. {product.name} - ${product.price:.2f} (Stock: {product.stock})")
        
        print(f"\n📋 ORDERS ({len(self.orders)})")
        print("-" * 40)
        for order in self.orders:
            details = self.get_order_details(order)
            print(f"  Order #{details['order_id']}: {details['user']} bought {details['quantity']}x {details['product']} (${details['total']:.2f})")
        
        # Sales summary
        total_revenue = 0
        for order in self.orders:
            product = self.get_product(order.product_id)
            total_revenue += product.price * order.quantity
        
        print("\n" + "-" * 40)
        print(f"💰 TOTAL REVENUE: ${total_revenue:.2f}")
        print("=" * 70)

# Usage
db = Database()

# Add users
db.add_user("alice", "alice@example.com")
db.add_user("bob", "bob@example.com")
db.add_user("charlie", "charlie@example.com")

# Add products
db.add_product("Laptop", 999.99, 10)
db.add_product("Mouse", 29.99, 50)
db.add_product("Keyboard", 79.99, 30)
db.add_product("Monitor", 299.99, 15)

# Place orders
db.place_order(1, 1, 1)  # Alice buys 1 Laptop
db.place_order(2, 2, 3)  # Bob buys 3 Mice
db.place_order(1, 3, 2)  # Alice buys 2 Keyboards
db.place_order(3, 4, 1)  # Charlie buys 1 Monitor

# Generate report
db.generate_report()

# Get user's orders
alice = db.get_user(1)
alice_orders = db.get_user_orders(1)
print(f"\n📧 Alice's orders: {len(alice_orders)}")
for order in alice_orders:
    details = db.get_order_details(order)
    print(f"  - {details['quantity']}x {details['product']} (${details['total']:.2f})")
```

### Example 6: Configuration Manager

```python
from collections import namedtuple

# Define config sections
DatabaseConfig = namedtuple('DatabaseConfig', ['host', 'port', 'username', 'password', 'database'])
APIConfig = namedtuple('APIConfig', ['base_url', 'api_key', 'timeout', 'retry_count'])
EmailConfig = namedtuple('EmailConfig', ['smtp_server', 'smtp_port', 'sender', 'recipients'])
LoggingConfig = namedtuple('LoggingConfig', ['level', 'file_path', 'max_size', 'backup_count'])

class ConfigManager:
    def __init__(self):
        self.db_config = None
        self.api_config = None
        self.email_config = None
        self.logging_config = None
    
    def load_database_config(self, host, port, username, password, database):
        self.db_config = DatabaseConfig(host, port, username, password, database)
        return self.db_config
    
    def load_api_config(self, base_url, api_key, timeout=30, retry_count=3):
        self.api_config = APIConfig(base_url, api_key, timeout, retry_count)
        return self.api_config
    
    def load_email_config(self, smtp_server, smtp_port, sender, recipients):
        self.email_config = EmailConfig(smtp_server, smtp_port, sender, recipients)
        return self.email_config
    
    def load_logging_config(self, level, file_path, max_size=10485760, backup_count=5):
        self.logging_config = LoggingConfig(level, file_path, max_size, backup_count)
        return self.logging_config
    
    def get_connection_string(self):
        if not self.db_config:
            return None
        return f"postgresql://{self.db_config.username}:{self.db_config.password}@{self.db_config.host}:{self.db_config.port}/{self.db_config.database}"
    
    def validate_configs(self):
        """Validate all configurations"""
        errors = []
        
        if not self.db_config:
            errors.append("Database configuration missing")
        else:
            if not self.db_config.host:
                errors.append("Database host missing")
            if not self.db_config.port:
                errors.append("Database port missing")
        
        if not self.api_config:
            errors.append("API configuration missing")
        else:
            if not self.api_config.base_url:
                errors.append("API base URL missing")
            if not self.api_config.api_key:
                errors.append("API key missing")
        
        return errors
    
    def display_config(self):
        """Display current configuration"""
        print("=" * 60)
        print("CURRENT CONFIGURATION")
        print("=" * 60)
        
        if self.db_config:
            print("\n📊 DATABASE CONFIGURATION")
            print("-" * 40)
            print(f"  Host: {self.db_config.host}")
            print(f"  Port: {self.db_config.port}")
            print(f"  Username: {self.db_config.username}")
            print(f"  Database: {self.db_config.database}")
            print(f"  Connection String: {self.get_connection_string()}")
        
        if self.api_config:
            print("\n🔌 API CONFIGURATION")
            print("-" * 40)
            print(f"  Base URL: {self.api_config.base_url}")
            print(f"  Timeout: {self.api_config.timeout}s")
            print(f"  Retry Count: {self.api_config.retry_count}")
        
        if self.email_config:
            print("\n📧 EMAIL CONFIGURATION")
            print("-" * 40)
            print(f"  SMTP Server: {self.email_config.smtp_server}")
            print(f"  SMTP Port: {self.email_config.smtp_port}")
            print(f"  Sender: {self.email_config.sender}")
            print(f"  Recipients: {', '.join(self.email_config.recipients)}")
        
        if self.logging_config:
            print("\n📝 LOGGING CONFIGURATION")
            print("-" * 40)
            print(f"  Level: {self.logging_config.level}")
            print(f"  File Path: {self.logging_config.file_path}")
            print(f"  Max Size: {self.logging_config.max_size / 1024 / 1024:.1f} MB")
            print(f"  Backup Count: {self.logging_config.backup_count}")
        
        print("=" * 60)

# Usage
config = ConfigManager()

# Load configurations
config.load_database_config(
    host="localhost",
    port=5432,
    username="admin",
    password="secret123",
    database="myapp_db"
)

config.load_api_config(
    base_url="https://api.example.com",
    api_key="abc123xyz",
    timeout=60,
    retry_count=5
)

config.load_email_config(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    sender="noreply@example.com",
    recipients=["admin@example.com", "support@example.com"]
)

config.load_logging_config(
    level="INFO",
    file_path="/var/log/myapp/app.log",
    max_size=20971520,  # 20 MB
    backup_count=10
)

# Validate
errors = config.validate_configs()
if errors:
    print("CONFIGURATION ERRORS:")
    for error in errors:
        print(f"  ❌ {error}")
else:
    print("✅ All configurations valid!")

# Display configuration
config.display_config()

# Access individual config values
print(f"\n🔗 Database connection: {config.get_connection_string()}")
print(f"🌐 API URL: {config.api_config.base_url}")
print(f"📧 Primary recipient: {config.email_config.recipients[0]}")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Single Element Tuple

```python
# ❌ WRONG - This is an int!
single = (5)
print(type(single))  # <class 'int'>

# ✅ CORRECT - Need comma
single = (5,)
print(type(single))  # <class 'tuple'>

# ✅ CORRECT - Without parentheses
single = 5,
print(type(single))  # <class 'tuple'>
```

### Pitfall 2: Trying to Modify Tuple

```python
# ❌ WRONG - Tuples are immutable
t = (1, 2, 3)
# t[0] = 99  # TypeError!

# ✅ CORRECT - Create new tuple
t = (99,) + t[1:]
print(t)  # (99, 2, 3)

# Or convert to list, modify, convert back
t = (1, 2, 3)
lst = list(t)
lst[0] = 99
t = tuple(lst)
print(t)  # (99, 2, 3)
```

### Pitfall 3: Forgetting Parentheses for Empty Tuple

```python
# ✅ CORRECT
empty = ()
print(type(empty))  # <class 'tuple'>

# ❌ WRONG - This is just a string
not_empty = ("")
print(type(not_empty))  # <class 'str'>
```

### Pitfall 4: Unpacking Mismatch

```python
t = (1, 2, 3)

# ❌ WRONG - Too many variables
# a, b = t  # ValueError!

# ❌ WRONG - Too few variables
# a, b, c, d = t  # ValueError!

# ✅ CORRECT - Match number of variables
a, b, c = t

# ✅ CORRECT - Use * for remaining
a, *rest = t
print(a)     # 1
print(rest)  # [2, 3]
```

---

## ⚡ Performance Tips

### Memory Efficiency

```python
import sys

# Tuples are more memory efficient than lists
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")
# Tuple is typically smaller!

# For large collections, difference is significant
large_list = list(range(10000))
large_tuple = tuple(range(10000))
print(f"Large list: {sys.getsizeof(large_list)} bytes")
print(f"Large tuple: {sys.getsizeof(large_tuple)} bytes")
```

### Speed Comparison

```python
import timeit

# Tuple creation is slightly faster
list_time = timeit.timeit('list(range(1000))', number=10000)
tuple_time = timeit.timeit('tuple(range(1000))', number=10000)

print(f"List creation: {list_time:.4f}s")
print(f"Tuple creation: {tuple_time:.4f}s")

# Tuple unpacking is very fast
def return_tuple():
    return 1, 2, 3

def return_list():
    return [1, 2, 3]

tuple_time = timeit.timeit('a,b,c = return_tuple()', globals=globals(), number=1000000)
list_time = timeit.timeit('a,b,c = return_list()', globals=globals(), number=1000000)

print(f"\nTuple unpacking: {tuple_time:.4f}s")
print(f"List unpacking: {list_time:.4f}s")
```

### When to Use Tuples vs Lists

```python
# ✅ USE TUPLE for:
# - Fixed data that shouldn't change
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# - Dictionary keys
locations = { (40.7128, -74.0060): "New York" }
# - Function return values
def get_min_max(data):
    return min(data), max(data)
# - Configuration data
CONFIG = ('localhost', 8080, 'debug')

# ✅ USE LIST for:
# - Dynamic data that changes
shopping_cart = []
# - Need to add/remove items
queue = [1, 2, 3]
queue.append(4)
# - Need to sort/modify
scores = [85, 92, 78, 90]
scores.sort()
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Tuple Reversal**
   ```python
   # Write a function to reverse a tuple without using [::-1]
   # Example: (1,2,3,4) → (4,3,2,1)
   ```

2. **Tuple to List Conversion**
   ```python
   # Convert tuple to list, modify it, convert back
   # Example: (1,2,3) → add 4 → (1,2,3,4)
   ```

3. **Find Element**
   ```python
   # Find index of element in tuple (handle if not found)
   # Example: (1,2,3,2,4), 2 → [1,3]
   ```

### Intermediate Level

4. **Merge and Sort Tuples**
   ```python
   # Merge two tuples and sort the result
   # Example: (1,3,5) + (2,4,6) → (1,2,3,4,5,6)
   ```

5. **Remove Duplicates**
   ```python
   # Remove duplicates from tuple while preserving order
   # Example: (1,2,3,2,4,3,5) → (1,2,3,4,5)
   ```

6. **Tuple of Squares**
   ```python
   # Create tuple of squares for numbers 1 to n
   # Example: n=5 → (1,4,9,16,25)
   ```

### Advanced Level

7. **Flatten Nested Tuple**
   ```python
   # Flatten nested tuple into single-level tuple
   # Example: (1,(2,3),(4,(5,6))) → (1,2,3,4,5,6)
   ```

8. **Rotate Tuple**
   ```python
   # Rotate tuple by k positions
   # Example: (1,2,3,4,5), k=2 → (4,5,1,2,3)
   ```

9. **Find Common Elements**
   ```python
   # Find common elements between multiple tuples
   # Example: (1,2,3), (2,3,4), (3,4,5) → (3,)
   ```

---

## 📚 Quick Reference Card

```python
# Creation
t = ()                    # Empty tuple
t = (1, 2, 3)            # With parentheses
t = 1, 2, 3              # Without parentheses
t = (5,)                 # Single element (note comma!)
t = tuple([1, 2, 3])     # From iterable

# Accessing
t[i]                     # Get item
t[i:j]                   # Slice
len(t)                   # Get length

# Methods
t.count(x)               # Count occurrences
t.index(x)               # Find index

# Operations
t1 + t2                  # Concatenation
t * 3                    # Repetition
x in t                   # Membership
x not in t               # Non-membership

# Unpacking
a, b, c = t              # Basic unpacking
a, *rest = t             # Star unpacking
*first, last = t         # Capture first/last

# Built-in functions
len(t)                   # Length
max(t)                   # Maximum
min(t)                   # Minimum
sum(t)                   # Sum
sorted(t)                # Sorted list
tuple(sorted(t))         # Sorted tuple

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
p.x, p.y                 # Access by name
p._asdict()              # Convert to dict
p._replace(x=30)         # Create copy with changed field
```

---

*Master tuples for immutable, memory-efficient collections! 🐍✨*
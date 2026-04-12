# 📘 MATH MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Math Module?](#what-is-the-math-module)
2. [Constants](#constants)
3. [Number Theory Functions](#number-theory-functions)
4. [Power and Logarithm Functions](#power-and-logarithm-functions)
5. [Trigonometric Functions](#trigonometric-functions)
6. [Angular Conversion Functions](#angular-conversion-functions)
7. [Hyperbolic Functions](#hyperbolic-functions)
8. [Special Functions](#special-functions)
9. [Real-World Examples](#real-world-examples)
10. [Practice Exercises](#practice-exercises)

---

## What is the Math Module?

The `math` module provides access to mathematical functions and constants. It's one of the most commonly used standard library modules.

```python
import math

# Constants
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
print(math.tau)         # 6.283185307179586

# Functions
print(math.sqrt(16))    # 4.0
print(math.factorial(5)) # 120
print(math.sin(math.pi/2)) # 1.0
```

**Key Characteristics:**
- ✅ All functions return floats (except `math.factorial()`)
- ✅ Domain and range follow mathematical definitions
- ✅ Errors for invalid inputs (e.g., `math.sqrt(-1)` raises `ValueError`)
- ✅ Most functions are thin wrappers around C math library

---

## Constants

### Mathematical Constants

```python
import math

# Pi (π) - ratio of circumference to diameter
print(math.pi)      # 3.141592653589793

# Euler's number (e) - base of natural logarithm
print(math.e)       # 2.718281828459045

# Tau (τ) - 2π, ratio of circumference to radius
print(math.tau)     # 6.283185307179586

# Infinity
print(math.inf)     # inf
print(-math.inf)    # -inf

# Not a Number (NaN)
print(math.nan)     # nan

# Check for infinity or NaN
print(math.isinf(math.inf))   # True
print(math.isnan(math.nan))   # True
```

### Practical Constant Usage

```python
import math

# Circle calculations
radius = 5
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Circle: r={radius}, C={circumference:.2f}, A={area:.2f}")

# Exponential growth
initial = 100
rate = 0.05
time = 10
result = initial * math.e ** (rate * time)
print(f"Growth: {initial} → {result:.2f}")

# Tau for radians (τ rad = full circle)
angle_rad = math.tau / 4  # 90 degrees
print(f"τ/4 rad = {angle_rad} rad")
```

---

## Number Theory Functions

### `math.ceil(x)` – Round Up

```python
import math

print(math.ceil(3.1))   # 4
print(math.ceil(3.9))   # 4
print(math.ceil(-3.1))  # -3
print(math.ceil(-3.9))  # -3
```

### `math.floor(x)` – Round Down

```python
import math

print(math.floor(3.1))   # 3
print(math.floor(3.9))   # 3
print(math.floor(-3.1))  # -4
print(math.floor(-3.9))  # -4
```

### `math.trunc(x)` – Truncate (Remove Decimal)

```python
import math

print(math.trunc(3.1))   # 3
print(math.trunc(3.9))   # 3
print(math.trunc(-3.1))  # -3
print(math.trunc(-3.9))  # -3
```

### `math.fabs(x)` – Absolute Value (Float)

```python
import math

print(math.fabs(-5))    # 5.0
print(math.fabs(3.14))  # 3.14
print(math.fabs(-0.0))  # 0.0
```

### `math.factorial(n)` – Factorial

```python
import math

print(math.factorial(5))   # 120
print(math.factorial(0))   # 1
print(math.factorial(10))  # 3628800

# Raises ValueError for negative numbers
# math.factorial(-1)  # ValueError
```

### `math.comb(n, k)` – Combinations (n choose k)

```python
import math

# Number of ways to choose k items from n items
print(math.comb(5, 2))   # 10
print(math.comb(10, 3))  # 120
print(math.comb(52, 5))  # 2598960 (poker hands)
```

### `math.perm(n, k)` – Permutations

```python
import math

# Number of ways to arrange k items from n items
print(math.perm(5, 2))   # 20
print(math.perm(10, 3))  # 720
print(math.perm(5, 5))   # 120 (same as factorial)
```

### `math.gcd(a, b)` – Greatest Common Divisor

```python
import math

print(math.gcd(48, 18))   # 6
print(math.gcd(100, 25))  # 25
print(math.gcd(17, 19))   # 1 (coprime)

# Works with multiple numbers (Python 3.9+)
print(math.gcd(48, 18, 30))  # 6
```

### `math.lcm(a, b)` – Least Common Multiple (Python 3.9+)

```python
import math

print(math.lcm(4, 6))     # 12
print(math.lcm(12, 18))   # 36
print(math.lcm(3, 5, 7))  # 105
```

### `math.isclose(a, b)` – Compare Floats

```python
import math

# Avoid float comparison issues
print(0.1 + 0.2 == 0.3)                    # False
print(math.isclose(0.1 + 0.2, 0.3))        # True

# Custom tolerance
print(math.isclose(1.0, 1.0001, rel_tol=1e-3))  # True
print(math.isclose(1.0, 1.0001, rel_tol=1e-5))  # False

# Absolute tolerance
print(math.isclose(0.001, 0.002, abs_tol=0.1))  # True
```

### `math.isfinite(x)` – Check Finite

```python
import math

print(math.isfinite(42))      # True
print(math.isfinite(float('inf')))   # False
print(math.isfinite(float('nan')))   # False
```

### `math.isinf(x)` – Check Infinity

```python
import math

print(math.isinf(float('inf')))   # True
print(math.isinf(42))             # False
```

### `math.isnan(x)` – Check NaN

```python
import math

print(math.isnan(float('nan')))   # True
print(math.isnan(42))             # False
```

---

## Power and Logarithm Functions

### `math.pow(x, y)` – Power (x^y)

```python
import math

print(math.pow(2, 3))     # 8.0
print(math.pow(5, 2))     # 25.0
print(math.pow(4, 0.5))   # 2.0 (square root)
print(math.pow(8, 1/3))   # 2.0 (cube root)

# Note: returns float, even for integers
```

### `math.sqrt(x)` – Square Root

```python
import math

print(math.sqrt(16))      # 4.0
print(math.sqrt(2))       # 1.4142135623730951
print(math.sqrt(0))       # 0.0

# Raises ValueError for negative numbers
# math.sqrt(-1)  # ValueError
```

### `math.exp(x)` – Exponential (e^x)

```python
import math

print(math.exp(1))    # 2.718281828459045
print(math.exp(2))    # 7.38905609893065
print(math.exp(-1))   # 0.36787944117144233
```

### `math.log(x[, base])` – Logarithm

```python
import math

# Natural logarithm (base e)
print(math.log(math.e))     # 1.0
print(math.log(100))        # 4.605170185988092

# Logarithm with specified base
print(math.log(100, 10))    # 2.0
print(math.log(8, 2))       # 3.0

# Raises ValueError for x <= 0
# math.log(-1)  # ValueError
```

### `math.log10(x)` – Base-10 Logarithm

```python
import math

print(math.log10(100))    # 2.0
print(math.log10(1000))   # 3.0
print(math.log10(1))      # 0.0
```

### `math.log2(x)` – Base-2 Logarithm

```python
import math

print(math.log2(8))       # 3.0
print(math.log2(16))      # 4.0
print(math.log2(1))       # 0.0
```

### `math.expm1(x)` – e^x - 1 (Accurate for small x)

```python
import math

# More accurate than math.exp(x) - 1 for small x
print(math.expm1(1e-10))   # 1.00000000005e-10
print(math.exp(1e-10) - 1) # 1.00000000005e-10 (less accurate)
```

### `math.log1p(x)` – ln(1 + x) (Accurate for small x)

```python
import math

# More accurate than math.log(1 + x) for small x
print(math.log1p(1e-10))   # 9.9999999995e-11
print(math.log(1 + 1e-10)) # 9.9999999995e-11 (less accurate)
```

---

## Trigonometric Functions

### Sine, Cosine, Tangent

```python
import math

# Sine (sin)
print(math.sin(math.pi/2))   # 1.0
print(math.sin(0))           # 0.0
print(math.sin(math.pi))     # 1.2246467991473532e-16 (approximately 0)

# Cosine (cos)
print(math.cos(0))           # 1.0
print(math.cos(math.pi))     # -1.0
print(math.cos(math.pi/2))   # 6.123233995736766e-17 (approximately 0)

# Tangent (tan)
print(math.tan(0))           # 0.0
print(math.tan(math.pi/4))   # 0.9999999999999999 (approximately 1)
```

### Inverse Trigonometric Functions

```python
import math

# Arc sine (inverse sine)
print(math.asin(1))          # 1.5707963267948966 (π/2)
print(math.asin(0))          # 0.0
print(math.asin(-1))         # -1.5707963267948966

# Arc cosine (inverse cosine)
print(math.acos(1))          # 0.0
print(math.acos(0))          # 1.5707963267948966 (π/2)
print(math.acos(-1))         # 3.141592653589793 (π)

# Arc tangent (inverse tangent)
print(math.atan(1))          # 0.7853981633974483 (π/4)
print(math.atan(0))          # 0.0
print(math.atan(-1))         # -0.7853981633974483

# Arc tangent of y/x (quadrant-aware)
print(math.atan2(1, 1))      # 0.7853981633974483 (π/4)
print(math.atan2(-1, -1))    # -2.356194490192345 (different quadrant)
```

### Practical Trigonometry

```python
import math

# Convert degrees to radians for trig functions
angle_deg = 45
angle_rad = math.radians(angle_deg)

sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

print(f"sin(45°) = {sin_val:.4f}")  # 0.7071
print(f"cos(45°) = {cos_val:.4f}")  # 0.7071
print(f"tan(45°) = {tan_val:.4f}")  # 1.0000

# Verify identity: sin²θ + cos²θ = 1
identity = sin_val**2 + cos_val**2
print(f"sin²θ + cos²θ = {identity:.4f}")  # 1.0000
```

---

## Angular Conversion Functions

### `math.degrees(x)` – Radians to Degrees

```python
import math

print(math.degrees(math.pi))      # 180.0
print(math.degrees(math.pi/2))    # 90.0
print(math.degrees(math.pi/4))    # 45.0
print(math.degrees(1))            # 57.29577951308232
```

### `math.radians(x)` – Degrees to Radians

```python
import math

print(math.radians(180))   # 3.141592653589793
print(math.radians(90))    # 1.5707963267948966
print(math.radians(45))    # 0.7853981633974483
print(math.radians(1))     # 0.017453292519943295
```

---

## Hyperbolic Functions

### Basic Hyperbolic Functions

```python
import math

# Hyperbolic sine
print(math.sinh(0))       # 0.0
print(math.sinh(1))       # 1.1752011936438014

# Hyperbolic cosine
print(math.cosh(0))       # 1.0
print(math.cosh(1))       # 1.5430806348152437

# Hyperbolic tangent
print(math.tanh(0))       # 0.0
print(math.tanh(1))       # 0.7615941559557649
```

### Inverse Hyperbolic Functions

```python
import math

# Inverse hyperbolic sine
print(math.asinh(0))      # 0.0
print(math.asinh(1))      # 0.881373587019543

# Inverse hyperbolic cosine
print(math.acosh(1))      # 0.0
print(math.acosh(2))      # 1.3169578969248166

# Inverse hyperbolic tangent
print(math.atanh(0))      # 0.0
print(math.atanh(0.5))    # 0.5493061443340549
```

---

## Special Functions

### `math.gamma(x)` – Gamma Function

```python
import math

# Γ(n) = (n-1)! for positive integers
print(math.gamma(5))      # 24.0 (4!)
print(math.gamma(6))      # 120.0 (5!)

# For non-integers
print(math.gamma(0.5))    # 1.772453850905516 (√π)
```

### `math.lgamma(x)` – Natural Log of Gamma

```python
import math

# More accurate for large values
print(math.lgamma(100))   # log(99!)
print(math.log(math.gamma(100)))  # Same but less accurate
```

### `math.erf(x)` – Error Function

```python
import math

# Used in statistics and probability
print(math.erf(0))        # 0.0
print(math.erf(1))        # 0.8427007929497149
print(math.erf(-1))       # -0.8427007929497149
```

### `math.erfc(x)` – Complementary Error Function

```python
import math

# erfc(x) = 1 - erf(x)
print(math.erfc(0))       # 1.0
print(math.erfc(1))       # 0.1572992070502851
```

---

## Real-World Examples

### Example 1: Circle Calculator

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def arc_length(self, angle_deg):
        """Calculate arc length for given angle in degrees"""
        angle_rad = math.radians(angle_deg)
        return self.radius * angle_rad
    
    def sector_area(self, angle_deg):
        """Calculate sector area for given angle in degrees"""
        angle_rad = math.radians(angle_deg)
        return 0.5 * self.radius ** 2 * angle_rad

# Usage
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Circumference: {circle.circumference:.2f}")
print(f"Area: {circle.area:.2f}")
print(f"Arc length (90°): {circle.arc_length(90):.2f}")
print(f"Sector area (90°): {circle.sector_area(90):.2f}")
```

### Example 2: Statistical Calculator

```python
import math

class StatisticsCalculator:
    @staticmethod
    def mean(data):
        return sum(data) / len(data)
    
    @staticmethod
    def variance(data):
        if len(data) < 2:
            return 0
        mean_val = StatisticsCalculator.mean(data)
        squared_diffs = [(x - mean_val) ** 2 for x in data]
        return sum(squared_diffs) / (len(data) - 1)
    
    @staticmethod
    def std_dev(data):
        return math.sqrt(StatisticsCalculator.variance(data))
    
    @staticmethod
    def correlation(x, y):
        """Pearson correlation coefficient"""
        if len(x) != len(y) or len(x) < 2:
            return 0
        
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(xi ** 2 for xi in x)
        sum_y2 = sum(yi ** 2 for yi in y)
        
        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
        
        if denominator == 0:
            return 0
        return numerator / denominator

# Usage
data = [10, 20, 30, 40, 50]
print(f"Data: {data}")
print(f"Mean: {StatisticsCalculator.mean(data)}")
print(f"Variance: {StatisticsCalculator.variance(data):.2f}")
print(f"Std Dev: {StatisticsCalculator.std_dev(data):.2f}")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
print(f"Correlation: {StatisticsCalculator.correlation(x, y):.4f}")
```

### Example 3: Physics Calculations

```python
import math

class Physics:
    G = 6.67430e-11  # Gravitational constant
    
    @staticmethod
    def projectile_range(velocity, angle_deg, g=9.81):
        """Calculate range of projectile"""
        angle_rad = math.radians(angle_deg)
        return (velocity ** 2 * math.sin(2 * angle_rad)) / g
    
    @staticmethod
    def projectile_height(velocity, angle_deg, g=9.81):
        """Calculate maximum height of projectile"""
        angle_rad = math.radians(angle_deg)
        return (velocity ** 2 * math.sin(angle_rad) ** 2) / (2 * g)
    
    @staticmethod
    def gravitational_force(m1, m2, r):
        """Calculate gravitational force between two masses"""
        return Physics.G * m1 * m2 / (r ** 2)
    
    @staticmethod
    def kinetic_energy(mass, velocity):
        """Calculate kinetic energy"""
        return 0.5 * mass * velocity ** 2
    
    @staticmethod
    def orbital_velocity(central_mass, radius):
        """Calculate orbital velocity"""
        return math.sqrt(Physics.G * central_mass / radius)

# Usage
velocity = 100  # m/s
angle = 45      # degrees

print("Projectile Motion:")
print(f"Range: {Physics.projectile_range(velocity, angle):.2f} m")
print(f"Max Height: {Physics.projectile_height(velocity, angle):.2f} m")

# Earth orbit
earth_mass = 5.972e24  # kg
earth_radius = 6371000  # m
print(f"\nOrbital velocity at surface: {Physics.orbital_velocity(earth_mass, earth_radius):.2f} m/s")
```

### Example 4: Financial Calculations

```python
import math

class Finance:
    @staticmethod
    def compound_interest(principal, rate, years, compounds_per_year=1):
        """Calculate compound interest"""
        return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    
    @staticmethod
    def present_value(future_value, rate, years):
        """Calculate present value"""
        return future_value / (1 + rate) ** years
    
    @staticmethod
    def loan_payment(principal, rate, years):
        """Calculate monthly loan payment"""
        monthly_rate = rate / 12
        months = years * 12
        if monthly_rate == 0:
            return principal / months
        payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        return payment
    
    @staticmethod
    def roi(initial, final):
        """Calculate Return on Investment"""
        return (final - initial) / initial * 100

# Usage
principal = 10000
rate = 0.05  # 5%
years = 10

print(f"Principal: ${principal}")
print(f"Rate: {rate * 100}%")
print(f"Years: {years}")
print(f"Compound Interest: ${Finance.compound_interest(principal, rate, years):.2f}")

loan = 200000
rate = 0.04  # 4% annual
years = 30
print(f"\nLoan: ${loan}")
print(f"Monthly Payment: ${Finance.loan_payment(loan, rate, years):.2f}")

initial_investment = 5000
final_value = 7500
print(f"\nROI: {Finance.roi(initial_investment, final_value):.1f}%")
```

### Example 5: Geometry Calculator

```python
import math

class Geometry:
    @staticmethod
    def distance(x1, y1, x2, y2):
        """Euclidean distance between two points"""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    @staticmethod
    def polygon_area(points):
        """Calculate area of polygon using shoelace formula"""
        n = len(points)
        area = 0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2
    
    @staticmethod
    def sphere_volume(radius):
        return (4/3) * math.pi * radius ** 3
    
    @staticmethod
    def sphere_surface_area(radius):
        return 4 * math.pi * radius ** 2
    
    @staticmethod
    def cone_volume(radius, height):
        return (1/3) * math.pi * radius ** 2 * height
    
    @staticmethod
    def cylinder_volume(radius, height):
        return math.pi * radius ** 2 * height

# Usage
print("Distance between (0,0) and (3,4):", Geometry.distance(0, 0, 3, 4))

points = [(0, 0), (4, 0), (4, 3), (0, 3)]
print(f"Rectangle area: {Geometry.polygon_area(points)}")

radius = 5
print(f"Sphere volume: {Geometry.sphere_volume(radius):.2f}")
print(f"Sphere surface area: {Geometry.sphere_surface_area(radius):.2f}")
```

---

## Practice Exercises

### Beginner Level

1. **Circle Calculator**
   ```python
   # Write function that takes radius and returns area and circumference
   ```

2. **Hypotenuse**
   ```python
   # Calculate hypotenuse of right triangle given two legs
   ```

3. **Temperature Conversion**
   ```python
   # Convert Celsius to Fahrenheit and vice versa
   ```

### Intermediate Level

4. **Quadratic Solver**
   ```python
   # Solve quadratic equation using math.sqrt()
   ```

5. **Trigonometric Table**
   ```python
   # Print sin, cos, tan for angles 0° to 90° in 15° increments
   ```

6. **Statistical Functions**
   ```python
   # Implement mean, variance, std_dev without statistics module
   ```

### Advanced Level

7. **Projectile Simulator**
   ```python
   # Calculate position of projectile over time
   ```

8. **Earthquake Magnitude**
   ```python
   # Convert between Richter scale and energy using logarithms
   ```

9. **GPS Distance**
   ```python
   # Calculate great-circle distance between two GPS coordinates
   ```

---

## Quick Reference Card

```python
import math

# Constants
math.pi          # π = 3.14159...
math.e           # e = 2.71828...
math.tau         # τ = 2π = 6.28318...
math.inf         # Infinity
math.nan         # Not a Number

# Rounding
math.ceil(x)     # Round up
math.floor(x)    # Round down
math.trunc(x)    # Remove decimal

# Number theory
math.factorial(n)   # n!
math.comb(n, k)     # n choose k
math.perm(n, k)     # n P k
math.gcd(a, b)      # Greatest common divisor
math.lcm(a, b)      # Least common multiple

# Powers and logs
math.sqrt(x)        # √x
math.pow(x, y)      # x^y
math.exp(x)         # e^x
math.log(x)         # ln(x)
math.log10(x)       # log₁₀(x)
math.log2(x)        # log₂(x)

# Trigonometry (radians)
math.sin(x)         # sine
math.cos(x)         # cosine
math.tan(x)         # tangent
math.asin(x)        # arc sine
math.acos(x)        # arc cosine
math.atan(x)        # arc tangent
math.atan2(y, x)    # arc tangent of y/x

# Conversion
math.degrees(x)     # radians → degrees
math.radians(x)     # degrees → radians

# Hyperbolic
math.sinh(x)        # hyperbolic sine
math.cosh(x)        # hyperbolic cosine
math.tanh(x)        # hyperbolic tangent

# Checks
math.isclose(a, b)  # Compare floats
math.isfinite(x)    # Check finite
math.isinf(x)       # Check infinity
math.isnan(x)       # Check NaN
```

---

## Next Step

- Move to [02_cmath.md](02_cmath.md) to learn about complex number mathematics.

---

*Master the math module for all your mathematical computing needs! 🐍✨*
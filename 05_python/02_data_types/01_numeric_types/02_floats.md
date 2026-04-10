# 📘 FLOATS (float) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Floats?](#what-are-floats)
2. [Creating Floats](#creating-floats)
3. [All Float Methods](#all-float-methods)
4. [Math Module Functions](#math-module-functions)
5. [Precision and Special Values](#precision-and-special-values)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Practice Exercises](#practice-exercises)

---

## 📖 What are Floats?

**Floats** (floating-point numbers) represent real numbers with decimal points. They follow the IEEE 754 double-precision standard (64-bit).

```python
# Examples of floats
pi = 3.14159
negative = -0.5
zero_point = 0.0
scientific = 1.2e-4  # 0.00012
```

**Key Features:**
- ✅ Decimal point support
- ✅ Scientific notation
- ✅ Special values: `inf`, `-inf`, `nan`
- ⚠️ Limited precision (~15 decimal digits)
- ⚠️ Binary representation can cause rounding errors

---

## 🎯 Creating Floats

### Method 1: Direct Assignment

```python
# Standard decimal notation
price = 19.99
temperature = -5.5
percentage = 0.75

# Leading zero optional
decimal1 = .5    # 0.5
decimal2 = -.25  # -0.25

# Scientific notation
large = 1.5e6    # 1,500,000.0
small = 2.5e-4   # 0.00025
electron = 9.109e-31  # Electron mass

print(large)     # 1500000.0
print(small)     # 0.00025
```

### Method 2: Using `float()` Constructor

```python
# From integer
print(float(42))      # 42.0

# From string
print(float("3.14"))  # 3.14
print(float("inf"))   # inf
print(float("-inf"))  # -inf
print(float("nan"))   # nan

# From boolean
print(float(True))    # 1.0
print(float(False))   # 0.0

# Invalid conversions (raise ValueError)
# float("abc")   # ValueError
# float("3.14.5") # ValueError
```

### Method 3: Using Underscores (Python 3.6+)

```python
# Makes large/small numbers readable
pi_approx = 3.141_592_653_589_793
avogadro = 6.022_140_76e23
planck = 6.626_070_15e-34

print(pi_approx)  # 3.141592653589793
```

---

## 🔧 All Float Methods

### 1. `is_integer()` – Check if float is whole number

```python
# Check if decimal part is zero
print((3.0).is_integer())   # True
print((3.14).is_integer())  # False
print((-5.0).is_integer())  # True
print((0.0).is_integer())   # True

# Real use: Validating input
def is_whole_number(value):
    try:
        return float(value).is_integer()
    except ValueError:
        return False

print(is_whole_number("5.0"))    # True
print(is_whole_number("5.5"))    # False
print(is_whole_number("abc"))    # False
```

### 2. `as_integer_ratio()` – Get fraction representation

```python
# Convert float to numerator/denominator
f = 0.75
ratio = f.as_integer_ratio()
print(f"{f} = {ratio[0]}/{ratio[1]}")  # 0.75 = 3/4

# Examples
numbers = [0.5, 0.3333333333333333, 1.25, -0.2]
for num in numbers:
    ratio = num.as_integer_ratio()
    print(f"{num:12} = {ratio[0]:6d}/{ratio[1]:6d} = {ratio[0]/ratio[1]}")

# Output:
# 0.5          =      3/     6 = 0.5
# 0.3333333333 = 6004799503160661/18014398509481984 = 0.3333333333333333
# 1.25         =      5/     4 = 1.25
# -0.2         =     -1/     5 = -0.2
```

### 3. `hex()` – Convert to hexadecimal string

```python
# Convert float to hex representation
f = 3.14159
hex_repr = f.hex()
print(f"3.14159 in hex: {hex_repr}")
# Output: 0x1.921f9f01b866ep+1

# Real use: Storing floats exactly
def save_float_exact(value, filename):
    with open(filename, 'w') as f:
        f.write(value.hex())

def load_float_exact(filename):
    with open(filename, 'r') as f:
        return float.fromhex(f.read())

# Save and restore without precision loss
original = 1/3  # 0.3333333333333333
save_float_exact(original, 'temp.txt')
restored = load_float_exact('temp.txt')
print(f"Original: {original}")
print(f"Restored: {restored}")
print(f"Equal: {original == restored}")  # True
```

### 4. `fromhex()` – Create float from hex (class method)

```python
# Recreate float from hex string
hex_string = '0x1.921f9f01b866ep+1'
restored = float.fromhex(hex_string)
print(restored)  # 3.14159

# Network transmission example
def float_to_hex(value):
    return value.hex()

def hex_to_float(hex_str):
    return float.fromhex(hex_str)

# Send over network
data = 123.456
hex_data = float_to_hex(data)
print(f"Sending: {hex_data}")

# Receive and restore
received = hex_to_float(hex_data)
print(f"Received: {received}")
```

### 5. `conjugate()` – Returns self (for complex compatibility)

```python
# For floats, just returns the number itself
x = 3.14
print(x.conjugate())  # 3.14

# Useful for generic numeric code
def process_number(n):
    if hasattr(n, 'conjugate'):
        return n.conjugate()
    return n

print(process_number(3.14))   # 3.14
print(process_number(2+3j))   # (2-3j)
```

---

## 📐 Math Module Functions

The `math` module provides many functions for floats.

### Basic Mathematical Functions

```python
import math

x = 16.0
y = 2.5

print(f"Square root: {math.sqrt(x)}")        # 4.0
print(f"Power: {math.pow(x, 2)}")            # 256.0
print(f"Exponential: {math.exp(1)}")         # 2.718281828459045
print(f"Natural log: {math.log(10)}")        # 2.302585092994046
print(f"Log base 10: {math.log10(100)}")     # 2.0
print(f"Log base 2: {math.log2(8)}")         # 3.0
print(f"Absolute: {math.fabs(-5.5)}")        # 5.5
```

### Trigonometric Functions

```python
import math

# Convert degrees to radians
angle_deg = 45
angle_rad = math.radians(angle_deg)

print(f"sin(45°): {math.sin(angle_rad):.4f}")    # 0.7071
print(f"cos(45°): {math.cos(angle_rad):.4f}")    # 0.7071
print(f"tan(45°): {math.tan(angle_rad):.4f}")    # 1.0000

print(f"arcsin(0.7071): {math.degrees(math.asin(0.7071)):.1f}°")  # 45.0°
print(f"arccos(0.7071): {math.degrees(math.acos(0.7071)):.1f}°")  # 45.0°
print(f"arctan(1): {math.degrees(math.atan(1)):.1f}°")            # 45.0°

# Convert radians to degrees
rad = math.pi / 4
print(f"{rad} rad = {math.degrees(rad)}°")  # 0.785 rad = 45.0°
```

### Rounding Functions

```python
import math

num = 3.14159

print(f"Original: {num}")

# Round to nearest integer
print(f"round(): {round(num)}")      # 3

# Floor (always down)
print(f"floor(): {math.floor(num)}") # 3

# Ceil (always up)
print(f"ceil(): {math.ceil(num)}")   # 4

# Truncate (towards zero)
print(f"trunc(): {math.trunc(num)}") # 3

# Round with decimal places
print(f"round(2 decimals): {round(num, 2)}")  # 3.14
print(f"round(3 decimals): {round(num, 3)}")  # 3.142

# Different rounding behaviors
negative = -3.14
print(f"\nNegative number: {negative}")
print(f"round(): {round(negative)}")    # -3
print(f"floor(): {math.floor(negative)}")  # -4 (always down!)
print(f"ceil(): {math.ceil(negative)}")    # -3 (always up!)
print(f"trunc(): {math.trunc(negative)}")  # -3 (towards zero)
```

### Constants in Math Module

```python
import math

print(f"π (pi): {math.pi}")          # 3.141592653589793
print(f"e: {math.e}")                # 2.718281828459045
print(f"τ (tau): {math.tau}")        # 6.283185307179586
print(f"Infinity: {math.inf}")       # inf
print(f"NaN: {math.nan}")            # nan

# Real use: Circle calculations
radius = 5.0
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Circle area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

---

## ⚡ Precision and Special Values

### Special Float Values

```python
# Infinity
positive_inf = float('inf')
negative_inf = float('-inf')
inf_from_math = math.inf

print(f"Positive infinity: {positive_inf}")
print(f"Negative infinity: {negative_inf}")
print(f"inf + 5 = {positive_inf + 5}")  # inf
print(f"inf * -1 = {positive_inf * -1}")  # -inf

# Not a Number (NaN)
nan = float('nan')
nan_from_math = math.nan

print(f"NaN: {nan}")
print(f"NaN == NaN: {nan == nan}")  # False! NaN is not equal to itself
print(f"math.isnan(nan): {math.isnan(nan)}")  # True

# Operations with special values
print(f"inf * 0 = {positive_inf * 0}")     # nan
print(f"inf / inf = {positive_inf / positive_inf}")  # nan
print(f"inf - inf = {positive_inf - positive_inf}")  # nan
```

### Checking Special Values

```python
import math

def analyze_float(value):
    """Analyze a float value"""
    if math.isnan(value):
        return "Not a Number (NaN)"
    elif math.isinf(value):
        if value > 0:
            return "Positive Infinity"
        else:
            return "Negative Infinity"
    elif value == 0:
        return "Zero"
    else:
        return f"Normal number: {value}"

# Test different values
test_values = [0.0, 3.14, float('inf'), float('-inf'), float('nan')]

for val in test_values:
    print(f"{val:10} → {analyze_float(val)}")
```

**Output:**
```
0.0        → Zero
3.14       → Normal number: 3.14
inf        → Positive Infinity
-inf       → Negative Infinity
nan        → Not a Number (NaN)
```

### Precision Issues

```python
# Float precision problem
print(0.1 + 0.2)  # 0.30000000000000004 (not 0.3!)
print(0.1 + 0.2 == 0.3)  # False!

# Why? Binary representation can't exactly represent some decimals
print(f"0.1 in binary: {0.1:.50f}")
print(f"0.2 in binary: {0.2:.50f}")
print(f"0.3 in binary: {0.3:.50f}")

# Solutions:
# 1. Use tolerance
tolerance = 1e-10
result = 0.1 + 0.2
print(f"Using tolerance: {abs(result - 0.3) < tolerance}")  # True

# 2. Use math.isclose()
import math
print(f"math.isclose(): {math.isclose(0.1 + 0.2, 0.3)}")  # True

# 3. Use Decimal for exact decimal math
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```

---

## 🌍 Real-World Examples

### Example 1: Loan EMI Calculator

```python
import math

def calculate_emi(principal, annual_rate, months):
    """
    Calculate EMI for a loan
    
    Formula: EMI = P * r * (1+r)^n / ((1+r)^n - 1)
    where:
    P = principal loan amount
    r = monthly interest rate
    n = number of months
    """
    monthly_rate = annual_rate / 12 / 100
    emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    return emi

def loan_amortization(principal, annual_rate, months):
    """Generate loan amortization schedule"""
    monthly_rate = annual_rate / 12 / 100
    emi = calculate_emi(principal, annual_rate, months)
    
    remaining = principal
    schedule = []
    
    for month in range(1, months + 1):
        interest = remaining * monthly_rate
        principal_paid = emi - interest
        remaining -= principal_paid
        
        schedule.append({
            'month': month,
            'emi': emi,
            'interest': interest,
            'principal': principal_paid,
            'remaining': max(0, remaining)
        })
        
        if remaining <= 0:
            break
    
    return schedule

# Calculate loan details
loan_amount = 500000  # ₹5,00,000
interest_rate = 8.5   # 8.5% per annum
tenure = 24           # 24 months

print("=" * 60)
print("LOAN EMI CALCULATOR")
print("=" * 60)
print(f"Loan Amount: ₹{loan_amount:,.2f}")
print(f"Interest Rate: {interest_rate}% per annum")
print(f"Tenure: {tenure} months")
print("=" * 60)

emi = calculate_emi(loan_amount, interest_rate, tenure)
total_payment = emi * tenure
total_interest = total_payment - loan_amount

print(f"Monthly EMI: ₹{emi:,.2f}")
print(f"Total Payment: ₹{total_payment:,.2f}")
print(f"Total Interest: ₹{total_interest:,.2f}")
print("=" * 60)

# Show first 5 months of amortization
schedule = loan_amortization(loan_amount, interest_rate, tenure)
print("\nFirst 5 months amortization:")
print(f"{'Month':<6} {'EMI':<12} {'Interest':<12} {'Principal':<12} {'Remaining':<12}")
print("-" * 60)

for payment in schedule[:5]:
    print(f"{payment['month']:<6} ₹{payment['emi']:<10,.2f} ₹{payment['interest']:<10,.2f} ₹{payment['principal']:<10,.2f} ₹{payment['remaining']:<10,.2f}")
```

**Output:**
```
============================================================
LOAN EMI CALCULATOR
============================================================
Loan Amount: ₹500,000.00
Interest Rate: 8.5% per annum
Tenure: 24 months
============================================================
Monthly EMI: ₹22,710.55
Total Payment: ₹545,053.20
Total Interest: ₹45,053.20
============================================================

First 5 months amortization:
Month  EMI          Interest     Principal    Remaining   
------------------------------------------------------------
1      ₹22,710.55   ₹3,541.67    ₹19,168.89   ₹480,831.11 
2      ₹22,710.55   ₹3,405.89    ₹19,304.66   ₹461,526.45 
3      ₹22,710.55   ₹3,269.15    ₹19,441.40   ₹442,085.05 
4      ₹22,710.55   ₹3,131.44    ₹19,579.11   ₹422,505.94 
5      ₹22,710.55   ₹2,992.75    ₹19,717.80   ₹402,788.14 
```

### Example 2: Temperature Monitoring System

```python
import math
from datetime import datetime

class TemperatureMonitor:
    def __init__(self, threshold=25.0):
        self.threshold = threshold
        self.readings = []
        self.alerts = []
    
    def add_reading(self, temperature, timestamp=None):
        """Add a temperature reading"""
        if timestamp is None:
            timestamp = datetime.now()
        
        reading = {
            'temp': temperature,
            'time': timestamp,
            'status': 'HIGH' if temperature > self.threshold else 'NORMAL'
        }
        
        self.readings.append(reading)
        
        if temperature > self.threshold:
            self.alerts.append(reading)
        
        return reading
    
    def get_statistics(self):
        """Calculate temperature statistics"""
        if not self.readings:
            return None
        
        temps = [r['temp'] for r in self.readings]
        
        return {
            'avg': sum(temps) / len(temps),
            'min': min(temps),
            'max': max(temps),
            'std_dev': self._std_deviation(temps),
            'count': len(temps),
            'alerts': len(self.alerts)
        }
    
    def _std_deviation(self, values):
        """Calculate standard deviation"""
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)
    
    def generate_report(self):
        """Generate temperature report"""
        stats = self.get_statistics()
        if not stats:
            return "No data available"
        
        print("=" * 60)
        print("TEMPERATURE MONITORING REPORT")
        print("=" * 60)
        print(f"Period: {self.readings[0]['time']} to {self.readings[-1]['time']}")
        print(f"Total Readings: {stats['count']}")
        print(f"Alerts Triggered: {stats['alerts']}")
        print("-" * 60)
        print(f"Average Temperature: {stats['avg']:.2f}°C")
        print(f"Minimum Temperature: {stats['min']:.2f}°C")
        print(f"Maximum Temperature: {stats['max']:.2f}°C")
        print(f"Standard Deviation: {stats['std_dev']:.3f}°C")
        print("=" * 60)
        
        # Show alert times
        if self.alerts:
            print("\nALERT LOG:")
            for alert in self.alerts:
                print(f"  {alert['time']}: {alert['temp']:.1f}°C (exceeds {self.threshold}°C)")

# Simulate temperature readings
monitor = TemperatureMonitor(threshold=30.0)

# Simulated temperature data (hourly for 24 hours)
simulated_temps = [
    22.5, 23.1, 22.8, 23.4, 24.2, 25.1,  # 12 AM - 5 AM
    26.3, 27.8, 28.9, 30.2, 31.5, 32.1,  # 6 AM - 11 AM
    32.5, 33.2, 32.8, 31.9, 30.5, 29.2,  # 12 PM - 5 PM
    27.8, 26.4, 25.1, 24.3, 23.5, 22.9   # 6 PM - 11 PM
]

print("Recording temperature data...")
for hour, temp in enumerate(simulated_temps):
    monitor.add_reading(temp)
    status = "⚠️ ALERT" if temp > monitor.threshold else "✓"
    print(f"Hour {hour:2d}: {temp:4.1f}°C {status}")

print("\n")
monitor.generate_report()
```

### Example 3: Currency Converter with Commission

```python
class CurrencyConverter:
    def __init__(self, rates, commission_rate=0.01):
        """
        rates: dict of exchange rates (base: USD)
        commission_rate: percentage (0.01 = 1%)
        """
        self.rates = rates
        self.commission_rate = commission_rate
        self.min_commission = 2.0
        self.max_commission = 50.0
    
    def convert(self, amount, from_currency, to_currency):
        """Convert currency with commission"""
        if from_currency == to_currency:
            return amount
        
        # Convert to USD first (base)
        if from_currency != 'USD':
            amount_usd = amount / self.rates[from_currency]
        else:
            amount_usd = amount
        
        # Convert from USD to target
        if to_currency != 'USD':
            result = amount_usd * self.rates[to_currency]
        else:
            result = amount_usd
        
        # Apply commission
        commission = result * self.commission_rate
        commission = max(self.min_commission, min(commission, self.max_commission))
        
        net_result = result - commission
        
        return {
            'gross': result,
            'commission': commission,
            'net': net_result,
            'rate_used': self.rates[to_currency] if to_currency != 'USD' else 1.0
        }
    
    def get_best_rate(self, amount, from_currency, to_currency, options):
        """Find best rate among multiple providers"""
        best = None
        best_result = -1
        
        for provider, rate in options.items():
            self.rates[to_currency] = rate
            result = self.convert(amount, from_currency, to_currency)
            
            if result['net'] > best_result:
                best_result = result['net']
                best = provider
        
        return best, best_result

# Exchange rates (1 USD = X currency)
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'INR': 83.45,
    'JPY': 148.32,
    'CAD': 1.35,
    'AUD': 1.52,
    'CNY': 7.18
}

converter = CurrencyConverter(exchange_rates, commission_rate=0.02)  # 2% commission

print("=" * 60)
print("CURRENCY CONVERTER")
print("=" * 60)

# Example conversions
conversions = [
    (100, 'USD', 'EUR'),
    (500, 'USD', 'INR'),
    (1000, 'EUR', 'GBP'),
    (50, 'USD', 'JPY')
]

for amount, from_curr, to_curr in conversions:
    result = converter.convert(amount, from_curr, to_curr)
    
    print(f"\n{amount:.2f} {from_curr} → {to_curr}")
    print(f"  Gross amount: {result['gross']:.2f} {to_curr}")
    print(f"  Commission: {result['commission']:.2f} {to_curr}")
    print(f"  Net amount: {result['net']:.2f} {to_curr}")
    print(f"  Exchange rate: 1 {from_curr} = {result['rate_used']:.4f} {to_curr}")

# Compare rates from different providers
print("\n" + "=" * 60)
print("BEST RATE COMPARISON")
print("=" * 60)

providers = {
    'Bank A': 83.45,
    'Bank B': 83.32,
    'Forex C': 83.68,
    'Online D': 83.15
}

amount = 1000
best_provider, best_amount = converter.get_best_rate(amount, 'USD', 'INR', providers)

print(f"Converting $1,000 USD to INR:")
for provider, rate in providers.items():
    converter.rates['INR'] = rate
    result = converter.convert(amount, 'USD', 'INR')
    print(f"  {provider}: ₹{result['net']:.2f} (rate: {rate})")

print(f"\n✅ Best provider: {best_provider} with ₹{best_amount:.2f}")
```

### Example 4: Circle Geometry Calculator

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def arc_length(self, angle_degrees):
        """Calculate arc length for given angle"""
        angle_rad = math.radians(angle_degrees)
        return self.radius * angle_rad
    
    def sector_area(self, angle_degrees):
        """Calculate sector area for given angle"""
        angle_rad = math.radians(angle_degrees)
        return 0.5 * self.radius ** 2 * angle_rad
    
    def segment_area(self, angle_degrees):
        """Calculate segment area for given angle"""
        angle_rad = math.radians(angle_degrees)
        return 0.5 * self.radius ** 2 * (angle_rad - math.sin(angle_rad))
    
    def distance_between_points(self, x1, y1, x2, y2):
        """Calculate distance between two points"""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def point_on_circle(self, angle_degrees):
        """Get coordinates of point on circle at given angle"""
        angle_rad = math.radians(angle_degrees)
        x = self.radius * math.cos(angle_rad)
        y = self.radius * math.sin(angle_rad)
        return (x, y)

# Create circles with different radii
radii = [1.0, 2.5, 5.0, 7.5, 10.0]

print("=" * 80)
print("CIRCLE GEOMETRY CALCULATOR")
print("=" * 80)

for radius in radii:
    circle = Circle(radius)
    
    print(f"\nCircle with radius = {radius:.1f} units")
    print("-" * 40)
    print(f"Diameter: {circle.diameter:.2f} units")
    print(f"Circumference: {circle.circumference:.2f} units")
    print(f"Area: {circle.area:.2f} sq units")
    
    # Calculate for 90° angle
    angle = 90
    print(f"\nFor {angle}° angle:")
    print(f"  Arc length: {circle.arc_length(angle):.2f} units")
    print(f"  Sector area: {circle.sector_area(angle):.2f} sq units")
    print(f"  Segment area: {circle.segment_area(angle):.2f} sq units")
    
    # Point on circle
    point = circle.point_on_circle(45)
    print(f"  Point at 45°: ({point[0]:.2f}, {point[1]:.2f})")

# Compare circles
print("\n" + "=" * 80)
print("CIRCLE COMPARISON")
print("=" * 80)
print(f"{'Radius':<8} {'Area':<12} {'Circumference':<14} {'Area Ratio':<12}")
print("-" * 80)

base_circle = Circle(1.0)
for radius in radii:
    circle = Circle(radius)
    area_ratio = circle.area / base_circle.area
    print(f"{radius:<8.1f} {circle.area:<12.2f} {circle.circumference:<14.2f} {area_ratio:<12.2f}")
```

### Example 5: Grade Calculator with Weighted Average

```python
class GradeCalculator:
    def __init__(self):
        self.categories = {}
        self.grades = []
    
    def add_category(self, name, weight, grade):
        """Add a grade category with weight"""
        self.categories[name] = {
            'weight': weight,
            'grade': grade
        }
    
    def calculate_weighted_average(self):
        """Calculate weighted average"""
        total_weight = 0
        weighted_sum = 0
        
        for category, data in self.categories.items():
            weighted_sum += data['grade'] * data['weight']
            total_weight += data['weight']
        
        if total_weight == 0:
            return 0
        
        return weighted_sum / total_weight
    
    def get_letter_grade(self, score):
        """Convert numeric score to letter grade"""
        if score >= 90:
            return ('A', 'Excellent!')
        elif score >= 80:
            return ('B', 'Good job!')
        elif score >= 70:
            return ('C', 'Satisfactory')
        elif score >= 60:
            return ('D', 'Need improvement')
        else:
            return ('F', 'Failed')
    
    def generate_report(self):
        """Generate complete grade report"""
        final_score = self.calculate_weighted_average()
        letter, remark = self.get_letter_grade(final_score)
        
        print("=" * 60)
        print("GRADE REPORT")
        print("=" * 60)
        print(f"{'Category':<15} {'Grade':<8} {'Weight':<8} {'Contribution':<12}")
        print("-" * 60)
        
        for category, data in self.categories.items():
            contribution = data['grade'] * data['weight']
            print(f"{category:<15} {data['grade']:<8.1f} {data['weight']:<8.2f} {contribution:<12.2f}")
        
        print("-" * 60)
        print(f"{'Final Score':<15} {final_score:<8.2f}")
        print(f"{'Letter Grade':<15} {letter:<8}")
        print(f"{'Remark':<15} {remark:<8}")
        print("=" * 60)

# Example usage
calculator = GradeCalculator()

# Add grade categories
calculator.add_category("Homework", 0.20, 88.5)
calculator.add_category("Quizzes", 0.15, 92.0)
calculator.add_category("Midterm", 0.30, 78.5)
calculator.add_category("Project", 0.15, 85.0)
calculator.add_category("Final Exam", 0.20, 91.5)

calculator.generate_report()

# What-if scenarios
print("\nWHAT-IF ANALYSIS")
print("=" * 60)

current_score = calculator.calculate_weighted_average()
print(f"Current score: {current_score:.2f}")

# Calculate needed score on final to achieve different grades
final_weight = 0.20
target_grades = {'A': 90, 'B': 80, 'C': 70}

for grade, target in target_grades.items():
    needed = (target - current_score * (1 - final_weight)) / final_weight
    needed = max(0, min(100, needed))
    print(f"To get {grade}: Need {needed:.1f}% on remaining work")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Float Equality Comparison

```python
# ❌ WRONG - Direct comparison
if 0.1 + 0.2 == 0.3:
    print("Equal")  # This won't print!

# ✅ CORRECT - Using tolerance
tolerance = 1e-10
if abs((0.1 + 0.2) - 0.3) < tolerance:
    print("Equal")  # This works

# ✅ CORRECT - Using math.isclose()
import math
if math.isclose(0.1 + 0.2, 0.3):
    print("Equal")  # This works

# ✅ CORRECT - Using Decimal for exact math
from decimal import Decimal
if Decimal('0.1') + Decimal('0.2') == Decimal('0.3'):
    print("Equal")  # Perfect!
```

### Pitfall 2: Division by Zero

```python
# ❌ WRONG - This crashes
# result = 5 / 0  # ZeroDivisionError

# ✅ CORRECT - Check before dividing
def safe_divide(a, b):
    if b == 0:
        return float('inf') if a > 0 else float('-inf') if a < 0 else float('nan')
    return a / b

print(safe_divide(5, 0))   # inf
print(safe_divide(-5, 0))  # -inf
print(safe_divide(0, 0))   # nan
```

### Pitfall 3: Unexpected Rounding

```python
# Rounding can be surprising
print(round(2.5))   # 2 (bankers rounding - rounds to even)
print(round(3.5))   # 4 (bankers rounding)

# For traditional rounding
def traditional_round(x):
    return int(x + 0.5) if x >= 0 else int(x - 0.5)

print(traditional_round(2.5))  # 3
print(traditional_round(3.5))  # 4

# For decimal rounding
from decimal import Decimal, ROUND_HALF_UP
print(Decimal('2.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP))  # 3
```

### Pitfall 4: Float as Dictionary Keys

```python
# ❌ BAD - Floats as keys (due to precision)
d = {}
d[0.1 + 0.2] = "value"
print(0.3 in d)  # False (different keys!)

# ✅ GOOD - Use integers or strings
d = {}
d["0.3"] = "value"
# OR use Decimal
from decimal import Decimal
d[Decimal('0.3')] = "value"
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Temperature Converter**
   ```python
   # Convert between Celsius, Fahrenheit, and Kelvin
   # C to F: (C * 9/5) + 32
   # C to K: C + 273.15
   ```

2. **Simple Interest Calculator**
   ```python
   # Calculate simple interest: I = P * r * t
   # P = principal, r = rate, t = time
   ```

3. **Average Calculator**
   ```python
   # Calculate average of multiple numbers
   # Handle empty list case
   ```

### Intermediate Level

4. **BMI Calculator**
   ```python
   # BMI = weight(kg) / height(m)²
   # Classify: Underweight, Normal, Overweight, Obese
   ```

5. **Shopping Cart Total**
   ```python
   # Calculate total with tax and discounts
   # Apply percentage discounts and fixed discounts
   ```

6. **Distance Between Points**
   ```python
   # Calculate Euclidean distance between 2D points
   # Formula: √[(x2-x1)² + (y2-y1)²]
   ```

### Advanced Level

7. **Statistical Calculator**
   ```python
   # Calculate mean, median, mode, variance, std deviation
   # Handle edge cases (empty list, single element)
   ```

8. **Investment Growth Calculator**
   ```python
   # Compound interest with monthly contributions
   # Show year-by-year growth
   ```

9. **Scientific Function Plotter**
   ```python
   # Generate (x,y) points for mathematical functions
   # Handle domain errors (log of negative, sqrt of negative)
   ```

---

## 📚 Quick Reference Card

```python
# Creation
x = 3.14                 # Direct
x = float(42)           # From int
x = float("3.14")       # From string
x = 1.2e-4              # Scientific

# Methods
x.is_integer()          # Check if whole
x.as_integer_ratio()    # Get fraction
x.hex()                 # To hex string
float.fromhex(hex_str)  # From hex

# Math functions
import math
math.sqrt(x)            # Square root
math.pow(x, y)          # Power
math.floor(x)           # Round down
math.ceil(x)            # Round up
round(x, n)             # Round to n decimals

# Special values
float('inf')            # Infinity
float('-inf')           # Negative infinity
float('nan')            # Not a Number
math.isinf(x)           # Check infinity
math.isnan(x)           # Check NaN
math.isclose(a, b)      # Safe comparison

# Constants
math.pi                 # 3.14159...
math.e                  # 2.71828...
math.tau                # 6.28318...
```

## Next Step

- Go to [03_complex_numbers.md](03_complex_numbers.md) for completion of Numeric Data Types.

---

*Master floats, and you'll handle real-world decimal calculations with confidence! 🐍✨*

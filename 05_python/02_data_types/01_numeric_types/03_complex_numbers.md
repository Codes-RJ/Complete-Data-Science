# 📘 COMPLEX NUMBERS (complex) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Complex Numbers?](#what-are-complex-numbers)
2. [Creating Complex Numbers](#creating-complex-numbers)
3. [Complex Properties](#complex-properties)
4. [Complex Operations](#complex-operations)
5. [Cmath Module Functions](#cmath-module-functions)
6. [Polar and Rectangular Forms](#polar-and-rectangular-forms)
7. [Real-World Examples](#real-world-examples)
8. [Common Pitfalls](#common-pitfalls)
9. [Practice Exercises](#practice-exercises)

---

## 📖 What are Complex Numbers?

**Complex numbers** are numbers that have both a real part and an imaginary part, written as `a + bj` where:
- `a` = real part
- `b` = imaginary part
- `j` = imaginary unit (√-1)

```python
# Examples of complex numbers
z1 = 3 + 4j      # Real=3, Imag=4
z2 = -2 - 5j     # Real=-2, Imag=-5
z3 = 5j          # Pure imaginary (Real=0)
z4 = 2 + 0j      # Pure real (Imag=0)
```

**Key Features:**
- ✅ Used in engineering, physics, and signal processing
- ✅ Supports all arithmetic operations
- ✅ Can be represented in polar form (magnitude + angle)
- ⚠️ Cannot be compared with <, > (only == and !=)
- ⚠️ Cannot be used as dictionary keys if imaginary part ≠ 0

---

## 🎯 Creating Complex Numbers

### Method 1: Direct Assignment (using `j`)

```python
# Standard form
z1 = 3 + 4j
z2 = -2.5 + 3.7j
z3 = 5j              # Pure imaginary
z4 = 2 + 0j          # Pure real

print(z1)  # (3+4j)
print(z2)  # (-2.5+3.7j)
print(z3)  # 5j
print(z4)  # (2+0j)

# Note: Use 'j' not 'i'
# z = 3 + 4i  # SyntaxError!
```

### Method 2: Using `complex()` Constructor

```python
# From two numbers
z1 = complex(3, 4)    # (3+4j)
z2 = complex(5)       # (5+0j)
z3 = complex(0, 5)    # 5j

print(z1)  # (3+4j)
print(z2)  # (5+0j)
print(z3)  # 5j

# From string
z4 = complex("3+4j")  # (3+4j)
z5 = complex("5j")    # 5j
z6 = complex("2")     # (2+0j)

print(z4)  # (3+4j)
print(z5)  # 5j
print(z6)  # (2+0j)

# Invalid strings (raise ValueError)
# complex("3+4")    # Missing 'j'
# complex("3 + 4j") # Spaces not allowed
```

### Method 3: Using `cmath.rect()` (from polar coordinates)

```python
import cmath

# Create from magnitude and phase (angle)
magnitude = 5
phase_rad = 0.9273  # About 53.13 degrees
z = cmath.rect(magnitude, phase_rad)
print(z)  # (3.000... + 4.000...j)

# Using degrees
import math
phase_deg = 53.13
phase_rad = math.radians(phase_deg)
z = cmath.rect(5, phase_rad)
print(z)  # Approximately (3+4j)
```

---

## 🔧 Complex Properties

Complex numbers have three built-in properties (no methods other than `conjugate()`).

### 1. `.real` – Access Real Part

```python
z = 3 + 4j
print(f"Real part: {z.real}")  # 3.0
print(type(z.real))            # <class 'float'>

# Real part is always a float
z2 = 5 + 0j
print(z2.real)  # 5.0 (not 5)

# Extracting real parts from list
complex_numbers = [3+4j, 2-5j, -1+3j, 4-2j]
real_parts = [z.real for z in complex_numbers]
print(real_parts)  # [3.0, 2.0, -1.0, 4.0]
```

### 2. `.imag` – Access Imaginary Part

```python
z = 3 + 4j
print(f"Imaginary part: {z.imag}")  # 4.0
print(type(z.imag))                  # <class 'float'>

# Pure imaginary number
z2 = 5j
print(z2.imag)  # 5.0

# Extracting imaginary parts
complex_numbers = [3+4j, 2-5j, -1+3j, 4-2j]
imag_parts = [z.imag for z in complex_numbers]
print(imag_parts)  # [4.0, -5.0, 3.0, -2.0]
```

### 3. `.conjugate()` – Return Complex Conjugate

```python
z = 3 + 4j
print(f"Original: {z}")
print(f"Conjugate: {z.conjugate()}")  # (3-4j)

# Conjugate of conjugate returns original
print(z.conjugate().conjugate())  # (3+4j)

# Real numbers are their own conjugate
z2 = 5 + 0j
print(z2.conjugate())  # (5+0j)

# Useful property: z * conjugate(z) = |z|²
z = 3 + 4j
product = z * z.conjugate()
print(f"z * conj(z) = {product}")  # (25+0j)
print(f"|z|² = {abs(z)**2}")        # 25.0
```

---

## 📐 Complex Operations

### Arithmetic Operations

```python
a = 3 + 4j
b = 1 - 2j

print(f"a = {a}")
print(f"b = {b}")
print()

# Addition
print(f"a + b = {a + b}")  # (4+2j)

# Subtraction
print(f"a - b = {a - b}")  # (2+6j)

# Multiplication
print(f"a * b = {a * b}")  # (11-2j)
# (3+4j)*(1-2j) = 3*1 + 3*(-2j) + 4j*1 + 4j*(-2j)
# = 3 -6j +4j -8j² = 3 -2j +8 = 11 -2j

# Division
print(f"a / b = {a / b}")  # (-1+2j)

# Power
print(f"a ** 2 = {a ** 2}")  # (-7+24j)
print(f"a ** 3 = {a ** 3}")  # (-117+44j)
```

### Comparison Operations

```python
a = 3 + 4j
b = 3 + 4j
c = 1 + 2j

# Equality (works)
print(f"a == b: {a == b}")  # True
print(f"a == c: {a == c}")  # False
print(f"a != c: {a != c}")  # True

# Ordering (does NOT work - raises TypeError)
# print(a > b)   # TypeError: '>' not supported
# print(a < c)   # TypeError: '<' not supported

# Compare magnitudes instead
print(f"|a| > |c|: {abs(a) > abs(c)}")  # True
```

### Built-in Functions with Complex

```python
z = 3 + 4j

# abs() - Magnitude (modulus)
print(f"Magnitude: {abs(z)}")  # 5.0 (√(3²+4²))

# complex() - Create complex
print(complex(5, -2))  # (5-2j)

# bool() - False only for 0+0j
print(bool(3+4j))   # True
print(bool(0+0j))   # False
print(bool(0j))     # False

# float() and int() - Don't work directly!
# float(z)  # TypeError: can't convert complex to float
# int(z)    # TypeError: can't convert complex to int

# Convert real part instead
print(float(z.real))  # 3.0
print(int(z.real))    # 3
```

---

## 📚 Cmath Module Functions

The `cmath` (complex math) module provides mathematical functions for complex numbers.

### Basic Functions

```python
import cmath
import math

z = 3 + 4j

# Phase (angle in radians)
phase = cmath.phase(z)
print(f"Phase: {phase} rad")                    # 0.927295...
print(f"Phase: {math.degrees(phase)}°")         # 53.1301°

# Polar coordinates (r, φ)
polar = cmath.polar(z)
print(f"Polar form: r={polar[0]:.2f}, φ={polar[1]:.2f} rad")  # r=5.00, φ=0.93

# Rectangular from polar
rect = cmath.rect(5, 0.9273)
print(f"Rectangular: {rect}")  # (3.000...+4.000...j)

# Exponential
print(f"exp(z): {cmath.exp(z)}")  # (-13.128+15.200j)

# Natural log
print(f"log(z): {cmath.log(z)}")  # (1.609+0.927j)

# Log base 10
print(f"log10(z): {cmath.log10(z)}")  # (0.699+0.402j)

# Square root
print(f"sqrt(z): {cmath.sqrt(z)}")  # (2+1j) (since (2+1j)² = 3+4j)
```

### Trigonometric Functions

```python
import cmath
import math

z = 1 + 1j

print(f"z = {z}")
print()

# Sine
sin_z = cmath.sin(z)
print(f"sin(z) = {sin_z}")
print(f"sin(z) real: {sin_z.real:.4f}, imag: {sin_z.imag:.4f}")

# Cosine
cos_z = cmath.cos(z)
print(f"cos(z) = {cos_z}")

# Tangent
tan_z = cmath.tan(z)
print(f"tan(z) = {tan_z}")

# Inverse trig functions
print(f"asin(sin(z)): {cmath.asin(sin_z)}")
print(f"acos(cos(z)): {cmath.acos(cos_z)}")
print(f"atan(tan(z)): {cmath.atan(tan_z)}")
```

### Hyperbolic Functions

```python
import cmath

z = 1 + 1j

print(f"z = {z}")
print()

# Hyperbolic sine
sinh_z = cmath.sinh(z)
print(f"sinh(z) = {sinh_z}")

# Hyperbolic cosine
cosh_z = cmath.cosh(z)
print(f"cosh(z) = {cosh_z}")

# Hyperbolic tangent
tanh_z = cmath.tanh(z)
print(f"tanh(z) = {tanh_z}")

# Inverse hyperbolic
print(f"asinh(sinh(z)): {cmath.asinh(sinh_z)}")
print(f"acosh(cosh(z)): {cmath.acosh(cosh_z)}")
print(f"atanh(tanh(z)): {cmath.atanh(tanh_z)}")
```

### Constants in Cmath

```python
import cmath

print(f"π (pi): {cmath.pi}")           # 3.141592653589793
print(f"e: {cmath.e}")                 # 2.718281828459045
print(f"τ (tau): {cmath.tau}")         # 6.283185307179586
print(f"Infinity: {cmath.inf}")        # inf
print(f"NaN: {cmath.nan}")             # nan

# Note: Same as math module constants
import math
print(cmath.pi == math.pi)  # True
```

---

## 🔄 Polar and Rectangular Forms

Complex numbers can be represented in two forms:

### 1. Rectangular Form: `a + bj`
- **a** = real part
- **b** = imaginary part

### 2. Polar Form: `r ∠ φ`
- **r** = magnitude (distance from origin)
- **φ** = phase angle (in radians)

```python
import cmath
import math

# Convert rectangular → polar
z_rect = 3 + 4j
r, phi = cmath.polar(z_rect)

print(f"Rectangular: {z_rect}")
print(f"Polar: r={r:.2f}, φ={phi:.2f} rad ({math.degrees(phi):.1f}°)")
print()

# Convert polar → rectangular
r = 5.0
phi_rad = math.radians(53.13)
z_polar = cmath.rect(r, phi_rad)

print(f"Polar: r={r}, φ={math.degrees(phi_rad):.1f}°")
print(f"Rectangular: {z_polar}")

# Real-world use: Easier multiplication in polar form
z1 = 2 + 3j
z2 = 4 + 5j

# Multiplication in rectangular (messy)
product_rect = z1 * z2
print(f"Product (rectangular): {product_rect}")

# Multiplication in polar (easier: multiply r's, add φ's)
r1, phi1 = cmath.polar(z1)
r2, phi2 = cmath.polar(z2)
r_product = r1 * r2
phi_product = phi1 + phi2
product_polar = cmath.rect(r_product, phi_product)
print(f"Product (polar): {product_polar}")
```

### Visualizing Complex Numbers

```python
import cmath
import math

def describe_complex(z):
    """Describe a complex number in multiple forms"""
    r, phi = cmath.polar(z)
    phi_deg = math.degrees(phi)
    
    print(f"Number: {z}")
    print(f"  Real part: {z.real:.2f}")
    print(f"  Imag part: {z.imag:.2f}")
    print(f"  Magnitude: {r:.2f}")
    print(f"  Phase: {phi:.3f} rad ({phi_deg:.1f}°)")
    
    # Quadrant
    if z.real > 0 and z.imag > 0:
        quadrant = "Q1 (0° to 90°)"
    elif z.real < 0 and z.imag > 0:
        quadrant = "Q2 (90° to 180°)"
    elif z.real < 0 and z.imag < 0:
        quadrant = "Q3 (180° to 270°)"
    elif z.real > 0 and z.imag < 0:
        quadrant = "Q4 (270° to 360°)"
    elif z.real == 0 and z.imag > 0:
        quadrant = "Positive imaginary axis"
    elif z.real == 0 and z.imag < 0:
        quadrant = "Negative imaginary axis"
    elif z.imag == 0 and z.real > 0:
        quadrant = "Positive real axis"
    elif z.imag == 0 and z.real < 0:
        quadrant = "Negative real axis"
    else:
        quadrant = "Origin"
    
    print(f"  Quadrant: {quadrant}")
    print()

# Test various complex numbers
numbers = [
    3 + 4j,      # Q1
    -3 + 4j,     # Q2
    -3 - 4j,     # Q3
    3 - 4j,      # Q4
    0 + 5j,      # Positive imag axis
    0 - 5j,      # Negative imag axis
    5 + 0j,      # Positive real axis
    -5 + 0j,     # Negative real axis
    0 + 0j       # Origin
]

for z in numbers:
    describe_complex(z)
```

---

## 🌍 Real-World Examples

### Example 1: AC Circuit Analysis (RLC Circuit)

```python
import cmath
import math

class ACCircuit:
    """AC Circuit analyzer using complex numbers"""
    
    def __init__(self, voltage_rms, frequency):
        self.voltage = complex(voltage_rms, 0)  # Reference at 0°
        self.frequency = frequency
        self.omega = 2 * math.pi * frequency
    
    def resistor(self, r):
        """Resistor impedance (pure real)"""
        return complex(r, 0)
    
    def inductor(self, l):
        """Inductor impedance (positive imaginary)"""
        return complex(0, self.omega * l)
    
    def capacitor(self, c):
        """Capacitor impedance (negative imaginary)"""
        return complex(0, -1 / (self.omega * c))
    
    def series_impedance(self, components):
        """Total impedance for series circuit"""
        return sum(components)
    
    def parallel_impedance(self, components):
        """Total impedance for parallel circuit"""
        reciprocal_sum = sum(1/z for z in components)
        return 1 / reciprocal_sum
    
    def current(self, impedance):
        """Calculate current using Ohm's Law"""
        return self.voltage / impedance
    
    def power(self, current):
        """Calculate real power (watts)"""
        apparent_power = self.voltage * current.conjugate()
        return apparent_power.real
    
    def analyze(self, components, connection="series"):
        """Complete circuit analysis"""
        if connection == "series":
            Z = self.series_impedance(components)
        else:
            Z = self.parallel_impedance(components)
        
        I = self.current(Z)
        P = self.power(I)
        power_factor = math.cos(cmath.phase(Z))
        
        return {
            'impedance': Z,
            'impedance_magnitude': abs(Z),
            'impedance_phase_deg': math.degrees(cmath.phase(Z)),
            'current': I,
            'current_magnitude': abs(I),
            'current_phase_deg': math.degrees(cmath.phase(I)),
            'power': P,
            'power_factor': power_factor
        }

# Create circuit
circuit = ACCircuit(voltage_rms=230, frequency=60)  # 230V, 60Hz

# Components
R = circuit.resistor(100)      # 100 Ω resistor
L = circuit.inductor(0.2)      # 0.2 H inductor
C = circuit.capacitor(50e-6)   # 50 μF capacitor

print("=" * 60)
print("AC CIRCUIT ANALYSIS")
print("=" * 60)
print(f"Source: {circuit.voltage.real}V RMS at {circuit.frequency}Hz")
print()

# Series RLC
print("SERIES RLC CIRCUIT")
print("-" * 40)
series_result = circuit.analyze([R, L, C], "series")

print(f"Total Impedance: {series_result['impedance']:.2f} Ω")
print(f"Impedance Magnitude: {series_result['impedance_magnitude']:.2f} Ω")
print(f"Phase Angle: {series_result['impedance_phase_deg']:.1f}°")
print(f"Current: {series_result['current_magnitude']:.2f} A at {series_result['current_phase_deg']:.1f}°")
print(f"Real Power: {series_result['power']:.1f} W")
print(f"Power Factor: {series_result['power_factor']:.3f}")

# Determine circuit nature
if series_result['impedance'].imag > 0:
    print("Circuit is INDUCTIVE (current lags voltage)")
elif series_result['impedance'].imag < 0:
    print("Circuit is CAPACITIVE (current leads voltage)")
else:
    print("Circuit is RESISTIVE (at resonance)")

print()

# Parallel RLC
print("PARALLEL RLC CIRCUIT")
print("-" * 40)
parallel_result = circuit.analyze([R, L, C], "parallel")

print(f"Total Impedance: {parallel_result['impedance']:.2f} Ω")
print(f"Impedance Magnitude: {parallel_result['impedance_magnitude']:.2f} Ω")
print(f"Phase Angle: {parallel_result['impedance_phase_deg']:.1f}°")
print(f"Current: {parallel_result['current_magnitude']:.2f} A at {parallel_result['current_phase_deg']:.1f}°")
print(f"Real Power: {parallel_result['power']:.1f} W")
print(f"Power Factor: {parallel_result['power_factor']:.3f}")

# Find resonance frequency
print("\n" + "=" * 60)
print("RESONANCE FREQUENCY CALCULATION")
print("=" * 60)

# At resonance: XL = XC → ωL = 1/(ωC) → ω = 1/√(LC)
L_value = 0.2   # Henries
C_value = 50e-6 # Farads
resonance_freq = 1 / (2 * math.pi * math.sqrt(L_value * C_value))

print(f"For L={L_value}H, C={C_value}F:")
print(f"Resonance Frequency: {resonance_freq:.1f} Hz")

# Analyze at resonance
circuit_resonant = ACCircuit(230, resonance_freq)
R_res = circuit_resonant.resistor(100)
L_res = circuit_resonant.inductor(L_value)
C_res = circuit_resonant.capacitor(C_value)

resonant_result = circuit_resonant.analyze([R_res, L_res, C_res], "series")
print(f"\nAt resonance:")
print(f"  Impedance: {resonant_result['impedance']:.2f} Ω (pure resistive)")
print(f"  Current: {resonant_result['current_magnitude']:.2f} A")
print(f"  Power Factor: {resonant_result['power_factor']:.3f}")
```

### Example 2: Quadratic Equation Solver

```python
import cmath
import math

class QuadraticSolver:
    """Solve quadratic equations: ax² + bx + c = 0"""
    
    @staticmethod
    def solve(a, b, c):
        """Return roots of quadratic equation"""
        if a == 0:
            if b == 0:
                return None  # No solution
            else:
                # Linear equation: bx + c = 0
                return (-c / b,)
        
        # Calculate discriminant
        discriminant = complex(b**2 - 4*a*c, 0)
        sqrt_d = cmath.sqrt(discriminant)
        
        # Calculate roots
        root1 = (-b + sqrt_d) / (2*a)
        root2 = (-b - sqrt_d) / (2*a)
        
        return (root1, root2)
    
    @staticmethod
    def analyze_roots(roots):
        """Analyze the nature of roots"""
        if roots is None:
            return "No solution"
        
        if len(roots) == 1:
            return "Linear equation (single root)"
        
        r1, r2 = roots
        
        # Check if roots are real
        is_real1 = abs(r1.imag) < 1e-10
        is_real2 = abs(r2.imag) < 1e-10
        
        if is_real1 and is_real2:
            if abs(r1.real - r2.real) < 1e-10:
                return "Real and equal (double root)"
            else:
                return "Real and distinct"
        else:
            return "Complex conjugates"
    
    @staticmethod
    def get_vertex(a, b, c):
        """Find vertex of parabola"""
        if a == 0:
            return None
        
        x_vertex = -b / (2*a)
        y_vertex = a * x_vertex**2 + b * x_vertex + c
        
        return (x_vertex.real, y_vertex.real)

# Test various equations
equations = [
    (1, -5, 6),     # Real distinct: x² -5x +6 = 0 → x=2, x=3
    (1, 0, 1),      # Complex: x² + 1 = 0 → x=±j
    (1, 2, 5),      # Complex: x² +2x +5 = 0 → x=-1±2j
    (1, 4, 4),      # Real equal: x² +4x +4 = 0 → x=-2
    (2, -3, 1),     # Real distinct: 2x² -3x +1 = 0 → x=1, x=0.5
    (0, 2, -4),     # Linear: 2x -4 = 0 → x=2
    (0, 0, 5)       # No solution: 5 = 0
]

print("=" * 70)
print("QUADRATIC EQUATION SOLVER")
print("=" * 70)

for a, b, c in equations:
    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    print("-" * 50)
    
    roots = QuadraticSolver.solve(a, b, c)
    nature = QuadraticSolver.analyze_roots(roots)
    
    print(f"Nature: {nature}")
    
    if roots:
        for i, root in enumerate(roots, 1):
            if abs(root.imag) < 1e-10:
                # Real root
                print(f"Root {i}: {root.real:.4f}")
            else:
                # Complex root
                print(f"Root {i}: {root:.4f}")
                print(f"  Real: {root.real:.4f}, Imag: {root.imag:.4f}")
    
    # Find vertex (for quadratic equations)
    vertex = QuadraticSolver.get_vertex(a, b, c)
    if vertex and a != 0:
        print(f"Vertex: ({vertex[0]:.2f}, {vertex[1]:.2f})")
        if a > 0:
            print(f"Parabola opens UP (minimum at vertex)")
        else:
            print(f"Parabola opens DOWN (maximum at vertex)")

# Interactive solver
print("\n" + "=" * 70)
print("INTERACTIVE SOLVER")
print("=" * 70)

try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    
    roots = QuadraticSolver.solve(a, b, c)
    nature = QuadraticSolver.analyze_roots(roots)
    
    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    print(f"Nature: {nature}")
    
    if roots:
        for i, root in enumerate(roots, 1):
            if abs(root.imag) < 1e-10:
                print(f"Root {i}: {root.real:.4f}")
            else:
                print(f"Root {i}: {root:.4f}")
    
    # Additional info
    if a != 0:
        vertex = QuadraticSolver.get_vertex(a, b, c)
        if vertex:
            print(f"Vertex: ({vertex[0]:.2f}, {vertex[1]:.2f})")
        
        # Discriminant
        D = b**2 - 4*a*c
        print(f"Discriminant: {D:.4f}")
        
        if D > 0:
            print("Discriminant > 0 → Two real roots")
        elif D == 0:
            print("Discriminant = 0 → One real root (double root)")
        else:
            print("Discriminant < 0 → Two complex roots")
            
except ValueError:
    print("Invalid input! Please enter numbers.")
```

### Example 3: Fourier Series Analysis

```python
import cmath
import math

class FourierAnalyzer:
    """Fourier series analysis using complex numbers"""
    
    def __init__(self, period=2*math.pi):
        self.period = period
        self.omega = 2 * math.pi / period
    
    def fourier_coefficient(self, func, n):
        """Calculate nth Fourier coefficient numerically"""
        def integrand(t):
            return func(t) * cmath.exp(-1j * n * self.omega * t)
        
        # Numerical integration using trapezoidal rule
        N = 1000
        dt = self.period / N
        integral = 0 + 0j
        
        for k in range(N):
            t = k * dt
            integral += integrand(t) * dt
        
        return integral / self.period
    
    def reconstruct(self, coefficients, t):
        """Reconstruct signal from Fourier coefficients"""
        result = 0 + 0j
        for n, cn in coefficients.items():
            result += cn * cmath.exp(1j * n * self.omega * t)
        return result.real  # Return real part
    
    def analyze_signal(self, func, num_harmonics=10):
        """Analyze signal and return harmonics"""
        coefficients = {}
        
        for n in range(-num_harmonics, num_harmonics + 1):
            cn = self.fourier_coefficient(func, n)
            if abs(cn) > 1e-10:  # Ignore very small coefficients
                coefficients[n] = cn
        
        return coefficients

# Define test signals
def square_wave(t):
    """Square wave with amplitude 1, period 2π"""
    period = 2 * math.pi
    return 1 if (t % period) < period/2 else -1

def sawtooth_wave(t):
    """Sawtooth wave with amplitude 1, period 2π"""
    period = 2 * math.pi
    return 2 * (t % period) / period - 1

def triangle_wave(t):
    """Triangle wave with amplitude 1, period 2π"""
    period = 2 * math.pi
    t_mod = t % period
    if t_mod < period/2:
        return 2 * t_mod / (period/2) - 1
    else:
        return 3 - 2 * t_mod / (period/2)

print("=" * 70)
print("FOURIER SERIES ANALYSIS")
print("=" * 70)

analyzer = FourierAnalyzer(period=2*math.pi)

# Analyze square wave
print("\nSQUARE WAVE ANALYSIS")
print("-" * 50)

coeffs_square = analyzer.analyze_signal(square_wave, num_harmonics=10)

print("Significant Fourier coefficients:")
for n in sorted(coeffs_square.keys()):
    cn = coeffs_square[n]
    if n == 0:
        print(f"  DC component (n=0): {cn:.4f}")
    else:
        magnitude = abs(cn)
        phase = math.degrees(cmath.phase(cn))
        print(f"  Harmonic n={n:2d}: magnitude={magnitude:.4f}, phase={phase:.1f}°")

# Note: For real signals, c(-n) = conjugate(c(n))
print("\nNote: For real signals, c(-n) = conjugate(c(n))")

# Analyze sawtooth wave
print("\n" + "=" * 70)
print("SAWTOOTH WAVE ANALYSIS")
print("=" * 70)

coeffs_sawtooth = analyzer.analyze_signal(sawtooth_wave, num_harmonics=10)

print("Significant Fourier coefficients:")
for n in sorted(coeffs_sawtooth.keys()):
    cn = coeffs_sawtooth[n]
    if n == 0:
        print(f"  DC component (n=0): {cn:.4f}")
    else:
        magnitude = abs(cn)
        phase = math.degrees(cmath.phase(cn))
        print(f"  Harmonic n={n:2d}: magnitude={magnitude:.4f}, phase={phase:.1f}°")

# Signal reconstruction comparison
print("\n" + "=" * 70)
print("SIGNAL RECONSTRUCTION")
print("=" * 70)

# Reconstruct square wave at a specific point
t_test = math.pi / 4  # 45 degrees
original = square_wave(t_test)
reconstructed = analyzer.reconstruct(coeffs_square, t_test)

print(f"At t = {t_test:.3f} rad:")
print(f"  Original square wave: {original}")
print(f"  Reconstructed (10 harmonics): {reconstructed:.4f}")
print(f"  Error: {abs(original - reconstructed):.4f}")

# Explain Gibbs phenomenon
print("\n" + "=" * 70)
print("GIBBS PHENOMENON")
print("=" * 70)
print("At discontinuities, Fourier series overshoots by about 9%")
print("This is called the Gibbs phenomenon and doesn't disappear")
print("even with more harmonics.")
```

### Example 4: Quantum Mechanics - Wave Function

```python
import cmath
import math

class QuantumParticle:
    """Simple quantum particle with complex wave function"""
    
    def __init__(self, mass, position=0, momentum=0):
        self.mass = mass
        self.position = position
        self.momentum = momentum
        self.hbar = 1.0545718e-34  # Reduced Planck constant
    
    def wave_function(self, x, t=0):
        """Wave function ψ(x,t) = A * exp(i(kx - ωt))"""
        # For a free particle
        k = self.momentum / self.hbar  # Wave number
        omega = self.momentum**2 / (2 * self.mass * self.hbar)  # Angular frequency
        
        phase = k * x - omega * t
        amplitude = 1 / math.sqrt(2 * math.pi)  # Normalization constant
        
        return amplitude * cmath.exp(1j * phase)
    
    def probability_density(self, x, t=0):
        """Probability density |ψ|²"""
        psi = self.wave_function(x, t)
        return abs(psi)**2
    
    def expectation_position(self, x_min, x_max, t=0, num_points=1000):
        """Calculate <x> = ∫ ψ* x ψ dx"""
        dx = (x_max - x_min) / num_points
        integral = 0 + 0j
        
        for i in range(num_points):
            x = x_min + i * dx
            psi = self.wave_function(x, t)
            integral += psi.conjugate() * x * psi * dx
        
        return integral.real
    
    def expectation_momentum(self, x_min, x_max, t=0, num_points=1000):
        """Calculate <p> = ∫ ψ* (-iℏ d/dx) ψ dx"""
        dx = (x_max - x_min) / num_points
        integral = 0 + 0j
        
        for i in range(1, num_points):
            x = x_min + i * dx
            psi = self.wave_function(x, t)
            
            # Numerical derivative
            psi_prev = self.wave_function(x - dx, t)
            dpsi_dx = (psi - psi_prev) / dx
            
            integral += psi.conjugate() * (-1j * self.hbar * dpsi_dx) * dx
        
        return integral.real

# Create quantum particle
electron_mass = 9.109e-31  # kg
momentum = 1e-24  # kg·m/s

particle = QuantumParticle(mass=electron_mass, momentum=momentum)

print("=" * 70)
print("QUANTUM MECHANICS - WAVE FUNCTION")
print("=" * 70)

print(f"Particle: Electron")
print(f"Mass: {electron_mass:.2e} kg")
print(f"Momentum: {momentum:.2e} kg·m/s")
print()

# Calculate wave function at different positions
positions = [-1e-9, 0, 1e-9]  # meters

print("Wave Function Values:")
for x in positions:
    psi = particle.wave_function(x)
    prob = particle.probability_density(x)
    
    print(f"\n  Position x = {x:.2e} m:")
    print(f"    ψ(x) = {psi:.4f}")
    print(f"    |ψ|² = {prob:.4f} (probability density)")
    print(f"    Real part: {psi.real:.4f}")
    print(f"    Imag part: {psi.imag:.4f}")

# Calculate expectation values
x_min, x_max = -5e-9, 5e-9
exp_x = particle.expectation_position(x_min, x_max)
exp_p = particle.expectation_momentum(x_min, x_max)

print("\n" + "=" * 70)
print("EXPECTATION VALUES")
print("=" * 70)
print(f"⟨x⟩ (expected position): {exp_x:.2e} m")
print(f"⟨p⟩ (expected momentum): {exp_p:.2e} kg·m/s")
print(f"Given momentum: {momentum:.2e} kg·m/s")
print(f"Match: {'✓' if abs(exp_p - momentum) < 1e-30 else '✗'}")

# Uncertainty principle check
print("\n" + "=" * 70)
print("HEISENBERG UNCERTAINTY PRINCIPLE")
print("=" * 70)

# Calculate Δx and Δp (simplified)
x_vals = [particle.wave_function(x_min + i * (x_max - x_min)/1000) 
          for i in range(1001)]
# Simplified uncertainty calculation
delta_x = (x_max - x_min) / math.sqrt(12)  # For uniform distribution
delta_p = momentum / math.sqrt(3)  # Approximate

product = delta_x * delta_p
hbar = 1.0545718e-34

print(f"Δx ≈ {delta_x:.2e} m")
print(f"Δp ≈ {delta_p:.2e} kg·m/s")
print(f"Δx · Δp = {product:.2e} J·s")
print(f"ℏ/2 = {hbar/2:.2e} J·s")
print(f"Uncertainty principle satisfied: {product >= hbar/2}")
```

### Example 5: Control Systems Stability Analysis

```python
import cmath
import math

class ControlSystem:
    """Control system analyzer using complex numbers"""
    
    @staticmethod
    def transfer_function(gain, poles, zeros):
        """
        Create transfer function H(s) = K * Π(s - zeros) / Π(s - poles)
        where s = σ + jω (complex frequency)
        """
        def H(s):
            num = gain
            for z in zeros:
                num *= (s - z)
            
            den = 1
            for p in poles:
                den *= (s - p)
            
            return num / den
        
        return H
    
    @staticmethod
    def evaluate_frequency_response(H, omega):
        """Evaluate H(jω) for frequency response"""
        s = complex(0, omega)  # s = jω
        return H(s)
    
    @staticmethod
    def is_stable(poles):
        """Check if system is stable (all poles in left half-plane)"""
        for p in poles:
            if p.real >= 0:
                return False
        return True
    
    @staticmethod
    def gain_margin(H, omega_range=(0.1, 100), num_points=1000):
        """Calculate gain margin (simplified)"""
        # Find frequency where phase = -180°
        # Simplified implementation
        return float('inf')  # Placeholder
    
    @staticmethod
    def phase_margin(H, omega_range=(0.1, 100), num_points=1000):
        """Calculate phase margin (simplified)"""
        # Find frequency where |H| = 1 (0 dB)
        # Simplified implementation
        return float('inf')  # Placeholder

# Define systems
print("=" * 70)
print("CONTROL SYSTEMS - STABILITY ANALYSIS")
print("=" * 70)

# System 1: Stable
poles1 = [-1, -2, -3]  # All negative real parts
zeros1 = []
gain1 = 10

H1 = ControlSystem.transfer_function(gain1, poles1, zeros1)
stable1 = ControlSystem.is_stable(poles1)

print("\nSYSTEM 1: Stable System")
print("-" * 50)
print(f"Transfer Function: H(s) = {gain1} / (s+1)(s+2)(s+3)")
print(f"Poles: {poles1}")
print(f"Zeros: {zeros1}")
print(f"Stable: {'✓ YES' if stable1 else '✗ NO'}")

# Evaluate at different frequencies
print("\nFrequency Response (jω):")
frequencies = [0.1, 1, 10, 100]
for w in frequencies:
    Hjw = ControlSystem.evaluate_frequency_response(H1, w)
    magnitude = abs(Hjw)
    phase = math.degrees(cmath.phase(Hjw))
    print(f"  ω = {w:3.0f} rad/s: |H| = {magnitude:.3f}, ∠H = {phase:.1f}°")

# System 2: Unstable
poles2 = [1, -2]  # One pole with positive real part
zeros2 = [-1]
gain2 = 5

H2 = ControlSystem.transfer_function(gain2, poles2, zeros2)
stable2 = ControlSystem.is_stable(poles2)

print("\n" + "=" * 70)
print("SYSTEM 2: Unstable System")
print("=" * 70)
print(f"Transfer Function: H(s) = {gain2}(s+1) / (s-1)(s+2)")
print(f"Poles: {poles2}")
print(f"Zeros: {zeros2}")
print(f"Stable: {'✓ YES' if stable2 else '✗ NO'}")

# Show why it's unstable
print("\nPole Locations:")
for p in poles2:
    if p.real > 0:
        print(f"  Pole at s = {p} → RIGHT half-plane → UNSTABLE")
    elif p.real < 0:
        print(f"  Pole at s = {p} → LEFT half-plane → stable")
    else:
        print(f"  Pole at s = {p} → ON imaginary axis → marginally stable")

# System 3: Critically stable
poles3 = [0, -1]  # Pole at origin
zeros3 = []
gain3 = 1

H3 = ControlSystem.transfer_function(gain3, poles3, zeros3)
stable3 = ControlSystem.is_stable(poles3)

print("\n" + "=" * 70)
print("SYSTEM 3: Marginally Stable System")
print("=" * 70)
print(f"Transfer Function: H(s) = 1 / s(s+1)")
print(f"Poles: {poles3}")
print(f"Stable: {'✓ YES' if stable3 else '✗ NO'}")
print("Note: Pole at origin → Integrator → Marginally stable")

# Step response simulation (simplified)
print("\n" + "=" * 70)
print("STEP RESPONSE SIMULATION")
print("=" * 70)

def step_response(poles, time_vector):
    """Simulate step response for a system with real poles"""
    response = []
    for t in time_vector:
        # Simplified step response (sum of exponentials)
        val = 1  # Steady state
        for p in poles:
            if p.real < 0:
                val += (1/abs(p)) * math.exp(p.real * t)
        response.append(val)
    return response

# Test with stable system
time = [i * 0.1 for i in range(50)]  # 0 to 5 seconds
response = step_response(poles1, time)

print("\nStable System Step Response:")
for i, t in enumerate(time[::10]):  # Show every 10th point
    print(f"  t = {t:.1f}s: output = {response[i*10]:.4f}")

print("\n✓ System settles to steady state")

# Complex conjugate poles (oscillatory response)
print("\n" + "=" * 70)
print("COMPLEX POLES - OSCILLATORY RESPONSE")
print("=" * 70)

# Poles: -1 ± 2j (damped oscillation)
poles_osc = [complex(-1, 2), complex(-1, -2)]
print(f"Poles: {poles_osc[0]:.2f}, {poles_osc[1]:.2f}")
print("These are complex conjugates → Oscillatory response")

# Calculate damping ratio and natural frequency
for p in poles_osc:
    if p.imag > 0:  # Upper half-plane
        sigma = -p.real
        omega_d = p.imag
        omega_n = math.sqrt(sigma**2 + omega_d**2)
        zeta = sigma / omega_n
        
        print(f"\n  Damping ratio ζ = {zeta:.3f}")
        print(f"  Natural frequency ωn = {omega_n:.3f} rad/s")
        print(f"  Damped frequency ωd = {omega_d:.3f} rad/s")
        
        if zeta < 1:
            print("  System is UNDERDAMPED (oscillatory)")
        elif zeta == 1:
            print("  System is CRITICALLY DAMPED")
        else:
            print("  System is OVERDAMPED")
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Using `i` Instead of `j`

```python
# ❌ WRONG - Python uses 'j' not 'i'
# z = 3 + 4i  # SyntaxError!

# ✅ CORRECT
z = 3 + 4j
print(z)  # (3+4j)

# Also works with capital J
z = 3 + 4J
print(z)  # (3+4j)
```

### Pitfall 2: Comparing Complex Numbers

```python
a = 3 + 4j
b = 1 + 2j

# ❌ WRONG - Cannot use <, >, <=, >=
# if a > b:  # TypeError!

# ✅ CORRECT - Compare magnitudes instead
if abs(a) > abs(b):
    print("a has larger magnitude")

# ✅ CORRECT - Compare real/imag parts separately
if a.real > b.real:
    print("a has larger real part")
```

### Pitfall 3: Complex Numbers as Dictionary Keys

```python
# ❌ BAD - Complex numbers are hashable but risky
d = {}
z1 = 3 + 4j
z2 = 3 + 4j
d[z1] = "value"
print(d[z2])  # Works (same value)

# But floating-point precision can cause issues
z3 = 0.1 + 0.2j
z4 = 0.30000000000000004 + 0.2j
d[z3] = "test"
print(z3 == z4)  # False (different keys!)

# ✅ GOOD - Use strings or tuples
d = {}
d[(3, 4)] = "value"  # Tuple of (real, imag)
```

### Pitfall 4: Forgetting to Import Cmath

```python
# ❌ WRONG - math module doesn't work with complex
import math
z = 3 + 4j
# print(math.sqrt(z))  # TypeError!

# ✅ CORRECT - Use cmath for complex numbers
import cmath
print(cmath.sqrt(z))  # (2+1j)

# math functions work on real parts
print(math.sqrt(z.real))  # 1.732...
```

### Pitfall 5: Phase Angle Interpretation

```python
import cmath
import math

z = -3 - 4j
phase = cmath.phase(z)
phase_deg = math.degrees(phase)

print(f"z = {z}")
print(f"Phase: {phase_deg:.1f}°")

# Phase is in range (-π, π] or (-180°, 180°]
# Not 0° to 360°!

# Convert to 0°-360° range
if phase_deg < 0:
    phase_deg_360 = phase_deg + 360
else:
    phase_deg_360 = phase_deg

print(f"Phase (0-360°): {phase_deg_360:.1f}°")
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Complex Number Basics**
   ```python
   # Create complex numbers with:
   # - Real part 5, imaginary 3
   # - Real part -2, imaginary 4
   # - Pure imaginary 7
   # Print real, imag, and conjugate
   ```

2. **Complex Arithmetic**
   ```python
   # Given z1 = 2+3j, z2 = 4-5j
   # Calculate and print:
   # - Addition
   # - Subtraction
   # - Multiplication
   # - Division
   ```

3. **Magnitude Calculator**
   ```python
   # Write a function that returns magnitude of complex number
   # Test with: 3+4j, 5+12j, 8+15j
   ```

### Intermediate Level

4. **Quadratic Equation Solver**
   ```python
   # Create a function that solves any quadratic equation
   # Handle real and complex roots
   # Display roots in a+bi format
   ```

5. **Polar Converter**
   ```python
   # Write functions to:
   # - Convert rectangular to polar (return magnitude, phase)
   # - Convert polar to rectangular (return complex)
   ```

6. **AC Circuit Calculator**
   ```python
   # Calculate total impedance of:
   # - Series RLC circuit
   # - Parallel RLC circuit
   # Display in both rectangular and polar forms
   ```

### Advanced Level

7. **Fourier Series Visualizer**
   ```python
   # Calculate Fourier coefficients for square wave
   # Reconstruct signal using different numbers of harmonics
   # Show how approximation improves with more harmonics
   ```

8. **Control System Stability**
   ```python
   # Given transfer function poles and zeros
   # Determine stability
   # Plot pole-zero map
   ```

9. **Quantum Wave Function Simulator**
   ```python
   # Simulate a free particle wave function
   # Calculate probability density
   # Show time evolution
   ```

---

## 🔗 Next Steps

After mastering complex numbers:
1. Review `01_integers.md` and `02_floats.md`
2. Move to `02_text_type/` for strings
3. Explore `decimal.Decimal` for precise decimal math

---

## 📚 Quick Reference Card

```python
# Creation
z = 3 + 4j                    # Direct
z = complex(3, 4)             # From parts
z = complex("3+4j")           # From string
z = cmath.rect(r, phi)        # From polar

# Properties
z.real                        # Real part
z.imag                        # Imag part
z.conjugate()                 # Complex conjugate
abs(z)                        # Magnitude

# Cmath functions
import cmath
cmath.phase(z)                # Phase angle
cmath.polar(z)                # (r, φ)
cmath.rect(r, phi)            # From polar
cmath.exp(z)                  # Exponential
cmath.log(z)                  # Natural log
cmath.sqrt(z)                 # Square root
cmath.sin(z)                  # Sine
cmath.cos(z)                  # Cosine
cmath.tan(z)                  # Tangent
cmath.sinh(z)                 # Hyperbolic sine
cmath.cosh(z)                 # Hyperbolic cosine
cmath.tanh(z)                 # Hyperbolic tangent

# Constants
cmath.pi                      # 3.14159...
cmath.e                       # 2.71828...
cmath.tau                     # 6.28318...
cmath.inf                     # Infinity
cmath.nan                     # Not a Number

# Operations (+, -, *, /, ** work normally)
z1 + z2                       # Addition
z1 - z2                       # Subtraction
z1 * z2                       # Multiplication
z1 / z2                       # Division
z1 ** 2                       # Power
```

## 📚 Next Steps

- Go to [02_text_data_type](/05_python/02_data_types/02_text_type/README.md) to learn it in detail.

---

*Master complex numbers, and you'll unlock advanced engineering, physics, and signal processing applications! 🐍✨*
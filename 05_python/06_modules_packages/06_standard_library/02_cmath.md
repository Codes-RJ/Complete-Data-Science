# 📘 CMATH MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Cmath Module?](#what-is-the-cmath-module)
2. [Complex Number Basics](#complex-number-basics)
3. [Constants](#constants)
4. [Conversion Functions](#conversion-functions)
5. [Power and Logarithm Functions](#power-and-logarithm-functions)
6. [Trigonometric Functions](#trigonometric-functions)
7. [Hyperbolic Functions](#hyperbolic-functions)
8. [Classification Functions](#classification-functions)
9. [Real-World Examples](#real-world-examples)
10. [Practice Exercises](#practice-exercises)

---

## What is the Cmath Module?

The `cmath` module provides mathematical functions for complex numbers. It's the complex number counterpart to the `math` module.

```python
import cmath
import math

# Real numbers (math module)
print(math.sqrt(4))    # 2.0
print(math.sqrt(-1))   # ValueError!

# Complex numbers (cmath module)
print(cmath.sqrt(4))   # (2+0j)
print(cmath.sqrt(-1))  # 1j (imaginary unit)
```

**Key Characteristics:**
- ✅ Works with complex numbers (a + bj)
- ✅ Handles negative square roots (returns complex)
- ✅ Functions return complex numbers
- ✅ Compatible with real numbers (treated as complex with imag=0)

---

## Complex Number Basics

### Creating Complex Numbers

```python
import cmath

# Different ways to create complex numbers
z1 = 3 + 4j
z2 = complex(3, 4)
z3 = complex(5)          # (5+0j)
z4 = complex("3+4j")

print(z1)   # (3+4j)
print(z2)   # (3+4j)
print(z3)   # (5+0j)
print(z4)   # (3+4j)

# Access real and imaginary parts
print(z1.real)    # 3.0
print(z1.imag)    # 4.0
print(z1.conjugate())  # (3-4j)
```

### Mathematical Operations

```python
import cmath

a = 3 + 4j
b = 1 - 2j

# Arithmetic
print(a + b)      # (4+2j)
print(a - b)      # (2+6j)
print(a * b)      # (11-2j)
print(a / b)      # (-1+2j)
print(a ** 2)     # (-7+24j)

# Magnitude (modulus)
print(abs(a))     # 5.0 (√(3²+4²))

# Phase (angle)
print(cmath.phase(a))  # 0.9272952180016122 rad
```

---

## Constants

### Mathematical Constants

```python
import cmath

# Pi (π)
print(cmath.pi)   # 3.141592653589793

# Euler's number (e)
print(cmath.e)    # 2.718281828459045

# Tau (τ = 2π)
print(cmath.tau)  # 6.283185307179586

# Infinity
print(cmath.inf)  # inf

# Not a Number
print(cmath.nan)  # nan

# Same as math module constants
import math
print(cmath.pi == math.pi)  # True
```

---

## Conversion Functions

### `cmath.phase(x)` – Phase (Argument) of Complex Number

```python
import cmath

# Phase angle in radians (-π to π)
z1 = 3 + 4j
print(cmath.phase(z1))           # 0.9272952180016122

z2 = -3 - 4j
print(cmath.phase(z2))           # -2.214297435588181

z3 = 1 + 0j
print(cmath.phase(z3))           # 0.0

z4 = 0 + 1j
print(cmath.phase(z4))           # 1.5707963267948966 (π/2)

# Convert to degrees
import math
phase_deg = math.degrees(cmath.phase(z1))
print(f"{phase_deg:.1f}°")       # 53.1°
```

### `cmath.polar(z)` – Polar Coordinates

```python
import cmath

z = 3 + 4j

# Returns (r, φ) where r = |z|, φ = phase(z)
r, phi = cmath.polar(z)
print(f"r = {r}, φ = {phi} rad")  # r = 5.0, φ = 0.9272952180016122 rad

# Manual calculation
r_manual = abs(z)
phi_manual = cmath.phase(z)
print(f"Manual: r = {r_manual}, φ = {phi_manual} rad")
```

### `cmath.rect(r, phi)` – Rectangular Coordinates from Polar

```python
import cmath

# Convert from polar to rectangular
r = 5.0
phi = 0.9272952180016122
z = cmath.rect(r, phi)
print(z)  # (3.0000000000000004+4j)

# Perfect square example
z = cmath.rect(1, cmath.pi/4)  # 45° angle
print(z)  # (0.7071067811865476+0.7071067811865475j)
```

---

## Power and Logarithm Functions

### `cmath.sqrt(x)` – Square Root

```python
import cmath

# Real numbers
print(cmath.sqrt(4))    # (2+0j)
print(cmath.sqrt(0))    # 0j

# Negative numbers (returns complex)
print(cmath.sqrt(-1))   # 1j
print(cmath.sqrt(-4))   # 2j

# Complex numbers
z = 3 + 4j
print(cmath.sqrt(z))    # (2+1j) because (2+1j)² = 3+4j

# Verify
print(cmath.sqrt(z) ** 2)  # (3+4j)
```

### `cmath.exp(x)` – Exponential (e^x)

```python
import cmath

# Real argument
print(cmath.exp(1))     # (2.718281828459045+0j)

# Complex argument (Euler's formula)
z = 1j * cmath.pi
print(cmath.exp(z))     # (-1+1.2246467991473532e-16j) ≈ -1

# Euler's formula: e^(iθ) = cosθ + i·sinθ
theta = cmath.pi / 2
print(cmath.exp(1j * theta))  # (6.123233995736766e-17+1j) ≈ i
```

### `cmath.log(x[, base])` – Logarithm

```python
import cmath

# Natural logarithm (base e)
print(cmath.log(1))       # 0j
print(cmath.log(cmath.e)) # (1+0j)

# Logarithm with specified base
print(cmath.log(8, 2))    # (3+0j)

# Complex numbers
z = 3 + 4j
print(cmath.log(z))       # (1.6094379124341003+0.9272952180016122j)

# Verify: e^log(z) should equal z
print(cmath.exp(cmath.log(z)))  # (3+4j)
```

### `cmath.log10(x)` – Base-10 Logarithm

```python
import cmath

print(cmath.log10(100))   # (2+0j)
print(cmath.log10(1000))  # (3+0j)

# Complex number
z = 3 + 4j
print(cmath.log10(z))     # (0.6989700043360187+0.4027191962733731j)
```

### `cmath.log2(x)` – Base-2 Logarithm

```python
import cmath

print(cmath.log2(8))      # (3+0j)
print(cmath.log2(16))     # (4+0j)

# Complex number
z = 3 + 4j
print(cmath.log2(z))      # (2.321928094887362+1.3378042124509761j)
```

---

## Trigonometric Functions

### Sine, Cosine, Tangent

```python
import cmath

# Real arguments (same as math module)
print(cmath.sin(0))       # 0j
print(cmath.cos(0))       # (1+0j)
print(cmath.tan(0))       # 0j

# Complex arguments
z = 1 + 2j
print(cmath.sin(z))       # (3.165778513216168+1.959601041421606j)
print(cmath.cos(z))       # (2.0327230070196656-3.0518977991518j)
print(cmath.tan(z))       # (0.0338128260798967+1.0147936161466335j)

# Verify identity: sin²(z) + cos²(z) = 1
sin_z = cmath.sin(z)
cos_z = cmath.cos(z)
identity = sin_z**2 + cos_z**2
print(identity)           # (1+0j) (within floating point error)
```

### Inverse Trigonometric Functions

```python
import cmath

# Arc sine (inverse sine)
z = 0.5 + 0.5j
print(cmath.asin(z))      # (0.45227844715119064+0.5306375309525178j)

# Arc cosine (inverse cosine)
print(cmath.acos(z))      # (1.1185178792437057-0.5306375309525178j)

# Arc tangent (inverse tangent)
print(cmath.atan(z))      # (0.5535743588970452+0.40235947810852507j)

# Verify: sin(asin(z)) should equal z
print(cmath.sin(cmath.asin(z)))  # (0.5+0.5j)
```

---

## Hyperbolic Functions

### Hyperbolic Sine, Cosine, Tangent

```python
import cmath

# Real arguments
print(cmath.sinh(0))      # 0j
print(cmath.cosh(0))      # (1+0j)
print(cmath.tanh(0))      # 0j

# Complex arguments
z = 1 + 2j
print(cmath.sinh(z))      # (-0.4890562590412937+1.4031192506220405j)
print(cmath.cosh(z))      # (-0.64214812471552+1.0686074213827783j)
print(cmath.tanh(z))      # (1.1667362572409198-0.24345820118572523j)

# Identity: cosh²(z) - sinh²(z) = 1
cosh_z = cmath.cosh(z)
sinh_z = cmath.sinh(z)
identity = cosh_z**2 - sinh_z**2
print(identity)           # (1+0j) (within floating point error)
```

### Inverse Hyperbolic Functions

```python
import cmath

z = 1 + 2j

# Inverse hyperbolic sine
print(cmath.asinh(z))     # (1.4693517443681852+1.063440023577752j)

# Inverse hyperbolic cosine
print(cmath.acosh(z))     # (1.4693517443681852+1.063440023577752j)

# Inverse hyperbolic tangent
print(cmath.atanh(z))     # (0.17328679513998627+1.1780972450961724j)

# Verify: sinh(asinh(z)) should equal z
print(cmath.sinh(cmath.asinh(z)))  # (1+2j)
```

---

## Classification Functions

### `cmath.isinf(x)` – Check Infinity

```python
import cmath

print(cmath.isinf(complex(float('inf'), 0)))   # True
print(cmath.isinf(complex(0, float('inf'))))   # True
print(cmath.isinf(3 + 4j))                    # False
```

### `cmath.isnan(x)` – Check NaN

```python
import cmath

print(cmath.isnan(complex(float('nan'), 0)))   # True
print(cmath.isnan(complex(0, float('nan'))))   # True
print(cmath.isnan(3 + 4j))                    # False
```

### `cmath.isfinite(x)` – Check Finite

```python
import cmath

print(cmath.isfinite(3 + 4j))                # True
print(cmath.isfinite(complex(float('inf'), 0)))  # False
print(cmath.isfinite(complex(float('nan'), 0)))  # False
```

---

## Real-World Examples

### Example 1: AC Circuit Analysis

```python
import cmath
import math

class ACCircuit:
    def __init__(self, voltage_rms, frequency):
        self.voltage = complex(voltage_rms, 0)
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
        reciprocal_sum = sum(1 / z for z in components)
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
circuit = ACCircuit(voltage_rms=230, frequency=60)

# Series RLC circuit
R = circuit.resistor(100)
L = circuit.inductor(0.5)
C = circuit.capacitor(50e-6)

result = circuit.analyze([R, L, C], "series")

print("AC CIRCUIT ANALYSIS")
print("=" * 40)
print(f"Source: {circuit.voltage.real}V at {circuit.frequency}Hz")
print(f"Impedance: {result['impedance']:.2f} Ω")
print(f"Impedance Magnitude: {result['impedance_magnitude']:.2f} Ω")
print(f"Phase Angle: {result['impedance_phase_deg']:.1f}°")
print(f"Current: {result['current_magnitude']:.2f} A")
print(f"Current Phase: {result['current_phase_deg']:.1f}°")
print(f"Real Power: {result['power']:.1f} W")
print(f"Power Factor: {result['power_factor']:.3f}")

# Determine circuit nature
if result['impedance'].imag > 0:
    print("Circuit is INDUCTIVE (current lags voltage)")
elif result['impedance'].imag < 0:
    print("Circuit is CAPACITIVE (current leads voltage)")
else:
    print("Circuit is RESISTIVE (at resonance)")
```

### Example 2: Quadratic Equation Solver

```python
import cmath
import math

class QuadraticSolver:
    @staticmethod
    def solve(a, b, c):
        """Solve quadratic equation ax² + bx + c = 0"""
        if a == 0:
            if b == 0:
                return None
            return (-c / b,)
        
        discriminant = complex(b**2 - 4*a*c, 0)
        sqrt_d = cmath.sqrt(discriminant)
        
        root1 = (-b + sqrt_d) / (2*a)
        root2 = (-b - sqrt_d) / (2*a)
        
        return (root1, root2)
    
    @staticmethod
    def analyze(roots):
        """Analyze the nature of roots"""
        if roots is None:
            return "No solution"
        
        if len(roots) == 1:
            return "One real root (double root)"
        
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

# Test equations
equations = [
    (1, -5, 6),     # x² - 5x + 6 = 0 → x = 2, 3
    (1, 0, 1),      # x² + 1 = 0 → x = ±i
    (1, 2, 5),      # x² + 2x + 5 = 0 → x = -1 ± 2i
    (1, 4, 4),      # x² + 4x + 4 = 0 → x = -2 (double)
    (2, -3, 1),     # 2x² - 3x + 1 = 0 → x = 1, 0.5
]

print("QUADRATIC EQUATION SOLVER")
print("=" * 50)

for a, b, c in equations:
    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    
    roots = QuadraticSolver.solve(a, b, c)
    nature = QuadraticSolver.analyze(roots)
    
    print(f"Nature: {nature}")
    
    if roots:
        for i, root in enumerate(roots, 1):
            if abs(root.imag) < 1e-10:
                print(f"  Root {i}: {root.real:.4f}")
            else:
                print(f"  Root {i}: {root:.4f}")
                print(f"    Real: {root.real:.4f}, Imag: {root.imag:.4f}")
    
    vertex = QuadraticSolver.get_vertex(a, b, c)
    if vertex:
        print(f"Vertex: ({vertex[0]:.2f}, {vertex[1]:.2f})")
```

### Example 3: Fourier Series Analysis

```python
import cmath
import math

class FourierAnalyzer:
    def __init__(self, period=2*math.pi):
        self.period = period
        self.omega = 2 * math.pi / period
    
    def fourier_coefficient(self, func, n):
        """Calculate nth Fourier coefficient numerically"""
        def integrand(t):
            return func(t) * cmath.exp(-1j * n * self.omega * t)
        
        # Numerical integration
        N = 1000
        dt = self.period / N
        integral = 0 + 0j
        
        for k in range(N):
            t = k * dt
            integral += integrand(t) * dt
        
        return integral / self.period
    
    def analyze(self, func, num_harmonics=10):
        """Analyze signal and return harmonics"""
        coefficients = {}
        
        for n in range(-num_harmonics, num_harmonics + 1):
            cn = self.fourier_coefficient(func, n)
            if abs(cn) > 1e-10:
                coefficients[n] = cn
        
        return coefficients
    
    def reconstruct(self, coefficients, t):
        """Reconstruct signal from Fourier coefficients"""
        result = 0 + 0j
        for n, cn in coefficients.items():
            result += cn * cmath.exp(1j * n * self.omega * t)
        return result.real

# Define square wave
def square_wave(t):
    period = 2 * math.pi
    return 1 if (t % period) < period/2 else -1

# Analyze
analyzer = FourierAnalyzer(period=2*math.pi)
coeffs = analyzer.analyze(square_wave, num_harmonics=10)

print("FOURIER SERIES ANALYSIS")
print("=" * 40)
print("Square Wave Harmonics:")

for n in sorted(coeffs.keys()):
    cn = coeffs[n]
    if n == 0:
        print(f"  DC (n=0): {cn:.4f}")
    else:
        magnitude = abs(cn)
        phase = math.degrees(cmath.phase(cn))
        print(f"  n={n:2d}: magnitude={magnitude:.4f}, phase={phase:.1f}°")

# Reconstruct at specific point
t_test = math.pi / 4  # 45 degrees
original = square_wave(t_test)
reconstructed = analyzer.reconstruct(coeffs, t_test)

print(f"\nAt t = {t_test:.3f} rad:")
print(f"  Original: {original}")
print(f"  Reconstructed: {reconstructed:.4f}")
print(f"  Error: {abs(original - reconstructed):.4f}")
```

### Example 4: Signal Processing

```python
import cmath
import math

class SignalProcessor:
    @staticmethod
    def to_phasor(amplitude, phase_deg):
        """Convert amplitude and phase to complex phasor"""
        phase_rad = math.radians(phase_deg)
        return amplitude * cmath.exp(1j * phase_rad)
    
    @staticmethod
    def from_phasor(phasor):
        """Convert phasor to amplitude and phase"""
        amplitude = abs(phasor)
        phase_deg = math.degrees(cmath.phase(phasor))
        return amplitude, phase_deg
    
    @staticmethod
    def add_signals(signals):
        """Add multiple signals (phasor addition)"""
        return sum(signals)
    
    @staticmethod
    def multiply_signals(signals):
        """Multiply multiple signals"""
        result = 1 + 0j
        for s in signals:
            result *= s
        return result
    
    @staticmethod
    def impedance(components):
        """Calculate total impedance of parallel/series components"""
        # components: list of (type, value)
        # type: 'R', 'L', 'C'
        # frequency required
        
        # Simplified for demonstration
        pass

# Create signals
sig1 = SignalProcessor.to_phasor(10, 0)    # 10∠0°
sig2 = SignalProcessor.to_phasor(5, 90)    # 5∠90°
sig3 = SignalProcessor.to_phasor(8, -45)   # 8∠-45°

print("SIGNAL PROCESSING")
print("=" * 40)

print(f"Signal 1: {sig1:.2f} (10∠0°)")
print(f"Signal 2: {sig2:.2f} (5∠90°)")
print(f"Signal 3: {sig3:.2f} (8∠-45°)")

# Add signals
sum_signal = SignalProcessor.add_signals([sig1, sig2, sig3])
amp, phase = SignalProcessor.from_phasor(sum_signal)

print(f"\nSum: {sum_signal:.2f}")
print(f"  Amplitude: {amp:.2f}")
print(f"  Phase: {phase:.1f}°")

# Multiply signals
prod_signal = SignalProcessor.multiply_signals([sig1, sig2, sig3])
amp, phase = SignalProcessor.from_phasor(prod_signal)

print(f"\nProduct: {prod_signal:.2f}")
print(f"  Amplitude: {amp:.2f}")
print(f"  Phase: {phase:.1f}°")
```

### Example 5: Mandelbrot Set Visualization

```python
import cmath

class Mandelbrot:
    @staticmethod
    def mandelbrot(c, max_iter=100):
        """Check if point is in Mandelbrot set"""
        z = 0
        for n in range(max_iter):
            z = z * z + c
            if abs(z) > 2:
                return n
        return max_iter
    
    @staticmethod
    def generate(width, height, x_min=-2.0, x_max=1.0, y_min=-1.5, y_max=1.5, max_iter=100):
        """Generate Mandelbrot set image data"""
        image = []
        
        for y in range(height):
            row = []
            for x in range(width):
                # Map pixel to complex plane
                real = x_min + (x / width) * (x_max - x_min)
                imag = y_min + (y / height) * (y_max - y_min)
                c = complex(real, imag)
                
                iterations = Mandelbrot.mandelbrot(c, max_iter)
                row.append(iterations)
            image.append(row)
        
        return image
    
    @staticmethod
    def display_ascii(image, max_iter=100):
        """Display Mandelbrot set as ASCII art"""
        chars = " .:-=+*#%@"
        
        for row in image:
            line = ""
            for value in row:
                if value == max_iter:
                    char = '@'  # Inside set
                else:
                    idx = int(value / max_iter * (len(chars) - 1))
                    char = chars[idx]
                line += char
            print(line)

# Generate smaller Mandelbrot set (for demonstration)
width = 60
height = 30
max_iter = 50

print("MANDELBROT SET (ASCII ART)")
print("=" * 40)

mandelbrot = Mandelbrot()
image = mandelbrot.generate(width, height, max_iter=max_iter)
mandelbrot.display_ascii(image, max_iter)
```

---

## Practice Exercises

### Beginner Level

1. **Complex Number Operations**
   ```python
   # Add, subtract, multiply, divide two complex numbers
   # Print results in a+bi form
   ```

2. **Polar Conversion**
   ```python
   # Convert complex number to polar coordinates (r, θ)
   # Convert back to rectangular form
   ```

3. **Square Root of Negative**
   ```python
   # Calculate square root of negative numbers using cmath
   # Example: √-9 = 3j
   ```

### Intermediate Level

4. **Quadratic Solver**
   ```python
   # Solve quadratic equation with complex roots
   # Display roots in a+bi format
   ```

5. **AC Circuit Calculator**
   ```python
   # Calculate impedance of RLC circuit
   # Display in polar and rectangular form
   ```

6. **Euler's Formula Visualizer**
   ```python
   # Compute e^(iθ) for various θ values
   # Verify Euler's formula: e^(iθ) = cosθ + i·sinθ
   ```

### Advanced Level

7. **Fourier Series**
   ```python
   # Calculate Fourier coefficients for square wave
   # Reconstruct signal from coefficients
   ```

8. **Mandelbrot Set**
   ```python
   # Generate Mandelbrot set image
   # Color based on iteration count
   ```

9. **Signal Processing**
   ```python
   # Add multiple sinusoidal signals
   # Calculate resultant amplitude and phase
   ```

---

## Quick Reference Card

```python
import cmath

# Constants
cmath.pi          # π = 3.14159...
cmath.e           # e = 2.71828...
cmath.tau         # τ = 2π = 6.28318...
cmath.inf         # Infinity
cmath.nan         # Not a Number

# Conversion
cmath.phase(z)    # Phase angle in radians
cmath.polar(z)    # Returns (r, φ)
cmath.rect(r, φ)  # Returns complex number

# Powers and logs
cmath.sqrt(z)     # Square root
cmath.exp(z)      # e^z
cmath.log(z)      # Natural logarithm
cmath.log10(z)    # Base-10 logarithm
cmath.log2(z)     # Base-2 logarithm

# Trigonometric
cmath.sin(z)      # Sine
cmath.cos(z)      # Cosine
cmath.tan(z)      # Tangent
cmath.asin(z)     # Arc sine
cmath.acos(z)     # Arc cosine
cmath.atan(z)     # Arc tangent

# Hyperbolic
cmath.sinh(z)     # Hyperbolic sine
cmath.cosh(z)     # Hyperbolic cosine
cmath.tanh(z)     # Hyperbolic tangent
cmath.asinh(z)    # Inverse hyperbolic sine
cmath.acosh(z)    # Inverse hyperbolic cosine
cmath.atanh(z)    # Inverse hyperbolic tangent

# Classification
cmath.isinf(z)    # Check infinity
cmath.isnan(z)    # Check NaN
cmath.isfinite(z) # Check finite

# Complex number properties
z.real            # Real part
z.imag            # Imaginary part
z.conjugate()     # Complex conjugate
abs(z)            # Magnitude
```

---

## Next Step

- Move to [03_random.md](03_random.md) to learn about random number generation.

---

*Master the cmath module for complex number mathematics and engineering applications! 🐍✨*
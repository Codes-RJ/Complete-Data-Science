# 📘 TIME MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Time Module?](#what-is-the-time-module)
2. [Time Representations](#time-representations)
3. [`time.time()` – Unix Timestamp](#timetime--unix-timestamp)
4. [`time.sleep()` – Delay Execution](#timesleep--delay-execution)
5. [`time.perf_counter()` – High-Resolution Timing](#timeperf_counter--high-resolution-timing)
6. [`time.localtime()` – Convert to Local Time](#timelocaltime--convert-to-local-time)
7. [`time.gmtime()` – Convert to UTC](#timegmtime--convert-to-utc)
8. [`time.strftime()` – Format Time](#timestrftime--format-time)
9. [`time.strptime()` – Parse Time](#timestrptime--parse-time)
10. [`time.monotonic()` – Monotonic Clock](#timemonotonic--monotonic-clock)
11. [Real-World Examples](#real-world-examples)
12. [Practice Exercises](#practice-exercises)

---

## What is the Time Module?

The `time` module provides functions for working with time, including delays, timestamps, and converting between time representations.

```python
import time

# Current timestamp
print(time.time())        # 1705315200.123456

# Sleep for 2 seconds
time.sleep(2)

# High-precision timer
start = time.perf_counter()
# ... code ...
end = time.perf_counter()
print(f"Took {end - start:.6f}s")
```

**Key Characteristics:**
- ✅ Access to system time
- ✅ High-resolution timers
- ✅ Sleep/delay functions
- ✅ Timezone-aware conversions
- ✅ Formatting and parsing

---

## Time Representations

Python's `time` module uses three main representations:

| Representation | Type | Description | Example |
|----------------|------|-------------|---------|
| **Timestamp** | `float` | Seconds since epoch (Jan 1, 1970) | `1705315200.123456` |
| **Struct time** | `struct_time` | Broken-down time components | `tm_year=2024, tm_mon=1...` |
| **String** | `str` | Formatted time string | `"2024-01-15 10:30:45"` |

```python
import time

# Timestamp
timestamp = time.time()
print(f"Timestamp: {timestamp}")

# Struct time
struct_time = time.localtime()
print(f"Year: {struct_time.tm_year}")
print(f"Month: {struct_time.tm_mon}")
print(f"Day: {struct_time.tm_mday}")

# String
time_string = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {time_string}")
```

---

## `time.time()` – Unix Timestamp

Returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC).

```python
import time

# Current timestamp
timestamp = time.time()
print(f"Timestamp: {timestamp}")

# Convert to different units
seconds = timestamp
minutes = timestamp / 60
hours = timestamp / 3600
days = timestamp / 86400
years = timestamp / 31536000

print(f"Seconds since epoch: {seconds:.0f}")
print(f"Minutes: {minutes:.0f}")
print(f"Hours: {hours:.0f}")
print(f"Days: {days:.0f}")
print(f"Years: {years:.2f}")
```

### Measuring Elapsed Time

```python
import time

start = time.time()

# Simulate work
time.sleep(1.5)

end = time.time()
elapsed = end - start

print(f"Elapsed: {elapsed:.3f} seconds")
```

---

## `time.sleep()` – Delay Execution

Pauses the program for a specified number of seconds.

```python
import time

# Sleep for 1 second
time.sleep(1)
print("After 1 second")

# Sleep for 0.5 seconds (500 milliseconds)
time.sleep(0.5)
print("After 0.5 seconds")

# Countdown
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)
print("Blast off!")
```

### Sleep with Progress Indicator

```python
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\rTime remaining: {i} seconds", end="")
        time.sleep(1)
    print("\nDone!")

countdown(5)
```

---

## `time.perf_counter()` – High-Resolution Timing

Provides the highest available resolution timer for performance measurement.

```python
import time

# Measure code execution time
start = time.perf_counter()

# Code to measure
result = sum(range(1000000))

end = time.perf_counter()
elapsed = end - start

print(f"Sum: {result}")
print(f"Time: {elapsed:.6f} seconds")
```

### Performance Comparison

```python
import time

def test_list_comprehension():
    return [x**2 for x in range(10000)]

def test_manual_loop():
    result = []
    for x in range(10000):
        result.append(x**2)
    return result

# Measure list comprehension
start = time.perf_counter()
test_list_comprehension()
end = time.perf_counter()
print(f"List comprehension: {end - start:.6f}s")

# Measure manual loop
start = time.perf_counter()
test_manual_loop()
end = time.perf_counter()
print(f"Manual loop: {end - start:.6f}s")
```

---

## `time.localtime()` – Convert to Local Time

Converts a timestamp to a struct_time in local time.

```python
import time

# Current local time
local = time.localtime()
print(local)
# time.struct_time(tm_year=2024, tm_mon=1, tm_mday=15, tm_hour=10, tm_min=30, tm_sec=45, tm_wday=0, tm_yday=15, tm_isdst=0)

# Access individual components
print(f"Year: {local.tm_year}")
print(f"Month: {local.tm_mon}")
print(f"Day: {local.tm_mday}")
print(f"Hour: {local.tm_hour}")
print(f"Minute: {local.tm_min}")
print(f"Second: {local.tm_sec}")
print(f"Weekday (0=Monday): {local.tm_wday}")
print(f"Day of year: {local.tm_yday}")
print(f"DST: {local.tm_isdst}")

# Convert specific timestamp
timestamp = 1705315200
local_time = time.localtime(timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))
```

---

## `time.gmtime()` – Convert to UTC

Converts a timestamp to a struct_time in UTC (Greenwich Mean Time).

```python
import time

# Current UTC time
utc = time.gmtime()
print(f"UTC: {time.strftime('%Y-%m-%d %H:%M:%S', utc)}")

# Local time
local = time.localtime()
print(f"Local: {time.strftime('%Y-%m-%d %H:%M:%S', local)}")

# Compare UTC and local
utc_hour = utc.tm_hour
local_hour = local.tm_hour
offset = local_hour - utc_hour
print(f"Timezone offset: {offset} hours")
```

---

## `time.strftime()` – Format Time

Converts a struct_time to a formatted string.

```python
import time

# Current time formatting
print(time.strftime("%Y-%m-%d"))              # 2024-01-15
print(time.strftime("%d/%m/%Y"))              # 15/01/2024
print(time.strftime("%B %d, %Y"))             # January 15, 2024
print(time.strftime("%A, %B %d, %Y"))         # Monday, January 15, 2024
print(time.strftime("%I:%M %p"))              # 10:30 AM
print(time.strftime("%H:%M:%S"))              # 10:30:45
print(time.strftime("%Y-%m-%d %H:%M:%S"))     # 2024-01-15 10:30:45

# With specific struct_time
local = time.localtime()
print(time.strftime("%Y/%m/%d %H:%M:%S", local))
```

### strftime Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Year (4 digits) | 2024 |
| `%y` | Year (2 digits) | 24 |
| `%m` | Month (01-12) | 01 |
| `%d` | Day (01-31) | 15 |
| `%H` | Hour (00-23) | 14 |
| `%I` | Hour (01-12) | 02 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%p` | AM/PM | AM |
| `%A` | Full weekday | Monday |
| `%a` | Abbreviated weekday | Mon |
| `%B` | Full month | January |
| `%b` | Abbreviated month | Jan |
| `%j` | Day of year (001-366) | 015 |
| `%U` | Week number (00-53) | 02 |
| `%w` | Weekday (0-6, Sunday=0) | 1 |
| `%c` | Locale date/time | Mon Jan 15 10:30:45 2024 |
| `%x` | Locale date | 01/15/24 |
| `%X` | Locale time | 10:30:45 |

---

## `time.strptime()` – Parse Time

Parses a time string into a struct_time.

```python
import time

# Parse standard formats
time_string = "2024-01-15 10:30:45"
parsed = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(parsed)

# Parse date only
date_string = "2024-12-25"
parsed = time.strptime(date_string, "%Y-%m-%d")
print(f"Year: {parsed.tm_year}, Month: {parsed.tm_mon}, Day: {parsed.tm_mday}")

# Parse with different format
date_string = "15/01/2024"
parsed = time.strptime(date_string, "%d/%m/%Y")
print(f"Year: {parsed.tm_year}, Month: {parsed.tm_mon}, Day: {parsed.tm_mday}")
```

---

## `time.monotonic()` – Monotonic Clock

Returns a monotonic clock that cannot go backward (unaffected by system time changes).

```python
import time

# Monotonic clock for measuring intervals
start = time.monotonic()

time.sleep(1.5)

end = time.monotonic()
print(f"Elapsed: {end - start:.3f} seconds")

# Unlike time.time(), monotonic() won't jump if system time changes
# Better for measuring durations
```

---

## Real-World Examples

### Example 1: Simple Stopwatch

```python
import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False
    
    def start(self):
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True
            print("Stopwatch started")
    
    def stop(self):
        if self.running:
            self.elapsed += time.perf_counter() - self.start_time
            self.running = False
            print(f"Stopwatch stopped. Total: {self.elapsed:.2f}s")
    
    def reset(self):
        self.elapsed = 0
        self.running = False
        self.start_time = None
        print("Stopwatch reset")
    
    def lap(self):
        if self.running:
            current = time.perf_counter() - self.start_time + self.elapsed
            print(f"Lap: {current:.2f}s")
        else:
            print("Stopwatch not running")
    
    def get_time(self):
        if self.running:
            return self.elapsed + (time.perf_counter() - self.start_time)
        return self.elapsed

# Usage
stopwatch = Stopwatch()
stopwatch.start()
time.sleep(2)
stopwatch.lap()
time.sleep(1)
stopwatch.stop()
```

### Example 2: Rate Limiter

```python
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, time_window):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
    
    def can_call(self):
        now = time.time()
        
        # Remove old calls
        while self.calls and self.calls[0] < now - self.time_window:
            self.calls.popleft()
        
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False
    
    def wait_if_needed(self):
        if not self.can_call():
            now = time.time()
            oldest = self.calls[0]
            wait_time = self.time_window - (now - oldest)
            print(f"Rate limit reached. Waiting {wait_time:.2f}s...")
            time.sleep(wait_time)
            self.calls.append(time.time())
        return True

# Usage
limiter = RateLimiter(max_calls=3, time_window=5)

for i in range(10):
    if limiter.can_call():
        print(f"Call {i+1} at {time.strftime('%H:%M:%S')}")
    else:
        print(f"Call {i+1} blocked")
    time.sleep(0.5)
```

### Example 3: Retry with Exponential Backoff

```python
import time
import random

def retry_with_backoff(func, max_retries=5, base_delay=1, backoff_factor=2):
    """Retry function with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (backoff_factor ** attempt)
            print(f"Attempt {attempt + 1} failed: {e}")
            print(f"Retrying in {delay:.2f} seconds...")
            time.sleep(delay)

# Example usage
def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

result = retry_with_backoff(unstable_function, max_retries=5)
print(f"Result: {result}")
```

### Example 4: Performance Benchmark

```python
import time

class Benchmark:
    def __init__(self, name="Benchmark"):
        self.name = name
        self.times = []
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        self.times.append(self.elapsed)
        print(f"{self.name}: {self.elapsed:.6f}s")
    
    def average(self):
        if not self.times:
            return 0
        return sum(self.times) / len(self.times)
    
    def stats(self):
        if not self.times:
            return {}
        return {
            'min': min(self.times),
            'max': max(self.times),
            'avg': sum(self.times) / len(self.times),
            'count': len(self.times)
        }

# Usage
def test_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Single measurement
with Benchmark("Test") as b:
    result = test_function()

# Multiple measurements
bench = Benchmark("Multiple")
for _ in range(5):
    with bench:
        test_function()

print(f"\nStats: {bench.stats()}")
```

### Example 5: Timeout Decorator

```python
import time
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds):
    """Decorator that raises TimeoutError after specified seconds"""
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError(f"Function timed out after {seconds} seconds")
        
        def wrapper(*args, **kwargs):
            # Set timeout handler
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)  # Disable alarm
            
            return result
        
        return wrapper
    return decorator

@timeout(3)
def slow_function():
    print("Starting...")
    time.sleep(5)
    print("Finished")
    return "Done"

try:
    result = slow_function()
except TimeoutError as e:
    print(f"Timeout: {e}")
```

---

## Practice Exercises

### Beginner Level

1. **Sleep and Print**
   ```python
   # Print numbers 1 to 5 with 1-second delay between each
   ```

2. **Current Timestamp**
   ```python
   # Print current timestamp and convert to readable format
   ```

3. **Simple Timer**
   ```python
   # Measure how long it takes to execute a loop
   ```

### Intermediate Level

4. **Countdown Timer**
   ```python
   # Create a countdown timer that prints remaining seconds
   ```

5. **Rate Limiter**
   ```python
   # Implement rate limiter that allows 2 calls per second
   ```

6. **Retry Logic**
   ```python
   # Retry failed function with increasing delays
   ```

### Advanced Level

7. **Stopwatch Class**
   ```python
   # Implement Stopwatch with start, stop, lap, reset methods
   ```

8. **Performance Benchmark**
   ```python
   # Create decorator to measure function execution time
   ```

9. **Timeout Decorator**
   ```python
   # Implement timeout decorator using alarm signals
   ```

---

## Quick Reference Card

```python
import time

# Timestamps
time.time()                 # Current timestamp (seconds since epoch)
time.sleep(seconds)         # Sleep for seconds

# Performance timing
time.perf_counter()         # High-resolution timer
time.monotonic()            # Monotonic clock (can't go backward)

# Time conversion
time.localtime(timestamp)   # Convert to local struct_time
time.gmtime(timestamp)      # Convert to UTC struct_time
time.mktime(struct_time)    # Convert struct_time to timestamp

# Formatting and parsing
time.strftime(format, struct)   # Format struct_time to string
time.strptime(string, format)   # Parse string to struct_time

# Time components
struct.tm_year              # Year (e.g., 2024)
struct.tm_mon               # Month (1-12)
struct.tm_mday              # Day of month (1-31)
struct.tm_hour              # Hour (0-23)
struct.tm_min               # Minute (0-59)
struct.tm_sec               # Second (0-61)
struct.tm_wday              # Weekday (0-6, Monday=0)
struct.tm_yday              # Day of year (1-366)
struct.tm_isdst             # Daylight savings flag

# Common format strings
"%Y-%m-%d"                  # 2024-01-15
"%H:%M:%S"                  # 10:30:45
"%Y-%m-%d %H:%M:%S"         # 2024-01-15 10:30:45
"%B %d, %Y"                 # January 15, 2024
"%A, %B %d, %Y"             # Monday, January 15, 2024
```

---

## Next Step

- Move to [02_platform.md](02_platform.md) to learn about platform identification.

---

*Master the time module for timing, delays, and performance measurement! 🐍✨*
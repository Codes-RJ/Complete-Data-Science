Here's the **`06_signal.md`** file - complete guide to the `signal` module for signal handling in Python.

---

# 📘 SIGNAL MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Signals?](#what-are-signals)
2. [Signal Module Overview](#signal-module-overview)
3. [Common Signals](#common-signals)
4. [Handling Signals](#handling-signals)
5. [Ignoring Signals](#ignoring-signals)
6. [Sending Signals](#sending-signals)
7. [Alarm Signals](#alarm-signals)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What are Signals?

**Signals** are software interrupts delivered to a process to notify it of events. They are used for inter-process communication, handling system events, and graceful shutdown.

```python
import signal
import time

# Handle Ctrl+C gracefully
def signal_handler(signum, frame):
    print("\nInterrupted! Cleaning up...")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Press Ctrl+C to interrupt")
while True:
    time.sleep(1)
    print("Running...")
```

**Key Characteristics:**
- ✅ Asynchronous notifications
- ✅ Used for process control
- ✅ Handle interrupts (Ctrl+C)
- ✅ Set timeouts with alarms
- ✅ Cross-platform (with limitations)

---

## Signal Module Overview

The `signal` module provides functions to handle signals in Python.

```python
import signal

# List available signals (Unix)
print(dir(signal))
# SIGABRT, SIGALRM, SIGCHLD, SIGCONT, SIGINT, SIGKILL, etc.

# Signal names
for name in dir(signal):
    if name.startswith('SIG') and not name.startswith('SIG_'):
        print(name)
```

### Platform Differences

```python
import signal
import platform

print(f"Platform: {platform.system()}")

# Signals available on all platforms
common_signals = ['SIGINT', 'SIGTERM', 'SIGABRT']

# Unix-specific signals
unix_signals = ['SIGKILL', 'SIGSTOP', 'SIGUSR1', 'SIGUSR2', 'SIGALRM']

print("\nAvailable signals:")
for sig in common_signals + unix_signals:
    if hasattr(signal, sig):
        print(f"  {sig}")
```

---

## Common Signals

### Signal Constants

| Signal | Number | Meaning |
|--------|--------|---------|
| `SIGINT` | 2 | Interrupt (Ctrl+C) |
| `SIGTERM` | 15 | Termination request |
| `SIGKILL` | 9 | Force kill (cannot be caught) |
| `SIGSTOP` | 17 | Stop process (cannot be caught) |
| `SIGCONT` | 18 | Continue stopped process |
| `SIGALRM` | 14 | Alarm clock |
| `SIGUSR1` | 10 | User-defined signal 1 |
| `SIGUSR2` | 12 | User-defined signal 2 |
| `SIGABRT` | 6 | Abort signal |
| `SIGSEGV` | 11 | Segmentation fault |
| `SIGPIPE` | 13 | Broken pipe |

### Signal Numbers

```python
import signal

# Get signal numbers
print(f"SIGINT number: {signal.SIGINT}")    # 2
print(f"SIGTERM number: {signal.SIGTERM}")  # 15
print(f"SIGKILL number: {signal.SIGKILL}")  # 9
print(f"SIGALRM number: {signal.SIGALRM}")  # 14

# Get signal name from number
def get_signal_name(signum):
    for name in dir(signal):
        if name.startswith('SIG') and getattr(signal, name) == signum:
            return name
    return f"Unknown({signum})"

print(get_signal_name(2))   # SIGINT
print(get_signal_name(15))  # SIGTERM
```

---

## Handling Signals

### Basic Signal Handler

```python
import signal
import sys
import time

def handler(signum, frame):
    """Generic signal handler"""
    signal_name = signal.Signals(signum).name
    print(f"\nReceived signal: {signal_name}")
    
    if signum == signal.SIGINT:
        print("Interrupted by user")
        sys.exit(0)
    elif signum == signal.SIGTERM:
        print("Termination requested")
        sys.exit(0)
    else:
        print(f"Unhandled signal: {signum}")

# Register handler for multiple signals
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print(f"PID: {os.getpid()}")
print("Waiting for signals...")
while True:
    time.sleep(1)
```

### Signal Handler with State

```python
import signal
import time

class GracefulShutdown:
    def __init__(self):
        self.shutdown_requested = False
        self.cleanup_done = False
        
        # Register handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        signal_name = signal.Signals(signum).name
        print(f"\nReceived {signal_name}")
        
        if not self.shutdown_requested:
            print("Shutting down gracefully...")
            self.shutdown_requested = True
        else:
            print("Force exiting...")
            self.force_exit()
    
    def force_exit(self):
        """Force exit on second signal"""
        print("Performing emergency cleanup...")
        self.cleanup()
        exit(1)
    
    def cleanup(self):
        """Perform cleanup operations"""
        if self.cleanup_done:
            return
        print("Cleaning up resources...")
        time.sleep(1)
        print("Cleanup complete")
        self.cleanup_done = True
    
    def run(self):
        """Main loop"""
        print(f"PID: {os.getpid()}")
        print("Press Ctrl+C to shutdown gracefully")
        print("Press Ctrl+C again to force exit")
        
        while not self.shutdown_requested:
            print("Working...")
            time.sleep(2)
        
        self.cleanup()
        print("Goodbye!")

# Usage
# shutdown = GracefulShutdown()
# shutdown.run()
```

---

## Ignoring Signals

### Ignoring Signals

```python
import signal
import time

# Ignore SIGINT (Ctrl+C won't work)
signal.signal(signal.SIGINT, signal.SIG_IGN)

print("SIGINT is ignored. Ctrl+C won't work!")
print("Press Ctrl+\\ to quit (SIGQUIT)")

try:
    while True:
        print("Running...")
        time.sleep(1)
except KeyboardInterrupt:
    print("This won't be printed because SIGINT is ignored")
```

### Restoring Default Handlers

```python
import signal
import time

# Custom handler
def custom_handler(signum, frame):
    print("Custom handler called")

# Set custom handler
signal.signal(signal.SIGINT, custom_handler)
print("Custom handler active")
time.sleep(1)

# Restore default handler
signal.signal(signal.SIGINT, signal.SIG_DFL)
print("Default handler restored. Ctrl+C will now terminate.")

while True:
    time.sleep(1)
    print("Running...")
```

---

## Sending Signals

### Sending Signals to Processes

```python
import signal
import os
import time

def send_signal(pid, signal_type):
    """Send signal to process"""
    try:
        os.kill(pid, signal_type)
        print(f"Sent {signal.Signals(signal_type).name} to PID {pid}")
        return True
    except ProcessLookupError:
        print(f"Process {pid} not found")
        return False
    except PermissionError:
        print(f"Permission denied to send signal to {pid}")
        return False

# Example: send SIGTERM to process
# send_signal(12345, signal.SIGTERM)

# Send SIGINT (like Ctrl+C)
# send_signal(12345, signal.SIGINT)
```

### Signaling Self

```python
import signal
import os
import time

def handler(signum, frame):
    print(f"Received {signal.Signals(signum).name}")

# Register handler
signal.signal(signal.SIGUSR1, handler)
signal.signal(signal.SIGUSR2, handler)

print(f"PID: {os.getpid()}")
print("Sending signals to self...")

# Send signals to self
os.kill(os.getpid(), signal.SIGUSR1)
time.sleep(0.5)
os.kill(os.getpid(), signal.SIGUSR2)

print("Done")
```

---

## Alarm Signals

### Basic Alarm

```python
import signal
import time

def timeout_handler(signum, frame):
    print("\nTimeout occurred!")
    raise TimeoutError("Operation timed out")

# Set alarm handler
signal.signal(signal.SIGALRM, timeout_handler)

# Set alarm for 3 seconds
signal.alarm(3)

print("Starting operation...")
try:
    time.sleep(5)  # This will be interrupted
    print("Operation completed")
except TimeoutError as e:
    print(f"Error: {e}")
finally:
    # Cancel alarm
    signal.alarm(0)
```

### Alarm with Retry

```python
import signal
import time

class TimeoutOperation:
    def __init__(self, timeout=5):
        self.timeout = timeout
        self.timed_out = False
    
    def timeout_handler(self, signum, frame):
        print(f"\nTimeout after {self.timeout} seconds")
        self.timed_out = True
    
    def run_with_timeout(self, func, *args, **kwargs):
        """Run function with timeout"""
        # Set up handler
        old_handler = signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(self.timeout)
        
        try:
            result = func(*args, **kwargs)
            signal.alarm(0)  # Cancel alarm
            return result
        finally:
            signal.signal(signal.SIGALRM, old_handler)
    
    def retry_with_backoff(self, func, max_retries=3, *args, **kwargs):
        """Retry function with exponential backoff"""
        for attempt in range(max_retries):
            self.timed_out = False
            try:
                return self.run_with_timeout(func, *args, **kwargs)
            except Exception as e:
                if not self.timed_out:
                    raise
                
                wait_time = 2 ** attempt
                print(f"Retry {attempt + 1} in {wait_time}s...")
                time.sleep(wait_time)
        
        raise TimeoutError(f"Failed after {max_retries} attempts")

# Usage
def slow_operation():
    time.sleep(10)
    return "Success"

# op = TimeoutOperation(timeout=3)
# try:
#     result = op.run_with_timeout(slow_operation)
#     print(f"Result: {result}")
# except TimeoutError:
#     print("Operation timed out")
```

---

## Real-World Examples

### Example 1: Graceful Shutdown for Server

```python
import signal
import time
import sys

class Server:
    def __init__(self):
        self.running = True
        self.connections = []
        
        # Register signal handlers
        signal.signal(signal.SIGINT, self.shutdown_handler)
        signal.signal(signal.SIGTERM, self.shutdown_handler)
    
    def shutdown_handler(self, signum, frame):
        """Handle shutdown signals"""
        signal_name = signal.Signals(signum).name
        print(f"\nReceived {signal_name}, shutting down...")
        self.running = False
    
    def close_connections(self):
        """Close all active connections"""
        print(f"Closing {len(self.connections)} connections...")
        for conn in self.connections:
            conn.close()
        self.connections.clear()
    
    def save_state(self):
        """Save current state"""
        print("Saving state...")
        time.sleep(0.5)
    
    def cleanup(self):
        """Perform cleanup"""
        print("Cleaning up resources...")
        time.sleep(0.5)
    
    def run(self):
        """Main server loop"""
        print(f"Server started (PID: {os.getpid()})")
        print("Press Ctrl+C to stop")
        
        while self.running:
            # Simulate accepting connections
            print("Accepting connections...")
            time.sleep(2)
            
            # Simulate new connection
            self.connections.append(f"conn_{len(self.connections)}")
            print(f"Active connections: {len(self.connections)}")
        
        # Graceful shutdown
        print("\nPerforming graceful shutdown...")
        self.close_connections()
        self.save_state()
        self.cleanup()
        print("Server stopped")

# Usage
# server = Server()
# server.run()
```

### Example 2: Process Watcher

```python
import signal
import os
import time
import subprocess

class ProcessWatcher:
    def __init__(self, command):
        self.command = command
        self.process = None
        self.running = True
        
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        print(f"\nReceived {signal.Signals(signum).name}")
        self.stop()
    
    def start(self):
        """Start the process"""
        print(f"Starting: {self.command}")
        self.process = subprocess.Popen(
            self.command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print(f"Process started with PID: {self.process.pid}")
        
        while self.running and self.process.poll() is None:
            # Read output line by line
            line = self.process.stdout.readline()
            if line:
                print(f"[OUT] {line.strip()}")
            time.sleep(0.1)
        
        if self.process.poll() is not None:
            print(f"Process exited with code: {self.process.returncode}")
    
    def stop(self):
        """Stop the process gracefully"""
        self.running = False
        
        if self.process and self.process.poll() is None:
            print("Terminating process...")
            self.process.terminate()
            
            # Wait for termination
            try:
                self.process.wait(timeout=5)
                print("Process terminated")
            except subprocess.TimeoutExpired:
                print("Force killing process...")
                self.process.kill()
                self.process.wait()
    
    def run(self):
        """Run the watcher"""
        try:
            self.start()
        except KeyboardInterrupt:
            self.stop()
        finally:
            if self.process:
                self.process.wait()

# Usage
# watcher = ProcessWatcher('ping google.com')
# watcher.run()
```

### Example 3: Timeout Decorator

```python
import signal
import time
from functools import wraps

class TimeoutError(Exception):
    pass

def timeout(seconds):
    """Decorator that raises TimeoutError after specified seconds"""
    def decorator(func):
        def timeout_handler(signum, frame):
            raise TimeoutError(f"Function '{func.__name__}' timed out after {seconds} seconds")
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Save old handler
            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(seconds)
            
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            
            return result
        
        return wrapper
    return decorator

# Usage
@timeout(3)
def slow_function():
    time.sleep(5)
    return "Done"

@timeout(1)
def fast_function():
    return "Instant"

try:
    print(fast_function())  # Instant
    print(slow_function())  # Raises TimeoutError
except TimeoutError as e:
    print(f"Error: {e}")
```

### Example 4: Signal-Based IPC

```python
import signal
import os
import time

class IPCSignal:
    def __init__(self):
        self.message = None
        self.sender_pid = None
        
        signal.signal(signal.SIGUSR1, self.sigusr1_handler)
        signal.signal(signal.SIGUSR2, self.sigusr2_handler)
    
    def sigusr1_handler(self, signum, frame):
        """Handle SIGUSR1 (custom message)"""
        self.message = "Ping received"
        self.sender_pid = None
    
    def sigusr2_handler(self, signum, frame):
        """Handle SIGUSR2 (custom message with data)"""
        # In real implementation, you'd need a way to pass data
        self.message = "Custom message received"
        self.sender_pid = None
    
    def send_message(self, target_pid, message_type='ping'):
        """Send message to another process"""
        if message_type == 'ping':
            signal_num = signal.SIGUSR1
        else:
            signal_num = signal.SIGUSR2
        
        try:
            os.kill(target_pid, signal_num)
            print(f"Sent {signal.Signals(signal_num).name} to PID {target_pid}")
            return True
        except ProcessLookupError:
            print(f"Process {target_pid} not found")
            return False
        except PermissionError:
            print(f"Permission denied to send signal to {target_pid}")
            return False
    
    def wait_for_message(self, timeout=10):
        """Wait for message with timeout"""
        start = time.time()
        while time.time() - start < timeout:
            if self.message:
                msg = self.message
                self.message = None
                return msg
            time.sleep(0.1)
        return None

# Usage in two processes:
# Process A (receiver)
# ipc = IPCSignal()
# print("Waiting for message...")
# msg = ipc.wait_for_message()
# print(f"Received: {msg}")

# Process B (sender)
# ipc = IPCSignal()
# ipc.send_message(target_pid, 'ping')
```

---

## Practice Exercises

### Beginner Level

1. **Handle Ctrl+C**
   ```python
   # Write program that prints "Goodbye!" when Ctrl+C is pressed
   ```

2. **Ignore Signal**
   ```python
   # Make program ignore SIGINT (Ctrl+C)
   ```

3. **Print Signal Info**
   ```python
   # Print signal number and name for SIGTERM
   ```

### Intermediate Level

4. **Graceful Shutdown**
   ```python
   # Implement graceful shutdown with cleanup
   ```

5. **Alarm Timer**
   ```python
   # Set alarm for 5 seconds and print "Time's up!"
   ```

6. **Signal Handler with State**
   ```python
   # Track number of times signal was received
   ```

### Advanced Level

7. **Timeout Decorator**
   ```python
   # Create decorator that times out functions
   ```

8. **Process Watcher**
   ```python
   # Monitor child process and handle its signals
   ```

9. **Signal-Based IPC**
   ```python
   # Implement simple IPC using user signals
   ```

---

## Quick Reference Card

```python
import signal

# Signal constants
signal.SIGINT      # Interrupt (Ctrl+C)
signal.SIGTERM     # Termination
signal.SIGKILL     # Kill (cannot be caught)
signal.SIGSTOP     # Stop (cannot be caught)
signal.SIGALRM     # Alarm
signal.SIGUSR1     # User-defined 1
signal.SIGUSR2     # User-defined 2
signal.SIGABRT     # Abort
signal.SIGPIPE     # Broken pipe

# Signal actions
signal.SIG_DFL     # Default action
signal.SIG_IGN     # Ignore signal

# Functions
signal.signal(signum, handler)    # Set signal handler
signal.getsignal(signum)          # Get current handler
signal.alarm(seconds)             # Schedule SIGALRM
signal.pause()                    # Wait for signal
signal.valid_signals()            # List valid signals (3.8+)
signal.strsignal(signum)          # Get signal name

# Send signal
os.kill(pid, signum)              # Send signal to process

# Signal handler
def handler(signum, frame):
    print(f"Received signal {signum}")

# Common patterns
# Graceful shutdown
def shutdown_handler(signum, frame):
    print("Shutting down...")
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

# Ignore signal
signal.signal(signal.SIGPIPE, signal.SIG_IGN)

# Alarm
def alarm_handler(signum, frame):
    print("Timeout!")

signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(5)  # 5 seconds
```

---

## Next Step

- Move to [07_file_handling](../07_file_handling/README.md) to learn about file operations.

---

*Master the signal module for process control and graceful shutdown! 🐍✨*
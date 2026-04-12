# 📘 HASHLIB MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Hashing?](#what-is-hashing)
2. [Hashlib Overview](#hashlib-overview)
3. [Common Hash Algorithms](#common-hash-algorithms)
4. [Hashing Strings and Bytes](#hashing-strings-and-bytes)
5. [Hashing Files](#hashing-files)
6. [Salt and Key Derivation](#salt-and-key-derivation)
7. [Real-World Examples](#real-world-examples)
8. [Practice Exercises](#practice-exercises)

---

## What is Hashing?

**Hashing** is a one-way function that converts input data of any size into a fixed-size string of characters. Hashes are deterministic (same input produces same output) but cannot be reversed.

```python
import hashlib

# Hash a string
text = "Hello World"
hash_object = hashlib.sha256(text.encode())
hex_digest = hash_object.hexdigest()

print(f"Original: {text}")
print(f"SHA-256: {hex_digest}")
# SHA-256: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

**Key Characteristics:**
- ✅ One-way (cannot reverse to original)
- ✅ Deterministic (same input = same output)
- ✅ Fixed length (regardless of input size)
- ✅ Avalanche effect (small change = completely different hash)
- ✅ Not encryption (cannot be decrypted)

---

## Hashlib Overview

The `hashlib` module provides a common interface to many secure hash algorithms.

### Available Algorithms

```python
import hashlib

# List available algorithms
print("Available algorithms:")
print(f"  hashlib.algorithms_available: {len(hashlib.algorithms_available)}")
print(f"  hashlib.algorithms_guaranteed: {len(hashlib.algorithms_guaranteed)}")

# Common algorithms
common_algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
for algo in common_algorithms:
    if algo in hashlib.algorithms_available:
        print(f"  ✓ {algo}")
    else:
        print(f"  ✗ {algo}")
```

### Basic Usage Pattern

```python
import hashlib

# Method 1: Create hash object then update
hash_obj = hashlib.sha256()
hash_obj.update(b"Hello")
hash_obj.update(b" World")
print(hash_obj.hexdigest())

# Method 2: One-shot hashing
hash_obj = hashlib.sha256(b"Hello World")
print(hash_obj.hexdigest())

# Method 3: Using convenience function
hash_obj = hashlib.new('sha256', b"Hello World")
print(hash_obj.hexdigest())
```

---

## Common Hash Algorithms

### MD5 (128-bit) – Fast but NOT Secure

```python
import hashlib

text = "Hello World"
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"MD5: {md5_hash}")
# MD5: b10a8db164e0754105b7a99be72e3fe5

# MD5 is cryptographically broken, but still useful for checksums
file_checksum = hashlib.md5(b"file content").hexdigest()
print(f"File checksum: {file_checksum}")
```

### SHA-1 (160-bit) – Deprecated

```python
import hashlib

text = "Hello World"
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
print(f"SHA-1: {sha1_hash}")
# SHA-1: 0a4d55a8d778e5022fab701977c5d840bbc486d0

# SHA-1 is also considered broken for security
```

### SHA-2 Family (SHA-224, SHA-256, SHA-384, SHA-512)

```python
import hashlib

text = "Hello World"

# SHA-224 (224 bits)
sha224 = hashlib.sha224(text.encode()).hexdigest()
print(f"SHA-224: {sha224}")

# SHA-256 (256 bits) - Most common
sha256 = hashlib.sha256(text.encode()).hexdigest()
print(f"SHA-256: {sha256}")

# SHA-384 (384 bits)
sha384 = hashlib.sha384(text.encode()).hexdigest()
print(f"SHA-384: {sha384}")

# SHA-512 (512 bits) - Most secure in SHA-2 family
sha512 = hashlib.sha512(text.encode()).hexdigest()
print(f"SHA-512: {sha512}")
```

### SHA-3 Family (Keccak)

```python
import hashlib

text = "Hello World"

# SHA3-224
sha3_224 = hashlib.sha3_224(text.encode()).hexdigest()
print(f"SHA3-224: {sha3_224}")

# SHA3-256
sha3_256 = hashlib.sha3_256(text.encode()).hexdigest()
print(f"SHA3-256: {sha3_256}")

# SHA3-384
sha3_384 = hashlib.sha3_384(text.encode()).hexdigest()
print(f"SHA3-384: {sha3_384}")

# SHA3-512
sha3_512 = hashlib.sha3_512(text.encode()).hexdigest()
print(f"SHA3-512: {sha3_512}")
```

### BLAKE2 (BLAKE2b, BLAKE2s)

```python
import hashlib

text = "Hello World"

# BLAKE2b (64-bit platform, faster on 64-bit)
blake2b = hashlib.blake2b(text.encode()).hexdigest()
print(f"BLAKE2b: {blake2b}")

# BLAKE2s (32-bit platform, faster on 32-bit)
blake2s = hashlib.blake2s(text.encode()).hexdigest()
print(f"BLAKE2s: {blake2s}")

# BLAKE2 with custom digest size
blake2b_32 = hashlib.blake2b(text.encode(), digest_size=32).hexdigest()
print(f"BLAKE2b-32: {blake2b_32}")
```

---

## Hashing Strings and Bytes

### Hashing Strings

```python
import hashlib

def hash_string(text, algorithm='sha256'):
    """Hash a string using specified algorithm"""
    if algorithm == 'md5':
        hash_obj = hashlib.md5(text.encode())
    elif algorithm == 'sha1':
        hash_obj = hashlib.sha1(text.encode())
    elif algorithm == 'sha256':
        hash_obj = hashlib.sha256(text.encode())
    elif algorithm == 'sha512':
        hash_obj = hashlib.sha512(text.encode())
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    
    return hash_obj.hexdigest()

# Examples
text = "password123"
print(f"Original: {text}")
print(f"MD5: {hash_string(text, 'md5')}")
print(f"SHA-256: {hash_string(text, 'sha256')}")
print(f"SHA-512: {hash_string(text, 'sha512')}")
```

### Incremental Hashing

```python
import hashlib

# Hash large data in chunks
def hash_large_data(data_chunks, algorithm='sha256'):
    """Hash data that comes in chunks"""
    hash_obj = hashlib.new(algorithm)
    
    for chunk in data_chunks:
        hash_obj.update(chunk)
    
    return hash_obj.hexdigest()

# Example with simulated chunks
chunks = [b"Hello ", b"World ", b"from ", b"Python"]
result = hash_large_data(chunks)
print(f"Incremental hash: {result}")

# Equivalent one-shot hash
full_data = b"".join(chunks)
direct_hash = hashlib.sha256(full_data).hexdigest()
print(f"Direct hash: {direct_hash}")
print(f"Match: {result == direct_hash}")
```

---

## Hashing Files

### Basic File Hashing

```python
import hashlib

def hash_file(filename, algorithm='sha256', chunk_size=4096):
    """Calculate hash of a file"""
    hash_obj = hashlib.new(algorithm)
    
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()

# Example (create a test file first)
with open('test.txt', 'w') as f:
    f.write('Hello World')

print(f"MD5: {hash_file('test.txt', 'md5')}")
print(f"SHA-256: {hash_file('test.txt', 'sha256')}")

# Clean up
import os
os.remove('test.txt')
```

### File Integrity Checker

```python
import hashlib
import os

class FileIntegrityChecker:
    def __init__(self, algorithm='sha256'):
        self.algorithm = algorithm
        self.manifest = {}
    
    def compute_hash(self, filepath):
        """Compute hash of a file"""
        hash_obj = hashlib.new(self.algorithm)
        
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    def create_manifest(self, directory):
        """Create manifest of all files in directory"""
        self.manifest = {}
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, directory)
                self.manifest[rel_path] = self.compute_hash(filepath)
        
        return self.manifest
    
    def verify_integrity(self, directory):
        """Verify files against manifest"""
        issues = []
        
        for rel_path, expected_hash in self.manifest.items():
            filepath = os.path.join(directory, rel_path)
            
            if not os.path.exists(filepath):
                issues.append(f"Missing: {rel_path}")
                continue
            
            current_hash = self.compute_hash(filepath)
            if current_hash != expected_hash:
                issues.append(f"Modified: {rel_path}")
        
        return issues

# Usage
checker = FileIntegrityChecker('sha256')
# checker.create_manifest('.')
# issues = checker.verify_integrity('.')
```

---

## Salt and Key Derivation

### Simple Salted Hashing

```python
import hashlib
import os

def hash_password(password, salt=None):
    """Hash password with salt"""
    if salt is None:
        salt = os.urandom(32)  # Generate random salt
    
    # Combine password and salt
    salted = password.encode() + salt
    
    # Hash the combination
    hash_obj = hashlib.pbkdf2_hmac('sha256', salted, salt, 100000)
    
    return salt, hash_obj

def verify_password(password, salt, stored_hash):
    """Verify password against stored hash"""
    _, computed_hash = hash_password(password, salt)
    return computed_hash == stored_hash

# Usage
password = "my_secret_password"
salt, hash_value = hash_password(password)

print(f"Salt (hex): {salt.hex()}")
print(f"Hash (hex): {hash_value.hex()}")

# Verify
is_valid = verify_password("my_secret_password", salt, hash_value)
print(f"Correct password: {is_valid}")

is_valid = verify_password("wrong_password", salt, hash_value)
print(f"Wrong password: {is_valid}")
```

### PBKDF2 – Key Derivation Function

```python
import hashlib
import binascii
import os

class PasswordHasher:
    def __init__(self, algorithm='sha256', iterations=100000):
        self.algorithm = algorithm
        self.iterations = iterations
    
    def hash(self, password, salt=None):
        """Hash password using PBKDF2"""
        if salt is None:
            salt = os.urandom(32)
        
        hash_bytes = hashlib.pbkdf2_hmac(
            self.algorithm,
            password.encode(),
            salt,
            self.iterations,
            dklen=64
        )
        
        return {
            'salt': binascii.hexlify(salt).decode(),
            'hash': binascii.hexlify(hash_bytes).decode(),
            'algorithm': self.algorithm,
            'iterations': self.iterations
        }
    
    def verify(self, password, stored_data):
        """Verify password against stored hash"""
        salt = binascii.unhexlify(stored_data['salt'])
        hash_bytes = hashlib.pbkdf2_hmac(
            stored_data['algorithm'],
            password.encode(),
            salt,
            stored_data['iterations'],
            dklen=64
        )
        
        computed_hash = binascii.hexlify(hash_bytes).decode()
        return computed_hash == stored_data['hash']
    
    @staticmethod
    def to_string(stored_data):
        """Convert stored data to string format"""
        return f"{stored_data['algorithm']}${stored_data['iterations']}${stored_data['salt']}${stored_data['hash']}"
    
    @staticmethod
    def from_string(data_string):
        """Parse stored data from string format"""
        algorithm, iterations, salt, hash_value = data_string.split('$')
        return {
            'algorithm': algorithm,
            'iterations': int(iterations),
            'salt': salt,
            'hash': hash_value
        }

# Usage
hasher = PasswordHasher(iterations=100000)

# Hash a password
stored = hasher.hash("my_secure_password")
print(f"Stored data: {stored}")

# Convert to string for storage
storage_string = PasswordHasher.to_string(stored)
print(f"Storage string: {storage_string}")

# Parse from string
parsed = PasswordHasher.from_string(storage_string)
print(f"Parsed data: {parsed}")

# Verify password
is_valid = hasher.verify("my_secure_password", parsed)
print(f"Valid: {is_valid}")

is_valid = hasher.verify("wrong_password", parsed)
print(f"Valid: {is_valid}")
```

### bcrypt Alternative (Third-party)

```python
# Note: bcrypt requires installation: pip install bcrypt
# import bcrypt

# password = b"my_secret_password"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# print(f"Hashed: {hashed}")
# 
# is_valid = bcrypt.checkpw(password, hashed)
# print(f"Valid: {is_valid}")
```

---

## Real-World Examples

### Example 1: Password Manager

```python
import hashlib
import os
import json
from getpass import getpass

class PasswordManager:
    def __init__(self, master_password, data_file='passwords.json'):
        self.master_password = master_password
        self.data_file = data_file
        self.passwords = {}
        self.salt = os.urandom(32)
    
    def _derive_key(self, password):
        """Derive encryption key from password"""
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self.salt,
            100000,
            dklen=32
        )
    
    def authenticate(self):
        """Authenticate user with master password"""
        derived = self._derive_key(self.master_password)
        # In real implementation, store and compare derived key
        return True
    
    def add_password(self, service, username, password):
        """Add a password for a service"""
        if service not in self.passwords:
            self.passwords[service] = []
        
        self.passwords[service].append({
            'username': username,
            'password': password
        })
        self._save()
    
    def get_password(self, service, username=None):
        """Retrieve password for a service"""
        if service not in self.passwords:
            return None
        
        if username:
            for entry in self.passwords[service]:
                if entry['username'] == username:
                    return entry['password']
            return None
        
        return self.passwords[service]
    
    def _save(self):
        """Save passwords to file (encrypted in real implementation)"""
        with open(self.data_file, 'w') as f:
            json.dump(self.passwords, f, indent=2)
    
    def _load(self):
        """Load passwords from file"""
        try:
            with open(self.data_file, 'r') as f:
                self.passwords = json.load(f)
        except FileNotFoundError:
            self.passwords = {}

# Usage
# manager = PasswordManager("master_password")
# manager.add_password("github", "alice", "secure_pass123")
# password = manager.get_password("github", "alice")
# print(f"Retrieved password: {password}")
```

### Example 2: File Integrity Monitor

```python
import hashlib
import os
import time
from datetime import datetime

class FileIntegrityMonitor:
    def __init__(self, directory, algorithm='sha256'):
        self.directory = directory
        self.algorithm = algorithm
        self.baseline = {}
    
    def compute_file_hash(self, filepath):
        """Compute hash of a single file"""
        hash_obj = hashlib.new(self.algorithm)
        
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    def create_baseline(self):
        """Create baseline snapshot of all files"""
        self.baseline = {}
        
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, self.directory)
                self.baseline[rel_path] = {
                    'hash': self.compute_file_hash(filepath),
                    'size': os.path.getsize(filepath),
                    'modified': os.path.getmtime(filepath)
                }
        
        return self.baseline
    
    def check_integrity(self):
        """Check current files against baseline"""
        changes = {
            'new': [],
            'modified': [],
            'deleted': [],
            'size_changed': []
        }
        
        # Check current files against baseline
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, self.directory)
                
                if rel_path not in self.baseline:
                    changes['new'].append(rel_path)
                else:
                    current_hash = self.compute_file_hash(filepath)
                    if current_hash != self.baseline[rel_path]['hash']:
                        changes['modified'].append(rel_path)
                    
                    current_size = os.path.getsize(filepath)
                    if current_size != self.baseline[rel_path]['size']:
                        changes['size_changed'].append(rel_path)
        
        # Check for deleted files
        for rel_path in self.baseline:
            filepath = os.path.join(self.directory, rel_path)
            if not os.path.exists(filepath):
                changes['deleted'].append(rel_path)
        
        return changes
    
    def generate_report(self, changes):
        """Generate integrity report"""
        print("=" * 60)
        print(f"INTEGRITY REPORT - {datetime.now()}")
        print("=" * 60)
        
        if not any(changes.values()):
            print("✓ No changes detected")
            return
        
        if changes['new']:
            print(f"\n📄 New files ({len(changes['new'])}):")
            for f in changes['new'][:10]:
                print(f"  + {f}")
            if len(changes['new']) > 10:
                print(f"  ... and {len(changes['new']) - 10} more")
        
        if changes['modified']:
            print(f"\n✏️ Modified files ({len(changes['modified'])}):")
            for f in changes['modified'][:10]:
                print(f"  ~ {f}")
            if len(changes['modified']) > 10:
                print(f"  ... and {len(changes['modified']) - 10} more")
        
        if changes['deleted']:
            print(f"\n🗑️ Deleted files ({len(changes['deleted'])}):")
            for f in changes['deleted'][:10]:
                print(f"  - {f}")
            if len(changes['deleted']) > 10:
                print(f"  ... and {len(changes['deleted']) - 10} more")
        
        if changes['size_changed']:
            print(f"\n📏 Size changed ({len(changes['size_changed'])}):")
            for f in changes['size_changed'][:5]:
                print(f"  ! {f}")

# Usage
monitor = FileIntegrityMonitor('.')
# monitor.create_baseline()
# time.sleep(2)
# changes = monitor.check_integrity()
# monitor.generate_report(changes)
```

### Example 3: Duplicate File Finder

```python
import hashlib
import os
from collections import defaultdict

class DuplicateFileFinder:
    def __init__(self, algorithm='sha256'):
        self.algorithm = algorithm
        self.file_hashes = defaultdict(list)
    
    def compute_hash(self, filepath):
        """Compute hash of a file"""
        hash_obj = hashlib.new(self.algorithm)
        
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    def scan_directory(self, directory):
        """Scan directory for duplicate files"""
        self.file_hashes.clear()
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                
                # Skip empty files
                if os.path.getsize(filepath) == 0:
                    continue
                
                file_hash = self.compute_hash(filepath)
                self.file_hashes[file_hash].append(filepath)
        
        return self.get_duplicates()
    
    def get_duplicates(self):
        """Get duplicate file groups"""
        return {h: files for h, files in self.file_hashes.items() if len(files) > 1}
    
    def generate_report(self):
        """Generate duplicate files report"""
        duplicates = self.get_duplicates()
        
        if not duplicates:
            print("No duplicate files found")
            return
        
        total_duplicates = sum(len(files) - 1 for files in duplicates.values())
        total_size = 0
        
        print("=" * 60)
        print("DUPLICATE FILES REPORT")
        print("=" * 60)
        print(f"Duplicate groups: {len(duplicates)}")
        print(f"Duplicate files: {total_duplicates}")
        
        for i, (hash_val, files) in enumerate(duplicates.items(), 1):
            size = os.path.getsize(files[0])
            total_size += size * (len(files) - 1)
            
            print(f"\nGroup {i}: {len(files)} duplicates ({size:,} bytes each)")
            for filepath in files:
                print(f"  {filepath}")
        
        print(f"\nTotal wasted space: {total_size:,} bytes ({total_size / (1024**2):.2f} MB)")
    
    def delete_duplicates(self, keep_first=True):
        """Delete duplicate files (except first in each group)"""
        deleted = []
        
        for hash_val, files in self.file_hashes.items():
            if len(files) <= 1:
                continue
            
            # Keep first file, delete others
            files_to_delete = files[1:] if keep_first else files[:-1]
            
            for filepath in files_to_delete:
                try:
                    os.remove(filepath)
                    deleted.append(filepath)
                except Exception as e:
                    print(f"Error deleting {filepath}: {e}")
        
        return deleted

# Usage
finder = DuplicateFileFinder()
# finder.scan_directory('.')
# finder.generate_report()
# finder.delete_duplicates()
```

### Example 4: Checksum Validator for Downloads

```python
import hashlib
import requests
import sys

class ChecksumValidator:
    @staticmethod
    def compute_file_hash(filepath, algorithm='sha256'):
        """Compute hash of a file"""
        hash_obj = hashlib.new(algorithm)
        
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    @staticmethod
    def compute_url_hash(url, algorithm='sha256'):
        """Compute hash of content from URL"""
        hash_obj = hashlib.new(algorithm)
        response = requests.get(url, stream=True)
        
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    @staticmethod
    def verify_file(filepath, expected_hash, algorithm='sha256'):
        """Verify file against expected hash"""
        actual_hash = ChecksumValidator.compute_file_hash(filepath, algorithm)
        return actual_hash == expected_hash
    
    @staticmethod
    def verify_url(url, expected_hash, algorithm='sha256'):
        """Verify URL content against expected hash"""
        actual_hash = ChecksumValidator.compute_url_hash(url, algorithm)
        return actual_hash == expected_hash
    
    @staticmethod
    def generate_checksum_file(directory, output_file='checksums.txt', algorithm='sha256'):
        """Generate checksum file for all files in directory"""
        with open(output_file, 'w') as f:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, directory)
                    file_hash = ChecksumValidator.compute_file_hash(filepath, algorithm)
                    f.write(f"{algorithm}  {file_hash}  {rel_path}\n")
        
        print(f"Checksums written to {output_file}")
    
    @staticmethod
    def verify_from_checksum_file(checksum_file, directory='.'):
        """Verify files using checksum file"""
        errors = []
        
        with open(checksum_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split('  ')
                if len(parts) != 3:
                    continue
                
                algorithm, expected_hash, rel_path = parts
                filepath = os.path.join(directory, rel_path)
                
                if not os.path.exists(filepath):
                    errors.append(f"Missing: {rel_path}")
                    continue
                
                actual_hash = ChecksumValidator.compute_file_hash(filepath, algorithm)
                if actual_hash != expected_hash:
                    errors.append(f"Corrupted: {rel_path}")
        
        if errors:
            print("VERIFICATION FAILED:")
            for error in errors:
                print(f"  {error}")
        else:
            print("All files verified successfully")
        
        return errors

# Usage
# ChecksumValidator.generate_checksum_file('.', 'checksums.txt')
# ChecksumValidator.verify_from_checksum_file('checksums.txt')
```

---

## Practice Exercises

### Beginner Level

1. **MD5 Hash**
   ```python
   # Calculate MD5 hash of a string
   ```

2. **SHA-256 Hash**
   ```python
   # Calculate SHA-256 hash of a file
   ```

3. **Hash Comparison**
   ```python
   # Compare two files using their hashes
   ```

### Intermediate Level

4. **Password Hasher**
   ```python
   # Implement password hashing with salt
   ```

5. **File Integrity Checker**
   ```python
   # Monitor file changes using hashes
   ```

6. **Duplicate Finder**
   ```python
   # Find duplicate files using hashing
   ```

### Advanced Level

7. **Password Manager**
   ```python
   # Build password manager with PBKDF2
   ```

8. **Checksum Validator**
   ```python
   # Verify downloaded files using checksums
   ```

9. **Blockchain Simulator**
   ```python
   # Simple blockchain using SHA-256
   ```

---

## Quick Reference Card

```python
import hashlib

# Create hash object
hash_obj = hashlib.md5()                    # MD5 (fast, insecure)
hash_obj = hashlib.sha1()                   # SHA-1 (deprecated)
hash_obj = hashlib.sha256()                 # SHA-256 (recommended)
hash_obj = hashlib.sha512()                 # SHA-512 (more secure)
hash_obj = hashlib.sha3_256()               # SHA-3 (newest)
hash_obj = hashlib.blake2b()                # BLAKE2b (fast)
hash_obj = hashlib.new('sha256')            # Generic constructor

# Update with data
hash_obj.update(b'data')                    # Add bytes
hash_obj.update('string'.encode())          # Add string

# Get digest
hash_obj.digest()                           # Raw bytes
hash_obj.hexdigest()                        # Hexadecimal string

# One-shot hashing
hashlib.md5(b'data').hexdigest()
hashlib.sha256(b'data').hexdigest()

# File hashing (chunk by chunk)
with open('file.txt', 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b''):
        hash_obj.update(chunk)

# Key derivation (PBKDF2)
hashlib.pbkdf2_hmac('sha256', password, salt, iterations, dklen=32)

# Available algorithms
hashlib.algorithms_available               # All available
hashlib.algorithms_guaranteed              # Always available
```

---

## Next Step

- Move to [14_glob.md](14_glob.md) to learn about file pattern matching.

---

*Master hashlib for cryptographic hashing and data integrity verification! 🐍✨*
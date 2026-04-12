# 📘 STAT MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Stat Module?](#what-is-the-stat-module)
2. [File Types](#file-types)
3. [File Permissions](#file-permissions)
4. [Checking File Types](#checking-file-types)
5. [Checking File Permissions](#checking-file-permissions)
6. [Real-World Examples](#real-world-examples)
7. [Practice Exercises](#practice-exercises)

---

## What is the Stat Module?

The `stat` module defines constants and functions for interpreting the results of `os.stat()`, `os.fstat()`, and `os.lstat()`. These constants represent file types, permissions, and other file attributes.

```python
import os
import stat

# Get file status
file_stat = os.stat('example.txt')

# Check if it's a regular file
if stat.S_ISREG(file_stat.st_mode):
    print("It's a regular file")

# Check permissions
is_readable = bool(file_stat.st_mode & stat.S_IRUSR)
print(f"Owner readable: {is_readable}")
```

**Key Characteristics:**
- ✅ Constants for file type checking
- ✅ Constants for permission bits
- ✅ Works with `os.stat()` results
- ✅ Cross-platform compatible
- ✅ Low-level file attribute access

---

## File Types

### File Type Constants

| Constant | Meaning |
|----------|---------|
| `S_IFREG` | Regular file |
| `S_IFDIR` | Directory |
| `S_IFLNK` | Symbolic link |
| `S_IFCHR` | Character device |
| `S_IFBLK` | Block device |
| `S_IFIFO` | FIFO (named pipe) |
| `S_IFSOCK` | Socket |

### File Type Checking Functions

| Function | Purpose |
|----------|---------|
| `S_ISREG(mode)` | Is regular file? |
| `S_ISDIR(mode)` | Is directory? |
| `S_ISLNK(mode)` | Is symbolic link? |
| `S_ISCHR(mode)` | Is character device? |
| `S_ISBLK(mode)` | Is block device? |
| `S_ISFIFO(mode)` | Is FIFO? |
| `S_ISSOCK(mode)` | Is socket? |

### Basic Example

```python
import os
import stat

def describe_file(path):
    """Describe file type"""
    try:
        file_stat = os.stat(path)
        mode = file_stat.st_mode
        
        if stat.S_ISREG(mode):
            print(f"{path}: Regular file")
        elif stat.S_ISDIR(mode):
            print(f"{path}: Directory")
        elif stat.S_ISLNK(mode):
            print(f"{path}: Symbolic link")
        elif stat.S_ISCHR(mode):
            print(f"{path}: Character device")
        elif stat.S_ISBLK(mode):
            print(f"{path}: Block device")
        elif stat.S_ISFIFO(mode):
            print(f"{path}: FIFO")
        elif stat.S_ISSOCK(mode):
            print(f"{path}: Socket")
        else:
            print(f"{path}: Unknown type")
    except FileNotFoundError:
        print(f"{path}: Not found")

# Usage
# describe_file('/tmp')
# describe_file('/dev/null')
# describe_file('example.txt')
```

---

## File Permissions

### Permission Constants (Owner)

| Constant | Meaning | Octal |
|----------|---------|-------|
| `S_IRUSR` | Owner read | 0o400 |
| `S_IWUSR` | Owner write | 0o200 |
| `S_IXUSR` | Owner execute | 0o100 |

### Permission Constants (Group)

| Constant | Meaning | Octal |
|----------|---------|-------|
| `S_IRGRP` | Group read | 0o040 |
| `S_IWGRP` | Group write | 0o020 |
| `S_IXGRP` | Group execute | 0o010 |

### Permission Constants (Others)

| Constant | Meaning | Octal |
|----------|---------|-------|
| `S_IROTH` | Others read | 0o004 |
| `S_IWOTH` | Others write | 0o002 |
| `S_IXOTH` | Others execute | 0o001 |

### Special Permissions

| Constant | Meaning | Octal |
|----------|---------|-------|
| `S_ISUID` | Set user ID on execution | 0o4000 |
| `S_ISGID` | Set group ID on execution | 0o2000 |
| `S_ISVTX` | Sticky bit | 0o1000 |

---

## Checking File Types

### Complete File Type Checker

```python
import os
import stat
from pathlib import Path

class FileTypeChecker:
    @staticmethod
    def get_type(path):
        """Get file type as string"""
        try:
            mode = os.stat(path).st_mode
            
            if stat.S_ISREG(mode):
                return 'regular_file'
            elif stat.S_ISDIR(mode):
                return 'directory'
            elif stat.S_ISLNK(mode):
                return 'symlink'
            elif stat.S_ISCHR(mode):
                return 'char_device'
            elif stat.S_ISBLK(mode):
                return 'block_device'
            elif stat.S_ISFIFO(mode):
                return 'fifo'
            elif stat.S_ISSOCK(mode):
                return 'socket'
            else:
                return 'unknown'
        except FileNotFoundError:
            return 'not_found'
    
    @staticmethod
    def is_regular_file(path):
        """Check if path is regular file"""
        try:
            return stat.S_ISREG(os.stat(path).st_mode)
        except FileNotFoundError:
            return False
    
    @staticmethod
    def is_directory(path):
        """Check if path is directory"""
        try:
            return stat.S_ISDIR(os.stat(path).st_mode)
        except FileNotFoundError:
            return False
    
    @staticmethod
    def is_symlink(path):
        """Check if path is symlink (use lstat)"""
        try:
            return stat.S_ISLNK(os.lstat(path).st_mode)
        except FileNotFoundError:
            return False

# Usage
checker = FileTypeChecker()
# print(checker.get_type('/tmp'))
# print(checker.is_directory('/tmp'))
# print(checker.is_symlink('/usr/bin/python'))
```

---

## Checking File Permissions

### Permission Checker

```python
import os
import stat

class PermissionChecker:
    @staticmethod
    def get_permissions(path):
        """Get permissions as string (like ls -l)"""
        try:
            mode = os.stat(path).st_mode
            
            # File type
            if stat.S_ISDIR(mode):
                perms = 'd'
            elif stat.S_ISLNK(mode):
                perms = 'l'
            else:
                perms = '-'
            
            # Owner permissions
            perms += 'r' if mode & stat.S_IRUSR else '-'
            perms += 'w' if mode & stat.S_IWUSR else '-'
            perms += 'x' if mode & stat.S_IXUSR else '-'
            
            # Group permissions
            perms += 'r' if mode & stat.S_IRGRP else '-'
            perms += 'w' if mode & stat.S_IWGRP else '-'
            perms += 'x' if mode & stat.S_IXGRP else '-'
            
            # Others permissions
            perms += 'r' if mode & stat.S_IROTH else '-'
            perms += 'w' if mode & stat.S_IWOTH else '-'
            perms += 'x' if mode & stat.S_IXOTH else '-'
            
            return perms
        except FileNotFoundError:
            return '?' * 10
    
    @staticmethod
    def is_readable(path, by_owner=True):
        """Check if file is readable"""
        try:
            mode = os.stat(path).st_mode
            if by_owner:
                return bool(mode & stat.S_IRUSR)
            else:
                return bool(mode & stat.S_IROTH)
        except FileNotFoundError:
            return False
    
    @staticmethod
    def is_writable(path, by_owner=True):
        """Check if file is writable"""
        try:
            mode = os.stat(path).st_mode
            if by_owner:
                return bool(mode & stat.S_IWUSR)
            else:
                return bool(mode & stat.S_IWOTH)
        except FileNotFoundError:
            return False
    
    @staticmethod
    def is_executable(path, by_owner=True):
        """Check if file is executable"""
        try:
            mode = os.stat(path).st_mode
            if by_owner:
                return bool(mode & stat.S_IXUSR)
            else:
                return bool(mode & stat.S_IXOTH)
        except FileNotFoundError:
            return False
    
    @staticmethod
    def get_octal_permissions(path):
        """Get permissions as octal number"""
        try:
            mode = os.stat(path).st_mode
            return oct(mode & 0o777)[2:]
        except FileNotFoundError:
            return '000'

# Usage
checker = PermissionChecker()
# print(checker.get_permissions('file.txt'))
# print(checker.get_octal_permissions('file.txt'))
# print(checker.is_readable('file.txt'))
# print(checker.is_writable('file.txt'))
# print(checker.is_executable('script.py'))
```

---

## Real-World Examples

### Example 1: Directory Lister with Details

```python
import os
import stat
import time
from datetime import datetime

class DetailedDirectoryLister:
    @staticmethod
    def format_size(size):
        """Format file size in human-readable form"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f}{unit}"
            size /= 1024.0
        return f"{size:.1f}PB"
    
    @staticmethod
    def format_permissions(mode):
        """Format permissions as string"""
        perms = []
        
        # File type
        if stat.S_ISDIR(mode):
            perms.append('d')
        elif stat.S_ISLNK(mode):
            perms.append('l')
        else:
            perms.append('-')
        
        # Owner
        perms.append('r' if mode & stat.S_IRUSR else '-')
        perms.append('w' if mode & stat.S_IWUSR else '-')
        perms.append('x' if mode & stat.S_IXUSR else '-')
        
        # Group
        perms.append('r' if mode & stat.S_IRGRP else '-')
        perms.append('w' if mode & stat.S_IWGRP else '-')
        perms.append('x' if mode & stat.S_IXGRP else '-')
        
        # Others
        perms.append('r' if mode & stat.S_IROTH else '-')
        perms.append('w' if mode & stat.S_IWOTH else '-')
        perms.append('x' if mode & stat.S_IXOTH else '-')
        
        return ''.join(perms)
    
    @staticmethod
    def list_directory(path='.'):
        """List directory with detailed information"""
        print(f"{'Permissions':12} {'Size':>8} {'Modified':20} {'Name'}")
        print("-" * 70)
        
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            
            try:
                file_stat = os.stat(item_path)
                perms = DetailedDirectoryLister.format_permissions(file_stat.st_mode)
                size = DetailedDirectoryLister.format_size(file_stat.st_size)
                mtime = datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                
                # Add trailing slash for directories
                if stat.S_ISDIR(file_stat.st_mode):
                    item += '/'
                elif stat.S_ISLNK(file_stat.st_mode):
                    item += '@'
                
                print(f"{perms:12} {size:>8} {mtime:20} {item}")
            except (PermissionError, OSError):
                print(f"{'Permission denied':12} {'':>8} {'':20} {item}")

# Usage
# lister = DetailedDirectoryLister()
# lister.list_directory('.')
```

### Example 2: File Finder with Conditions

```python
import os
import stat

class FileFinder:
    def __init__(self, root_path='.'):
        self.root_path = root_path
        self.results = []
    
    def find_by_type(self, file_type='file'):
        """Find files by type"""
        self.results = []
        
        for root, dirs, files in os.walk(self.root_path):
            if file_type == 'file':
                for file in files:
                    self.results.append(os.path.join(root, file))
            elif file_type == 'dir':
                for dir_name in dirs:
                    self.results.append(os.path.join(root, dir_name))
        
        return self.results
    
    def find_by_permission(self, permission='read'):
        """Find files with specific permission"""
        self.results = []
        
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    mode = os.stat(file_path).st_mode
                    
                    if permission == 'read':
                        if mode & stat.S_IRUSR:
                            self.results.append(file_path)
                    elif permission == 'write':
                        if mode & stat.S_IWUSR:
                            self.results.append(file_path)
                    elif permission == 'execute':
                        if mode & stat.S_IXUSR:
                            self.results.append(file_path)
                except (PermissionError, OSError):
                    pass
        
        return self.results
    
    def find_by_size(self, min_size=0, max_size=float('inf')):
        """Find files by size range"""
        self.results = []
        
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path)
                    if min_size <= size <= max_size:
                        self.results.append((file_path, size))
                except (PermissionError, OSError):
                    pass
        
        return sorted(self.results, key=lambda x: x[1], reverse=True)
    
    def find_executables(self):
        """Find executable files"""
        return self.find_by_permission('execute')

# Usage
finder = FileFinder('/usr/bin')
# executables = finder.find_executables()
# print(f"Found {len(executables)} executables")
```

### Example 3: File Permission Modifier

```python
import os
import stat

class PermissionModifier:
    @staticmethod
    def add_read_permission(path, for_owner=True, for_group=False, for_others=False):
        """Add read permission"""
        current = os.stat(path).st_mode
        
        if for_owner:
            os.chmod(path, current | stat.S_IRUSR)
        if for_group:
            os.chmod(path, current | stat.S_IRGRP)
        if for_others:
            os.chmod(path, current | stat.S_IROTH)
    
    @staticmethod
    def add_write_permission(path, for_owner=True, for_group=False, for_others=False):
        """Add write permission"""
        current = os.stat(path).st_mode
        
        if for_owner:
            os.chmod(path, current | stat.S_IWUSR)
        if for_group:
            os.chmod(path, current | stat.S_IWGRP)
        if for_others:
            os.chmod(path, current | stat.S_IWOTH)
    
    @staticmethod
    def add_execute_permission(path, for_owner=True, for_group=False, for_others=False):
        """Add execute permission"""
        current = os.stat(path).st_mode
        
        if for_owner:
            os.chmod(path, current | stat.S_IXUSR)
        if for_group:
            os.chmod(path, current | stat.S_IXGRP)
        if for_others:
            os.chmod(path, current | stat.S_IXOTH)
    
    @staticmethod
    def remove_read_permission(path, for_owner=True, for_group=False, for_others=False):
        """Remove read permission"""
        current = os.stat(path).st_mode
        
        if for_owner:
            os.chmod(path, current & ~stat.S_IRUSR)
        if for_group:
            os.chmod(path, current & ~stat.S_IRGRP)
        if for_others:
            os.chmod(path, current & ~stat.S_IROTH)
    
    @staticmethod
    def set_permission_octal(path, octal_mode):
        """Set permission using octal mode (e.g., 0o755)"""
        os.chmod(path, octal_mode)
    
    @staticmethod
    def make_executable(path):
        """Make file executable (adds +x for owner)"""
        current = os.stat(path).st_mode
        os.chmod(path, current | stat.S_IXUSR)
    
    @staticmethod
    def make_readonly(path):
        """Make file read-only (remove write for owner)"""
        current = os.stat(path).st_mode
        os.chmod(path, current & ~stat.S_IWUSR)

# Usage
# PermissionModifier.make_executable('script.py')
# PermissionModifier.make_readonly('important.txt')
```

### Example 4: File Type Statistics

```python
import os
import stat
from collections import defaultdict

class FileTypeStats:
    def __init__(self, root_path='.'):
        self.root_path = root_path
        self.stats = defaultdict(int)
    
    def analyze(self):
        """Analyze file types in directory tree"""
        self.stats.clear()
        
        for root, dirs, files in os.walk(self.root_path):
            # Count directories
            for dir_name in dirs:
                self.stats['directories'] += 1
            
            # Count files by type
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    mode = os.stat(file_path).st_mode
                    
                    if stat.S_ISREG(mode):
                        self.stats['regular_files'] += 1
                        
                        # Count by extension
                        ext = os.path.splitext(file)[1].lower()
                        if ext:
                            self.stats[f'ext_{ext}'] += 1
                        else:
                            self.stats['no_extension'] += 1
                    
                    elif stat.S_ISLNK(mode):
                        self.stats['symlinks'] += 1
                    elif stat.S_ISCHR(mode):
                        self.stats['char_devices'] += 1
                    elif stat.S_ISBLK(mode):
                        self.stats['block_devices'] += 1
                    elif stat.S_ISFIFO(mode):
                        self.stats['fifos'] += 1
                    elif stat.S_ISSOCK(mode):
                        self.stats['sockets'] += 1
                except (PermissionError, OSError):
                    self.stats['permission_denied'] += 1
        
        return dict(self.stats)
    
    def print_report(self):
        """Print analysis report"""
        stats = self.analyze()
        
        print("FILE TYPE STATISTICS")
        print("=" * 40)
        
        categories = [
            ('directories', 'Directories'),
            ('regular_files', 'Regular files'),
            ('symlinks', 'Symbolic links'),
            ('char_devices', 'Character devices'),
            ('block_devices', 'Block devices'),
            ('fifos', 'FIFOs'),
            ('sockets', 'Sockets'),
            ('permission_denied', 'Permission denied'),
        ]
        
        for key, label in categories:
            if key in stats:
                print(f"{label}: {stats[key]}")
        
        # Show file extensions
        print("\nFile extensions:")
        ext_stats = {k: v for k, v in stats.items() if k.startswith('ext_')}
        for ext, count in sorted(ext_stats.items(), key=lambda x: x[1], reverse=True)[:10]:
            ext_name = ext[4:] if ext != 'no_extension' else '(no extension)'
            print(f"  {ext_name}: {count}")

# Usage
# stats = FileTypeStats('/home/user')
# stats.print_report()
```

---

## Practice Exercises

### Beginner Level

1. **Check File Type**
   ```python
   # Use stat to check if a path is a regular file or directory
   ```

2. **Check Read Permission**
   ```python
   # Check if file is readable by owner
   ```

3. **Get Octal Permissions**
   ```python
   # Get file permissions as octal number (e.g., 0o644)
   ```

### Intermediate Level

4. **Directory Lister**
   ```python
   # List directory with permissions and sizes
   ```

5. **File Finder**
   ```python
   # Find all executable files in directory tree
   ```

6. **Permission Modifier**
   ```python
   # Add or remove read/write/execute permissions
   ```

### Advanced Level

7. **File Type Statistics**
   ```python
   # Generate report of file types in directory tree
   ```

8. **Backup Script**
   ```python
   # Backup files with specific permissions
   ```

9. **Security Scanner**
   ```python
   # Find files with world-writable permissions
   ```

---

## Quick Reference Card

```python
import os
import stat

# Get file status
st = os.stat(path)          # Follows symlinks
st = os.lstat(path)         # Doesn't follow symlinks

# File type checking
stat.S_ISREG(st.st_mode)    # Regular file
stat.S_ISDIR(st.st_mode)    # Directory
stat.S_ISLNK(st.st_mode)    # Symbolic link
stat.S_ISCHR(st.st_mode)    # Character device
stat.S_ISBLK(st.st_mode)    # Block device
stat.S_ISFIFO(st.st_mode)   # FIFO
stat.S_ISSOCK(st.st_mode)   # Socket

# Owner permissions
st.st_mode & stat.S_IRUSR   # Owner read
st.st_mode & stat.S_IWUSR   # Owner write
st.st_mode & stat.S_IXUSR   # Owner execute

# Group permissions
st.st_mode & stat.S_IRGRP   # Group read
st.st_mode & stat.S_IWGRP   # Group write
st.st_mode & stat.S_IXGRP   # Group execute

# Others permissions
st.st_mode & stat.S_IROTH   # Others read
st.st_mode & stat.S_IWOTH   # Others write
st.st_mode & stat.S_IXOTH   # Others execute

# Special permissions
st.st_mode & stat.S_ISUID   # Set UID
st.st_mode & stat.S_ISGID   # Set GID
st.st_mode & stat.S_ISVTX   # Sticky bit

# Modify permissions
os.chmod(path, st.st_mode | stat.S_IXUSR)  # Add execute
os.chmod(path, st.st_mode & ~stat.S_IWUSR) # Remove write
os.chmod(path, 0o755)                      # Set exact permissions

# Common octal modes
0o400  # r--------
0o600  # rw-------
0o644  # rw-r--r--
0o700  # rwx------
0o750  # rwxr-x---
0o755  # rwxr-xr-x
0o777  # rwxrwxrwx
```

---

## Next Step

- Move to [06_signal.md](06_signal.md) to learn about signal handling.

---

*Master the stat module for detailed file information and permission management! 🐍✨*
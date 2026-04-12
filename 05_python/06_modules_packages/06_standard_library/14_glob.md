# 📘 GLOB MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Glob?](#what-is-glob)
2. [Pattern Syntax](#pattern-syntax)
3. [`glob.glob()` – Find Matching Paths](#globglob--find-matching-paths)
4. [`glob.iglob()` – Iterator Version](#globiglob--iterator-version)
5. [`glob.escape()` – Escape Special Characters](#globescape--escape-special-characters)
6. [Real-World Examples](#real-world-examples)
7. [Practice Exercises](#practice-exercises)

---

## What is Glob?

The `glob` module finds all pathnames matching a specified pattern according to Unix shell rules. It's useful for finding files matching patterns like `*.py`, `data*.csv`, etc.

```python
import glob

# Find all Python files
py_files = glob.glob('*.py')
print(py_files)  # ['script1.py', 'script2.py', 'utils.py']

# Find all text files in subdirectories
txt_files = glob.glob('**/*.txt', recursive=True)
print(txt_files)  # ['docs/readme.txt', 'data/notes.txt']
```

**Key Characteristics:**
- ✅ Uses Unix shell-style pattern matching
- ✅ Returns results as list of strings
- ✅ Works on Windows, Linux, Mac
- ✅ Supports recursive search
- ✅ Handles wildcards and character ranges

---

## Pattern Syntax

### Wildcards

| Pattern | Meaning | Example |
|---------|---------|---------|
| `*` | Matches any number of characters (including none) | `*.py` matches all Python files |
| `?` | Matches exactly one character | `?.txt` matches `a.txt`, `1.txt` |
| `[abc]` | Matches one character from the set | `[0-9].py` matches `1.py`, `2.py` |
| `[!abc]` | Matches one character NOT in the set | `[!0-9].txt` matches non-digit names |
| `**` | Matches any files/directories recursively | `**/*.py` finds all Python files |

### Pattern Examples

```python
import glob

# Match all files with .txt extension
txt_files = glob.glob('*.txt')
print(f"Text files: {txt_files}")

# Match files starting with 'data' and ending with .csv
data_files = glob.glob('data*.csv')
print(f"Data files: {data_files}")

# Match files with single character before extension
single_char = glob.glob('?.py')
print(f"Single char py files: {single_char}")

# Match files with numeric names
numeric = glob.glob('[0-9]*.txt')
print(f"Numeric files: {numeric}")

# Match files not starting with digit
non_numeric = glob.glob('[!0-9]*.txt')
print(f"Non-numeric files: {non_numeric}")

# Recursive search for all Python files
all_py = glob.glob('**/*.py', recursive=True)
print(f"All Python files: {all_py}")
```

---

## `glob.glob()` – Find Matching Paths

### Basic Usage

```python
import glob

# Get all files in current directory
all_files = glob.glob('*')
print(f"All files: {all_files}")

# Get only directories
dirs = [d for d in glob.glob('*/') if d.endswith('/')]
print(f"Directories: {dirs}")

# Get files with multiple extensions
py_and_txt = glob.glob('*.py') + glob.glob('*.txt')
print(f"Python and text files: {py_and_txt}")

# Using absolute paths
import os
abs_paths = glob.glob(os.path.join('/home/user', '*.py'))
print(f"Absolute paths: {abs_paths}")
```

### Recursive Search

```python
import glob

# Recursive search for all Python files
all_py = glob.glob('**/*.py', recursive=True)
print(f"All Python files: {all_py}")

# Recursive search for all files in subdirectories
all_files_recursive = glob.glob('**/*', recursive=True)
print(f"All files recursively: {all_files_recursive[:10]}...")  # First 10

# Find all README files anywhere
readme_files = glob.glob('**/README*', recursive=True)
print(f"README files: {readme_files}")

# Find all config files in subdirectories
config_files = glob.glob('**/config.*', recursive=True)
print(f"Config files: {config_files}")
```

### Root Directory Parameter

```python
import glob

# Using root_dir parameter (Python 3.10+)
# files = glob.glob('*.py', root_dir='/path/to/dir')

# Without root_dir (old way)
import os
os.chdir('/path/to/dir')
files = glob.glob('*.py')

# With root_dir (cleaner)
# files = glob.glob('*.py', root_dir='/path/to/dir')
```

---

## `glob.iglob()` – Iterator Version

`iglob()` returns an iterator instead of a list, which is more memory-efficient for large results.

```python
import glob

# Using iglob (memory efficient)
for file in glob.iglob('**/*.py', recursive=True):
    print(f"Found: {file}")
    if some_condition:
        break  # Can break early

# Compare memory usage
import sys

# glob() returns list (all at once)
list_result = glob.glob('**/*.py', recursive=True)
print(f"List size: {sys.getsizeof(list_result)} bytes")

# iglob() returns iterator (lazy)
iter_result = glob.iglob('**/*.py', recursive=True)
print(f"Iterator size: {sys.getsizeof(iter_result)} bytes")
```

---

## `glob.escape()` – Escape Special Characters

Escape special characters in a pathname so they are treated as literal characters.

```python
import glob

# Special characters that need escaping
special_path = '/path/with/[special]/chars/*.txt'

# Escape the path
escaped = glob.escape(special_path)
print(f"Original: {special_path}")
print(f"Escaped: {escaped}")

# Real use: Searching for files with brackets in name
# Create a file named 'file[1].txt'
# Without escaping: glob.glob('file[1].txt') won't work correctly
escaped_pattern = glob.escape('file[1].txt')
files = glob.glob(escaped_pattern)
print(f"Found: {files}")
```

---

## Real-World Examples

### Example 1: Batch File Processor

```python
import glob
import os
import shutil
from datetime import datetime

class BatchProcessor:
    def __init__(self, pattern, recursive=False):
        self.pattern = pattern
        self.recursive = recursive
        self.files = []
    
    def find_files(self):
        """Find files matching pattern"""
        self.files = glob.glob(self.pattern, recursive=self.recursive)
        return self.files
    
    def copy_files(self, destination):
        """Copy all matching files to destination"""
        copied = []
        for file in self.files:
            dest_path = os.path.join(destination, os.path.basename(file))
            shutil.copy2(file, dest_path)
            copied.append((file, dest_path))
        return copied
    
    def move_files(self, destination):
        """Move all matching files to destination"""
        moved = []
        for file in self.files:
            dest_path = os.path.join(destination, os.path.basename(file))
            shutil.move(file, dest_path)
            moved.append((file, dest_path))
        return moved
    
    def delete_files(self):
        """Delete all matching files"""
        deleted = []
        for file in self.files:
            os.remove(file)
            deleted.append(file)
        return deleted
    
    def add_timestamp(self, suffix_format='_%Y%m%d_%H%M%S'):
        """Add timestamp to filenames"""
        renamed = []
        timestamp = datetime.now().strftime(suffix_format)
        
        for file in self.files:
            dirname = os.path.dirname(file)
            basename = os.path.basename(file)
            name, ext = os.path.splitext(basename)
            new_name = f"{name}{timestamp}{ext}"
            new_path = os.path.join(dirname, new_name)
            os.rename(file, new_path)
            renamed.append((file, new_path))
        
        return renamed
    
    def process_by_extension(self, extension_handlers):
        """Process files based on extension"""
        results = {}
        
        for file in self.files:
            ext = os.path.splitext(file)[1].lower()
            if ext in extension_handlers:
                result = extension_handlers[ext](file)
                results[file] = result
        
        return results

# Usage
processor = BatchProcessor('*.txt')
files = processor.find_files()
print(f"Found {len(files)} text files")

# Add timestamp to files
# renamed = processor.add_timestamp()
# print(f"Renamed {len(renamed)} files")

# Process by extension
def process_py(file):
    print(f"Processing Python file: {file}")
    return 'processed'

def process_txt(file):
    print(f"Processing text file: {file}")
    return 'processed'

handlers = {'.py': process_py, '.txt': process_txt}
# results = processor.process_by_extension(handlers)
```

### Example 2: File Organizer by Extension

```python
import glob
import os
import shutil

class FileOrganizer:
    EXTENSION_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.md'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv'],
        'Presentations': ['.ppt', '.pptx'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
        'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
        'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv'],
        'Music': ['.mp3', '.wav', '.flac', '.aac'],
        'Executables': ['.exe', '.msi', '.app', '.dmg']
    }
    
    def __init__(self, directory='.'):
        self.directory = directory
        self.files = []
    
    def get_category(self, filename):
        """Get category for a file based on extension"""
        ext = os.path.splitext(filename)[1].lower()
        
        for category, extensions in self.EXTENSION_MAP.items():
            if ext in extensions:
                return category
        return 'Others'
    
    def scan_directory(self):
        """Scan directory for all files"""
        pattern = os.path.join(self.directory, '*')
        self.files = [f for f in glob.glob(pattern) if os.path.isfile(f)]
        return self.files
    
    def organize(self, dry_run=True):
        """Organize files into category folders"""
        if not self.files:
            self.scan_directory()
        
        organized = {}
        
        for file in self.files:
            category = self.get_category(file)
            organized.setdefault(category, []).append(file)
            
            if not dry_run:
                category_dir = os.path.join(self.directory, category)
                os.makedirs(category_dir, exist_ok=True)
                
                dest = os.path.join(category_dir, os.path.basename(file))
                shutil.move(file, dest)
        
        return organized
    
    def generate_report(self):
        """Generate organization report"""
        if not self.files:
            self.scan_directory()
        
        report = {}
        for file in self.files:
            category = self.get_category(file)
            report.setdefault(category, []).append(file)
        
        print("FILE ORGANIZATION REPORT")
        print("=" * 50)
        print(f"Total files: {len(self.files)}")
        
        for category, files in sorted(report.items()):
            print(f"\n{category} ({len(files)} files):")
            for file in files[:5]:
                print(f"  {os.path.basename(file)}")
            if len(files) > 5:
                print(f"  ... and {len(files) - 5} more")
        
        return report

# Usage
organizer = FileOrganizer('.')
organizer.generate_report()
# organizer.organize(dry_run=False)
```

### Example 3: Backup Script

```python
import glob
import os
import shutil
import zipfile
from datetime import datetime

class BackupManager:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    def get_files_to_backup(self, patterns):
        """Get files matching patterns"""
        files_to_backup = []
        
        for pattern in patterns:
            search_pattern = os.path.join(self.source_dir, pattern)
            files = glob.glob(search_pattern, recursive=True)
            files_to_backup.extend(files)
        
        return files_to_backup
    
    def create_zip_backup(self, files, include_timestamp=True):
        """Create ZIP backup of files"""
        backup_filename = self.backup_name
        if include_timestamp:
            backup_filename = f"{self.backup_name}.zip"
        else:
            backup_filename = "backup.zip"
        
        backup_path = os.path.join(self.backup_dir, backup_filename)
        os.makedirs(self.backup_dir, exist_ok=True)
        
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                arcname = os.path.relpath(file, self.source_dir)
                zipf.write(file, arcname)
        
        return backup_path
    
    def create_copy_backup(self, files):
        """Create copy backup (preserve structure)"""
        backup_path = os.path.join(self.backup_dir, self.backup_name)
        os.makedirs(backup_path, exist_ok=True)
        
        copied_files = []
        for file in files:
            rel_path = os.path.relpath(file, self.source_dir)
            dest_path = os.path.join(backup_path, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(file, dest_path)
            copied_files.append((file, dest_path))
        
        return copied_files
    
    def incremental_backup(self, last_backup_time):
        """Backup files modified since last backup"""
        files = []
        
        for root, dirs, files_in_dir in os.walk(self.source_dir):
            for file in files_in_dir:
                filepath = os.path.join(root, file)
                mtime = os.path.getmtime(filepath)
                if mtime > last_backup_time:
                    files.append(filepath)
        
        return self.create_copy_backup(files)
    
    def clean_old_backups(self, keep_count=5):
        """Delete old backups, keep only recent N"""
        backup_files = glob.glob(os.path.join(self.backup_dir, 'backup_*'))
        backup_files.sort(key=os.path.getmtime, reverse=True)
        
        deleted = []
        for old_backup in backup_files[keep_count:]:
            if os.path.isdir(old_backup):
                shutil.rmtree(old_backup)
            else:
                os.remove(old_backup)
            deleted.append(old_backup)
        
        return deleted

# Usage
backup = BackupManager('/path/to/source', '/path/to/backup')

# Backup specific patterns
patterns = ['*.py', '*.txt', 'data/*.csv']
files = backup.get_files_to_backup(patterns)
print(f"Found {len(files)} files to backup")

# Create ZIP backup
# zip_path = backup.create_zip_backup(files)
# print(f"Backup created: {zip_path}")

# Clean old backups
# deleted = backup.clean_old_backups(keep_count=5)
# print(f"Deleted {len(deleted)} old backups")
```

### Example 4: Log File Analyzer

```python
import glob
import os
import re
from datetime import datetime
from collections import defaultdict

class LogAnalyzer:
    def __init__(self, log_pattern, date_pattern='*'):
        self.log_pattern = log_pattern
        self.date_pattern = date_pattern
        self.log_files = []
    
    def find_log_files(self):
        """Find log files matching pattern"""
        pattern = f"{self.log_pattern}{self.date_pattern}"
        self.log_files = glob.glob(pattern)
        return self.log_files
    
    def parse_log_line(self, line):
        """Parse a log line (customize based on log format)"""
        # Example: 2024-01-15 10:30:45 [ERROR] Message
        pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)'
        match = re.match(pattern, line)
        
        if match:
            return {
                'date': match.group(1),
                'time': match.group(2),
                'level': match.group(3),
                'message': match.group(4)
            }
        return None
    
    def analyze_all_logs(self):
        """Analyze all log files"""
        self.find_log_files()
        
        stats = {
            'total_entries': 0,
            'by_level': defaultdict(int),
            'by_date': defaultdict(int),
            'by_hour': defaultdict(int),
            'errors': []
        }
        
        for log_file in self.log_files:
            with open(log_file, 'r') as f:
                for line in f:
                    parsed = self.parse_log_line(line)
                    if parsed:
                        stats['total_entries'] += 1
                        stats['by_level'][parsed['level']] += 1
                        stats['by_date'][parsed['date']] += 1
                        stats['by_hour'][parsed['time'][:2]] += 1
                        
                        if parsed['level'] == 'ERROR':
                            stats['errors'].append({
                                'file': log_file,
                                'line': line.strip(),
                                'timestamp': f"{parsed['date']} {parsed['time']}"
                            })
        
        return stats
    
    def generate_report(self, stats):
        """Generate analysis report"""
        print("LOG ANALYSIS REPORT")
        print("=" * 60)
        print(f"Log files analyzed: {len(self.log_files)}")
        print(f"Total entries: {stats['total_entries']}")
        
        print("\nLOG LEVELS:")
        for level, count in sorted(stats['by_level'].items()):
            percentage = count / stats['total_entries'] * 100
            bar = '█' * int(percentage / 2)
            print(f"  {level}: {count} ({percentage:.1f}%) {bar}")
        
        print("\nTOP ERROR MESSAGES:")
        error_messages = defaultdict(int)
        for error in stats['errors']:
            error_messages[error['line'][:100]] += 1
        
        for msg, count in sorted(error_messages.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {count}x: {msg[:80]}...")
        
        print("\nACTIVITY BY HOUR:")
        for hour in sorted(stats['by_hour'].keys()):
            count = stats['by_hour'][hour]
            bar = '█' * int(count / max(stats['by_hour'].values()) * 20)
            print(f"  {hour}:00 - {count:4} entries {bar}")

# Usage
analyzer = LogAnalyzer('app.log', '*.log')
# stats = analyzer.analyze_all_logs()
# analyzer.generate_report(stats)
```

### Example 5: Image Resizer (Batch Processing)

```python
import glob
import os
from PIL import Image  # Requires: pip install Pillow

class ImageProcessor:
    def __init__(self, pattern='*.jpg'):
        self.pattern = pattern
        self.images = []
    
    def find_images(self, recursive=False):
        """Find all images matching pattern"""
        self.images = glob.glob(self.pattern, recursive=recursive)
        return self.images
    
    def resize_images(self, size, output_dir='resized', suffix='_resized'):
        """Resize all images to specified size"""
        os.makedirs(output_dir, exist_ok=True)
        results = []
        
        for img_path in self.images:
            try:
                img = Image.open(img_path)
                img.thumbnail(size)
                
                name, ext = os.path.splitext(os.path.basename(img_path))
                output_path = os.path.join(output_dir, f"{name}{suffix}{ext}")
                
                img.save(output_path)
                results.append((img_path, output_path))
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
        
        return results
    
    def convert_format(self, target_format='png', output_dir='converted'):
        """Convert images to different format"""
        os.makedirs(output_dir, exist_ok=True)
        results = []
        
        for img_path in self.images:
            try:
                img = Image.open(img_path)
                name = os.path.splitext(os.path.basename(img_path))[0]
                output_path = os.path.join(output_dir, f"{name}.{target_format}")
                
                img.save(output_path, target_format.upper())
                results.append((img_path, output_path))
            except Exception as e:
                print(f"Error converting {img_path}: {e}")
        
        return results
    
    def create_contact_sheet(self, output_file='contact_sheet.jpg', cols=4):
        """Create contact sheet of all images"""
        if not self.images:
            return
        
        images = []
        for img_path in self.images:
            try:
                img = Image.open(img_path)
                img.thumbnail((200, 200))
                images.append(img)
            except Exception as e:
                print(f"Error loading {img_path}: {e}")
        
        if not images:
            return
        
        rows = (len(images) + cols - 1) // cols
        sheet_width = cols * 210
        sheet_height = rows * 210
        
        contact_sheet = Image.new('RGB', (sheet_width, sheet_height), color='white')
        
        for i, img in enumerate(images):
            row = i // cols
            col = i % cols
            x = col * 210
            y = row * 210
            contact_sheet.paste(img, (x, y))
        
        contact_sheet.save(output_file)
        print(f"Contact sheet saved: {output_file}")

# Usage
processor = ImageProcessor('*.jpg')
images = processor.find_images()
print(f"Found {len(images)} images")

# Resize images
# processor.resize_images((800, 600), output_dir='thumbnails')

# Convert to PNG
# processor.convert_format('png', output_dir='png_files')

# Create contact sheet
# processor.create_contact_sheet('my_photos.jpg', cols=3)
```

---

## Practice Exercises

### Beginner Level

1. **List Python Files**
   ```python
   # Use glob to list all .py files in current directory
   ```

2. **Count Files by Extension**
   ```python
   # Count number of .txt, .csv, .json files
   ```

3. **Find Specific Pattern**
   ```python
   # Find all files starting with 'data' and ending with '.csv'
   ```

### Intermediate Level

4. **Recursive Search**
   ```python
   # Find all .log files in subdirectories
   ```

5. **File Organizer**
   ```python
   # Organize files by extension into folders
   ```

6. **Batch Rename**
   ```python
   # Add prefix to all matching files
   ```

### Advanced Level

7. **Backup Script**
   ```python
   # Backup files matching patterns to ZIP archive
   ```

8. **Log Analyzer**
   ```python
   # Analyze multiple log files matching pattern
   ```

9. **Image Processor**
   ```python
   # Batch resize/convert images matching pattern
   ```

---

## Quick Reference Card

```python
import glob

# Basic patterns
glob.glob('*.py')                       # All Python files
glob.glob('data*.csv')                  # Files starting with 'data'
glob.glob('?.txt')                      # Single character names
glob.glob('[0-9]*.py')                  # Files starting with digit
glob.glob('[!0-9]*.py')                 # Files NOT starting with digit

# Recursive
glob.glob('**/*.py', recursive=True)    # All Python files recursively
glob.glob('**/*', recursive=True)       # All files recursively

# Multiple patterns
files = glob.glob('*.py') + glob.glob('*.txt')

# With root_dir (Python 3.10+)
glob.glob('*.py', root_dir='/path/to/dir')

# Iterator (memory efficient)
for file in glob.iglob('**/*.py', recursive=True):
    process(file)

# Escape special characters
pattern = glob.escape('file[1].txt')
files = glob.glob(pattern)

# Combine with os.path
import os
all_files = glob.glob(os.path.join('data', '*.csv'))

# Filter results
dirs = [d for d in glob.glob('*/') if d.endswith('/')]
files = [f for f in glob.glob('*') if os.path.isfile(f)]
```

---

## Next Step

- Move to [15_shutil.md](15_shutil.md) to learn about high-level file operations.

---

*Master glob for powerful file pattern matching and batch processing! 🐍✨*
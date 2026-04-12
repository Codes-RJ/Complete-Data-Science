# 📘 TEMPFILE MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Tempfile?](#what-is-tempfile)
2. [Temporary Files](#temporary-files)
3. [Named Temporary Files](#named-temporary-files)
4. [Temporary Directories](#temporary-directories)
5. [Temporary File Security](#temporary-file-security)
6. [Real-World Examples](#real-world-examples)
7. [Practice Exercises](#practice-exercises)

---

## What is Tempfile?

The `tempfile` module creates temporary files and directories for temporary data storage. These files are automatically deleted when closed or when the program ends.

```python
import tempfile

# Create a temporary file
with tempfile.TemporaryFile() as temp_file:
    temp_file.write(b'Hello World')
    temp_file.seek(0)
    data = temp_file.read()
    print(data)  # b'Hello World'
# File is automatically deleted here

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temp directory: {temp_dir}")
    # Use the directory...
# Directory is automatically deleted here
```

**Key Characteristics:**
- ✅ Files are automatically deleted
- ✅ Secure (random names, restricted permissions)
- ✅ Cross-platform compatible
- ✅ Memory-efficient (can use memory instead of disk)
- ✅ Essential for testing and temporary data processing

---

## Temporary Files

### `tempfile.TemporaryFile()` – Anonymous Temporary File

```python
import tempfile

# Create anonymous temporary file
with tempfile.TemporaryFile() as temp_file:
    # Write data
    temp_file.write(b'Some temporary data')
    temp_file.write(b'More data')
    
    # Read back (seek to beginning)
    temp_file.seek(0)
    data = temp_file.read()
    print(data)  # b'Some temporary dataMore data'
    
    # File is automatically deleted after with block

# Without context manager (must close manually)
temp_file = tempfile.TemporaryFile()
temp_file.write(b'data')
temp_file.close()  # File deleted
```

### `tempfile.TemporaryFile()` with Text Mode

```python
import tempfile

# Text mode (default is binary)
with tempfile.TemporaryFile(mode='w+') as temp_file:
    temp_file.write('Hello World')
    temp_file.seek(0)
    content = temp_file.read()
    print(content)  # Hello World

# Specify encoding
with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as temp_file:
    temp_file.write('Unicode text: 你好')
    temp_file.seek(0)
    print(temp_file.read())
```

### `tempfile.SpooledTemporaryFile()` – Memory-Based Temporary File

```python
import tempfile

# SpooledTemporaryFile keeps data in memory until size limit
with tempfile.SpooledTemporaryFile(max_size=1024) as temp_file:
    temp_file.write(b'Small data')  # Stays in memory
    temp_file.seek(0)
    print(temp_file.read())  # b'Small data'
    
    # When data exceeds max_size, it's written to disk
    temp_file.write(b'X' * 2000)  # Exceeds 1024, now on disk

# Check if data is still in memory
with tempfile.SpooledTemporaryFile(max_size=1024) as temp_file:
    temp_file.write(b'Small')
    print(f"In memory: {temp_file._rolled}")  # False
    
    temp_file.write(b'X' * 2000)
    print(f"In memory: {temp_file._rolled}")  # True (rolled to disk)
```

---

## Named Temporary Files

### `tempfile.NamedTemporaryFile()` – Temporary File with Name

```python
import tempfile
import os

# Create named temporary file
with tempfile.NamedTemporaryFile() as temp_file:
    print(f"File name: {temp_file.name}")
    temp_file.write(b'Hello')
    temp_file.seek(0)
    
    # Can access the file by name from other processes
    print(f"File exists: {os.path.exists(temp_file.name)}")  # True
    
    # File is deleted after with block

# Keep file after close (delete=False)
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b'Data to keep')
    temp_file_name = temp_file.name

print(f"File still exists: {os.path.exists(temp_file_name)}")  # True

# Manually delete when done
os.remove(temp_file_name)
```

### Custom Suffix and Prefix

```python
import tempfile

# Custom prefix and suffix
with tempfile.NamedTemporaryFile(prefix='myprefix_', suffix='.txt') as temp_file:
    print(f"File name: {temp_file.name}")
    # Example: /tmp/myprefix_xxxxxx.txt

# Custom directory
with tempfile.NamedTemporaryFile(dir='/custom/path') as temp_file:
    print(f"File name: {temp_file.name}")
```

---

## Temporary Directories

### `tempfile.TemporaryDirectory()` – Temporary Directory

```python
import tempfile
import os

# Create temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temp directory: {temp_dir}")
    
    # Create files in the directory
    file_path = os.path.join(temp_dir, 'test.txt')
    with open(file_path, 'w') as f:
        f.write('Hello')
    
    # Directory exists
    print(f"Directory exists: {os.path.exists(temp_dir)}")  # True
    
    # Directory and contents automatically deleted

# Without context manager
temp_dir = tempfile.TemporaryDirectory()
print(f"Temp directory: {temp_dir.name}")
temp_dir.cleanup()  # Manually delete

# Keep directory after cleanup
temp_dir = tempfile.TemporaryDirectory()
temp_dir_name = temp_dir.name
temp_dir.cleanup()
print(f"Deleted: {not os.path.exists(temp_dir_name)}")  # True
```

### Custom Temporary Directory Parameters

```python
import tempfile

# Custom prefix, suffix, and directory
with tempfile.TemporaryDirectory(prefix='myapp_', suffix='_temp', dir='/tmp') as temp_dir:
    print(f"Directory: {temp_dir}")
    # Example: /tmp/myapp_xxxxxx_temp

# Ignore cleanup errors (keep files for debugging)
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temp_dir:
    # Even if cleanup fails, no error raised
    pass
```

---

## Temporary File Security

### `tempfile.mkstemp()` – Low-Level Temporary File

```python
import tempfile
import os

# mkstemp returns (file_descriptor, path)
fd, path = tempfile.mkstemp()
print(f"File descriptor: {fd}")
print(f"File path: {path}")

# Use the file descriptor
with os.fdopen(fd, 'w') as f:
    f.write('Hello')

# Clean up
os.close(fd)  # Close descriptor
os.remove(path)  # Delete file

# With custom parameters
fd, path = tempfile.mkstemp(prefix='custom_', suffix='.log', text=True)
os.close(fd)
os.remove(path)
```

### `tempfile.mkdtemp()` – Low-Level Temporary Directory

```python
import tempfile
import os
import shutil

# Create temporary directory
temp_dir = tempfile.mkdtemp()
print(f"Temp directory: {temp_dir}")

# Use the directory
file_path = os.path.join(temp_dir, 'test.txt')
with open(file_path, 'w') as f:
    f.write('data')

# Clean up
shutil.rmtree(temp_dir)
```

### Security Features

```python
import tempfile
import os
import stat

# Temporary files are created with restricted permissions
with tempfile.NamedTemporaryFile() as temp_file:
    stat_info = os.stat(temp_file.name)
    print(f"Permissions: {oct(stat_info.st_mode)[-3:]}")  # 600 (rw-------)

# On Unix, files are only readable/writable by owner
# On Windows, appropriate restrictions apply

# Get temporary directory location
print(f"System temp dir: {tempfile.gettempdir()}")
print(f"Temp dir prefix: {tempfile.gettempprefix()}")
```

---

## Real-World Examples

### Example 1: Large Data Processing

```python
import tempfile
import csv
import random

class LargeDataProcessor:
    def __init__(self, chunk_size=10000):
        self.chunk_size = chunk_size
    
    def generate_data(self, num_records):
        """Generate large dataset using temporary file"""
        temp_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False)
        
        writer = csv.writer(temp_file)
        writer.writerow(['id', 'value', 'category'])
        
        for i in range(num_records):
            writer.writerow([
                i,
                random.randint(1, 1000),
                random.choice(['A', 'B', 'C'])
            ])
        
        temp_file.seek(0)
        return temp_file
    
    def process_in_chunks(self, temp_file):
        """Process data in chunks to save memory"""
        results = []
        
        reader = csv.DictReader(temp_file)
        chunk = []
        
        for row in reader:
            chunk.append(row)
            if len(chunk) >= self.chunk_size:
                results.extend(self.process_chunk(chunk))
                chunk = []
        
        if chunk:
            results.extend(self.process_chunk(chunk))
        
        return results
    
    def process_chunk(self, chunk):
        """Process a single chunk of data"""
        # Simulate processing
        processed = []
        for row in chunk:
            row['value'] = int(row['value']) * 2
            processed.append(row)
        return processed
    
    def cleanup(self, temp_file):
        """Clean up temporary file"""
        temp_file.close()
        import os
        os.remove(temp_file.name)

# Usage
processor = LargeDataProcessor(chunk_size=1000)
temp_file = processor.generate_data(50000)
results = processor.process_in_chunks(temp_file)
print(f"Processed {len(results)} records")
processor.cleanup(temp_file)
```

### Example 2: File Downloader with Temporary Storage

```python
import tempfile
import requests
import os
import shutil

class DownloadManager:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def download_file(self, url):
        """Download file to temporary location"""
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(
            dir=self.temp_dir,
            suffix=os.path.splitext(url)[1],
            delete=False
        )
        
        # Download to temporary file
        response = requests.get(url, stream=True)
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                temp_file.write(chunk)
        
        temp_file.close()
        return temp_file.name
    
    def process_file(self, file_path):
        """Process downloaded file"""
        print(f"Processing: {file_path}")
        # Simulate processing
        with open(file_path, 'rb') as f:
            data = f.read(100)
            print(f"First 100 bytes: {data[:50]}...")
        return True
    
    def save_permanently(self, temp_path, dest_path):
        """Save temporary file permanently"""
        shutil.copy2(temp_path, dest_path)
        print(f"Saved to: {dest_path}")
    
    def cleanup(self):
        """Delete all temporary files and directory"""
        shutil.rmtree(self.temp_dir)
        print(f"Cleaned up: {self.temp_dir}")

# Usage
downloader = DownloadManager()
# url = "https://example.com/file.pdf"
# temp_file = downloader.download_file(url)
# downloader.process_file(temp_file)
# downloader.save_permanently(temp_file, '/path/to/save/file.pdf')
# downloader.cleanup()
```

### Example 3: Unit Testing with Temporary Files

```python
import tempfile
import unittest
import json
import os

class DataProcessor:
    def process(self, input_file, output_file):
        """Process data from input to output"""
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Process data
        result = [x * 2 for x in data['numbers']]
        
        with open(output_file, 'w') as f:
            json.dump({'result': result}, f)

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """Create temporary directory for test files"""
        self.test_dir = tempfile.TemporaryDirectory()
        self.processor = DataProcessor()
    
    def tearDown(self):
        """Clean up temporary files"""
        self.test_dir.cleanup()
    
    def create_test_file(self, filename, content):
        """Helper to create test file in temp directory"""
        file_path = os.path.join(self.test_dir.name, filename)
        with open(file_path, 'w') as f:
            json.dump(content, f)
        return file_path
    
    def test_process(self):
        # Create input file
        input_data = {'numbers': [1, 2, 3, 4, 5]}
        input_file = self.create_test_file('input.json', input_data)
        
        # Output file path
        output_file = os.path.join(self.test_dir.name, 'output.json')
        
        # Process
        self.processor.process(input_file, output_file)
        
        # Verify output
        with open(output_file, 'r') as f:
            output_data = json.load(f)
        
        self.assertEqual(output_data['result'], [2, 4, 6, 8, 10])
    
    def test_empty_input(self):
        # Test with empty list
        input_data = {'numbers': []}
        input_file = self.create_test_file('empty.json', input_data)
        output_file = os.path.join(self.test_dir.name, 'empty_output.json')
        
        self.processor.process(input_file, output_file)
        
        with open(output_file, 'r') as f:
            output_data = json.load(f)
        
        self.assertEqual(output_data['result'], [])

# Run tests
# unittest.main()
```

### Example 4: Image Processing with Temporary Files

```python
import tempfile
import os
from PIL import Image, ImageFilter

class ImageProcessor:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def load_image(self, image_path):
        """Load image to temporary file"""
        img = Image.open(image_path)
        temp_path = os.path.join(self.temp_dir, 'original.png')
        img.save(temp_path)
        return temp_path
    
    def apply_filter(self, image_path, filter_type='blur'):
        """Apply filter and save to new temporary file"""
        img = Image.open(image_path)
        
        if filter_type == 'blur':
            filtered = img.filter(ImageFilter.BLUR)
        elif filter_type == 'sharpen':
            filtered = img.filter(ImageFilter.SHARPEN)
        elif filter_type == 'contour':
            filtered = img.filter(ImageFilter.CONTOUR)
        else:
            filtered = img
        
        temp_path = os.path.join(self.temp_dir, f'filtered_{filter_type}.png')
        filtered.save(temp_path)
        return temp_path
    
    def resize_image(self, image_path, size=(800, 600)):
        """Resize image and save to temporary file"""
        img = Image.open(image_path)
        img.thumbnail(size)
        
        temp_path = os.path.join(self.temp_dir, 'resized.png')
        img.save(temp_path)
        return temp_path
    
    def convert_format(self, image_path, target_format='JPEG'):
        """Convert image format"""
        img = Image.open(image_path)
        temp_path = os.path.join(self.temp_dir, f'converted.{target_format.lower()}')
        img.save(temp_path, format=target_format)
        return temp_path
    
    def cleanup(self):
        """Delete all temporary files"""
        import shutil
        shutil.rmtree(self.temp_dir)
        print(f"Cleaned up: {self.temp_dir}")

# Usage
processor = ImageProcessor()
# temp_original = processor.load_image('photo.jpg')
# temp_filtered = processor.apply_filter(temp_original, 'blur')
# temp_resized = processor.resize_image(temp_filtered, (400, 300))
# processor.cleanup()
```

### Example 5: Log Rotator with Temporary Storage

```python
import tempfile
import os
import time
import gzip
from datetime import datetime

class LogRotator:
    def __init__(self, log_dir, max_size_mb=10):
        self.log_dir = log_dir
        self.max_size = max_size_mb * 1024 * 1024
        self.temp_dir = tempfile.mkdtemp()
    
    def rotate_log(self, log_file):
        """Rotate log file if too large"""
        if not os.path.exists(log_file):
            return False
        
        if os.path.getsize(log_file) < self.max_size:
            return False
        
        # Create timestamped archive name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        archive_name = f"{os.path.basename(log_file)}.{timestamp}.gz"
        archive_path = os.path.join(self.log_dir, archive_name)
        
        # Use temporary file for compression
        temp_archive = os.path.join(self.temp_dir, archive_name)
        
        # Compress log file to temporary location
        with open(log_file, 'rb') as f_in:
            with gzip.open(temp_archive, 'wb') as f_out:
                f_out.writelines(f_in)
        
        # Move to final location
        os.rename(temp_archive, archive_path)
        
        # Clear original log file
        open(log_file, 'w').close()
        
        print(f"Rotated: {log_file} -> {archive_path}")
        return True
    
    def rotate_all_logs(self):
        """Rotate all log files in directory"""
        rotated = []
        for file in os.listdir(self.log_dir):
            if file.endswith('.log'):
                log_path = os.path.join(self.log_dir, file)
                if self.rotate_log(log_path):
                    rotated.append(log_path)
        return rotated
    
    def cleanup(self):
        """Clean up temporary directory"""
        import shutil
        shutil.rmtree(self.temp_dir)
        print(f"Cleaned up: {self.temp_dir}")

# Usage
rotator = LogRotator('/var/log/myapp', max_size_mb=5)
# rotated = rotator.rotate_all_logs()
# rotator.cleanup()
```

---

## Practice Exercises

### Beginner Level

1. **Create Temporary File**
   ```python
   # Create a temporary file and write data to it
   ```

2. **Read from Temporary File**
   ```python
   # Write data to temporary file and read it back
   ```

3. **Temporary Directory**
   ```python
   # Create a temporary directory and create a file inside it
   ```

### Intermediate Level

4. **Named Temporary File**
   ```python
   # Create named temporary file with custom prefix
   ```

5. **Spooled Temporary File**
   ```python
   # Use SpooledTemporaryFile for memory-efficient storage
   ```

6. **Test with Temp Files**
   ```python
   # Write unit tests using temporary files
   ```

### Advanced Level

7. **Large Data Processor**
   ```python
   # Process large dataset using temporary files for chunking
   ```

8. **Download Manager**
   ```python
   # Download files to temporary location before processing
   ```

9. **Log Rotator**
   ```python
   # Implement log rotation using temporary files
   ```

---

## Quick Reference Card

```python
import tempfile

# Temporary files
with tempfile.TemporaryFile() as f:
    f.write(b'data')
    f.seek(0)
    data = f.read()

# Named temporary files
with tempfile.NamedTemporaryFile() as f:
    print(f.name)
    f.write(b'data')

# Keep after close
with tempfile.NamedTemporaryFile(delete=False) as f:
    f.write(b'data')
    name = f.name

# Spooled (memory then disk)
with tempfile.SpooledTemporaryFile(max_size=1024) as f:
    f.write(b'data')

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(temp_dir)

# Low-level
fd, path = tempfile.mkstemp()  # File descriptor
os.close(fd)
os.remove(path)

temp_dir = tempfile.mkdtemp()   # Directory
shutil.rmtree(temp_dir)

# Configuration
tempfile.gettempdir()           # System temp directory
tempfile.gettempprefix()        # Temp file prefix

# Parameters
tempfile.NamedTemporaryFile(
    prefix='custom_',           # Prefix
    suffix='.txt',              # Suffix
    dir='/custom/path',         # Directory
    mode='w+',                  # Mode
    encoding='utf-8'            # Encoding
)
```

---

## Next Step

- Move to [17_subprocess.md](17_subprocess.md) to learn about running system commands.

---

*Master tempfile for secure temporary file and directory management! 🐍✨*
# 📘 SHUTIL MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Shutil?](#what-is-shutil)
2. [Copying Files and Directories](#copying-files-and-directories)
3. [Moving and Renaming](#moving-and-renaming)
4. [Deleting Directories](#deleting-directories)
5. [Archiving (Zip/Tar)](#archiving-zip-tar)
6. [Disk Usage Information](#disk-usage-information)
7. [Real-World Examples](#real-world-examples)
8. [Practice Exercises](#practice-exercises)

---

## What is Shutil?

The `shutil` (shell utility) module provides high-level operations for copying, moving, and removing files and directories.

```python
import shutil
import os

# Copy a file
shutil.copy('source.txt', 'destination.txt')

# Copy a directory
shutil.copytree('source_dir', 'destination_dir')

# Move a file
shutil.move('old.txt', 'new.txt')

# Remove a directory tree
shutil.rmtree('directory_to_delete')
```

**Key Characteristics:**
- ✅ High-level file operations
- ✅ Copies file permissions and metadata
- ✅ Handles directories recursively
- ✅ Creates archives (zip, tar)
- ✅ Platform independent

---

## Copying Files and Directories

### `shutil.copy(src, dst)` – Copy File (Content + Permissions)

```python
import shutil

# Copy file to new name
shutil.copy('source.txt', 'destination.txt')

# Copy file to directory
shutil.copy('source.txt', 'backup_folder/')

# Copy with metadata (permissions)
shutil.copy('script.py', 'script_backup.py')
```

### `shutil.copy2(src, dst)` – Copy File (Preserve Metadata)

```python
import shutil
import os
import time

# Create a file with metadata
with open('original.txt', 'w') as f:
    f.write('Hello World')

# copy2 preserves timestamps
shutil.copy2('original.txt', 'copy2.txt')

# Compare timestamps
print(f"Original modified: {os.path.getmtime('original.txt')}")
print(f"Copy2 modified: {os.path.getmtime('copy2.txt')}")  # Same

# copy (without 2) may not preserve timestamps
shutil.copy('original.txt', 'copy.txt')
print(f"Copy modified: {os.path.getmtime('copy.txt')}")  # Different
```

### `shutil.copyfile(src, dst)` – Copy File Content Only

```python
import shutil

# Copy only the content (no metadata)
shutil.copyfile('source.txt', 'destination.txt')

# Raises error if destination is a directory
# shutil.copyfile('source.txt', 'backup_folder/')  # IsADirectoryError
```

### `shutil.copyfileobj(fsrc, fdst, length=16384)` – Copy File Objects

```python
import shutil

# Copy between file objects
with open('source.txt', 'rb') as fsrc:
    with open('destination.txt', 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)

# Custom buffer size
with open('large_file.bin', 'rb') as fsrc:
    with open('large_copy.bin', 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst, length=65536)  # 64KB buffer
```

### `shutil.copymode(src, dst)` – Copy Permissions Only

```python
import shutil
import os
import stat

# Create files with different permissions
with open('source.txt', 'w') as f:
    f.write('source')
os.chmod('source.txt', 0o755)  # rwxr-xr-x

with open('dest.txt', 'w') as f:
    f.write('dest')
os.chmod('dest.txt', 0o644)    # rw-r--r--

# Copy permissions only
shutil.copymode('source.txt', 'dest.txt')
print(f"Dest permissions: {oct(os.stat('dest.txt').st_mode)[-3:]}")
```

### `shutil.copystat(src, dst)` – Copy Metadata Only

```python
import shutil
import os
import time

# Copy timestamps and permissions
shutil.copystat('source.txt', 'dest.txt')
```

### `shutil.copytree(src, dst, symlinks=False, ignore=None)` – Copy Directory

```python
import shutil

# Basic directory copy
shutil.copytree('source_dir', 'destination_dir')

# Copy with symlinks preserved
shutil.copytree('source_dir', 'dest_dir', symlinks=True)

# Copy ignoring certain files
def ignore_patterns(directory, files):
    return [f for f in files if f.endswith('.tmp')]

shutil.copytree('source_dir', 'dest_dir', ignore=ignore_patterns)

# Use built-in ignore patterns
shutil.copytree('source_dir', 'dest_dir', 
                ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))

# Copy with dirs_exist_ok (Python 3.8+)
# shutil.copytree('source_dir', 'dest_dir', dirs_exist_ok=True)
```

---

## Moving and Renaming

### `shutil.move(src, dst)` – Move File or Directory

```python
import shutil
import os

# Move file
shutil.move('old_name.txt', 'new_name.txt')

# Move file to directory
shutil.move('file.txt', 'backup_folder/')

# Move directory
shutil.move('old_folder', 'new_location/folder')

# Move and rename
shutil.move('data/file.csv', 'archive/data_2024.csv')
```

---

## Deleting Directories

### `shutil.rmtree(path, ignore_errors=False, onerror=None)` – Remove Directory Tree

```python
import shutil
import os

# Remove directory and all contents
shutil.rmtree('directory_to_delete')

# Ignore errors (continue even if some files can't be deleted)
shutil.rmtree('directory_to_delete', ignore_errors=True)

# Custom error handling
def handle_error(func, path, exc_info):
    print(f"Error deleting {path}: {exc_info[1]}")

shutil.rmtree('directory_to_delete', onerror=handle_error)

# Remove read-only files (force)
import stat
def remove_readonly(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree('readonly_dir', onerror=remove_readonly)
```

---

## Archiving (Zip/Tar)

### `shutil.make_archive(base_name, format, root_dir=None, base_dir=None)` – Create Archive

```python
import shutil

# Create ZIP archive
archive_path = shutil.make_archive('backup', 'zip', 'folder_to_backup')
print(f"Created: {archive_path}")

# Create TAR archive
archive_path = shutil.make_archive('backup', 'tar', 'folder_to_backup')
print(f"Created: {archive_path}")

# Create compressed TAR
archive_path = shutil.make_archive('backup', 'gztar', 'folder_to_backup')
print(f"Created: {archive_path}")

# With custom base directory
shutil.make_archive('backup', 'zip', root_dir='/path/to/root', base_dir='subfolder')

# Available formats
print(shutil.get_archive_formats())
# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), 
#  ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
```

### `shutil.unpack_archive(filename, extract_dir=None, format=None)` – Extract Archive

```python
import shutil

# Extract ZIP archive
shutil.unpack_archive('backup.zip', 'extracted_folder')

# Extract TAR archive
shutil.unpack_archive('backup.tar.gz', 'extracted_folder')

# Auto-detect format (default)
shutil.unpack_archive('archive.zip', 'output_dir')

# Specify format explicitly
shutil.unpack_archive('archive.zip', 'output_dir', format='zip')

# Get registered unpack formats
print(shutil.get_unpack_formats())
```

---

## Disk Usage Information

### `shutil.disk_usage(path)` – Get Disk Usage Statistics

```python
import shutil

# Get disk usage for current directory
usage = shutil.disk_usage('/')
print(f"Total: {usage.total / (1024**3):.2f} GB")
print(f"Used: {usage.used / (1024**3):.2f} GB")
print(f"Free: {usage.free / (1024**3):.2f} GB")
print(f"Usage: {usage.used / usage.total * 100:.1f}%")

# For specific path
usage = shutil.disk_usage('/home/user')
print(f"Free space: {usage.free / (1024**3):.2f} GB")
```

---

## Real-World Examples

### Example 1: Backup System

```python
import shutil
import os
import time
from datetime import datetime

class BackupSystem:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def full_backup(self):
        """Create full backup with timestamp"""
        backup_name = f"backup_{self.timestamp}"
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        print(f"Creating full backup: {backup_path}")
        shutil.copytree(self.source_dir, backup_path)
        
        # Create archive of backup
        archive_path = shutil.make_archive(
            backup_path, 'zip', self.source_dir
        )
        print(f"Archive created: {archive_path}")
        
        return backup_path
    
    def incremental_backup(self, last_backup_time):
        """Backup files modified since last backup"""
        backup_name = f"incremental_{self.timestamp}"
        backup_path = os.path.join(self.backup_dir, backup_name)
        os.makedirs(backup_path, exist_ok=True)
        
        copied = 0
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                src_path = os.path.join(root, file)
                if os.path.getmtime(src_path) > last_backup_time:
                    rel_path = os.path.relpath(src_path, self.source_dir)
                    dst_path = os.path.join(backup_path, rel_path)
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    shutil.copy2(src_path, dst_path)
                    copied += 1
        
        print(f"Incremental backup complete: {copied} files copied")
        return backup_path
    
    def clean_old_backups(self, keep_count=5):
        """Delete old backups, keep only recent N"""
        backups = []
        for item in os.listdir(self.backup_dir):
            item_path = os.path.join(self.backup_dir, item)
            if os.path.isdir(item_path) and item.startswith('backup_'):
                backups.append((item_path, os.path.getmtime(item_path)))
        
        backups.sort(key=lambda x: x[1], reverse=True)
        
        deleted = []
        for backup_path, _ in backups[keep_count:]:
            shutil.rmtree(backup_path)
            deleted.append(backup_path)
            print(f"Deleted old backup: {backup_path}")
        
        # Also delete old zip archives
        for zip_file in os.listdir(self.backup_dir):
            if zip_file.startswith('backup_') and zip_file.endswith('.zip'):
                zip_path = os.path.join(self.backup_dir, zip_file)
                if zip_path not in backups:
                    os.remove(zip_path)
                    deleted.append(zip_path)
        
        return deleted

# Usage
backup = BackupSystem('/path/to/source', '/path/to/backup')
# backup.full_backup()
# backup.clean_old_backups(keep_count=3)
```

### Example 2: File Synchronizer

```python
import shutil
import os
import hashlib
from datetime import datetime

class FileSync:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def get_file_hash(self, filepath):
        """Calculate MD5 hash of file"""
        hash_md5 = hashlib.md5()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def get_directory_state(self, directory):
        """Get state of directory (file paths and hashes)"""
        state = {}
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, directory)
                state[rel_path] = self.get_file_hash(filepath)
        return state
    
    def sync(self, dry_run=True):
        """Sync source to destination"""
        print(f"\nSyncing {self.source} -> {self.destination}")
        print("=" * 50)
        
        if not os.path.exists(self.destination):
            if not dry_run:
                os.makedirs(self.destination)
            print(f"Created destination directory")
        
        source_state = self.get_directory_state(self.source)
        dest_state = self.get_directory_state(self.destination)
        
        # Files to copy (new or modified)
        to_copy = []
        for rel_path, src_hash in source_state.items():
            if rel_path not in dest_state:
                to_copy.append(('NEW', rel_path))
            elif src_hash != dest_state[rel_path]:
                to_copy.append(('MODIFIED', rel_path))
        
        # Files to delete (exist in dest but not in source)
        to_delete = [rel_path for rel_path in dest_state if rel_path not in source_state]
        
        print(f"\nFiles to copy: {len(to_copy)}")
        for action, rel_path in to_copy[:10]:
            print(f"  {action}: {rel_path}")
        if len(to_copy) > 10:
            print(f"  ... and {len(to_copy) - 10} more")
        
        print(f"\nFiles to delete: {len(to_delete)}")
        for rel_path in to_delete[:10]:
            print(f"  DELETE: {rel_path}")
        if len(to_delete) > 10:
            print(f"  ... and {len(to_delete) - 10} more")
        
        if dry_run:
            print("\n[DRY RUN] No changes were made")
            return
        
        # Perform copy
        for action, rel_path in to_copy:
            src_path = os.path.join(self.source, rel_path)
            dst_path = os.path.join(self.destination, rel_path)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
        
        # Perform delete
        for rel_path in to_delete:
            dst_path = os.path.join(self.destination, rel_path)
            os.remove(dst_path)
        
        # Remove empty directories
        for root, dirs, files in os.walk(self.destination, topdown=False):
            if not files and not dirs and root != self.destination:
                os.rmdir(root)
        
        print(f"\nSync complete!")

# Usage
syncer = FileSync('/path/to/source', '/path/to/destination')
# syncer.sync(dry_run=True)  # Preview only
# syncer.sync(dry_run=False) # Actually sync
```

### Example 3: File Organizer with Archive

```python
import shutil
import os
import glob
from datetime import datetime

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.archive_dir = os.path.join(directory, 'archived')
    
    def archive_old_files(self, days_old=30):
        """Archive files older than specified days"""
        cutoff_time = datetime.now().timestamp() - (days_old * 86400)
        archived = []
        
        os.makedirs(self.archive_dir, exist_ok=True)
        
        for file in glob.glob(os.path.join(self.directory, '*')):
            if os.path.isfile(file) and os.path.getmtime(file) < cutoff_time:
                shutil.move(file, self.archive_dir)
                archived.append(file)
        
        print(f"Archived {len(archived)} files")
        return archived
    
    def create_archive_of_archived(self):
        """Create ZIP archive of archived files"""
        timestamp = datetime.now().strftime("%Y%m%d")
        archive_name = os.path.join(self.directory, f"archive_{timestamp}")
        
        archive_path = shutil.make_archive(archive_name, 'zip', self.archive_dir)
        print(f"Created archive: {archive_path}")
        
        # Optionally delete original archived files
        # shutil.rmtree(self.archive_dir)
        
        return archive_path
    
    def organize_by_extension(self):
        """Organize files by extension into folders"""
        files = [f for f in glob.glob(os.path.join(self.directory, '*')) 
                if os.path.isfile(f) and not f.startswith(self.archive_dir)]
        
        organized = {}
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if not ext:
                ext = 'no_extension'
            else:
                ext = ext[1:]  # Remove dot
            
            ext_dir = os.path.join(self.directory, ext)
            os.makedirs(ext_dir, exist_ok=True)
            
            dest = os.path.join(ext_dir, os.path.basename(file))
            shutil.move(file, dest)
            organized.setdefault(ext, []).append(file)
        
        print(f"Organized {len(files)} files into {len(organized)} categories")
        return organized
    
    def compress_directory(self, directory_name=None):
        """Compress a directory to ZIP"""
        if directory_name is None:
            directory_name = os.path.basename(self.directory)
        
        parent_dir = os.path.dirname(self.directory)
        archive_name = os.path.join(parent_dir, directory_name)
        
        archive_path = shutil.make_archive(archive_name, 'zip', self.directory)
        print(f"Compressed {self.directory} -> {archive_path}")
        return archive_path

# Usage
organizer = FileOrganizer('/path/to/directory')
# organizer.archive_old_files(days_old=30)
# organizer.create_archive_of_archived()
# organizer.organize_by_extension()
# organizer.compress_directory()
```

### Example 4: Deployment Script

```python
import shutil
import os
import tempfile
import zipfile

class DeploymentManager:
    def __init__(self, project_dir, deploy_dir):
        self.project_dir = project_dir
        self.deploy_dir = deploy_dir
        self.temp_dir = None
    
    def create_deployment_package(self, version):
        """Create deployment package"""
        # Create temp directory
        self.temp_dir = tempfile.mkdtemp()
        
        # Copy project files to temp
        temp_project = os.path.join(self.temp_dir, 'app')
        shutil.copytree(self.project_dir, temp_project, 
                       ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git', 'tests'))
        
        # Create version file
        with open(os.path.join(temp_project, 'version.txt'), 'w') as f:
            f.write(version)
        
        # Create archive
        archive_name = os.path.join(self.deploy_dir, f"app_v{version}")
        archive_path = shutil.make_archive(archive_name, 'zip', self.temp_dir)
        
        return archive_path
    
    def deploy(self, archive_path):
        """Deploy from archive"""
        # Backup current deployment
        if os.path.exists(self.deploy_dir):
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            backup_path = os.path.join(os.path.dirname(self.deploy_dir), backup_name)
            shutil.move(self.deploy_dir, backup_path)
            print(f"Backed up to: {backup_path}")
        
        # Extract new deployment
        os.makedirs(self.deploy_dir, exist_ok=True)
        shutil.unpack_archive(archive_path, self.deploy_dir)
        print(f"Deployed to: {self.deploy_dir}")
    
    def rollback(self, backup_path):
        """Rollback to previous version"""
        if os.path.exists(self.deploy_dir):
            shutil.rmtree(self.deploy_dir)
        shutil.copytree(backup_path, self.deploy_dir)
        print(f"Rolled back to: {backup_path}")
    
    def cleanup(self):
        """Clean up temporary files"""
        if self.temp_dir and os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            print(f"Cleaned up: {self.temp_dir}")

# Usage
deploy = DeploymentManager('/path/to/project', '/path/to/deploy')
# archive = deploy.create_deployment_package('1.0.0')
# deploy.deploy(archive)
# deploy.cleanup()
```

### Example 5: Disk Space Monitor

```python
import shutil
import os
import time
from datetime import datetime

class DiskMonitor:
    def __init__(self, paths, threshold_percent=90):
        self.paths = paths
        self.threshold = threshold_percent
        self.alerts = []
    
    def check_disk_usage(self):
        """Check disk usage for all paths"""
        results = []
        for path in self.paths:
            try:
                usage = shutil.disk_usage(path)
                percent = (usage.used / usage.total) * 100
                
                results.append({
                    'path': path,
                    'total_gb': usage.total / (1024**3),
                    'used_gb': usage.used / (1024**3),
                    'free_gb': usage.free / (1024**3),
                    'percent': percent,
                    'alert': percent >= self.threshold
                })
                
                if percent >= self.threshold:
                    self.alerts.append({
                        'timestamp': datetime.now(),
                        'path': path,
                        'percent': percent
                    })
            
            except Exception as e:
                print(f"Error checking {path}: {e}")
        
        return results
    
    def generate_report(self):
        """Generate disk usage report"""
        results = self.check_disk_usage()
        
        print("=" * 70)
        print(f"DISK USAGE REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        for result in results:
            status = "⚠️ ALERT" if result['alert'] else "✓ OK"
            print(f"\n{result['path']}:")
            print(f"  Total: {result['total_gb']:.2f} GB")
            print(f"  Used:  {result['used_gb']:.2f} GB")
            print(f"  Free:  {result['free_gb']:.2f} GB")
            print(f"  Usage: {result['percent']:.1f}% {status}")
            
            if result['alert']:
                bar_length = 50
                filled = int(bar_length * result['percent'] / 100)
                bar = '█' * filled + '░' * (bar_length - filled)
                print(f"  [{bar}]")
        
        if self.alerts:
            print(f"\n⚠️ ALERTS: {len(self.alerts)}")
            for alert in self.alerts[-5:]:
                print(f"  {alert['timestamp'].strftime('%H:%M:%S')}: {alert['path']} - {alert['percent']:.1f}%")
    
    def find_largest_directories(self, path, top_n=10):
        """Find largest directories"""
        sizes = []
        
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                try:
                    total_size = 0
                    for root, dirs, files in os.walk(item_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            total_size += os.path.getsize(file_path)
                    sizes.append((item, total_size))
                except (PermissionError, OSError):
                    pass
        
        sizes.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\nLARGEST DIRECTORIES IN {path}:")
        for name, size in sizes[:top_n]:
            size_gb = size / (1024**3)
            size_mb = size / (1024**2)
            if size_gb >= 1:
                print(f"  {name}: {size_gb:.2f} GB")
            else:
                print(f"  {name}: {size_mb:.2f} MB")
        
        return sizes

# Usage
monitor = DiskMonitor(['/', '/home', '/var'], threshold_percent=80)
monitor.generate_report()
# monitor.find_largest_directories('/home/user', top_n=10)
```

---

## Practice Exercises

### Beginner Level

1. **Copy File**
   ```python
   # Copy a file from one location to another
   ```

2. **Move File**
   ```python
   # Move a file to a different directory
   ```

3. **Delete Directory**
   ```python
   # Delete a directory and all its contents
   ```

### Intermediate Level

4. **Backup Script**
   ```python
   # Create backup of directory to ZIP file
   ```

5. **File Organizer**
   ```python
   # Organize files by extension into folders
   ```

6. **Disk Space Checker**
   ```python
   # Check available disk space and alert if low
   ```

### Advanced Level

7. **Synchronization Tool**
   ```python
   # Sync two directories (copy new/modified files)
   ```

8. **Deployment Script**
   ```python
   # Create deployment package with versioning
   ```

9. **Cleanup Utility**
   ```python
   # Delete old files and empty directories
   ```

---

## Quick Reference Card

```python
import shutil

# Copy files
shutil.copy(src, dst)               # Copy file (permissions)
shutil.copy2(src, dst)              # Copy file (metadata)
shutil.copyfile(src, dst)           # Copy file content only
shutil.copyfileobj(fsrc, fdst)      # Copy between file objects

# Copy directories
shutil.copytree(src, dst)           # Copy directory tree
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*.pyc'))

# Copy metadata
shutil.copymode(src, dst)           # Copy permissions
shutil.copystat(src, dst)           # Copy timestamps

# Move
shutil.move(src, dst)               # Move file or directory

# Delete
shutil.rmtree(path)                 # Delete directory tree
shutil.rmtree(path, ignore_errors=True)  # Ignore errors

# Archives
shutil.make_archive(base, format, root_dir)   # Create archive
shutil.unpack_archive(filename, extract_dir)  # Extract archive
shutil.get_archive_formats()                  # List formats
shutil.get_unpack_formats()                   # List unpack formats

# Disk usage
shutil.disk_usage(path)             # Get disk usage statistics

# Which
shutil.which(cmd)                   # Find executable in PATH
```

---

## Next Step

- Move to [16_tempfile.md](16_tempfile.md) to learn about temporary files and directories.

---

*Master shutil for efficient file and directory operations! 🐍✨*
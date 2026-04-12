# 📘 SUBPROCESS MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Subprocess?](#what-is-subprocess)
2. [`subprocess.run()` – Run Command](#subprocessrun--run-command)
3. [Capturing Output](#capturing-output)
4. [Error Handling](#error-handling)
5. [Input/Output Pipes](#inputoutput-pipes)
6. [`subprocess.Popen()` – Advanced Control](#subprocesspopen--advanced-control)
7. [Shell vs Executable](#shell-vs-executable)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What is Subprocess?

The `subprocess` module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It's the recommended way to run system commands from Python.

```python
import subprocess

# Run a command
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)

# Run with shell (not recommended)
result = subprocess.run('ls -la', shell=True, capture_output=True, text=True)
print(result.stdout)
```

**Key Characteristics:**
- ✅ Run any system command
- ✅ Capture stdout and stderr
- ✅ Handle return codes
- ✅ Provide input to commands
- ✅ Replace older `os.system()` and `os.popen()`

---

## `subprocess.run()` – Run Command

### Basic Usage

```python
import subprocess

# Run command, wait for completion
result = subprocess.run(['echo', 'Hello World'])
print(f"Return code: {result.returncode}")

# Command with arguments
result = subprocess.run(['ls', '-la', '/tmp'])

# With shell (use with caution)
result = subprocess.run('echo "Hello World"', shell=True)
```

### Checking Return Code

```python
import subprocess

# Successful command
result = subprocess.run(['true'])
print(f"Success return code: {result.returncode}")  # 0

# Failed command
result = subprocess.run(['false'])
print(f"Failed return code: {result.returncode}")   # 1

# Check without raising exception
if result.returncode == 0:
    print("Command succeeded")
else:
    print("Command failed")
```

---

## Capturing Output

### Capturing stdout and stderr

```python
import subprocess

# Capture stdout
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(f"STDOUT:\n{result.stdout}")
print(f"STDERR:\n{result.stderr}")

# Capture without text (returns bytes)
result = subprocess.run(['ls', '-la'], capture_output=True)
print(f"STDOUT (bytes): {result.stdout[:50]}...")

# Only capture specific streams
result = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
print(f"STDOUT: {result.stdout}")
```

### Using `check_output()` (Legacy)

```python
import subprocess

# Get output as string
output = subprocess.check_output(['echo', 'Hello'], text=True)
print(output)  # Hello

# With stderr capture
output = subprocess.check_output(['ls', '-la'], stderr=subprocess.STDOUT, text=True)
```

---

## Error Handling

### Automatic Exception on Error

```python
import subprocess

# check=True raises CalledProcessError on non-zero exit
try:
    result = subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with code: {e.returncode}")
    print(f"Command: {e.cmd}")

# With capture
try:
    result = subprocess.run(['ls', 'nonexistent'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"Error output: {e.stderr}")
```

### Custom Error Handling

```python
import subprocess

def run_command(cmd, capture=True, raise_on_error=False):
    """Run command with custom error handling"""
    try:
        result = subprocess.run(
            cmd,
            capture_output=capture,
            text=True,
            check=raise_on_error
        )
        return {'success': True, 'stdout': result.stdout, 'stderr': result.stderr}
    except subprocess.CalledProcessError as e:
        return {
            'success': False,
            'returncode': e.returncode,
            'stdout': e.stdout,
            'stderr': e.stderr
        }
    except FileNotFoundError:
        return {'success': False, 'error': f"Command not found: {cmd[0]}"}

# Usage
result = run_command(['ls', '-la'])
if result['success']:
    print(result['stdout'])
else:
    print(f"Error: {result.get('error', result.get('stderr'))}")
```

---

## Input/Output Pipes

### Providing Input to Command

```python
import subprocess

# Provide input via stdin
result = subprocess.run(
    ['grep', 'hello'],
    input='hello world\ngoodbye world',
    capture_output=True,
    text=True
)
print(result.stdout)  # hello world

# With file input
with open('input.txt', 'r') as f:
    result = subprocess.run(['wc', '-l'], stdin=f, capture_output=True, text=True)
    print(result.stdout)
```

### Chaining Commands (Pipes)

```python
import subprocess

# Method 1: Using shell pipe (not recommended)
result = subprocess.run('ls -la | grep .py', shell=True, capture_output=True, text=True)
print(result.stdout)

# Method 2: Using Popen (recommended)
p1 = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(['grep', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # Allow p1 to receive SIGPIPE
output = p2.communicate()[0]
print(output)

# Method 3: Using run with pipe (Python 3.7+)
# result = subprocess.run('ls -la | grep .py', shell=True, capture_output=True, text=True)
```

---

## `subprocess.Popen()` – Advanced Control

### Basic Popen Usage

```python
import subprocess
import time

# Start process without waiting
process = subprocess.Popen(['sleep', '5'])
print(f"Process started: PID {process.pid}")
time.sleep(2)
process.wait()  # Wait for completion
print(f"Process finished: {process.returncode}")

# Non-blocking check
process = subprocess.Popen(['sleep', '5'])
while process.poll() is None:
    print("Still running...")
    time.sleep(1)
print(f"Finished with code: {process.returncode}")
```

### Communicating with Process

```python
import subprocess

# Send data and get output
process = subprocess.Popen(
    ['grep', 'hello'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input='hello world\ngoodbye world')
print(f"Output: {stdout}")
print(f"Error: {stderr}")
print(f"Return code: {process.returncode}")
```

### Timeout Handling

```python
import subprocess

try:
    result = subprocess.run(
        ['sleep', '10'],
        timeout=3,
        capture_output=True,
        text=True
    )
except subprocess.TimeoutExpired as e:
    print(f"Command timed out after {e.timeout} seconds")
    print(f"Partial output: {e.stdout}")
```

---

## Shell vs Executable

### When to Use `shell=True`

```python
import subprocess

# ❌ Avoid shell=True when possible (security risk)
result = subprocess.run('ls -la', shell=True)

# ✅ Better: Use list of arguments
result = subprocess.run(['ls', '-la'])

# When shell features are needed (carefully)
result = subprocess.run('ls -la | grep .py', shell=True)  # Pipe requires shell

# With variables (dangerous if variable contains user input)
user_input = "file.txt"
result = subprocess.run(f'cat {user_input}', shell=True)  # Command injection risk!
```

### Security Considerations

```python
import subprocess
import shlex

# ❌ Dangerous - command injection
def delete_file_unsafe(filename):
    subprocess.run(f'rm {filename}', shell=True)
# delete_file_unsafe('test.txt; rm -rf /')  # Disaster!

# ✅ Safe - using list arguments
def delete_file_safe(filename):
    subprocess.run(['rm', filename])

# ✅ Safe - using shlex.quote()
def delete_file_quoted(filename):
    subprocess.run(f'rm {shlex.quote(filename)}', shell=True)
```

---

## Real-World Examples

### Example 1: System Information Gatherer

```python
import subprocess
import platform

class SystemInfo:
    @staticmethod
    def run_command(cmd):
        """Run command and return output"""
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"
    
    @staticmethod
    def get_os_info():
        """Get operating system information"""
        info = {}
        
        if platform.system() == 'Linux':
            info['os'] = SystemInfo.run_command(['lsb_release', '-ds'])
            info['kernel'] = SystemInfo.run_command(['uname', '-r'])
            info['hostname'] = SystemInfo.run_command(['hostname'])
        elif platform.system() == 'Darwin':  # macOS
            info['os'] = SystemInfo.run_command(['sw_vers', '-productName']) + ' ' + \
                        SystemInfo.run_command(['sw_vers', '-productVersion'])
            info['kernel'] = SystemInfo.run_command(['uname', '-r'])
            info['hostname'] = SystemInfo.run_command(['hostname'])
        elif platform.system() == 'Windows':
            info['os'] = platform.system() + ' ' + platform.release()
            info['hostname'] = platform.node()
        
        return info
    
    @staticmethod
    def get_cpu_info():
        """Get CPU information"""
        if platform.system() == 'Linux':
            output = SystemInfo.run_command(['nproc'])
            return {'cores': output}
        elif platform.system() == 'Darwin':
            output = SystemInfo.run_command(['sysctl', '-n', 'hw.ncpu'])
            return {'cores': output}
        return {'cores': 'Unknown'}
    
    @staticmethod
    def get_memory_info():
        """Get memory information"""
        if platform.system() == 'Linux':
            output = SystemInfo.run_command(['free', '-h'])
            lines = output.split('\n')
            if len(lines) > 1:
                mem_line = lines[1].split()
                return {
                    'total': mem_line[1],
                    'used': mem_line[2],
                    'free': mem_line[3]
                }
        return {'info': 'Memory info not available'}
    
    @staticmethod
    def get_disk_info():
        """Get disk information"""
        if platform.system() == 'Linux':
            output = SystemInfo.run_command(['df', '-h', '/'])
            lines = output.split('\n')
            if len(lines) > 1:
                disk_line = lines[1].split()
                return {
                    'size': disk_line[1],
                    'used': disk_line[2],
                    'available': disk_line[3],
                    'use_percent': disk_line[4]
                }
        return {'info': 'Disk info not available'}

# Usage
print("SYSTEM INFORMATION")
print("=" * 40)
print(f"OS: {SystemInfo.get_os_info()}")
print(f"CPU: {SystemInfo.get_cpu_info()}")
print(f"Memory: {SystemInfo.get_memory_info()}")
print(f"Disk: {SystemInfo.get_disk_info()}")
```

### Example 2: Git Automation

```python
import subprocess
import os

class GitAutomation:
    def __init__(self, repo_path='.'):
        self.repo_path = repo_path
    
    def run_git(self, *args):
        """Run git command"""
        cmd = ['git'] + list(args)
        result = subprocess.run(
            cmd,
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        return result
    
    def status(self):
        """Get git status"""
        result = self.run_git('status', '--porcelain')
        if result.stdout:
            changes = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    status = line[:2]
                    file = line[3:]
                    changes.append({'status': status, 'file': file})
            return changes
        return []
    
    def commit(self, message):
        """Commit changes"""
        result = self.run_git('commit', '-m', message)
        return result.returncode == 0, result.stdout, result.stderr
    
    def push(self, remote='origin', branch=None):
        """Push to remote"""
        if branch is None:
            branch = self.get_current_branch()
        result = self.run_git('push', remote, branch)
        return result.returncode == 0, result.stdout, result.stderr
    
    def pull(self, remote='origin', branch=None):
        """Pull from remote"""
        if branch is None:
            branch = self.get_current_branch()
        result = self.run_git('pull', remote, branch)
        return result.returncode == 0, result.stdout, result.stderr
    
    def get_current_branch(self):
        """Get current branch name"""
        result = self.run_git('rev-parse', '--abbrev-ref', 'HEAD')
        return result.stdout.strip()
    
    def log(self, n=10):
        """Get commit log"""
        result = self.run_git('log', f'-{n}', '--oneline')
        commits = []
        for line in result.stdout.strip().split('\n'):
            if line:
                parts = line.split(' ', 1)
                commits.append({'hash': parts[0], 'message': parts[1] if len(parts) > 1 else ''})
        return commits
    
    def diff(self, file=None):
        """Show diff"""
        if file:
            result = self.run_git('diff', file)
        else:
            result = self.run_git('diff')
        return result.stdout
    
    def add(self, *files):
        """Add files to staging"""
        result = self.run_git('add', *files)
        return result.returncode == 0

# Usage
git = GitAutomation('/path/to/repo')
print(f"Current branch: {git.get_current_branch()}")
print(f"Changes: {git.status()}")
print(f"Recent commits: {git.log(5)}")
```

### Example 3: Process Manager

```python
import subprocess
import psutil
import time
import signal

class ProcessManager:
    def __init__(self):
        self.processes = {}
    
    def start_process(self, name, cmd):
        """Start a new process"""
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.processes[name] = {
                'process': process,
                'cmd': cmd,
                'start_time': time.time()
            }
            print(f"Started {name} (PID: {process.pid})")
            return True
        except Exception as e:
            print(f"Failed to start {name}: {e}")
            return False
    
    def stop_process(self, name, timeout=10):
        """Stop a process gracefully"""
        if name not in self.processes:
            print(f"Process {name} not found")
            return False
        
        process_info = self.processes[name]
        process = process_info['process']
        
        # Try graceful termination
        process.terminate()
        
        try:
            process.wait(timeout=timeout)
            print(f"Stopped {name}")
        except subprocess.TimeoutExpired:
            # Force kill
            process.kill()
            process.wait()
            print(f"Force killed {name}")
        
        # Get output
        stdout, stderr = process.communicate()
        if stdout:
            print(f"Output from {name}:\n{stdout}")
        if stderr:
            print(f"Errors from {name}:\n{stderr}")
        
        del self.processes[name]
        return True
    
    def stop_all(self):
        """Stop all processes"""
        for name in list(self.processes.keys()):
            self.stop_process(name)
    
    def get_status(self, name):
        """Get process status"""
        if name not in self.processes:
            return None
        
        process = self.processes[name]['process']
        return {
            'running': process.poll() is None,
            'pid': process.pid,
            'cmd': self.processes[name]['cmd'],
            'uptime': time.time() - self.processes[name]['start_time']
        }
    
    def list_processes(self):
        """List all managed processes"""
        if not self.processes:
            print("No processes running")
            return
        
        print("\nMANAGED PROCESSES")
        print("=" * 50)
        for name, info in self.processes.items():
            status = "RUNNING" if info['process'].poll() is None else "STOPPED"
            uptime = time.time() - info['start_time']
            print(f"  {name}: {status} (PID: {info['process'].pid}, Uptime: {uptime:.0f}s)")
    
    def monitor_processes(self, interval=5):
        """Monitor processes continuously"""
        try:
            while True:
                self.list_processes()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped")

# Usage
pm = ProcessManager()
# pm.start_process('web_server', ['python', '-m', 'http.server', '8000'])
# pm.start_process('data_processor', ['python', 'processor.py'])
# pm.list_processes()
# time.sleep(10)
# pm.stop_process('web_server')
# pm.stop_all()
```

### Example 4: Backup Script with Compression

```python
import subprocess
import os
import glob
from datetime import datetime

class BackupScript:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def create_backup_tar(self):
        """Create tar.gz backup"""
        backup_name = f"backup_{self.timestamp}.tar.gz"
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        cmd = ['tar', '-czf', backup_path, '-C', self.source_dir, '.']
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Backup created: {backup_path}")
            return backup_path
        else:
            print(f"Backup failed: {result.stderr}")
            return None
    
    def create_backup_zip(self):
        """Create zip backup"""
        backup_name = f"backup_{self.timestamp}.zip"
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        cmd = ['zip', '-r', backup_path, '.']
        
        result = subprocess.run(cmd, cwd=self.source_dir, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Backup created: {backup_path}")
            return backup_path
        else:
            print(f"Backup failed: {result.stderr}")
            return None
    
    def create_backup_rsync(self, dest_dir):
        """Create backup using rsync"""
        cmd = ['rsync', '-avz', '--delete', f"{self.source_dir}/", dest_dir]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Rsync backup completed to {dest_dir}")
            return True
        else:
            print(f"Rsync failed: {result.stderr}")
            return False
    
    def list_backups(self):
        """List existing backups"""
        pattern = os.path.join(self.backup_dir, 'backup_*')
        backups = glob.glob(pattern)
        backups.sort(key=os.path.getmtime, reverse=True)
        
        print("\nEXISTING BACKUPS")
        print("=" * 50)
        for backup in backups:
            size = os.path.getsize(backup) / (1024**2)
            mtime = datetime.fromtimestamp(os.path.getmtime(backup))
            print(f"  {os.path.basename(backup)} - {size:.2f} MB - {mtime}")
        
        return backups
    
    def restore_backup(self, backup_file, dest_dir):
        """Restore from backup"""
        if backup_file.endswith('.tar.gz'):
            cmd = ['tar', '-xzf', backup_file, '-C', dest_dir]
        elif backup_file.endswith('.zip'):
            cmd = ['unzip', backup_file, '-d', dest_dir]
        else:
            print("Unsupported backup format")
            return False
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Restored backup to {dest_dir}")
            return True
        else:
            print(f"Restore failed: {result.stderr}")
            return False

# Usage
backup = BackupScript('/path/to/source', '/path/to/backup')
# backup.create_backup_tar()
# backup.create_backup_zip()
# backup.list_backups()
# backup.restore_backup('/path/to/backup/backup_20240115_120000.tar.gz', '/path/to/restore')
```

### Example 5: Command Line Tool Wrapper

```python
import subprocess
import argparse
import sys

class CommandWrapper:
    def __init__(self, command, description=""):
        self.command = command
        self.description = description
    
    def run(self, args):
        """Run the command with arguments"""
        cmd = [self.command] + args
        print(f"Running: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)
            return result.returncode
        except FileNotFoundError:
            print(f"Command not found: {self.command}", file=sys.stderr)
            return 127
        except KeyboardInterrupt:
            print("\nInterrupted by user", file=sys.stderr)
            return 130
    
    def run_interactive(self, args):
        """Run command with interactive output"""
        cmd = [self.command] + args
        print(f"Running: {' '.join(cmd)}")
        
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Read output line by line
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output, end='')
            
            # Get any remaining stderr
            _, stderr = process.communicate()
            if stderr:
                print(stderr, file=sys.stderr)
            
            return process.returncode
        except FileNotFoundError:
            print(f"Command not found: {self.command}", file=sys.stderr)
            return 127
        except KeyboardInterrupt:
            process.terminate()
            print("\nInterrupted by user", file=sys.stderr)
            return 130
    
    def add_arguments(self, parser):
        """Add command-specific arguments"""
        pass

class DockerWrapper(CommandWrapper):
    def __init__(self):
        super().__init__('docker', 'Docker container management')
    
    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='docker_command', help='Docker commands')
        
        # ps command
        ps_parser = subparsers.add_parser('ps', help='List containers')
        ps_parser.add_argument('-a', '--all', action='store_true', help='Show all containers')
        
        # images command
        images_parser = subparsers.add_parser('images', help='List images')
        
        # run command
        run_parser = subparsers.add_parser('run', help='Run a container')
        run_parser.add_argument('image', help='Image name')
        run_parser.add_argument('-d', '--detach', action='store_true', help='Run in background')
        run_parser.add_argument('-p', '--port', help='Port mapping')
        run_parser.add_argument('--name', help='Container name')
    
    def run(self, args):
        """Override to handle specific docker commands"""
        if hasattr(args, 'docker_command'):
            if args.docker_command == 'ps':
                cmd = ['docker', 'ps']
                if args.all:
                    cmd.append('-a')
                return self.run_interactive(cmd)
            elif args.docker_command == 'images':
                return self.run_interactive(['docker', 'images'])
            elif args.docker_command == 'run':
                cmd = ['docker', 'run']
                if args.detach:
                    cmd.append('-d')
                if args.port:
                    cmd.extend(['-p', args.port])
                if args.name:
                    cmd.extend(['--name', args.name])
                cmd.append(args.image)
                return self.run_interactive(cmd)
        
        return super().run(args)

# Usage
wrapper = DockerWrapper()
parser = argparse.ArgumentParser(description=wrapper.description)
wrapper.add_arguments(parser)
args = parser.parse_args()
sys.exit(wrapper.run(args))
```

---

## Practice Exercises

### Beginner Level

1. **Run `ls` Command**
   ```python
   # Run ls -la and print output
   ```

2. **Capture Output**
   ```python
   # Run command and capture stdout/stderr
   ```

3. **Check Return Code**
   ```python
   # Run command and check if it succeeded
   ```

### Intermediate Level

4. **Pipe Commands**
   ```python
   # Chain two commands using pipes
   ```

5. **Timeout Handling**
   ```python
   # Run command with timeout
   ```

6. **Provide Input**
   ```python
   # Provide input to command via stdin
   ```

### Advanced Level

7. **Process Manager**
   ```python
   # Manage multiple subprocesses
   ```

8. **Git Automation**
   ```python
   # Automate git operations
   ```

9. **Backup Script**
   ```python
   # Create backup using tar/zip
   ```

---

## Quick Reference Card

```python
import subprocess

# Run command, wait for completion
subprocess.run(['ls', '-la'])
subprocess.run('ls -la', shell=True)  # Avoid if possible

# Capture output
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
print(result.returncode)

# Check return code
result = subprocess.run(['ls', '-la'], check=True)  # Raises on error

# Timeout
result = subprocess.run(['sleep', '10'], timeout=5)

# Provide input
result = subprocess.run(['grep', 'hello'], input='hello world', text=True)

# Popen (advanced)
process = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

# Non-blocking
process = subprocess.Popen(['sleep', '10'])
while process.poll() is None:
    print("Still running...")
    time.sleep(1)

# Constants
subprocess.PIPE      # Standard pipe
subprocess.STDOUT    # Redirect stderr to stdout
subprocess.DEVNULL   # Discard output

# Exceptions
subprocess.CalledProcessError  # Non-zero exit with check=True
subprocess.TimeoutExpired      # Command timed out
subprocess.SubprocessError     # Base class
```

---

## Next Step

- Move to [third_party](third_party/README.md) to learn about third-party modules.

---

*Master subprocess for powerful system command execution from Python! 🐍✨*
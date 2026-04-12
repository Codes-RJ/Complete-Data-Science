# 📘 SHLEX MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is Shlex?](#what-is-shlex)
2. [`shlex.split()` – Split String Like Shell](#shlexsplit--split-string-like-shell)
3. [`shlex.quote()` – Quote for Shell Safety](#shlexquote--quote-for-shell-safety)
4. [`shlex.shlex` Class – Custom Lexer](#shlexshlex-class--custom-lexer)
5. [`shlex.join()` – Join Tokens (Python 3.8+)](#shlexjoin--join-tokens-python-38)
6. [Real-World Examples](#real-world-examples)
7. [Practice Exercises](#practice-exercises)

---

## What is Shlex?

The `shlex` module provides functions for parsing shell-like syntax, splitting strings like a Unix shell would, and safely quoting strings for use in shell commands.

```python
import shlex

# Split a string like a shell
tokens = shlex.split('echo "Hello World"')
print(tokens)  # ['echo', 'Hello World']

# Quote a string for shell safety
user_input = "file.txt; rm -rf /"
safe = shlex.quote(user_input)
print(safe)  # 'file.txt; rm -rf /'
```

**Key Characteristics:**
- ✅ Parses shell-style syntax
- ✅ Handles quotes and escapes
- ✅ Safe quoting for subprocess
- ✅ Customizable lexer
- ✅ Prevents command injection

---

## `shlex.split()` – Split String Like Shell

### Basic Usage

```python
import shlex

# Simple split (like str.split())
print(shlex.split("one two three"))  # ['one', 'two', 'three']

# Handles quotes (preserves spaces inside quotes)
print(shlex.split('echo "Hello World"'))  # ['echo', 'Hello World']

# Handles single quotes
print(shlex.split("echo 'Hello World'"))  # ['echo', 'Hello World']

# Handles escaped characters
print(shlex.split('echo "Hello\\"World"'))  # ['echo', 'Hello"World']

# Multiple spaces are collapsed
print(shlex.split("one    two    three"))  # ['one', 'two', 'three']
```

### Complex Examples

```python
import shlex

# Mixed quotes
cmd = 'echo "Hello" world \'Python rules\''
print(shlex.split(cmd))
# ['echo', 'Hello', 'world', 'Python rules']

# Escaped spaces
cmd = 'echo Hello\\ World'
print(shlex.split(cmd))  # ['echo', 'Hello World']

# Comments (ignored by default)
cmd = 'echo hello # this is a comment'
print(shlex.split(cmd))  # ['echo', 'hello']

# With comments preserved (using posix=False)
print(shlex.split(cmd, posix=False))  # ['echo', 'hello', '#', 'this', 'is', 'a', 'comment']
```

### Using `shlex.split()` with Subprocess

```python
import shlex
import subprocess

# Safe way to run user input
user_input = 'echo "Hello World"'
tokens = shlex.split(user_input)
result = subprocess.run(tokens, capture_output=True, text=True)
print(result.stdout)  # Hello World

# Without shlex.split (dangerous)
# subprocess.run(user_input, shell=True)  # Command injection risk!
```

---

## `shlex.quote()` – Quote for Shell Safety

### Basic Usage

```python
import shlex

# Quote a string for shell safety
filename = "my file.txt"
quoted = shlex.quote(filename)
print(quoted)  # 'my file.txt'

# Special characters are escaped
dangerous = "file; rm -rf /"
safe = shlex.quote(dangerous)
print(safe)  # 'file; rm -rf /'

# Empty string
empty = shlex.quote("")
print(empty)  # ''
```

### Preventing Command Injection

```python
import shlex
import subprocess

def safe_delete_file(filename):
    """Safely delete a file using rm"""
    # Bad - command injection possible
    # subprocess.run(f'rm {filename}', shell=True)
    
    # Good - using quote
    subprocess.run(['rm', shlex.quote(filename)], shell=False)
    
    # Better - using list arguments (no quote needed)
    subprocess.run(['rm', filename])

# User input could be malicious
user_input = "important.txt; rm -rf /"

# Without quoting (dangerous)
# subprocess.run(f'rm {user_input}', shell=True)  # Would delete everything!

# With quoting (safe)
safe_cmd = f'rm {shlex.quote(user_input)}'
print(safe_cmd)  # rm 'important.txt; rm -rf /'
```

### Building Safe Commands

```python
import shlex

def build_command(cmd, *args):
    """Build a safe shell command string"""
    parts = [cmd]
    for arg in args:
        parts.append(shlex.quote(str(arg)))
    return ' '.join(parts)

# Examples
print(build_command('echo', 'Hello', 'World'))
# echo 'Hello' 'World'

print(build_command('rm', 'file with spaces.txt'))
# rm 'file with spaces.txt'

print(build_command('grep', 'pattern', 'file.txt'))
# grep 'pattern' 'file.txt'
```

---

## `shlex.shlex` Class – Custom Lexer

### Basic Lexer Usage

```python
import shlex

# Create lexer
lexer = shlex.shlex('echo "Hello World"')

# Tokenize
tokens = list(lexer)
print(tokens)  # ['echo', 'Hello World']

# Lexer as iterator
lexer = shlex.shlex('one two "three four"')
for token in lexer:
    print(token)
# one
# two
# three four
```

### Customizing the Lexer

```python
import shlex

# Custom word characters
text = 'var_name=value'
lexer = shlex.shlex(text)
lexer.wordchars += '='  # Add '=' as word character
print(list(lexer))  # ['var_name=value']

# Custom comment character
text = 'command arg # comment'
lexer = shlex.shlex(text)
lexer.commenters = '#'  # Treat # as comment start
print(list(lexer))  # ['command', 'arg']

# Custom quote characters
text = "say [Hello World]"
lexer = shlex.shlex(text)
lexer.quotes = '[]'  # Use [] as quotes
print(list(lexer))  # ['say', 'Hello World']
```

### Lexer Configuration Options

```python
import shlex

text = 'echo "Hello" # comment'

# POSIX mode (default) - respects quotes
lexer = shlex.shlex(text, posix=True)
print(list(lexer))  # ['echo', 'Hello']

# Non-POSIX mode - doesn't treat quotes specially
lexer = shlex.shlex(text, posix=False)
print(list(lexer))  # ['echo', '"Hello"', '#', 'comment']

# Control whitespace splitting
lexer = shlex.shlex('a,b,c', posix=True)
lexer.whitespace = ','  # Split on comma
print(list(lexer))  # ['a', 'b', 'c']
```

---

## `shlex.join()` – Join Tokens (Python 3.8+)

```python
import shlex

# Join tokens into a shell-escaped string
tokens = ['echo', 'Hello World', 'Python']
result = shlex.join(tokens)
print(result)  # echo 'Hello World' Python

# With special characters
tokens = ['rm', 'file with spaces.txt', 'file;rm']
result = shlex.join(tokens)
print(result)  # rm 'file with spaces.txt' 'file;rm'

# Reverse of split
original = 'echo "Hello" world'
tokens = shlex.split(original)
reconstructed = shlex.join(tokens)
print(reconstructed)  # echo 'Hello' world
```

---

## Real-World Examples

### Example 1: Safe Command Builder

```python
import shlex
import subprocess

class SafeCommand:
    @staticmethod
    def build(cmd, *args):
        """Build safe command string"""
        parts = [cmd]
        for arg in args:
            parts.append(shlex.quote(str(arg)))
        return ' '.join(parts)
    
    @staticmethod
    def run(cmd, *args, capture=True):
        """Run command safely"""
        if capture:
            result = subprocess.run(
                [cmd] + list(args),
                capture_output=True,
                text=True
            )
            return result.stdout, result.stderr, result.returncode
        else:
            return subprocess.run([cmd] + list(args))
    
    @staticmethod
    def run_shell(cmd_string):
        """Run shell command safely (using shlex.split)"""
        args = shlex.split(cmd_string)
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode

# Usage
# stdout, stderr, code = SafeCommand.run('echo', 'Hello', 'World')
# print(stdout)

# Using shell string
# stdout, stderr, code = SafeCommand.run_shell('echo "Hello World"')
# print(stdout)
```

### Example 2: Configuration File Parser

```python
import shlex

class ConfigParser:
    def __init__(self, filename=None):
        self.config = {}
        if filename:
            self.load(filename)
    
    def load(self, filename):
        """Load configuration from file"""
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Split line like shell
                tokens = shlex.split(line)
                if len(tokens) >= 2:
                    key = tokens[0]
                    value = ' '.join(tokens[1:])
                    self.config[key] = value
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def save(self, filename):
        """Save configuration to file"""
        with open(filename, 'w') as f:
            for key, value in self.config.items():
                f.write(f"{key} {shlex.quote(value)}\n")
    
    def __str__(self):
        lines = []
        for key, value in self.config.items():
            lines.append(f"{key}={value}")
        return '\n'.join(lines)

# Usage
# Create config file
# with open('app.conf', 'w') as f:
#     f.write("host localhost\n")
#     f.write("port 8080\n")
#     f.write("name 'My App'\n")

# config = ConfigParser('app.conf')
# print(config.get('host'))  # localhost
# print(config.get('port'))  # 8080
```

### Example 3: Simple Shell Emulator

```python
import shlex
import subprocess
import os

class SimpleShell:
    def __init__(self):
        self.commands = {
            'echo': self.cmd_echo,
            'exit': self.cmd_exit,
            'help': self.cmd_help,
            'pwd': self.cmd_pwd,
            'cd': self.cmd_cd,
            'ls': self.cmd_ls,
        }
        self.running = True
    
    def cmd_echo(self, args):
        """Echo command"""
        print(' '.join(args))
    
    def cmd_exit(self, args):
        """Exit command"""
        self.running = False
        print("Goodbye!")
    
    def cmd_help(self, args):
        """Help command"""
        print("Available commands:")
        for cmd in self.commands:
            print(f"  {cmd}")
    
    def cmd_pwd(self, args):
        """Print working directory"""
        print(os.getcwd())
    
    def cmd_cd(self, args):
        """Change directory"""
        if args:
            try:
                os.chdir(args[0])
            except Exception as e:
                print(f"Error: {e}")
        else:
            os.chdir(os.path.expanduser('~'))
    
    def cmd_ls(self, args):
        """List directory"""
        path = args[0] if args else '.'
        try:
            items = os.listdir(path)
            for item in items:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    def execute(self, line):
        """Execute a command line"""
        if not line.strip():
            return
        
        try:
            # Parse command line
            tokens = shlex.split(line)
            cmd = tokens[0].lower()
            args = tokens[1:]
            
            if cmd in self.commands:
                self.commands[cmd](args)
            else:
                # Try running as external command
                result = subprocess.run(tokens, capture_output=True, text=True)
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr)
        except Exception as e:
            print(f"Error: {e}")
    
    def run(self):
        """Run the shell"""
        print("Simple Shell v1.0")
        print("Type 'help' for commands, 'exit' to quit")
        
        while self.running:
            try:
                line = input("$ ")
                self.execute(line)
            except KeyboardInterrupt:
                print("\nType 'exit' to quit")
            except EOFError:
                print("\nGoodbye!")
                break

# Usage
# shell = SimpleShell()
# shell.run()
```

### Example 4: CSV-Like Parser with Quotes

```python
import shlex

class CSVParser:
    @staticmethod
    def parse_line(line, delimiter=','):
        """Parse CSV line handling quoted fields"""
        # Replace delimiter with space for shlex
        # But preserve quoted delimiters
        result = []
        current = []
        in_quotes = False
        
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
                current.append(char)
            elif char == delimiter and not in_quotes:
                result.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        
        if current:
            result.append(''.join(current).strip())
        
        # Use shlex to unquote
        return [shlex.split(item)[0] if item else '' for item in result]
    
    @staticmethod
    def parse_line_shlex(line, delimiter=','):
        """Alternative using shlex directly"""
        # Replace delimiter with space, then use shlex
        modified = line.replace(delimiter, ' ')
        tokens = shlex.split(modified)
        return tokens
    
    @staticmethod
    def format_line(fields, delimiter=','):
        """Format fields as CSV line with quotes if needed"""
        quoted_fields = []
        for field in fields:
            if delimiter in str(field) or ' ' in str(field):
                quoted_fields.append(shlex.quote(str(field)))
            else:
                quoted_fields.append(str(field))
        return delimiter.join(quoted_fields)

# Test
line = 'Alice, "Smith, John", 30, "New York, NY"'
print(f"Original: {line}")

# Parse
parsed = CSVParser.parse_line(line)
print(f"Parsed: {parsed}")

# Format back
formatted = CSVParser.format_line(parsed)
print(f"Formatted: {formatted}")
```

### Example 5: Environment Variable Parser

```python
import shlex
import os

class EnvParser:
    @staticmethod
    def parse_env_file(filename):
        """Parse .env file with support for quoted values"""
        env_vars = {}
        
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Use shlex to unquote if needed
                    if value and value[0] in '"\'':
                        value = shlex.split(value)[0]
                    
                    env_vars[key] = value
        
        return env_vars
    
    @staticmethod
    def write_env_file(filename, env_vars):
        """Write .env file with proper quoting"""
        with open(filename, 'w') as f:
            for key, value in env_vars.items():
                # Quote if contains spaces or special chars
                if any(c in value for c in ' \t\n\r="\'$'):
                    value = shlex.quote(value)
                f.write(f"{key}={value}\n")
    
    @staticmethod
    def substitute(text, env_vars):
        """Substitute environment variables in text"""
        # Simple substitution: $VAR or ${VAR}
        result = text
        for key, value in env_vars.items():
            result = result.replace(f'${key}', value)
            result = result.replace(f'${{{key}}}', value)
        return result

# Usage
env_vars = {
    'APP_NAME': 'My Application',
    'APP_PORT': '8080',
    'APP_HOST': 'localhost',
    'APP_PATH': '/path/with spaces'
}

# Write .env file
EnvParser.write_env_file('.env', env_vars)

# Read .env file
loaded = EnvParser.parse_env_file('.env')
print("Loaded env vars:")
for key, value in loaded.items():
    print(f"  {key}={value}")

# Substitute
template = "Starting $APP_NAME on $APP_HOST:$APP_PORT"
result = EnvParser.substitute(template, loaded)
print(f"\nTemplate: {template}")
print(f"Result: {result}")
```

---

## Practice Exercises

### Beginner Level

1. **Split Command**
   ```python
   # Use shlex.split() to parse 'echo "Hello World"'
   ```

2. **Quote String**
   ```python
   # Quote a string with spaces for shell safety
   ```

3. **Parse CSV Line**
   ```python
   # Use shlex to parse 'value1,"value with comma",value3'
   ```

### Intermediate Level

4. **Safe Command Builder**
   ```python
   # Build function to safely construct shell commands
   ```

5. **Config File Parser**
   ```python
   # Parse config file with quoted values
   ```

6. **Custom Lexer**
   ```python
   # Create lexer that treats ':' as delimiter
   ```

### Advanced Level

7. **Simple Shell**
   ```python
   # Implement basic shell with command parsing
   ```

8. **Environment File Parser**
   ```python
   # Parse .env file with quoted values
   ```

9. **CSV Parser**
   ```python
   # Implement CSV parser using shlex
   ```

---

## Quick Reference Card

```python
import shlex

# Splitting
shlex.split(s)                      # Split string like shell
shlex.split(s, posix=False)         # Non-POSIX mode (preserve comments)

# Quoting
shlex.quote(s)                      # Quote string for shell safety

# Joining (Python 3.8+)
shlex.join(tokens)                  # Join tokens with shell escaping

# Custom lexer
lexer = shlex.shlex(s)              # Create lexer
lexer.wordchars += '_-'             # Add word characters
lexer.whitespace = ',;'             # Custom whitespace
lexer.commenters = '#'              # Comment characters
lexer.quotes = '"\''                # Quote characters

# Lexer attributes
lexer.posix = True/False            # POSIX mode
lexer.escape = '\\'                 # Escape character
lexer.escape_chars = '\\'           # Characters to escape

# Iterate tokens
for token in lexer:
    print(token)

# Get all tokens
tokens = list(lexer)

# Subprocess safety
# Bad (command injection risk)
subprocess.run(f'echo {user_input}', shell=True)

# Good (using list)
subprocess.run(['echo', user_input])

# Good (using shlex.quote)
subprocess.run(f'echo {shlex.quote(user_input)}', shell=True)
```

---

## Next Step

- Move to [04_io.md](04_io.md) to learn about core I/O tools (StringIO, BytesIO).

---

*Master shlex for safe shell command parsing and execution! 🐍✨*
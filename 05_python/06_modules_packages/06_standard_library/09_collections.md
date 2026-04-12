# 📘 COLLECTIONS MODULE – COMPLETE GUIDE

## 📌 Table of Contents
1. [What is the Collections Module?](#what-is-the-collections-module)
2. [Counter](#counter)
3. [DefaultDict](#defaultdict)
4. [OrderedDict](#ordereddict)
5. [Deque](#deque)
6. [NamedTuple](#namedtuple)
7. [ChainMap](#chainmap)
8. [Real-World Examples](#real-world-examples)
9. [Practice Exercises](#practice-exercises)

---

## What is the Collections Module?

The `collections` module provides specialized container datatypes that extend the functionality of built-in types like `list`, `dict`, `set`, and `tuple`.

```python
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

# Examples
counter = Counter([1, 1, 2, 3, 3, 3])
print(counter)  # Counter({3: 3, 1: 2, 2: 1})

default = defaultdict(int)
default['a'] += 1
print(default['a'])  # 1
print(default['b'])  # 0 (default)

queue = deque([1, 2, 3])
queue.appendleft(0)
print(queue)  # deque([0, 1, 2, 3])
```

**Key Benefits:**
- ✅ More efficient for specific use cases
- ✅ Provide additional functionality
- ✅ Memory efficient alternatives
- ✅ Thread-safe options (deque)

---

## Counter

`Counter` is a dictionary subclass for counting hashable objects.

### Creating Counters

```python
from collections import Counter

# From list
counter1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(counter1)  # Counter({'a': 3, 'b': 2, 'c': 1})

# From string
counter2 = Counter('abracadabra')
print(counter2)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# From dictionary
counter3 = Counter({'a': 3, 'b': 2, 'c': 1})

# From keyword arguments
counter4 = Counter(a=3, b=2, c=1)

# Empty counter
counter5 = Counter()
```

### Counter Methods

```python
from collections import Counter

c = Counter('abracadabra')

# Most common elements
print(c.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]

# Total count
print(sum(c.values()))  # 11

# Convert to list (elements repeated)
print(list(c.elements()))  # ['a','a','a','a','a','b','b','r','r','c','d']

# Subtract counts
c.subtract('aaaa')
print(c['a'])  # 1 (5 - 4)

# Update counts
c.update('bb')
print(c['b'])  # 4 (2 + 2)

# Get count with default
print(c.get('z', 0))  # 0
```

### Counter Operations

```python
from collections import Counter

c1 = Counter('abracadabra')
c2 = Counter('abracadabra')

# Addition
c3 = c1 + c2
print(c3['a'])  # 10

# Subtraction
c4 = c1 - c2
print(c4)  # Counter() (all zeros)

# Intersection (min)
c5 = c1 & c2
print(c5['a'])  # 5

# Union (max)
c6 = c1 | c2
print(c6['a'])  # 5

# Comparison
print(c1 == c2)  # True
print(c1 > c2)   # False
```

### Practical Counter Examples

```python
from collections import Counter

# Word frequency
text = "the cat and the dog and the bird"
words = text.split()
word_count = Counter(words)
print(word_count)
# Counter({'the': 3, 'and': 2, 'cat': 1, 'dog': 1, 'bird': 1})

# Character frequency
text = "hello world"
char_count = Counter(text)
print(char_count)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Find most common characters
print(char_count.most_common(2))  # [('l', 3), ('o', 2)]

# Find unique elements
unique = [item for item, count in char_count.items() if count == 1]
print(unique)  # ['h', 'e', ' ', 'w', 'r', 'd']
```

---

## DefaultDict

`defaultdict` is a dictionary that provides a default value for missing keys.

### Basic Usage

```python
from collections import defaultdict

# Default type: int (default 0)
dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print(dd['a'])  # 1
print(dd['c'])  # 0 (default)

# Default type: list (default [])
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(dd['fruits'])  # ['apple', 'banana']
print(dd['vegetables'])  # [] (default)

# Default type: set (default set())
dd = defaultdict(set)
dd['colors'].add('red')
dd['colors'].add('blue')
print(dd['colors'])  # {'red', 'blue'}

# Default type: str (default '')
dd = defaultdict(str)
dd['name'] += 'John'
print(dd['name'])  # 'John'
print(dd['city'])  # '' (default)
```

### Custom Default Factory

```python
from collections import defaultdict

# Custom default value using lambda
dd = defaultdict(lambda: 'N/A')
dd['name'] = 'Alice'
print(dd['name'])    # Alice
print(dd['age'])     # N/A

# Default value as function
def default_value():
    return {'count': 0, 'total': 0}

dd = defaultdict(default_value)
dd['product1']['count'] += 1
dd['product1']['total'] += 100
print(dd['product1'])  # {'count': 1, 'total': 100}
print(dd['product2'])  # {'count': 0, 'total': 0}
```

### Practical DefaultDict Examples

```python
from collections import defaultdict

# Grouping items by category
items = [('fruit', 'apple'), ('fruit', 'banana'), ('veg', 'carrot'), ('fruit', 'orange')]

grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)

print(dict(grouped))
# {'fruit': ['apple', 'banana', 'orange'], 'veg': ['carrot']}

# Counting without if statements
data = ['a', 'b', 'a', 'c', 'b', 'a']
count = defaultdict(int)
for item in data:
    count[item] += 1
print(dict(count))  # {'a': 3, 'b': 2, 'c': 1}

# Nested defaultdict (defaultdict of defaultdict)
nested = defaultdict(lambda: defaultdict(int))
nested['math']['Alice'] += 95
nested['math']['Bob'] += 87
nested['science']['Alice'] += 92

print(dict(nested))
# {'math': {'Alice': 95, 'Bob': 87}, 'science': {'Alice': 92}}
```

---

## OrderedDict

`OrderedDict` is a dictionary that remembers the insertion order of keys.

### Basic Usage

```python
from collections import OrderedDict

# Regular dict (Python 3.7+ maintains order, but OrderedDict has additional methods)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move to end
od.move_to_end('a')
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move to beginning
od.move_to_end('c', last=False)
print(od)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# Pop last item
last = od.popitem()
print(last)  # ('a', 1)
print(od)    # OrderedDict([('c', 3), ('b', 2)])

# Pop first item
first = od.popitem(last=False)
print(first)  # ('c', 3)
print(od)     # OrderedDict([('b', 2)])
```

### OrderedDict vs Regular Dict

```python
from collections import OrderedDict

# In Python 3.7+, regular dict preserves order
regular = {}
regular['a'] = 1
regular['b'] = 2
regular['c'] = 3
print(regular)  # {'a': 1, 'b': 2, 'c': 3} (ordered)

# But OrderedDict has additional methods
ordered = OrderedDict()
ordered['a'] = 1
ordered['b'] = 2
ordered['c'] = 3

# Equality comparison (order matters for OrderedDict)
print(regular == {'a': 1, 'b': 2, 'c': 3})  # True
print(ordered == OrderedDict([('a', 1), ('b', 2), ('c', 3)]))  # True
print(ordered == OrderedDict([('c', 3), ('b', 2), ('a', 1)]))  # False
```

### Practical OrderedDict Examples

```python
from collections import OrderedDict

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Usage
cache = LRUCache(2)
cache.put('a', 1)
cache.put('b', 2)
print(cache.get('a'))  # 1
cache.put('c', 3)      # Removes 'b'
print(cache.get('b'))  # -1

# Preserving order for serialization
config = OrderedDict()
config['version'] = '1.0'
config['debug'] = True
config['host'] = 'localhost'
config['port'] = 8080

import json
print(json.dumps(config, indent=2))
# {
#   "version": "1.0",
#   "debug": true,
#   "host": "localhost",
#   "port": 8080
# }
```

---

## Deque

`deque` (double-ended queue) is a list-like container with fast appends and pops from both ends.

### Basic Usage

```python
from collections import deque

# Create deque
d = deque([1, 2, 3, 4, 5])
print(d)  # deque([1, 2, 3, 4, 5])

# Append to right
d.append(6)
print(d)  # deque([1, 2, 3, 4, 5, 6])

# Append to left
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4, 5, 6])

# Pop from right
right = d.pop()
print(right)  # 6
print(d)      # deque([0, 1, 2, 3, 4, 5])

# Pop from left
left = d.popleft()
print(left)  # 0
print(d)     # deque([1, 2, 3, 4, 5])
```

### Deque Methods

```python
from collections import deque

d = deque([1, 2, 3, 4, 5])

# Extend right
d.extend([6, 7, 8])
print(d)  # deque([1, 2, 3, 4, 5, 6, 7, 8])

# Extend left
d.extendleft([0, -1, -2])
print(d)  # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

# Rotate (shift elements)
d.rotate(2)   # Rotate right by 2
print(d)      # deque([7, 8, -2, -1, 0, 1, 2, 3, 4, 5, 6])

d.rotate(-3)  # Rotate left by 3
print(d)      # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, -2])

# Max length
d = deque(maxlen=3)
d.extend([1, 2, 3])
print(d)  # deque([1, 2, 3], maxlen=3)
d.append(4)
print(d)  # deque([2, 3, 4], maxlen=3)  # Removed leftmost
```

### Deque Performance

```python
from collections import deque
import timeit

# List pop(0) is O(n), deque popleft is O(1)
list_time = timeit.timeit('lst.pop(0)', setup='lst=list(range(10000))', number=1000)
deque_time = timeit.timeit('dq.popleft()', setup='from collections import deque; dq=deque(range(10000))', number=1000)

print(f"List pop(0): {list_time:.4f}s")
print(f"Deque popleft: {deque_time:.4f}s")
print(f"Deque is {list_time/deque_time:.0f}x faster")
```

### Practical Deque Examples

```python
from collections import deque

# Queue (FIFO)
queue = deque()
queue.append('task1')
queue.append('task2')
queue.append('task3')

print(queue.popleft())  # task1
print(queue.popleft())  # task2
print(queue.popleft())  # task3

# Stack (LIFO)
stack = deque()
stack.append('item1')
stack.append('item2')
stack.append('item3')

print(stack.pop())  # item3
print(stack.pop())  # item2
print(stack.pop())  # item1

# Sliding window
def sliding_window_average(data, window_size):
    window = deque(maxlen=window_size)
    averages = []
    
    for num in data:
        window.append(num)
        if len(window) == window_size:
            averages.append(sum(window) / window_size)
    
    return averages

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sliding_window_average(data, 3))
# [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

# Recent items (keep last N)
recent = deque(maxlen=5)
for i in range(10):
    recent.append(f"item{i}")
    print(f"Added item{i}: {list(recent)}")
```

---

## NamedTuple

`namedtuple` creates tuple subclasses with named fields.

### Basic Usage

```python
from collections import namedtuple

# Define namedtuple
Point = namedtuple('Point', ['x', 'y'])
# Alternative syntaxes
# Point = namedtuple('Point', 'x y')
# Point = namedtuple('Point', 'x, y')

# Create instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

# Access by name
print(p1.x)  # 10
print(p1.y)  # 20

# Access by index (still a tuple)
print(p1[0])  # 10
print(p1[1])  # 20

# Unpacking
x, y = p2
print(x, y)  # 30 40
```

### NamedTuple Methods

```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instance
alice = Person('Alice', 30, 'NYC')

# Convert to dictionary
print(alice._asdict())  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Create new instance with replaced fields
bob = alice._replace(name='Bob', age=25)
print(bob)  # Person(name='Bob', age=25, city='NYC')

# Get field names
print(Person._fields)  # ('name', 'age', 'city')

# Create from iterable
data = ['Charlie', 35, 'LA']
charlie = Person._make(data)
print(charlie)  # Person(name='Charlie', age=35, city='LA')

# Get field defaults (Python 3.7+)
Person2 = namedtuple('Person2', ['name', 'age', 'city'], defaults=['Unknown', 0, 'Unknown'])
p = Person2('Alice')
print(p)  # Person2(name='Alice', age=0, city='Unknown')
```

### Practical NamedTuple Examples

```python
from collections import namedtuple

# RGB Color
Color = namedtuple('Color', ['red', 'green', 'blue'])
white = Color(255, 255, 255)
black = Color(0, 0, 0)
red = Color(255, 0, 0)

print(f"White: R={white.red}, G={white.green}, B={white.blue}")

# Stock Quote
Stock = namedtuple('Stock', ['symbol', 'price', 'volume', 'change'])
aapl = Stock('AAPL', 175.50, 50000000, 2.5)
print(f"{aapl.symbol}: ${aapl.price} (Change: {aapl.change}%)")

# HTTP Response
Response = namedtuple('Response', ['status_code', 'body', 'headers'])
resp = Response(200, '{"data": "success"}', {'Content-Type': 'application/json'})
if resp.status_code == 200:
    print("Request successful!")

# Database record
User = namedtuple('User', ['id', 'username', 'email', 'created_at'])
user = User(1, 'alice123', 'alice@example.com', '2024-01-15')
print(f"User {user.username} ({user.email}) created on {user.created_at}")
```

---

## ChainMap

`ChainMap` groups multiple dictionaries into a single view.

### Basic Usage

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Create ChainMap
chain = ChainMap(dict1, dict2, dict3)
print(chain)  # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

# Access values (searches in order)
print(chain['a'])  # 1 (from dict1)
print(chain['c'])  # 3 (from dict2)
print(chain['e'])  # 5 (from dict3)

# Keys and values
print(list(chain.keys()))    # ['a', 'b', 'c', 'd', 'e', 'f']
print(list(chain.values()))  # [1, 2, 3, 4, 5, 6]

# Check existence
print('a' in chain)  # True
print('z' in chain)  # False
```

### ChainMap Operations

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}  # 'b' exists in both

chain = ChainMap(dict1, dict2)

# Access returns first found
print(chain['b'])  # 1 (from dict1, not dict2)

# New dict for modifications
new_dict = {}
chain = chain.new_child(new_dict)
print(chain)  # ChainMap({}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# Add to front
chain = chain.new_child({'d': 5})
print(chain.maps)  # [{'d': 5}, {}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4}]

# Get parent chain
parent = chain.parents
print(parent.maps)  # [{}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
```

### Practical ChainMap Examples

```python
from collections import ChainMap

# Configuration with defaults and overrides
defaults = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'timeout': 30
}

user_config = {
    'port': 9090,
    'debug': True
}

config = ChainMap(user_config, defaults)

print(f"Host: {config['host']}")      # localhost (from defaults)
print(f"Port: {config['port']}")      # 9090 (from user_config)
print(f"Debug: {config['debug']}")    # True (from user_config)
print(f"Timeout: {config['timeout']}") # 30 (from defaults)

# Command line arguments priority
import sys

# Priority: command line > environment > defaults
cmd_args = {'debug': 'true'}  # Parsed from sys.argv
env_vars = {'PORT': '8080'}   # From os.environ
defaults = {'debug': 'false', 'port': '3000'}

# Convert to dict format
cmd_dict = {k: v for k, v in cmd_args.items()}
env_dict = {k.lower(): v for k, v in env_vars.items()}

config = ChainMap(cmd_dict, env_dict, defaults)
print(f"Debug: {config.get('debug', 'false')}")  # true
print(f"Port: {config.get('port', '3000')}")     # 8080

# Layered configuration
base = {'db': 'postgres', 'host': 'localhost'}
dev = {'debug': True, 'host': 'dev.local'}
prod = {'debug': False, 'host': 'prod.example.com'}

dev_config = ChainMap(dev, base)
prod_config = ChainMap(prod, base)

print(f"Dev DB: {dev_config['db']}, Host: {dev_config['host']}, Debug: {dev_config['debug']}")
print(f"Prod DB: {prod_config['db']}, Host: {prod_config['host']}, Debug: {prod_config['debug']}")
```

---

## Real-World Examples

### Example 1: Word Frequency Analyzer

```python
from collections import Counter, defaultdict
import re

class WordAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\b\w+\b', text.lower())
        self.counter = Counter(self.words)
    
    def most_common(self, n=10):
        """Get n most common words"""
        return self.counter.most_common(n)
    
    def least_common(self, n=10):
        """Get n least common words"""
        return self.counter.most_common()[:-n-1:-1]
    
    def word_frequency(self, word):
        """Get frequency of specific word"""
        return self.counter.get(word.lower(), 0)
    
    def unique_words(self):
        """Get number of unique words"""
        return len(self.counter)
    
    def total_words(self):
        """Get total number of words"""
        return len(self.words)
    
    def words_by_length(self):
        """Group words by length"""
        by_length = defaultdict(list)
        for word in self.words:
            by_length[len(word)].append(word)
        return dict(by_length)
    
    def generate_report(self):
        """Generate analysis report"""
        print("WORD FREQUENCY ANALYSIS")
        print("=" * 40)
        print(f"Total words: {self.total_words()}")
        print(f"Unique words: {self.unique_words()}")
        print(f"\nTop 5 most common words:")
        for word, count in self.most_common(5):
            print(f"  {word}: {count}")
        print(f"\nTop 5 least common words:")
        for word, count in self.least_common(5):
            print(f"  {word}: {count}")

# Usage
text = """
Python is a powerful programming language. Python is great for data science.
Data science uses Python extensively. Python has a simple syntax.
Many companies use Python for their backend systems.
"""

analyzer = WordAnalyzer(text)
analyzer.generate_report()
```

### Example 2: Task Scheduler with Deque

```python
from collections import deque
from datetime import datetime, timedelta

class TaskScheduler:
    def __init__(self):
        self.tasks = deque()
        self.history = deque(maxlen=100)  # Keep last 100 tasks
    
    def add_task(self, task, priority=0):
        """Add task with priority (higher priority = higher number)"""
        task_entry = {
            'task': task,
            'priority': priority,
            'created': datetime.now()
        }
        
        # Insert at correct position based on priority
        inserted = False
        for i, existing in enumerate(self.tasks):
            if existing['priority'] < priority:
                self.tasks.insert(i, task_entry)
                inserted = True
                break
        
        if not inserted:
            self.tasks.append(task_entry)
        
        print(f"Added task: {task} (priority {priority})")
    
    def execute_next(self):
        """Execute and remove next task"""
        if not self.tasks:
            print("No tasks to execute")
            return None
        
        task = self.tasks.popleft()
        task['executed'] = datetime.now()
        self.history.append(task)
        
        print(f"Executing: {task['task']}")
        return task
    
    def view_tasks(self):
        """View pending tasks"""
        if not self.tasks:
            print("No pending tasks")
            return
        
        print("\nPending Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"  {i}. {task['task']} (Priority: {task['priority']})")
    
    def view_history(self):
        """View executed tasks history"""
        if not self.history:
            print("No task history")
            return
        
        print("\nTask History:")
        for task in self.history:
            duration = (task['executed'] - task['created']).total_seconds()
            print(f"  {task['task']} - took {duration:.2f}s")

# Usage
scheduler = TaskScheduler()
scheduler.add_task("Email report", 1)
scheduler.add_task("Backup database", 3)
scheduler.add_task("Process data", 2)
scheduler.add_task("Send notifications", 1)

scheduler.view_tasks()
scheduler.execute_next()
scheduler.execute_next()
scheduler.view_history()
```

### Example 3: Configuration Manager with ChainMap

```python
from collections import ChainMap
import json
import os

class ConfigManager:
    def __init__(self, config_files=None):
        self.configs = []
        
        # Load default config
        self.configs.append(self.get_defaults())
        
        # Load file configs
        if config_files:
            for file in config_files:
                self.load_file(file)
        
        # Load environment variables
        self.load_env()
        
        self.chain = ChainMap(*self.configs)
    
    def get_defaults(self):
        return {
            'app': {
                'name': 'MyApp',
                'version': '1.0.0',
                'debug': False
            },
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp',
                'user': 'admin',
                'password': 'secret'
            },
            'logging': {
                'level': 'INFO',
                'file': 'app.log'
            }
        }
    
    def load_file(self, filename):
        """Load configuration from JSON file"""
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
                self.configs.insert(0, config)
                print(f"Loaded config from {filename}")
        except FileNotFoundError:
            print(f"Config file {filename} not found")
        except json.JSONDecodeError as e:
            print(f"Error parsing {filename}: {e}")
    
    def load_env(self):
        """Load configuration from environment variables"""
        env_config = {}
        
        for key, value in os.environ.items():
            if key.startswith('APP_'):
                # Convert APP_DATABASE_HOST to database.host
                parts = key[4:].lower().split('_')
                target = env_config
                for part in parts[:-1]:
                    target = target.setdefault(part, {})
                target[parts[-1]] = value
        
        if env_config:
            self.configs.insert(0, env_config)
            print("Loaded environment variables")
    
    def get(self, key, default=None):
        """Get configuration value using dot notation"""
        keys = key.split('.')
        value = self.chain
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value
    
    def display(self):
        """Display current configuration"""
        print("\nCurrent Configuration:")
        print(json.dumps(dict(self.chain), indent=2))

# Usage
# Set environment variable
os.environ['APP_DATABASE_HOST'] = 'prod-db.example.com'

# Create config with files
config = ConfigManager(['config.json', 'local.json'])

print(f"App name: {config.get('app.name')}")
print(f"Database host: {config.get('database.host')}")
print(f"Database port: {config.get('database.port')}")
print(f"Debug mode: {config.get('app.debug')}")

config.display()
```

### Example 4: Data Pipeline with Deque

```python
from collections import deque
import time
import random

class DataPipeline:
    def __init__(self, max_size=1000):
        self.input_queue = deque(maxlen=max_size)
        self.processing_queue = deque(maxlen=max_size)
        self.output_queue = deque(maxlen=max_size)
        self.stats = {
            'processed': 0,
            'errors': 0,
            'avg_time': 0
        }
    
    def add_data(self, data):
        """Add data to input queue"""
        self.input_queue.append({
            'data': data,
            'timestamp': time.time(),
            'id': self.stats['processed'] + 1
        })
    
    def process_batch(self, batch_size=10):
        """Process batch of data"""
        processed = 0
        for _ in range(min(batch_size, len(self.input_queue))):
            item = self.input_queue.popleft()
            
            try:
                # Simulate processing
                result = self._process_item(item)
                self.processing_queue.append(result)
                processed += 1
            except Exception as e:
                self.stats['errors'] += 1
                print(f"Error processing item {item['id']}: {e}")
        
        return processed
    
    def _process_item(self, item):
        """Process single item"""
        # Simulate processing time
        time.sleep(random.uniform(0.01, 0.05))
        
        # Simulate occasional errors
        if random.random() < 0.05:
            raise ValueError("Random processing error")
        
        return {
            'id': item['id'],
            'original': item['data'],
            'processed': item['data'] * 2,
            'processing_time': time.time() - item['timestamp']
        }
    
    def collect_results(self, batch_size=10):
        """Collect processed results"""
        collected = []
        for _ in range(min(batch_size, len(self.processing_queue))):
            result = self.processing_queue.popleft()
            self.output_queue.append(result)
            collected.append(result)
            self.stats['processed'] += 1
            
            # Update average time
            current_avg = self.stats['avg_time']
            self.stats['avg_time'] = (
                (current_avg * (self.stats['processed'] - 1) + result['processing_time'])
                / self.stats['processed']
            )
        
        return collected
    
    def get_stats(self):
        """Get pipeline statistics"""
        return {
            'input_size': len(self.input_queue),
            'processing_size': len(self.processing_queue),
            'output_size': len(self.output_queue),
            'total_processed': self.stats['processed'],
            'total_errors': self.stats['errors'],
            'avg_processing_time': self.stats['avg_time']
        }
    
    def run(self, iterations=100, batch_size=10):
        """Run pipeline for specified iterations"""
        print("Starting data pipeline...")
        
        for i in range(iterations):
            # Generate data
            for _ in range(random.randint(5, 20)):
                self.add_data(random.randint(1, 100))
            
            # Process
            self.process_batch(batch_size)
            results = self.collect_results(batch_size)
            
            if i % 10 == 0:
                stats = self.get_stats()
                print(f"Iteration {i}: Processed {stats['total_processed']}, "
                      f"Avg time: {stats['avg_processing_time']:.3f}s")
        
        print("\nPipeline complete!")
        return self.get_stats()

# Usage
pipeline = DataPipeline(max_size=500)
stats = pipeline.run(iterations=50, batch_size=20)

print("\nFinal Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value}")
```

---

## Practice Exercises

### Beginner Level

1. **Word Counter**
   ```python
   # Use Counter to count word frequencies in a sentence
   ```

2. **DefaultDict Sum**
   ```python
   # Use defaultdict to sum values by category
   ```

3. **Deque Queue**
   ```python
   # Implement FIFO queue using deque
   ```

### Intermediate Level

4. **LRU Cache**
   ```python
   # Implement LRU cache using OrderedDict
   ```

5. **NamedTuple Data**
   ```python
   # Define namedtuple for employee data
   ```

6. **ChainMap Config**
   ```python
   # Layer multiple configuration dictionaries
   ```

### Advanced Level

7. **Text Analyzer**
   ```python
   # Build complete text analysis tool using Counter
   ```

8. **Task Scheduler**
   ```python
   # Priority queue using deque with priority
   ```

9. **Configuration Manager**
   ```python
   # Multi-layer config using ChainMap
   ```

---

## Quick Reference Card

```python
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

# Counter
Counter(iterable)               # Create counter
.most_common(n)                 # Most common elements
.elements()                     # Iterator of elements
.subtract(iterable)             # Subtract counts
.update(iterable)               # Add counts

# defaultdict
defaultdict(int)                # Default 0
defaultdict(list)               # Default []
defaultdict(set)                # Default set()
defaultdict(lambda: value)      # Custom default

# OrderedDict
OrderedDict()                   # Create ordered dict
.move_to_end(key, last=True)    # Move key to end
.popitem(last=True)             # Pop last or first

# deque
deque(iterable, maxlen=n)       # Create deque
.append(x)                      # Add to right
.appendleft(x)                  # Add to left
.pop()                          # Remove from right
.popleft()                      # Remove from left
.extend(iterable)               # Extend right
.extendleft(iterable)           # Extend left (reversed)
.rotate(n)                      # Rotate n steps

# namedtuple
namedtuple('Name', fields)      # Create namedtuple
._asdict()                      # Convert to dict
._replace(**kwargs)             # Create copy with replaced fields
._make(iterable)                # Create from iterable
._fields                        # Tuple of field names

# ChainMap
ChainMap(*maps)                 # Create ChainMap
.new_child(m=None)              # New ChainMap with m at front
.parents                        # ChainMap without first map
.maps                           # List of maps
```

---

## Next Step

- Move to [10_itertools.md](10_itertools.md) to learn about efficient looping tools.

---

*Master the collections module for specialized and efficient data structures! 🐍✨*
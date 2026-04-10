# 📘 TYPE HINTS – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Type Hints?](#what-are-type-hints)
2. [Basic Type Hints](#basic-type-hints)
3. [Collection Types](#collection-types)
4. [Optional and Union Types](#optional-and-union-types)
5. [Custom Types and Aliases](#custom-types-and-aliases)
6. [Type Variables and Generics](#type-variables-and-generics)
7. [Protocols and ABCs](#protocols-and-abcs)
8. [Real-World Examples](#real-world-examples)
9. [Common Pitfalls](#common-pitfalls)
10. [Practice Exercises](#practice-exercises)

---

## What are Type Hints?

**Type hints** (also called type annotations) allow you to specify the expected types of variables, function parameters, and return values in Python. They were introduced in **PEP 484** (Python 3.5+).

```python
# Without type hints (traditional)
def greet(name):
    return f"Hello, {name}"

# With type hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hello, {name}"

# Variable annotation
age: int = 30
name: str = "Alice"
prices: list[float] = [19.99, 29.99, 39.99]
```

**Key Characteristics:**
- ✅ Optional (Python ignores them at runtime)
- ✅ Improve code readability and documentation
- ✅ Enable static type checking with tools like mypy
- ✅ Enhance IDE support (autocomplete, refactoring)
- ✅ Catch type-related bugs early

---

## Basic Type Hints

### Primitive Types

```python
# Basic types
age: int = 25
price: float = 19.99
name: str = "Alice"
is_active: bool = True
data: bytes = b'hello'
nothing: None = None

# Function annotations
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"

def divide(a: float, b: float) -> float:
    return a / b

def is_even(n: int) -> bool:
    return n % 2 == 0

# Multiple parameters
def create_user(name: str, age: int, email: str, is_active: bool = True) -> dict:
    return {
        "name": name,
        "age": age,
        "email": email,
        "is_active": is_active
    }
```

### Type Hints for Variables

```python
# Variable annotations (Python 3.6+)
x: int = 42
y: float = 3.14
name: str = "Alice"
is_valid: bool = True

# Without initialization (Python 3.6+)
count: int
count = 10

# Multiple variables
a: int = 1
b: int = 2
c: int = 3

# Class attributes
class Person:
    name: str
    age: int
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

---

## Collection Types

### Lists

```python
from typing import List

# Python 3.9+ (list[int])
def process_numbers(numbers: list[int]) -> list[int]:
    return [n * 2 for n in numbers]

# Python 3.8 and below
from typing import List
def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

# Nested lists
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6]]

# Mixed types
mixed_list: list[object] = [1, "hello", 3.14, True]

# Real use
def filter_even(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)
```

### Tuples

```python
from typing import Tuple

# Fixed-size tuple
def get_user() -> tuple[str, int, str]:
    return ("Alice", 30, "alice@example.com")

# Tuple with different types
person: tuple[str, int, bool] = ("Bob", 25, True)

# Empty tuple
empty: tuple = ()

# Variable-length tuple (homogeneous)
def process_items(items: tuple[int, ...]) -> int:
    return sum(items)

# Named tuple
from typing import NamedTuple
class Point(NamedTuple):
    x: int
    y: int

def distance(p1: Point, p2: Point) -> float:
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
```

### Dictionaries

```python
from typing import Dict

# Python 3.9+
def process_config(config: dict[str, any]) -> dict[str, any]:
    config["processed"] = True
    return config

# Python 3.8 and below
from typing import Dict
def process_config(config: Dict[str, any]) -> Dict[str, any]:
    config["processed"] = True
    return config

# Specific types
user_data: dict[str, int] = {"age": 30, "score": 95}
scores: dict[str, list[float]] = {
    "Alice": [85.5, 90.0, 88.5],
    "Bob": [78.0, 82.5, 79.0]
}

# Real use
def count_words(text: str) -> dict[str, int]:
    words = text.lower().split()
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

def merge_configs(config1: dict[str, any], config2: dict[str, any]) -> dict[str, any]:
    return {**config1, **config2}
```

### Sets

```python
from typing import Set

# Python 3.9+
def get_unique_items(items: list[int]) -> set[int]:
    return set(items)

# Python 3.8 and below
from typing import Set
def get_unique_items(items: List[int]) -> Set[int]:
    return set(items)

# Type-specific set
tags: set[str] = {"python", "coding", "tutorial"}
numbers: set[int] = {1, 2, 3, 4, 5}

# Real use
def find_common(a: set[str], b: set[str]) -> set[str]:
    return a & b

def unique_characters(text: str) -> set[str]:
    return set(text.lower())
```

---

## Optional and Union Types

### Optional (Can be None)

```python
from typing import Optional

# Optional means value can be type or None
def find_user(user_id: int) -> Optional[dict]:
    if user_id in database:
        return database[user_id]
    return None

# Python 3.10+ alternative
def find_user(user_id: int) -> dict | None:
    if user_id in database:
        return database[user_id]
    return None

# Optional parameter
def connect(timeout: Optional[int] = None) -> None:
    if timeout is None:
        timeout = 30
    print(f"Connecting with timeout {timeout}")

# Optional return
def get_value(key: str) -> Optional[str]:
    cache = {"name": "Alice"}
    return cache.get(key)  # May return None
```

### Union (Multiple Types)

```python
from typing import Union

# Value can be int or float
def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

# Python 3.10+ alternative
def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

# Multiple types
def process(value: Union[int, float, str]) -> str:
    return str(value)

# Real use: Flexible function
def add(a: int | float, b: int | float) -> int | float:
    return a + b

def safe_divide(a: int | float, b: int | float) -> int | float | None:
    if b == 0:
        return None
    return a / b
```

### Combining Optional and Union

```python
from typing import Optional, Union

# Value can be int, float, or None
def process(value: Optional[Union[int, float]]) -> str:
    if value is None:
        return "No value"
    return f"Value: {value}"

# Python 3.10+
def process(value: int | float | None) -> str:
    if value is None:
        return "No value"
    return f"Value: {value}"

# Real use: Configuration
def get_config(key: str, default: Optional[str | int | bool] = None) -> str | int | bool | None:
    config = {"debug": True, "port": 8080}
    return config.get(key, default)
```

---

## Custom Types and Aliases

### Type Aliases

```python
from typing import List, Dict, Tuple, Union

# Create readable aliases
UserId = int
UserName = str
UserData = Dict[str, Union[str, int, bool]]

def get_user(user_id: UserId) -> UserData:
    return {"id": user_id, "name": "Alice", "active": True}

# Complex aliases
Vector = List[float]
Matrix = List[List[float]]
Point2D = Tuple[float, float]
RGB = Tuple[int, int, int]

def dot_product(v1: Vector, v2: Vector) -> float:
    return sum(a * b for a, b in zip(v1, v2))

def color_to_hex(rgb: RGB) -> str:
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

# Nested aliases
JSONValue = Union[str, int, float, bool, None, List['JSONValue'], Dict[str, 'JSONValue']]
JSONObject = Dict[str, JSONValue]

def parse_json(data: JSONObject) -> None:
    print(f"Parsing {len(data)} keys")
```

### NewType (Creating Distinct Types)

```python
from typing import NewType

# Create distinct types (even if same underlying type)
UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user(user_id: UserId) -> dict:
    return {"id": user_id, "name": "User"}

def get_product(product_id: ProductId) -> dict:
    return {"id": product_id, "name": "Product"}

# These work
user_id = UserId(123)
product_id = ProductId(456)

get_user(user_id)      # OK
get_product(product_id) # OK

# These would be flagged by type checker
# get_user(product_id)   # Error! Wrong type
# get_product(user_id)   # Error! Wrong type

# NewType with validation
class Email(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if '@' not in v:
            raise ValueError("Invalid email")
        return cls(v)

def send_email(to: Email, subject: str, body: str) -> None:
    print(f"Sending to {to}")
```

---

## Type Variables and Generics

### Basic Generics

```python
from typing import TypeVar, List, Generic

# Type variable
T = TypeVar('T')

# Generic function
def first_item(items: List[T]) -> T:
    return items[0]

# Works with any type
print(first_item([1, 2, 3]))        # 1 (int)
print(first_item(["a", "b", "c"]))  # 'a' (str)
print(first_item([True, False]))    # True (bool)

# Multiple type variables
K = TypeVar('K')
V = TypeVar('V')

def get_value(dict: dict[K, V], key: K, default: V) -> V:
    return dict.get(key, default)

# Bounded type variables
Number = TypeVar('Number', int, float)

def double(x: Number) -> Number:
    return x * 2

print(double(5))      # 10 (int)
print(double(3.14))   # 6.28 (float)
```

### Generic Classes

```python
from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        if self._items:
            return self._items.pop()
        return None
    
    def peek(self) -> Optional[T]:
        if self._items:
            return self._items[-1]
        return None
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def size(self) -> int:
        return len(self._items)

# Usage
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack.pop())  # 3

str_stack = Stack[str]()
str_stack.push("a")
str_stack.push("b")
print(str_stack.pop())  # "b"

# This would be flagged
# int_stack.push("hello")  # Error! Expected int
```

### Generic Constraints

```python
from typing import TypeVar, Generic

# Constrained type variable
Comparable = TypeVar('Comparable', bound='Comparable')

class Comparable(Generic[Comparable]):
    def __lt__(self, other: Comparable) -> bool:
        return True

# Upper bound
Numeric = TypeVar('Numeric', int, float)

def average(values: list[Numeric]) -> float:
    return sum(values) / len(values)

print(average([1, 2, 3, 4, 5]))        # Works
print(average([1.5, 2.5, 3.5]))        # Works
# print(average(["a", "b", "c"]))      # Would be flagged

# Multiple bounds
class HasLength:
    def __len__(self) -> int:
        return 0

Sized = TypeVar('Sized', bound=HasLength)

def get_size(obj: Sized) -> int:
    return len(obj)

print(get_size([1, 2, 3]))   # 3
print(get_size("hello"))     # 5
print(get_size({1, 2, 3}))   # 3
```

---

## Protocols and ABCs

### Protocols (Structural Subtyping)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Drawing circle"

class Square:
    def draw(self) -> str:
        return "Drawing square"

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    # No draw method

def render(shape: Drawable) -> None:
    print(shape.draw())

render(Circle())  # OK
render(Square())  # OK
# render(Point(10, 20))  # Would be flagged (no draw method)

# More complex protocol
class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool:
        ...

def sort_items(items: list[Comparable]) -> list[Comparable]:
    return sorted(items)  # Works if items implement __lt__

# Works with int, float, str (they implement __lt__)
print(sort_items([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
```

### Abstract Base Classes (ABCs)

```python
from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass
    
    @abstractmethod
    def move(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"
    
    def move(self) -> str:
        return "Running"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"
    
    def move(self) -> str:
        return "Walking"

class Fish(Animal):
    def move(self) -> str:
        return "Swimming"
    # Missing speak method - would be flagged

def animal_sounds(animals: list[Animal]) -> List[str]:
    return [animal.speak() for animal in animals]

dog = Dog()
cat = Cat()
print(animal_sounds([dog, cat]))  # ['Woof!', 'Meow!']

# Using ABC from collections.abc
from collections.abc import Iterable, Sequence, MutableSequence

def process_iterable(items: Iterable[int]) -> int:
    return sum(items)

def process_sequence(items: Sequence[str]) -> str:
    return ' '.join(items)

def modify_list(items: MutableSequence[int]) -> None:
    items.append(999)

print(process_iterable([1, 2, 3]))       # 6
print(process_iterable((1, 2, 3)))      # 6
print(process_iterable({1, 2, 3}))      # 6

print(process_sequence(["a", "b", "c"])) # "a b c"
print(process_sequence(("x", "y", "z"))) # "x y z"
```

---

## Real-World Examples

### Example 1: Data Processing Pipeline

```python
from typing import List, Dict, Optional, Callable, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    """Data class for financial transactions"""
    id: int
    amount: float
    timestamp: datetime
    category: str
    description: str

class DataPipeline:
    """Generic data processing pipeline with type hints"""
    
    def __init__(self) -> None:
        self._filters: List[Callable[[Transaction], bool]] = []
        self._transformers: List[Callable[[Transaction], Transaction]] = []
    
    def add_filter(self, filter_func: Callable[[Transaction], bool]) -> None:
        """Add a filter to the pipeline"""
        self._filters.append(filter_func)
    
    def add_transformer(self, transformer: Callable[[Transaction], Transaction]) -> None:
        """Add a transformer to the pipeline"""
        self._transformers.append(transformer)
    
    def process(self, transactions: List[Transaction]) -> List[Transaction]:
        """Process all transactions through the pipeline"""
        result = transactions.copy()
        
        # Apply filters
        for filter_func in self._filters:
            result = [t for t in result if filter_func(t)]
        
        # Apply transformers
        for transformer in self._transformers:
            result = [transformer(t) for t in result]
        
        return result

# Define filters and transformers
def filter_by_category(category: str) -> Callable[[Transaction], bool]:
    def filter_func(transaction: Transaction) -> bool:
        return transaction.category == category
    return filter_func

def filter_min_amount(min_amount: float) -> Callable[[Transaction], bool]:
    def filter_func(transaction: Transaction) -> bool:
        return transaction.amount >= min_amount
    return filter_func

def add_tax(tax_rate: float) -> Callable[[Transaction], Transaction]:
    def transformer(transaction: Transaction) -> Transaction:
        return Transaction(
            id=transaction.id,
            amount=transaction.amount * (1 + tax_rate),
            timestamp=transaction.timestamp,
            category=transaction.category,
            description=f"{transaction.description} (with tax)"
        )
    return transformer

# Usage
print("DATA PROCESSING PIPELINE")
print("=" * 50)

# Create sample transactions
transactions = [
    Transaction(1, 100.0, datetime.now(), "food", "Groceries"),
    Transaction(2, 500.0, datetime.now(), "electronics", "Laptop"),
    Transaction(3, 50.0, datetime.now(), "food", "Restaurant"),
    Transaction(4, 200.0, datetime.now(), "clothing", "Jacket"),
    Transaction(5, 75.0, datetime.now(), "food", "Takeout"),
]

print(f"Original transactions: {len(transactions)}")

# Create pipeline
pipeline = DataPipeline()

# Add filters and transformers
pipeline.add_filter(filter_by_category("food"))
pipeline.add_filter(filter_min_amount(60.0))
pipeline.add_transformer(add_tax(0.10))  # 10% tax

# Process
processed = pipeline.process(transactions)

print(f"Processed transactions: {len(processed)}")
for t in processed:
    print(f"  {t.id}: ${t.amount:.2f} - {t.description}")
```

### Example 2: API Client with Type Hints

```python
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
import json
import requests

@dataclass
class APIResponse:
    """Generic API response wrapper"""
    status_code: int
    data: Optional[Dict[str, Any]]
    error: Optional[str]
    success: bool

class APIClient:
    """API client with comprehensive type hints"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """Make GET request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.get(url, params=params)
            data = response.json() if response.content else None
            
            return APIResponse(
                status_code=response.status_code,
                data=data,
                error=None if response.ok else data.get("message", "Unknown error"),
                success=response.ok
            )
        except requests.RequestException as e:
            return APIResponse(
                status_code=0,
                data=None,
                error=str(e),
                success=False
            )
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        """Make POST request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.post(url, json=data)
            response_data = response.json() if response.content else None
            
            return APIResponse(
                status_code=response.status_code,
                data=response_data,
                error=None if response.ok else response_data.get("message", "Unknown error"),
                success=response.ok
            )
        except requests.RequestException as e:
            return APIResponse(
                status_code=0,
                data=None,
                error=str(e),
                success=False
            )

# User type definitions
@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool

@dataclass
class CreateUserRequest:
    name: str
    email: str
    password: str

class UserAPI:
    """User-specific API client"""
    
    def __init__(self, client: APIClient) -> None:
        self.client = client
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        response = self.client.get(f"/users/{user_id}")
        
        if response.success and response.data:
            data = response.data
            return User(
                id=data["id"],
                name=data["name"],
                email=data["email"],
                is_active=data.get("is_active", True)
            )
        return None
    
    def list_users(self, active_only: bool = True) -> List[User]:
        """List all users"""
        params = {"active_only": active_only} if active_only else None
        response = self.client.get("/users", params=params)
        
        users = []
        if response.success and response.data:
            for user_data in response.data:
                users.append(User(
                    id=user_data["id"],
                    name=user_data["name"],
                    email=user_data["email"],
                    is_active=user_data.get("is_active", True)
                ))
        return users
    
    def create_user(self, request: CreateUserRequest) -> Optional[User]:
        """Create new user"""
        response = self.client.post("/users", data={
            "name": request.name,
            "email": request.email,
            "password": request.password
        })
        
        if response.success and response.data:
            data = response.data
            return User(
                id=data["id"],
                name=data["name"],
                email=data["email"],
                is_active=True
            )
        return None

# Usage (simulated without actual API)
print("API CLIENT WITH TYPE HINTS")
print("=" * 50)

# Create client (simulated)
client = APIClient("https://api.example.com", api_key="test-key")
user_api = UserAPI(client)

# Simulated response (since no actual API)
print("Type hints provide excellent IDE support and documentation")
print("\nUserAPI methods:")
print("  get_user(user_id: int) -> Optional[User]")
print("  list_users(active_only: bool = True) -> List[User]")
print("  create_user(request: CreateUserRequest) -> Optional[User]")
```

### Example 3: Repository Pattern with Generics

```python
from typing import TypeVar, Generic, List, Optional, Dict, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(Generic[T, ID], ABC):
    """Generic repository interface"""
    
    @abstractmethod
    def save(self, entity: T) -> T:
        """Save entity"""
        pass
    
    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find by ID"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Find all entities"""
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> bool:
        """Delete by ID"""
        pass
    
    @abstractmethod
    def update(self, id: ID, entity: T) -> Optional[T]:
        """Update entity"""
        pass

@dataclass
class User:
    id: int
    name: str
    email: str
    age: int

@dataclass
class Product:
    id: str
    name: str
    price: float
    stock: int

class InMemoryRepository(Repository[T, ID]):
    """In-memory implementation of repository"""
    
    def __init__(self) -> None:
        self._storage: Dict[ID, T] = {}
        self._next_id: int = 1
    
    def save(self, entity: T) -> T:
        """Save entity (auto-generate ID for int IDs)"""
        # Auto-generate ID for int-based IDs
        if hasattr(entity, 'id'):
            if getattr(entity, 'id') == 0 or getattr(entity, 'id') is None:
                setattr(entity, 'id', self._next_id)
                self._next_id += 1
        
        entity_id = getattr(entity, 'id')
        self._storage[entity_id] = entity
        return entity
    
    def find_by_id(self, id: ID) -> Optional[T]:
        return self._storage.get(id)
    
    def find_all(self) -> List[T]:
        return list(self._storage.values())
    
    def delete(self, id: ID) -> bool:
        if id in self._storage:
            del self._storage[id]
            return True
        return False
    
    def update(self, id: ID, entity: T) -> Optional[T]:
        if id in self._storage:
            self._storage[id] = entity
            return entity
        return None

# Usage
print("REPOSITORY PATTERN WITH GENERICS")
print("=" * 50)

# Create repositories
user_repo: Repository[User, int] = InMemoryRepository()
product_repo: Repository[Product, str] = InMemoryRepository()

# Create and save users
user1 = User(id=0, name="Alice", email="alice@example.com", age=30)
user2 = User(id=0, name="Bob", email="bob@example.com", age=25)

saved_user1 = user_repo.save(user1)
saved_user2 = user_repo.save(user2)

print(f"Saved users: {saved_user1.id}, {saved_user2.id}")

# Find users
found_user = user_repo.find_by_id(1)
print(f"Found user: {found_user}")

# List all users
all_users = user_repo.find_all()
print(f"All users: {all_users}")

# Create and save products
product1 = Product(id="", name="Laptop", price=999.99, stock=10)
product2 = Product(id="", name="Mouse", price=29.99, stock=50)

saved_product1 = product_repo.save(product1)
saved_product2 = product_repo.save(product2)

print(f"\nSaved products: {saved_product1.id}, {saved_product2.id}")

# Find product
found_product = product_repo.find_by_id(saved_product1.id)
print(f"Found product: {found_product}")

# Delete user
deleted = user_repo.delete(1)
print(f"\nUser 1 deleted: {deleted}")

# Verify deletion
all_users = user_repo.find_all()
print(f"Remaining users: {all_users}")
```

### Example 4: Event System with Callbacks

```python
from typing import Dict, List, Callable, Any, Generic, TypeVar
from dataclasses import dataclass, field
from datetime import datetime

T = TypeVar('T')

@dataclass
class Event(Generic[T]):
    """Generic event class"""
    name: str
    data: T
    timestamp: datetime = field(default_factory=datetime.now)

class EventBus:
    """Event bus with type-safe callbacks"""
    
    def __init__(self) -> None:
        self._listeners: Dict[str, List[Callable[[Event[Any]], None]]] = {}
    
    def subscribe(self, event_name: str, callback: Callable[[Event[Any]], None]) -> None:
        """Subscribe to an event"""
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(callback)
    
    def unsubscribe(self, event_name: str, callback: Callable[[Event[Any]], None]) -> bool:
        """Unsubscribe from an event"""
        if event_name in self._listeners:
            try:
                self._listeners[event_name].remove(callback)
                return True
            except ValueError:
                pass
        return False
    
    def emit(self, event: Event[Any]) -> None:
        """Emit an event"""
        if event.name in self._listeners:
            for callback in self._listeners[event.name]:
                callback(event)
    
    def emit_sync(self, event_name: str, data: Any) -> None:
        """Emit event with data"""
        self.emit(Event(event_name, data))

# Type-specific event handlers
def handle_user_login(event: Event[dict]) -> None:
    """Handle user login event"""
    user = event.data
    print(f"[{event.timestamp}] User logged in: {user['name']}")

def handle_user_logout(event: Event[dict]) -> None:
    """Handle user logout event"""
    user = event.data
    print(f"[{event.timestamp}] User logged out: {user['name']}")

def handle_order_placed(event: Event[dict]) -> None:
    """Handle order placed event"""
    order = event.data
    print(f"[{event.timestamp}] Order placed: #{order['id']} for ${order['total']:.2f}")

def handle_error(event: Event[Exception]) -> None:
    """Handle error event"""
    error = event.data
    print(f"[{event.timestamp}] Error occurred: {error}")

# Usage
print("EVENT SYSTEM WITH TYPE HINTS")
print("=" * 50)

# Create event bus
bus = EventBus()

# Subscribe to events
bus.subscribe("user.login", handle_user_login)
bus.subscribe("user.logout", handle_user_logout)
bus.subscribe("order.placed", handle_order_placed)
bus.subscribe("error", handle_error)

# Emit events
bus.emit_sync("user.login", {"name": "Alice", "id": 1})
bus.emit_sync("user.login", {"name": "Bob", "id": 2})

bus.emit_sync("order.placed", {"id": 1001, "total": 299.99})
bus.emit_sync("order.placed", {"id": 1002, "total": 599.50})

bus.emit_sync("user.logout", {"name": "Alice", "id": 1})

try:
    raise ValueError("Database connection failed")
except Exception as e:
    bus.emit_sync("error", e)

# Type hints provide clear expectations
print("\nEvent types:")
print("  user.login: Event[dict]")
print("  user.logout: Event[dict]")
print("  order.placed: Event[dict]")
print("  error: Event[Exception]")
```

---

## Common Pitfalls

### Pitfall 1: Type Hints Are Ignored at Runtime

```python
# Type hints do NOT enforce types at runtime
def add(a: int, b: int) -> int:
    return a + b

# This works even though types are wrong
result = add("hello", "world")
print(result)  # "helloworld"

# Use runtime checking if needed
def add_safe(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be int")
    return a + b
```

### Pitfall 2: Mutable Default Arguments

```python
# ❌ Wrong - Mutable default with type hint
def add_item(item: str, items: list[str] = []) -> list[str]:
    items.append(item)
    return items

# ✅ Correct
def add_item(item: str, items: Optional[list[str]] = None) -> list[str]:
    if items is None:
        items = []
    items.append(item)
    return items
```

### Pitfall 3: Circular Imports

```python
# file1.py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from file2 import ClassB

class ClassA:
    def method(self, b: 'ClassB') -> None:
        pass

# file2.py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from file1 import ClassA

class ClassB:
    def method(self, a: 'ClassA') -> None:
        pass
```

---

## Practice Exercises

### Beginner Level

1. **Annotate Function**
   ```python
   # Add type hints to this function
   def multiply_list(numbers, factor):
       return [n * factor for n in numbers]
   ```

2. **Optional Parameters**
   ```python
   # Add type hints with Optional
   def find_user(user_id, default=None):
       return users.get(user_id, default)
   ```

3. **Union Types**
   ```python
   # Add type hints with Union
   def to_string(value):
       return str(value)
   ```

### Intermediate Level

4. **Generic Stack**
   ```python
   # Implement generic Stack class with type hints
   # Support push, pop, peek, is_empty
   ```

5. **Repository Pattern**
   ```python
   # Implement generic repository interface
   # Add type hints for CRUD operations
   ```

6. **Event System**
   ```python
   # Implement type-safe event system
   # Support generic event types
   ```

### Advanced Level

7. **Dependency Injection**
   ```python
   # Implement type-checked dependency injection
   # Use type hints to resolve dependencies
   ```

8. **ORM with Type Hints**
   ```python
   # Create simple ORM with type hints
   # Map Python types to database types
   ```

9. **Type Validator**
   ```python
   # Create runtime type validator
   # Validate nested structures with type hints
   ```

---

## Quick Reference Card

```python
# Primitive types
x: int = 42
y: float = 3.14
name: str = "Alice"
flag: bool = True
data: bytes = b'hello'

# Collections (Python 3.9+)
numbers: list[int] = [1, 2, 3]
names: tuple[str, ...] = ("a", "b", "c")
config: dict[str, any] = {"key": "value"}
tags: set[str] = {"python", "coding"}

# Optional and Union
value: Optional[int] = None  # Python 3.8
value: int | None = None     # Python 3.10+
mixed: int | float | str = 42

# Type aliases
UserId = int
UserDict = dict[str, any]

# Function annotations
def func(param: type) -> return_type:
    pass

# Generic types
T = TypeVar('T')
class Box(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item

# Protocols
class Drawable(Protocol):
    def draw(self) -> None: ...

# Type checking tools
# mypy, pyright, pytype, pydantic
```

## Next Step

- Go to [PRACTICE_EXERCISES.md](/05_python/02_data_types/PRACTICE_EXERCISES.md) for understanding its usage and work scenarios.
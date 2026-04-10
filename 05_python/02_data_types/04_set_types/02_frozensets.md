# 📘 FROZENSETS (frozenset) – COMPLETE GUIDE

## 📌 Table of Contents
1. [What are Frozensets?](#what-are-frozensets)
2. [Creating Frozensets](#creating-frozensets)
3. [Frozenset Methods](#frozenset-methods)
4. [Frozenset Operations](#frozenset-operations)
5. [Why Use Frozensets?](#why-use-frozensets)
6. [Real-World Examples](#real-world-examples)
7. [Common Pitfalls](#common-pitfalls)
8. [Performance Tips](#performance-tips)
9. [Practice Exercises](#practice-exercises)

---

## 📖 What are Frozensets?

**Frozensets** are immutable versions of sets. Once created, they cannot be changed (no adding, removing, or modifying elements).

```python
# Examples of frozensets
fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset(["apple", "banana", "cherry"])
fs3 = frozenset()  # Empty frozenset
```

**Key Features:**
- ✅ Immutable (cannot be changed after creation)
- ✅ Hashable (can be used as dictionary keys)
- ✅ Unordered (no index positions)
- ✅ Unique elements (no duplicates)
- ✅ Fast membership testing (O(1))
- ✅ Support all set operations (union, intersection, etc.)
- ✅ Can contain other frozensets (but not regular sets)

---

## 🎯 Creating Frozensets

### Method 1: `frozenset()` Constructor

```python
# Empty frozenset
empty = frozenset()
print(empty)  # frozenset()
print(type(empty))  # <class 'frozenset'>

# From list
my_list = [1, 2, 2, 3, 3, 3]
fs = frozenset(my_list)
print(fs)  # frozenset({1, 2, 3})

# From tuple
my_tuple = (1, 2, 2, 3)
fs = frozenset(my_tuple)
print(fs)  # frozenset({1, 2, 3})

# From string (creates set of characters)
my_string = "hello"
fs = frozenset(my_string)
print(fs)  # frozenset({'h', 'e', 'l', 'o'})

# From range
fs = frozenset(range(5))
print(fs)  # frozenset({0, 1, 2, 3, 4})

# From another set
my_set = {1, 2, 3, 4, 5}
fs = frozenset(my_set)
print(fs)  # frozenset({1, 2, 3, 4, 5})
```

### Method 2: From Set Comprehension

```python
# Create frozenset from comprehension
fs = frozenset(x**2 for x in range(10))
print(fs)  # frozenset({0, 1, 4, 9, 16, 25, 36, 49, 64, 81})

# With condition
fs = frozenset(x for x in range(20) if x % 2 == 0)
print(fs)  # frozenset({0, 2, 4, 6, 8, 10, 12, 14, 16, 18})
```

### Method 3: Converting Between Set and Frozenset

```python
# Set to frozenset
my_set = {1, 2, 3, 4, 5}
fs = frozenset(my_set)
print(fs)  # frozenset({1, 2, 3, 4, 5})

# Frozenset to set
my_frozenset = frozenset([1, 2, 3])
back_to_set = set(my_frozenset)
print(back_to_set)  # {1, 2, 3}
```

---

## 📚 Frozenset Methods

Frozensets have **fewer methods** than regular sets because they are immutable. Only methods that don't modify the set are available.

### Available Methods

```python
fs = frozenset([1, 2, 3, 4, 5])

# 1. copy() - Returns a shallow copy
fs_copy = fs.copy()
print(fs_copy)  # frozenset({1, 2, 3, 4, 5})
print(fs is fs_copy)  # False (different object)

# 2. difference() - Returns difference of sets
other = frozenset([3, 4, 5, 6])
print(fs.difference(other))  # frozenset({1, 2})

# 3. intersection() - Returns intersection
print(fs.intersection(other))  # frozenset({3, 4, 5})

# 4. union() - Returns union
print(fs.union(other))  # frozenset({1, 2, 3, 4, 5, 6})

# 5. symmetric_difference() - Returns symmetric difference
print(fs.symmetric_difference(other))  # frozenset({1, 2, 6})

# 6. isdisjoint() - Check if disjoint
print(fs.isdisjoint({6, 7, 8}))  # True
print(fs.isdisjoint({5, 6, 7}))  # False

# 7. issubset() - Check if subset
print(fs.issubset({1, 2, 3, 4, 5, 6}))  # True
print(fs.issubset({1, 2, 3}))  # False

# 8. issuperset() - Check if superset
print(fs.issuperset({1, 2, 3}))  # True
print(fs.issuperset({1, 2, 6}))  # False
```

### Unavailable Methods (Would Modify)

```python
fs = frozenset([1, 2, 3])

# These methods do NOT exist on frozensets
# fs.add(4)           # AttributeError!
# fs.remove(1)        # AttributeError!
# fs.discard(2)       # AttributeError!
# fs.pop()            # AttributeError!
# fs.clear()          # AttributeError!
# fs.update([4,5])    # AttributeError!
```

### Comparison of Methods: Set vs Frozenset

| Operation | set | frozenset |
|-----------|-----|-----------|
| `add()` | ✅ | ❌ |
| `remove()` | ✅ | ❌ |
| `discard()` | ✅ | ❌ |
| `pop()` | ✅ | ❌ |
| `clear()` | ✅ | ❌ |
| `update()` | ✅ | ❌ |
| `intersection_update()` | ✅ | ❌ |
| `difference_update()` | ✅ | ❌ |
| `symmetric_difference_update()` | ✅ | ❌ |
| `copy()` | ✅ | ✅ |
| `union()` | ✅ | ✅ |
| `intersection()` | ✅ | ✅ |
| `difference()` | ✅ | ✅ |
| `symmetric_difference()` | ✅ | ✅ |
| `issubset()` | ✅ | ✅ |
| `issuperset()` | ✅ | ✅ |
| `isdisjoint()` | ✅ | ✅ |

---

## 🔢 Frozenset Operations

### All Set Operations Work (Return Frozensets)

```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

# Union (|)
print(a | b)  # frozenset({1, 2, 3, 4, 5, 6})
print(a.union(b))  # frozenset({1, 2, 3, 4, 5, 6})

# Intersection (&)
print(a & b)  # frozenset({3, 4})
print(a.intersection(b))  # frozenset({3, 4})

# Difference (-)
print(a - b)  # frozenset({1, 2})
print(a.difference(b))  # frozenset({1, 2})

# Symmetric Difference (^)
print(a ^ b)  # frozenset({1, 2, 5, 6})
print(a.symmetric_difference(b))  # frozenset({1, 2, 5, 6})

# Subset/Superset
print(a <= frozenset([1, 2, 3, 4, 5]))  # True
print(a >= frozenset([1, 2]))  # True

# Membership
print(3 in a)  # True
print(10 in a)  # False
```

### Operations with Regular Sets

```python
# Frozenset can work with regular sets (returns frozenset)
fs = frozenset([1, 2, 3])
s = {3, 4, 5}

print(fs | s)   # frozenset({1, 2, 3, 4, 5})
print(fs & s)   # frozenset({3})
print(fs - s)   # frozenset({1, 2})
print(fs ^ s)   # frozenset({1, 2, 4, 5})

# Regular set with frozenset (returns set)
print(s | fs)   # {1, 2, 3, 4, 5} (set, not frozenset)
```

### Iteration

```python
fs = frozenset(["apple", "banana", "cherry"])

# Basic iteration (order not guaranteed)
for fruit in fs:
    print(fruit)

# Sorted iteration
for fruit in sorted(fs):
    print(fruit)  # apple, banana, cherry

# With enumeration
for i, fruit in enumerate(fs):
    print(f"{i}: {fruit}")
```

### Length and Membership

```python
fs = frozenset([1, 2, 3, 4, 5])

print(len(fs))  # 5
print(3 in fs)  # True
print(10 in fs)  # False
print(3 not in fs)  # False
```

---

## 🎯 Why Use Frozensets?

### 1. As Dictionary Keys

Regular sets cannot be used as dictionary keys because they are mutable and unhashable. Frozensets can.

```python
# ❌ WRONG - Set as key (TypeError)
# my_dict = {{1, 2, 3}: "value"}  # TypeError!

# ✅ CORRECT - Frozenset as key
my_dict = {frozenset([1, 2, 3]): "value for {1,2,3}"}
print(my_dict[frozenset([1, 2, 3])])  # "value for {1,2,3}"

# Real use: Cache for set operations
cache = {}
def get_union(a, b):
    key = frozenset(a) | frozenset(b)
    if key not in cache:
        cache[key] = a | b
    return cache[key]

result1 = get_union({1, 2, 3}, {3, 4, 5})
result2 = get_union({1, 2, 3}, {3, 4, 5})  # Uses cache
print(f"Cached results: {len(cache)}")  # Cached results: 1
```

### 2. In Other Sets

Sets can only contain hashable elements. Frozensets are hashable, so they can be nested.

```python
# ❌ WRONG - Set containing set (TypeError)
# set_of_sets = {{1, 2}, {3, 4}}  # TypeError!

# ✅ CORRECT - Set containing frozensets
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(set_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}

# Real use: Grouping by set of features
users = {
    frozenset(["admin", "editor"]): ["alice", "bob"],
    frozenset(["viewer"]): ["charlie", "david", "eve"],
    frozenset(["admin", "viewer"]): ["frank"]
}

for permissions, users_list in users.items():
    print(f"Permissions {permissions}: {users_list}")
```

### 3. Immutability Guarantee

When you need to ensure data doesn't change, frozenset provides immutability.

```python
# Regular set can be modified
config_set = {1, 2, 3}
config_set.add(4)  # Modified accidentally

# Frozenset cannot be modified
config_frozenset = frozenset([1, 2, 3])
# config_frozenset.add(4)  # AttributeError! Protected

# Real use: Configuration constants
DEFAULT_PERMISSIONS = frozenset(["read", "write"])
# DEFAULT_PERMISSIONS.add("delete")  # Would raise error

class Config:
    ALLOWED_STATUSES = frozenset(["active", "inactive", "pending"])
    
    @classmethod
    def is_valid_status(cls, status):
        return status in cls.ALLOWED_STATUSES

print(Config.is_valid_status("active"))  # True
print(Config.is_valid_status("deleted"))  # False
```

### 4. Function Arguments

When passing to functions, frozenset ensures the data won't be modified.

```python
def process_data(data):
    # data is guaranteed not to be modified
    # (no add, remove, etc. operations possible)
    return sum(data)

# Safe to pass frozenset
result = process_data(frozenset([1, 2, 3, 4, 5]))
print(result)  # 15

# If you pass a set, it could be modified
my_set = {1, 2, 3}
process_data(my_set)  # Works, but my_set might be modified
```

---

## 🌍 Real-World Examples

### Example 1: Cache System with Frozenset Keys

```python
class QueryCache:
    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0
    
    def get_key(self, *args, **kwargs):
        """Create cache key from arguments"""
        # Convert mutable arguments to immutable
        key_parts = []
        
        for arg in args:
            if isinstance(arg, (list, set)):
                key_parts.append(frozenset(arg))
            elif isinstance(arg, dict):
                key_parts.append(frozenset(arg.items()))
            else:
                key_parts.append(arg)
        
        for k, v in sorted(kwargs.items()):
            if isinstance(v, (list, set)):
                key_parts.append((k, frozenset(v)))
            elif isinstance(v, dict):
                key_parts.append((k, frozenset(v.items())))
            else:
                key_parts.append((k, v))
        
        return frozenset(key_parts)
    
    def get(self, *args, **kwargs):
        """Get value from cache"""
        key = self.get_key(*args, **kwargs)
        
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        
        self.misses += 1
        return None
    
    def set(self, value, *args, **kwargs):
        """Set value in cache"""
        key = self.get_key(*args, **kwargs)
        self.cache[key] = value
    
    def stats(self):
        """Get cache statistics"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        
        return {
            'size': len(self.cache),
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f"{hit_rate:.1f}%"
        }

# Usage
cache = QueryCache()

# Expensive operation simulation
def expensive_calculation(numbers, multiplier=1):
    print(f"Calculating for {numbers}...")
    return sum(numbers) * multiplier

# Using cache
result1 = cache.get([1, 2, 3, 4, 5], multiplier=2)
if result1 is None:
    result1 = expensive_calculation([1, 2, 3, 4, 5], multiplier=2)
    cache.set(result1, [1, 2, 3, 4, 5], multiplier=2)

result2 = cache.get([1, 2, 3, 4, 5], multiplier=2)
if result2 is None:
    result2 = expensive_calculation([1, 2, 3, 4, 5], multiplier=2)
    cache.set(result2, [1, 2, 3, 4, 5], multiplier=2)

print(f"Result: {result1}")
print(f"Cache stats: {cache.stats()}")
```

### Example 2: Set of Sets for Clustering

```python
class ClusterManager:
    def __init__(self):
        self.clusters = set()  # Set of frozensets
    
    def add_cluster(self, elements):
        """Add a cluster (as frozenset)"""
        self.clusters.add(frozenset(elements))
    
    def remove_cluster(self, elements):
        """Remove a cluster"""
        self.clusters.discard(frozenset(elements))
    
    def find_cluster_containing(self, element):
        """Find cluster containing element"""
        for cluster in self.clusters:
            if element in cluster:
                return cluster
        return None
    
    def merge_clusters(self, cluster1, cluster2):
        """Merge two clusters"""
        merged = cluster1 | cluster2
        self.clusters.remove(cluster1)
        self.clusters.remove(cluster2)
        self.clusters.add(merged)
        return merged
    
    def get_cluster_sizes(self):
        """Get sizes of all clusters"""
        return {cluster: len(cluster) for cluster in self.clusters}
    
    def find_connected_components(self):
        """Find connected components (simplified)"""
        components = []
        remaining = set(self.clusters)
        
        while remaining:
            component = {next(iter(remaining))}
            changed = True
            
            while changed:
                changed = False
                to_add = set()
                
                for cluster in remaining:
                    for existing in component:
                        if cluster & existing:
                            to_add.add(cluster)
                            break
                
                if to_add:
                    component.update(to_add)
                    remaining -= to_add
                    changed = True
            
            components.append(component)
        
        return components
    
    def display(self):
        """Display all clusters"""
        print("=" * 50)
        print("CLUSTERS")
        print("=" * 50)
        
        for i, cluster in enumerate(sorted(self.clusters, key=len, reverse=True), 1):
            print(f"Cluster {i}: {cluster} (size: {len(cluster)})")
        
        print("=" * 50)

# Usage
cm = ClusterManager()

# Add clusters
cm.add_cluster([1, 2, 3])
cm.add_cluster([4, 5, 6])
cm.add_cluster([7, 8, 9])
cm.add_cluster([2, 3, 4])  # Overlapping cluster
cm.add_cluster([10, 11])

cm.display()

# Find cluster containing element
element = 5
cluster = cm.find_cluster_containing(element)
print(f"\nCluster containing {element}: {cluster}")

# Get cluster sizes
print(f"\nCluster sizes: {cm.get_cluster_sizes()}")

# Merge clusters
if len(cm.clusters) >= 2:
    clusters = list(cm.clusters)
    merged = cm.merge_clusters(clusters[0], clusters[1])
    print(f"\nMerged: {merged}")

cm.display()
```

### Example 3: Permission Groups (Immutable)

```python
class PermissionSystem:
    def __init__(self):
        self.user_permissions = {}  # user -> frozenset of permissions
        self.role_permissions = {}  # role -> frozenset of permissions
        self.user_roles = {}        # user -> frozenset of roles
    
    def add_role(self, role_name, permissions):
        """Add a role with immutable permissions"""
        self.role_permissions[role_name] = frozenset(permissions)
    
    def assign_role(self, user, role):
        """Assign role to user"""
        if role not in self.role_permissions:
            print(f"Role '{role}' not found")
            return
        
        if user not in self.user_roles:
            self.user_roles[user] = set()
        
        self.user_roles[user].add(role)
        self._update_user_permissions(user)
    
    def assign_roles(self, user, roles):
        """Assign multiple roles to user"""
        if user not in self.user_roles:
            self.user_roles[user] = set()
        
        self.user_roles[user].update(roles)
        self._update_user_permissions(user)
    
    def _update_user_permissions(self, user):
        """Update user's permissions based on roles"""
        if user not in self.user_roles:
            return
        
        permissions = set()
        for role in self.user_roles[user]:
            permissions.update(self.role_permissions.get(role, set()))
        
        self.user_permissions[user] = frozenset(permissions)
    
    def has_permission(self, user, permission):
        """Check if user has permission"""
        if user not in self.user_permissions:
            return False
        return permission in self.user_permissions[user]
    
    def has_any_permission(self, user, permissions):
        """Check if user has any of the permissions"""
        if user not in self.user_permissions:
            return False
        return bool(self.user_permissions[user] & frozenset(permissions))
    
    def has_all_permissions(self, user, permissions):
        """Check if user has all permissions"""
        if user not in self.user_permissions:
            return False
        return frozenset(permissions).issubset(self.user_permissions[user])
    
    def get_user_permissions(self, user):
        """Get user's permissions (immutable)"""
        return self.user_permissions.get(user, frozenset())
    
    def get_users_with_permission(self, permission):
        """Get all users with a specific permission"""
        users = set()
        for user, perms in self.user_permissions.items():
            if permission in perms:
                users.add(user)
        return frozenset(users)
    
    def generate_report(self):
        """Generate permission report"""
        print("=" * 60)
        print("PERMISSION SYSTEM REPORT")
        print("=" * 60)
        
        print("\nROLES AND PERMISSIONS:")
        for role, perms in self.role_permissions.items():
            print(f"  {role}: {perms}")
        
        print("\nUSER ROLES:")
        for user, roles in self.user_roles.items():
            print(f"  {user}: {roles}")
        
        print("\nUSER PERMISSIONS:")
        for user, perms in self.user_permissions.items():
            print(f"  {user}: {perms}")
        
        print("=" * 60)

# Usage
ps = PermissionSystem()

# Add roles
ps.add_role("admin", {"read", "write", "delete", "manage_users", "manage_roles"})
ps.add_role("editor", {"read", "write", "publish"})
ps.add_role("viewer", {"read"})
ps.add_role("moderator", {"read", "delete", "ban_users"})

# Assign roles
ps.assign_role("alice", "admin")
ps.assign_role("bob", "editor")
ps.assign_roles("charlie", ["viewer", "moderator"])
ps.assign_role("david", "viewer")

# Check permissions
print("PERMISSION CHECKS")
print("-" * 40)

users = ["alice", "bob", "charlie", "david"]
for user in users:
    print(f"\n{user.upper()}:")
    print(f"  Permissions: {ps.get_user_permissions(user)}")
    print(f"  Has 'write': {ps.has_permission(user, 'write')}")
    print(f"  Has 'delete': {ps.has_permission(user, 'delete')}")
    print(f"  Has 'manage_users': {ps.has_permission(user, 'manage_users')}")

# Advanced checks
print("\n" + "-" * 40)
print("ADVANCED CHECKS:")
print(f"Users with 'read' permission: {ps.get_users_with_permission('read')}")
print(f"Users with 'delete' permission: {ps.get_users_with_permission('delete')}")

print(f"\nDoes charlie have 'read' AND 'delete'? {ps.has_all_permissions('charlie', ['read', 'delete'])}")
print(f"Does david have 'read' OR 'write'? {ps.has_any_permission('david', ['read', 'write'])}")

# Generate report
ps.generate_report()
```

### Example 4: Graph Representation

```python
class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()  # Set of frozensets (each edge is frozenset of 2 vertices)
    
    def add_vertex(self, vertex):
        """Add a vertex"""
        self.vertices.add(vertex)
    
    def add_edge(self, v1, v2):
        """Add an edge between two vertices"""
        self.vertices.add(v1)
        self.vertices.add(v2)
        self.edges.add(frozenset([v1, v2]))
    
    def remove_edge(self, v1, v2):
        """Remove an edge"""
        self.edges.discard(frozenset([v1, v2]))
    
    def has_edge(self, v1, v2):
        """Check if edge exists"""
        return frozenset([v1, v2]) in self.edges
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        neighbors = set()
        for edge in self.edges:
            if vertex in edge:
                neighbors.update(edge - {vertex})
        return frozenset(neighbors)
    
    def degree(self, vertex):
        """Get degree of vertex"""
        return len(self.get_neighbors(vertex))
    
    def find_triangles(self):
        """Find all triangles in graph"""
        triangles = set()
        
        for edge in self.edges:
            v1, v2 = edge
            neighbors_v1 = self.get_neighbors(v1)
            neighbors_v2 = self.get_neighbors(v2)
            
            common = neighbors_v1 & neighbors_v2
            for v3 in common:
                triangle = frozenset([v1, v2, v3])
                triangles.add(triangle)
        
        return triangles
    
    def is_connected(self):
        """Check if graph is connected"""
        if not self.vertices:
            return True
        
        start = next(iter(self.vertices))
        visited = set()
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.get_neighbors(vertex))
        
        return visited == self.vertices
    
    def get_components(self):
        """Get connected components"""
        components = []
        remaining = set(self.vertices)
        
        while remaining:
            start = next(iter(remaining))
            component = set()
            stack = [start]
            
            while stack:
                vertex = stack.pop()
                if vertex not in component:
                    component.add(vertex)
                    stack.extend(self.get_neighbors(vertex))
            
            components.append(frozenset(component))
            remaining -= component
        
        return components
    
    def display(self):
        """Display graph"""
        print("=" * 50)
        print("GRAPH")
        print("=" * 50)
        print(f"Vertices: {self.vertices}")
        print(f"Edges: {self.edges}")
        print(f"Number of vertices: {len(self.vertices)}")
        print(f"Number of edges: {len(self.edges)}")
        
        if self.vertices:
            print(f"\nDegree of vertices:")
            for v in sorted(self.vertices):
                print(f"  {v}: {self.degree(v)}")
        
        triangles = self.find_triangles()
        if triangles:
            print(f"\nTriangles: {len(triangles)}")
            for triangle in triangles:
                print(f"  {triangle}")
        
        components = self.get_components()
        print(f"\nConnected components: {len(components)}")
        for i, comp in enumerate(components, 1):
            print(f"  Component {i}: {comp}")
        
        print(f"Graph is connected: {self.is_connected()}")
        print("=" * 50)

# Usage
g = Graph()

# Add vertices
for v in ["A", "B", "C", "D", "E"]:
    g.add_vertex(v)

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")  # Creates triangle A-B-C
g.add_edge("C", "D")
g.add_edge("D", "E")

g.display()

# Check specific edge
print(f"\nEdge between A and B: {g.has_edge('A', 'B')}")
print(f"Edge between A and D: {g.has_edge('A', 'D')}")

# Get neighbors
print(f"\nNeighbors of C: {g.get_neighbors('C')}")

# Remove edge
g.remove_edge("C", "D")
print("\nAfter removing edge C-D:")
print(f"Neighbors of C: {g.get_neighbors('C')}")
print(f"Graph is connected: {g.is_connected()}")
```

### Example 5: Document Indexing System

```python
class DocumentIndex:
    def __init__(self):
        self.index = {}  # term -> frozenset of document IDs
        self.documents = {}  # doc_id -> frozenset of terms
    
    def add_document(self, doc_id, text):
        """Add document to index"""
        # Tokenize and clean text
        words = text.lower().split()
        terms = frozenset(words)  # Unique terms in document
        
        self.documents[doc_id] = terms
        
        # Update index
        for term in terms:
            if term not in self.index:
                self.index[term] = set()
            self.index[term].add(doc_id)
        
        # Convert to frozenset for immutability
        for term in self.index:
            self.index[term] = frozenset(self.index[term])
    
    def search_exact(self, terms):
        """Search for documents containing ALL specified terms"""
        if not terms:
            return frozenset()
        
        term_set = frozenset(terms)
        result = None
        
        for term in term_set:
            docs = self.index.get(term, frozenset())
            if result is None:
                result = docs
            else:
                result &= docs
        
        return result or frozenset()
    
    def search_any(self, terms):
        """Search for documents containing ANY specified terms"""
        if not terms:
            return frozenset()
        
        result = set()
        for term in terms:
            result.update(self.index.get(term, set()))
        
        return frozenset(result)
    
    def search_without(self, terms, exclude):
        """Search for documents containing terms but not exclude"""
        include_docs = self.search_exact(terms)
        exclude_docs = self.search_any(exclude)
        
        return include_docs - exclude_docs
    
    def get_document_terms(self, doc_id):
        """Get all terms in a document"""
        return self.documents.get(doc_id, frozenset())
    
    def find_similar_documents(self, doc_id, min_similarity=0.5):
        """Find documents similar to given document"""
        if doc_id not in self.documents:
            return {}
        
        doc_terms = self.documents[doc_id]
        similarities = {}
        
        for other_id, other_terms in self.documents.items():
            if other_id == doc_id:
                continue
            
            # Jaccard similarity
            intersection = len(doc_terms & other_terms)
            union = len(doc_terms | other_terms)
            similarity = intersection / union if union > 0 else 0
            
            if similarity >= min_similarity:
                similarities[other_id] = similarity
        
        return dict(sorted(similarities.items(), key=lambda x: x[1], reverse=True))
    
    def get_term_frequency(self, term):
        """Get number of documents containing term"""
        return len(self.index.get(term, frozenset()))
    
    def get_all_terms(self):
        """Get all terms in index"""
        return frozenset(self.index.keys())
    
    def generate_report(self):
        """Generate index report"""
        print("=" * 60)
        print("DOCUMENT INDEX REPORT")
        print("=" * 60)
        print(f"Total Documents: {len(self.documents)}")
        print(f"Total Unique Terms: {len(self.index)}")
        
        # Most common terms
        term_counts = [(term, len(docs)) for term, docs in self.index.items()]
        term_counts.sort(key=lambda x: x[1], reverse=True)
        
        print("\nMost Common Terms:")
        for term, count in term_counts[:10]:
            print(f"  '{term}': {count} documents")
        
        # Document statistics
        print("\nDocument Term Counts:")
        for doc_id, terms in self.documents.items():
            print(f"  {doc_id}: {len(terms)} unique terms")
        
        print("=" * 60)

# Usage
index = DocumentIndex()

# Add documents
index.add_document(1, "Python is a great programming language for data science")
index.add_document(2, "Java is also popular for enterprise applications")
index.add_document(3, "Python and data science go together perfectly")
index.add_document(4, "JavaScript is great for web development")
index.add_document(5, "Data science uses Python, R, and many other tools")

# Search examples
print("SEARCH RESULTS")
print("=" * 40)

print("\n1. Documents containing ALL terms ['python', 'data']:")
results = index.search_exact(["python", "data"])
for doc_id in results:
    print(f"  Document {doc_id}: {index.get_document_terms(doc_id)}")

print("\n2. Documents containing ANY of ['java', 'javascript']:")
results = index.search_any(["java", "javascript"])
for doc_id in results:
    print(f"  Document {doc_id}: {index.get_document_terms(doc_id)}")

print("\n3. Documents containing 'python' but NOT 'web':")
results = index.search_without(["python"], ["web"])
for doc_id in results:
    print(f"  Document {doc_id}: {index.get_document_terms(doc_id)}")

# Similar documents
print("\n" + "=" * 40)
print("SIMILAR DOCUMENTS")
print("=" * 40)

for doc_id in [1, 2, 3]:
    similar = index.find_similar_documents(doc_id, min_similarity=0.2)
    if similar:
        print(f"\nDocument {doc_id} is similar to:")
        for other_id, sim in similar.items():
            print(f"  Document {other_id} (similarity: {sim:.2f})")

# Generate report
index.generate_report()
```

### Example 6: Configuration Manager with Immutable Sets

```python
class ConfigManager:
    def __init__(self):
        self.configs = {}  # name -> frozenset of values
        self.defaults = {}
    
    def set_config(self, name, values, is_default=False):
        """Set configuration as frozenset"""
        self.configs[name] = frozenset(values)
        if is_default:
            self.defaults[name] = frozenset(values)
    
    def get_config(self, name):
        """Get configuration (immutable)"""
        return self.configs.get(name, frozenset())
    
    def update_config(self, name, new_values):
        """Update configuration (creates new frozenset)"""
        if name in self.configs:
            self.configs[name] = frozenset(new_values)
        else:
            print(f"Config '{name}' not found")
    
    def add_to_config(self, name, value):
        """Add value to config (creates new frozenset)"""
        if name in self.configs:
            new_set = self.configs[name] | {value}
            self.configs[name] = new_set
        else:
            print(f"Config '{name}' not found")
    
    def remove_from_config(self, name, value):
        """Remove value from config (creates new frozenset)"""
        if name in self.configs:
            new_set = self.configs[name] - {value}
            self.configs[name] = new_set
        else:
            print(f"Config '{name}' not found")
    
    def reset_to_default(self, name):
        """Reset config to default"""
        if name in self.defaults:
            self.configs[name] = self.defaults[name]
        else:
            print(f"No default for '{name}'")
    
    def is_subset_of_config(self, name, values):
        """Check if values are subset of config"""
        if name not in self.configs:
            return False
        return frozenset(values).issubset(self.configs[name])
    
    def is_superset_of_config(self, name, values):
        """Check if config is superset of values"""
        if name not in self.configs:
            return False
        return self.configs[name].issuperset(frozenset(values))
    
    def get_intersection(self, name1, name2):
        """Get intersection of two configs"""
        config1 = self.configs.get(name1, frozenset())
        config2 = self.configs.get(name2, frozenset())
        return config1 & config2
    
    def get_union(self, name1, name2):
        """Get union of two configs"""
        config1 = self.configs.get(name1, frozenset())
        config2 = self.configs.get(name2, frozenset())
        return config1 | config2
    
    def get_difference(self, name1, name2):
        """Get difference of two configs (name1 - name2)"""
        config1 = self.configs.get(name1, frozenset())
        config2 = self.configs.get(name2, frozenset())
        return config1 - config2
    
    def display(self):
        """Display all configurations"""
        print("=" * 60)
        print("CONFIGURATION MANAGER")
        print("=" * 60)
        
        for name, values in self.configs.items():
            is_default = name in self.defaults and values == self.defaults[name]
            default_marker = " (DEFAULT)" if is_default else ""
            print(f"\n{name}{default_marker}:")
            print(f"  Values: {values}")
            print(f"  Count: {len(values)}")
        
        print("=" * 60)

# Usage
config = ConfigManager()

# Set configurations
config.set_config("allowed_ips", ["192.168.1.1", "192.168.1.2", "10.0.0.1"], is_default=True)
config.set_config("blocked_ips", ["10.0.0.5", "172.16.0.1"])
config.set_config("features", ["login", "signup", "search", "profile"])
config.set_config("admin_features", ["login", "profile", "admin_panel", "user_management"])

# Display initial config
config.display()

# Modify configurations
print("\nMODIFYING CONFIGURATIONS")
print("-" * 40)

config.add_to_config("allowed_ips", "192.168.1.3")
print(f"After adding IP: {config.get_config('allowed_ips')}")

config.remove_from_config("blocked_ips", "10.0.0.5")
print(f"After removing IP: {config.get_config('blocked_ips')}")

# Check relationships
print("\nRELATIONSHIP CHECKS")
print("-" * 40)

print(f"Is ['login', 'profile'] subset of features? {config.is_subset_of_config('features', ['login', 'profile'])}")
print(f"Is features superset of ['login', 'profile']? {config.is_superset_of_config('features', ['login', 'profile'])}")
print(f"Is ['admin', 'login'] subset of features? {config.is_subset_of_config('features', ['admin', 'login'])}")

# Set operations
print("\nSET OPERATIONS")
print("-" * 40)

print(f"Intersection of features and admin_features: {config.get_intersection('features', 'admin_features')}")
print(f"Union of features and admin_features: {config.get_union('features', 'admin_features')}")
print(f"Features not in admin_features: {config.get_difference('features', 'admin_features')}")
print(f"Admin features not in features: {config.get_difference('admin_features', 'features')}")

# Reset to default
print("\nRESETTING TO DEFAULT")
print("-" * 40)
config.reset_to_default("allowed_ips")
print(f"After reset: {config.get_config('allowed_ips')}")

# Final display
config.display()
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Trying to Modify Frozenset

```python
# ❌ WRONG - Frozensets are immutable
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError!
# fs.remove(1)  # AttributeError!
# fs.clear()  # AttributeError!

# ✅ CORRECT - Create new frozenset
fs = frozenset([1, 2, 3])
fs = fs | {4}  # Create new frozenset with 4 added
print(fs)  # frozenset({1, 2, 3, 4})

# Or convert to set, modify, convert back
temp_set = set(fs)
temp_set.add(4)
fs = frozenset(temp_set)
print(fs)  # frozenset({1, 2, 3, 4})
```

### Pitfall 2: Empty Frozenset Creation

```python
# ✅ CORRECT - Empty frozenset
empty = frozenset()
print(empty)  # frozenset()
print(len(empty))  # 0

# ❌ WRONG - This creates empty set, not frozenset
# empty = frozenset({})  # Works but redundant

# ✅ CORRECT - Frozenset with one element
single = frozenset([1])
print(single)  # frozenset({1})
```

### Pitfall 3: Frozenset Containing Unhashable Types

```python
# ❌ WRONG - Cannot contain mutable types
# fs = frozenset([[1, 2], [3, 4]])  # TypeError!

# ✅ CORRECT - Use frozenset for nested structures
fs = frozenset([frozenset([1, 2]), frozenset([3, 4])])
print(fs)  # frozenset({frozenset({1, 2}), frozenset({3, 4})})

# ✅ CORRECT - Use tuples for nested sequences
fs = frozenset([(1, 2), (3, 4)])
print(fs)  # frozenset({(1, 2), (3, 4)})
```

### Pitfall 4: Assuming Order Preservation

```python
# Frozensets are unordered
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 2, 1])

print(fs1 == fs2)  # True (same elements, order doesn't matter)
print(list(fs1))  # Order may vary

# ✅ CORRECT - Use sorted for predictable order
for item in sorted(fs1):
    print(item)  # Always 1, 2, 3
```

---

## ⚡ Performance Tips

### Memory Efficiency

```python
import sys

# Frozenset vs Set memory usage
my_set = set(range(1000))
my_frozenset = frozenset(range(1000))

print(f"Set memory: {sys.getsizeof(my_set)} bytes")
print(f"Frozenset memory: {sys.getsizeof(my_frozenset)} bytes")

# Frozensets are slightly more memory efficient
```

### Hashing Performance

```python
import timeit

# Frozensets are hashable, can be used as dict keys
fs = frozenset([1, 2, 3, 4, 5])
my_dict = {fs: "value"}

# Lookup is O(1)
def lookup():
    return my_dict[frozenset([1, 2, 3, 4, 5])]

time = timeit.timeit(lookup, number=100000)
print(f"Frozenset key lookup: {time:.4f}s")
```

### When to Use Frozenset vs Set

```python
# Use frozenset when:
# 1. Need immutable data structure
# 2. Need hashable object (dict keys, set elements)
# 3. Data won't change
# 4. Want to prevent accidental modification
# 5. Need to cache results

# Use set when:
# 1. Need to modify data
# 2. Don't need hashability
# 3. Performance of modifications is important
# 4. Building collection incrementally
```

---

## 📝 Practice Exercises

### Beginner Level

1. **Create Frozenset**
   ```python
   # Create frozenset from list with duplicates
   # Example: [1,2,2,3,3,3] → frozenset({1,2,3})
   ```

2. **Frozenset Operations**
   ```python
   # Perform union, intersection, difference on two frozensets
   # Example: {1,2,3} and {3,4,5} → union={1,2,3,4,5}
   ```

3. **Membership Test**
   ```python
   # Check if element exists in frozenset
   # Example: 3 in frozenset({1,2,3}) → True
   ```

### Intermediate Level

4. **Frozenset as Dictionary Key**
   ```python
   # Use frozenset as key to store data about sets
   # Example: {frozenset([1,2]): "data for {1,2}"}
   ```

5. **Set of Frozensets**
   ```python
   # Create a set containing multiple frozensets
   # Example: {frozenset([1,2]), frozenset([3,4])}
   ```

6. **Convert Set to Frozenset**
   ```python
   # Convert regular set to frozenset after modifications
   # Build set, add elements, then convert to frozenset
   ```

### Advanced Level

7. **Cache Implementation**
   ```python
   # Implement LRU cache using frozenset keys
   # Store results of expensive operations keyed by frozenset
   ```

8. **Immutable Graph**
   ```python
   # Implement graph using frozenset for edges
   # Vertices as frozenset, edges as frozenset of frozensets
   ```

9. **Configuration Versioning**
   ```python
   # Track configuration changes using frozenset
   # Store history of config states as frozensets
   ```

---

## 📚 Quick Reference Card

```python
# Creation
fs = frozenset()                 # Empty frozenset
fs = frozenset([1, 2, 3])       # From iterable
fs = frozenset({1, 2, 3})       # From set
fs = frozenset("abc")           # From string

# Methods
fs.copy()                       # Shallow copy
fs.union(other)                 # Union
fs.intersection(other)          # Intersection
fs.difference(other)            # Difference
fs.symmetric_difference(other)  # Symmetric difference
fs.issubset(other)              # Subset check
fs.issuperset(other)            # Superset check
fs.isdisjoint(other)            # Disjoint check

# Operations
fs | other                      # Union
fs & other                      # Intersection
fs - other                      # Difference
fs ^ other                      # Symmetric difference
len(fs)                         # Length
x in fs                         # Membership
x not in fs                     # Non-membership

# Properties
hash(fs)                        # Hash value (hashable)
```

## Next Step

- Go to [05_mapping_type](/05_python/02_data_types/05_mapping_type/README.md) for understanding about Mapping Data Types  

---

*Master frozensets for immutable, hashable set operations! 🐍✨*
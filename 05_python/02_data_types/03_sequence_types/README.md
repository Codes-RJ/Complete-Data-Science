# Sequence Types 📚

---

## What are Sequence Types?

Sequence types store **ordered collections** of items.

Python’s core sequence types covered here:
- **`list`** → mutable, ordered, can contain mixed types
- **`tuple`** → immutable, ordered, can be used as dict keys (if elements are hashable)
- **`range`** → memory-efficient arithmetic progression (commonly used in loops)

---

## Quick Comparison

| Type | Mutable | Ordered | Syntax | Example |
|------|---------|---------|--------|---------|
| `list` | ✅ Yes | ✅ Yes | `[]` | `[1, 2, 3]` |
| `tuple` | ❌ No | ✅ Yes | `()` | `(1, 2, 3)` |
| `range` | ❌ No | ✅ Yes | `range()` | `range(1, 6)` |

---

## Files in This Folder 📁

| File | Focus |
|------|-------|
| `01_lists.py` | list creation, indexing, slicing, methods |
| `02_tuples.py` | tuple packing/unpacking, immutability, use cases |
| `03_ranges.py` | range, step, slicing, membership |
| `exercises.md` | practice |

---

## Run

```bash
python 01_lists.py
python 02_tuples.py
python 03_ranges.py
```

---

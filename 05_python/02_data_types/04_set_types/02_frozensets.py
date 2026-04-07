"""
Frozen sets in Python (`frozenset`) ❄️

`frozenset` is an immutable version of `set`.
Because it is immutable, it can be used as:
- dictionary keys
- elements inside another set

Run:
    python 02_frozensets.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating frozensets")
    fs1 = frozenset([1, 2, 2, 3])
    fs2 = frozenset({"a", "b", "c"})
    print("fs1 =", fs1)
    print("fs2 =", fs2)

    # Expected:
    # fs1 = frozenset({1, 2, 3})


def demo_immutability() -> None:
    section("2) Immutability")
    fs = frozenset([1, 2, 3])
    print("fs =", fs)
    try:
        fs.add(4)  # type: ignore[attr-defined]
    except AttributeError as e:
        print("Cannot add to frozenset:", e)


def demo_operations() -> None:
    section("3) Operations (same as set)")
    a = frozenset([1, 2, 3, 4])
    b = frozenset([3, 4, 5])
    print("a | b =", a | b)
    print("a & b =", a & b)
    print("a - b =", a - b)
    print("a ^ b =", a ^ b)


def demo_as_dict_key() -> None:
    section("4) frozenset as dict key")
    permissions = {
        frozenset({"read"}): "viewer",
        frozenset({"read", "write"}): "editor",
        frozenset({"read", "write", "delete"}): "admin",
    }
    key = frozenset({"read", "write"})
    print("role for", key, "=", permissions[key])

    # Expected:
    # role for frozenset({'read', 'write'}) = editor


def demo_set_of_frozensets() -> None:
    section("5) set of frozensets")
    groups = {
        frozenset({1, 2}),
        frozenset({2, 3}),
        frozenset({1, 2}),  # duplicate, ignored
    }
    print("groups =", groups)


def main() -> None:
    demo_creation()
    demo_immutability()
    demo_operations()
    demo_as_dict_key()
    demo_set_of_frozensets()


if __name__ == "__main__":
    main()

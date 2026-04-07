"""
Booleans in Python (`bool`) ✅❌

Run:
    python booleans.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_basic() -> None:
    section("1) Basic bool values")
    print(True, type(True))
    print(False, type(False))


def demo_comparisons() -> None:
    section("2) Comparisons return bool")
    print("10 > 5  =", 10 > 5)      # True
    print("10 == 5 =", 10 == 5)     # False
    print("3 != 3  =", 3 != 3)      # False


def demo_logical_ops() -> None:
    section("3) Logical operators: and/or/not")
    a = True
    b = False
    print("a and b =", a and b)  # False
    print("a or b  =", a or b)   # True
    print("not a   =", not a)    # False

    # Short-circuiting demo:
    print("\nShort-circuiting:")
    print("False and (1/0) never evaluates second part")
    print("True or (1/0) never evaluates second part")


def demo_truthiness() -> None:
    section("4) Truthy vs falsy")
    values = [0, 1, 0.0, 0.1, "", "0", [], [0], {}, {"a": 1}, None]
    for v in values:
        print(f"{repr(v):>8} -> bool = {bool(v)}")

    # Expected (key lines):
    # 0 -> False
    # "0" -> True
    # [] -> False


def demo_bool_is_int() -> None:
    section("5) bool is a subclass of int (important)")
    print("isinstance(True, int) =", isinstance(True, int))  # True
    print("True + True + False =", True + True + False)      # 2
    print("int(True) =", int(True))                          # 1
    print("int(False) =", int(False))                        # 0


def demo_common_pitfalls() -> None:
    section("6) Common pitfalls")
    # Pitfall: using '==' with None
    x = None
    print("x is None:", x is None)    # recommended
    print("x == None:", x == None)    # works, but not recommended style

    # Pitfall: chained comparisons
    n = 7
    print("1 < n < 10 =", 1 < n < 10)  # True (Python supports chaining)

    # Pitfall: empty strings/lists in if
    s = ""
    if not s:
        print("Empty string is falsy")


def main() -> None:
    demo_basic()
    demo_comparisons()
    demo_logical_ops()
    demo_truthiness()
    demo_bool_is_int()
    demo_common_pitfalls()


if __name__ == "__main__":
    main()

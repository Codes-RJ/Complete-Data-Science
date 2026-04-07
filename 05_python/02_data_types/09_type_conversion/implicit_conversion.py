"""
Implicit type conversion 🔄

Python does some automatic conversions, mostly with numbers.

Run:
    python implicit_conversion.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_numeric_promotion() -> None:
    section("1) Numeric promotion (int -> float)")
    a = 5      # int
    b = 2.0    # float
    c = a + b  # float
    print("a =", a, type(a))
    print("b =", b, type(b))
    print("c = a + b =", c, type(c))

    # Expected:
    # c = a + b = 7.0 <class 'float'>


def demo_division() -> None:
    section("2) Division always returns float")
    print("5 / 2 =", 5 / 2)     # 2.5
    print("5 // 2 =", 5 // 2)   # 2 (floor division)


def demo_bool_as_int() -> None:
    section("3) bool behaves like int in arithmetic")
    print("True + 2 =", True + 2)     # 3
    print("False + 2 =", False + 2)   # 2


def demo_why_no_implicit_str_number() -> None:
    section("4) No implicit conversion between str and number")
    try:
        print("5" + 3)  # TypeError
    except TypeError as e:
        print("TypeError:", e)

    print("Correct:", int("5") + 3)


def demo_complex_promotion() -> None:
    section("5) int/float -> complex when mixed")
    z = 2 + 3j
    x = 5
    y = 2.5
    print("z + x =", z + x, type(z + x))
    print("z + y =", z + y, type(z + y))


def main() -> None:
    demo_numeric_promotion()
    demo_division()
    demo_bool_as_int()
    demo_why_no_implicit_str_number()
    demo_complex_promotion()


if __name__ == "__main__":
    main()

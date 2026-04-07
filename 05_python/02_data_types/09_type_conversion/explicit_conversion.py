"""
Explicit type conversion 🔄

Run:
    python explicit_conversion.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_numbers() -> None:
    section("1) Converting to int / float")
    print("int('123') =", int("123"))
    print("float('123.45') =", float("123.45"))
    print("int(123.99) =", int(123.99))  # truncates toward 0
    print("int(-123.99) =", int(-123.99))

    # Expected:
    # int(123.99) = 123
    # int(-123.99) = -123


def demo_bool() -> None:
    section("2) Converting to bool (truthiness)")
    values = [0, 1, "", "0", [], [0], {}, {"a": 1}, None]
    for v in values:
        print(f"{repr(v):>8} -> {bool(v)}")


def demo_str() -> None:
    section("3) Converting to str")
    n = 42
    pi = 3.14159
    print("str(42) =", str(n))
    print("str(3.14159) =", str(pi))


def demo_list_tuple_set() -> None:
    section("4) list / tuple / set conversions")
    s = "abcd"
    print("list('abcd') =", list(s))
    print("tuple('abcd') =", tuple(s))
    print("set('abca') =", set("abca"))  # duplicates removed

    r = range(5)
    print("list(range(5)) =", list(r))


def demo_dict_conversions() -> None:
    section("5) Dict conversions")
    d = {"a": 1, "b": 2}
    print("list(d) =", list(d))                # keys
    print("list(d.keys()) =", list(d.keys()))
    print("list(d.values()) =", list(d.values()))
    print("list(d.items()) =", list(d.items()))

    pairs = [("x", 10), ("y", 20)]
    print("dict(pairs) =", dict(pairs))


def demo_errors() -> None:
    section("6) Common conversion errors")
    examples = ["12", "12.3", "abc", ""]
    for x in examples:
        try:
            print("int(", repr(x), ") =", int(x))
        except ValueError as e:
            print("int(", repr(x), ") -> ValueError:", e)


def main() -> None:
    demo_numbers()
    demo_bool()
    demo_str()
    demo_list_tuple_set()
    demo_dict_conversions()
    demo_errors()


if __name__ == "__main__":
    main()

"""
Tuples in Python (`tuple`) 📦

Tuples are:
- ordered
- immutable
- often used for fixed collections and multiple return values

Run:
    python 02_tuples.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating tuples")
    t1 = (1, 2, 3)
    t2 = 1, 2, 3          # parentheses optional (tuple packing)
    t3 = (42,)            # single element tuple needs a trailing comma
    t4 = tuple([1, 2, 3]) # from list

    print("t1 =", t1)
    print("t2 =", t2)
    print("t3 =", t3)
    print("t4 =", t4)

    # Expected:
    # t3 = (42,)


def demo_index_slice() -> None:
    section("2) Indexing and slicing")
    t = ("a", "b", "c", "d")
    print("t =", t)
    print("t[0] =", t[0])
    print("t[-1] =", t[-1])
    print("t[1:3] =", t[1:3])


def demo_immutability() -> None:
    section("3) Immutability")
    t = (1, 2, 3)
    try:
        t[0] = 99  # type: ignore[misc]
    except TypeError as e:
        print("Cannot modify tuple:", e)


def demo_unpacking() -> None:
    section("4) Unpacking")
    point = (10, 20)
    x, y = point
    print("point =", point)
    print("x =", x, "y =", y)

    values = (1, 2, 3, 4, 5)
    a, b, *rest = values
    print("a =", a, "b =", b, "rest =", rest)


def demo_tuple_as_key() -> None:
    section("5) Tuples as dict keys (hashable if elements are hashable)")
    locations = {
        (0, 0): "origin",
        (1, 2): "point A",
    }
    print("locations[(1, 2)] =", locations[(1, 2)])

    # Expected:
    # locations[(1, 2)] = point A


def main() -> None:
    demo_creation()
    demo_index_slice()
    demo_immutability()
    demo_unpacking()
    demo_tuple_as_key()


if __name__ == "__main__":
    main()

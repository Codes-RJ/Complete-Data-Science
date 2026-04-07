"""
Lists in Python (`list`) 🧺

Lists are:
- ordered
- mutable
- can store mixed types

Run:
    python 01_lists.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating lists")
    a = [1, 2, 3]
    b = list("abc")
    c = []  # empty list
    d = [1, "two", 3.0, True]

    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

    # Expected:
    # a = [1, 2, 3]
    # b = ['a', 'b', 'c']


def demo_index_slice() -> None:
    section("2) Indexing and slicing")
    nums = [10, 20, 30, 40, 50]
    print("nums =", nums)
    print("nums[0] =", nums[0])       # 10
    print("nums[-1] =", nums[-1])     # 50
    print("nums[1:4] =", nums[1:4])   # [20, 30, 40]
    print("nums[::2] =", nums[::2])   # [10, 30, 50]
    print("nums[::-1] =", nums[::-1]) # reversed


def demo_mutability() -> None:
    section("3) Mutability (in-place changes)")
    nums = [1, 2, 3]
    print("before:", nums)
    nums[0] = 99
    nums.append(4)
    print("after :", nums)

    # Expected:
    # before: [1, 2, 3]
    # after : [99, 2, 3, 4]


def demo_methods() -> None:
    section("4) Common list methods")
    items = ["a", "b", "c"]
    print("start:", items)
    items.append("d")
    print("append:", items)
    items.extend(["e", "f"])
    print("extend:", items)
    items.insert(1, "X")
    print("insert:", items)

    popped = items.pop()
    print("pop() ->", popped, "| now:", items)

    items.remove("b")
    print("remove('b'):", items)

    print("count('a'):", items.count("a"))
    print("index('c'):", items.index("c"))

    items.sort()
    print("sort():", items)
    items.reverse()
    print("reverse():", items)


def demo_copying() -> None:
    section("5) Copying: reference vs copy")
    a = [1, 2, 3]
    b = a          # reference (same object)
    c = a.copy()   # shallow copy (new list)

    b.append(4)
    c.append(5)

    print("a =", a)  # changed via b
    print("b =", b)
    print("c =", c)  # independent

    # Expected:
    # a = [1, 2, 3, 4]
    # c = [1, 2, 3, 5]


def demo_unpacking() -> None:
    section("6) Unpacking")
    values = [10, 20, 30, 40]
    a, b, *rest = values
    print("values =", values)
    print("a =", a, "b =", b, "rest =", rest)

    # Expected:
    # a = 10 b = 20 rest = [30, 40]


def main() -> None:
    demo_creation()
    demo_index_slice()
    demo_mutability()
    demo_methods()
    demo_copying()
    demo_unpacking()


if __name__ == "__main__":
    main()

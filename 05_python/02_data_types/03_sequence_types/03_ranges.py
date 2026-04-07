"""
Ranges in Python (`range`) 🧮

`range` represents an arithmetic progression and is memory efficient.

Run:
    python 03_ranges.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating ranges")
    r1 = range(5)         # 0..4
    r2 = range(2, 10)     # 2..9
    r3 = range(1, 10, 2)  # 1,3,5,7,9

    print("r1 =", r1)
    print("list(r1) =", list(r1))
    print("list(r2) =", list(r2))
    print("list(r3) =", list(r3))

    # Expected:
    # list(r1) = [0, 1, 2, 3, 4]


def demo_membership_and_indexing() -> None:
    section("2) Membership, indexing, slicing")
    r = range(0, 20, 2)  # evens
    print("list(r) =", list(r))
    print("10 in r ?", 10 in r)  # True
    print("11 in r ?", 11 in r)  # False
    print("r[0] =", r[0])        # 0
    print("r[-1] =", r[-1])      # 18
    print("r[2:6] =", list(r[2:6]))  # slice returns another range


def demo_common_use() -> None:
    section("3) Common use in loops")
    total = 0
    for i in range(1, 6):
        total += i
    print("sum 1..5 =", total)

    # Expected:
    # sum 1..5 = 15


def main() -> None:
    demo_creation()
    demo_membership_and_indexing()
    demo_common_use()


if __name__ == "__main__":
    main()

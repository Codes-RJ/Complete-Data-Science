"""
Sets in Python (`set`) 🧺

Sets store unique values (no duplicates) and support set operations.

Run:
    python 01_sets.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating sets")
    a = {1, 2, 3, 3, 2}
    b = set([1, 2, 2, 3])
    empty_dict = {}
    empty_set = set()

    print("a =", a)
    print("b =", b)
    print("type({}) =", type(empty_dict))
    print("empty_set =", empty_set, "| type =", type(empty_set))

    # Expected (order may differ):
    # a = {1, 2, 3}
    # type({}) = <class 'dict'>


def demo_membership() -> None:
    section("2) Membership (fast)")
    fruits = {"apple", "banana", "cherry"}
    print("'banana' in fruits ?", "banana" in fruits)  # True
    print("'mango' in fruits ?", "mango" in fruits)    # False


def demo_add_remove() -> None:
    section("3) Add / remove")
    s = {1, 2, 3}
    print("start:", s)
    s.add(4)
    print("add(4):", s)
    s.update([5, 6, 6])
    print("update([5, 6, 6]):", s)

    s.remove(2)     # error if missing
    print("remove(2):", s)
    s.discard(999)  # no error if missing
    print("discard(999):", s)
    popped = s.pop()  # removes an arbitrary element
    print("pop() ->", popped, "| now:", s)


def demo_set_operations() -> None:
    section("4) Set operations")
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("a =", a)
    print("b =", b)
    print("union (a | b) =", a | b)
    print("intersection (a & b) =", a & b)
    print("difference (a - b) =", a - b)
    print("symmetric difference (a ^ b) =", a ^ b)

    # Expected (order may differ):
    # intersection = {3, 4}


def demo_subset_superset() -> None:
    section("5) Subset / superset")
    a = {1, 2, 3}
    b = {1, 2, 3, 4, 5}
    print("a <= b ?", a <= b)  # subset
    print("b >= a ?", b >= a)  # superset
    print("a < b ?", a < b)    # proper subset


def demo_common_use_case() -> None:
    section("6) Remove duplicates from a list")
    nums = [1, 2, 2, 3, 3, 3, 4]
    unique = set(nums)
    print("nums   =", nums)
    print("unique =", unique)
    print("sorted unique =", sorted(unique))

    # Expected:
    # unique = {1, 2, 3, 4} (order may differ)


def main() -> None:
    demo_creation()
    demo_membership()
    demo_add_remove()
    demo_set_operations()
    demo_subset_superset()
    demo_common_use_case()


if __name__ == "__main__":
    main()

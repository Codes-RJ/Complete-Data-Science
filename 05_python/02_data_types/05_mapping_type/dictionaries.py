"""
Dictionaries in Python (`dict`) 🗂️

This script covers:
- creating dictionaries
- reading and updating values
- safe access patterns
- iterating through keys/values/items
- common dictionary patterns

Run:
    python dictionaries.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating dictionaries")
    d1 = {"name": "Ava", "age": 20}
    d2 = dict(name="RJ", city="Delhi")
    d3 = dict([("a", 1), ("b", 2)])
    d4 = {}  # empty dict

    print("d1 =", d1)
    print("d2 =", d2)
    print("d3 =", d3)
    print("d4 =", d4)

    # Expected:
    # d1 = {'name': 'Ava', 'age': 20}


def demo_access_update() -> None:
    section("2) Access and update")
    person = {"name": "Ava", "age": 20}
    print("person['name'] =", person["name"])

    # safe get (no KeyError)
    print("person.get('city') =", person.get("city"))  # None
    print("person.get('city', 'NA') =", person.get("city", "NA"))

    # update / add new key
    person["city"] = "Mumbai"
    person["age"] = 21
    print("updated person =", person)


def demo_membership() -> None:
    section("3) Membership (keys)")
    d = {"a": 1, "b": 2}
    print("'a' in d ?", "a" in d)   # True (checks keys)
    print("'x' in d ?", "x" in d)   # False


def demo_iteration() -> None:
    section("4) Iteration")
    d = {"name": "Ava", "age": 20, "city": "Pune"}
    print("keys:")
    for k in d:
        print(" ", k)

    print("values:")
    for v in d.values():
        print(" ", v)

    print("items:")
    for k, v in d.items():
        print(f"  {k} -> {v}")


def demo_common_patterns() -> None:
    section("5) Common patterns")
    # counting frequency
    text = "banana"
    freq: dict[str, int] = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    print("freq for 'banana' =", freq)

    # dict comprehension
    squares = {n: n * n for n in range(1, 6)}
    print("squares =", squares)

    # merging dictionaries (Python 3.9+)
    a = {"x": 1, "y": 2}
    b = {"y": 999, "z": 3}
    merged = a | b
    print("merged (a | b) =", merged)

    # Expected:
    # merged (a | b) = {'x': 1, 'y': 999, 'z': 3}


def demo_nested_dict() -> None:
    section("6) Nested dictionaries")
    student = {
        "name": "Ava",
        "marks": {"math": 90, "science": 95},
    }
    print("student =", student)
    print("math marks =", student["marks"]["math"])


def main() -> None:
    demo_creation()
    demo_access_update()
    demo_membership()
    demo_iteration()
    demo_common_patterns()
    demo_nested_dict()


if __name__ == "__main__":
    main()

"""
Dictionary methods (`dict` methods) 🧰

Run:
    python dict_methods.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_get_setdefault() -> None:
    section("1) get() and setdefault()")
    d = {"a": 1, "b": 2}
    print("d.get('a') =", d.get("a"))                 # 1
    print("d.get('x') =", d.get("x"))                 # None
    print("d.get('x', 0) =", d.get("x", 0))           # 0

    # setdefault: returns value; inserts key if missing
    print("setdefault('c', 3) ->", d.setdefault("c", 3))
    print("now d =", d)


def demo_update_merge() -> None:
    section("2) update() and merge")
    d = {"a": 1, "b": 2}
    d.update({"b": 999, "c": 3})
    print("after update:", d)

    a = {"x": 1}
    b = {"x": 2, "y": 3}
    print("a | b =", a | b)  # merge (Python 3.9+)


def demo_pop_popitem_clear() -> None:
    section("3) pop(), popitem(), clear()")
    d = {"a": 1, "b": 2, "c": 3}
    print("pop('b') ->", d.pop("b"))
    print("now:", d)

    k, v = d.popitem()  # removes last inserted item (Python 3.7+ ordering)
    print("popitem() ->", (k, v))
    print("now:", d)

    d.clear()
    print("after clear():", d)


def demo_keys_values_items() -> None:
    section("4) keys(), values(), items() views")
    d = {"name": "Ava", "age": 20}
    print("keys =", d.keys())
    print("values =", d.values())
    print("items =", d.items())

    print("\nConvert views to list:")
    print(list(d.keys()))
    print(list(d.values()))
    print(list(d.items()))


def demo_copy_fromkeys() -> None:
    section("5) copy() and fromkeys()")
    d1 = {"a": [1, 2], "b": [3, 4]}
    d2 = d1.copy()  # shallow copy
    d2["a"].append(999)
    print("d1 =", d1)
    print("d2 =", d2)

    # fromkeys creates a dict with same default value for each key
    keys = ["x", "y", "z"]
    d = dict.fromkeys(keys, 0)
    print("fromkeys:", d)


def main() -> None:
    demo_get_setdefault()
    demo_update_merge()
    demo_pop_popitem_clear()
    demo_keys_values_items()
    demo_copy_fromkeys()


if __name__ == "__main__":
    main()

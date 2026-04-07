"""
None in Python (`NoneType`) 🚫

Run:
    python none_type.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_basics() -> None:
    section("1) Basics")
    x = None
    print("x =", x)
    print("type(x) =", type(x))

    # Expected:
    # x = None
    # type(x) = <class 'NoneType'>


def demo_return_none() -> None:
    section("2) Functions can return None")

    def greet(name: str) -> None:
        print("Hello,", name)

    result = greet("Ava")
    print("result of greet =", result)

    # Expected:
    # Hello, Ava
    # result of greet = None


def demo_is_none() -> None:
    section("3) Checking None: use 'is'")
    x = None
    print("x is None =", x is None)
    print("x == None =", x == None)  # works, but not recommended style


def demo_truthiness() -> None:
    section("4) None is falsy")
    x = None
    if not x:
        print("None behaves like False in conditions")


def demo_common_pattern() -> None:
    section("5) Common pattern: default = None")

    def add_item(item: int, lst: list[int] | None = None) -> list[int]:
        if lst is None:
            lst = []
        lst.append(item)
        return lst

    print(add_item(1))
    print(add_item(2))

    # Expected:
    # [1]
    # [2]


def main() -> None:
    demo_basics()
    demo_return_none()
    demo_is_none()
    demo_truthiness()
    demo_common_pattern()


if __name__ == "__main__":
    main()

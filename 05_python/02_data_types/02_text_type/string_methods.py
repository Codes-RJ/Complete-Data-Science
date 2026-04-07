"""
String methods (`str` methods) 🧰

This script demonstrates common string methods grouped by purpose.

Run:
    python string_methods.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_cleaning() -> None:
    section("1) Cleaning / casing")
    text = "  Python is Fun!  "
    print("Original:", repr(text))
    print("strip():", repr(text.strip()))
    print("lstrip():", repr(text.lstrip()))
    print("rstrip():", repr(text.rstrip()))
    print("lower():", text.lower())
    print("upper():", text.upper())
    print("title():", text.title())
    print("capitalize():", text.capitalize())
    print("swapcase():", text.swapcase())

    # Expected (key line):
    # strip(): 'Python is Fun!'


def demo_searching() -> None:
    section("2) Searching")
    s = "banana"
    print("s =", s)
    print("'na' in s ?", "na" in s)
    print("find('na') =", s.find("na"))         # first index
    print("rfind('na') =", s.rfind("na"))       # last index
    print("index('na') =", s.index("na"))       # like find but raises if not found
    print("count('a') =", s.count("a"))
    print("startswith('ba') =", s.startswith("ba"))
    print("endswith('na') =", s.endswith("na"))

    # Expected:
    # find('na') = 2
    # rfind('na') = 4


def demo_split_join_replace() -> None:
    section("3) split / join / replace")
    text = "one,two,three"
    parts = text.split(",")
    print("text =", text)
    print("split(',') =", parts)
    print("join with ' | ' =", " | ".join(parts))
    print("replace two -> 2 =", text.replace("two", "2"))

    # maxsplit example
    s = "a-b-c-d"
    print("split('-', maxsplit=2) =", s.split("-", maxsplit=2))


def demo_partition() -> None:
    section("4) partition / rpartition")
    email = "user@example.com"
    left, sep, right = email.partition("@")
    print("email =", email)
    print("partition('@') ->", (left, sep, right))

    # Expected:
    # ('user', '@', 'example.com')


def demo_checks() -> None:
    section("5) is* checks")
    samples = ["123", "12.3", "abc", "ABC", "abc123", "   ", ""]
    for x in samples:
        print(
            f"{repr(x):>8} | isdigit={x.isdigit()} | isnumeric={x.isnumeric()} | "
            f"isalpha={x.isalpha()} | isalnum={x.isalnum()} | isspace={x.isspace()}"
        )

    # Note:
    # - '12.3'.isdigit() is False (because of the dot)


def demo_padding_alignment() -> None:
    section("6) Padding / alignment")
    s = "python"
    print("center(10, '-') =", s.center(10, "-"))
    print("ljust(10, '.')  =", s.ljust(10, "."))
    print("rjust(10, '.')  =", s.rjust(10, "."))
    print("zfill(10)       =", "42".zfill(10))


def demo_translate() -> None:
    section("7) translate / maketrans")
    s = "hello world"
    table = str.maketrans({"h": "H", "w": "W", "o": "0"})
    print("before:", s)
    print("after :", s.translate(table))

    # Expected:
    # Hell0 W0rld


def main() -> None:
    demo_cleaning()
    demo_searching()
    demo_split_join_replace()
    demo_partition()
    demo_checks()
    demo_padding_alignment()
    demo_translate()


if __name__ == "__main__":
    main()


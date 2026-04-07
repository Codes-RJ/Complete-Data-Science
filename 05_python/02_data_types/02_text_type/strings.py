"""
Strings in Python (`str`) 🧵

This file covers:
- creating strings (single/double/triple quotes)
- escape sequences and raw strings
- indexing and slicing
- immutability
- unicode + encoding basics

Run:
    python strings.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating strings")
    s1 = "Hello"
    s2 = 'World'
    s3 = """Multi-line
string example"""

    print("s1 =", s1, "| type =", type(s1))
    print("s2 =", s2, "| type =", type(s2))
    print("s3 =", repr(s3))

    # Expected (key lines):
    # s1 = Hello | type = <class 'str'>


def demo_escape_and_raw() -> None:
    section("2) Escape sequences and raw strings")
    path1 = "C:\\new\\test"
    path2 = r"C:\new\test"  # raw string: backslashes not treated as escapes
    quote = "He said: \"Python\""
    newline = "Line1\nLine2"

    print("path1 =", path1)
    print("path2 =", path2)
    print("quote =", quote)
    print("newline printed:")
    print(newline)

    # Expected:
    # path1 = C:\new\test
    # path2 = C:\new\test


def demo_indexing_slicing() -> None:
    section("3) Indexing and slicing")
    s = "Python"
    print("s =", s)
    print("s[0]  =", s[0])     # P
    print("s[-1] =", s[-1])    # n
    print("s[0:2] =", s[0:2])  # Py
    print("s[2:]  =", s[2:])   # thon
    print("s[:4]  =", s[:4])   # Pyth
    print("s[::2] =", s[::2])  # Pto
    print("s[::-1] =", s[::-1])  # nohtyP

    # Expected:
    # s[0]  = P
    # s[::-1] = nohtyP


def demo_immutability() -> None:
    section("4) Immutability")
    s = "Python"
    try:
        s[0] = "J"  # type: ignore[misc]
    except TypeError as e:
        print("Cannot modify a string in-place:", e)

    # Correct way: create a new string
    s2 = "J" + s[1:]
    print("New string:", s2)

    # Expected:
    # New string: Jython


def demo_unicode_and_encoding() -> None:
    section("5) Unicode and encoding")
    s = "café"
    print("s =", s)
    print("len(s) =", len(s))  # 4 characters

    b = s.encode("utf-8")
    print("utf-8 bytes =", b)
    print("len(bytes) =", len(b))  # may be > len(s)
    s_back = b.decode("utf-8")
    print("decoded back =", s_back)

    # Expected (bytes may vary by encoding):
    # utf-8 bytes = b'caf\\xc3\\xa9'


def demo_chr_ord() -> None:
    section("6) chr() and ord()")
    print("ord('A') =", ord("A"))        # 65
    print("chr(65) =", chr(65))          # A
    print("ord('₹') =", ord("₹"))        # Unicode code point


def main() -> None:
    demo_creation()
    demo_escape_and_raw()
    demo_indexing_slicing()
    demo_immutability()
    demo_unicode_and_encoding()
    demo_chr_ord()


if __name__ == "__main__":
    main()


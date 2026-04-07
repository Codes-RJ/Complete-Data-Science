"""
Bytes in Python (`bytes`) 🧪

`bytes` is an immutable sequence of integers in range 0..255.

Run:
    python 01_bytes.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creating bytes")
    b1 = b"ABC"
    b2 = bytes([65, 66, 67])  # ASCII codes
    b3 = "café".encode("utf-8")

    print("b1 =", b1)
    print("b2 =", b2)
    print("b3 (utf-8) =", b3)

    # Expected:
    # b1 = b'ABC'
    # b2 = b'ABC'


def demo_indexing() -> None:
    section("2) Indexing and slicing")
    b = b"Hello"
    print("b =", b)
    print("b[0] =", b[0])          # 72 (int)
    print("b[1:4] =", b[1:4])      # b'ell'

    # Expected:
    # b[0] = 72


def demo_immutability() -> None:
    section("3) Immutability")
    b = b"ABC"
    try:
        b[0] = 90  # type: ignore[misc]
    except TypeError as e:
        print("Cannot modify bytes:", e)


def demo_decode() -> None:
    section("4) Decoding bytes to str")
    b = "नमस्ते".encode("utf-8")
    s = b.decode("utf-8")
    print("bytes =", b)
    print("decoded =", s)


def demo_common_methods() -> None:
    section("5) Common bytes methods")
    b = b"hello world"
    print("upper() =", b.upper())
    print("replace(b'world', b'python') =", b.replace(b"world", b"python"))
    print("split() =", b.split())
    print("count(b'l') =", b.count(b"l"))


def main() -> None:
    demo_creation()
    demo_indexing()
    demo_immutability()
    demo_decode()
    demo_common_methods()


if __name__ == "__main__":
    main()

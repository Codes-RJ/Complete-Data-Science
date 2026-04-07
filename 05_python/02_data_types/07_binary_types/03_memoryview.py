"""
Memoryview in Python (`memoryview`) 👁️

`memoryview` provides a view into a bytes-like object without copying data.
Useful for slicing large binary data efficiently.

Run:
    python 03_memoryview.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_basic_view() -> None:
    section("1) Basic memoryview")
    b = b"abcdefghijklmnopqrstuvwxyz"
    mv = memoryview(b)
    print("type(mv) =", type(mv))
    print("mv[0] =", mv[0])          # int
    print("bytes(mv[0:5]) =", bytes(mv[0:5]))

    # Expected:
    # bytes(mv[0:5]) = b'abcde'


def demo_no_copy_slice() -> None:
    section("2) Slices share the same buffer")
    ba = bytearray(b"HELLO WORLD")
    mv = memoryview(ba)
    part = mv[0:5]  # view, not a copy

    print("before:", ba)
    part[0] = ord("h")  # modifies underlying bytearray
    print("after :", ba)

    # Expected:
    # before: bytearray(b'HELLO WORLD')
    # after : bytearray(b'hELLO WORLD')


def demo_cast() -> None:
    section("3) Casting (advanced)")
    # 4 bytes can be interpreted as different formats using cast()
    data = bytearray([1, 0, 0, 0])
    mv = memoryview(data)
    as_bytes = mv.cast("B")  # unsigned bytes
    print("as bytes:", list(as_bytes))

    # Note: casting to larger types depends on platform endianness and alignment.


def main() -> None:
    demo_basic_view()
    demo_no_copy_slice()
    demo_cast()


if __name__ == "__main__":
    main()

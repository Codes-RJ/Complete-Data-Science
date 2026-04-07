"""
Bytearray in Python (`bytearray`) 🧪

`bytearray` is like `bytes`, but mutable.

Run:
    python 02_bytearray.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation_and_edit() -> None:
    section("1) Create and edit")
    ba = bytearray(b"HELLO")
    print("start:", ba)

    # modify in-place
    ba[0] = ord("h")
    ba[-1] = ord("!")
    print("after edits:", ba)
    print("as bytes:", bytes(ba))

    # Expected:
    # start: bytearray(b'HELLO')
    # after edits: bytearray(b'hELL!')


def demo_append_extend() -> None:
    section("2) append / extend")
    ba = bytearray()
    ba.append(65)            # 'A'
    ba.extend([66, 67, 68])  # 'BCD'
    print("ba =", ba)
    print("decoded =", ba.decode("ascii"))

    # Expected:
    # decoded = ABCD


def demo_remove_and_pop() -> None:
    section("3) pop / remove")
    ba = bytearray(b"abcd")
    last = ba.pop()
    print("popped:", last, "chr:", chr(last))
    print("now:", ba)


def demo_common_use_case() -> None:
    section("4) Common use: editing bytes data")
    data = bytearray(b"\x00\x01\x02\x03")
    print("before:", data)
    for i in range(len(data)):
        data[i] = (data[i] + 10) % 256
    print("after :", data)


def main() -> None:
    demo_creation_and_edit()
    demo_append_extend()
    demo_remove_and_pop()
    demo_common_use_case()


if __name__ == "__main__":
    main()

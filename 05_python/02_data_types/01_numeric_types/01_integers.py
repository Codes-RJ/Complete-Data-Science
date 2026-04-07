"""
Integers in Python (`int`) 🔢

Python integers:
- have **unlimited precision** (no overflow like many languages)
- support **bases** (binary/octal/hex)
- support **bitwise** operations

Run:
    python 01_integers.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_basics() -> None:
    section("1) Basics")
    a = 10
    b = -3
    big = 2**100

    print("a =", a, "| type =", type(a))
    print("b =", b, "| type =", type(b))
    print("big = 2**100 =", big)

    # Expected output (shortened):
    # a = 10 | type = <class 'int'>
    # b = -3 | type = <class 'int'>


def demo_arithmetic() -> None:
    section("2) Arithmetic Operators")
    x, y = 10, 3
    print("x + y  =", x + y)     # 13
    print("x - y  =", x - y)     # 7
    print("x * y  =", x * y)     # 30
    print("x / y  =", x / y)     # 3.333...
    print("x // y =", x // y)    # 3  (floor division)
    print("x % y  =", x % y)     # 1  (remainder)
    print("x ** y =", x ** y)    # 1000

    # Expected output:
    # x + y  = 13
    # x // y = 3
    # x % y  = 1


def demo_bases() -> None:
    section("3) Number Bases (binary, octal, hex)")
    n = 42
    print("n =", n)
    print("bin(n) =", bin(n))  # 0b101010
    print("oct(n) =", oct(n))  # 0o52
    print("hex(n) =", hex(n))  # 0x2a

    print("\nParse from strings:")
    print("int('101010', 2)  =", int("101010", 2))   # 42
    print("int('52', 8)      =", int("52", 8))       # 42
    print("int('2a', 16)     =", int("2a", 16))      # 42

    # Expected output:
    # bin(n) = 0b101010
    # int('2a', 16)     = 42


def demo_bitwise() -> None:
    section("4) Bitwise Operations")
    a = 0b1100  # 12
    b = 0b1010  # 10

    print("a =", a, "bin =", bin(a))
    print("b =", b, "bin =", bin(b))
    print("a & b  =", a & b,  "bin =", bin(a & b))   # AND
    print("a | b  =", a | b,  "bin =", bin(a | b))   # OR
    print("a ^ b  =", a ^ b,  "bin =", bin(a ^ b))   # XOR
    print("~a     =", ~a)                             # NOT
    print("a << 2 =", a << 2, "bin =", bin(a << 2))  # shift left
    print("a >> 2 =", a >> 2, "bin =", bin(a >> 2))  # shift right

    # Expected output (key lines):
    # a & b  = 8  bin = 0b1000
    # a | b  = 14 bin = 0b1110


def demo_helpers() -> None:
    section("5) Useful Built-ins")
    print("abs(-42) =", abs(-42))          # 42
    print("pow(2, 10) =", pow(2, 10))      # 1024
    print("pow(2, 10, 1000) =", pow(2, 10, 1000))  # modular exponent
    print("divmod(10, 3) =", divmod(10, 3))         # (3, 1)

    # Expected output:
    # divmod(10, 3) = (3, 1)


def demo_common_pitfalls() -> None:
    section("6) Common Pitfalls")
    print("Floor division with negatives:")
    print("-7 // 3 =", -7 // 3)  # -3 (floors toward -infinity)
    print("-7 % 3  =", -7 % 3)   # 2  (remainder keeps divisor sign)

    # Expected output:
    # -7 // 3 = -3
    # -7 % 3  = 2


def main() -> None:
    demo_basics()
    demo_arithmetic()
    demo_bases()
    demo_bitwise()
    demo_helpers()
    demo_common_pitfalls()


if __name__ == "__main__":
    main()


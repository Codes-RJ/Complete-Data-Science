"""
Complex numbers in Python (`complex`) 🧿

Complex numbers are written as:
    a + bj
where:
    a = real part
    b = imaginary part
    j = sqrt(-1)

Run:
    python 03_complex_numbers.py
"""

from __future__ import annotations

import cmath


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_creation() -> None:
    section("1) Creation")
    z1 = 2 + 3j
    z2 = complex(1, -4)  # 1 - 4j
    z3 = complex("2+5j")

    print("z1 =", z1, "| type =", type(z1))
    print("z2 =", z2)
    print("z3 =", z3)

    # Expected:
    # z1 = (2+3j) | type = <class 'complex'>


def demo_parts() -> None:
    section("2) Parts and conjugate")
    z = 3 - 4j
    print("z =", z)
    print("real =", z.real)                 # 3.0
    print("imag =", z.imag)                 # -4.0
    print("conjugate =", z.conjugate())     # 3+4j
    print("|z| (magnitude) =", abs(z))      # 5.0

    # Expected:
    # |z| (magnitude) = 5.0


def demo_arithmetic() -> None:
    section("3) Arithmetic")
    z1 = 2 + 3j
    z2 = 1 - 4j
    print("z1 + z2 =", z1 + z2)
    print("z1 * z2 =", z1 * z2)
    print("z1 / z2 =", z1 / z2)


def demo_cmath() -> None:
    section("4) cmath (complex math)")
    z = 1 + 1j
    print("z =", z)
    print("phase(z) =", cmath.phase(z))  # angle in radians
    print("polar(z) =", cmath.polar(z))  # (r, phi)
    print("rect(r, phi) from polar =", cmath.rect(*cmath.polar(z)))
    print("sqrt(-1) =", cmath.sqrt(-1))
    print("exp(i*pi) =", cmath.exp(1j * cmath.pi))

    # Expected (approx):
    # sqrt(-1) = 1j
    # exp(i*pi) = (-1+1.2246467991473532e-16j)


def main() -> None:
    demo_creation()
    demo_parts()
    demo_arithmetic()
    demo_cmath()


if __name__ == "__main__":
    main()


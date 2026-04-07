"""
Floats in Python (`float`) 🌊

Python floats are IEEE-754 double precision numbers.
That means some decimal values cannot be represented exactly.

Run:
    python 02_floats.py
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import math


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_basics() -> None:
    section("1) Basics")
    x = 3.14
    y = 1.0 / 3.0
    print("x =", x, "| type =", type(x))
    print("y = 1/3 =", y)

    # Expected:
    # x = 3.14 | type = <class 'float'>


def demo_precision_issue() -> None:
    section("2) Precision Issues")
    a = 0.1 + 0.2
    print("0.1 + 0.2 =", a)
    print("(0.1 + 0.2) == 0.3 ?", a == 0.3)

    # Expected (typical):
    # 0.1 + 0.2 = 0.30000000000000004
    # (0.1 + 0.2) == 0.3 ? False


def demo_comparisons() -> None:
    section("3) Comparing floats safely")
    a = 0.1 + 0.2
    b = 0.3
    print("abs(a-b) =", abs(a - b))
    print("math.isclose(a, b) =", math.isclose(a, b))
    print("math.isclose(a, b, rel_tol=1e-12) =", math.isclose(a, b, rel_tol=1e-12))

    # Expected:
    # math.isclose(a, b) = True


def demo_rounding_and_formatting() -> None:
    section("4) Rounding and formatting")
    value = 12.34567
    print("round(value, 2) =", round(value, 2))  # 12.35
    print("f-string 2 decimals:", f"{value:.2f}")
    print("f-string commas:", f"{12345.6789:,.2f}")  # 12,345.68
    print("scientific:", f"{value:.3e}")

    # Expected:
    # round(value, 2) = 12.35
    # f-string commas: 12,345.68


def demo_special_values() -> None:
    section("5) Special float values: inf and nan")
    inf = float("inf")
    neg_inf = float("-inf")
    nan = float("nan")

    print("inf >", 1e308, "?", inf > 1e308)
    print("neg_inf <", -1e308, "?", neg_inf < -1e308)
    print("nan == nan ?", nan == nan)  # always False
    print("math.isnan(nan) =", math.isnan(nan))

    # Expected:
    # nan == nan ? False
    # math.isnan(nan) = True


def demo_decimal_for_money() -> None:
    section("6) Decimal (better for currency-like exact decimals)")
    getcontext().prec = 28
    a = Decimal("0.1")
    b = Decimal("0.2")
    print("Decimal('0.1') + Decimal('0.2') =", a + b)
    print("Is it exactly Decimal('0.3')?", (a + b) == Decimal("0.3"))

    # Expected:
    # Decimal('0.1') + Decimal('0.2') = 0.3
    # Is it exactly Decimal('0.3')? True


def main() -> None:
    demo_basics()
    demo_precision_issue()
    demo_comparisons()
    demo_rounding_and_formatting()
    demo_special_values()
    demo_decimal_for_money()


if __name__ == "__main__":
    main()


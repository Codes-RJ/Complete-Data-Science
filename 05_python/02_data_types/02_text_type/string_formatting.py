"""
String formatting in Python 🧾

Covers:
- f-strings (best for modern Python)
- str.format()
- % formatting (legacy)
- alignment, width, precision, commas

Run:
    python string_formatting.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demo_fstrings() -> None:
    section("1) f-strings")
    name = "Ava"
    score = 93.4567
    print(f"Hello, {name}!")
    print(f"Score: {score:.2f}")
    print(f"Upper: {name.upper()}")
    print(f"Math inside: 5 * 7 = {5 * 7}")

    # Expected:
    # Hello, Ava!
    # Score: 93.46


def demo_format() -> None:
    section("2) format()")
    name = "Ava"
    score = 93.4567
    print("Hello, {}!".format(name))
    print("Score: {:.2f}".format(score))
    print("Name: {n}, Score: {s:.1f}".format(n=name, s=score))


def demo_alignment() -> None:
    section("3) Alignment and width")
    for n in [1, 20, 300]:
        print(f"{n:>5} | squared = {n*n:<6}")

    # Expected:
    #     1 | squared = 1
    #    20 | squared = 400


def demo_numeric_formats() -> None:
    section("4) Numeric formats")
    value = 12345.6789
    print(f"default: {value}")
    print(f"2 decimals: {value:.2f}")
    print(f"comma + 2 decimals: {value:,.2f}")
    print(f"scientific (3): {value:.3e}")
    print(f"percentage: {0.1234:.2%}")


def demo_percent_legacy() -> None:
    section("5) Percent formatting (legacy)")
    name = "Ava"
    score = 93.4567
    print("Name: %s, Score: %.2f" % (name, score))


def main() -> None:
    demo_fstrings()
    demo_format()
    demo_alignment()
    demo_numeric_formats()
    demo_percent_legacy()


if __name__ == "__main__":
    main()


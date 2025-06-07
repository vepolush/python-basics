from typing import Self


class Fraction:
    """
    Class for 'Fraction' description
    """
    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def __mul__(self, other: Self):
        new_fraction_a = self.a * other.a
        new_fraction_b = self.b * other.b

        new_fraction = Fraction(new_fraction_a, new_fraction_b)

        return new_fraction

    def __add__(self, other: Self):
        new_fraction_a = self.a * other.b + self.b * other.a
        new_fraction_b = self.b * other.b

        new_fraction = Fraction(new_fraction_a, new_fraction_b)

        return new_fraction

    def __sub__(self, other: Self):
        new_fraction_a = self.a * other.b - self.b * other.a
        new_fraction_b = self.b * other.b

        new_fraction = Fraction(new_fraction_a, new_fraction_b)

        return new_fraction

    def __eq__(self, other: Self) -> bool:
        numerator = self.a / self.b
        denominator = other.a / other.b

        return numerator == denominator

    def __gt__(self, other: Self) -> bool:
        numerator = self.a / self.b
        denominator = other.a / other.b

        return numerator > denominator

    def __lt__(self, other: Self) -> bool:
        numerator = self.a / self.b
        denominator = other.a / other.b

        return numerator < denominator

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

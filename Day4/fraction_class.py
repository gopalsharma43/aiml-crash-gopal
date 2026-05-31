# This program demonstrates dunder methods using a Fraction class.

from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        common = gcd(self.numerator, self.denominator)

        return Fraction(
            self.numerator // common,
            self.denominator // common
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):

        new_num = (
            self.numerator * other.denominator +
            other.numerator * self.denominator
        )

        new_den = (
            self.denominator * other.denominator
        )

        return Fraction(new_num, new_den).simplify()

    def __eq__(self, other):

        f1 = self.simplify()
        f2 = other.simplify()

        return (
            f1.numerator == f2.numerator and
            f1.denominator == f2.denominator
        )

    def __lt__(self, other):

        return (
            self.numerator * other.denominator <
            other.numerator * self.denominator
        )


# Test Cases

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

print("Fraction 1:", f1)
print("Fraction 2:", f2)

print("\nAddition:")
print(f1 + f2)

print("\nEquality:")
print(Fraction(2, 4) == Fraction(1, 2))

print("\nLess Than:")
print(Fraction(1, 3) < Fraction(1, 2))
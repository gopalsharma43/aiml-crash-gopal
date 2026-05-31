# This program demonstrates a calculator using type hints.

from typing import Optional


def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """Returns division result or None if denominator is zero."""

    if b == 0:
        return None

    return a / b


def power(a: float, b: float) -> float:
    """Returns a raised to the power b."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Returns remainder."""
    return a % b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by Zero:", divide(10, 0))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))
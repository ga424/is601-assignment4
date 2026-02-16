"""Tests for arithmetic operations."""

import pytest

from app.operations import Operations


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Basic and edge cases for addition.
        (1, 1, 2),
        (-1, -1, -2),
        (5, -3, 2),
        (5, 0, 5),
        (1.5, 2.5, 4.0),
    ],
    ids=[
        "adds two positive numbers",
        "adds two negative numbers",
        "adds numbers with mixed signs",
        "adds a number and zero",
        "adds two floating point numbers",
    ],
)
def test_addition(a, b, expected):
    """Validate addition across basic cases."""
    assert Operations.addition(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Basic and edge cases for subtraction.
        (1, 1, 0),
        (-5, -3, -2),
        (5, -3, 8),
        (5, 0, 5),
        (5.5, 2.5, 3.0),
    ],
    ids=[
        "subtracts two positive numbers",
        "subtracts two negative numbers",
        "subtracts numbers with mixed signs",
        "subtracts with zero",
        "subtracts floating point numbers",
    ],
)
def test_subtraction(a, b, expected):
    """Validate subtraction across basic cases."""
    assert Operations.subtraction(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Basic and edge cases for multiplication.
        (2, 3, 6),
        (-2, -3, 6),
        (2, -3, -6),
        (5, 0, 0),
        (2.5, 4, 10.0),
    ],
    ids=[
        "multiplies two positive numbers",
        "multiplies two negative numbers",
        "multiplies numbers with mixed signs",
        "multiplies by zero",
        "multiplies floating point numbers",
    ],
)
def test_multiplication(a, b, expected):
    """Validate multiplication across basic cases."""
    assert Operations.multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Basic and edge cases for division.
        (6, 2, 3),
        (-6, -2, 3),
        (6, -2, -3),
        (5.0, 2.0, 2.5),
        (0, 5, 0),
    ],
    ids=[
        "divides two positive numbers",
        "divides two negative numbers",
        "divides numbers with mixed signs",
        "divides floating point numbers",
        "divides when numerator is zero",
    ],
)
def test_division(a, b, expected):
    """Validate division across basic cases."""
    assert Operations.division(a, b) == expected


def test_division_by_zero():
    """Ensure division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.division(1, 0)

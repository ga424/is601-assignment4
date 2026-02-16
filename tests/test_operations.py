"""Tests for arithmetic operations."""

import pytest

from app.calculation import CalculationFactory


def _create_calculation(operation: str, a: float, b: float):
    """Create a calculation using the factory."""
    return CalculationFactory.create_calculation(operation, a, b)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (4, 0.5, 2.0),
        (-2, 3, -8),
    ],
    ids=[
        "powers with positive exponent",
        "powers with zero exponent",
        "powers with fractional exponent",
        "powers with negative base",
    ],
)
def test_power(a, b, expected):
    """Validate exponentiation across basic cases."""
    calculation = _create_calculation("power", a, b)
    assert calculation.execute() == expected


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
    calculation = _create_calculation("add", a, b)
    assert calculation.execute() == expected


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
    calculation = _create_calculation("subtract", a, b)
    assert calculation.execute() == expected


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
    calculation = _create_calculation("multiply", a, b)
    assert calculation.execute() == expected


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
    calculation = _create_calculation("divide", a, b)
    assert calculation.execute() == expected


def test_division_by_zero():
    """Ensure division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = _create_calculation("divide", 1, 0)
        calculation.execute()


def test_calculation_str():
    """Verify __str__ returns a formatted calculation string."""
    calculation = _create_calculation("add", 5, 3)
    result_str = str(calculation)
    assert "AddCalculation" in result_str
    assert "5" in result_str
    assert "3" in result_str
    assert "8" in result_str


def test_calculation_repr():
    """Verify __repr__ returns a debug representation."""
    calculation = _create_calculation("multiply", 2, 4)
    repr_str = repr(calculation)
    assert "MultiplyCalculation" in repr_str
    assert "a=2" in repr_str
    assert "b=4" in repr_str


def test_unregistered_operation():
    """Ensure attempting to create an unregistered operation raises ValueError."""
    with pytest.raises(ValueError, match="is not registered"):
        CalculationFactory.create_calculation("unknown_operation", 1, 2)


def test_duplicate_registration():
    """Ensure registering the same operation twice raises ValueError."""
    with pytest.raises(ValueError, match="is already registered"):
        @CalculationFactory.register_calculation("add")
        class _DuplicateAddCalculation:  # pylint: disable=too-few-public-methods
            """Minimal duplicate for registration collision testing."""
            def __init__(self, a, b):
                self.a = a
                self.b = b

            def execute(self):
                """Return a deterministic value for test registration."""
                return self.a + self.b

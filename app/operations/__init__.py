"""Core arithmetic operations for the calculator."""


class Operations:
    """Collection of basic arithmetic operations."""

    @staticmethod
    def addition(a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Return the difference of two numbers."""
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """Return the quotient of two numbers."""
        # Guard against division by zero.
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Return a raised to the power of b."""
        return a**b

__all__ = ["Operations"]

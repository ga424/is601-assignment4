# Commenting this code as it has been re-factored to use a factory pattern
# instead of a static class for operations.

# """Core arithmetic operations for the calculator."""


# class Operations:
#     """Collection of basic arithmetic operations."""

#     @staticmethod
#     def addition(a: float, b: float) -> float:
#         """Return the sum of two numbers."""
#         return a + b

#     @staticmethod
#     def subtraction(a: float, b: float) -> float:
#         """Return the difference of two numbers."""
#         return a - b

#     @staticmethod
#     def multiplication(a: float, b: float) -> float:
#         """Return the product of two numbers."""
#         return a * b

#     @staticmethod
#     def division(a: float, b: float) -> float:
#         """Return the quotient of two numbers."""
#         # Guard against division by zero.
#         if b == 0:
#             raise ValueError("Cannot divide by zero.")
#         return a / b


# __all__ = ["Operations"]

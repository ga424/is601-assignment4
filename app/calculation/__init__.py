"""Calculation types and factory registration for the calculator."""

from abc import ABC, abstractmethod
from typing import Dict, Type
from app.operations import Operations

# These simple value-object style classes intentionally expose one public method.
# pylint: disable=too-few-public-methods


class Calculation(ABC):
    """Base class for calculators types such as add, subtract, multiply, divide."""

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        """Perform the calculation. This method must be implemented by subclasses."""

    def __str__(self) -> str:
        """Return a formatted string representation of the calculation."""
        result = self.execute()
        operation_name = self.__class__.__name__.replace("Calculation", "")
        return (
            f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"
        )

    def __repr__(self) -> str:
        """Return a detailed representation for debugging."""
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class CalculationFactory:
    """Factory for registered calculation classes."""

    # Registry of calculation types mapped to their corresponding classes.
    calculations: Dict[str, Type[Calculation]] = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """Decorator to register calculation classes by operation name."""
        calculation_type_lower = calculation_type.lower()

        def decorator(subclass: Type[Calculation]) -> Type[Calculation]:
            """Register the subclass under the normalized calculation type."""
            if calculation_type_lower in cls.calculations:
                raise ValueError(
                    f"Calculation type '{calculation_type_lower}' is already registered."
                )
            cls.calculations[calculation_type_lower] = subclass
            return subclass

        return decorator

    @classmethod
    def create_calculation(cls, operation, a: float, b: float) -> Calculation:
        """Create a calculation instance for the provided operation."""

        operation_name = getattr(operation, "name", operation)
        operation_key = str(operation_name).lower()
        calculation_class = cls.calculations.get(operation_key)

        if calculation_class is None:
            raise ValueError(
                "Calculation type "
                f"'{operation_key}' is not registered. "
                f"Available calculations: {list(cls.calculations.keys())}"
            )

        return calculation_class(a, b)


@CalculationFactory.register_calculation("add")
class AddCalculation(Calculation):
    """Addition calculation."""

    def execute(self) -> float:
        return Operations.addition(self.a, self.b)


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    """Subtraction calculation."""

    def execute(self) -> float:
        return Operations.subtraction(self.a, self.b)


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    """Multiplication calculation."""

    def execute(self) -> float:
        return Operations.multiplication(self.a, self.b)


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    """Division calculation."""

    def execute(self) -> float:
        return Operations.division(self.a, self.b)


@CalculationFactory.register_calculation("power")
class PowerCalculation(Calculation):
    """Exponentiation calculation."""

    def execute(self) -> float:
        return Operations.power(self.a, self.b)


__all__ = [
    "Calculation",
    "CalculationFactory",
    "AddCalculation",
    "SubtractCalculation",
    "MultiplyCalculation",
    "DivideCalculation",
    "PowerCalculation",
]

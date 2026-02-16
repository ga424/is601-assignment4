from abc import ABC, abstractmethod
from typing import Dict, Type


class Calculation(ABC):
    """Base class for calculators types such as add, subtract, multiply, divide."""

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        """Perform the calculation. This method must be implemented by subclasses."""

    def __str__(self) -> str:
        """Return a string representation of the calculation. Specifically, it executes the calculation and formats the result."""
        result = self.execute()
        operation_name = self.__class__.__name__.replace("Calculation", "")
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"

    def __repr__(self) -> str:
        """Return a detailed string representation of the calculation instance. Provides the class name and the values of a and b for debugging purposes."""
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class CalculationFactory:
    """Factory for registered calculation classes."""

    """Registry of calculation types mapped to their corresponding classes. 
    This is a class-level dictionary that stores the mapping of operation names (as lowercase strings) to their respective Calculation subclasses. 
    It is used by the factory methods to look up and instantiate the correct calculation class based on the operation requested. It acts like a central registry for all available calculation types, 
    allowing for dynamic creation of calculation instances without hardcoding specific classes in the factory logic."""
    
    calculations: Dict[str, Type[Calculation]] = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """Decorator to register calculation classes by operation name. 
        A decorator method that allows for the registration of Calculation subclasses under a specific operation name.
        This is helpful here for dynamically adding new calculation types without modifying the factory logic. 
        The decorator takes a string representing the calculation type (e.g., "add", "subtract") 
        and returns a decorator function that registers the decorated class in the calculations registry under 
        the lowercase version of the provided type name."""
        
        calculation_type_lower = calculation_type.lower()

        

        def decorator(subclass: Type[Calculation]) -> Type[Calculation]:
            """This inner function performs the actual registration of the subclass in the calculations registry. 
            It checks if the calculation type is already registered to prevent overwriting existing entries. 
            If the type is not already registered, it adds the subclass to the registry under the lowercase version of the calculation type name."""
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
        return self.a + self.b


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    """Subtraction calculation."""

    def execute(self) -> float:
        return self.a - self.b


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    """Multiplication calculation."""

    def execute(self) -> float:
        return self.a * self.b


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    """Division calculation."""

    def execute(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b


@CalculationFactory.register_calculation("power")
class PowerCalculation(Calculation):
    """Exponentiation calculation."""

    def execute(self) -> float:
        return self.a**self.b


__all__ = [
    "Calculation",
    "CalculationFactory",
    "AddCalculation",
    "SubtractCalculation",
    "MultiplyCalculation",
    "DivideCalculation",
    "PowerCalculation",
]



"""Calculator REPL implementation and entry point."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Callable, Dict, Tuple

from app.calculation import CalculationFactory


class Calculator:  # pylint: disable=too-few-public-methods
    """Interactive calculator that supports basic operations."""
    def __init__(
        self,
        operations: Dict[str, Callable[[float, float], float]] | None = None,
        input_func: Callable[[str], str] | None = None,
        output_func: Callable[[str], None] | None = None,
    ) -> None:
        if operations is None:
            operations = self._build_operation_registry()
        self.operations = operations
        self.input_func = input if input_func is None else input_func
        self.output_func = print if output_func is None else output_func

    def _build_operation_registry(self) -> Dict[str, Callable[[float, float], float]]:
        """Build an operations registry based on factory registrations."""
        for attribute in ("calculations", "_calculations", "_registry"):
            registry = getattr(CalculationFactory, attribute, None)
            if isinstance(registry, dict) and registry:
                return {name: None for name in registry.keys()}
        return {}

    def run(self) -> None:
        """Run the calculator REPL loop."""
        # Drive the REPL loop until exit or interruption.
        self._print_welcome()
        while True:
            try:
                user_input = self.input_func(">>> ").strip()
                if user_input.lower() == "exit":
                    self.output_func("Goodbye!")
                    break

                operation, operand1, operand2 = self._parse_input(user_input)
                result = self._execute(operation, operand1, operand2)
                self.output_func(f"{operand1} {operation} {operand2} = {result}")
            except ValueError as exc:
                self.output_func(f"Error: {exc}")
            except KeyboardInterrupt:
                self.output_func("\n\nGoodbye!")
                break
            except Exception as exc:  # pylint: disable=broad-exception-caught
                self.output_func(f"Unexpected error: {exc}")

    def _print_welcome(self) -> None:
        """Print usage instructions and available operations."""
        # Show usage instructions and available operations.
        self.output_func("Welcome to the Calculator REPL!")
        self.output_func(
            f"Available operations: {', '.join(self.operations.keys())}"
        )
        self.output_func("Usage: operation operand1 operand2")
        self.output_func("Example: add 1 1")
        self.output_func("Type 'exit' to quit.\n")

    def _parse_input(self, user_input: str) -> Tuple[str, float, float]:
        """Parse and validate user input into operation and operands."""
        # Parse and validate the user's input.
        parts = user_input.split()
        if len(parts) != 3:
            raise ValueError("Invalid format. Please provide: operation operand1 operand2")

        operation, operand1_str, operand2_str = parts
        if operation.lower() not in self.operations:
            raise ValueError(f"Unknown operation '{operation}'")

        try:
            operand1 = float(operand1_str)
            operand2 = float(operand2_str)
        except ValueError as exc:
            raise ValueError(
                f"Operands must be numbers. Got '{operand1_str}' and '{operand2_str}'"
            ) from exc

        return operation, operand1, operand2

    def _execute(self, operation: str, operand1: float, operand2: float) -> float:
        """Execute the selected operation and return the result."""
        # Dispatch to the selected operation.
        operation_key = operation.lower()
        calculation = CalculationFactory.create_calculation(
            SimpleNamespace(name=operation_key),
            operand1,
            operand2,
        )
        return calculation.execute()


def calculator() -> None:
    """
    Interactive calculator REPL that accepts operations and two operands.
    Usage: operation operand1 operand2
    Example: add 1 1
    Type 'exit' to quit.
    """
    # Provide a simple module-level entry point.
    Calculator().run()

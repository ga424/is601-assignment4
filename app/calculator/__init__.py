from __future__ import annotations

from typing import Callable, Dict, Tuple

from app.operations import Operations


class Calculator:
    def __init__(
        self,
        operations: Dict[str, Callable[[float, float], float]] | None = None,
        input_func: Callable[[str], str] | None = None,
        output_func: Callable[[str], None] | None = None,
    ) -> None:
        if operations is None:
            operations = {
                "add": Operations.addition,
                "subtract": Operations.subtraction,
                "multiply": Operations.multiplication,
                "divide": Operations.division,
            }
        self.operations = operations
        self.input_func = input if input_func is None else input_func
        self.output_func = print if output_func is None else output_func

    def run(self) -> None:
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
            except Exception as exc:
                self.output_func(f"Unexpected error: {exc}")

    def _print_welcome(self) -> None:
        # Show usage instructions and available operations.
        self.output_func("Welcome to the Calculator REPL!")
        self.output_func(
            f"Available operations: {', '.join(self.operations.keys())}"
        )
        self.output_func("Usage: operation operand1 operand2")
        self.output_func("Example: add 1 1")
        self.output_func("Type 'exit' to quit.\n")

    def _parse_input(self, user_input: str) -> Tuple[str, float, float]:
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
        except ValueError:
            raise ValueError(
                f"Operands must be numbers. Got '{operand1_str}' and '{operand2_str}'"
            )

        return operation, operand1, operand2

    def _execute(self, operation: str, operand1: float, operand2: float) -> float:
        # Dispatch to the selected operation.
        operation_key = operation.lower()
        return self.operations[operation_key](operand1, operand2)


def calculator() -> None:
    """
    Interactive calculator REPL that accepts operations and two operands.
    Usage: operation operand1 operand2
    Example: add 1 1
    Type 'exit' to quit.
    """
    # Provide a simple module-level entry point.
    Calculator().run()

import sys
from app.operations import addition, substraction, multiplication, division

def calculator():
    """
    Interactive calculator REPL that accepts operations and two operands.
    Usage: operation operand1 operand2
    Example: add 1 1
    Type 'exit' to quit.
    """
    operations = {
        'add': addition,
        'subtract': substraction,
        'multiply': multiplication,
        'divide': division,
    }
    
    print("Welcome to the Calculator REPL!")
    print("Available operations: add, subtract, multiply, divide")
    print("Usage: operation operand1 operand2")
    print("Example: add 1 1")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            # Get input from user
            user_input = input(">>> ").strip()
            
            # Check for exit command
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            # Parse input
            parts = user_input.split()
            
            # Validate input length
            if len(parts) != 3:
                print("Error: Invalid format. Please provide: operation operand1 operand2")
                print("Example: add 1 1")
                continue
            
            operation, operand1_str, operand2_str = parts
            
            # Validate operation
            if operation.lower() not in operations:
                print(f"Error: Unknown operation '{operation}'")
                print(f"Available operations: {', '.join(operations.keys())}")
                continue
            
            # Validate operands are numbers
            try:
                operand1 = float(operand1_str)
                operand2 = float(operand2_str)
            except ValueError:
                print(f"Error: Operands must be numbers. Got '{operand1_str}' and '{operand2_str}'")
                continue
            
            # Perform operation
            result = operations[operation.lower()](operand1, operand2)
            print(f"{operand1} {operation} {operand2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

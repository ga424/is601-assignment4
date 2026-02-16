import pytest
from unittest.mock import patch
from io import StringIO
from app.calculator import calculator


@pytest.mark.parametrize(
    "user_input,expected",
    [
        # Happy-path operations, including case-insensitive command and floats.
        ("add 1 1", "1.0 add 1.0 = 2.0"),
        ("subtract 5 3", "5.0 subtract 3.0 = 2.0"),
        ("multiply 2 3", "2.0 multiply 3.0 = 6.0"),
        ("divide 6 2", "6.0 divide 2.0 = 3.0"),
        ("ADD 2 3", "2.0 ADD 3.0 = 5.0"),
        ("add 1.5 2.5", "1.5 add 2.5 = 4.0"),
    ],
    ids=[
        "adds two integers",
        "subtracts two integers",
        "multiplies two integers",
        "divides two integers",
        "accepts uppercase operation input",
        "adds floating point numbers",
    ],
)
def test_calculator_basic_operations(user_input, expected):
    with patch('builtins.input', side_effect=[user_input, 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert expected in output


@pytest.mark.parametrize(
    "user_input,expected",
    [
        # Invalid inputs and error messaging.
        ("divide 1 0", "Error: Cannot divide by zero."),
        ("invalid 1 2", "Error: Unknown operation 'invalid'"),
        ("add 1 abc", "Error: Operands must be numbers"),
        ("add 1", "Error: Invalid format"),
        ("add 1 2 3", "Error: Invalid format"),
    ],
    ids=[
        "reports an error for division by zero",
        "reports an error for an unknown operation",
        "reports an error for non-numeric operands",
        "reports an error for too few arguments",
        "reports an error for too many arguments",
    ],
)
def test_calculator_error_cases(user_input, expected):
    with patch('builtins.input', side_effect=[user_input, 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert expected in output


def test_calculator_exit_command():
    # Ensure a single exit command terminates the REPL.
    with patch('builtins.input', side_effect=['exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert 'Goodbye!' in output


def test_calculator_multiple_operations():
    # Ensure the REPL processes multiple commands before exit.
    with patch('builtins.input', side_effect=['add 1 1', 'multiply 2 3', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '1.0 add 1.0 = 2.0' in output
            assert '2.0 multiply 3.0 = 7.0' in output
            assert 'Goodbye!' in output


def test_calculator_keyboard_interrupt():
    # Ensure KeyboardInterrupt exits cleanly.
    with patch('builtins.input', side_effect=KeyboardInterrupt()):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert 'Goodbye!' in output


def test_calculator_error_recovery():
    # Ensure the REPL continues after a bad command.
    with patch('builtins.input', side_effect=['add abc def', 'add 1 1', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert "Error: Operands must be numbers" in output
            assert '1.0 add 1.0 = 2.0' in output
            assert 'Goodbye!' in output


def test_calculator_unexpected_exception():
    # Ensure unexpected errors are surfaced without crashing the loop.
    with patch('builtins.input', side_effect=['add 1 1', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Mock the addition operation from app.operations to raise an unexpected error
            with patch('app.calculator.Operations.addition', side_effect=RuntimeError("Unexpected error")):
                calculator()
                output = fake_out.getvalue()
                assert "Unexpected error" in output

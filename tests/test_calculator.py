import pytest
from unittest.mock import patch
from io import StringIO
from app.calculator import calculator


def test_calculator_addition():
    """Test calculator with addition operation"""
    with patch('builtins.input', side_effect=['add 1 1', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '1.0 add 1.0 = 2.0' in output


def test_calculator_subtraction():
    """Test calculator with subtraction operation"""
    with patch('builtins.input', side_effect=['subtract 5 3', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '5.0 subtract 3.0 = 2.0' in output


def test_calculator_multiplication():
    """Test calculator with multiplication operation"""
    with patch('builtins.input', side_effect=['multiply 2 3', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '2.0 multiply 3.0 = 6.0' in output


def test_calculator_division():
    """Test calculator with division operation"""
    with patch('builtins.input', side_effect=['divide 6 2', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '6.0 divide 2.0 = 3.0' in output


def test_calculator_division_by_zero():
    """Test calculator handles division by zero"""
    with patch('builtins.input', side_effect=['divide 1 0', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert 'Error: Cannot divide by zero.' in output


def test_calculator_invalid_operation():
    """Test calculator handles invalid operation"""
    with patch('builtins.input', side_effect=['invalid 1 2', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert "Error: Unknown operation 'invalid'" in output


def test_calculator_invalid_operand():
    """Test calculator handles non-numeric operands"""
    with patch('builtins.input', side_effect=['add 1 abc', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert "Error: Operands must be numbers" in output


def test_calculator_invalid_format_too_few_args():
    """Test calculator handles too few arguments"""
    with patch('builtins.input', side_effect=['add 1', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert "Error: Invalid format" in output


def test_calculator_invalid_format_too_many_args():
    """Test calculator handles too many arguments"""
    with patch('builtins.input', side_effect=['add 1 2 3', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert "Error: Invalid format" in output


def test_calculator_exit_command():
    """Test calculator exits with 'exit' command"""
    with patch('builtins.input', side_effect=['exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert 'Goodbye!' in output


def test_calculator_case_insensitive_operations():
    """Test calculator operations are case insensitive"""
    with patch('builtins.input', side_effect=['ADD 2 3', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '2.0 ADD 3.0 = 5.0' in output


def test_calculator_multiple_operations():
    """Test calculator can perform multiple operations"""
    with patch('builtins.input', side_effect=['add 1 1', 'multiply 2 3', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '1.0 add 1.0 = 2.0' in output
            assert '2.0 multiply 3.0 = 6.0' in output
            assert 'Goodbye!' in output


def test_calculator_floating_point_operands():
    """Test calculator handles floating point numbers"""
    with patch('builtins.input', side_effect=['add 1.5 2.5', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert '1.5 add 2.5 = 4.0' in output


def test_calculator_keyboard_interrupt():
    """Test calculator handles keyboard interrupt gracefully"""
    with patch('builtins.input', side_effect=KeyboardInterrupt()):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert 'Goodbye!' in output


def test_calculator_error_recovery():
    """Test calculator continues after an error"""
    with patch('builtins.input', side_effect=['add abc def', 'add 1 1', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            calculator()
            output = fake_out.getvalue()
            assert "Error: Operands must be numbers" in output
            assert '1.0 add 1.0 = 2.0' in output
            assert 'Goodbye!' in output


def test_calculator_unexpected_exception():
    """Test calculator handles unexpected exceptions"""
    with patch('builtins.input', side_effect=['add 1 1', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Mock the addition operation from app.operations to raise an unexpected error
            with patch('app.calculator.addition', side_effect=RuntimeError("Unexpected error")):
                calculator()
                output = fake_out.getvalue()
                assert "Unexpected error" in output

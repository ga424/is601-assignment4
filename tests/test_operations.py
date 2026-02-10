import pytest
from app.operations import addition, substraction, multiplication, division


class TestAddition:
    """Test cases for addition operation"""
    
    def test_addition_positive_numbers(self):
        """Test addition of two positive numbers"""
        assert addition(1, 1) == 2
    
    def test_addition_negative_numbers(self):
        """Test addition of two negative numbers"""
        assert addition(-1, -1) == -2
    
    def test_addition_mixed_signs(self):
        """Test addition of numbers with mixed signs"""
        assert addition(5, -3) == 2
    
    def test_addition_with_zero(self):
        """Test addition with zero"""
        assert addition(5, 0) == 5
    
    def test_addition_floats(self):
        """Test addition of floating point numbers"""
        assert addition(1.5, 2.5) == 4.0


class TestSubtraction:
    """Test cases for subtraction operation"""
    
    def test_substraction_positive_numbers(self):
        """Test subtraction of two positive numbers"""
        assert substraction(1, 1) == 0
    
    def test_substraction_negative_numbers(self):
        """Test subtraction of two negative numbers"""
        assert substraction(-5, -3) == -2
    
    def test_substraction_mixed_signs(self):
        """Test subtraction of numbers with mixed signs"""
        assert substraction(5, -3) == 8
    
    def test_substraction_with_zero(self):
        """Test subtraction with zero"""
        assert substraction(5, 0) == 5
    
    def test_substraction_floats(self):
        """Test subtraction of floating point numbers"""
        assert substraction(5.5, 2.5) == 3.0


class TestMultiplication:
    """Test cases for multiplication operation"""
    
    def test_multiplication_positive_numbers(self):
        """Test multiplication of two positive numbers"""
        assert multiplication(2, 3) == 6
    
    def test_multiplication_negative_numbers(self):
        """Test multiplication of two negative numbers"""
        assert multiplication(-2, -3) == 6
    
    def test_multiplication_mixed_signs(self):
        """Test multiplication of numbers with mixed signs"""
        assert multiplication(2, -3) == -6
    
    def test_multiplication_by_zero(self):
        """Test multiplication by zero"""
        assert multiplication(5, 0) == 0
    
    def test_multiplication_floats(self):
        """Test multiplication of floating point numbers"""
        assert multiplication(2.5, 4) == 10.0


class TestDivision:
    """Test cases for division operation"""
    
    def test_division_positive_numbers(self):
        """Test division of two positive numbers"""
        assert division(6, 2) == 3
    
    def test_division_negative_numbers(self):
        """Test division of two negative numbers"""
        assert division(-6, -2) == 3
    
    def test_division_mixed_signs(self):
        """Test division of numbers with mixed signs"""
        assert division(6, -2) == -3
    
    def test_division_floats(self):
        """Test division of floating point numbers"""
        assert division(5.0, 2.0) == 2.5
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            division(1, 0)
    
    def test_division_zero_numerator(self):
        """Test division of zero"""
        assert division(0, 5) == 0

class Operations:
   
    @staticmethod
    def addition(a: float, b: float) -> float:
        # Return the sum of two numbers.
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        # Return the difference of two numbers.
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        # Return the product of two numbers.
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        # Guard against division by zero.
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


__all__ = ["Operations"]
def addition(a: float, b: float) -> float:
    return a + b

def substraction(a: float, b: float) -> float:
    return a - b

def multiplication(a:float, b: float) -> float:
    return a * b

def division(a: float, b:  float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b   
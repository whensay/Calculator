# calculator.py
class Calculator:
    def add(self, a, b):
        return round(a + b, 3)

    def subtract(self, a, b):
        return round(a - b, 3)

    def multiply(self, a, b):
        return round(a * b, 3)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零The divisor cannot be 0")
        return round(a / b, 3)

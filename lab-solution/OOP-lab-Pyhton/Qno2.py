# 2. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

# Example usage:
calculator = Calculator()

# Perform operations
print("Addition (5 + 3):", calculator.add(5, 3))
print("Subtraction (5 - 3):", calculator.subtract(5, 3))
print("Multiplication (5 * 3):", calculator.multiply(5, 3))
print("Division (5 / 3):", calculator.divide(5, 3))

# create a calculator capable of performing addition,subtraction,
# multiplication and Division operations on two numbers.
# your program should format the output in readable manner!

print("Simple Calculator")

# Input numbers and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation and print result
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Invalid operation"

print(f"The result of {num1} {operation} {num2} is: {result}")

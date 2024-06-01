# WAP to read two complex num from the user and perform their add, sub, mul, div then display the result.

# Function to read a complex number from the user
def read_complex(prompt):
    real = float(input(f"Enter the real part of {prompt}: "))
    imag = float(input(f"Enter the imaginary part of {prompt}: "))
    return complex(real, imag)

# Function to perform arithmetic operations on complex numbers
def complex_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    return addition, subtraction, multiplication, division

# Read two complex numbers from the user
complex1 = read_complex("the first complex number")
complex2 = read_complex("the second complex number")

# Perform the operations
add, sub, mul, div = complex_operations(complex1, complex2)

# Display the results
print(f"\nThe results are:")
print(f"Addition: {complex1} + {complex2} = {add}")
print(f"Subtraction: {complex1} - {complex2} = {sub}")
print(f"Multiplication: {complex1} * {complex2} = {mul}")
print(f"Division: {complex1} / {complex2} = {div}")

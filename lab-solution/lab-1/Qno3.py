# WAP that accepts variable number of arguments from user and 
# finds factorial of each number and then displays factorial of every number.

import math

def factorial_of_numbers(*numbers):
    factorials = {num: math.factorial(num) for num in numbers}
    return factorials

# Read a variable number of arguments from the user
user_input = input("Enter numbers separated by space: ")
numbers = map(int, user_input.split())

# Find the factorial of each number
factorials = factorial_of_numbers(*numbers)

# Display the factorials
for num, fac in factorials.items():
    print(f"Factorial of {num} is {fac}")

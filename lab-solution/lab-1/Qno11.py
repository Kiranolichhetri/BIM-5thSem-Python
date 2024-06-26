# WAP to find square root of all numbers in a list using map tool.

import math

# Function to compute square root of a number
def square_root(num):
    return math.sqrt(num)

# Example list of numbers
numbers = [25, 9, 16, 36, 49]

# Using map to apply square_root function to each element in numbers
square_roots = list(map(square_root, numbers))

# Display the results
print("Square roots of numbers in the list:")
for index, root in enumerate(square_roots):
    print(f"Square root of {numbers[index]} is {root}")

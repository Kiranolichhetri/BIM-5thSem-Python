# create a list and find maximum, minimum and cumulative sun
# using reduce functional toll 
from functools import reduce

# Create a list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Find the maximum value using reduce
max_value = reduce(lambda a, b: a if a > b else b, numbers)

# Find the minimum value using reduce
min_value = reduce(lambda a, b: a if a < b else b, numbers)

# Find the cumulative sum using reduce
cumulative_sum = reduce(lambda a, b: a + b, numbers)

print(f"List of numbers: {numbers}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Cumulative sum: {cumulative_sum}")
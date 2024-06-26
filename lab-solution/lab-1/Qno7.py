# WAP to count odd and even numbers in a list.


# Predefined list of numbers
numbers = [10, 21, 4, 45, 98, 35, 67]

# Initialize counters for odd and even numbers
odd_count = 0
even_count = 0

# Iterate through the list and count odd and even numbers
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display the counts
print(f"Number of odd numbers: {odd_count}")
print(f"Number of even numbers: {even_count}")

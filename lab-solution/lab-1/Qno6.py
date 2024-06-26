# WAP to find second largest from a list of elements without using sorting.

# Predefined list of numbers
numbers = [10, 20, 4, 45, 99, 35, 67]

if len(numbers) < 2:
    print("Not enough elements to determine the second largest.")
else:
    first_largest = second_largest = float('-inf')
    
    for number in numbers:
        if number > first_largest:
            second_largest = first_largest
            first_largest = number
        elif first_largest > number > second_largest:
            second_largest = number
    
    if second_largest == float('-inf'):
        print("There is no second largest element.")
    else:
        print("The second largest element in the list is:", second_largest)

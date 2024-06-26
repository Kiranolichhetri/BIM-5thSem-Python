# WAP to extract all prime numbers from a list using filter tool.


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    
    # Check for factors from 3 up to the square root of num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

# Example list of numbers
numbers = [23, 45, 67, 12, 34, 17, 29, 31]

# Using filter to extract prime numbers from numbers list
prime_numbers = list(filter(is_prime, numbers))

# Display the prime numbers
print("Prime numbers in the list:")
print(prime_numbers)

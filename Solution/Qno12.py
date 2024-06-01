# WAP to create a function that accepts variable number of arguments and defines the factorial of each. 
# then display all result.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorials(*args):
    results = {}
    for num in args:
        if isinstance(num, int) and num >= 0:  # Check if the number is a non-negative integer
            results[num] = factorial(num)
        else:
            results[num] = "Invalid input (must be a non-negative integer)"
    return results

# Example usage
numbers = [5, 3, 7, 1, 0, -1, 4.5]
factorials = calculate_factorials(*numbers)

# Display the results
for num, result in factorials.items():
    print(f"Factorial of {num}: {result}")

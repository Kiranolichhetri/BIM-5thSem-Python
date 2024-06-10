def square(n):
    """Takes in a number n, returns the 
    square of the n
    """
    square(5)
    print(square.__doc__)




# for a function 
def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.

    Example:
    >>> add(2, 3)
    5
    >>> add(5.5, 4.5)
    10.0
    """
    return a + b

# Example usage
print(add(2, 3))  # Output: 5
print(add(5.5, 4.5))  # Output: 10.0

# WAP to handle divide by zero and invalid array index exceptions using
# try....except.....finally blocks.

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of division: {result}")
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Division operation completed.")

def access_array_element(array, index):
    try:
        element = array[index]
        print(f"Element at index {index}: {element}")
    except IndexError as e:
        print("Error: Invalid array index.")
    finally:
        print("Array access operation completed.")

# Test the functions
divide_numbers(10, 2)
divide_numbers(10, 0)

array = [1, 2, 3, 4, 5]
access_array_element(array, 2)
access_array_element(array, 10)

# WAP to read two complex numbers from user and then perform their addition, subtraction, multiplication, and 
# division and display the results.


# Read two complex numbers from the user
c1 = complex(input("Enter the first complex number (in the form a+bj): "))
c2 = complex(input("Enter the second complex number (in the form a+bj): "))

# Perform addition, subtraction, multiplication, and division
addition = c1 + c2
subtraction = c1 - c2
multiplication = c1 * c2
division = c1 / c2

# Display the results
print(f"Addition of {c1} and {c2} is: {addition}")
print(f"Subtraction of {c1} and {c2} is: {subtraction}")
print(f"Multiplication of {c1} and {c2} is: {multiplication}")
print(f"Division of {c1} by {c2} is: {division}")

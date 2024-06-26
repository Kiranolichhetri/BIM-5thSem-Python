# 1.WAP to read two numbers (say x and y) and perform following operations:
# a.Display binary equivalent of the numbers
# b.Perform bitwise AND, OR and XOR operations and display their results in binary format
# c.Perform once complement of x and display the result in binary format
# d.Left shift the x by 3 positions and display the result in binary format
# e.Left shift the y by 2 positions and display the result in binary format




# Read two numbers from the user
x = int(input("Enter the first number (x): "))
y = int(input("Enter the second number (y): "))

# Display binary equivalent of the numbers
print(f"Binary equivalent of x: {bin(x)}")
print(f"Binary equivalent of y: {bin(y)}")

# Perform bitwise AND, OR and XOR operations and display their results in binary format
print(f"Bitwise AND of x and y: {bin(x & y)}")
print(f"Bitwise OR of x and y: {bin(x | y)}")
print(f"Bitwise XOR of x and y: {bin(x ^ y)}")

# Perform one's complement of x and display the result in binary format
print(f"One's complement of x: {bin(~x)}")

# Left shift the x by 3 positions and display the result in binary format
print(f"Left shift x by 3 positions: {bin(x << 3)}")

# Left shift the y by 2 positions and display the result in binary format
print(f"Left shift y by 2 positions: {bin(y << 2)}")

x = 5
y = 6
z = x

print(id(x))  # Print the memory address of x
print(id(y))  # Print the memory address of y
print(id(z))  # Print the memory address of z

# Check if x, y, and z refer to the same object
if id(x) == id(y):
    print("x and y refer to the same object")
else:
    print("x and y do not refer to the same object")

if id(x) == id(z):
    print("x and z refer to the same object")
else:
    print("x and z do not refer to the same object")

if id(y) == id(z):
    print("y and z refer to the same object")
else:
    print("y and z do not refer to the same object")

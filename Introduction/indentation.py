#indentation is used to define the structure and scope of the code.
#It is crucial for Python's syntax and readability.

if True:
    print("This code is indented, so it is inside the if block.")
    print("This code is also inside the if block.")
print("This code is not indented, so it is outside the if block.")

x=8
y=12
if x > 5:
    print("x is greater than 5")  # This line is inside the if block
    if y > 10:
        print("y is greater than 10")  # This line is inside the nested if block
    print("This is still inside the if block")  # This line is inside the if block but outside the nested if block
print("This is outside the if block")  # This line is outside the if block

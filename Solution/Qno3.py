#input 3 numbers from user and display largest and smallest.

# Take input from the user for 3 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

smallest = num1
largest = num1

# Compare num2 and num3 with num1 to find the smallest and largest numbers
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# Display the smallest and largest numbers
print("The smallest number is:", smallest)
print("The largest number is:", largest)

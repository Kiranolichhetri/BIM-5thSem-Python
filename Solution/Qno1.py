#find the largest number of list
numbers = [20,12,45,3,60,8]

largestNum = numbers[0] #assume first number to be largest initially

for number in numbers :
    if number > largestNum :
        largestNum = number
        
print("The largeest number is",largestNum)        
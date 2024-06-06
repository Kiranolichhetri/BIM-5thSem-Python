def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is:", sum / len(numbers))
        
average(5,6,3)           
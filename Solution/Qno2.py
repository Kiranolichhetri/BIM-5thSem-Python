#Search in list whether it contains the multiple of 5 and 3 (use else clause in for loop)

numbers = [10,15,20,25,30,]

for number in numbers :
    if number % 5 == 0  and number % 3 == 0:
        print(f"{number} is multiple of both 5 and 3")
        
    else:
        print(f"{number} is not the multiple of both 5 and 3")
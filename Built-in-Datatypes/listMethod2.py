my_list = [7, 8, 3,4, 4, 5]

# slicing 
print(my_list[1:4])  # Output: [20, 4, 5]

# list comprehensions 
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# sorting 
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# count 
print(my_list.count(4))

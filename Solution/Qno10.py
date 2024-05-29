#  Display the list items in reverse order and in ascending order 

my_list = [5, 2, 9, 1, 5, 6]

reversed_list = list(reversed(my_list))
ascending_list = sorted(reversed_list)


print("List items in reverse order:")

for item in reversed_list:
    print(item)
    
    
print("List items in ascending order:")
for item in ascending_list:
    print(item)    
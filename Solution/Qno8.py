# Create two lists and merge them.also delete 2nd item after merge then add two item after 5th index 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]


merged_list = list1 + list2


del merged_list[2]


merged_list.insert(5,11)
merged_list.insert(6,12)

print("Merged List after modification:",merged_list)
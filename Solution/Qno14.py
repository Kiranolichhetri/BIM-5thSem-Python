# WAp to demstate diference between list and tuple.


# Creating a list and a tuple

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("Original List:", my_list)
print("Original Tuple:", my_tuple)

# Mutability: Lists are mutable, Tuples are immutable
my_list[0] = 10
print("Modified List:", my_list)

try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error modifying Tuple:", e)
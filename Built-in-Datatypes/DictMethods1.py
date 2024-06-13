# clear 
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.clear()
print(my_dict)  # Output: {}


# copy
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

# fromkeys
keys = ('name', 'age', 'city')
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}

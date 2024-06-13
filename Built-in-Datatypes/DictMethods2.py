# pop 
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
age = my_dict.pop('age')
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}


# popitem()
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
item = my_dict.popitem()
print(item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 25}

# setdefault
my_dict = {'name': 'John', 'age': 25}
email = my_dict.setdefault('email', 'john@example.com')
print(email)  # Output: john@example.com
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'email': 'john@example.com'}


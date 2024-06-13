# Using curly braces
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Using the dict() function
my_dicti = dict(name='kiran', age=25, city='Nepalgunj')


print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 25

print(my_dicti['name'])  # Output: John
print(my_dicti.get('age'))  # Output: 25

print(my_dicti.keys())

for keys in my_dicti.keys():
    print(my_dicti[keys])
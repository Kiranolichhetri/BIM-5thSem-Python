# using the range function
for i in range(1, 10, 2):
    print(i)



# Iterating Over a Dictionary

person = {"name": "Alice", "age": 25, "city": "New York"}

# Iterate over keys
for key in person:
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

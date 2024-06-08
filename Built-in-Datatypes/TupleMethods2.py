my_tuple = (1, 2, 3, 4, 5,2,2)

# count 
print(my_tuple.count(2))

# index 
print(my_tuple.index(4))

# tuple operations 

# concatenation 

tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  


# repetition 

repeated_tuple = tuple1 * 3
print(repeated_tuple) 

# tuple unpacking 
# values of a tuple into variables 
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  


# Example 

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements
print(my_tuple[0])  

# Slicing
print(my_tuple[1:3])  

# Tuple methods
print(my_tuple.count(20))  
print(my_tuple.index(30))  
# Concatenation
new_tuple = my_tuple + (60, 70)
print(new_tuple)  

# Repetition
repeated_tuple = my_tuple * 2
print(repeated_tuple)  

# Unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  


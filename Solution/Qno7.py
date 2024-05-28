# In list delete all items containing other that alphabets 
# Define the list with mixed items
items = ["apple", "banana123", "cherry", "123", "date", "egg3plant", "fig", "grape!"]

# Use list comprehension to keep only alphabetic items
items = [item for item in items if item.isalpha()]

# Print the updated list
print("Filtered items:", items)

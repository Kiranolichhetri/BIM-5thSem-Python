# create the list and generate another list having items that occurs in both list.
# Define two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Create an empty list to store common items
common_items = []

# Iterate through the first list
for item in list1:
    # Check if the item is also in the second list
    if item in list2:
        # Add the item to the common items list
        common_items.append(item)

# Print the common items
print("Common items:", common_items)

# WAP to read two sets from users and then perform set union, set intersection, 
# and set difference operation and display results

# Read two sets from the user
set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())

# Perform set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

# Display the results
print(f"Set Union: {union_set}")
print(f"Set Intersection: {intersection_set}")
print(f"Difference (set1 - set2): {difference_set1}")
print(f"Difference (set2 - set1): {difference_set2}")

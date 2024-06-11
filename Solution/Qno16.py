# Create two sets and display their, union, intersection and difference.
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Display the union of the sets
union_set = set1.union(set2)
print("Union:", union_set)

# Display the intersection of the sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Display the difference of the sets (set1 - set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Display the difference of the sets (set2 - set1)
difference_set2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2)

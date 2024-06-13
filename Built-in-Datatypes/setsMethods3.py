# Subset and Superset Operations

# issubset(other)
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # Output: True

# issuperset(other)
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))  # Output: True

# isdisjoint(other)
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # Output: True



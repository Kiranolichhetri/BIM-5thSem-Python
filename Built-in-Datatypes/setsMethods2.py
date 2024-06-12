# Set Operations
# union(*others)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)  # Output: {1, 2, 3, 4, 5}


# intersection(*others)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
print(s3)  # Output: {3}

# difference(*others)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)
print(s3)  # Output: {1, 2}

# symmetric_difference(other)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3)  # Output: {1, 2, 4, 5}

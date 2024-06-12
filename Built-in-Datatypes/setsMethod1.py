# Adding Elements 
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# Removing Elements 

# remove(elem)
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}

# discard(elem)
s = {1, 2, 3}
s.discard(2)
print(s)  # Output: {1, 3}

# pop()
s = {1, 2, 3}
elem = s.pop()
print(elem)  # Output: (1, 2, or 3)
print(s)     # Output: Remaining elements in the set

# clear()
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()




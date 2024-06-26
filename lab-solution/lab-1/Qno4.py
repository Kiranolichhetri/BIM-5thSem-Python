# WAP that reads a string from user and then 
# finds number of alphabets, digits, and special characters in the string.

def count_characters(input_string):
    alphabets = digits = special_chars = 0
    
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1
            
    return alphabets, digits, special_chars

# Read a string from the user
user_input = input("Enter a string: ")

# Count the number of alphabets, digits, and special characters
alphabets, digits, special_chars = count_characters(user_input)

# Display the results
print(f"Number of alphabets: {alphabets}")
print(f"Number of digits: {digits}")
print(f"Number of special characters: {special_chars}")

# WAP that reads inputs from user and writes it to the file test.txt until user enters
# bye. Then read and display the content of file.

def write_to_file(filename):
    with open(filename, 'w') as file:
        while True:
            user_input = input("Enter text (type 'bye' to finish): ")
            if user_input.lower() == 'bye':
                break
            file.write(user_input + '\n')

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

filename = 'test.txt'
write_to_file(filename)
print("\nContent of the file:")
print(read_from_file(filename))

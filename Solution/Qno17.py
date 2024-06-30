
#Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.
def readContent():
    file = open("poem.txt","r")
    data = file.readlines()
    for line in data:
        print(line)
readContent()

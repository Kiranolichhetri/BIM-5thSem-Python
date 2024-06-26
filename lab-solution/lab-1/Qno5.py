# WAP that reads a multi-sentence string from user. 
# Separate each sentence in the string and display each sentence. 
# Again separate each word in the string and display then. Comma should not be included in the words.

import re

def separate_sentences(text):
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

def separate_words(text):
    # Remove commas and split the text into words
    words = re.sub(r',', '', text).split()
    return words

# Read a multi-sentence string from the user
user_input = input("Enter a multi-sentence string: ")

# Separate each sentence and display
sentences = separate_sentences(user_input)
print("\nSentences:")
for sentence in sentences:
    print(sentence)

# Separate each word and display
words = separate_words(user_input)
print("\nWords:")
for word in words:
    print(word)

# Andrew Grant
# 105226219

# Program to determine if word or words form a palindrome

# Function to determine if a word or series of words is a palindrome.
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


# Defining a list to story the lines from the file
dictionaryPal = []

# Opening the input file and placing the words into the list
with open('inputfile.txt', 'r') as file1:
    for line in file1:
        line = line.strip("\n")  # removes the \n from string
        dictionaryPal.append(line)

# loop to run through each spot in list and test for palindrome
for words in dictionaryPal:
    # calling the palindrome function while removing spaces and putting all lower case for the word/words
    if is_palindrome(words.replace(" ", "").lower()):
        print(f'''{words} ~ is a palindrome.''')  # Output
    else:
        print(f'''{words} ~ is not a palindrome.''')  # Output

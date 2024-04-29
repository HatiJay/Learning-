# Part 1
# Read in a string from the user
string = input("Enter your string: ")
print(string)

# Create a variable 'new_string' to hold the modified string 
new_string = ""

# Iterate through each character in the 'string' variable
for index, char in enumerate(string):
    # Check if the index is even
    if index % 2 == 0:
        # Convert even-indexed numbers into uppercase
        new_string = new_string + char.upper()
    # Convert odd-indexed numbers into lowercase
    else: new_string = new_string + char.lower()

# Send 'new_string' to screen
print("Your new string: ", new_string)

# Part 2
# Convert the string into a list using 'split()' function and store it in 'sentence' variable
sentence = string.split()

# Create a variable 'new_sentence' to hold the modified string 
new_sentence = ""

# Iterate through each word in the 'sentence' variable 
for index, word in enumerate(sentence):
    # Check if the string index is even 
    if index % 2 == 0:
        # Convert the even-indexed words into capitals 
        new_sentence = new_sentence + word.upper()
    # Convert odd-indexed words into lowercase
    else: new_sentence = new_sentence + word.lower()

if index < len(new_sentence) - 1:
        new_sentence += " "

# Send 'new_sentence' to screen
print("Your second string: ", new_sentence)

#Not sure how to input spaces between each letter. looking forward to feedback
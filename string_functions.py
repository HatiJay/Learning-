# Capitalise all characters
name = "ikea"
name2 = name.upper()

# Capitalise only the first letter 
message = "happy birthday"
message2 = message.capitalize()

# Convert all to lowercase 
song = "JOLENE"
song2 = song.lower()

# Display corrected strings
print(name2)
print(message2)
print(song2)

# Find a character index using the 'find()' function
sentence = "The Power Of Python"
print(sentence.find("P"))

# Remove white spaces from the beginning and end of a string using "strip()" function
door_number = " 134 "
print(door_number.strip())

# Remove a specified character from a string using 'strip()' function
food = "Ha,mburger,,,,"
food2 = food.strip(",")
print(food2) #error not removing comma in the middle of string

# Replace specific text with desired text
movie_title = "The Adventures of Mystery Woman"
new_movie_title = movie_title.replace("Mystery", "Wonder")
print(new_movie_title)

# Split a string into a list using 'split()' function
string = "bananas apples pears grapes"
string = string.split()
print(string)

# Split a string with a specified seperator 
string2 = "bananas#apples#pears"
string2 = string2.split("#")
print(string2)

# Split a string with a specific seperator and maxsplit (how many splits)
string3 = "Hatice, Jamiah, Akina, Douglas Osmond"
string3 = string3.split(", ", 3)
print(string3)
# Store animal types in a list of variables
animals = ["cat", "dog", "parrot", "gorilla"]

# Ask the user to select their favourite animal 
print("Please select your animal")
choice = int(input())

# Create a loop if user enters a value greater than the list 
if choice > 3:
    print("Please choose a number on the list")
    choice = int(input())
    print(f"Your choice is: " , animals[choice])

else:
    print(f"Your choice is: " , animals[choice])


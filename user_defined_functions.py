# Create a function for an alarm 
def alarm(name):
    print("Good morning", name)
    print("Have a wonderful day")

# Call the function
alarm("Hatice")

# Create a function that needs to store a value 
def total(price, quantity):
    total = price * quantity
    return total
   
# Calling the function and using return value
coat = total(10,5)
print("Can't Afford: ", coat > 100)

# Default values created if the argument isnt defined
def greet(name = "Guest"):
    print("Welcome", name)

# Welcome Guest
greet() 

# Welcome Hatice
greet("Hatice") # default is overwritten if arguments are inputted


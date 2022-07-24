# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("How are you doing!")
    print("Is the weather fine there?")

greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name("Jake")


#Function with more than one arguments
def greet_with(name, location):
    print(f"Hello {name}, {location}?")

greet_with("Jake", "Meghalaya")

#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")

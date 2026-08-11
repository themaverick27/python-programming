# Function - block of code that does a specific work, can be executed any number of times

# defining function
def greet():
    print("Hello, How are you?")

# calling function 
greet()


# Types of arguments: positional, named and default

# positional argument
def printSum(num1, num2): # parameters
    print(f"The sum of two numbers is {num1 + num2}")

printSum(18, 45) # arguments

printSum(10, 74)

# default argument
def greetPerson(name = "Guest"):
    print(f"Hello, {name}")

greetPerson()
greetPerson("Hathway")

# named/keyword argument

def printDetails(name, age):
    print(f"The name of the person is {name} and age is {age}")

printDetails(name = "Avi", age = 26)
printDetails(age = 34, name ="Mist")
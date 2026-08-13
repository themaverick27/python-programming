# custom decorator example

def my_decorator(func):
    def wrapper(a, b):
        print("The addition of your numbers is: ")
        func(a, b)
        print("Hope, you liked it.")
    return wrapper;

@my_decorator
def addition(a, b):
    print(f"{a + b}")

addition(12, 54)

# you have to pass argument to the wrapper as well. 
# problem: what if the next time you pass three parameters, or maybe four but the decorator only accepts two right now. 
# we have to create new decorator or change decorator everytime. 
# solution: *args

def custom_decorator(func):
    def wrapper(*args):
        print("The addition of your numbers is: ")
        func(*args)
        print("Hope, you liked it.")
    return wrapper;

@custom_decorator
def add(*args):
    ans = 0
    for i in args:
        ans += i
    print(f"{ans}")


add(4, 5)
add(45, 12, -5)
add(7)
add(34, 78, 25, 100)

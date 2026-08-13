# Decorators

class Animal:
    @property
    def show(self):
        print("this is a method!")

obj = Animal()
#obj.show()

obj.show


# custom decorator
def my_decorator(func):
    def wrapper():
        print("Run before function execution!")
        func()
        print("Run after function execution!")
    return wrapper

@my_decorator
def demo():
    print("this is a demo function")

demo()

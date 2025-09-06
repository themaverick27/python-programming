# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Volvo", "EX30")
print(my_car) # reference of my_car object

print(my_car.brand)
print(my_car.model)

# Note:
# 1. The __init__ method in Python is a special method, often referred to as a constructor, that is automatically called when a new instance (object) of a class is created.

# 2. Its primary purpose is to initialize the object's attributes and perform any necessary setup tasks for the object.

# 3. self keyword: In Python, self is a conventional name for the first parameter of instance methods within a class

# 4. self keyword: self explicitly refers to the instance of the class on which the method is being called.
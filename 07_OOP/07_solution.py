# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod #  a static method is a method that belongs to the class itself, rather than to any specific instance (object) of that class, we don't use self as we do not link it with object or instance
    def general_description():
        return "Car are means of transport!"


print(Car.general_description) # prints the reference of the function

print(Car.general_description()) 
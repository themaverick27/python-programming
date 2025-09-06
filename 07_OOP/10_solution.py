# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Battery:
    def battery_info(self):
        return "This is battery of Electric Vehicle!"

class Engine:
    def engine_info(self):
        return "This is engine of Electric Vehicle!"

class ElectricCar(Battery, Engine, Car):
    pass

my_car = ElectricCar("Tesla", "Model S")
print(my_car.battery_info())
print(my_car.engine_info())
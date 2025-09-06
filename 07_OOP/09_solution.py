# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car): # ElectricCar class inherits from Car class
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # super refers to the parent class
        self.battery_size = battery_size


my_car = Car("Volvo", "EX30")

my_new_car = ElectricCar("Tesla", "Model S", "80kWh")
print(my_new_car.battery_size)

print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))

print(isinstance(my_new_car, Car))
print(isinstance(my_new_car, ElectricCar))

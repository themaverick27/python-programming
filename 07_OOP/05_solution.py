# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_car = Car("Volvo", "EX30")
print(my_car.fuel_type())

my_new_car = ElectricCar("Tesla", "Model S", "80kWh")
print(my_new_car.fuel_type())
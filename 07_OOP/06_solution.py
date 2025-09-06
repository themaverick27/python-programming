# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


my_car = Car("Volvo", "EX30")
print(my_car.full_name())

#print(Car.total_car)

my_new_car = Car("Mercedes", "Hatchbacks-Benz")
print(my_new_car.full_name())

#print(Car.total_car)

my_another_car = Car("Hyundai", "Venue")
print(my_another_car.full_name())

print(Car.total_car)
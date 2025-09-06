# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model


my_car = Car("Mercedes", "Hatchbacks-Benz")
print(my_car.model)

# my_car.model = "Benz AMG GT" # not allowed - property take cares of it
print(my_car.model)
# print(my_car.__model) # cannot access - private
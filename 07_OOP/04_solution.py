# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self): # getter method
        return self.__brand

my_car = Car("Volvo", "EX30")
# print(my_car.__brand) # doesn't exists as brand is private
print(my_car.get_brand())
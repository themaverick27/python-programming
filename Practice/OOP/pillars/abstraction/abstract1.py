# Abstraction in python - Python provides abstraction mainly through the abc module:
# ABC means Abstract Base Class


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# you cannot instantiate abstract class 
# animal = animal() # error
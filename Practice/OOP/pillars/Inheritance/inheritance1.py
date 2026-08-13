class Animal: # parent class/ super class
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal): # child class/ sub class
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.sleep()
dog.bark()

# Note: A child class can access the attributes and methods of its parent class.


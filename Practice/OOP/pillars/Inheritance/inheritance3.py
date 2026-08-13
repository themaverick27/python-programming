# method overriding - same function name

class Animal:
    def sound(self):
        print("Some generic sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")


animal = Animal()
dog = Dog()

#animal.sound()
dog.sound()
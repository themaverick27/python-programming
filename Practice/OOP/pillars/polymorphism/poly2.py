class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Human:
    def speak(self):
        print("Hello")


def make_sound(obj):
    obj.speak()


make_sound(Dog())
make_sound(Cat())
make_sound(Human())

# Python often achieves polymorphism through duck typing, 
# where the object's behavior matters more than its explicit type or inheritance hierarchy.
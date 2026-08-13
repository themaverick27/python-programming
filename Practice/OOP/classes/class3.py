class Person:
    count = 0 # class attribute
    def __init__(self, age): # instance method
        #print(self) # self target specific location of object
        self.age = age # instance attribute

    def show(self): # instance method
        print(f"The person age is: {self.age}")

    @classmethod  
    def demo(cls): # class method
        #print(cls) # cls targets class location
        print("This a class method! Targets class not object")
        #print(f"This a class method! Targets class not object: {cls.age}") # error as cls target class and there is no property as age of class

    @staticmethod 
    def test(): # static method
        print("This is a static method!")


obj = Person(12)

obj.show()
obj.demo()
obj.test()
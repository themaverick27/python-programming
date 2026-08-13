class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


class Student(Person):
    def __init__(self, name, college):
        super().__init__(name) # calls the parent constuctor __init__()
        self.college = college


student = Student("Aniwesh", "KIET")

student.introduce()
print(student.college)
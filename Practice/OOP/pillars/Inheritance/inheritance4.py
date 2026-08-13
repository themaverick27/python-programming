class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

    def work(self):
        print("Employee is working")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        print(f"{self.name} is writing {self.programming_language} code")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing {self.team_size} employees")


developer = Developer("Rahul", 80000, "Python")
manager = Manager("Pari", 100000, 10)

developer.display_info()
developer.work()

print()

manager.display_info()
manager.work()
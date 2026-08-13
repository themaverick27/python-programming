# runtime polymorphism - method overrding
# Python does not support traditional method overloading like Java/C++. Uses *args to achieve this behaviour.

class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team")


developer = Developer()
manager = Manager()

developer.work()
manager.work()

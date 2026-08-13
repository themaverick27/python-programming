# protected - underscore before attributes and methods

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

account = BankAccount(10000)
print(account._balance)

# Python does not actually prevent access.
# The underscore is mainly a convention.


# private - double underscore before attributes and methods

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(10000)
print(account.__balance) # attribute error

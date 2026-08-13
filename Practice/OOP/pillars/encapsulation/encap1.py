# problem 

class BankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BankAccount(10000)
account.balance = -500000 # anyone can change value (here balance is public)


# to control such things - python uses access modifier: public, protected, private
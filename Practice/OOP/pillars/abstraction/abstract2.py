from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class PayPal(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


payments = [
    UPI(),
    CreditCard(),
    PayPal()
]

for payment in payments:
    payment.pay(1000)


# abstract class can have normal methods as well.
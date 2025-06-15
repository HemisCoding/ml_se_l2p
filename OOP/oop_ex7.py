##Abstract Base Classes (abc)
# Exercise 7: PaymentMethod abstract class

from abc import ABC, abstractmethod

# Abstract class PaymentMethod with abstract method pay(amount)

# Subclasses: CreditCard, PayPal – each with custom pay() behavior

# Create a list of payment methods and call pay(100) on each

class PaymentMethod(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        self.balance -= amount
        return self.balance

class PayPal(PaymentMethod):
    def pay(self, amount):
        self.balance -= amount
        return self.balance

credit = CreditCard(300)
paypal = PayPal(300)

print(credit.pay(100))
print(paypal.pay(100))



    

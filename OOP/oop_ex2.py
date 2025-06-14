# Define a class BankAccount with attributes:
# - owner (string)
# - balance (float, default 0)

# Methods:
# - deposit(amount)
# - withdraw(amount) – don't allow going negative
# - display_balance()

# Create an object and test each method.


class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"The current balance is: {self.balance}")

account1 = BankAccount("John", 1000)
account1.deposit(700)
account1.withdraw(350)
account1.display_balance()

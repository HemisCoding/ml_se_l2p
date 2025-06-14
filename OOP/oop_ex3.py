## Instance vs Class vs Static Methods
# Exercise 3: Create a User class

# Track total number of users with a class variable

# Define:
# - __init__ with name and email
# - greet() instance method
# - from_string() class method (input: "Name,email")
# - is_valid_email() static method

# Test all methods and print total user count.
class AccountManager:
    count = 0

    def __init__(self, name, email):
        AccountManager.count += 1
        self.name = name
        self.email = email

    def greet(self):
        print(f"Hello {self.name}, please login using name and email")
        print(AccountManager.count)

    @classmethod
    def from_string(cls, data_str):
        name, email = data_str.split(",")
        print(name, email)
        return cls(name.strip(), email.strip())
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email 



account1 = AccountManager("John", "john@gmail.com")
account1.greet()

print(f"Mail check: ", AccountManager.is_valid_email(account1.email))

account2 = AccountManager.from_string("hem, hem@gmail.com")
account2.greet()
print(f"Mail check again: ", AccountManager.is_valid_email(account2.email))





    


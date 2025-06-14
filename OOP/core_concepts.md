## 🧱 Core OOP Concepts in Python with Examples

---

### 🔹 Inheritance

**What it means:**  
A subclass inherits attributes and methods from a parent class.

**Why it’s useful:**  
- Reuse code from existing classes  
- Override behavior where needed  
- Model real-world relationships (e.g. a `Dog` *is a* `Animal`)

**Example:**
```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Woof!



🔹 Polymorphism
What it means:
Different objects can respond to the same method call in different ways.

Why it’s useful:

Write cleaner, more flexible code

Treat unrelated objects through a common interface

Useful in loops, APIs, and plugins

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

animals = [Cat(), Cow()]

for animal in animals:
    print(animal.sound())
# Output: Meow
#         Moo


🔹 Encapsulation
What it means:
Hide internal state and protect it using naming conventions like _protected or __private.

Why it’s useful:

Protect internal data from accidental modification

Create clean and stable interfaces

Separate implementation from usage


class Account:
    def __init__(self, owner):
        self._balance = 0            # Protected (convention)
        self.__owner = owner         # Private (name-mangled)

    def deposit(self, amount):
        self._balance += amount

    def get_owner(self):
        return self.__owner

account = Account("Alice")
account.deposit(100)
print(account._balance)       # Accessible but discouraged
print(account.get_owner())    # Correct access to private data



🔹 Properties
What it means:
Use @property and @<name>.setter decorators to control access to attributes.

Why it’s useful:

Add validation or transformation when getting/setting values

Keep your class flexible and safe without changing external syntax

Make attributes read-only or computed dynamically

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero!")
        self._celsius = value

temp = Temperature(25)
print(temp.celsius)       # 25
temp.celsius = 10         # OK
# temp.celsius = -300     # Raises ValueError


🔹 Abstract Classes
What it means:
A class that defines a required structure using @abstractmethod, but cannot be instantiated directly.

Why it’s useful:

Force subclasses to implement specific methods

Ensure consistency across different child classes

Define clear interfaces or contracts

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started")

# vehicle = Vehicle()  # ❌ TypeError: Can't instantiate abstract class
car = Car()
car.start_engine()  # Output: Engine started

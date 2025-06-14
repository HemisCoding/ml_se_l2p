1. What is OOP (Object-Oriented Programming)?
OOP is a way of structuring code around objects — each representing a real-world concept, with:

Attributes (state/data)

Methods (behavior/functionality)


2. Defining a class:
class Dog:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

➕ __init__ method
Called when you create an object: dog = Dog("Rex", 5)

self refers to the specific object being created

You initialize instance variables using self



3. Instance Methods
Defined with self as the first argument. They:

Can access or modify object-level data

Define object-specific behavior

    def bark(self):
        print(f"{self.name} says woof!")


4. Class Variables vs Instance Variables
| Type              | Belongs to              | Shared? | Declared in            |
| ----------------- | ----------------------- | ------- | ---------------------- |
| Instance Variable | One object (e.g. `dog`) | ❌ No    | Inside `__init__`      |
| Class Variable    | Whole class             | ✅ Yes   | Directly in class body |

class Dog:
    species = "Canis lupus"  # class variable

    def __init__(self, name):
        self.name = name     # instance variable



5. Class Methods (@classmethod)
Defined with cls as first param
Access or modify class-level data
Often used as alternative constructors

    @classmethod
    def from_string(cls, data_str):
        name, email = data_str.split(",")
        return cls(name.strip(), email.strip())


6. Static Methods (@staticmethod)
No self or cls

Pure utility functions that belong to the class logically

Cannot access class or instance data

    @staticmethod
    def is_valid_email(email):
        return "@" in email




| Method                  | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| `__str__`               | Custom string when you call `str(obj)`    |
| `__repr__`              | Official string used in debugging / shell |
| `__eq__`                | Compare objects with `==`                 |
| `__lt__`, `__gt__`      | For `<`, `>`, etc.                        |
| `__len__`               | Define behavior for `len(obj)`            |
| `__getitem__`           | Allow indexing like `obj[0]`              |
| `__iter__`              | Make your object iterable                 |
| `__enter__`, `__exit__` | For `with` context managers               |

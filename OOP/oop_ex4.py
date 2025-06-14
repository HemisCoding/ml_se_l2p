## Inheritance and Polymorphism
# Exercise 4: Shape -> Rectangle, Circle

# Base class: Shape with method area() that raises NotImplementedError
# Subclasses:
# - Rectangle(width, height) implements area()
# - Circle(radius) implements area()

# Instantiate and test polymorphic behavior:
# loop over a list of shapes and call area()

import math 

class Shape:
    def area(self):
        raise NotImplementedError("Please set the dimensions for area")
    
    def test(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
shapes = [Rectangle(3, 4), Circle(2)]

for shape in shapes:
    print(shape.area())
    print(shape.test())
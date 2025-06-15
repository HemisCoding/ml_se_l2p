## Encapsulation & Properties
# Exercise 5: Temperature class

# Create class Temperature with private attribute _celsius

# Provide:
# - property `celsius` with getter/setter
# - property `fahrenheit` (read-only, computed from celsius)

# Prevent setting negative temperatures
# Test usage: t = Temperature(25), t.celsius = 30, print(t.fahrenheit)


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def transform(self):
        return self._celsius * 33.8

bucharest = Temperature(20)
print(bucharest.celsius)
print(bucharest.transform)
# bucharest.celsius(15)

# bucharest.transform()

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius  # uses the setter for validation

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value):
#         if value < 0:
#             raise ValueError("Temperature cannot be negative.")
#         self._celsius = value

#     @property
#     def fahrenheit(self):
#         return (self._celsius * 9/5) + 32

# # Test usage
# t = Temperature(25)
# t.celsius = 30
# print(t.fahrenheit)  # 86.0

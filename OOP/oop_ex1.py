# Define a class Car with attributes: brand, model, year
# Add a method `start()` that prints "<brand> <model> is starting"

# Instantiate two car objects and call their methods


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("The brand and model are: ", self.brand, self.model)

car1 = Car("lambo", "aventador", 2020)
car2 = Car("dacia", "logan", 2025)

car1.start()
car2.start()
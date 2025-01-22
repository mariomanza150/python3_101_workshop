class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)
        self.color = color

print(Car.__mro__)

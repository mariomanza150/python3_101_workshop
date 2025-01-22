class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        return f"The {self.color} {self.brand} is driving!"

my_car = Car("Toyota", "red")
print(my_car.drive())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

class Car:
    speed = 0
    wheels = 4

    def __init__(self, brand="Toyata", color="blanco"):
        self.brand = brand
        self.color = color
        self.year = "2024"

    @classmethod
    def info(cls):
        print(type(cls))
        print(cls)

    @staticmethod
    def cotizar(brand, color, year):
        # Aun no definimos el proceso exacto de calculo/lookup
        pass

    def drive(self, factor):
        self.speed *= factor
        return f"The {self.color} {self.brand} is driving!"


# Crea un objecto con la magia de __init__
my_car = Car("Toyota", "red")
# Utiliza un metodo
print(my_car.drive())
# Accede a sus atributos
my_car.wheels


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Crea dos vectores, se ejecuta el metodo __init__
v1 = Vector(2, 3)
v2 = Vector(5, 7)

# Usa la magia de __add__, ahora tienes suma vectorial en Python facilisimo!
v3 = v1 + v2

# Imprime los vectores, __repr__ define como se vera el resultado
print("v1 =", v1)  # Output: Vector(2, 3)
print("v2 =", v2)  # Output: Vector(5, 7)
print("v3 =", v3)  # Output: Vector(7, 10)

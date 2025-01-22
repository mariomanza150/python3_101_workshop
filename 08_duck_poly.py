class Bird:
    def fly(self):
        return "Flying!"
    
class Plane:
    def fly(self):
        return "Soaring through the skies!"

def take_off(flyable):
    print(flyable.fly())

take_off(Bird())
take_off(Plane())

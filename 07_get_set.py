class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._protected = "Protected"
        self.__private = "Private"
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive!")

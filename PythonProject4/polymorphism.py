class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def medium(self):
        pass

class Car(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

    def medium(self):
        print("road")

class plane(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

    def medium(self):
        print("air")

class boat(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

    def medium(self):
        print("water")

bt = boat("bat", 20, 2020)
bt.medium()
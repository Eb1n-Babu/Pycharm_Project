class Parent:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print(self.firstName, self.lastName)


class child(Parent):
    def __init__(self, firstName, lastName , name):
        Parent.__init__(self, firstName, lastName)
        self.name = name

ch = child("John", "Smith", "amal")
ch.display()
par = Parent("akil","robert")
par.display()



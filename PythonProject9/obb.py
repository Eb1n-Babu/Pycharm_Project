class phone:
    def __init__(self,brand, model, year , price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price




    def display(self):
        return f"{self.brand} {self.model} {self.year} {self.__price}"

new_phone = phone("iphone", "iphone 15", "2023",900000)
print(new_phone.display())

new_phone.brand = "iphonettt"
print(new_phone.display())
new_phone.price = 90785
print(new_phone.display())
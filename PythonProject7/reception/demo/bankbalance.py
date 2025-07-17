from reception.demo.exceptionclass import ValueError1

class bank:
    def __init__(self ,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError1(amount)
        else:
            self.balance -= amount



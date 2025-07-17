class Balance:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance <= amount:
            raise Exception("Insufficient balance")
        else:
            self.balance -= amount
            print(self.balance)

if __name__ == '__main__':
    try:
        obj = Balance(50)
        obj.withdraw(100)
    except Exception as e:
        print(e)
class ValueError1(Exception):
    def __init__(self,amount):
        super().__init__(f'{amount}  insufficient balance')



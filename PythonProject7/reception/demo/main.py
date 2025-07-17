from reception.demo.exceptionclass import ValueError1
from reception.demo.bankbalance import bank

if __name__ == '__main__':
   try:
       ibj = bank(10000)
       ibj.withdraw(20000)
   except ValueError1 as e:
       print(e)




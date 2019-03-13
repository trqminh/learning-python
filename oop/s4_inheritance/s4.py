from account import *
from vehicle import *


def main():
    # a = Account(1500)
    # print(a)
    # a.recharge(1500)
    # a.withdraw(1000)
    # print(a)

    # sa = SavingAccount(1000, 12, 1.5, 3)
    # sa.recharge(500) #6000
    # sa.withdraw(500)
    # print(sa)

    tr = Truck(200, 100)
    print(tr)
    tr.run(20)
    print(tr)

    mt = Motor(50, 30)
    print(mt)
    mt.unload_goods(10)
    mt.run(10)
    print(mt)


if __name__ == '__main__':
    main()

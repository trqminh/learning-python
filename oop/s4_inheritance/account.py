class Account:
    def __init__(self, balance):
        self._balance = balance   # protected

    def __repr__(self):
        return "Account balance: {}".format(self._balance)

    def recharge(self, money_amount):
        self._balance += money_amount

    def withdraw(self, money_amount):
        if self._balance >= money_amount:
            self._balance -= money_amount


class SavingAccount(Account):
    def __init__(self, balance, period, interest_rate, month):
        super().__init__(balance)
        self.__period = period
        self.__interest_rate = interest_rate
        self.__month = month

    def recharge(self, money_amount):
        self._balance += self._balance * self.__month * self.__interest_rate
        self.__month = 0
        super().recharge(money_amount)

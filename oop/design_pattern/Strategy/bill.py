# https://en.wikipedia.org/wiki/Strategy_pattern#UML_class_and_sequence_diagram
import abc


class Customer:
    def __init__(self, drinks, strategy):
        self.__drinks = drinks
        self.strategy = strategy

    def add(self, price, quantity):
        self.__drinks.append(self.strategy.get_act_price(price*quantity))

    def print_bill(self):
        total = 0
        for i in range(len(self.__drinks)):
            total += self.__drinks[i]

        print('total due: ' + str(total))
        self.__drinks.clear()


class IBillingStrategy(abc.ABC):
    @abc.abstractmethod
    def get_act_price(self, raw_price):
        pass


class NormalStrategy(IBillingStrategy):
    def get_act_price(self, raw_price):
        return raw_price


class HappyHourStrategy(IBillingStrategy):
    def get_act_price(self, raw_price):
        return raw_price*0.5


def main():
    normal_strategy = NormalStrategy()
    happy_strategy = HappyHourStrategy()

    first_customer = Customer([], normal_strategy)
    first_customer.add(3,5)

    first_customer.strategy = happy_strategy
    first_customer.add(3,5)

    first_customer.print_bill()


if __name__ == '__main__':
    main()






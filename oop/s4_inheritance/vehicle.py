class Vehicle:
    def __init__(self, fuel, weight):
        self._fuel = fuel
        self._weight = weight  # protected

    def add_goods(self, goods_weight):
        self._weight += goods_weight

    def unload_goods(self, goods_weight):
        self._weight -= goods_weight

    def refuel(self, fuel_amt):
        self._fuel += fuel_amt

    def run(self, len_of_road):
        pass

    def check_fuel(self):
        return self._fuel > 0

    def __repr__(self):
        return "fuel: {} liter, weight: {} kg".format(self._fuel, self._weight)


class Truck(Vehicle):
    def __init__(self, fuel, weight):
        super().__init__(fuel, weight)
        self._fuel_consumption = 0.2 + (self._weight // 1000) * 0.01

    def run(self, len_of_road):
        super().run(len_of_road)
        self._fuel -= self._fuel_consumption * len_of_road
        self._fuel = max(0, self._fuel)


class Motor(Vehicle):
    def __init__(self, fuel, weight):
        super().__init__(fuel, weight)
        self._fuel_consumption = 0.02 + (self._weight // 10) * 0.001

    def run(self, len_of_road):
        super().run(len_of_road)
        self._fuel -= self._fuel_consumption * len_of_road
        self._fuel = max(0, self._fuel)

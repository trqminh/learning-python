import math


class Fraction:
    # class attributes for all instance, it's static variable
    type = 'R'  # real number

    # instance attributes
    def __init__(self, num, deno):
        self.__num = num    # __ : private
        self.__deno = deno

    def input(self):
        print('Enter num: ', end='')
        self.__num = int(input())
        print('Enter deno: ', end='')
        self.__deno = int(input())

    def output(self):
        self.simplify()
        print('(', self.__num, '/', self.__deno, ')')

    # Can not you @setter because of declare __
    # Mind set: if you want it to private by declare __, you should not implement getter and setter
    def set_num(self, value):
        self.__num = value

    def set_deno(self, value):
        self.__deno = value

    def inverse(self):
        self.__deno, self.__num = self.__num, self.__deno

    def simplify(self):
        gcd = int(math.gcd(self.__num, self.__deno))
        self.__num = int(self.__num / gcd)
        self.__deno = int(self.__deno / gcd)

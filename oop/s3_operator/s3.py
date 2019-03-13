from fraction import Fraction


def main():
    f1 = Fraction(3, 6)
    f2 = Fraction(4, 12)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 / f2)
    print(f1 * f2)
    print(f1 < f2)
    print(f1 <= f2)
    print(f1 > f2)
    print(f1 >= f2)
    print(f1 == f2)
    print(f1 != f2)


if __name__ == '__main__':
    main()

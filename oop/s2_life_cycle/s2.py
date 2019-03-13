from fraction import Fraction
from incremental_array import IncrementalArray


def main():
    # f1 = Fraction(1, 2)
    # print(f1)
    # f2 = Fraction.from_string('4/12')
    # f2.simplify()
    # print(f2)

    # print("Number of fraction: {}".format(Fraction.num_fraction))

    print("Array a = ", end='')
    a = [5, -4, 1, -2, -1]
    iarr = IncrementalArray.create_incre_array_from(a)
    #iarr = IncrementalArray.create_incre_array_from([2, -4, -4, -3, -1, -5, -6, -3, -5])
    print(a)
    print("Incremental array from a: ", end='')
    print(iarr)
    print("Index from 1")
    print("Interval that sum equal zero: ", end='')
    print(iarr.interval_sum_zero())
    print("Interval that has max sum: ", end='')
    print(iarr.interval_sum_max())
    print("Longest interval that has positive sum: ", end='')
    print(iarr.longest_interval_sum_positive())


if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def main(args):
#a
    #i
    print(list([x**3 for x in range(1, 11) if (x**3) % 2 == 0]))
    #ii
    number = 123456
    print(list([x for x in range(2, number) if (number % x) == 0]))
    #iii
    print(list([x for x in range(10000, 10100) if all(x % y != 0 for y in range(2, x))]))

#b
    #i
    print(list(map(lambda x: x**3, filter(lambda w: (w**3) % 2 == 0, range(1, 11)))))
    #ii
    number = 123456
    print(list(map(lambda x: x, filter(lambda w: (number % w) == 0, range(2, number)))))
    #iii
    

    print(", ".join(args))


if __name__ == '__main__':
    main(sys.argv[1:])

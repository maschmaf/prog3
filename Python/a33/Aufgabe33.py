#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main(args):
#a
    #i
    print(list([x**3 for x in range(1,11) if (x**3)%2 == 0]))
    #ii
    zahl = 123456
    print(list([x for x in range(2,zahl) if (zahl%x) == 0]))
    #iii
    print(list([x for x in range(10000, 10100) if all(x%y != 0 for y in range(2,x))]))

#b
    #i
    print(", ".join(args))


if __name__ == '__main__':
    main(sys.argv[1:])

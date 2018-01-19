#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def main(args):
    text = "ijthxel, lgnajt lnth’p gkp!"
    b = dict(zip("irjmnzltacogdeksvbphxqyuwf ", "abcdefghijklmnopqrstuvwxyz "))
    print("".join(list([b.get(x) for x in text if x in b])))


    #print("".join(list([y for (x,y) in zip("irjmnzltacogdeksvbphxqyuwf ", "abcdefghijklmnopqrstuvwxyz ")  ])))

if __name__ == '__main__':
    main(sys.argv[1:])
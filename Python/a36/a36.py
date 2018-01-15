#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def noncomprehensiongehalt():
    liste = []
    for line in open("bonz.txt").readlines():
        line = line.split(";")
        if line[0].__eq__("Frau"):
            liste.append(int(line[3]))

    return (sum(liste))

def noncomprehensionwohnort():
    liste = []
    completedList = []
    for line in open("bonz.txt").readlines():
        line = line.split(";")
        if line[0].__eq__("Herr"):
            liste.append(line)

    liste.sort(key=lambda x: x[4])

    for ele in liste:
        completedList.append(ele[4])

    return(completedList)

def comprehensionWohnort():
    print(list([[x for x in line.split(";")] for line in open("bonz.txt")]))
    print("\n")
    print([[[y for y in l] for l in [l for l in line.split(";")]] for line in open("bonz.txt")])

def main(args):
    print(noncomprehensionwohnort())
    print(noncomprehensiongehalt())


if __name__ == '__main__':

    main(sys.argv[1:])

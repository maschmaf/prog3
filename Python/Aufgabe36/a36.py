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
    #print(list([[eintrag for eintrag in line.split(";")] for line in open("bonz.txt")()]))
    print(list(sorted([line.split(";")[-1].strip() for line in open("bonz.txt") if line.startswith("Herr")])))
    
def comprehensionGehalt():
    print(sum(list([int(line.split(";")[-2]) for line in open("bonz.txt") if line.startswith("Frau")])))
    
def meistesEinkommenJ():
    print("Bla")

def main(args):
    #print(noncomprehensionwohnort())
    #print(noncomprehensiongehalt())
    comprehensionWohnort()
    comprehensionGehalt()
    meistesEinkommenJ()
if __name__ == '__main__':
    main(sys.argv[1:])

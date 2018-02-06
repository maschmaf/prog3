'''
Created on 05.02.2018

@author: mschm001
'''
import re

class Spaltenfehler(Exception):
    pass

class Syntaxfehler(Exception):
    pass

pattern = re.compile("^\"[\d]+\",\"[A-Za-z]+\",\"[A-Za-z]+\"$")
    
def gleicheEintraege(spaltenname):
    index = 0
    dic = {}

    with open("bla", "r") as datei:
        ersteZeile = datei.readline().split(",")
        for ele in ersteZeile:
            if ele[1:-1] == spaltenname:
                print("Hure mit dem Index " + str(index))
                break
            else:
                index+=1
        
        lines = [line.strip().split(",") for line in datei]
        
        for ele in lines:
            if ele[index][1:-1] not in dic:
                dic[ele[index][1:-1]] = "UNIQUE"
            else:
                if dic[ele[index][1:-1]] == "UNIQUE":
                    dic[ele[index][1:-1]] = 2
                else:
                    dic[ele[index][1:-1]] += 1
    
    print(dic)
        

def auswerten():
    with open("bla","r") as datei:
        for line in datei:
            laenge = len(line.strip().split(","))
            if laenge is not 3:
                raise Spaltenfehler("falsche Anzahl an Spalten")
            match = pattern.match(line)
            if match == None :
                raise Syntaxfehler
            
        
def auswertenLine(line):
    laenge = len(line.strip().split(","))
    print(line)
    if laenge is not 3:
        raise Spaltenfehler("falsche Anzahl an Spalten")
    match = pattern.match(line)
    if match == None :
        raise Syntaxfehler

def auswertenIndex():
    zeile = 0
    spalte = 0
    with open("bla", "r") as datei:
        datei.readline()
        
        for line in datei:
            zeile +=1
            try:
                auswertenLine(line)
            except (Syntaxfehler, Spaltenfehler) as info:
                if type(info) is Syntaxfehler:
                    if(re.compile("^\"[\d]+$").match(line[0])) == None:
                        spalte = 0
                    if(re.compile("^\"[A-Za-z]+$").match(line[1])) == None:
                        spalte = 1
                    if(re.compile("^\"[A-Za-z]+$").match(line[2])) == None:
                        spalte = 2        
                        
                return "#Syntaxfehler: Zeile:" + str(zeile) + " Spalte:"+ str(spalte)
gleicheEintraege("Vorname")
print(auswertenIndex())



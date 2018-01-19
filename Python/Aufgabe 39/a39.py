'''
Created on 16.01.2018

@author: mschm001
'''
from macpath import split


class Messwerte():
    zeitpunkt = None
    temp = None
    
    def __init__(self, *value):
        if len(value) == 1:
            liste = value[0].split(",")
            self.zeitpunkt = liste[0][1:-1]
            self.temp = float(liste[1])
        else:
            self.zeitpunkt = value[0][1:-1]
            self.temp = float(value[1])
            
    def __repr__(self):
        return "Messwerte(\"'{0}'\", {1})".format(self.zeitpunkt, self.temp)
    
    def __eq__(self, other):
        return self.zeitpunkt == other.zeitpunkt and self.temp == other.temp
    
    def __lt__(self, other):
        return self.zeitpunkt < other.zeitpunkt
    
    def __gt__(self, other):
        return self.zeitpunkt > other.zeitpunkt
    
    
line = [line.strip() for line in open("messwerte.csv")][0:2]
mw = Messwerte(line[0])
mw2 = Messwerte(line[1])


print(mw.zeitpunkt)

liste = []
liste.append(mw)
liste.append(mw2)
print(liste)
print(sorted(liste,reverse=True))



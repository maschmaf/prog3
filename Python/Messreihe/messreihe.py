'''
Created on 06.02.2018

@author: mschm001
'''
import re

patternZeitpunkt = re.compile("^'[12][\d]{3}-((0[1-9])|(1[0-2]))-(([0-2][0-9])|(3[01]))\s(([01][0-9])|2[0-3])(:([0-5][0-9])){2}\.[0-9]'$")
patternTemp = re.compile('[0-9]{2]\.[0-9]')

class Messwert():
    
    def __init__(self, *value):
        if len(value) == 1:
            line = value[0].split(",")
            self.zeitpunkt = line[0][1:-1]
            self.temp = float(line[1])
        else:
            self.zeitpunkt = value[0]
            self.temp = float(value[1])
    
    def __repr__(self):
        return "Messwert('{}', {})".format(self.zeitpunkt, self.temp)
    
    def __eq__(self, other):
        return self.zeitpunkt == other.zeitpunkt and self.temp == other.temp
    
    def __lt__(self, other):
        if self.zeitpunkt == other.zeitpunkt:
            return self.temp < other.temp
        
        return self.zeitpunkt < other.zeitpunkt
    
    def __gt__(self, other):
        if self.zeitpunkt == other.zeitpunkt:
            return self.temp > other.temp
        
        return self.zeitpunkt > other.zeitpunkt
    
    def __hash__(self):
        return hash((self.zeitpunkt,self.temp))
    
class Messreihe():
    def __init__(self, file=None):
        self.werte = []
        if file is not None:
            with open(file) as datei:
                for line in datei:
                    self.werte.append(Messwert(line))
    
    def __len__(self):
        return len(self.werte)
    
    def add(self, *value):
        for wert in value:
            assert(isinstance(wert, Messwert))
            if isinstance(wert, Messwert):
                self.werte.append(wert)
                
    def __add__(self, other):
        assert(isinstance(self, Messreihe))
        assert(isinstance(other, Messreihe))
        mr = Messreihe()
        print(type(other), type(self))
        for ele in other.werte:
            mr.add(ele)
            
        for ele in self.werte:
            if ele not in mr.werte:
                mr.add(ele)
        return mr
    
    def addNew(self, mw):
        ele = sorted(self.werte, reverse = True)[0]
        if mw < ele:
            raise MonotonieVerstossError("SCHEISSEN EINGABE!" + ele.zeitpunkt + str(ele.temp))
        self.add(mw)
    
    def __iter__(self):
        self.pos = -1
        return self

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.werte):
            raise StopIteration
        return self.werte[self.pos]
    
    def __getitem__(self, n):
        if isinstance(n, int):
            return self.werte[n-1]
        elif isinstance(n, str):
            retListe = []
            for ele in self.werte:
                if n in ele.zeitpunkt:
                    retListe.append(ele)
                    
            return retListe
        elif isinstance(n, slice):
            return self.werte[n.start:n.stop:n.step]
        
    def enum(self):
        i = 0
        
        while True:
            if i >= len(self.werte):
                raise StopIteration
            yield i, self.werte[i]
            i+=1
            
        
class ReiheIter():
    def __init__(self, reihe):
        self.mr = reihe
        self.pos = -1
    
    def __iter__(self):
        return self
    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.mr):
            raise StopIteration
        return self.mr[self.pos]
    
class ErzeugeGenerator():
    def __init__(self, reihe):
        self.mr = reihe
    
    def gen(self):
        for ele in self.mr:
            yield ele
            
    def __iter__(self):
        return self.gen()
    
class MonotonieVerstossError(ValueError):
    pass
    
mw = Messwert("2017-01-10 17:17:17.0", 17.8)
mw2 = Messwert("'2017-01-10 17:17:17.1', 30.8")
mw3 = Messwert("'2018-01-10 17:17:17.1', 25.8")
mw4 = Messwert("'2018-01-10 17:17:17.0', 17.0")
mw5 = Messwert("2019-01-10 17:17:17.0", 17.8)
mw6 = Messwert("2009-01-10 17:17:17.0", 17.8)
mr1 = Messreihe()
mr1.add(mw, mw2)
mr2 = Messreihe()
mr2.add(mw3, mw4)
mr3 = mr1+mr2

print(len([ele for ele in mr3.werte]))

print(max(mr3.werte, key = lambda x : x.temp), min(mr3.werte, key = lambda x : x.temp))

print([wert.zeitpunkt for wert in[ele for ele in mr3.werte] if wert.temp > 33.0])

print(len([wert for wert in[ele for ele in mr3.werte] if wert.temp > 26.0]))

print(sorted([wert for wert in [ele for ele in mr3.werte] if int(wert.temp) == 17],reverse = True)[0])

print("HURE")
#reihe = ReiheIter(mr3)
#print(next(reihe),next(reihe),next(reihe),next(reihe))
#it = ErzeugeGenerator(mr3).__iter__()
#print(next(it))


#for nr, messwert in mr3.enum():
#    print(nr, "->", messwert)

try:
    mr3.addNew(mw5)
    mr3.addNew(mw6)
except (MonotonieVerstossError, ValueError, RuntimeError) as info:
    if isinstance(info, MonotonieVerstossError):
        print("SCHESSE MONOTON!")
    elif isinstance(info, ValueError):
        print("SCHEISSE VALUE!")
    else:
        print("SCHEISS LAUFZEIT")

print(mr3.werte)
    


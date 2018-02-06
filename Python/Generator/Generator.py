'''
Created on 06.02.2018

@author: mschm001
'''


def lucasfolge():
    zweiVorher = 2
    vorher = 1
    
    yield zweiVorher
    yield vorher
    
    aktuell = zweiVorher+vorher
    while True:
        yield aktuell
        aktuell, vorher , zweiVorher = aktuell + vorher, aktuell,vorher
        
def pellfolge():
    zweiVorher = 0
    vorher = 1
    
    yield zweiVorher
    yield vorher
    
    aktuell = 2*vorher + zweiVorher
    
    while True:
        yield aktuell
        aktuell, vorher, zweiVorher = 2*aktuell + vorher, aktuell, vorher
        

test = lucasfolge()
print(next(test),next(test),next(test),next(test),next(test),next(test),next(test),next(test))

test = pellfolge()
print(next(test),next(test),next(test),next(test),next(test),next(test),next(test),next(test))
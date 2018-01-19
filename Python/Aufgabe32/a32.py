'''
Created on 19.01.2018

@author: mschm001
'''

def auskunft(linie, start, ziel):
    verbindungen = sorted([line.strip().split(";") for line in open("zeiten.txt")])
    gefunden = False
    weg = []
    station = None
    naechsteStation = ""
    linienInformationen = [line for line in verbindungen if line[0] == linie]
    print(linienInformationen)
    
    zeit = 0
    
    while(gefunden is not True):    
        for ele in linienInformationen:
            if station is not None and station[1] == ziel:
                gefunden = True
                break
            
            if naechsteStation == "" and ele[1] == start:
                station = ele   #station auf startpunkt setzen
                zeit += int(ele[3])  #zeit addieren
                naechsteStation = ele[2]    #station auf nächste haltestelle
                weg.append(ele[1])
                break
            else:
                if naechsteStation != "" and ele[1] == naechsteStation:
                    if ele[1] != ziel:
                        zeit += int(ele[3])
                    station = ele
                    naechsteStation = ele[2]
                    weg.append(ele[1])
                    break
    
    print(zeit, weg)
    

auskunft("U4", "Kruppstrasse", "Seckbacher Landstrasse")
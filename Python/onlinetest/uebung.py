'''
Created on 05.02.2018

@author: mschm001
'''

liste = ([line.strip().split(";") for line in open("bestellungen")])

liste.sort(key = lambda x: (x[0], x[1]))

dic = {}
drinne = False

for ele in liste:
    if ele[0] not in dic:
        dic[ele[0]] = [(ele[1], int(ele[2]))]
    else:
        drinne = False
        for name, preis in dic[ele[0]]:     
            if name == ele[1]:
                drinne = True
                
        if not drinne:
            dic[ele[0]].append((ele[1], int(ele[2])))
        else:
            liste = [(tup[0],tup[1] + int(ele[2])) if tup[0] == ele[1] else (tup[0], tup[1]) for tup in dic[ele[0]]]
            dic[ele[0]] = liste
            

print(dic)

test = sorted(dic.items(), key = lambda x: x[0])
print(test)


[print(plz + ": "," ".join([(name + "("+ str(preis)+ ")") for name,preis in tup])) for plz, tup in test]

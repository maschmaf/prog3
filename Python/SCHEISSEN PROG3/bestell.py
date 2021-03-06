'''
Created on 06.02.2018

@author: mschm001
'''


def bestellungen(file):
    dic = {}
    index = 0
    eingefuegt = False
    with open(file) as datei:
        lines = [line.strip().split(";") for line in datei]
        lines.sort(key=lambda x: x[1])
        for ele in lines:
            eingefuegt = False
            if ele[0] not in dic:
                dic[ele[0]] = [(ele[1], int(ele[2]))]
            else:
                for name, preis in dic[ele[0]]:
                    if ele[1] in name:
                        dic[ele[0]][index] = (ele[1],int(ele[2]) + preis)
                        eingefuegt = True
                    index += 1
                    
                index = 0
                if eingefuegt is False:
                    dic[ele[0]].append((ele[1],int(ele[2])))
                    
                    
    return(dic)
                    
        
        

sortiert = sorted(bestellungen("bestellungen").items())
print(sortiert)

for ele in sortiert:
    print(str(ele[0]) + ":"+ "".join([" {}({})".format(name,preis) for name,preis in ele[1]]))





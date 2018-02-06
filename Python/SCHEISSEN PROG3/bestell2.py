'''
Created on 06.02.2018

@author: mschm001
'''


def bestellungen(file):
    dic = {}
    with open(file) as datei:
        lines = [line.strip().split(";") for line in datei]
        for ele in lines:
            if ele[0] not in dic:
                dic[ele[0]] = {str(ele[1]):int(ele[2])}
            else:
                if ele[1] not in dic[ele[0]]:
                    dic[ele[0]][ele[1]] = ele[2]
                else:
                    dic[ele[0]][ele[1]] = int(dic[ele[0]][ele[1]]) + int(ele[2])
    return dic
dic = bestellungen("bestellungen")
liste = sorted(dic.items())
for key, value in liste:
    print(key + ":" + "".join([" {}({})".format(k,v) for k,v in sorted(value.items())]))
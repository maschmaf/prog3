'''
Created on 06.02.2018

@author: mschm001
'''


def flatten(seq):
    liste = []
    if isinstance(seq, list):
        for ele in seq:
            if isinstance(ele, list) or isinstance(ele, tuple):
                tmp = (flatten(ele))
                for ele2 in tmp:
                    liste.append(ele2)
            else:
                liste.append(ele)
    if isinstance(seq, tuple):
        for ele in seq:
            if isinstance(ele, list) or isinstance(ele, tuple):
                tmp = (flatten(ele))
                for ele2 in tmp:
                    liste.append(ele2)
            else:
                liste.append(ele)
        
    return liste
    

def flat(seq,res):
    if type(seq) != type(tuple()) and type(seq) != type(list()):
        res.append(seq)
    else:
        for e in seq:
            res = flat(e, res)
    return res

def flattenAnders(seq):
    res = []
    return flat(seq,res)




seq = [1,2,3,(4,5),[6,(7,8),[9,10]]]

k = flattenAnders(seq)
print(k)
neu = flatten(seq)
print(neu)

seq[0] = 77
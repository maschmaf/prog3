def dreh(lst):
    "Dreht eine Liste rekursiv um"
    neu =  []
    if len(lst) > 1:
        merke = [lst[0]]
        neu += dreh(lst[1:]) + merke
    else:
        return lst
    return neu

print(dreh([1,2,3]))

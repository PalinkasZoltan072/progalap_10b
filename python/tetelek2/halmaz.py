# halmazkeszites tetel ( egyediek kivalogatasa)

def bennevan(lista:list, elem:int):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

def egyediek_kivalogatasa(lista:list):
    h = []
    for i in range(len(lista)):
        if not bennevan(h, lista[i]):
            h.append(lista[i])
    return h

lista=[7, 3, 1, 7, 2 ,3 ,3, 8, 5]
#halmaz=[7, 3, 2, 5, ]
halmaz = egyediek_kivalogatasa(lista)
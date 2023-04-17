# halmazkeszites tetel ( egyediek kivalogatasa)



def egyediek_kivalogatasa(lista:list):
    h = []
    for i in range(len(lista)):
        if lista[i] not in h:
            h.append(lista[i])
    return h

lista=[7, 3, 1, 7, 2 ,3 ,3, 8, 5]
#halmaz=[7, 3, 2, 5, ]
halmaz = egyediek_kivalogatasa(lista)
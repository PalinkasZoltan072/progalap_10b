def parosak_kivalogatasa(x):

    y =[]
    for i in range (len(x)):
        if x[i] % 2 == 0:
            y.append(x[i])
    return y 
 
def kiir(y):
    for i in range(len(y)):
        print(y[i], end=" ")

x = [7, 3, 4, 2, 1, 0, -8]

#kivalogatas
parosak=parosak_kivalogatasa(x)
kiir(parosak)
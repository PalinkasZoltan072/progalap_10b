from random import randint
from minimum_kivalasztas import rendezes_minimum
from buborekos import buborekos
from os import system
from time import time
#visszater egy "n" elemu listaval
#amiben [1, 20] intervallumbol vannak
#random szamok

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(1, 20)
        x.append(r)
    return x




def main():
    system("cls")
    x = feltolt(10)

    print("\nRendezes elott:")
    print(x)

    

    y = x.copy()
    start=time()
    rendezes_minimum(y)
    stop = time()
    print("\nMinimum-kivalasztasos")
    print(y)
    print("ido" ,round(stop - start, 20))

    y = x.copy()
    buborekos(y)
    print("\nBuborekos:")
    print(y)

    y = x.copy()
    y.sort()
    print("\nLista sort:")
    print(y)

main()
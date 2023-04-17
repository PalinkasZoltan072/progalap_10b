def beolvas(oldalak, szelessegek, szinek):
    fr = open("kerites.txt", "r")
    sor = fr.readline().split()
    while sor != " ":
        oldalak.append(int(sor[0]))
        szelessegek.append(int(sor[1]))
        szinek.append(sor[2])
        sor = fr.readline().split()

def fel2(oldalak):
    print("Az eladott telkek száma:", len(oldalak))

def fel3(oldalak, hszamok, paratlan, paros):
    parosok = 0
    paratlanok=-1
    for  i in range(len(oldalak)):
        if oldalak[i] == 0:
            parosok += 2
            hszamok.append(parosok)
            paros.append(i)
        else:
            paratlanok +=2
            hszamok.append(paratlanok)
            paratlan.append(i)
            
    print(parosok)
    print()
    print(paratlanok)




def main():
    oldalak = [] # 1 paratlan , 0 = pros
    szelessegek = []
    szinek = []
    hszamok= [] # hazszamok[i] : i-edik haz szama
    paratlan=[]
    paros=[]

    fel2(oldalak)
    fel3(oldalak, hszamok, paratlan, paros)
    beolvas(oldalak, szelessegek, szinek)
    

main()


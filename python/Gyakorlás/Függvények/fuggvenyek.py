def beolvas(szamok:list):
    fr = open("adatok.txt", "r")
    sor =fr.readline()
    
    while sor != "":
        szamok.append(int(sor.strip()))
        sor = fr.readline()
    fr.close()

    # while not szam % a == 0:
    # -1
    
    # a += -1
    # if szam % a == 0:
        #vizsgalo = false

def pozitiv_szamok(szamok:list):
    pozitivak_kivalogat=[]
    for i in range(len(szamok)):
        if 0 < szamok[i]:
            pozitivak_kivalogat.append(szamok[i])
    return pozitivak_kivalogat
    


def nagyobbak_szama(szamok:list, k: int):
    db= 0
    for i in range(len(szamok)):
        if k < szamok[i]:
            db += 1
    return db


def paratlan_e(szamok:list):
    paros = 0
    for i in range(len(szamok)):
        if szamok[i] % 2 == 0 :
            paros += 1
            
        



def main():
    nagyobb = []
    szamok = []
    pozitivak_kivalogat = []
    beolvas(szamok)
    print(szamok)
    pozitiv_szamok(szamok, pozitivak_kivalogat)
    print(pozitivak_kivalogat)
    nagyobbak_szama(szamok, nagyobb)
    print(nagyobb)
    paratlan_e(szamok)


main()


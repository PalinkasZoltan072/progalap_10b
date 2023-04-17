def beolvas(d, c, e, i, m):
    fr = open("lista.txt", "r")
    sor = fr.readline().strip()
    while sor != "":
        d.append(sor)
        sor = fr.readline().strip()
        c.append(sor)
        sor = fr.readline().strip()
        e.append(sor)
        sor = fr.readline().strip()
        i.append(int(sor))
        sor = fr.readline().strip()
        m.append(int(sor))
        sor = fr.readline().strip()
    fr.close()

def kiir(n):
    print("\n" + str(n) + ". feladat")

def feladat2(datumok):
    kiir(2)
    db = 0
    for i in range(len(datumok)):
        if datumok[i] != "NI":
            db += 1
    print("A listában " + str(db) + " db vetítési dátummal rendelkező epizód van.")
 
def feladat3(megneztek):
    kiir(3)
    db = 0
    mind = len(megneztek)
    for i in range(len(megneztek)):
        if megneztek[i] == 1:
            db += 1
    megszamolt = round(db/mind*100, 2)
    print("A listában lévő epizódok " + str(megszamolt) +"%-át látta.")
 



# def feladat5(datumok, megneztek, epizodok, cimek):
#     kiir(5)
#     date = input("Adjon meg egy dátumot! Dátum= ")
#     for i in range(len(datumok)):
#         if datumok[i] <= date and megneztek[i] == 0:
#             print(epizodok[i] + "\t" + cimek[i])


def hetnapja(ev, ho, nap):
    napok= ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok= [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    return napok[(ev + ev // 4 – ev // 100 + 
 ev // 400 + honapok[ho-1] + nap) mod 7]

def feladat7(datumok, cimek):
    print(7)
    hetnap=input("adja meg a hét napjat (pl:cs) nap= ")
    sorozatok = []
    for i in range(len[datumok]):
        if datumok[i] != "NI":
            darabok = datumok[i].split(".")
            ev = int(darabok[0])
            honap = int(darabok[1])
            nap = int(darabok[2])
            if hetnap(ev, honap, nap) == hetnap:
                sorozatok.append(cimek[i])
    for i in range(len(sorozatok)):
        print(sorozatok[i])
    if len(sorozatok) == 0:
        print("az adott napon nem kerul adasba sorozat.")

def feladat4(megneztek:list, idotartamok:list):
    perc = 0
    perc2 = 0
    ora = 0
    ora2 = 0
    nap = 0
    nap1= 1


    for i in range(len(megneztek)):
        if megneztek[i] == 1:
            perc += idotartamok[i]
    perc2 = abs(perc // 60*60-perc) # perc
    ora = perc // 60
    ora2= ora % 24
    nap = ora // 24

    print(perc2)
    print(ora2)
    print(nap)


def feladat8(cimek, idotartamok):
    fw = open("summa.txt, w")
    db = 1
    ido = idotartamok[0]
    for i in range(1, len(cimek)):
        if cimek[i] != cimek[i-1]:
            fw.write(cimek[i-1], + " " + str(ido) + " " str(db)+"\n")
            db = 1
            ido = idotartamok[i]
        else:
            db += 1
            ido += idotartamok[i]
    print(cimek[len(cimek)-1], ido, db)


        



def main():
    datumok = []
    cimek = []
    epizodok = []
    idotartamok = []
    megneztek = []
    beolvas(datumok, cimek, epizodok, idotartamok, megneztek)
    feladat2(datumok)
    feladat3(megneztek)
    feladat4(megneztek, idotartamok )
    print(hetnapja(2023, 3, 20))
    feladat7(datumok, cimek)
    feladat8(cimek, idotartamok)
    
    # feladat5(datumok, megneztek, epizodok, cimek)
    #print(cimek)

main()
from random import randint



def beolvas(k, v, p, t):
    fr = open("felszam.txt", "r")
    kerdes = fr.readline().strip() #readline szoveget ad vissza, trips is + leveszi a cuccokat (\n)
    while kerdes != "":
        k.append(kerdes)
        valasz = fr.readline().strip()
        valasz = valasz.split()
        v.append(int(valasz[0]))
        p.append(int(valasz[1]))
        t.append((valasz[2]))
        kerdes = fr.readline().strip()
    fr.close()

def feladat2(kerdesek):
    print("\n2. feladat")
    print("Az adatfájlban", len(kerdesek), "feladat van.")

def feladat3(pontok, temak):
    db = 0
    p1, p2, p3 = 0, 0, 0 #pi: i pontos feladatbol hany van
    print("\n3. feladat")
    for i in range(len(temak)):
        if temak[i] == "matematika":
            db += 1
            if pontok[i] == 1:
                p1 += 1
            elif pontok[i] == 2:
                p2 += 1
            else:
                p3 += 1
    print("Az adatfálban", db, "matematika feladat van, 1 pontot er ", p1,  "feladat, 2 pontot er", p2, "feladat, 3 pontot er", p3, "feladat")



def feladat4(valaszok):
    print("\n4. feladat")
    minert = valaszok[0]
    maxert = valaszok[0]
    for i in range(1, len(valaszok)):
        if valaszok[i] < minert:
            minert = valaszok[i]
        if valaszok[i] > maxert:
            maxert = valaszok[i]
    print("A feladatok valaszaink ", minert, "-tol ", maxert, "-ig terjed", sep="")



def feladat5(temak):
    print("\n5. feladat")
    tema = []
    for i in range(len(temak)):
        if temak[i] not in tema[i]:
            tema.append(temak[i])
            
    for i in range(len(tema)):
        print(tema[i])

def kivalogat(temak, tantargy):
    kivalogatottak = []
    for i in range(len(temak)):
        if temak[i] == tantargy:
            kivalogatottak.append(i)
    return kivalogatottak

def feladat6(kerdesek, valaszok, pontok, temak):
    print("\n5. feladat")
    tantargy = int("Milyen temakorbol szeretne kerdest kapni:")
    sorszamok=kivalogat(temak, tantargy)
    r = randint(0, len(sorszamok)-1)
    index = sorszamok[r]
    print(kerdesek[index])
    valasz= int(input())
    if valasz == valaszok[index]
    print("A valasz" + str((pontok[index])) + "pontot er")



def main():
    kerdesek=[]
    valaszok =[]
    pontok =[]
    temak=[]
    beolvas(kerdesek, valaszok, pontok, temak)
    feladat2(kerdesek)
    feladat3(pontok, temak)
    feladat4(valaszok)
    feladat5(temak)
    feladat6(kerdesek, valaszok, pontok, temak)
    


main()
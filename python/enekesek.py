
def kiir(ciganymeggy:list, db:list):
    fv= open("remek_nevek.txt", "w")
    for i in range(len(ciganymeggy)):
        fv.write(ciganymeggy[i] + ";" + str(db[i]) + "\n")
    fv.close()


def megszamol(ciganymeggy:list):
    e_darabok=[]
    for i in range(len(ciganymeggy)):
        darabszam= 0
        nev = ciganymeggy[i] #sesusak
        for j in range(len(nev)):
            if nev[j].lower() == "e":
                darabszam += 1
        e_darabok.append(darabszam)
    return e_darabok


def rendez(ciganymeggy:list):

    for i in range(len(ciganymeggy)-1, 0, -1):
        for j in range(i):
            e_egy = ciganymeggy[j].lower().find("e")
            e_ketto= ciganymeggy[j+1].lower().find("e")
            if e_egy > e_ketto : 
                ciganymeggy[j], ciganymeggy[j+1] = ciganymeggy[j+1], ciganymeggy[j]

def kivalogat(nevek:list, ciganymeggy:list):
    kicsi = "e"
    nagy = "E"

    for i in range(len(nevek)):

        if kicsi in nevek[i] or nagy in nevek[i]:
            ciganymeggy.append(nevek[i])




def beolvas(nevek, orszagok):
    fr = open("enekesek.txt", "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.split(" - ")
        nev = sor[0]
        orszag = sor[1].strip()
        nevek.append(nev)
        orszagok.append(orszag)
        sor = fr.readline()
    fr.close()

def javitas(nevek, orszagok):
    for i in range(len(nevek)):
        nevek[i]=nevek[i].replace("$", "s")
        nevek[i]=nevek[i].title() # susu kaba,  Susu Kaba
        orszagok[i]=orszagok[i].upper()
        orszagok[i]=orszagok[i].replace("EGYBESULT KARAJSAG", "EGYESULT KIRALYSAG")
        


def main():
    nevek, orszagok = [], []
    ciganymeggy=[]
    beolvas(nevek, orszagok)
    javitas(nevek, orszagok)
    #print(nevek, orszagok)
    kivalogat(nevek, ciganymeggy)
    #print(ciganymeggy)
    rendez(ciganymeggy)
    #print(ciganymeggy)
    db = megszamol(ciganymeggy)
    kiir(ciganymeggy, db)
main()
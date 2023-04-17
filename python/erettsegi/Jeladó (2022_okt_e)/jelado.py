
def feladat2(xs, ys):
    print("2. feladat")
    fel2 = int(input())
    print("x=" + str(xs[fel2-1]) + "y=" + str(ys[fel2-1]))





def beolvasas(orak, percek, mpercek, xs, ys):
    fr=open("jel.txt", "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.split
        orak.append(int(sor[0]))
        percek.append(int(sor[1]))
        mpercek.append(int(sor[2]))
        xs.append(int(sor[3]))
        ys.append(int(sor[4]))
        sor = fr.readline()

    fr.close        

def eltelt(o1, p1, mp1, o2, p2, mp2):
    ido1 = o1 * 3600 + p1 * 60 + mp1
    ido2 = o2 * 3600 + p2 * 60 + mp2
    return abs(ido1-ido2)

def f4(o, p, mp):
    print("4. Feladat")
    utolso = len(o) -1
    ido = eltelt(o[0], p[0], mp[0], o[utolso], p[utolso], mp[utolso])
    ora = ido // 3600
    ido = ido % 3600
    perc = ido // 60
    mperc =  ido % 60

def f7(orak, percek, mpercek, xs, ys ):
    for i in range(1, len(orak)):
        idoelteres = eltelt(orak[i-1], percek[i-1], mpercek[i-1], orak[i], percek[i])
        if idoelteres % 300 == 0:
            idodb= idoelteres // 300 -1
        else:
            idodb= idoelteres // 300
        if idodb >= 1:
            print(str(orak[i]) + " " + str(percek[i]) + " " + str(mpercek[i]) + "idoelteres" + str(idodb))

def main():
    orak, percek, mpercek, xs, ys = [], [], [], [], [],
    beolvasas(orak, percek, mpercek, xs, ys)
    feladat2(xs, ys)
    #print(eltelt(2, 15, 20, 3, 30, 15)) 
    f4(orak, percek, mpercek)   
    f7(orak, percek, mpercek)
main()
fuck you